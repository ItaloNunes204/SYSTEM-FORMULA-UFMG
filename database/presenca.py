import os
import sys
import connection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..classes.presenca import *

def cria_presenca(con, presenca):
    comando = ("INSERT INTO system_formula.presenca(entrada, saida, matricula_membro)"
               "VALUE(\'{}\',\'{}\',\'{}\')".format(presenca.entrada, presenca.saida, presenca.matricula_membro))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao criar a presença: {}".format(e))
        saida = False
    return saida

def modifica_presenca(con, presenca):
    comando = ("UPDATE system_formula.presenca SET entrada = \'{}\', saida = \'{}\', matricula_membro = \'{}\' WHERE id_presenca = \'{}\' ".format(presenca.entrada, presenca.saida, presenca.matricula_membro, presenca.id_presenca))
    try:
        con.cursor().execute(comando)
        con.commit()
        saida = True
    except connection.Error as e:
        print("erro ao modificar a presença: {}".format(e))
        saida = False
    return saida
