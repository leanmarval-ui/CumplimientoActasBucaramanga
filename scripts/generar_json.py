import pandas as pd

# Leer archivo generado por main.py
df = pd.read_excel("output/calendario_comparado.xlsx")

# =========================
# FILTRAR COLUMNAS
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

# =========================
# GUARDAR NUEVO EXCEL
# =========================
df_resumen.to_excel("output/resumen_filtrado.xlsx", index=False)

print("✅ Archivo resumen_filtrado.xlsx generado")
