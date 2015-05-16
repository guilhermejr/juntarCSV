Hoje Camila (http://www.camilaoliveira.net) me perguntou se eu conhecia algum
programa que juntava arquivos CSV. Como eu não conheço, imediatamente comecei a
fazer esse Script Python para resolver o problema dela. Ele simplesmente lê
todos os arquivos CSV de uma pasta e junta todos em um só, antes ele pergunta se
é para retirar as primeiras linhas (Título) a partir do segundo arquivo.

Como utilizo OS X Yosemite esse Script Python foi desenvolvido e testado para
ele, não sei se vai funcionar em outras versões do OS X nem se vai funcionar em
alguma distribuição Linux ou no MS Windows.

Para executa-lo::

	$ python juntarCSV.py /caminho/da/pasta/

Depois do processamento será informado a quantidade de arquivos juntados e o
total de linhas do novo arquivo. O nome do arquivo gerado será arquivo.csv
	
Dúvidas e Sugestões favor mandar um e-mail falecom@guilhermejr.net
