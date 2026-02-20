from __future__ import annotations 
from class_item import ItemEstoque
from class_funcoes import Funcoes
from faker import Faker
from typing import List 


# Definindo a classe Estoque 

objeto_funcoes = Funcoes()

class Estoque: 

    estoques_criados: List[Estoque] = []
    qnt_estoques = len(estoques_criados)

    def __init__(self, produtos: List[ItemEstoque]= []):

        

        # Atributos de acesso privado
        self.__id_ = objeto_funcoes.gerar_id()
        self.__produtos = produtos 
        self.__custo_total = sum([item.custo * item.quantidade for item in self.__produtos])
        self.__preco_total = sum([item.preco for item in self.__produtos])
        self.__custo_medio_item = (sum([item.custo for item in self.__produtos]) / len(self.__produtos)) if len(self.__produtos) > 0 else 0
        # Quando o status é true o produto está dentro do prazo de validade. 
        self.__itens_validos = [item for item in self.__produtos if item.status_produto == True] 

        Estoque.estoques_criados.append(self)


    # Alterando dinâmicamente o valor de custo do estoque 
    # def _relatorio(self):
    #     self.__custo_total = sum([item.custo for item in self.__produtos])

    # _relatorio()
    # Construindo as regras de acesso

    # Regras de Leitura 
    @property 
    def id_(self)-> str:
        return self.__id_

    @property 
    def produtos(self)-> List[ItemEstoque]:
        self.__custo_total = sum([item.custo for item in self.__produtos]) 
        return self.__produtos 

    @property 
    def custo_total(self)-> float: 
        return self.__custo_total 

    @property 
    def preco_total(self)-> float: 
        return self.__preco_total 

    @property 
    def custo_medio_item(self)-> float: 
        return self.__custo_medio_item

    @property 
    def itens_validos(self)-> List[ItemEstoque]:
        return self.__itens_validos 



    # Regras de escrita 

    @id_.setter 
    def id_(self, nv_id: str)-> None: 
        self.__id_ = nv_id 

    @produtos.setter 
    def produtos(self, nv_produtos: List[ItemEstoque])-> None: 
        self.__produtos = nv_produtos 

    @custo_total.setter 
    def custo_total(self, nv_custo: float)-> None:
        self.__custo_total = nv_custo 

    @preco_total.setter 
    def preco_total(self, nv_preco: float)-> None:
        self.__preco_total = nv_preco 

    @custo_medio_item.setter 
    def custo_medio_item(self, nv_custo_medio: float)-> None: 
        self.__custo_medio_item = nv_custo_medio 

    @itens_validos.setter 
    def itens_validos(self, nv_itens_validos: List[ItemEstoque])-> None:
        self.__itens_validos = nv_itens_validos 


    # Método que permite imprimirmos os objetos e acessarmos uma string ao invés 
    # de um endereço de memória.

    # Criando um método que imprime um relatório sobre o estoque 



    def __repr__(self):
        return f""" Estoque N° {len(Estoque.estoques_criados)}"""


def main():

    estoque = Estoque()

    # faker = Faker('pt_BR')
    faker = Faker('en_US')

    produto_a = ItemEstoque("Arroz", "Amil", "Arroz tipo 1 (5kg)", 100, "13/10/2027",
                            12, [str(faker.company()) for a in range(3)])


    # estoque.produtos = [produto_a]

    produto_b = ItemEstoque("Feijão", "Cristal", "Feijão tipo 1 (1kg)", 200, "13/07/2030")

    # estoque.produtos.extend([produto_b])

    estoque = Estoque([produto_a, produto_b])

    print(estoque.produtos)

    print(Estoque.estoques_criados)

    # Imprimindo o objeto estoque. 

    print(estoque)


    # print(estoque.custo_medio_item)
    print(estoque.custo_total)

    print(produto_a.custo)

    produto_c = ItemEstoque(custo= 100)

    estoque.produtos.append(produto_c)

    print(estoque.custo_total)

    print(estoque.produtos)

    print(estoque.custo_total)


# main()