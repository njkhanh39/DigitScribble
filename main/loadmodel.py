import numpy as np
from sklearn import svm
from sklearn.decomposition import PCA
from joblib import load

#data 28 x 28 --> pca transform to 50 --> normalize / 255.0

class RBF_SVM: #use pca to reduce feature dimension from 28x28 --> 50
    def __init__(self, C = 5, gamma = 0.05):
        self.C = C
        self.gamma = gamma
        self.model = svm.SVC(C= self.C, gamma = self.gamma)


    #if we call load then no need for fitting
    def load(self, dir = 'main\input\pca_svm_pipeline.joblib'):
        pipeline = load(dir)
        self.pca = pipeline['pca']
        self.model = pipeline['svm']

    #X_train input 28 x 28
    def fit(self, X_train, Y_train):
        X_train_pca = self.pca.fit_transform(X_train)
        #normalize
        X_train_pca = X_train_pca / 255.0
        self.model.fit(X_train_pca, Y_train)
    
    #X_pred input = 28 x 28
    def predict(self, X_pred):
        X_pred_pca = self.pca.transform(X_pred)
        #normalize
        X_pred_pca = X_pred_pca / 255.0
        return self.model.predict(X_pred_pca)
    
