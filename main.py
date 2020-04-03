import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_csv("data_set.csv", sep=",")
df = df.dropna(how='any',axis=0) 
df.overlooking = pd.Categorical(df.overlooking)
df.facing = pd.Categorical(df.facing)
df['overlooking_code'] = df.overlooking.cat.codes
df['facing_code'] = df.facing.cat.codes
del df['overlooking']
del df['facing']
df.to_csv("after_changes.csv", sep=',')
predict = "price"
X = np.array(df.drop([predict], 1))
y = np.array(df[predict])

best = 0
for _ in range(100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    if acc > best:
        best = acc
        with open("housing_prediction.pickle", "wb") as f:
            pickle.dump(linear, f)
print(best)

