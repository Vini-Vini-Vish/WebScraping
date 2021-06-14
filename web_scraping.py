import requests

#Tenha instalado o compilador de python no computador
    #instale as dependencias 
        # python -m pip install requests
        # python -m pip install beautifulsoup4
        # python -m pip install pandas

# Para indicar o PDF escolhido, adicione o link entre aspas duplas.
file_url = "https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao_tiss_componente_organizacional_202104.pdf"
 
r = requests.get(file_url, stream = True)

#Ente as aspas duplas escreva o nome desejado para o PDF. 
with open("TISS.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)

