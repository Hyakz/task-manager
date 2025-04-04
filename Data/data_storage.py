import json
from Tarefas.tarefas import Tarefa

def carregar_tarefas(arquivo="tarefas.json"):
    try:
        with open(arquivo, 'r') as file:
            tarefas_data = json.load(file)
            return [Tarefa(t['descricao'], t['concluida']) for t in tarefas_data]
    except FileNotFoundError:
        return []

def salvar_tarefas(arquivo, tarefas):
    tarefas_data = [{'descricao': t.descricao, 'concluida': t.concluida} for t in tarefas]
    with open(arquivo, 'w') as file:
        json.dump(tarefas_data, file, indent=4)