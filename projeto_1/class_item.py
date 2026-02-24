from __future__ import annotations 
from class_funcoes import Funcoes
from typing import List 
from typing import Union 
from datetime import datetime, timedelta 
from class_funcoes import Funcoes 

Fornecedor = int 


class ItemEstoque:

    margem_lucro = 140 / 100
    tributacao = 130 / 100  
    total_items: List[ItemEstoque] = [] # Atributos de classe. 
    def __init__(self, nome: str= "", marca: str= "", descricao: str= "",
            quantidade: int= 0, validade: datetime= datetime.now(), custo: float= 0.0,
            fornecedores: List[Union[str, Fornecedor]]= [])-> None:

        # Nós criamos um objeto, ItemEstoque, acessamos este objeto e associamos a ele 
        # espaços reservados para os seguintes atributos e atribuimos os argumentos declarados 
        # Aos atributos; 


        # Criando um objeto funcões 

        objeto_funcoes = Funcoes()

        # Atributos privados. 

        self.__id_ = objeto_funcoes.gerar_id()
        self.__nome = nome 
        self.__marca = marca 
        self.__descricao = descricao 
        self.__quantidade = quantidade 
        self.__validade = validade 
        self.__custo = custo 
        self.__preco = (self.__custo * ItemEstoque.tributacao) * ItemEstoque.margem_lucro 
        self.__fornecedores = fornecedores
        self.__status_produto = True

        # Adicionando o objeto item ao atributo de classe total_items.
        ItemEstoque.total_items.append(self)

    # Construnindo os getters, regras de acesso, leitura dos atributos dos objetos. 
    
    @property 
    def id_(self):
        return self.__id_ 
    
    @property 
    def nome(self)-> str:

        # nome_f = ''.join(['*' for id_ in range(len(self.__nome) - 3)])
        return self.__nome 

    @property 
    def marca(self)-> str:
        return self.__marca

    @property 
    def descricao(self)-> str: 
        return self.__descricao 

    @property 
    def preco(self)-> float: 
        return self.__preco

    @property 
    def custo(self)-> float: 
        return self.__custo 

    @property 
    def quantidade(self)-> int:
        return self.__quantidade

    @property     
    def validade(self)-> str:
        return self.__validade 

    @property 
    def fornecedores(self)-> List[Fornecedor]:
        return self.__fornecedores

    @property 
    def status_produto(self)-> bool:

        validade = self.__validade
        hoje = datetime.now()

        if validade <= hoje:
            self.__status_produto = False 

        return self.__status_produto

    # Construindo os setters, uma forma protegida de acesso, no caso escrita de 
    # objetos. 

    @nome.setter 
    def nome(self, nv_nome: str)-> None:
        self.__nome 

    @marca.setter 
    def marca(self, nv_marca: str)-> None: 
        self.__marca = nv_marca 

    @descricao.setter 
    def descricao(self, nv_descricao: str)-> None:
        self.__descricao = nv_descricao 

    @preco.setter 
    def preco(self, nv_preco: float)-> None:
        self.__preco = nv_preco 

    @custo.setter
    def custo(self, nv_custo: float)-> None:
        self.__custo = nv_custo 

    @quantidade.setter 
    def quantidade(self, nv_quantidade: int)-> None: 
        self.__quantidade = nv_quantidade 

    @validade.setter 
    def validade(self, nv_validade: str)-> None:
        self.__validade = nv_validade

    # Definindo a regra de acesso voltada a alteração de atributos, que tipo de 
    # alteração poderá ser feita. 

    # No caso eu posso substituir o atributo id por qualquer outro id, mas poderiamos 
    # muito bem restringir este acesso impondo uma regra mais proibitiva. 
    @id_.setter
    def id_(self, nv_id_: str):
        self.__id_ = nv_id_ 

    @status_produto.setter 
    def status_produto(self, nv_status_produto: bool):
        self.__status_produto = nv_status_produto 
    # Métodos referente ao nossos objetos. 

    def exibir_item(self)-> str:

        """
            Método que exibe informações
            sobre o objeto, informações sobre
            todos os atributos. 

        """

        return f"""
Nome: {self.__nome}
Marca: {self.__marca}

Descrição: {self.__descricao}

Valor: {self.__preco}
Custo: {self.__custo}
Quantidade: {self.__quantidade}
Validade: {self.__validade}
Fornecedores: {str(fornecedor for fornecedor in self.__fornecedores)}
                """


    # Um método "mágico", método dunder. 

    def __repr__(self)-> str:

        return f"""Nome: {self.__nome} | Quantidade: {self.__quantidade}"""


# Testando os obejetos. 

# objeto = ItemEstoque("Arroz", "Amil", "Arroz Parbolizado 2kg")

# print(objeto)

# print(objeto.exibir_item())

def teste():

    objeto_cls_funcoes = Funcoes()

    # Testando a data de um produto vencido. 
    validade = objeto_cls_funcoes.validade_aleatoria(-100)

    item = ItemEstoque(validade= validade)

    # print(item.status_produto) 

    if item.status_produto:
        print("Produto dentro do prazo de validade!")

    else:
        print("Produto vencido!")


# teste()