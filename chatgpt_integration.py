# chatgpt_integration.py

import openai
from config import OPENAI_API_KEY

# Configurar a chave da API
openai.api_key = OPENAI_API_KEY

def obter_sugestoes(modelo_descricao):
    prompt = (
        "Sou um desenvolvedor trabalhando em um modelo de Machine Learning com a seguinte descrição:\n"
        f"{modelo_descricao}\n"
        "Quais melhorias você sugere para aprimorar este modelo?"
    )
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    sugestoes = resposta.choices[0].message['content'].strip()
    return sugestoes
