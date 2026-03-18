# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path = "estrellas.csv"
df_estrellas = pd.read_csv(path, sep=",")
print(df_estrellas.describe())

print("\n\n")
# Inciso 1
# Discretice por frecuencia el atributo Luminosidad en dos intervalos llamados Baja y Alta.
df_estrellas["Luminosidad_freq"], bins = pd.qcut(
    df_estrellas["Luminosidad"], q=2, labels=["Baja", "Alta"], retbins=True
)
print(df_estrellas["Luminosidad_freq"].value_counts())
print("Intervalos de corte:", bins)

min = df_estrellas["Luminosidad"].min()
Q2 = df_estrellas["Luminosidad"].quantile(0.5)
max = df_estrellas["Luminosidad"].max()

intervalo_bajo = (int(min), int(Q2))
intervalo_alto = (int(Q2), int(max))
print("Intervalos de frecuencia: ", intervalo_bajo, intervalo_alto)

print("\n\n")
# Inciso 2
# Discretice por rango el atributo Luminosidad en dos intervalos llamados Baja y Alta.
df_estrellas["Luminosidad_rango"], bins_rango = pd.cut(
    df_estrellas["Luminosidad"], bins=2, labels=["Baja", "Alta"], retbins=True
)
print(df_estrellas["Luminosidad_rango"].value_counts())
print("Intervalos de corte:", [int(b) for b in bins_rango])

print("\n\n")
# Inciso 3
# Calcule la correlación lineal entre los atributos Luminosidad y Temperatura.
corr = df_estrellas["Luminosidad"].corr(df_estrellas["Temperatura"])
print("El coeficiente de correlación lineal entre los atributos Luminosidad y Temperatura es: ", corr)

print("\n\n")
# Inciso 4
# Dibuje un Diagrama de Caja de Tukey de la variable Luminosidad e inclúyalo en la respuesta.
lum = df_estrellas["Luminosidad"]

Q1 = lum.quantile(0.25)
mediana = lum.quantile(0.5)
Q3 = lum.quantile(0.75)

RI = Q3 - Q1

lim_atipicos_leves_inf = Q1 - 1.5 * RI
lim_atipicos_leves_sup = Q3 + 1.5 * RI

lim_atipicos_ext_inf = Q1 - 3 * RI
lim_atipicos_ext_sup = Q3 + 3 * RI

outliers_leves = lum[(lum < lim_atipicos_leves_inf) | (lum > lim_atipicos_leves_sup)]
outliers_extremos = lum[(lum < lim_atipicos_ext_inf) | (lum > lim_atipicos_ext_sup)]

bigote_inferior = lum[lum >= lim_atipicos_leves_inf].min()
bigote_superior = lum[lum <= lim_atipicos_leves_sup].max()

print("Mediana:", mediana)
print("Q1:", Q1)
print("Q3:", Q3)
print("RI:", RI)

print("Bigote inferior:", bigote_inferior)
print("Bigote superior:", bigote_superior)

print("Intervalo atípicos leves:", lim_atipicos_leves_inf, lim_atipicos_leves_sup)
print("Intervalo atípicos extremos:", lim_atipicos_ext_inf, lim_atipicos_ext_sup)

print("Valores atípicos leves:", outliers_leves.values)
print("Valores atípicos extremos:", outliers_extremos.values)


sns.boxplot(x=df_estrellas["Luminosidad"])
plt.title("Diagrama de Caja de Tukey - Luminosidad", fontsize=14)
plt.xlabel("Luminosidad")
plt.grid(True)
plt.tight_layout()
plt.savefig("diagrama.png", dpi=300)

print(df_estrellas.head())
