# 📧 Email Classifier AI

🔗 **Link do APP:** [https://email-classifier-mu.vercel.app](https://email-classifier-mu.vercel.app)

---

## 📄 Descrição
O **Email Classifier AI** é uma aplicação web full-stack que utiliza **Inteligência Artificial** para analisar o conteúdo de e-mails.  
O usuário pode **colar o texto de um e-mail** ou **fazer upload de um arquivo** (`.txt` ou `.pdf`), e a aplicação irá:

- Classificar o e-mail como **"Produtivo"** ou **"Improdutivo"**.  
- Sugerir uma **resposta automática apropriada** para o contexto.  
---

## ✨ Tecnologias Utilizadas

A aplicação é dividida em dois componentes principais:

### 🔹 Frontend (Interface Web)
- **Framework:** Vue.js 3 (Composition API)  
- **Linguagem:** TypeScript  
- **Build Tool:** Vite  
- **Estilização:** Tailwind CSS  
- **Cliente HTTP:** Axios
- **Containerização:** Docker & Docker Compose  
- **Hospedagem:** Vercel  

### 🔹 Backend (API de IA)
- **Framework:** FastAPI  
- **Linguagem:** Python 3.12  
- **Modelo de IA:** Google Gemini 1.5 Flash  
- **Gerenciamento de Pacotes:** [uv](https://github.com/astral-sh/uv) (via `pyproject.toml`)  
- **Containerização:** Docker & Docker Compose  
- **Hospedagem:** Render  

---

## 🚀 Rodando o Projeto Localmente

Para executar a aplicação completa na sua máquina, é necessário ter o **Docker** e o **Docker Compose** instalados.

### 1. Clone o Repositório
```bash
git clone https://github.com/Gs-Toledo/EmailClassifier.git
cd EmailClassifier
```

### 2. Configure as Variáveis de Ambiente
O backend precisa de uma **chave de API** para se comunicar com o **Google Gemini**.

- Vá até a pasta `backend`.  
- Crie uma cópia do arquivo `.env.example` (se existir) ou crie um novo arquivo `.env`.  
- Adicione sua chave do **Google AI Studio**:  

Arquivo: `backend/.env`
```env
GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
```
Atenção: O arquivo .env é local e não deve ser enviado para o repositório do Git.



### 3. Suba os Contêineres com Docker Compose
Na raiz do projeto, execute o seguinte comando. Ele irá construir as imagens do frontend e do backend e iniciar os contêineres.

Arquivo: `root`
```bash
docker-compose up --build
```
O --build é importante na primeira vez para garantir que as imagens sejam criadas a partir dos Dockerfiles.

### 4. Acesse a Aplicação
Após os contêineres subirem com sucesso:

Frontend: Acesse http://localhost:5173 no seu navegador.

Backend API: A API estará disponível em http://localhost:8000.

Documentação da API: Você pode ver a documentação interativa do FastAPI em http://localhost:8000/docs.

### 5. Para Parar a Aplicação
No terminal onde o docker-compose está rodando, pressione Ctrl + C. Para garantir que os contêineres e as redes sejam removidos, execute:
```bash
docker-compose down
```


