# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:18:56 2021

@author: Aleff
"""

class Calculadora:
    def __init__(self):
        self.__lista = []
        
    def add_numero(self, numero):
        self.__lista.append(numero)
    
    def get_hist(self):
        return self.__lista[-1]
    
    def soma(self):
        result = self.__lista[-1] + self.__lista[-2]
        self.__lista.append(result)
        
    def sub(self):
        self.__lista[0] -= self.__lista[-1]
        self.__lista.append(self.__lista[0])
        
    def mult(self):
        self.__lista[0] *= self.__lista[-1]
        self.__lista.append(self.__lista[0])
        
    def div(self):
        self.__lista[0] //= self.__lista[-1]
        self.__lista.append(self.__lista[0])

a = Calculadora()

on = True

while (on):
    for x in range(2):
        a.add_numero(int(input("Digite um número: ")))
        
    operação = str(input("Digite a operação: "))
    
    if (operação == "soma"):
        a.soma()
        print(a.get_hist())
    elif (operação == "sub"):
        a.sub()
        print(a.get_hist())
    elif (operação == "mult"):
        a.mult()
        print(a.get_hist())
    elif (operação == "div"):
        a.div()
        print(a.get_hist())
    else:
        print("Operação não existente!")