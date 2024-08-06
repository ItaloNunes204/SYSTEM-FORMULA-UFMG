import os
import sys
import connection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..classes.membros import *

def cria_membro(con, membro):
    comando = ("INSERT INTO system_formula.membros(nome, telefone, nascimento, cpf, rg, email, matricula, curso, periodo, id_subgrupo, telefone_emergencia, tipo, senha, statuss)"
               "VALUE(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format( membro.nome, membro.telefone, membro.nascimento, membro.cpf, membro.rg, membro.email, membro.matricula, membro.curso, membro.periodo, membro.id_subgrupo, membro.telefone_emergencia, membro.tipo, membro.senha, membro.statuss))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao criar o menbro: {}".format(e))
        saida = False
    return saida

def busca_membros(con,statuss):
    comando = ("SELECT*FROM system_formula.membros WHERE statuss = \'{}\'".format(statuss))
    try:
        con.cursor().execute(comando)
        linhas = con.cursor().fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(membros(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10],linha[11],linha[12],linha[13]))
    except connection.Error as e:
        print("erro ao buscar os membros: {}".format(e))
        saida = False
    return saida

def busca_membro(con, matricula):
    comando = ("SELECT*FROM system_formula.membros WHERE matricula = \'{}\'".format(matricula))
    try:
        con.cursor().execute(comando)
        linhas = con.cursor().fetchall()
        if len(linhas) == 0:
            saida = "sem registros"
        else:
            saida = []
            for linha in linhas:
                saida.append(membros(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10],linha[11],linha[12],linha[13]))
    except connection.Error as e:
        print("erro ao buscar o membro: {}".format(e))
        saida = False
    return saida

def login(con, matricula, senha, statuss):
    comando = ("SELECT*FROM system_formula.membros WHERE matricula = \'{}\' AND senha = \'{}\' AND statuss = \'{}\'".format(matricula, senha, statuss))
    try:
        con.cursor().execute(comando)
        linhas = con.cursor().fetchall()
        if len(linhas) == 0:
            saida = False
        else:
            saida = True
    except connection.Error as e:
        print("erro no login: {}".format(e))
        saida = "Erro"
    return saida

def modifica_membro(con, membro):
    comando = ("UPDATE system_formula.membros SET nome = \'{}\', telefone = \'{}\', nascimento = \'{}\', cpf = \'{}\', rg = \'{}\', email = \'{}\', curso = \'{}\', periodo = \'{}\', id_subgrupo = \'{}\', telefone_emergencia = \'{}\', tipo = \'{}\', senha = \'{}\', statuss = \'{}\' WHERE matricula = \'{}\' ".format(membro.nome, membro.telefone, membro.nascimento, membro.cpf, membro.rg, membro.email, membro.curso, membro.periodo, membro.id_subgrupo, membro.telefone_emergencia, membro.tipo, membro.senha, membro.statuss, membro.matricula))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao modificar o subgrupo: {}".format(e))
        saida = False
    return saida
