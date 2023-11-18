import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados
df_carros = pd.read_csv('vehicles.csv')

# Cabeçalho da aplicação
st.title('Análise de Anúncios de Vendas de Carros')

# Texto introdutório
st.header('Explorando Dados de Anúncios de Carros')
st.write('Este aplicativo permite explorar visualmente os dados de anúncios de vendas de carros.')

# Pergunta 1: Criar um histograma da quilometragem dos carros
st.header('Histograma da Quilometragem')
hist_button = st.button('Criar Histograma')

if hist_button:
    st.write('Visualizando a distribuição da quilometragem dos carros')
    fig_hist = px.histogram(df_carros, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Pergunta 2: Criar um gráfico de dispersão entre preço e ano de fabricação
st.header('Gráfico de Dispersão: Preço vs. Ano de Fabricação')
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button:
    st.write('Visualizando a relação entre preço e ano de fabricação dos carros')
    fig_scatter = px.scatter(df_carros, x='year', y='price', color='type')
    st.plotly_chart(fig_scatter, use_container_width=True)

# Caixa de seleção para visualizar carros de uma marca específica
st.header('Visualizar Carros por Marca')
selected_manufacturer = st.selectbox('Selecione uma Marca de Carro',
                                     df_carros['type'].unique())

if selected_manufacturer:
    st.write(f'Visualizando carros da marca {selected_manufacturer}')
    filtered_data = df_carros[df_carros['type'] == selected_manufacturer]
    fig_manufacturer = px.histogram(filtered_data, x='odometer', color='model')
    st.plotly_chart(fig_manufacturer, use_container_width=True)

     
