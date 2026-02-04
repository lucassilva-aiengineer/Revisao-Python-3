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


palavras = "Tenha um bom dia"
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
    # print(numero)

# print("Antes de alterar a função:", numero)

funcao_a() # Eu consigo alterar a função a variável no interior da função. 

# print(numero)

# Funções lambda. 

# Funções lambda, são funções anônimas compostas apenas três coisas: palavra_chave argumento : expressão. 

dobrar = lambda argumento : argumento * 2

# print(dobrar(10))

adicionar = lambda parcela_a, parcela_b : parcela_a + parcela_b 

# print(adicionar(10, 10)) 

multiplicar = lambda fator_a, fator_b : fator_a * fator_b 

# print(multiplicar(10, 2)) 

dividir = lambda numerador, denominador : numerador / denominador if denominador != 0 else "Esta conta não pode ser feita"

# print(10, 0)

assert dividir(10, 0) == "Esta conta não pode ser feita", "O código deveria retornar esta string caso tudo ocorra como o esperado. " 

# print(dividir(10, 0))
