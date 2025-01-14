import streamlit as st

st.set_page_config(page_title='SUPORTE | GROFER', layout='wide', page_icon= 'images/icon.png')

col1, col2, col3 = st.columns(3)

col1.image('images/logo.png')
col1.title('Suporte Grofer')

problemas = ['Problema de visualização',
             'Dados incorretos',
             'Tela não carrega']

st.selectbox('Selecione o tipo do problema', problemas)

st.text_area('Descreva o problema detalhadamente', height = 500)

c1, c2, c3 = st.columns(3)
c1.file_uploader('Anexe prints ou videos do problema acontecendo', type=['png','jpg','avi','mp4','wmv'])
st.divider()
st.button('Enviar', type='primary')
