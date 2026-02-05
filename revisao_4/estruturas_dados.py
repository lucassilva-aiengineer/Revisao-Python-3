# Listas 

# Listas são estruturas de dados que armazenam uma quantidade indeterminada de valores de 
# diferentes tipos de dados, são estruturas de dados ordenadas, modificáveis que permitem 
# a duplicação de elementos e que têm os índices estão associados a elementos. 

from faker import Faker
from typing import List, Dict, Union 
import random 


def adicionar_pessoas(qntd_pessoas: int = 0)-> List[Union[int, str]]:

    # assert type(qntd_pessoas) == int,   """ A quantidade de pessoas deve ser
                                            # indicada utilizando números inteiros."""

    assert isinstance(qntd_pessoas, int) == True


    """
        Uma função que adiciona um nome, cpf e duas notas a uma 
        lista o objetivo é tentamos manipular essas lista posteriormente

        lista_alunos = [nome, cpf, nota_1, nota_2, nome_2, cpf_2, nota_2, nota_3...]

    """
    pessoas: List[Union[int, str]] = []

    faker = Faker('pt_BR')
    faker_a = Faker('en_US')

    pessoas_adicionadas = 0 
    pessoas_adicionar = int(input("Indique a quantidade de pessoas adicionádas: ")) if qntd_pessoas == 0 else qntd_pessoas

    while pessoas_adicionadas <= pessoas_adicionar: 

        pessoa_nome = faker_a.name()
        cpf = faker.cpf()

        nota1 = random.randint(0, 11)
        nota2 = random.randint(0, 11)

        
        pessoas.append(pessoa_nome)
        pessoas.append(cpf)
        pessoas.append(nota1)        
        pessoas.append(nota2)


        pessoas_adicionadas += 1 


    return pessoas

import json 

lista_alunos = adicionar_pessoas()

# print(lista_alunos[:10])

# print(lista_alunos[:])

# Adicionando esses itens a jsons separados

# dicionario_pessoas: Dict[str, Union[str, int]] = {}


# Manipular as listas geradas e gerar versões melhores
# e continuar revisando contúdos importantes. 

# lista_pessoas: List[dict] = []

# num_item = 0 
# for item in lista_alunos:

#     dicionario_pessoa: Dict[str, int] = {}

#     if num_item < 4: 

#         dicionario_pessoa[str(num_item)] = 0 

#         lista_pessoas.append(pessoa)


# #     for i in range(0, 4): 



