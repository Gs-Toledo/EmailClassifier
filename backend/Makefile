.PHONY: help install dev

help:
	@echo "Comandos disponíveis:"
	@echo "  make install   - Cria o ambiente virtual e instala as dependências (usa o uv)."
	@echo "  make dev       - Inicia o servidor de desenvolvimento com auto-reload."

install:
	@echo "Configurando ambiente virtual com uv..."
	uv venv
	@echo "Instalando dependências do pyproject.toml..."
	uv pip install -e .
	@echo "Ambiente pronto! Use 'source .venv/bin/activate' ou 'uv shell' para ativá-lo."

dev:
	@echo "Iniciando servidor de desenvolvimento em http://localhost:8000"
	# O 'uv run' executa o comando dentro do ambiente virtual detectado
	uv run uvicorn app.main:app --reload