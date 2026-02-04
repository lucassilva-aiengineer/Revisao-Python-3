# Loop for 

# O loop for é um laço de repetição que itera, executa um bloco de código 
# um número determinado de vezes, descritas por um intervalo de itens como 
# um range ou iteráveis com tuplas, listas e dicionário, ou seja executa um 
# bloco de código, uma instrução, uma quantidade predeterminada de vezes. 


import time 
import random 
from typing import List, Dict 

def loop_for()-> None:
    for numero in range(10):
        print(numero)

    print("")
    for numero in range(4, 10, 2):
        time.sleep(2)
        print(numero)


minha_lista = [random.randint(0, 100000) for a in range(10000)]
# print(gerar_lista)

numeros_impares: List[int] = []
numeros_pares: List[int] = [] 

numero_encontrado = 0 

for numero in minha_lista: 

    if numero % 2 == 0: 
        # print(numero)

        numeros_pares.append(numero)
        continue # Pulando o número caso ele seja par 

    elif numero == 100: 
        print("Número 100 encontrado!")
        numero_encontrado += 1
        # break

    else: 
        numeros_impares.append(numero)

        # print(numero)

# print("A quantidade de números ímpares", len(numeros_impares))
# print(f"A quantidade de números pares: {len(numeros_pares)}")

# print(f"A quantidade de repetições: {numero_encontrado}")

# Criando o nossa nossa própria função counter. 

Vetor = List[int]

def meu_counter(vetor: Vetor)-> list:

    """
        Esta função recebe um vetor verifica se aquele número 
        faz parte do dicionário e conta quantas vezes aquele
        número aparece no vetor. 

    """

    dicionario: Dict[str, int] = {}

    for numero in minha_lista: 

        if not str(numero) in dicionario:

            dicionario[str(numero)] = 1 

        else: 

            dicionario[str(numero)] += 1 

    tupla_meu_counter = dicionario.items()

    # Ordenando o nosso dicionário. 

    tuplas_ordenadas = sorted(tupla_meu_counter, key= lambda tupla: tupla[1], reverse= True)

    return tuplas_ordenadas





print(meu_counter(minha_lista)[:5])