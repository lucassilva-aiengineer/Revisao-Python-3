# Tuplas. 


from faker import Faker 
import random 
from typing import List, Tuple


faker = Faker('en_US')




def gerar_pessoas(qntd_criar: int= 0)-> List[Tuple[str, float, float, float]]:


    """ 
        Essa Função cria uma tupla 
        contendo: nome, idade e notas de 'alunos'. 

    """

    pessoas: List[tuple] = []


    pessoas_criadas = 0
    while pessoas_criadas <= qntd_criar: 

        nome = faker.name_male()
        idade = random.randint(9, 17)

        nota_1 = random.uniform(0, 10)
        nota_2 = random.uniform(0, 10)
        nota_3 = random.uniform(0, 10)

        pessoa = (str(nome), idade, nota_1, nota_2, nota_3) 

        pessoas.append(pessoa)

        pessoas_criadas += 1  


    # print(pessoas) 

    return pessoas 

alunos = gerar_pessoas(qntd_criar= 10)

copia_alunos = alunos[:]

for tupla in alunos: 

    # Adicionando um ponto estra para cada aluno. 

    # tupla[1] = tupla[1] + 1 

    tupla_f = list(tupla)

    # print("Nota Anterior: ")
    # print(tupla[2])

    tupla_f[2] = tupla_f[2] + 1
    tupla_f[3] = tupla_f[3] + 1
    tupla_f[4] += 1 

    # print("Nota Adicionada: ")
    # print(tupla_f[2])

    # tupla_f[1] 

    # print(tupla_f[1]

    # print(tupla_f)
    
    alunos.remove(tupla)
    alunos.append(tuple(tupla_f))

    # alunos.replace(tupla, tupla_f) 


# for aluno in alunos:
# for a in range(10): 

#     print("Nota antiga")


# for aluno in enumerate(alunos): 

#     print("Nota antiga: ")

# lista = [1, 2, 3, 4, 5, 6]

# print(list(enumerate(lista)))

print(list(enumerate(alunos))) 

alunos_enumerate = list(enumerate(alunos))

# for aluno in alunos_enumerate: 

#     print(f"""
#     Nota antiga: {copia_alunos(aluno[0])}
#     Nota nova: {aluno[0]}""")

# print(copia_alunos[0])

# print(alunos_enumerate[0][0])


# print(copia_alunos)

for aluno in alunos_enumerate: 

    print(f"""
        Nota Anterior da Prova 1 {copia_alunos[aluno[0]][2]}
        Nota Atualizada da Prova 1 {aluno[1]}.
    """)