from bs4 import BeautifulSoup
import re
import requests

# Verificando se o site permite ser raspado
url = "https://www.amazon.com.br/"

# Jogando o conteúdo HTML na page
page = requests.get(url)

# Mensagem 401 (?)
print(page.status_code)