import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import streamlit as st
import numpy as np

conexao = sqlite3.connect('data.db', check_same_thread=False)
cursor = conexao.cursor()






def cadastrar_produto(marca, modelo , numeracao):
    
    dados = {'Marca': [marca] , 'Modelo': [modelo], 'Numeraçao': [numeracao]}
    novo_produto = pd.DataFrame(dados)
    produto_cadastrado = pd.read_csv('cadastro_produto.csv')
    novo_produto2 = pd.DataFrame(produto_cadastrado)
    produto = pd.concat([novo_produto , novo_produto2] , ignore_index=True)
    produto.to_csv('cadastro_produto.csv')

def finalizar_venda(data,codigo,produto,valor,cartao):
    
    dados = {'Data': [data] , 'Código':[codigo] , 'Produto': [produto] , 'Valor': [valor] , 'Cartão': [cartao]}
    vendas = pd.DataFrame(dados)
    vendas_cadastradas = pd.read_csv('vendas_final.csv')
    venda = pd.DataFrame(vendas_cadastradas)
    vendas_final = pd.concat([vendas , venda] , ignore_index=True)
    vendas_final.to_csv('vendas_final.csv')
    

def criar_tabela():
    cursor.execute('CREATE TABLE IF NOT EXISTS vendas(data DATE , codigo INTEGER, produto TEXT  , valor DECIMAL , cartao TEXT)')

def selecionar_tabela():
    cursor.execute('SELECT * FROM vendas')
    data = cursor.fetchall()
    return data


def salvar_venda(data,codigo, produto,valor,cartao):
        
    cursor.execute("""INSERT INTO vendas(data,codigo,produto,valor,cartao) VALUES (?,?,?,?,?)""" , (str(data), str(codigo),str(produto),str(valor),str(cartao)))
    conexao.commit()
  



