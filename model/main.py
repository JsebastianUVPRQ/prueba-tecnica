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
st.title('Predicción de la variable Sale Price')

# subir archivo
uploaded_file = st.file_uploader("Suba un archivo csv", type=['csv'])

if uploaded_file is not None:
    try:
        # leer el archivo
        df = pd.read_csv(uploaded_file)
        # predecir
        print('Sale Price')
        numero = df.shape[0]
        y_pred = model.predict(df)
        # usar numeros naturales en el resultado y_pred
        y_pred = [int(i) for i in y_pred]
        # mostrar el resultado. numero | y_pred
        st.write(f'El número filas para predecir es: {numero}')
        st.write(y_pred)    
    
    except ValueError as e:
        st.error(f"Error reading JSON file: {e}")



