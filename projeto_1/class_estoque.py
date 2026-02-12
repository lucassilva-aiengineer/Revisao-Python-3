from __future__ import annotations 
from class_item import ItemEstoque
from class_funcoes import Funcoes
from typing import List 


# Definindo a classe Estoque 

objeto_funcoes = Funcoes()

class Estoque: 

    def __init__(self, produtos: List[ItemEstoque]= []):

        

        # Atributos de acesso privado
        self.__id_ = objeto_funcoes.gerar_id()
        self.__produtos = produtos 
        self.__estoque_custo_total = sum([item.custo for item in self.__produtos])
        self.__custo_medio_item = sum([item.custo for item in self.__produtos]) / len(self.__produtos)
