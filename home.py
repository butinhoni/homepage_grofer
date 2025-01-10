import streamlit as st
import webbrowser
st.set_page_config('Home | Grofer',layout='wide', page_icon= 'images/icon.png')

col1, col2, col3, col4 = st.columns(4)

col1.image('images/logo.png')
#col4.title('Grofer APP')

#st.title('Quem Somos')
st.title('Te ajudamos a otimizar seus processos de controle e obtenção de insighs com relatórios automatizados')
st.divider()

col1, col2, col3 = st.columns(3)

col1.title('Relatórios de BI')
col1.markdown('Te ajudamos a visualizar os resultados da sua empresa de maneira simples através de relatórios de bussiness inteligence')
col1.image(r'images/report.png', use_container_width = True)
col2.title('Sistemas')
col2.markdown('Oferecemos controles para os dados da sua empresa através de sistemas modernos e de fácil utilização')
col2.image(r'images/os.png')
col3.title('Automação de processos')
col3.markdown('Automatizamos as tarefas repetitivas para economizar tempo e mão de obra para sua empresa.')
col3.image(r'images/automation.png')
st.divider()


st.title('Fique a vontade para entrar em contato com um de nossos consultores.')
url = 'https://wa.link/lskqhf'
botao = st.button('Entrar em contato', type='primary', use_container_width= False)
if botao:
    webbrowser.open_new_tab(url)