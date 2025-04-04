class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida  

    def __str__(self):
        return(f'{self.descricao} - {"Concluída" if self.concluida else "Pendente"}')
