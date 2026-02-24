# Importações 

import random 
import string 
from typing import List, Union
from datetime import datetime, timedelta

class Funcoes: 

    @staticmethod 
    def gerar_id()-> str:
        """
            Um método que gera ids
        """
        letras: List[str] = []

        letras += string.ascii_lowercase + string.ascii_uppercase
        id_: List[str] = [random.choice(letras) if random.randint(0, 1) == 0 else str(random.randint(0, 9)) for _ in range(0, 5)]

        id_f= ''.join(id_)

        return id_f


    @staticmethod 
    def validade_aleatoria(dias: int= 0):

        if not dias: 
            dias = int(input("Indique a quantidade de dias: "))

        hoje = datetime.now()
        validade = hoje + timedelta(dias)

        return validade 

def testes():

    letras: List[str] = []

    letras += string.ascii_lowercase + string.ascii_uppercase

    print(letras)

# testes()

# def main():

    # objeto_funcao = Funcoes()

    # print(objeto_funcao.gerar_id())

    # print(objeto_funcao.validade_aleatoria(random.randint(0, 200)))

    # print(objeto_funcao.validade_aleatoria())

# main()