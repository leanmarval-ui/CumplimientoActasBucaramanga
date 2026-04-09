import streamlit as st
import os

st.title("📊 Cumplimiento de Actas")

st.write("Haz clic para generar el gráfico")

if st.button("Generar gráfico"):
    st.write("Procesando información...")

    # Ejecuta tu script principal
    os.system("python scripts/main.py")

    # Muestra la imagen generada
    st.image("output/grafico.png")
