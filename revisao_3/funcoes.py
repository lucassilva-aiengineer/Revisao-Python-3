# 12:20 - 13:20 

import time

# Argumentos de palavra chave e argumentos de asterísco. 

def funcao(*posicionais, **palavra_chave):

    print("Argumentos Posicionais: ", posicionais)
    print("Argumentos Palavra Chave", palavra_chave)


# funcao("Argumento_1", "Argumento_2", "Argumento_3", a= "Kw1", b= "kw2")


from typing import Tuple 

def imprimir_nomes(*args_posicionaistupla)-> None:

    print(f"Tupla: {args_posicionaistupla}")

    print("")
    for nome in args_posicionaistupla:

        if nome.lower().startswith("a"):
            print("Pulando nome com a letra A.")
            continue 

        elif nome.lower().startswith("b"):
            print("Encontrei um nome que começa com a letra B.")
            time.sleep(2)
            print("Parando...")
            time.sleep(2)

            break 

        else: 
            print(nome)



# imprimir_nomes("Mateus", "Adam", "Mattew", "Braden", "Mark")

string_original = "Marcos"
copiando_string = string_original[:]

copiando_string += " Silva"

# print(string_original)
# print(copiando_string)

# print(string_original[:4])


palavras = "Fique tranquilo tudo irá dar certo"
lista_palavras = palavras.split(" ")
# print(lista_palavras) 

# Contando a quantidade total de letras

from collections import Counter, defaultdict 
from typing import Dict 

def contando_letras()-> None:
    dicionario_contagem: Dict[str, int] = defaultdict(int)

    for palavra in lista_palavras: 

        for letra in palavra: 

            dicionario_contagem[letra] += palavra.count(letra)

    print(dicionario_contagem) 



# Escopo de variável. 

numero = 5
def funcao_a():

    global numero 

    numero = 10
    print(numero)

print("Antes de alterar a função:", numero)

funcao_a()

print(numero)