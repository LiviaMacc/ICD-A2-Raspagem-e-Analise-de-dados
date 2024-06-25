from openai import OpenAI

api_key = "API_KEY"
client = OpenAI(api_key=api_key)

def gerar_insight(todos_produtos):
    pergunta_user = f'''Você é um especialista em produtos de barbear:: {todos_produtos}'''
    
    prompt = [{"role": "user", "content": pergunta_user}]
    
    resposta_assistant = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        messages = prompt,
        max_tokens = 1000,
        temperature = 0
    )
    
    resposta_assistant = resposta_assistant.choices[0].message.content
    
    return resposta_assistant