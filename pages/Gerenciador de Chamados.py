import streamlit as st
import pandas as pd

st.set_page_config(page_title='SUPORTE | GROFER', layout='wide', page_icon= 'images/icon.png')

col1, col2, col3 = st.columns(3)

col1.image('images/logo.png')
col1.title('Registro de Chamados')

dict = {
    'Assunto':[
        'Problema de visualização',
        'Dados incorretos',
        'Tela não carrega'],
    'Usuario':[
        'Guilherme',
        'Fernando',
        'Rodolfo'],
    'Status':[
        'Resolvido',
        'Em Andamento',
        'Aguardando'
    ]
    }

df = pd.DataFrame(dict)

c1, c2, c3, c4 = st.columns(4)

filtros = c1.checkbox('Ativar Filtros')

if filtros:
    coluna = c2.selectbox('Filtrar por', df.columns)
    valor = c3.selectbox(coluna, df[coluna].unique())
    df = df[df[coluna] == valor]

st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.header('Assunto')
c2.header('Usuario')
c3.header('Status')

for i, row in df.iterrows():
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    c1.subheader(row['Assunto'])
    c2.subheader(row['Usuario'])
    c3.subheader(row['Status'])
    c4.button('Visualizar', key=f'botao{i}')