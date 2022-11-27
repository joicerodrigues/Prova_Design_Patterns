class Index():
    _tabela = {}
        
    def tabela_partida(cls):
        print("Ranking do jogos da copa ")
        print(" Posição no rank ---- Seleção ------- Pontos ----------------- Jogadores --------------")
        for key, value in sorted(cls._tabela.items()):
            print(f"|\t{key}\t|\t{value[0]}\t|\t{value[1]}\t|\t{value[2]}\t|")
        print()
    
    def add_partida(cls, posicao_rank, selecao, pontos, jogadores):
        cls._tabela[posicao_rank] = selecao, pontos, jogadores