# Ejercicio 01

Calcular el coeficiente de correlación lineal entre los atributos “petallength” y “petalwidth”.

## Notas

El coeficiente de correlación lineal se calcula con el metodo `corr` del dataframe.

``` python
correlation = df['petallength'].corr(df['petalwidth'])
```