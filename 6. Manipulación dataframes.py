# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:27:26 2023

Lectura y manipulación de bases de datos
@author: eruiz
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

#%%
# LECTURA DEL ARCHIVO
ruta = r'C:\Users\ed_22\Downloads'
nombre_archivo = 'SIO_junio.xlsx'
os.chdir(ruta)
df = pd.read_excel(nombre_archivo)
#%%
# leer los primeros renglones
df.head() # método
# leer los últimos renglones
df.tail()
# ver nombres de columnas
df.columns # atributo
# forma
df.shape
# siempre para un análisis exploratorio
df.info()
# estadísticos importantes
df.describe()
#%%
# cambiar nombre de columnas
df.columns = ['fecha', 'nombre', 'id', 'descripcion', 'operacion',
              'importe', 'desagregado']
print(df.head())
#%%
# PASE POR VALOR
# cambiar uno en específico
df.rename(columns = {'fecha':'corte'}) # pase por valor
df_aux = df.rename(columns = {'fecha':'corte'})
df = df.rename(columns = {'fecha':'corte'})
#%%
# SELECT
df = df[['corte', 'nombre', 'descripcion', 'operacion', 'importe']]
print(df.head(2))
#%%
# AGRUPACIONES
total_nombre = df.groupby('nombre').agg({'importe':'sum'})

#%%
# AGREGAR COLUMNAS
# (3).__add__(2)
total_nombre['%'] = total_nombre['importe']/total_nombre['importe'].sum() * 100
#%%
# ORDENAR
total_nombre = total_nombre.sort_values('importe', ascending = False)
#%%
top5 = total_nombre.head()
n = total_nombre.shape[0]
suma_resto = total_nombre['importe'].\
    tail(n-5).sum()
#%%
print(top5)
print(suma_resto)
# ¿tiene sentido todo esto?
#%%
# filtramos por nombre de aseguradora
aseguradora = 'Quálitas'
filtro_nombre = df['nombre'] == aseguradora # mask
qualitas = df[filtro_nombre]
# comprobamos que sólo sea Quálitas
qualitas['nombre'].unique() # set(qualitas['nombre'])
#%%
# agrupamos por operación
operacion_qualitas = qualitas.groupby('operacion').agg({'importe':'sum'})
operacion_qualitas.shape
operacion_qualitas.index
# convertir nuevamente a dataframe con índices normales
operacion_qualitas = operacion_qualitas.reset_index()
#%%
# métodos de str
operacion_qualitas['operacion'] = operacion_qualitas.operacion.\
    str.replace('?', 'ñ')
operacion_qualitas['operacion'] = operacion_qualitas.operacion.\
    str.replace('*', '')
    
#%%
plt.bar(df.operacion, df.importe)
plt.xlabel('Aseguradora')
plt.ylabel('Importe')
plt.title('Importe de Operaciones por Aseguradora')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas en el eje x para mayor legibilidad
plt.show()