from webscraping import raspagem_todos_produtos
from insight_openai import gerar_insight

url = "https://www.makeupalley.com/product/searching?CategorySlug=mens-shaving&page="

if __name__ == "__main__":
    todos_produtos = raspagem_todos_produtos(url)
    
    insight_ai = gerar_insight(todos_produtos)
    
    # tabela