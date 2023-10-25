def calcular_dados(dados, valor): #funcao comeca aqui
    return dados.count(valor) #o metodo count vai contar quantas vezes o valor aparece na lista de dados

def calcular_pontuacao():
    # nessa funcao de calcular pontuacao o usuario podera inserir o valor dos 6 dados
    dado1 = int(input("Digite o dado 1: "))
    dado2 = int(input("Digite o dado 2: "))
    dado3 = int(input("Digite o dado 3: "))
    dado4 = int(input("Digite o dado 4: "))
    dado5 = int(input("Digite o dado 5: "))
    dado6 = int(input("Digite o dado 6: "))

    dados = [dado1, dado2, dado3, dado4, dado5, dado6] #aqui nessa lista os valores dos dados sao guardados 
    
    pontuacao = 0 #essa variavel ai facilitar na hora de calcular a pontuacao

    for numero in range(1, 7): #o for vai iterar os valores de 1 a 6 para fazer a verificacao
        quantidade = calcular_dados(dados, numero) #a funcao calcular daos vai verificar quantas vezes esse valor aparece na lista de dados la em cima

        #aqui acontece a verificacao das regras do jogo
        if quantidade == 1:
            if numero == 1:
                pontuacao += 100
            elif numero == 5:
                pontuacao += 50
        elif quantidade == 3:
            if numero == 1:
                pontuacao += 1000
            else:
                pontuacao += numero * 100
        elif quantidade >= 4:
            pontuacao += numero * 100 * (quantidade - 3)

    #nessa parte acontece a verificacao dos valores se estao dentro de 1 a 6. o 7 esta aí pq sabemos q a contagem acontece iniciando em 0 
    if set(dados) == set(range(1, 7)):
        pontuacao = 1200

    #aqui verifica se existem pares nos dados
    if len(set(dados)) == 3 and all(dados.count(valor) == 2 for valor in set(dados)):
        pontuacao = 800

    return pontuacao

#nessa parte a funcao de calcular a pontuacao é chamada para calcular os dados
pontuacao = calcular_pontuacao()
print("Pontuação:", pontuacao) #depois do valor ser armazenado dentro da variavel pontuacao, ela é printada na tela