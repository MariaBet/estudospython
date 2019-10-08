#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Importação de modulos"""
import os
import sys

# Obtendo informações do que os modulos possuem
print('Informações do modulo OS.:\n',dir(os),'\n\n\n')
print('Informações do modulo SYS.:\n',dir(sys),'\n\n\n')
print('O que é a função platform do modulo sys.:\n',dir(sys.platform),'\n\n\n')

# Pega qual é o SO
so = sys.platform
print('O Sistema Operacional atual é.:',so,'\n\n\n\n')



### AQUI COMEÇA O PROGRAMA DE FATO


"""FUNÇÕES"""

""""Função Main"""
def main():
    print('Lista de filmes favoritos\n')

    while True:
        print('\nEscolha uma das opções abaixo\n')
        print('1 - Ver a lista')
        print('2 - Adicionar filmes na lista')
        print('3 - Excluir filmes da lista')
        print('0 - Sair\n')
        opcao = input('Entre com o número da opcao.: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adicionar()
        elif (opcao == '3'):
            excluir()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opcao inválida')


""""Função Visualizar Lista"""
def ver():
    # Usado a função path.isfile do modulo OS, para verificar
    # a existencia do arquivo de lista
    if os.path.isfile('/home/eduardo/github/EstudosPython/Arquivos_de_Texto/'
                        'filmes_chacal.txt') == True:

        print('Lista de filmes existente\n')

        # Abrir arquivo no modo leitura (r)
        arquivo = open('filmes_chacal.txt', 'r')
        # Lendo o conteudo do arquivo com a função read
        print(arquivo.read())
        # Chamando o menu principal novamente
        main()

    else:
        print('A lista de filmes não existe, volte ao menu e escolha outra opção')
        main()


""""Função Adicionar Lista"""
def adicionar():
    if os.path.isfile('/home/eduardo/github/EstudosPython/Arquivos_de_Texto/'
                        'filmes_chacal.txt') == True:
        print('Lista de filmes existente\n')

        # Abrir arquivo no modo append (a)
        # O modo append preserva o conteudo existe do arquivo caso ele
        # já exista. Diferente do modo (w) que exclui o conteudo e adiciona
        # um novo conteudo.
        arquivo = open('filmes_chacal.txt', 'a')

        conteudo = '0'
        while conteudo != 'fim':
            conteudo = input('Digite o nome de um filme.: ')
            if conteudo == 'fim':
                break
            arquivo.write(conteudo + '\n')
            arquivo.write('\n')

        # Fechando arquivo p/ salvar
        arquivo.close()
        main()

    else:
        print('A lista de filmes não existe, adicione novos filmes e uma lista'
                'sera criada pra você!')

        arquivo = open('filmes_chacal.txt', 'w')

        conteudo = '0'
        while conteudo != 'fim':
            conteudo = input('Digite o nome de um filme.: ')
            if conteudo == 'fim':
                break
            arquivo.write(conteudo)
            arquivo.write('\n')

            # Fechando arquivo p/ salvar
            arquivo.close()


""""Função Excluir Lista"""
def excluir():
    if os.path.isfile('/home/eduardo/github/EstudosPython/Arquivos_de_Texto/'
                        'filmes_chacal.txt') == True:

        ver()
        remover = input('Digite o nome do filme p/ excluir da lista.: ')

        # Usado o metodo del(lista[conteudo]) para remover um item da lista
        del(filmes[remover])
        ver()

    main()

main()