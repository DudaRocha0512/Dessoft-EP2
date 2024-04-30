# Criação da Matriz
def cria_mapa(dimensao):
    matriz = []
    termo = ' '
    x = 0
    while x < dimensao:
        linha = []
        i = 0
        while i < dimensao:
            linha.append(termo)
            i += 1
        matriz.append(linha)
        x += 1
    return matriz
    

# Verificação de Finalização
def foi_derrotado(matriz):
    final = []
    for linha in matriz:
        for termo in linha:
            if termo == 'N':
                final.append('N')
    if 'N' in final:
        resposta = False
    else:
        resposta = True

    return resposta
