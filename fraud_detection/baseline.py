# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:14:48 2021

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
pd.set_option('display.max_columns', None)


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

with open('reddit_edges.json') as f:
  reddit_edges = json.load(f)
  
key_list = list(reddit_edges.keys())
val_list = list(reddit_edges.values())
#%%
'''Explore Data check Distribution and Frequency to see if Embedding can be used'''
# Get graph size distribution and plot it, from the result we can see most of graph have less than 25 pairs, so they are all small graph
list_size = [x.__len__() for x in val_list]
list_size = pd.DataFrame(list_size, columns = ['list_size'])
list_size.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Size Distribution')
plt.xlabel('graph size')

# Get pair frequency, from the result we can see a lot pairs are overlapping, so we can use embedding to train model    
pair_freq = pd.Series(val_list, name="count").explode().value_counts()
pair_freq = pair_freq.to_frame()
pair_freq['pair'] = pair_freq.index
pair_freq = pair_freq.sort_values(by=['pair'])

#pair_freq['count'].plot.hist(grid=True, bins=100, rwidth=0.9, color='#607c8e')
pair_freq[pair_freq['count']<1000]['count'].plot.hist(grid=True, bins=100, rwidth=0.9, color='#607c8e')
plt.title('Pair Frequency Distribution')
plt.xlabel('Pair Frequency')
plt.ylabel('Count')

# Plot the graph
sample_1 = data_training[data_training['count_user'] == 11][data_training['target'] == 1]['id'].values
sample_2 = data_training[data_training['count_user'] == 11][data_training['target'] == 0]['id'].values

plot_id = 9
import networkx as nx
from networkx.algorithms.dag import dag_longest_path
G = nx.Graph() 
G.add_edges_from(val_list[sample_1[plot_id]]) 
nx.draw_networkx(G, with_labels = True, node_color ='green') 

G = nx.Graph() 
G.add_edges_from(val_list[sample_2[plot_id]]) 
nx.draw_networkx(G, with_labels = True, node_color ='green') 




#%%
'''Generate Simple Variable to Fit Model, already generated, so pls dont run it if you have reddit_simple_var.csv in the folder'''
from itertools import chain
from collections import Counter

def counter_avg(df, var_list, i):
#    df['depth'][i] = len(dag_longest_path(nx.DiGraph(val_list[i])))
    df['max_centrality'][i] = max(nx.degree_centrality(nx.DiGraph(val_list[i])).values())
#    df['max2nd_centrality'][i] = len(dag_longest_path(nx.DiGraph(val_list[i])))
    sample_counter = Counter(chain.from_iterable(val_list[i]))
    df['avg_val'][i] = statistics.mean(sample_counter.values())
    df['max_val'][i] = max(sample_counter.values())
    df['count_user'][i] = len(sample_counter)
    df['pct_gt_2'][i] = sum(j > 2 for j in sample_counter.values())/len(sample_counter)
    df['pct_gt_3'][i] = sum(j > 3 for j in sample_counter.values())/len(sample_counter)
    df['pct_gt_4'][i] = sum(j > 4 for j in sample_counter.values())/len(sample_counter)
    df['n_gt_2'][i] = sum(j > 2 for j in sample_counter.values())
    df['n_gt_3'][i] = sum(j > 3 for j in sample_counter.values())
    df['n_gt_4'][i] = sum(j > 4 for j in sample_counter.values())
    
data_size = len(val_list)
#data_size = 10
df_simple_var = pd.DataFrame(index=range(data_size), columns=['avg_val','max_val', 'count_user', 'max_centrality',
                                                              'pct_gt_2', 'pct_gt_3', 'pct_gt_4',
                                                              'n_gt_2', 'n_gt_3', 'n_gt_4'])   
list(map(lambda i:counter_avg(df_simple_var, val_list, i), range(0, data_size)))
df_simple_var['id'] = df_simple_var.index
#df_simple_var.to_csv("reddit_simple_var.csv", index=False)

#%% 
'''Fit Simple Model'''
data_training = data_training.merge(df_simple_var, how = 'left', on = 'id')
data_testing = data_testing.merge(df_simple_var, how = 'left', on = 'id')
data_scoring = test.merge(df_simple_var, how = 'left', on = 'id')

col = ['avg_val','max_val', 'count_user', 'pct_gt_2', 'pct_gt_3', 'pct_gt_4', 'n_gt_2', 'n_gt_3', 'n_gt_4']
X_train = data_training[col]
y_train = data_training['target']
X_test = data_testing[col]
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


# K-FOLD CV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy import mean
from numpy import std
cv = KFold(n_splits=10, random_state=1, shuffle=True)
logreg = LogisticRegression()
scores = cross_val_score(logreg, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1)
print('Accuracy: %.3f (%.3f)' % (mean(scores), std(scores)))


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

#%% https://stellargraph.readthedocs.io/en/stable/demos/basics/loading-numpy.html
'''test stellar package'''
from stellargraph import StellarGraph
