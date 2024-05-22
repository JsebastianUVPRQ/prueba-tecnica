#crea la app usando streamlit
import streamlit as st
import pandas as pd
import pickle
import joblib

# app que usa el modelo model.pkl, en la cual se sube un archivo prueba.csv y se obtiene el resultado de la predicción
# de la variable target

# cargar el modelo
model = joblib.load('model.pkl')

# título de la app
st.title('Predicción de la variable target')

# subir archivo
uploaded_file = st.file_uploader("Subir archivo", type=['csv'])

if uploaded_file is not None:
    # leer el archivo
    df = pd.read_csv(uploaded_file)
    # predecir
    print('Sale Price')
    y_pred = model.predict(df)
    # mostrar el resultado
    st.write(y_pred)
    
    
    
