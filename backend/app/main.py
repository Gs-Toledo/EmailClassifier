import time
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ClassificationResponse

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:5173",  # frontend
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Status": "API do Email Classifier esta rodando!"}


@app.post("/api/classify", response_model=ClassificationResponse)
async def classify_email(
    email_file: UploadFile | None = File(None),
    email_text: str | None = Form(None),  # NOQA
):
    """
    Recebe um email (via upload de arquivo ou texto)
    e retorna uma classificação mockada.
    """

    # Fluxo da LLM ainda não implementada, sleep para testar
    time.sleep(2)

    if not email_file and not email_text:
        return {"error": "Nenhum arquivo ou texto foi enviado."}

    # Mock
    if email_file and "fatura" in email_file.filename.lower():
        return ClassificationResponse(
            filename=email_file.filename,
            classification="Produtivo",
            suggested_reply="Prezados, recebemos a fatura. O pagamento será processado em breve. Atenciosamente.",  # noqa
        )
    else:
        return ClassificationResponse(
            filename=email_file.filename if email_file else "Texto Direto",
            classification="Improdutivo",
            suggested_reply="Agradecemos o contato. Arquivaremos esta mensagem para referência futura.",  # noqa
        )
