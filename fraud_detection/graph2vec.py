# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:10:43 2021

@author: lijinfe
"""

import os
os.chdir("C:\\Users\\lijinfe\\OneDrive - Manulife\\DataScientistCompetition\\GraphAnalysis -- 2021Winter")

import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
from sklearn.model_selection import train_test_split
import sklearn as skl
def split_test_dataset(dataset, index_var, target_var, size):
    X = dataset[index_var]
    y = dataset[target_var]
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=size, random_state=1)
    train = dataset[dataset[index_var].isin(X_train)]
    test = dataset[dataset[index_var].isin(X_test)]
    return train, test
def model_report(name, X, y, model, top):
    y_h = model.predict(xgb.DMatrix(X, label=y))
    
    threshold = np.quantile(y_h, q=1-top)
    print(name, " with threshold ", threshold)
    print("AUC =", np.round(skl.metrics.roc_auc_score(y, y_h), 4))
    
    y_h = np.where(y_h >= threshold, True, False)
    df = pd.DataFrame(y)
    df['y'] = y
    df['y_h'] = y_h
    print(np.round(100*pd.crosstab(df['y'], df['y_h'], normalize=True), 2))
    print(np.round(pd.crosstab(df['y'], df['y_h'], normalize=False), 2)) 
    print('Accuracy of XGBoost classifier on test set: {:.2f}'.format(accuracy_score(df['y'], df['y_h'])))
    
'''Load Data'''
train = pd.read_csv('reddit_train.csv', header=0)
test = pd.read_csv('reddit_test.csv', header=0)
df_simple_var = pd.read_csv('reddit_simple_var.csv', header=0) 
data_training, data_testing = split_test_dataset(train, 'id' , 'target', 0.3)

embedding_32 = pd.read_csv('reddit_embedding_32.csv', header=0)
embedding_32 = embedding_32.add_prefix('col_')
embedding_32 = embedding_32.rename(columns={"col_0": "id"})

with open('reddit_edges.json') as f:
  reddit_edges = json.load(f)
  
key_list = list(reddit_edges.keys())
val_list = list(reddit_edges.values())


#%% 
'''Fit Simple Model'''

data_training = data_training.merge(embedding_32, how = 'left', on = 'id')
data_testing = data_testing.merge(embedding_32, how = 'left', on = 'id')
data_scoring = test.merge(embedding_32, how = 'left', on = 'id')

X_train = data_training.drop(['id', 'target'], axis=1)
y_train = data_training['target']
X_test = data_testing.drop(['id', 'target'], axis=1)
y_test = data_testing['target']

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# Simple Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(accuracy_score(y_test, y_pred)))
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print(classification_report(y_test, y_pred))
print('AUC of logistic regression binary prediction on test set: {:.2f}'.format(roc_auc_score(y_test, logreg.predict(X_test))))
print('AUC of logistic regression prob prediction on test set: {:.2f}'.format(roc_auc_score(y_test, logreg.predict_proba(X_test)[:,1])))

# Random Forest
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import confusion_matrix
rfreg = RandomForestClassifier(n_estimators = 100, random_state = 0) 
rfreg.fit(X_train, y_train)   
y_pred = rfreg.predict(X_test)
print('Accuracy of Random Forest classifier on test set: {:.2f}'.format(accuracy_score(y_test, y_pred)))
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print(classification_report(y_test, y_pred))
print('AUC of Random Forest Classification prediction on test set: {:.2f}'.format(roc_auc_score(y_test, rfreg.predict(X_test))))

rfreg = RandomForestRegressor(n_estimators = 100, random_state = 0) 
rfreg.fit(X_train, y_train)   
y_pred = rfreg.predict(X_test)
print('AUC of Random Forest Regression prediction on test set: {:.2f}'.format(roc_auc_score(y_test, rfreg.predict_proba(X_test)[:,1])))


# XGBoost
import xgboost as xgb
param = {
    'tree_method': 'approx',
    'max_depth': 3,  # the maximum depth of each tree
    'eta': 0.3,  # the training step for each iteration
    'objective': 'binary:logistic',
    'eval_metric': 'mae',
    'scale_pos_weight': 200}  # error evaluation for regression

dtrain = xgb.DMatrix(X_train, label = y_train)
dtest = xgb.DMatrix(X_test, label = y_test)

xgb_model = xgb.train(param, dtrain, num_boost_round = 100)
model_report('model test performance', X_test, y_test, xgb_model, top=0.5) #AUC = 0.8554 with frac 0.01; 0.8557 with frac 0.1
from matplotlib import pyplot
xgb.plot_importance(xgb_model)
pyplot.rcParams['figure.figsize']=[5,5]
pyplot.show()

