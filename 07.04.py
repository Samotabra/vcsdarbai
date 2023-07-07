from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd


# iris = load_iris()
# X = iris.data
# y = iris.target
#
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
#
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
#
# prediction = model.predict(X_test)
# accuracy = accuracy_score(y_test, prediction)
# print("Tikslumas: ", accuracy)
# ...........................................

# data = pd.DataFrame({
#     'Atributas 1': [4,2,3,1,5],
#     'Atributas 2': [2,4,3,5,1],
#     'Klase': ['Suo', 'Kate', 'Kate', 'Ziurkenas', 'Ziurkenas']
# })
# X = data[['Atributas 1', 'Atributas 2']]
# y = data['Klase']
#
# model = DecisionTreeClassifier()
#
# model.fit(X, y)
#
# naujas_gyvunas = pd.DataFrame({
#     'Atributas 1': [3],
#     'Atributas 2': [4]
#  })
#
# predict = model.predict(naujas_gyvunas)
# print('Prognoze:', predict)