## web app with streamlit
# we wanna build an inflation calculator
# the value of IPC changes every year

# the data are in COL_inflacion_anual_Dic.dat and USA_inflacion_anual_Dic.dat
# we have to read them and create a dictionary with the data

# we have to create a function that receives the year, the country (two options) and the amount of money
# USD and COP (colombian pesos)

# we have to return the value of the money up to date (2023)

import streamlit as st
import pandas as pd
import numpy as np
import os

# read the data
def read_data():
    # read the data
    COL = pd.read_csv('COL_inflacion_anual_Dic.dat', sep='\t')
    USA = pd.read_csv('USA_inflacion_anual_Dic.dat', sep='\t')
    return COL, USA

# create the dictionary
def create_dict(COL, USA):
    # create the dictionary
    COL_dict = dict(zip(COL['year'], COL['IPC']))
    USA_dict = dict(zip(USA['year'], USA['IPC']))
    return COL_dict, USA_dict

# calculate the value of the money today
def calculate_value(year, country, amount, COL_dict, USA_dict):
    # calculate the value of the money today
    if country == 'COL':
        while year < 2023:
            amount = amount * (1 + COL_dict[year])
            year += 1
    elif country == 'USA':
        while year < 2023:
            amount = amount * (1 + USA_dict[year])
            year += 1
    return amount

# main function
def main():
    # read the data
    COL, USA = read_data()
    # create the dictionary
    COL_dict, USA_dict = create_dict(COL, USA)
    # create the web app
    st.title('Inflation Calculator')
    year = st.number_input('Year', min_value=1900, max_value=2022, value=2022, step=1)
    country = st.selectbox('Country', ['COL', 'USA'])
    amount = st.number_input('Amount', min_value=0, value=1000, step=1)
    if st.button('Calculate'):
        value = calculate_value(year, country, amount, COL_dict, USA_dict)
        st.write(f'The value of {amount} in {year} is {value} in 2023')
    st.write('Created by: Juan Sebastian')

# run the main function
if __name__ == '__main__':
    main()