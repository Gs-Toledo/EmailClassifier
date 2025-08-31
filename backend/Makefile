.PHONY: help install dev clean lint format

VENV_DIR=.venv

help:
	@echo "Comandos disponíveis:"
	@echo "  make install   - Cria o ambiente virtual e instala as dependências (usa o uv)."
	@echo "  make dev       - Inicia o servidor de desenvolvimento com auto-reload."
	@echo "  make lint      - Verifica o código por erros e problemas de estilo com o Ruff."
	@echo "  make format    - Formata o código automaticamente com o Ruff."
	@echo "  make clean     - Remove o ambiente virtual (.venv)."

install:
	@echo "Configurando ambiente virtual com uv..."
	uv venv
	@echo "Instalando dependências do pyproject.toml..."
	uv pip sync pyproject.toml
	@echo "Ambiente pronto! Use 'source $(VENV_DIR)/bin/activate' ou 'uv shell' para ativá-lo."

dev:
	@echo "Iniciando servidor de desenvolvimento em http://localhost:8000"
	uv run uvicorn app.main:app --reload

lint:
	@echo "Verificando o código com o Ruff..."
	uv run -- ruff check .

format:
	@echo "Formatando o código com o Ruff..."
	uv run -- ruff format .

clean:
	@echo "Removendo ambiente virtual..."
	rm -rf $(VENV_DIR)
	@echo "Limpeza concluída."