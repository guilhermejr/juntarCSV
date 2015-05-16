#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from glob import glob

def main(): 

	# --- Verifica a quantidade de parâmetros ---
	qtdParametros = len(sys.argv)
	if qtdParametros != 2:
		os.system('clear')
		print("Uso: python juntarCSV.py /caminho/da/pasta/")
		sys.exit(1)

	# --- Caminho da pasta com os arquivos a serem juntados ---
	pasta = sys.argv[1]

	# --- Verifica se a pasta realmente existe ---
	if not os.path.isdir(pasta):
		os.system('clear')
		print("Não foi possível encontrar a pasta \"%s\"." % pasta)
		sys.exit(1)

	# --- Pergunta de deseja que retire a primeira linha ---
	while True:
		os.system('clear')
		opcao = raw_input("Deseja retirar a primeira linha (Títulos) a partir do segundo arquivo? (s/n) ")

		if opcao.lower() == "s":
			titulo = False
			break

		if opcao.lower() == "n":
			titulo = True
			break

	# --- Variáveis de controle para saber quantos arquivos e linhas foram juntadas ---
	qtdArquivos = 0;
	qtdLinhas = 0;

	# --- Cria o arquivo que vai juntar todos os arquivos CSV ---
	with open("arquivo.csv", "a") as arquivo:
		# --- Lê todos os arquivos CSV da pasta e joga no arquivo criado ---
	    for arquivoCSV in glob(pasta + "*.csv"):
	    	qtdArquivos += 1
	    	primeiraLinha = True
	        for linha in open(arquivoCSV, "r"):
	        	if not titulo and qtdArquivos > 1 and primeiraLinha:
	        		primeiraLinha = False
	        		continue
	        	qtdLinhas += 1
	        	arquivo.write(linha)

	# --- Mensagem de saída ---
	os.system('clear')
	print("Foram juntados "+ str(qtdArquivos) +" arquivos e um total de "+ str(qtdLinhas) +" linhas.")

if __name__ == "__main__":
	main()