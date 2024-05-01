# Bibliotecas
import random

# Listas dos Países
paises = {'Brasil': {'cruzador': 1,'torpedeiro': 2,'destroyer': 1,'couracado': 1,'porta-avioes': 1}, 
    'França': {'cruzador': 3, 'porta-avioes': 1, 'destroyer': 1, 'submarino': 1, 'couracado': 1},
    'Austrália': {'couracado': 1,'cruzador': 3, 'submarino': 1,'porta-avioes': 1, 'torpedeiro': 1},
    'Rússia': {'cruzador': 1,'porta-avioes': 1,'couracado': 2,'destroyer': 1,'submarino': 1},
    'Japão': {'torpedeiro': 2,'cruzador': 1,'destroyer': 2,'couracado': 1,'submarino': 1}}

# Iniciando o Jogo
nome = input('Digite seu nome: ')
print(f'\nBem-vindo(a) à Batalha Naval, {nome}! Iniciando jogo...\n')

# Sorteando um país para a máquina
lista = []
for p in paises.keys():
    lista.append(p)
pais_comp = random.choice(lista)

# Criando a Matriz Inicial
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

for linha in matriz_comp:
    lista_linha = '   '.join(linha)
    #print(lista_linha)
