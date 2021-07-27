import numpy as np
import pandas as pd


clients = np.array([(1, 10000, 21, 2300, 0), (2, 18000, 32, 1780, 0), (3, 7500, 19, 5500, 1)])
# print(clients)

df = pd.DataFrame(clients)
# print(df)

previsores_x = df.iloc[:, 1:4].values
# print(previsores_x)
# print(type(previsores_x))

classe_y = df.iloc[:, 4].values
# print(classe_y)
# print(type(classe_y))
print(previsores_x[:,0].min(), previsores_x[:,1].min(), previsores_x[:,2].min())
print(previsores_x[:,0].max(), previsores_x[:,1].max(), previsores_x[:,2].max())

def ProjectInorganicMolecule():
    pass