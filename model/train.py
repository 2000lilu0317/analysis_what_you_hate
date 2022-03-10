import gc
import os
import pickle
import random

import MeCab
import lightgbm as lgb
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

random.seed(42)

class WakatiMecab():
    def __init__(self):
        self.m = MeCab.Tagger ("-Ochasen")

    def __call__(self, text):
        wakati = [w.split("\t") for w in self.m.parse (text).split("\n")[:-2]]
        return wakati

    def wakati(self, text):
        wakati = self.__call__(text)
        wakati = [w[0] for w in wakati]
        return " ".join(wakati)

def make_models():
    df_tweet = pd.read_csv('data/mukatweet.tsv', sep ='\t')
    docs, nega_labels, mount_labels, ill_labels  = load_corpus(df_tweet)
    indices = list(range(len(docs)))
    random.shuffle(indices)

    train_data   = [docs[i] for i in indices[0:80]]
    train_nega_labels = [nega_labels[i] for i in indices[0:80]]
    train_mount_labels = [mount_labels[i] for i in indices[0:80]]
    train_ill_labels = [ill_labels[i] for i in indices[0:80]]
    valid_data    = [docs[i] for i in indices[80:]]
    valid_nega_labels  = [nega_labels[i] for i in indices[80:]]
    valid_mount_labels  = [mount_labels[i] for i in indices[80:]]
    valid_ill_labels  = [ill_labels[i] for i in indices[80:]]

    wakati_mecab = WakatiMecab()

    train_corpus = [wakati_mecab.wakati(s) for s in train_data]
    valid_corpus = [wakati_mecab.wakati(s) for s in valid_data]

    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(train_corpus)
    X_valid = vectorizer.transform(valid_corpus)
    pickle.dump(vectorizer, open('model/vectorizer.pkl', 'wb'))


    train_model(X_train, train_nega_labels, X_valid, valid_nega_labels, 'model/tf_lgb_nega.pkl')
    train_model(X_train, train_mount_labels, X_valid, valid_mount_labels, 'model/tf_lgb_mount.pkl')
    train_model(X_train, train_ill_labels, X_valid, valid_ill_labels, 'model/tf_lgb_ill.pkl')


def load_corpus(df):
    doc_lst = []
    nega_label_lst = []
    mount_label_lst = []
    ill_label_lst = []
    for i, row in df.iterrows():
        doc_lst.append(row.tweet)
        nega_label_lst.append(row.negative)
        mount_label_lst.append(row.mount)
        ill_label_lst.append(row.ill)
    return doc_lst, nega_label_lst, mount_label_lst, ill_label_lst


def train_model(train_data, train_labels, valid_data, valid_labels, model_name):
    if os.path.isfile(model_name):
        os.remove(model_name)
    train_set = lgb.Dataset(train_data, train_labels)
    valid_set = lgb.Dataset(valid_data, valid_labels)

    params = {
        "objective" : "multiclass",
        "metric" : "multi_logloss",
        "num_class" : 5,
        "learning_rate": 0.03
    }
    model = lgb.train(
        params = params,
        train_set = train_set,
        valid_sets = [train_set, valid_set],
        num_boost_round = 3000,
        early_stopping_rounds = 20,
        verbose_eval = 1,
    )
    y_test_pred = model.predict(valid_data, num_iteration=model.best_iteration)
    preds = y_test_pred.argmax(axis = 1)
    print(preds)
    pickle.dump(model, open(model_name, 'wb'))
    del model
    gc.collect()


if __name__ == '__main__':
    make_models()
