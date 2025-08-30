from pydantic import BaseModel


# Modelo para a resposta da API
class ClassificationResponse(BaseModel):
    classification: str
    suggested_reply: str
    filename: str | None = None
