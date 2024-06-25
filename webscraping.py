import requests
from bs4 import BeautifulSoup, Tag

def raspagem_cada_produto(url_produto):
    pagina_produto = requests.get(url_produto)
    soup_pagina_produto = BeautifulSoup(pagina_produto.text, "lxml")
    
    tag_h1 = soup_pagina_produto.find("h1", class_="mb-1")
    tag_nome = tag_h1.find("a") if tag_h1 else None
    nome = tag_nome.text.strip() if tag_nome else "No name found"
    
    tag_classificacao = soup_pagina_produto.find("h3", class_="rating-value ml-1 mr-3")
    classificacao = float(tag_classificacao.text.strip()) if tag_classificacao else 0.0
    
    tag_avaliacoes = soup_pagina_produto.find("a", class_="overall-rating")
    total_avaliacoes = int(tag_avaliacoes.text.split()[0]) if tag_avaliacoes else 0
    
    avaliacoes = soup_pagina_produto.find_all("div", class_="product-review-text")
    conteudo_avaliacoes = []
    
    for avaliacao in avaliacoes[:5]:
        if isinstance(avaliacao, Tag):
            tag_texto_avaliacao = avaliacao.find("div", class_="__ReviewTextReadMoreV2__")
            texto_avaliacao = tag_texto_avaliacao.get("data-text", "").strip() if tag_texto_avaliacao else "No review text found"
            
            tag_classificacao_avaliacao = avaliacao.find_previous_sibling("div").find("span", class_="rating-value")
            classificacao_avaliacao = float(tag_classificacao_avaliacao.text.strip()) if tag_classificacao_avaliacao else 0.0
            
            conteudo_avaliacoes.append(f"Classificação: {classificacao_avaliacao}, Avaliação: {texto_avaliacao}")
    
    return {
        'Nome': nome,
        'Classificação': classificacao,
        'Total de Avaliações': total_avaliacoes,
        'Conteúdo das Avaliações': conteudo_avaliacoes
    }

def raspagem_todos_produtos(url_site):
    numero_pagina = 1
    todos_produtos = []
    
    while numero_pagina <= 5:
        url_pagina = url_site + str(numero_pagina)
        pagina_atual = requests.get(url_pagina)
        soup_pagina_atual = BeautifulSoup(pagina_atual.text, "lxml")
        produtos_pagina = soup_pagina_atual.find_all("article", class_="item product-result-row")
        
        for produto in produtos_pagina:
            if not isinstance(produto, Tag):
                print(f"Unexpected object type: {type(produto)}")
                continue
            
            tag_link_produto = produto.find("a", class_="item-name")
            if tag_link_produto:
                url_produto = "https://www.makeupalley.com" + tag_link_produto['href']
                dados_produto = raspagem_cada_produto(url_produto)
                todos_produtos.append(dados_produto)
            else:
                print(f"Product link not found for a product on page {numero_pagina}")
        
        numero_pagina += 1
    
    return todos_produtos