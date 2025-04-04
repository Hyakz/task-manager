from Tarefas.tarefas import Tarefa
from Data.data_storage import carregar_tarefas, salvar_tarefas

class GerenciadorTarefas:
    def __init__(self, arquivo="tarefas.json"):
        self.arquivo = arquivo
        self.tarefas = carregar_tarefas(self.arquivo)

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)  
        self.tarefas.append(nova_tarefa)
        salvar_tarefas(self.arquivo, self.tarefas)

    def editar_tarefa(self, index, nova_descricao):
        if 0 <= index < len(self.tarefas):
            self.tarefas[index].descricao = nova_descricao
            salvar_tarefas(self.arquivo, self.tarefas)
        else:
            raise IndexError("Tarefa não encontrada")

    def excluir_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            del self.tarefas[index]
            salvar_tarefas(self.arquivo, self.tarefas)
        else:
            raise IndexError("Tarefa não encontrada")

    def concluir_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            self.tarefas[index].concluida = True
            salvar_tarefas(self.arquivo, self.tarefas)
        else:
            raise IndexError("Tarefa não encontrada")

    def listar_tarefas(self):
        return [str(tarefa) for tarefa in self.tarefas]
