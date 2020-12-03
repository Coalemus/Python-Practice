import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from math import sqrt

df = pd.read_csv('regressionexample.csv', error_bad_lines=False)
print(df.shape)
df.describe()


target_column = ['unemploy']
predictors = list(set(list(df.columns))-set(target_column))
df[predictors] = df[predictors]/df[predictors].max()
df.describe()


X = df[predictors].values
Y = df[target_column].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size==0.30, random.state==40)
print(X_train.shape); print(X_test.shape)