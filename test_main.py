# EXECUTAR => pytest -v
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tasks_initially_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_create_task():
    task = {"id": 1, "title": "Test Task", "completed": False}
    response = client.post("/tasks", json=task)
    assert response.status_code == 200
    assert response.json() == task

def test_get_tasks_after_creation():
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Test Task"
    assert tasks[0]["completed"] is False

def test_update_task():
    response = client.put("/tasks/1")
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["id"] == 1
    assert updated_task["completed"] is True

def test_update_task_not_found():
    response = client.put("/tasks/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted"}
    # Confirm task is deleted
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [] 