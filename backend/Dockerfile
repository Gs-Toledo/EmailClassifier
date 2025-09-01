FROM python:3.12

WORKDIR /app

RUN pip install uv

COPY pyproject.toml ./

RUN uv pip sync --system pyproject.toml

COPY ./app /app/app

EXPOSE 8000

# host 0.0.0.0 para que a porta seja acessível de fora do contêiner
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]