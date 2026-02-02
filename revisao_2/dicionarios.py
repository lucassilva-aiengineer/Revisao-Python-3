from typing import Dict
import random 

dicionario_a: Dict[str, list] = {}




dicionario_a["brasil"] = ["Goiânia", "Rio de Janeiro", "São Paulo"]
dicionario_a["estados_unidos"] = ["New York", "Washington", "Dallas", "Chicago", "New Orleans"]
dicionario_a["reino_unido"] = ["London", "Gravesend"]


def exibir_dicionario():
    print(dicionario_a["brasil"][0])


    print(dicionario_a.items())

    for indice_a, indice_b in dicionario_a.items():

        # print("País: " + " " + indice_a) 
        # pais formatado

        pais_nome_formatado = indice_a.replace("_", " ")
        
        print(" ")
        print(pais_nome_formatado.title())
        print(" ")

        for pais in indice_b:
            print(pais)



def exibir_dicionario_a():

    for chave in dicionario_a: 

        nome_formatado = chave.replace("_", " ")
        print("")
        print("=========",nome_formatado.title(),"=========") 
        # print("\n")

        for valor in range(len(dicionario_a[chave])): 

            print(dicionario_a[chave][valor])


# exibir_dicionario_a() 

# if "brasil" in dicionario_a: 
#     print("Brasil Faz parte do dicionário A!")

# else: 
#     print("Brasil Não Faz parte do dicionário A.")

def deletando_paises()-> None:

    if "brasil" in dicionario_a:
        del dicionario_a["brasil"] 

    if "brasil" in dicionario_a:
        print("Brasil faz parte do dicionário de países.")

    else:
        print("Brasil não faz parte do dicionário de países.") 


from collections import defaultdict 


meu_dicionario: Dict[str, list] = defaultdict(list)

# Cria um dicionário com uma lista caso uma chave buscada ainda não 
# fassa parte do dicionário. 

def adicionan_valores():

    meu_dicionario["mateus"] = []

    # print(meu_dicionario["mateus"])

    meu_dicionario["lucas"].append("emprego1")


    print(meu_dicionario["lucas"])



dicionario_dicionarios: Dict[str, dict] = defaultdict(dict)

dicionario_dicionarios["id0001"]["nome"] = "Lucas"

print(dicionario_dicionarios["id0001"])


dicionario_dicionarios["id0002"]["nome"] = "Mateus"

print(dicionario_dicionarios["id0002"])



from typing import List



# Loops 

# nomes: List[str] = []
# nomes_adicionados = 0

# while nomes_adicionados <= 100:

#     nomes.append("Marcos") 

#     nomes_adicionados = nomes_adicionados + 1

# print(nomes[ :10])

# Utilizando um loop while para preencher um dicionário. 

from faker import Faker 


def preencher_dicionario(pessoas_gerar: int= 0)-> dict: 

    assert type(pessoas_gerar) == int, "A quantidade de pessoas deve ser indicada utilizando o tipo de dados int"

    defaultdict_a: Dict[str, dict] = defaultdict(dict)

    faker = Faker('pt_BR')



    ids_adicionados = 0
    while ids_adicionados <= pessoas_gerar: 

        ids_adicionados += 1 

        id_ = "id" + str(ids_adicionados)   # String concatena-se apenas com string. 

        informacoes = ["nome", "idade", "ensino_superior", "endereco"]

        for informacao in informacoes: 

            if informacoes.index(informacao) == 0:

                nome = faker.name_male()

                defaultdict_a[id_][informacao] = nome 

            elif informacoes.index(informacao) == 1: 

                idade = random.randint(20, 30)

                defaultdict_a[id_][informacao] = idade 


            elif informacoes.index(informacao) == 2: 

                ensino_superior = random.randint(0, 2)

                defaultdict_a[id_][informacao] = False if ensino_superior == 0 else True 


            else: 

                endereco = faker.address()

                defaultdict_a[id_][informacao] = endereco 


    return defaultdict_a 


dicionario = preencher_dicionario(10)

print(dicionario)