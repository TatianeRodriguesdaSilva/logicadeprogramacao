def calcular_pontuacao(dado1, dado2, dado3, dado4, dado5, dado6):
    dados = [dado1, dado2, dado3, dado4, dado5, dado6]
    pontos = 0
    
    # Verifica quantas vezes cada número aparece
    for numero in range(1, 7):
        quantidade = dados.count(numero)
        
        if quantidade >= 3:
            if numero == 1:
                pontos += 1000  # Regra 3: três números 1
            else:
                pontos += numero * 100  # Regras 4-8: três números 2-6
            quantidade -= 3
        
        # Verifica se ainda sobraram números 1 ou 5
        if numero == 1:
            pontos += quantidade * 100  # Regra 1: números 1
        elif numero == 5:
            pontos += quantidade * 50  # Regra 2: números 5
    
    # Verifica se existem quatro ou mais números iguais
    for numero in range(1, 7):
        quantidade = dados.count(numero)
        if quantidade >= 4:
            pontos += 2 * numero * 100  # Regra 9: quatro números iguais
        if quantidade >= 5:
            pontos += 4 * numero * 100  # Regra 10: cinco números iguais
        if quantidade == 6:
            pontos += 8 * numero * 100  # Regra 11: seis números iguais
    
    # Verifica sequência de 1 a 6
    if set(dados) == set(range(1, 7)):
        pontos = 1200  # Regra 13: sequência de 1 a 6
    
    return pontos

# Exemplo de uso:
dado1 = 1
dado2 = 2
dado3 = 3
dado4 = 4
dado5 = 5
dado6 = 6

pontuacao = calcular_pontuacao(dado1, dado2, dado3, dado4, dado5, dado6)
print("Pontuação:", pontuação)