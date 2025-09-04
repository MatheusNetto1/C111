import pandas as pd

# data = {
#     "Categoria": ['A', 'A', 'B', 'B', 'C', 'A'],
#     "Valor": [10, 20, 30, 40, 50, 60]
# }
# 
# df = pd.DataFrame(data)
# 
# grupo = df.groupby('Categoria')
# grupo['Valor'].sum()
# 
# print(df.groupby('Categoria')['Valor'].agg((['sum', 'mean', 'max'])))

#  --------------------------------

dfPaises = pd.read_csv('groupby/paises.csv', sep=';')

# group_region = dfPaises.groupby('Region')

# print(group_region.count()['Country'])
# 
# print('\n')
# 
# print(group_region.sum()['Population'])
# 
# print('\n')
# 
# print(group_region.describe())
# 
# print('\n')

def tenpercent(x):
    return x*0.9

deathrate1 = dfPaises['Deathrate']

deathrate2 = dfPaises['Deathrate'].apply(tenpercent)

print(pd.concat([deathrate1, deathrate2], axis=1))