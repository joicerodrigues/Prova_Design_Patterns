from jogos_cliente import jogos

partida1 = jogos()
print("Quantas seleções irá adicionar?")
n = int(input())
i=0

while i < n:
    print("Digite a posição do rank:")
    rank = input()
    print("Digite a seleção:")
    selecao = input()
    print("Digite os pontos:")
    pontos = input()
    print("Digite os jogadores:")
    jogadores = input()
    partida1.add_partida(rank, selecao, pontos, jogadores)
    i+=1
partida1.index.tabela_partida()