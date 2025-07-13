# EXECUTAR => uvicorn main:app --reload

# Importa a classe FastAPI para criar a aplicação web e HTTPException para erros HTTP
from fastapi import FastAPI, HTTPException
# Importa BaseModel do Pydantic para validação de dados
from pydantic import BaseModel
# Importa List para tipagem de listas
from typing import List
# Importa status para definir códigos de status HTTP
from fastapi import status

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define o modelo de dados para uma tarefa (Task)
class Task(BaseModel):
    id: int  # Identificador único da tarefa
    title: str  # Título ou descrição da tarefa
    completed: bool = False  # Status de conclusão da tarefa (padrão: False)

# Lista que irá armazenar todas as tarefas em memória
tasks: List[Task] = []

# Endpoint para obter todas as tarefas cadastradas
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks  # Retorna a lista de tarefas

# Endpoint para criar uma nova tarefa
@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    tasks.append(task)  # Adiciona a nova tarefa à lista
    return task  # Retorna a tarefa criada

# Endpoint para alternar o status de conclusão de uma tarefa pelo id
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int):
    for task in tasks:  # Percorre todas as tarefas
        if task.id == task_id:  # Se encontrar a tarefa com o id informado
            task.completed = not task.completed  # Alterna o status de conclusão
            return task  # Retorna a tarefa atualizada
    # Se não encontrar a tarefa, retorna erro 404
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint para deletar uma tarefa pelo id
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks  # Indica que irá modificar a variável global tasks
    tasks = [task for task in tasks if task.id != task_id]  # Remove a tarefa com o id informado
    return {"message": "Task deleted"}  # Retorna mensagem de sucesso