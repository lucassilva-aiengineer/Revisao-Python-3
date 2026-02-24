# Classe mercado 
from typing import List 
from class_estoque import Estoque
import typing 
from class_item import ItemEstoque 
from class_funcionario import Funcionario 
from class_funcoes import Funcoes 
from typing import Union 
from class_fornecedor import Fornecedor 
from faker import Faker 
from dados_projeto import lista_produtos_a 
from dados_projeto import lista_produtos_a
import random 
from datetime import datetime

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


    def __repr__(self):
        return f"Mercado Nome: {self.__nome}" 


    def exibir_relatorio(self): 

        pass 

def main(): 

    """
        Função princípal que testa estes objetos. 
    """

    faker = Faker('en_US')    
    faker_br = Faker('pt_BR')

    # nome do mercado
    nome_mercado = f"Super Mercado {faker.company()}"

    # Endereço do Mercado. 
    endereco = faker_br.address()

    # Criando um objeto estoque fara parte do mercado. 

    def gerar_produtos(qntd_parametro: int= 0)-> List[ItemEstoque]:


        if not qntd_parametro: 
            quantidade = int(input("Indique a quantidade de produtos: "))


        lista_produtos = []

        for _ in range(qntd_parametro if qntd_parametro else quantidade): 

            random.shuffle(lista_produtos_a.produtos_mercado)

            # Nome do produto
            produto_nome = random.choice(lista_produtos_a.produtos_mercado)

            # Marca 
            marca = faker.company()
            # Descrição 
            descricao = ""

            # Custo do produto
            custo = random.uniform(10, 20)

            # Quantidade
            quantidade = random.randint(0, 100)

            # Validade 
            validade = funcoes.validade_aleatoria(random.randint(0, 400))

            # status

            # custo 

            # fornecedores

            objeto_funcoes = Funcoes()
            fornecedores = [Fornecedor(faker_br.company(), faker_br.address(), faker_br.cnpj(),
                                        objeto_funcoes.validade_aleatoria(random.randint(0, 100))) for _ in range(random.randint(1, 2))]


            produto =   ItemEstoque(produto_nome, marca, quantidade= quantidade,
                                    validade= validade, custo= custo, fornecedores= fornecedores)


            # Adicionando os produtos à lista de produtos 

            lista_produtos.append(produto)

        return lista_produtos


    produtos_gerados = gerar_produtos(10)

    for produto in produtos_gerados:
        print(produto)


    faker = Faker('pt_BR')
    faker_br = Faker('en_US')


    # Estoque
    estoque_a = Estoque(produtos_gerados)

    # Funcionários 
    cargos_tipos = ["Estratégico", "Controle", "Controle", "Operacional"]


    funcionarios_a = [Funcionario(faker_br.name(), random.randint(20, 50), 
                                    cpf= faker.cpf(), cargo= random.choice(lista_produtos_a.cargos_mercado[random.choice(cargos_tipos)])) for _ in range(10)]

    # fornecedores_a = [prd.fornecedores for prd in Estoque.produtos]

    mercado = Mercado(faker.company(), faker_br.address(), 
                        estoque= estoque_a, funcionarios= funcionarios_a)



    # print(mercado) 

    print(mercado.nome)

main()