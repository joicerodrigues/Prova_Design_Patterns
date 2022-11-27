from index import Index
from partida_interface import partida_rank_interface

class jogos(partida_rank_interface):
    def __init__(self):
        self.index = Index()
    
    def add_partida(self, posicao_rank, selecao, pontos, jogadores):
        self.index.add_partida(posicao_rank, selecao, pontos, jogadores)