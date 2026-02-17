from __future__ import annotations 
from typing import List
from class_funcoes import Funcoes 
from datetime import datetime 

funcoes = Funcoes()

class Relatorio: 

    """
        Esta classe define os moldes do objeto relatório, 
        o qual se trata de anotações de comportamentos que 
        merecem destaque, positivo ou negativo. 

    """

    relatorios_gerados: List[Relatorio] = []

    def __init__(self, id_colab: str= "00000-00", nome_colab: str= "nome",
                idade_colab: int= 0, cpf_colab: str= "00000000-00", anotacao: str= ""):

    # Métodos privados 
        self.__id_relatorio = funcoes.gerar_id()
        self.__data_relatorio = datetime.now()
        self.__id_colab = id_colab
        self.__nome_colab = nome_colab 
        self.__idade_colab = idade_colab 
        self.__cpf_colab = cpf_colab 
        self.__anotacao = anotacao
        self.__teor = True 
        # Adicionando ao relatório relatório 
        Relatorio.relatorios_gerados.append(self)

    # Criando o encapsulamento, o encapsulamento e como o oficial de fronteira, 
    # que impede o acesso irrestrito. Dessa forma, e possível limitar-mos as maneiras 
    # de leitura, os getters, e de escrita, os setters. 

    # Getters - Leitura dos atributos. 
    @property 
    def id_relatorio(self)-> str:
        return self.__id_colab 

    @property 
    def data_relatorio(self)-> datetime:
        return self.__data_relatorio

    @property 
    def id_colab(self)-> str: 
        return self.__id_colab 

    @property
    def nome_colab(self)-> str: 
        return self.__nome_colab 

    @property 
    def idade_colab(self)-> int:
        return self.__idade_colab 

    @property 
    def cpf_colab(self)-> str:
        return self.__cpf_colab 

    @property 
    def teor(self)-> bool: 
        """O teor no caso é o tipo de conteúdo que o relatório carrega, 
        se trata-se de algo bom, um elogio, teor True, do contrário teor False"""
        return self.__teor 

    # Utilizando um método mágico, dunder ou double underscore, para 
    # exibir algo diferente do indereço de memória, uma string, quando 
    # o objeto for impresso. 


    def __repr__(self):
        return f"""Relatório Id: {self.__id_relatorio}| Colaborador: {self.__nome_colab}| Idade: {self.__idade_colab}"""



    # Método que exibe o relatório. 

    def mostrar_relatorio(self)-> str:

        return f"""
ID Relatório: {self.__id_relatorio}
Nome Colaborador: {self.__nome_colab}                                                      ID:   {self.__id_colab}
Idade:            {self.__idade_colab}                                                        CPF:  {self.__cpf_colab}
================================================================================================
        
Anotação:                                                       Data: {self.__data_relatorio}
        {self.__anotacao}

================================================================================================
        """


def main():

    # Testando a classe. 
    # Criando uma instância Relatório. 

    relatorio_a = Relatorio("0000012-5",        # E agora temos o nosso próprio objeto 
                            "Lucas",            # Particular, detentor de seus próprios atributos 
                            20,                 # e métodos. 
                            "000.000.000-00",
                            "O Lucas é um ótimo engenheiro de Deep-Learning!"
                            )
    

    print(relatorio_a.mostrar_relatorio())

    print(relatorio_a)


# main()