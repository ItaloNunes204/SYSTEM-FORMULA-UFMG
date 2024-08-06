from datetime import datetime
class presenca:
    def __init__(self, id_presenca, entrada, saida, matricula_membro) -> None:
        self.id_presenca = id_presenca
        self.entrada = entrada
        self.saida = saida
        self.matricula_membro = matricula_membro