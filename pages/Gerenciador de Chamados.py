import streamlit as st
import pandas as pd
import hmac

st.set_page_config(page_title='SUPORTE | GROFER', layout='wide', page_icon= 'images/icon.png')

col1, col2, col3 = st.columns(3)

col1.image('images/logo.png')
col1.title('Registro de Chamados')


#Login
def check_password():

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Usuário", key="username")
            st.text_input("Senha", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
        st.divider()

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(
                st.session_state["password"],
                st.secrets.passwords[st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            # Retrieve user category after successful login
            st.session_state["user_category"] = st.secrets["user_categories"].get(st.session_state["username"], "default")
            del st.session_state["password"]  # Don't store the username or password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True 

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("Usuário ou senha incorreta")
    return False


def check_user_access():
    """Check if the user has access to the current page based on their category"""
    user_category = st.session_state.get("user_category", "default")
    return True

if not check_password():
    st.stop()

# Assuming you have a way to determine the current page
# Replace 'current_page' with the identifier of the current page
if check_password:
    if not check_user_access():
        st.stop()

user_category = st.session_state.get("user_category", "default")


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