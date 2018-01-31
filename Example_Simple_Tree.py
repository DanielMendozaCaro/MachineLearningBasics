# Ejemplo simple de arbol de decision
# Daniel Mendoza
# 30/01/2018

from sklearn import tree

'''
    Variables basicas - String
    features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
    labels = ["apple", "apple", "orange", "orange"]
'''

# Variables
features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # 1 - smooth  // 0 - bumpy
labels = [1, 1, 0, 0]  # 1 - apple // 0 - orange

# Crear clasificador // arbol de decisión
clf = tree.DecisionTreeClassifier()

# Entrenar algoritmo
clf = clf.fit(features, labels)

# Consultar datos
weight = input(print("Ingrese el peso de la fruta: "))
texture = input(print("Ingrese la textura de la fruta: "))

# Predecimos
if clf.predict([[weight, texture]]) != 1:
    print("Es una naranja")
else:
    print("Es una manzana")





