# O objetivo deste arquivo é testar o funcionamento das classes 
from class_mercado import Mercado 
from class_estoque import Estoque 
from class_fornecedor import Fornecedor
from class_funcionario import Funcionario
from class_item import ItemEstoque 
from faker import Faker 
import random 


def main():

    faker = Faker('en_US')

    nomes_produtos = ["Arroz", "Feijão", "Açucar", "Refrigerante", "Farinha de Trigo"]
    produtos = [ItemEstoque(random.choice(nomes_produtos),
                            faker.company(), quantidade= random.randint(0, 30),
                            custo= random.uniform(0, 20)) for _ in range(5)]

    for produto in produtos:
        print(produto.exibir_item())


main()