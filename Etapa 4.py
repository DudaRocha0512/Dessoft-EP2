# ETAPA 1 - INICIANDO E CRIANDO MATRIZ

# Bibliotecas
import random
import numpy as np

# Funções criadas
def cria_mapa(dimensao):    # Criação da Matriz
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

def aloca_navios(mapa,blocos):
    def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
        tamanho = len(mapa)
        if linha < 0 or coluna < 0 or linha >= tamanho:
            return False
        elif orientacao == 'v':
            if linha + blocos > tamanho:
                return False
            for i in range(linha,linha + blocos):
                if mapa[i][coluna] != ' ':
                    return False
        elif orientacao == 'h':
            if coluna + blocos > tamanho:
                return False
            for j in range(coluna,coluna + blocos):
                if mapa[linha][j] != ' ':
                    return False
        else:
            return False
        return True
    
    n_linha = len(mapa)
    n_coluna = len(mapa[0])
    c = 'N'
    for navio in blocos:
        linha_sort = random.randint(0,n_linha-1)
        coluna_sort = random.randint(0,n_coluna-1)
        orientacao = random.choice(['h','v'])
        while posicao_suporta(mapa,navio,linha_sort,coluna_sort,orientacao) == False:
            linha_sort = random.randint(0,n_linha-1)
            coluna_sort = random.randint(0,n_coluna-1)
            orientacao = random.choice(['h','v'])
        if orientacao == 'v':
            for i in range(linha_sort,linha_sort+navio):
                mapa[i][coluna_sort] = c
        elif orientacao == 'h':
            for j in range(coluna_sort,coluna_sort+navio):
                mapa[linha_sort][j] = c

    return mapa


# Listas dos Países
paises = {'Brasil': {'cruzador': 1,'torpedeiro': 2,'destroyer': 1,'couracado': 1,'porta-avioes': 1}, 
    'França': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Austrália': {'couracado': 1,'cruzador': 3, 'submarino': 1,'porta-avioes': 1, 'torpedeiro': 1},
    'Rússia': {'cruzador': 1,'porta-avioes': 1,'couracado': 2,'destroyer': 1,'submarino': 1},
    'Japão': {'torpedeiro': 2,'cruzador': 1,'destroyer': 2,'couracado': 1,'submarino': 1}}

# Iniciando o Jogo
nome = input('Qual seu nome?: ')
print(f'\nBem-vindo(a) à Batalha Naval, {nome}! Iniciando jogo...\n')
print('Países disponíveis e suas tropas:\n')

lista_p = ['Brasil', 'França', 'Austrália', 'Rússia', 'Japão']
for i in range(len(lista_p)):
    print(f'{i+1} - {lista_p[i]}')
    for nav in paises[lista_p[i]].keys():
        print(nav)
    print('\n')

# Sorteando um país para a máquina
lista = []
for p in paises.keys():
    lista.append(p)
pais_comp = random.choice(lista)

# Criando a Matriz Inicial
matriz_inicial = cria_mapa(12)
matriz_comp = cria_mapa(12)

ALFABETO = [' ','A','B','C','D','E','F','G','H','I','J',' ']   # Inserindo as letras nas colunas
i = 0
while i < len(matriz_comp[0]):
    for letra in ALFABETO:
        matriz_comp[0][i] = letra   
        matriz_comp[11][i] = letra 
        i += 1
    
NUMEROS = NUMEROS = [' ',1,2,3,4,5,6,7,8,9,10,' ']   # Inserindo os números nas linhasD
j = 0
while j < len(matriz_comp[0]):
    for numero in NUMEROS:

        if numero == 10:
            matriz_comp[j][0] = (f'{numero:01}')
            matriz_comp[j][11] = (f'{numero:01}')
        else:
            matriz_comp[j][0] = (f'{numero:02}')   
            matriz_comp[j][11] = (f'{numero:02}')
        j += 1

matriz_comp[0][0] = '  '
matriz_comp[0][11] = '  '
matriz_comp[11][0] = '  '
matriz_comp[11][11] = '  '

#------------------------------------------------------------------

# ETAPA 2 - ALOCANDO OS NAVIOS DO COMPUTADOR

# Escolhendo o local para tropas
print(f'\nO Computador está alocando os navios do país {pais_comp}...')

CONFIGURACAO = {'destroyer': 3,'porta-avioes': 5,'submarino': 2,'torpedeiro': 3,'cruzador': 2,'couracado': 4} # Quantidade de blocos por navio

tropa_comp = paises[pais_comp]  # Navios que fazem parte da tropa do país ecolhido
lista_alocacao_comp = []
for t in tropa_comp.keys():
    lista_alocacao_comp.append(t)

blocos = []       # Total de blocos utilizados
for l in lista_alocacao_comp:
    blocos.append(CONFIGURACAO[l])

mapa = matriz_comp

# Substituição aleatória dos espaços pelos navios
mapa_novo_coputador = aloca_navios(mapa,blocos)
#print(mapa_novo_coputador)

print(f'\n         COMPUTADOR - {pais_comp.upper()}')
for linha_2 in mapa_novo_coputador:
    lista_linha2 = '  '.join(linha_2)
    print(lista_linha2)


print('\nO Computador está pronto para começar!')

#------------------------------------------------------------------

# ETAPA 3 - ALOCANDO OS NAVIOS DO JOGADOR

# Alocando os navios do Jogador
print('\nAgora é sua vez!\n')


todos_paises = []
for a in paises.keys():
    todos_paises.append(a)

while True:
    pai = input('Escolha a nação para ser sua frota (digite o número correspondente): ')
    lista_n = ['1','2','3','4','5']
    if pai not in lista_n:
        print('Valor inválido! Escolha novamente')
    else:
        pais = int(pai)
        break

pais_jog = todos_paises[pais-1]
print(f'Nação escolhida: {pais_jog}!\n')   

i = 0
while i < len(matriz_inicial[0]):
    for letra in ALFABETO:
        matriz_inicial[0][i] = letra   
        matriz_inicial[11][i] = letra 
        i += 1
    
j = 0
while j < len(matriz_inicial[0]):
    for numero in NUMEROS:

        if numero == 10:
            matriz_inicial[j][0] = (f'{numero:01}')
            matriz_inicial[j][11] = (f'{numero:01}')
        else:
            matriz_inicial[j][0] = (f'{numero:02}')   
            matriz_inicial[j][11] = (f'{numero:02}')
        j += 1

matriz_inicial[0][0] = '  '
matriz_inicial[0][11] = '  '
matriz_inicial[11][0] = '  '
matriz_inicial[11][11] = '  '

print(f'\n             {nome.upper()} - {pais_jog.upper()}')
for linha_5 in matriz_inicial:
    lista_linha5 = '  '.join(linha_5)
    print(lista_linha5)

print(f'\nAloque os navios no mapa:')

tropa_jog = paises[pais_jog]  # Navios que fazem parte da tropa do país ecolhido
lista_alocacao_jog = []
for t in tropa_jog.keys():
    lista_alocacao_jog.append(t)

blocos_jog = []       # Total de blocos utilizados
for l in lista_alocacao_jog:
    blocos_jog.append(CONFIGURACAO[l])

matriz_jog = cria_mapa(12)

j = 0
while j < len(matriz_jog[0]):
    for numero in NUMEROS:

        if numero == 10:
            matriz_jog[j][0] = (f'{numero:01}')
            matriz_jog[j][11] = (f'{numero:01}')
        else:
            matriz_jog[j][0] = (f'{numero:02}')   
            matriz_jog[j][11] = (f'{numero:02}')
        j += 1
i = 0
while i < len(matriz_jog[0]):
    for letra in ALFABETO:
        matriz_jog[0][i] = letra   
        matriz_jog[11][i] = letra 
        i += 1

matriz_jog[0][0] = '  '
matriz_jog[0][11] = '  '
matriz_jog[11][0] = '  ' 
matriz_jog[11][11] = '  '

#print(matriz_jog)
mapa_jog = matriz_jog

def aloca_navios_jog(mapa,blocos_jog):
    def posicao_suporta(mapa,blocos_jog,linha,coluna,orientacao):
        tamanho = len(mapa)
        if linha < 0 or coluna < 0 or linha >= tamanho or coluna >= tamanho :
            return False
        elif orientacao == 'v':
            if linha + blocos_jog > tamanho:
                return False
            for i in range(linha,linha + blocos_jog):
                if mapa[i][coluna] != ' ':
                    return False
        elif orientacao == 'h':
            if coluna + blocos_jog > tamanho:
                return False
            for j in range(coluna,coluna + blocos_jog):
                if mapa[linha][j] != ' ':
                    return False
        else:
            return False
        return True
    
    n_linha = len(mapa)
    n_coluna = len(mapa[0])
    c = 'N'

    nav_tm = 0
    while True:
        for navio in blocos_jog:

            tm_jog = paises[pais_jog]
            lista_tm_jog = []
            for t in tm_jog.values():
                lista_tm_jog.append(t)
            
            nav = lista_alocacao_jog[nav_tm]
            tamanho_j = blocos_jog[nav_tm]
            print(f'\nNavio: {nav}. Tamanho: {tamanho_j}')


            while True:
                linha_so = input('\nEscolha a linha: ')     # Condições dadas pelo jogador
                lista_n = ['1','2','3','4','5','6','7','8','9','10']
                if linha_so not in lista_n:
                    print('Valor inválido! Escolha novamente')
                else:
                    linha_sort = int(linha_so)
                    break
            while True:
                coluna_s = input('Escolha a coluna: ')
                coluna_so = coluna_s.upper()
                if coluna_so not in ALFABETO:
                    print('Valor inválido! Escolha novamente')
                else:
                    h = 0
                    for i in ALFABETO:
                        if i == coluna_so:
                            coluna_sort = h
                        h += 1
                    break
            while True:
                orientacao = input('Escolha a orientação (v ou h): ')
                pos = ['v','h']
                #print(orientacao)
                if orientacao not in pos:
                    print('Valor inválido! Escolha novamente')
                else:
                    break
            
            lista_linha = np.arange(linha_sort,linha_sort + len(blocos_jog),1)
            #print(lista_linha)
            lista_coluna = np.arange(coluna_sort,coluna_sort + len(blocos_jog),1)
            #print(lista_coluna)

            alterou = 'não'
            if orientacao == 'v':    # Posicionamento
                j = tamanho_j
                g = 0
                lista_conf = []
                while j > 0:
                    lista_conf.append(mapa[linha_sort][coluna_sort+b])
                    if lista_conf.count(' ') != len(lista_conf): 
                        print('Não é possível alocar o navio nesse local! 5')
                        break
                    else:
                        a = tamanho_j
                        m = 0
                        #elif KeyError or TypeError or IndexError:
                        #   print('Não é possível alocar o navio nesse local! 2')
                        while a > 0:
                            mapa[linha_sort+g][coluna_sort] = c
                            m += 1
                            a -= 1
                    g += 1
                    j -= 1
                alterou = 'sim'

                
            elif orientacao == 'h':
                j = tamanho_j
                b = 0
                lista_conf = []
                while j > 0:
                    lista_conf.append(mapa[linha_sort][coluna_sort+b])
                    if lista_conf.count(' ') != len(lista_conf): 
                        print('Não é possível alocar o navio nesse local! 5')
                        break
                    #elif KeyError or TypeError or IndexError:
                      # print('Não é possível alocar o navio nesse local! 4')

                    else:

                        f = tamanho_j
                        v = 0
                        while f > 0:
                            mapa[linha_sort][coluna_sort+b] = c
                            v += 1
                            f -= 1
                    b += 1
                    j -= 1
                alterou = 'sim'


            if alterou == 'sim':
                print(f'\n             {nome.upper()} - {pais_jog.upper()}')
                for linha_j in matriz_jog:
                    lista_linhaj = '  '.join(linha_j)
                    print(lista_linhaj)
            nav_tm += 1 
        break
    return mapa

mapa_novo_jog = aloca_navios_jog(mapa_jog,blocos_jog)

print('\nTudo pronto para começar!')

'''
        alterou = 'não'
        if orientacao == 'v':    # Posicionamento
            for i in lista_linha:
                mapa[i][coluna_sort] = c
        
                alterou = 'sim'
                break
        elif orientacao == 'h':
            for j in lista_coluna:
                #print(linha_sort)
                mapa[linha_sort][j] = c
                alterou = 'sim'
                break
'''
