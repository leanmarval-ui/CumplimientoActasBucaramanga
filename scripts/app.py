import streamlit as st
from grafica import generar_grafico

st.title("📊 Cumplimiento de Actas")

st.write("Haz clic para generar el gráfico")

if st.button("Generar gráfico"):
    st.write("Procesando información...")
    
    # Aquí debes integrar tu lógica real
    generar_grafico(comparacion)
    
    st.image("output/grafico.png")
