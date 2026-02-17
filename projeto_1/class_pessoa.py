from class_funcoes import Funcoes 
from typing import List, Optional

from class_relatorio import Relatorio 

# try: 
#     from class_relatorio import Relatorio

# except FileNotFoundError as message: 
#     print("Arquivo não encontrado!")

# else: 
#     print("Arquivo executado sem erros!")

# finally:
#     print("Código iterado!")


funcoes = Funcoes()

class Pessoa:

    def __init__(self, nome: str= "nome_a", idade: int= 0,
                cpf: str= "000000000-00", relatorios: List[Optional[Relatorio]]= []):

        # Atributos Privados

        self.__id_ = funcoes.gerar_id()
        self.__idade = idade 
        self.__cpf = cpf 
        self.__relatorios = relatorios  


    # Definindo o escapsulamento, proteção do acesso aos atributos. 

    # Defindo as regras de acesso, leitura. 
    @property 
    def id_(self)-> str:
        return self.__id_

    @property 
    def idade(self)-> int:
        return self.__idade 

    @property 
    def cpf(self)-> str:
        return self.__cpf 

    @property 
    def relatorios(self)-> list: 
        return self.__relatorios 


    # Definindo as regras de acesso, escrita. 

    @id_.setter 
    def id_(self, nv_id_: str)-> None:
        self.__id_ = nv_id_ 

    @idade.setter 
    def idade(self, nv_idade: int)-> None:
        self.__idade = nv_idade 

    @cpf.setter 
    def cpf(self, nv_cpf)-> None:
        self.__cpf = nv_cpf

    @relatorios.setter 
    def relatorio(self, nv_relatorios)-> None:
        self.__relatorios = nv_relatorios  