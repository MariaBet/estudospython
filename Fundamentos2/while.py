#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
while
"""
numero_da_sorte = 33
tentativa = 5

while tentativa > 0:
    print("Tentativa: ", tentativa)
    numero_da_sorte = int(input("Digite um numero da sorte: "))
    tentativa -= 1
    if numero_da_sorte == 33:
        print("Voce acertou, seu premio eh de R$1000,00 " '\n')
        break
    else:
        print("Voce errou nao recebeu nenhum valor" '\n')

print("Fim da sorte!")
