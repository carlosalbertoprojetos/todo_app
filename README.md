# Tarefas Simples - API FastAPI

Esta aplicação fornece uma API básica de gerenciamento de tarefas (to-do list).

**Objetivo:** Criar uma lista de tarefas com operações básicas de CRUD (Create, Read, Update, Delete).

---

## Funcionalidades
- Adicionar uma nova tarefa
- Listar todas as tarefas
- Atualizar o status de conclusão da tarefa
- Deletar uma tarefa

---

## Dependências
- `fastapi`: Framework principal da aplicação.
- `uvicorn`: Servidor ASGI para rodar localmente.

---

## Instalação e configuração

### 1. Clone ou acesse a pasta do projeto
```bash
cd todo_app_junior
```

### 2. (Opcional) Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

---

## Como executar
```bash
uvicorn main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Requisitos

- Python 3.8 ou superior
- pip instalado

---

## Interface Swagger

A FastAPI gera uma interface interativa para testar todos os endpoints automaticamente, acessível em:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)