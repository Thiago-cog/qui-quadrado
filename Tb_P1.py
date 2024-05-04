import numpy as np
from scipy.stats import chi2_contingency

data = np.loadtxt('dados.csv', delimiter=',', skiprows=1, usecols=range(1, 5))

chi2, p, dof, expected = chi2_contingency(data)
print(f"qui-quadrado: {chi2}")
print(f"p-value: {p}")
print(f"Grau de liberdade: {dof}")
print(f"Valor esperado:\n {expected}")

