import pandas as pd

path = 'iris.csv'
df = pd.read_csv(path, sep=';', decimal=',')

correlation = df['petallength'].corr(df['petalwidth'])
print(f'\nCoeficiente de correlación lineal entre petallength y petalwidth: {correlation}\n')