from Tarefas.gerenciador_tarefas import GerenciadorTarefas
from Utils.utils import tratar_entrada

class App:
    def __init__(self):
        self.gerenciador = GerenciadorTarefas()

    def exibir_menu(self):
        while True:
            print("\nGerenciador de Tarefas")
            print("1. Adicionar Tarefa")
            print("2. Editar Tarefa")
            print("3. Excluir Tarefa")
            print("4. Marcar como Concluída")
            print("5. Listar Tarefas")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_tarefa()
            elif opcao == '2':
                self.editar_tarefa()
            elif opcao == '3':
                self.excluir_tarefa()
            elif opcao == '4':
                self.marcar_concluida()
            elif opcao == '5':
                self.listar_tarefas()
            elif opcao == '6':
                print("Saindo...")
                break
            else:
                tratar_entrada()

    def adicionar_tarefa(self):
        descricao = input("Digite a descrição da tarefa: ")
        self.gerenciador.adicionar_tarefa(descricao)
        print(f"Tarefa '{descricao}' adicionada!")

    def editar_tarefa(self):
        self.listar_tarefas()
        try:
            index = int(input("Digite o número da tarefa para editar: ")) - 1
            nova_descricao = input("Digite a nova descrição: ")
            self.gerenciador.editar_tarefa(index, nova_descricao)
            print(f"Tarefa {index+1} atualizada para '{nova_descricao}'")
        except (ValueError, IndexError):
            tratar_entrada()

    def excluir_tarefa(self):
        self.listar_tarefas()
        try:
            index = int(input("Digite o número da tarefa para excluir: ")) - 1
            self.gerenciador.excluir_tarefa(index)
            print("Tarefa excluída!")
        except (ValueError, IndexError):
            tratar_entrada()

    def marcar_concluida(self):
        self.listar_tarefas()
        try:
            index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
            self.gerenciador.concluir_tarefa(index)
            print("Tarefa marcada como concluída!")
        except (ValueError, IndexError):
            tratar_entrada()

    def listar_tarefas(self):
        tarefas = self.gerenciador.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in tarefas:
                print(tarefa)

if __name__ == "__main__":
    app = App()
    app.exibir_menu()
