import os
import sys
import connection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..classes.subgrupos import *

def cria_subgrupos(con, subgrupo):
    comando = ("INSERT INTO system_formula.subgrupos(nome, matricula_diretor)"
               "VALUE(\'{}\',\'{}\')".format(subgrupo.nome,subgrupo.matricula_diretor))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao criar o subgrupo: {}".format(e))
        saida = False
    return saida

def modifica_subgrupo(con, subgrupo):
    comando = ("UPDATE system_formula.subgrupos SET nome = \'{}\', matricula_diretor = \'{}\' WHERE id_subgrupo = \'{}\' ".format(subgrupo.nome,subgrupo.matricula_diretor,subgrupo.id_subgrupo))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao modificar o subgrupo: {}".format(e))
        saida = False
    return saida

def busca_subgrupo(con, id_subgrupo):
    comando = ("SELECT*FROM system_formula.subgrupos WHERE id_subgrupo = \'{}\'".format(id_subgrupo))
    try:
        con.cursor().execute(comando)
        linhas = con.cursor().fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(subgrupos(linha[0],linha[1],linha[2]))
    except connection.Error as e:
        print("erro ao buscar o subgrupo: {}".format(e))
        saida = False
    return saida

def busca_subgrupos(con):
    comando = ("SELECT*FROM system_formula.subgrupos")
    try:
        con.cursor().execute(comando)
        linhas = con.cursor().fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(subgrupos(linha[0],linha[1],linha[2]))
    except connection.Error as e:
        print("erro ao buscar o subgrupo: {}".format(e))
        saida = False
    return saida
