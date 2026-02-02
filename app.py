import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_env.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Criar scatter plot') # criar um botão
if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um scatter plot para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um scatter plot
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)        