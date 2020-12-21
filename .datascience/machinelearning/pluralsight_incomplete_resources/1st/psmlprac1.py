import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("diabetes.csv")
print(df.shape)
df.describe()

##TODO: make sense of this code below.
#y = df[diabetes].values
#x = df.drop('diabetes', axis=1).values

#X_train. X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)
#X_train.shape, X_test.shape
#((460,8), (308,8))

#logreg = LogisticRegression()
#logreg.fit(X_train, y_train)

#y_pred = logreg.predict(X_test)

#print(confusion_matrix(y_test, y_pred))
#print(classification_report(y_test, y_pred))

plt.show()