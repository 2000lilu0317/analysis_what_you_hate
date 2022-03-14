import pickle
from train import WakatiMecab

class ScoreGenerator():
    def __init__(self, text):
        self.text = [text]
        self.paths = ['/code/model/tf_lgb_nega.pkl', 
                      '/code/model/tf_lgb_mount.pkl',
                      '/code/model/tf_lgb_ill.pkl']
        self.models = []
        for path in self.paths:
            model = pickle.load(open(path, 'rb'))
            self.models.append(model)

    #与えられたテキストをベクトル化する
    def text2vec(self, vectorizer_path='/code/model/vectorizer.pkl'):
        wakati_mecab = WakatiMecab()
        test_corpus = [wakati_mecab.wakati(s) for s in self.text]

        vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        text_vec = vectorizer.transform(test_corpus)

        return text_vec

    """
    モデルを読み込みスコアを返す関数
    """
    def calculate_score(self):
        text_vec = self.text2vec()

        labels = ['negative', 'mount', 'ill']
        score_each_label = {}
        for label, model in zip(labels, self.models):
            predict = model.predict(text_vec)
            
            #クラスの分布する確率とクラスの数字の内積で連続値のスコアを計算
            expected_score = sum([score * prob for score, prob in enumerate(predict[0])])
            score_each_label[label] = expected_score 
        
        return score_each_label
