import streamlit as st 
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Gráfico de industria automotriz')

# Botón para crear histograma
hist_button = st.button('Construcción de histograma')

if hist_button:
    """Si se presiona el botón se creará un histograma"""
    st.write('Creación de un histograma para el conjuinto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width = True)

# Botón para crear dispresión
scatt_button = st.button('Construcción de gráfico de dispersión')

if scatt_button:
    """Si se presiona el botón se crea gráfico de dispersión"""
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x='odometer', y ='price', title='Gráfico de dispersión odómetro vs precio')
    st.plotly_chart(fig, use_container_width = True)

# Casilla de verificción para crear histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Constuir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width = True)

# Casilla de verificación para crear un gráfico de dispersión
build_scatter = st.checkbox('Constuir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x='odometer', y ='price', title='Gráfico de dispersión odómetro vs precio')
    st.plotly_chart(fig, use_container_width = True)






