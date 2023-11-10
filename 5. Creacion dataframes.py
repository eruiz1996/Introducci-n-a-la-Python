# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:00:19 2023

@author: eruiz
"""

import pandas as pd
import matplotlib.pyplot as plt

# diccionario
lenguajes = {
    'México':[100, 80, 100, 40, 68],
    'Argentina':[77, 98, 100, 50, 40],
    'Brasil':[100, 100, 100, 80, 40],
    'Ecuador':[19, 80, 60, 100, 50]
}

df = pd.DataFrame(lenguajes)
#%%
# agregando un índice
materias = ['Matemáticas', 'Español', 'Geografía',
            'Historia', 'Inglés']
df2 = pd.DataFrame(lenguajes,
                   index = materias)
#%%
df = df2.copy()
# filtrado de renglones
df.loc['Matemáticas']
# filtrado de varios renglones
df.loc[['Matemáticas', 'Historia']]
#%%
# filtrado de columnas
df.loc[:, 'México'] # uso de slicing
df.loc[['Inglés', 'Español'], ['Brasil', 'México']]
# nota que respeta el orden que le dimos
#%%
# filtrado por iloc
df.iloc[:2, 0] # primeros dos de la primer columna
df.iloc[-2:, 0] # últimos dos de la primer columna
# segundo y tercero de la tercer columna
df.iloc[1:3, 2]
#%%
# gráficos con pandas
plt.plot(df)
df.plot(kind = 'bar')









