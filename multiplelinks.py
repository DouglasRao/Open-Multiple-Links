import webbrowser

try:
	arquivo = str(input("Digite o caminho do arquivo de texto: "))
	links =  open(arquivo)
except IOError:
	print("O arquivo não existe!")
else:
	urls = [url.strip() for url in links.readlines()]
	for url in urls:
		webbrowser.open(url,new=2)
		links.close()
