import pandas as pd

# Leer el archivo
df = pd.read_excel("output/calendario_comparado.xlsx")

print("Columnas del archivo:")
print(df.columns)

print("\nPrimeras filas:")
print(df.head())
