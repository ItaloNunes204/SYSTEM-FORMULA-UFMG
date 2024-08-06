from datetime import date
class competicao:
    def __init__(self, id_competicao, dia, tipo, nome) -> None:
        self.id_competicao = id_competicao
        dia = str(dia).split('/')
        self.dia = date(int(dia[2]),int(dia[1]),int(dia[0]))
        self.tipo = tipo
        self.nome = nome

pw = competicao(111,'06/08/2024',2343,'isfjoifod')