# função converter para arabico chmando a string romano
def converter_para_arabico(romano):
    converter_para_arabico = {  # aqui fiz uma especie de dicionario para definir oq cada letra representa
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    arabico = 0  # essa variavel est aqui pra facilitar o codigo

    # Itere pela string romana da direita para a esquerda
    valor_anterior = 0
    # aqui a string romano esta sendo iterada para verificar quando um simbolo é menor para fazer a subtração
    for letra in reversed(romano):
        valor = converter_para_arabico.get(letra, 0)

        # aqui da pra ver bem a subtracao acontecendo
        if valor < valor_anterior:
            arabico -= valor
        else:
            arabico += valor

        valor_anterior = valor

    return arabico


# aqui o usuario pode inserir o valor em numero romano para ver  conversao
numero_romano = input("Digite o número romano: ").upper()


# aqui a funcao de converter esta sendo chamada
resultado = converter_para_arabico(numero_romano)
# aqui o resultado ja convertido para arabico é exibido
print(f"O número arábico é: {resultado}")
