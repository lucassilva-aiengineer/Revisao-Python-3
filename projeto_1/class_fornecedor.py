# Classe Fornecedor 

from class_pessoa import Pessoa 
from class_relatorio import Relatorio
from typing import List, Optional
from class_item import ItemEstoque
from datetime import datetime
from class_funcoes import Funcoes 
from faker import Faker
# class Fornecedor(Pessoa):

#     """
#         As instâncias desta classe serão os fornecedores dos 
#         produtos que compõem o estoque.
#     """

#     def __init__(self, nome: str= "nome_fornedor", idade: int= 0, cpf: str= "000.000.000-00", 
#                 relatorios: List[Optional[Relatorio]]= [], produtos: List[ItemEstoque]= []):
#         # "Criamos" um objeto padrão pela classe mãe.
#         super().__init__(nome, idade, cpf, relatorios)

#         # Especializamos. 
#         """Os produtos que são fornecidos pelo nosso fornecedor. """
#         self.__produtos = produtos

class Fornecedor:

    def __init__(self, razao_social: str= "Fornecedora de Alimentos", localizacao: str= "", cnpj: str= "00000000", 
                    inicio_parceria: datetime=  datetime.now(), relatorios: List[Relatorio]= [], tipo: str= ""): 

        funcoes = Funcoes()

    # Atributos Privados 

        self.__id_ = funcoes.gerar_id()
        self.__razao_social = razao_social 
        self.__cnpj = cnpj
        self.__localizacao = localizacao 
        self.__inicio_parceria = inicio_parceria 
        self.__relatorios = relatorios 
        self.__tipo = tipo 


    # Desenvolvendo o encapsulamento, uma forma de restringir o acesso 
    # aos atributos, assim os protegendo tanto em relação a escrita quanto a leitura, é algo que 
    # impede o acesso direto, uma forma de munitorar o acesso, é como uma oficial de fronteira, que monitora 
    # as pessoas que estão entrando no país. 


    # Getters 
    # Criando estratégias de acesso - Leitura dos atributos. 

    @property 
    def id_(self)-> str:
        return self.__id_ 

    @property 
    def razao_social(self)-> str: 
        return self.__razao_social 

    @property 
    def cnpj(self)-> str: 
        return self.__cnpj 

    @property 
    def localizacao(self)-> str: 
        return self.__localizacao 

    @property 
    def inicio_parceria(self)-> datetime: 
        return self.__inicio_parceria 

    relatorio_tipo = List[Relatorio] 
    @property 
    def relatorios(self)-> relatorio_tipo:
        return self.__relatorios 

    @property 
    def tipo(self)-> str:
        return self.__tipo 

    # Setters - Controlando o acesso a escrita, dos atributos. 

    @razao_social.setter 
    def razao_social(self, nv_razao_social: str)-> None:
        self.__razao_social = nv_razao_social

    @cnpj.setter 
    def cnpj(self, nv_cnpj: str)-> None:
        self.__cnpj = nv_cnpj 

    @localizacao.setter 
    def localizacao(self, nv_localizacao: str)-> None:
        self.__localizacao = nv_localizacao

    @inicio_parceria.setter 
    def inicio_parceria(self, nv_inicio)-> None:
        self.__inicio_parceria = nv_inicio 

    @relatorios.setter
    def relatorios(self, nv_relatorios)-> None: 
        self.__relatorios = nv_relatorios 

    @tipo.setter 
    def tipo(self, nv_tipo)-> None:
        self.__tipo = nv_tipo


    def mostrar_fornecedor(self)-> str:

        return f"""
===========================================================================
Razão Social: {self.__razao_social}                     CNPJ: {self.__cnpj}
Início da parceria: {self.__inicio_parceria}             tipo: {self.__tipo}
==========================================================================="""


def main():

    """
    Testando as instâncias da classe fornecedor.
    """

    faker = Faker('en_US')
    faker_a = Faker('pt_BR')

    # fornecedor = Fornecedor(faker.company(), faker.address(),   faker_a.cnpj())

    # print(faker_a.cnpj())

main()