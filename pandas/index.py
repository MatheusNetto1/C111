import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
dados = [10, 20, 30]

s = pd.Series(index=labels, data=dados)
print(s)
print(s['a'])

# ---------------------------

s1 = pd.Series({'a':10, 'b':20, 'c': 30})
s2 = pd.Series({'a':10, 'c':50, 'd': 80})
print(s1 + s2)
print(s1.add(s2, fill_value=0))

# ---------------------------

print(np.sum(s1))
print(s1[['a', 'c']])
print(s1[1:])

# --------------------------- DataFrames

np.random.seed(10)
df = pd.DataFrame(index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'],
                  data=np.random.randint(1, 50, [5, 4])
                  )
print(df)
print(df['W']['A'])

# --------------------------- loc e iloc

print(df.loc[['A', 'B'], ['X', 'Y', 'Z']])
print(df.iloc[0:2, 1:])

df = pd.read_csv('paises.csv', delimiter=';')

