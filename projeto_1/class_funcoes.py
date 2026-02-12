# Importações 

import random 
import string 
from typing import List, Union


class Funcoes: 

    @staticmethod 
    def gerar_id()-> str:

        letras: List[str] = []

        letras += string.ascii_lowercase + string.ascii_uppercase
        id_: List[str] = [random.choice(letras) if random.randint(0, 1) == 0 else str(random.randint(0, 9)) for _ in range(0, 5)]

        id_f= ''.join(id_)

        return id_f



def testes():

    letras: List[str] = []

    letras += string.ascii_lowercase + string.ascii_uppercase

    print(letras)

# testes()

def main():

    objeto_funcao = Funcoes()

    print(objeto_funcao.gerar_id())