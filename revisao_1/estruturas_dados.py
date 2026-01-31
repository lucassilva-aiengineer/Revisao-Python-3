from __future__ import annotations  # Utilizamos para indicar a classe como tipo 
                                    # de dado dentro da classe.  

from faker import Faker 
from typing import Union    # Utilizando este módulo e este objeto para indicar que certo parâmetro receberá um dos tipos. 
import random    
from typing import List   
import time

# Criando um objeto pessoa. 

class Pessoa:

    pessoas_criadas = 0 # Atributo de classe 

    def __init__(self, nome, idade, endereco)-> None:

        Pessoa.pessoas_criadas += 1 

    # Atributos privados. 
        self.__nome = nome 
        self.__idade = idade 
        self.__endereco = endereco 



    # Definindo o encapsulamento 

    # Os getters 
    # Uma regra de  para leitura dos atributos. 
    @property 
    def nome(self)-> str:       # Anotações de tipo, indicando o tipo retornado
        return self.__nome 

    @property 
    def idade(self)-> int:      # Retornando o tipo de dados inteiro. 
        return self.__idade 

    @property 
    def endereco(self)-> str: # Retornando a string 
        return self.__endereco 


    # Definindo os setters
    # Uma regra de acesso para a inscrita dos atributos. 
    @nome.setter 
    def nome(self, novo_nome: str)-> None:
        self.__nome = novo_nome 


    @idade.setter 
    def idade(self, nova_idade: int)-> None:
        self.__idade = nova_idade 

    @endereco.setter 
    def endereco(self, novo_endereco: str)-> None:
        self.__endereco = novo_endereco 




def criar_obj_pss(quantidade_pessoas: Union[int, None]= None) -> List[Pessoa]:

    faker = Faker('pt_BR')


    if not quantidade_pessoas:
        quantidade_pessoas = int(input("Indique a quantidade de pessoas que você gostaria de criar: "))

    lista: List[Pessoa] = []

    for numero in range(0, quantidade_pessoas):

        nome = faker.name_male()
        idade = random.randint(24, 30)
        endereco = faker.address()

        pessoa = Pessoa(nome, idade, endereco)

        lista.append(pessoa)

    return lista


# Criando um dicionário de funções 

from typing import Dict 

distribuicao: Dict[str, list]  = {}


pessoas = criar_obj_pss(10)

cargos = ["analista_de_testes", "engenheiro_de_ia", "cientista_de_dados"]

for numero in range(0, 3):

    cargo = cargos[numero]

    distribuicao[cargo] = [random.choice(pessoas) for _ in range(0, 3)]


# print(distribuicao['analista_testes'])

# print(distribuicao)

# for funcionario in distribuicao['analista_testes']:
#     print(funcionario.nome)


for chave, valor in distribuicao.items():
    # print(chave)

    chave_formatada = chave.replace("_", " ")

    print(f"============= {chave_formatada.title()} ==============")
    print("")

    for funcionario in valor:
        print(f"""Nome: {funcionario.nome} 
Idade: {funcionario.idade}
Endereço: {funcionario.endereco}
""")



# try:
#     pessoas = criar_obj_pss()

#     for pessoa in pessoas:

#         print(pessoa.nome)

        

# except ValueError as message:

#     print(message)
#     time.sleep(2)

#     print("""A quantidade de pessoas deve 
# ser descrita utilizando números inteiros.""")
#     time.sleep(2)

#     print("Tentando novamente...")
#     time.sleep(2)

#     pessoas = criar_obj_pss(10)

#     for pessoa in pessoas:

#         print(f"""
# {pessoa.nome}
# """)


# else: 

#     print("Operação concluída com sucesso...")
#     time.sleep(2)

#     print("Nenhum erro detectado!")
#     time.sleep(2)

# finally:

#     print("Programa iterado...")
#     time.sleep(2)

