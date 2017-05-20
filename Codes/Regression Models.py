# -*- coding: utf-8 -*-
"""
Created on Tue May 09 17:59:27 2017
References - http://machinelearningmastery.com/evaluate-performance-machine-learning-algorithms-python-using-resampling/
@author: Anish
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import TimeSeriesSplit
from sklearn import model_selection
from sklearn import linear_model

#Read from excel file
dfw = pd.read_csv('../Weather_ride_NJ.csv',index_col=0,header=0)
dfw

feature_cols = ['Weather Events']
#feature_cols = ['Date', 'android_ratings_2', 'android_ratings_4', 'android_ratings_5']
X = dfw[feature_cols]
Y = dfw['Number of Tweets']

X = pd.DataFrame(X)
Y = pd.DataFrame(Y)

test_size = 0.33
seed = 7
kfold = model_selection.ShuffleSplit(n_splits=10, test_size=test_size, random_state=seed)
model0 = LinearRegression()
model1 = linear_model.ElasticNet(alpha=2.0)
model2 = linear_model.Ridge(alpha=1.0)

results0 = model_selection.cross_val_score(model0, X, Y, cv=kfold)
results1 = model_selection.cross_val_score(model1, X, Y, cv=kfold)
results2 = model_selection.cross_val_score(model2, X, Y, cv=kfold)
#results = model_selection.cross_val_score(model0, X, Y, cv=TimeSeriesSplit(n_splits=2).split(tweet_number))
print("Accuracy: %.3f%% (%.3f%%)") % (results0.mean()*100.0, results0.std()*100.0)
print("Accuracy: %.3f%% (%.3f%%)") % (results1.mean()*100.0, results1.std()*100.0)
print("Accuracy: %.3f%% (%.3f%%)") % (results2.mean()*100.0, results2.std()*100.0)
#print results.mean()*100.0

'''Testing by 2/3rd, 1/3rd split
feature_cols = ['Temp','Weather Events']
#feature_cols = ['Date', 'android_ratings_2', 'android_ratings_4', 'android_ratings_5']
X = dfw[feature_cols]
Y = dfw['Number of Tweets']

X = pd.DataFrame(X)
Y = pd.DataFrame(Y)

X_train = X[:15]
Y_train = Y[:15]

X_test = X[15:]
Y_test = Y[15:]

ols = linear_model.Lasso(alpha=1.0)
model = ols.fit(X_train, Y_train)
print "Coef: ",model.coef_
print "R square: ",model.score(X_test, Y_test)

# Apply the model we created using the training data
# to the test data, and calculate the RSS.
print ((Y_test - model.predict(X_test))**2).sum()

#import numpy as np
# Calculate the MSE
np.mean((model.predict(X_test) - Y_test) **2) '''