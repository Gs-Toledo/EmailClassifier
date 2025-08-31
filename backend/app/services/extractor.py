from fastapi import UploadFile
import fitz


async def extract_text_from_file(file: UploadFile) -> str:
    """Extrai texto de um arquivo UploadFile, aceita PDF e TXT."""

    file_extension = file.filename.split(".")[-1].lower()

    if file_extension == "pdf":
        pdf_bytes = await file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text

    elif file_extension == "txt":
        txt_bytes = await file.read()
        return txt_bytes.decode("utf-8")

    else:
        try:
            text_bytes = await file.read()
            return text_bytes.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError(
                f"Formato de arquivo não suportado: {file_extension}"
            )  # Noqa
