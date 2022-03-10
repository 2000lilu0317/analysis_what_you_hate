import pickle

from train import WakatiMecab

if __name__ == '__main__':
    wakati_mecab = WakatiMecab()
    test_data = ['それってあなたの感想ですよね？']
    test_corpus = [wakati_mecab.wakati(s) for s in test_data]

    vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

    X_test = vectorizer.transform(test_corpus)

    model = pickle.load(open('model/tf_lgb_nega.pkl', 'rb'))

    print(model.predict(X_test))
