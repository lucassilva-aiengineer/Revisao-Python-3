# Classe mercado 
from typing import List 
from class_estoque import Estoque
import typing 
from class_item import ItemEstoque 
from class_funcionario import Funcionario 
from class_funcoes import Funcoes 
from typing import Union 
from class_fornecedor import Fornecedor 

funcoes = Funcoes()

class Mercado:

    """
        O objetivo desta classe é administrar as outras classes.
    """

    def __init__(self, nome: str= "Supermecado Padrão", endereco: str= "rua A qd 123, Setor ABCD, Goiânia - Goiás", 
                estoque: typing.Union[Estoque, List[ItemEstoque]] = [], funcionarios: typing.List[Funcionario]= [],
                fornecedores: List[Fornecedor]= []):


    # Atributos Privados

        self.__id_ = funcoes.gerar_id()
        self.__nome = nome 
        self.__endereco = endereco 
        self.__estoque = estoque 
        self.__funcionarios = funcionarios 
        self.__fornecedores = fornecedores 

    # Encapsulamento se resume em vetar o acesso direto a atributos de objetos tanto em relação a 
    # escrita quanto a leitura, é algo bem parecido com o oficial de fronteira que impede o acesso 
    # livre a um determinado país. 


    # Criando os getters, os métodos relacionados a leitura dos objetos.
    @property 
    def id_(self)-> str:
        return self.__id_

    @property
    def nome(self)-> str:
        return self.__nome 

    @property
    def endereco(self)-> str:
        return self.__endereco 

    @property
    def estoque(self)-> Union[Estoque, List[ItemEstoque]]:
        return self.__estoque 

    @property 
    def funcionario(self)-> list: 
        return self.__funcionarios 

    @property 
    def fornecedores(self)-> List[Fornecedor]:
        return self.__fornecedores

    # Criando os setters, 
    # Os métodos de acesso relacionados a escrita. 

    @id_.setter
    def id_(self, nv_id_)-> None:
        self.__id_ = nv_id_ 

    @nome.setter 
    def nome(self, nv_nome)-> None:
        self.__nome = nv_nome 

    @endereco.setter 
    def endereco(self, nv_endereco)-> None:
        self.__endereco = nv_endereco 

    @estoque.setter 
    def estoque(self, nv_estoque)-> None:
        self.__estoque = nv_estoque 

    @funcionario.setter 
    def funcionario(self, nv_funcionario)-> None:
        self.__funcionarios = nv_funcionario 

    @fornecedores.setter 
    def fornecedores(self, nv_fornecedores)-> None:
        self.__fornecedores = nv_fornecedores



# mercado = Mercado()
# print(mercado)