from __future__ import annotations 
from typing import List 



class ItemEstoque:

    total_items: List[ItemEstoque] = [] # Atributos de classe. 
    def __init__(self, nome: str= "", descricao: str= "", quantidade: int= 0, validade: str= "07/02/2026")-> None:

        # Nós criamos um objeto, ItemEstoque, acessamos este objeto e associamos a ele 
        # espaços reservados para os seguintes atributos e atribuimos os argumentos declarados 
        # Aos atributos; 


        # Atributos privados. 

        self.__nome = nome 
        self.__descricao = descricao 
        self.__quantidade = quantidade 
        self.__validade = validade 


    @property 
    def nome(self)-> str:

        nome_f = ''.join(['*' for id_ in range(len(self.__nome) - 3)])

        return nome_f 






