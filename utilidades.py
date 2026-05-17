import random
from datetime import date

def retorna_data():
    data_atual = date.today()
    return data_atual

def calcula_percentual(lista):
    if len(lista) == 0:
        return 0 # evita divisão por 0
    
    tarefas_concluidas = 0
    for tarefa in lista:
        if tarefa["concluida"] == True:
            tarefas_concluidas += 1
    
    percentual = (tarefas_concluidas / len(lista)) * 100
    return percentual


def sorteia_tarefa(lista):
    tarefa_sorteada = random.choice(lista)
    return tarefa_sorteada
