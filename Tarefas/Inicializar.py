from Tarefas.gerenciador_tarefas import GerenciadorTarefas
from Utils.utils import Utils

class Inicializar:
    def __init__(self):
        self.gerenciador = GerenciadorTarefas()
        self.utils = Utils()

    def exibir_menu(self):
        while True:
            print("\nGerenciador de Tarefas")
            print("1 - Adicionar Tarefa")
            print("2 - Editar Tarefa")
            print("3 - Excluir Tarefa")
            print("4 - Marcar como Concluída")
            print("5 - Listar Tarefas")
            print("6 - Sair")
            
            try:
                opcao = input("Escolha uma opção: ")
                self.processar_opcao(opcao)
            except KeyboardInterrupt:
                self.utils.tratar_interrupcao()

    def processar_opcao(self, opcao):
        opcoes = {
            '1': self.adicionar_tarefa,
            '2': self.editar_tarefa,
            '3': self.excluir_tarefa,
            '4': self.marcar_concluida,
            '5': self.listar_tarefas,
            '6': self.sair
        }
        
        try:
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.utils.tratar_entrada()
        except KeyboardInterrupt:
            self.utils.tratar_interrupcao()

    def adicionar_tarefa(self):
        descricao = input("Digite a descrição da tarefa: ")
        self.gerenciador.adicionar_tarefa(descricao)
        print(f"Tarefa '{descricao}' adicionada!")

    def editar_tarefa(self):
        index = self.obter_indice_tarefa("editar")
        if index is not None:
            nova_descricao = input("Digite a nova descrição: ")
            self.gerenciador.editar_tarefa(index, nova_descricao)

            print(f"Tarefa {index+1} atualizada para '{nova_descricao}'")

    def excluir_tarefa(self):
        index = self.obter_indice_tarefa("excluir")
        if index is not None:
            self.gerenciador.excluir_tarefa(index)
            print("Tarefa excluída!")

    def marcar_concluida(self):
        index = self.obter_indice_tarefa("marcar como concluída")
        if index is not None:
            self.gerenciador.concluir_tarefa(index)
            print("Tarefa marcada como concluída!")

    def listar_tarefas(self):
        tarefas = self.gerenciador.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in tarefas:
                print(tarefa)

    def obter_indice_tarefa(self, acao):
        self.listar_tarefas()
        try:
            index = int(input(f"Digite o número da tarefa para {acao}: ")) - 1
            return index
        except (ValueError, IndexError):
            self.utils.tratar_entrada()
            return None

    def sair(self):
        print("Saindo...")
        exit()

