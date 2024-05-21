import os
# usa streamlit para crear la interfaz web para el modelo 'model.pkl'
import streamlit as st
import pandas as pd

# Carga el modelo
model = pd.read_pickle('model.pkl')

# Crea la interfaz web
st.title('Modelo de Machine Learning')
st.write('Este es un modelo de Machine Learning que predice la clase de un objeto.')

# server
if __name__ == '__main__':
    st.write('Modelo cargado correctamente.')
    st.write('Puedes usar este modelo para predecir la clase de un objeto.')
    st.write('Para hacer una predicción, introduce los valores de las características del objeto en el formulario de abajo y haz clic en el botón "Predecir".')
    st.write('El modelo te dará la clase del objeto.')
    st.write('¡Buena suerte!')

    # Crea un formulario para introducir los valores de las características del objeto
    feature1 = st.number_input('Introduce el valor de la característica 1:', min_value=0, max_value=100, value=50)
    feature2 = st.number_input('Introduce el valor de la característica 2:', min_value=0, max_value=100, value=50)
    feature3 = st.number_input('Introduce el valor de la característica 3:', min_value=0, max_value=100, value=50)
    feature4 = st.number_input('Introduce el valor de la característica 4:', min_value=0, max_value=100, value=50)

    # Crea un botón para hacer la predicción
    if st.button('Predecir'):
        # Hace la predicción
        prediction = model.predict([[feature1, feature2, feature3, feature4]])
        st.write('La clase del objeto es:', prediction[0])
    
    st.write('¡Gracias por usar este modelo!')
    
    # Ejecuta la aplicación
    st.write('Para ejecutar la aplicación, ejecuta el siguiente comando en tu terminal:')
    st.write('streamlit run main.py')
    
    # Enlace a la documentación de Streamlit
    
