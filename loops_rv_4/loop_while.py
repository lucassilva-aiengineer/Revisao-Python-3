# Loop while
# O loop while, é diferente do loop for, o loop while executa uma instrução 
# enquanto uma condição se verificar verdadeira. Existem as condições de parada, 
# estas que, determinam a quantidade de repetições, iterções, execuções de um determinado 
# bloco de código serão realizadas, podendo ser implícitas ou explecitas. 

from typing import List, Dict
import random 
import time




# Pensando sobre condições de para explícitas. 

def gerar_nomes()-> Dict[str, dict]:

    # nomes: List[str] = [] 

    pessoas: Dict[str, dict] = {}

    print("Bem vindo ao sistema!")

    while True: 

        print("Para sair digite finalizar")

        # nome = input("Indique um nome para a lista:")
        pessoa: Dict[str, str] = {}

        nome = input("Indique o nome da pessoa: ")
        cpf = input("Indique o cpf da pessoa: ")

        # nomes.append(pessoa) 

        pessoa["nome"] = nome 
        pessoa["cpf"] = cpf 

        pessoas[str(random.randint(0, 100))] = pessoa 
        time.sleep(1)


        if nome.lower() == "finalizar":
            
            print("Saindo...")
            time.sleep(2)
            
            break



    return pessoas


nomes = gerar_nomes()

print(nomes)

