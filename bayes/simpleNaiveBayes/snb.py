from sklearn.naive_bayes import BernoulliNB
from typing import Union

class sklearnBasis:

    def __init__(self, X_train: list[list[int]], Y_train: list[int], X_test : Union[list[int], bool] = False):
        "Initializes Bernoulli Naive Bayes and training first probe."

        # result
        self.__result = []

        # initialize
        self.__clf = BernoulliNB(alpha = 1, fit_prior=True)

        # first training
        self.retrain(X_train, Y_train)

        # if X-test given - return tested
        if X_test: self.__call__(X_test)


    def __call__(self, X_test : list[int]):
        "Returns prediction based on trained model."
        self.__prediction(X_test)
        return self.__result


    def retrain(self,  X_train: list[int], Y_train: list[int]):
        "Trains model again."
        self.__clf.fit(X_train, Y_train)


    def __prediction(self, X_test : list[int]):
        "Prediction based on trained model."
        self.__result = self.__clf.predict(X_test)
        #self.__result = self.__clf.predict_proba(X_test)


