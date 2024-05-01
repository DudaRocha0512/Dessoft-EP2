import random
def mostrarMapa(mat1, mat2):
    print('   A  B  C  D  E  F  G  H  I  J    A  B  C  D  E  F  G  H  I  J')
    for linha in range(10):
        print(f'{linha+1:2d}', end='')
        for coluna in range(10):
            print(f' {mat1[linha][coluna]} ', end='')
        print(f'    {linha+1:2d}', end='')
        for coluna in range(10):
            print(f' {mat2[linha][coluna]} ', end='')
        print()

def posicao_suporta(mapa, n_blocos, linha, coluna, orientacao):
    tamanho_mapa = len(mapa)
    if linha < 0 or coluna < 0 or linha >= tamanho_mapa or coluna >= tamanho_mapa:
        return False
    if orientacao == 'v':
        if linha + n_blocos > tamanho_mapa:
            return False
        for i in range(linha, linha + n_blocos):
            if mapa[i][coluna] != ' ':
                return False
    elif orientacao == 'h':
        if coluna + n_blocos > tamanho_mapa:
            return False
        for k in range(coluna, coluna + n_blocos):
            if mapa[linha][k] != ' ':
                return False
    else:
        return False
    return True

def aloca_navios(mapa_alocacao, n_blocos):
    n_linha = len(mapa_alocacao)
    n_coluna = len(mapa_alocacao[0])
    print(n_linha, n_coluna)
    caractere_navio = 'N'
    for navio in n_blocos:
        linha_sort = random.randint(0, n_linha-1)
        coluna_sort = random.randint(0, n_coluna-1)
        orientacao = random.choice(['h', 'v'])
        while posicao_suporta(mapa_alocacao, navio, linha_sort, coluna_sort, orientacao) == False: #vai fazer caber de qualquer forma
            linha_sort = random.randint(0, n_linha-1)
            coluna_sort = random.randint(0, n_coluna-1)
            orientacao = random.choice(['h', 'v'])
        if posicao_suporta(mapa_alocacao, navio, linha_sort, coluna_sort, orientacao):
            if orientacao == "v":
                for i in range(linha_sort, linha_sort + navio):
                    mapa_alocacao[i][coluna_sort] = caractere_navio
            elif orientacao == "h":
                for j in range(coluna_sort, coluna_sort + navio):
                    mapa_alocacao[linha_sort][j] = caractere_navio
                
    return mapa_alocacao