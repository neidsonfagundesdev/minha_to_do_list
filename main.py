import tarefas
import utilidades

minha_lista = []

while True:
    print("\n1 Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Concluir tarefa")
    print("5 - Mostrar porcentagem concluida")
    print("6 - Sortear tarefa aleatória")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefas.adiciona_tarefa(minha_lista)
    elif opcao == "2":
        tarefas.lista_tarefa(minha_lista)
    elif opcao == "3":
        indice = int(input("Número: "))
        tarefas.remove_tarefa(minha_lista, indice)
    elif opcao == "4":
        indice = int(input("Número: "))
        tarefas.concluir(minha_lista,indice)
    elif opcao == "5":
        porcentagem = utilidades.calcula_percentual(minha_lista)
        print(f"Progresso: {porcentagem:.1f}% das tarefas concluidas")
    elif opcao == "6":
        sorteio = utilidades.sorteia_tarefa(minha_lista)
        print(f"A tarefa sorteada é: {sorteio["nome"]}")            
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida")

