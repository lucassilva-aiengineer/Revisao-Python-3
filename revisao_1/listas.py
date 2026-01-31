

from faker import Faker
from typing import List


faker = Faker('pt_BR')

# gerar_nomes = lambda argumento : argumento.name_male()

# print(gerar_nomes(faker))

# Criando uma função que remove os pré-fixos 

def gerar_nomes_tratados(quantidade_nomes: int)-> List[str]:

    nomes: List[str] = []

    for _ in range(quantidade_nomes):

        nome = faker.name_male()
        nome_lista = nome.split(" ")

        if len(nome_lista[0]) < 4: 
            nome_lista.remove(nome_lista[0])

        nome_formatado = ' '.join(nome_lista)
        nomes.append(nome_formatado)

        # print(nome)

    return nomes 


nomes_gerados = gerar_nomes_tratados(10)

copia_a = nomes_gerados[:]

nome_add = "Marcos Levi"

copia_a.append(nome_add)


if "Marcos Levi" in nomes_gerados:
    print("A lista original também foi modificada!")

else:
    print("A lista original não foi alterada.")


print("Cópia Real: ")
print(" - " + copia_a[-1])

# print(nomes_gerados)

