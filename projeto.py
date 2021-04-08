import streamlit as st
import pandas as pd
import funcoes
import sqlite3

conexao = sqlite3.connect('data.db' , check_same_thread=False)
cursor = conexao.cursor()





# Aqui vai ficar os Sidebar
st.sidebar.title('Menu')
# relatorio = st.sidebar.button('Relatórios')
# contas_pagar = st.sidebar.button('Contas a pagar')
# cadastro_produto = st.sidebar.button('Cadastro de produtos')
opcoes = st.sidebar.selectbox('Escolha uma opção' , ['Ponto de vendas' , 'Relatórios' , 'Cadastrar Produto'])

if opcoes == 'Cadastrar Produto':
    
    titulo = st.title('Cadastro de produtos')
    data = st.date_input(' ')
    marca = st.text_input('Digite a marca do produto')
    modelo = st.selectbox('Escolha o modelo' , ['Rasteirina' , 'Sandalia' , 'Tênis' , 'Bota' , 'Alpargata'])
    numeracao = st.selectbox('Menor numero' ,['34','35','36','37','38','39'])
    

    if st.button('Cadastrar produto'):
        funcoes.cadastrar_produto(marca , modelo, numeracao)
        st.success('Produto cadastrado corretamente')


if opcoes == 'Relatórios':
    titulo = st.title('Relátórios')
    data = st.date_input('')

    st.markdown('Base de dados de vendas anuais')
    vendas = pd.read_excel('Loja_2018.xlsx')
    st.dataframe(vendas)
    st.markdown('---')

    

if opcoes == 'Ponto de vendas':
    titulo = st.title('Ponto de vendas')
    data = st.date_input('')
    codigo , produto = st.beta_columns([1,3])
    codigo.text_input('Digite o código do produto')
    produto.text_input('Nome do produto')

    valor , cartao  = st.beta_columns([1,3])
    valor.text_input('R$')
    cartao.radio('Cartão', ('Crédito a vista' , 'Crédito parcelado' , 'Débito'))
    finalizar_venda , cancelar_venda = st.beta_columns(2)
    mostrar_dados = st.checkbox('Mostrar os dados')

    if mostrar_dados:
        resultado = funcoes.selecionar_tabela()
        limpar_db = pd.DataFrame(resultado , columns=['data' , 'codigo' , 'produto' , 'valor' , 'cartao'])
        st.dataframe(limpar_db)
    

    if finalizar_venda.button('Finalizar a venda'):
        # funcoes.finalizar_venda(codigo,produto,valor)
        funcoes.criar_tabela()
        funcoes.salvar_venda(data,codigo, produto,valor,cartao)
        
        st.success('Venda finalizada com sucesso!')
                

    if cancelar_venda.button('Cancelar a venda'):
        st.warning('Venda cancelada')

        
        
    
    
    

    
    