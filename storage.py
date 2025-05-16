import json
import os

TASKS_FILE = 'data/tasksstorage.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:  # arquivo vazio
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Arquivo JSON corrompido, iniciando lista vazia.")
        return []

def save_tasks(tasks):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
