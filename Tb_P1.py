import numpy as np
from scipy.stats import chi2_contingency

data = np.loadtxt('dados.csv', delimiter=',', skiprows=1, usecols=range(1, 5))

# data = np.array([[156,14,2,4],[124,20,5,4],[77, 11, 7, 13],[82, 36, 15, 7],[53, 11, 1, 57],[32, 24, 4, 53],[33, 23, 9, 55],[12, 46, 23, 15],[10, 51, 75, 3],[13, 13, 21, 66],[8, 1, 53, 77],[0, 3, 160, 2],[0, 1, 6, 153]])

chi2, p, dof, expected = chi2_contingency(data)
print(f"qui-quadrado: {chi2}")
print(f"p-value: {p}")
print(f"Grau de liberdade: {dof}")
print(f"Valor esperado:\n {expected}")

