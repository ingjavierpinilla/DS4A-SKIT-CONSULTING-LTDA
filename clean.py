
# %% Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import warnings
import sklearn
import operator

sklearn.__version__
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)
warnings.filterwarnings("ignore")  # Suppress all warnings

# %% Load db 

df = pd.read_excel('Base_KIT_Comp.xlsx', index_col=None, sheet_name='ActividadesSKIT')  
df.rename(columns={'Versión': 'Version', 'Característica': 'Caracteristica'}, inplace=True)

#%% limpar na

for c in df.columns: 
  print (c,': ', df[c].isnull().sum())

df['Tarea'] = df['Tarea'].fillna('No informado')
# %% Load db 
"""
Graficas con las fechas de modificacion por cliente, proyecto y version;
Asi podemos limpiar los datos que nos comento Olga cuando decia que algunos proyectos
tenias entradas bastante tiempo despues que se terminaran 

"""
clientes = df.Cliente.unique()
for c in clientes:
    proyectos = df[df.Cliente == c].Proyecto.unique()
    for p in proyectos:
        versiones = df[(df.Cliente == c)&(df.Proyecto == p)].Version.unique()
        for v in versiones:
            aux = df[(df.Version == v)&(df.Proyecto == p)&(df.Cliente == c)]
            print('Actividades: ' + str(len(aux.Actividad.unique())))
            aux = aux[['Fecha']]
            t = 'Cliente: ' + c + ', Proyecto: ' + p + ', Version: ' + v
            #print(t)
            #aux.groupby([aux["Fecha"].dt.year, aux["Fecha"].dt.month]).count().plot(kind="bar", title  = t)
        break
    break

#%% one hot enconde para la columna actividad

print(len(df.Actividad.unique()))
aux = pd.get_dummies(df, columns=["Actividad"], prefix=["Actividad"])
#print(aux.head())