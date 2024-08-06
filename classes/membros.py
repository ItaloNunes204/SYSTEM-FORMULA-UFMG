from datetime import date
class membros:
    def __init__(self, nome, telefone, nascimento, cpf, rg, email, matricula, curso, periodo, id_subgrupo, telefone_emergencia, tipo, senha, statuss) -> None:
        self.nome = nome
        self.telefone = telefone
        nascimento = str(nascimento).split('/')
        self.nascimento = date(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo
        self.id_subgrupo = id_subgrupo
        self.telefone_emergencia = telefone_emergencia
        self.tipo = tipo
        self.senha = senha
        self.statuss = statuss

    def valida_cpf(self):
        cpf = str(self.cpf)
        cpf = list(cpf)
        if len(cpf) != 11:
            return False
        else:
            i = 0
            valida = 0 
            while i < 9:
                valida = valida + (int(cpf[i]) * (i + 1))
                i = i + 1
            resto = str(valida % 11)
            verificador = list(resto)
            if len(verificador) == 2:
                verificador = resto[1]
            else:
                verificador = resto[0]
            if verificador != cpf[9]:
                return False
            else:
                i = 0
                valida = 0 
                while i < 10:
                    valida = valida + (int(cpf[i]) * (i))
                    i = i + 1
                resto = str(valida % 11)
                verificador = list(resto)
                if len(verificador) == 2:
                    verificador = resto[1]
                else:
                    verificador = resto[0]
                if verificador != cpf[10]:
                    return False
                else:
                    return True
