FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml ./

RUN uv pip install --system .

COPY ./app /app/app
COPY .env /app/.env

EXPOSE 8000

# host 0.0.0.0 para que a porta seja acessível de fora do contêiner
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]