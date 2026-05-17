lista_armazena_tarefa = []

def adiciona_tarefa(lista):
    nome = input("Digite o nome da tarefa: ")
    
    descricao = input("Digite a descrição da tarefa: ")
    
    dicionario = {}

    dicionario["nome"] = f"{nome}: {descricao}"

    dicionario["concluida"] = False

    lista.append(dicionario)

def lista_tarefa(lista):
    for item, tarefa in enumerate(lista):
        print(f"{item + 1}: {tarefa["nome"]}, {tarefa["concluida"]}")

def remove_tarefa(lista, indice):
    if type(indice) == str:
        indice = int(indice)
    indice = indice - 1
    lista.pop(indice)

def concluir(lista, indice):
    if type(indice) == str:
        indice = int(indice)
    indice = indice - 1
    lista[indice]["concluida"] = True
