#crea la app usando streamlit
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import joblib

# app que usa el modelo model.pkl, en la cual se sube un archivo prueba.json y se obtiene la predicción
# se debe retornar un json con la prediccion 

# Load the model
model = joblib.load('./model.pkl')


def main():
    st.title('Predicción de la variable objetivo')
    st.write('Este es un ejemplo de cómo usar un modelo de Machine Learning para predecir la variable objetivo de un conjunto de datos.')
    st.write('En este caso, se ha entrenado un modelo de regresión lineal con un conjunto de datos de ejemplo y se ha guardado el modelo en un archivo `model.pkl`.')
    st.write('A continuación, se muestra un formulario en el que puedes subir un archivo con los datos de prueba y obtener la predicción de la variable objetivo.')

    uploaded_file = st.file_uploader("Sube un archivo JSON con los datos de prueba", type=["json"])
    if uploaded_file is not None:
        data = json.load(uploaded_file)
        X = pd.DataFrame(data, index=[0])
        y_pred = model.predict(X)
        st.write('La predicción de la variable objetivo es:')
        st.write(y_pred[0])
        
        # Return the prediction as a JSON
        st.write('La predicción de la variable objetivo es:')
        st.json({'prediction': y_pred[0]})
        
if __name__ == '__main__':
    main()
    
#para correr la app se debe ejecutar el siguiente comando en la terminal
#streamlit run main.py

