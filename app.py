import pandas as pd
import plotly.express as px
import streamlit as st
     
df_carros = pd.read_csv('C:\\Users\\Veronica\\Downloads\\vehicles.csv.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_carros, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão') # criar outro botão

if scatter_button: # se o botão do gráfico de dispersão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(df_carros, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
