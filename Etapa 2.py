# ETAPA 1 - INICIANDO E CRIANDO MATRIZ

# Bibliotecas
import random

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

# Sorteando um país para a máquina
lista = []
for p in paises.keys():
    lista.append(p)
pais_comp = random.choice(lista)

# Criando a Matriz Inicial
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

'''
print(f'\n         COMPUTADOR - {pais_comp.upper()}')        # MATRIZ INICIAL PADRÃO
for linha_1 in matriz_comp:
    lista_linha = '  '.join(linha_1)
    print(lista_linha)
'''

#------------------------------------------------------------------

# ETAPA 2 - ALOCANDO OS NAVIOS DO COMPOTADOR

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

#print(f'\n         COMPUTADOR - {pais_comp.upper()}')
for linha_2 in mapa_novo_coputador:
    lista_linha2 = '  '.join(linha_2)
    #print(lista_linha2)


print('\nO Computador está pronto para começar!')
