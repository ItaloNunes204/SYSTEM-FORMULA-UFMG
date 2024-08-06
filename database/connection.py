import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
from mysql.connector import Error
from security.senhas import senha_banco



# conectando ao banco
def cria_connection():
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'system_formula', user='root', password = senha_banco)
        return con
        #cursor = con.cursor()
    except Error as erro:
        print("Erro ao se conectar ao banco de dados: {}".format(erro))
        return 'Erro'
