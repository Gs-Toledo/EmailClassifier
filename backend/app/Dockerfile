FROM python:3.12-slim

# diretório de trabalho dentro do contêiner
WORKDIR /app

# Define variaveis de ambiente para otimização do Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

# instala dependências
RUN uv pip install --system --frozen

COPY ./app /app/app

EXPOSE 8000

# host 0.0.0.0 para que a porta seja acessível de fora do contêiner
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]