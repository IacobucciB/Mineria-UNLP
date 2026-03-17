import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path = "estrellas.csv"
df_estrellas = pd.read_csv(path, sep=";")
print(df_estrellas.describe())

# Inciso 1
# Discretice por frecuencia el atributo Velocidad en dos intervalos llamados Baja y Alta.
df_estrellas["Velocidad_freq"] = pd.qcut(
    df_estrellas["Velocidad"], q=2, labels=["Baja", "Alta"]
)
print(df_estrellas["Velocidad_freq"].value_counts())

# Inciso 2
# Discretice por rango el atributo Velocidad en dos intervalos llamados Baja y Alta.
df_estrellas["Velocidad_rango"] = pd.cut(
    df_estrellas["Velocidad"], bins=[-np.inf, 100, np.inf], labels=["Baja", "Alta"]
)
print(df_estrellas["Velocidad_rango"].value_counts())

# Inciso 3
# Calcule la correlación lineal entre los atributos Velocidad y Temperatura.
corr = df_estrellas["Velocidad"].corr(df_estrellas["Temperatura"])
print(corr)

# Inciso 4
# Dibuje un Diagrama de Caja de Tukey de la variable Velocidad e inclúyalo en la respuesta.
vel = df_estrellas["Velocidad"]

Q1 = vel.quantile(0.25)
mediana = vel.quantile(0.5)
Q3 = vel.quantile(0.75)

RI = Q3 - Q1

lim_atipicos_leves_inf = Q1 - 1.5 * RI
lim_atipicos_leves_sup = Q3 + 1.5 * RI

lim_atipicos_ext_inf = Q1 - 3 * RI
lim_atipicos_ext_sup = Q3 + 3 * RI

outliers_leves = vel[(vel < lim_atipicos_leves_inf) | (vel > lim_atipicos_leves_sup)]
outliers_extremos = vel[(vel < lim_atipicos_ext_inf) | (vel > lim_atipicos_ext_sup)]

bigote_inferior = vel[vel >= lim_atipicos_leves_inf].min()
bigote_superior = vel[vel <= lim_atipicos_leves_sup].max()

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


sns.boxplot(x=df_estrellas["Velocidad"])
plt.title("Diagrama de Caja de Tukey - Velocidad", fontsize=14)
plt.xlabel("Velocidad")
plt.grid(True)
plt.tight_layout()
plt.savefig("diagrama.png", dpi=300)

print(df_estrellas.head())
