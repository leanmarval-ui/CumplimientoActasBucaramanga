import pandas as pd

# Leer archivo
df = pd.read_excel("output/calendario_comparado.xlsx")

# =========================
# SELECCIÓN DE COLUMNAS
# =========================

df_resumen = df[[
    "Sucursal",
    "Proyecto",

    "DiaIntermedia",
    "PosibleIntermedia",
    "RealIntermedia",
    "CoincidenciasIntermedia",
    "ConteoCoincidenciasIntermedia",
    "CumplimientoIntermedia",

    "DiaSemanal",
    "PosibleSemanal",
    "RealSemanal",
    "CoincidenciasSemanal",
    "ConteoCoincidenciasSemanal",
    "CumplimientoSemanal"
]]

print("Columnas filtradas:")
print(df_resumen.columns)

print("\nPrimeras filas:")
print(df_resumen.head())
