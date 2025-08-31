from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ClassificationResponse
from .services import extractor, classifier

app = FastAPI(title="API Email Classifier com IA")

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

    if not email_file and not email_text:
        return {"error": "Nenhum arquivo ou texto foi enviado."}

    text_to_process = ""
    filename = None

    try:
        if email_file:
            filename = email_file.filename
            text_to_process = await extractor.extract_text_from_file(email_file) # noqa
        elif email_text:
            filename = "Texto Direto"
            text_to_process = email_text

        if not text_to_process.strip():
            raise HTTPException(
                status_code=400, detail="O conteúdo do e-mail está vazio."
            )

        analysis_result = await classifier.classify_email_with_gemini(text_to_process) # noqa

        return ClassificationResponse(
            filename=filename,
            classification=analysis_result.get("classification", "Erro"),
            suggested_reply=analysis_result.get(
                "suggested_reply", "Não foi possível sugerir uma resposta."
            ),
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        print(f"Erro inesperado no endpoint: {e}")
        raise HTTPException(
            status_code=500, detail="Ocorreu um erro interno no servidor."
        )
