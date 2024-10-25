import pandas as pd

#Data frame de ejemplo
data = {
    'Edad': [23, 25, 26, 24, 30, 24, 22, 28, 27, 24],
    'Salario': [48000, 52000, 58000, 49000, 60000, 48000, 50000, 62000, 59000, 54000]
}

df = pd.DataFrame(data)
print('Describe: ', df.describe())

#Calculando la media
media_edad = df['Edad'].mean()
media_salario = df['Salario'].mean()

#Calculando la mediana
mediana_edad = df['Edad'].median()
mediana_salario = df['Salario'].median()

#Calculando la moda
moda_edad = df['Edad'].mode()[0]
moda_salario = df['Salario'].mode()[0]

#medidas de dispersión
#Calculando el rango
rango_edad = df['Edad'].max() - df['Edad'].min()
rango_salario = df['Salario'].max() - df['Salario'].min()

#Calculando la varianza
varianza_edad = df['Edad'].var()
varianza_salario = df['Salario'].var()

#Calculando la desviación estándar
desviacion_edad = df['Edad'].std()
desviacion_salario = df['Salario'].std()

#medidas de posición
#Calculando los percentiles
percentil_25_edad = df['Edad'].quantile(0.25)
percentil_50_edad = df['Edad'].quantile(0.50)
percentil_75_edad = df['Edad'].quantile(0.75)

percentil_25_salario = df['Salario'].quantile(0.25)
percentil_50_salario = df['Salario'].quantile(0.50)
percentil_75_salario = df['Salario'].quantile(0.75)

#calculando cuartiles
cuartil_1_edad = percentil_25_edad
cuartil_2_edad = percentil_50_edad
cuartil_3_edad = percentil_75_edad

cuartil_1_salario = percentil_25_salario
cuartil_2_salario = percentil_50_salario
cuartil_3_salario = percentil_75_salario

#calculando los deciles
deciles_edad = df['Edad'].quantile([i/10 for i in range(1, 10)])
deciles_salario = df['Salario'].quantile([i/10 for i in range(1, 10)])

#mostrar resultados
print("Medidas de tendencia central")
print(f"Media de edad: {media_edad:0.3} Salario: {media_salario}")
print(f"Mediana de edad: {mediana_edad} Salario: {mediana_salario}")
print(f"Moda de edad: {moda_edad} Salario: {moda_salario}")
print()

print("Medidas de dispersión")
print(f"Rango de edad: {rango_edad} Salario: {rango_salario}")
print(f"Varianza de edad: {varianza_edad:0.3} Salario: {varianza_salario:0.3}")
print(f"Desviación estándar de edad: {desviacion_edad:0.3} Salario: {desviacion_salario:0.3}")
print()

print("Medidas de posición")
print(f"Percentil 25 de edad: {percentil_25_edad}, Percentil 50 de edad: {percentil_50_edad}, Percentil 75 de edad: {percentil_75_edad}")
print(f"Percentil 25 de salario: {percentil_25_salario}, Percentil 50 de salario: {percentil_50_salario}, Percentil 75 de salario: {percentil_75_salario}")
print()
print("Cuartiles - Edad : Q1", cuartil_1_edad, "Q2", cuartil_2_edad, "Q3", cuartil_3_edad)
print("Cuartiles - Salario : Q1", cuartil_1_salario, "Q2", cuartil_2_salario, "Q3", cuartil_3_salario)