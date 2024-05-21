import streamlit as st
import pandas as pd
import joblib
import json

# Cargar el modelo
model = joblib.load('model.pkl')

# Título y descripción
st.title('Aplicación de Predicción')
st.markdown("""
Esta aplicación utiliza un modelo de machine learning para hacer predicciones a partir de un archivo JSON.
""")

# Cargar archivo JSON
st.sidebar.header('Cargar archivo JSON')
uploaded_file = st.sidebar.file_uploader("Sube tu archivo JSON", type="json")

if uploaded_file:
    # Leer archivo JSON
    data = json.load(uploaded_file)
    
    # Convertir JSON a DataFrame
    df = pd.json_normalize(data)
    
    # Mostrar datos cargados
    st.subheader('Datos cargados')
    st.write(df)
    
    # Realizar predicciones
    if st.button('Realizar predicción'):
        predictions = model.predict(df)
        
        # Mostrar predicciones
        st.subheader('Predicciones')
        st.write(predictions)

# Mejoras en la interfaz gráfica
st.markdown("""
<style>
    .main {
        background-color: #f0f0f5;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)