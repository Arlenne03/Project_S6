import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis de datos de vehículos") # agregamos encabezado

hist_button = st.button('Visualizar histograma del kilometraje') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma del kilometraje para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=['indianred'])
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    
hist_button = st.button('Visualizar mapa de calor del kilometraje y los cilindros de los coches') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un mapa de calor de densidad del kilometraje y los cilindros de los coches')
            
    # crear un histograma
    fig = px.density_heatmap(car_data, x="odometer", y="cylinders")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

build_scatter = st.checkbox('Visualizar diagrama de caja de los cilindros') # crear un botón

if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Boxplot de los cilindros de los vehículos en venta')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

build_scatter = st.checkbox('Visualizar un scatterplot del kilometraje y los precios') # crear un botón
  
if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Diagrama del kilometraje y los precios de los coches')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Visualizar histograma de las condiciones de los coches') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma de las condiciones de los vehículos en venta')
            
    # crear un histograma
    fig = px.histogram(car_data, x="condition", color_discrete_sequence=['royalblue'])
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
