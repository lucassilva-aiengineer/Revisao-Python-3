from class_pessoa import Pessoa 
from class_relatorio import Relatorio
from typing import List, Optional
import time 

class Funcionario(Pessoa):

    def __init__(self, nome, idade, cpf, relatorios: List[Optional[Relatorio]], cargo: str= "funcionario",
                salario: float= 0):
        super().__init__(nome, idade, cpf, relatorios) # Criamos um objeto pai 


        # E especializamos

        # Atributos Privados
        self.__cargo = cargo 
        self.__salario = salario 

    # Criando os métodos de acesso, leitura. 
    # Pelos quais podemos ler os atributos, é algo como 
    # uma fronteira. 

    @property 
    def cargo(self)-> str:
        return self.__cargo 

    @property 
    def salario(self)-> float:
        return self.__salario 

    # Defindo os getters 
    # Os métodos de acesso voltado a escrita. 

    @cargo.setter 
    def cargo(self, nv_cargo)-> str: 
        self.__cargo = nv_cargo 


    @salario.setter 
    def salario(self, nv_salario)-> None:


        assert type(nv_salario) == float, "O salário deve ser um tipo de dados float"

        if 1400 < nv_salario < 30000: 

            self.__salario = nv_salario  

        else: 
            print("Troca de salário não altorizada!")
            time.sleep(2)
            print("""O salário sempre deve ser um valor entre 
            R$ 1.400, 00 e R$ 30.000,00""")

            time.sleep(2)
            print("Tente novamente!")
