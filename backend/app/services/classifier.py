import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# carrega as variaveis de ambiente
load_dotenv()

# configura a API do Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# prompt para a LLM.
PROMPT_TEMPLATE = """
<instructions>
  Sua única função é atuar como um analisador de e-mails. Você deve analisar o texto fornecido dentro das tags <email_text> e retornar um objeto JSON.

  O objeto JSON deve conter as seguintes chaves:
  1. "classification": Classifique o e-mail como "Produtivo" ou "Improdutivo".
     - "Produtivo": E-mails que exigem uma ação, como faturas, solicitações de trabalho, agendamentos, relatórios importantes.
     - "Improdutivo": E-mails de marketing, newsletters, spam, notificações de redes sociais que não exigem ação imediata.
  2. "justification": Uma frase curta (máximo 15 palavras) explicando o motivo da classificação.
  3. "suggested_reply": Sugira uma resposta curta e educada apropriada para a classificação. Se for improdutivo, a resposta pode ser "Nenhuma resposta necessária.".
</instructions>

<email_text>
{email_text}
</email_text>
"""


async def classify_email_with_gemini(text: str) -> dict:
    """
    Envia o texto do e-mail para a LLM (Gemini) e retorna a classificação e a resposta sugerida. # NOQA
    """
    if not text.strip():
        raise ValueError("O texto do e-mail não pode estar vazio.")

    try:
        model = genai.GenerativeModel(
            "gemini-1.5-flash-latest",
            generation_config={"response_mime_type": "application/json"},
        )

        prompt = PROMPT_TEMPLATE.format(email_text=text)

        response = await model.generate_content_async(prompt)

        response_text = response.text.strip()

        # Converte a string de JSON em dicionário
        result = json.loads(response_text)

        return result

    except Exception as e:
        print(f"Erro ao chamar a API do Gemini ou processar a resposta: {e}")
        raise ConnectionError("Falha ao comunicar com o serviço de IA.")
