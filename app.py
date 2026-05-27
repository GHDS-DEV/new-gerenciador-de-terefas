tarefas = []
tarefas_concluidas = []


def adicionar_tarefa():
    try:
        adicionando_tarefa = input("Qual tarefa voce deseja adicionar? ").strip()
        tarefas.append(adicionando_tarefa)
        print(
            f"A tarefa \n {adicionando_tarefa} foi adicionada a sua lista com sucesso!"
        )
    except ValueError:
        print("Informações inválidas!")


def listando_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")

    for tarefa in enumerate(tarefas):
        print(f"Essas sao todas as suas tarefas: {tarefa}")


def removendo_tarefa():
    for tarefa in enumerate(tarefas):
        try:
            print(f"Essas sao as tarefas disponíveis no sistema: {tarefas} ")
            removendo_tarefa = int(input("Qual tarefa voce deseja remover: ").strip())
            tarefas.pop(removendo_tarefa)
            print(f"A tarefa {removendo_tarefa} foi removida com sucesso da sua lista!")
        except ValueError:
            print("Insira uma informacao valida, essa tarefa nao existe em sua lista!")


def concluindo_tarefas():

    try:
        for tarefa in enumerate(tarefas):
            if not tarefa:
                print("Nenhuma tarefa cadastrada.")
                break

            print(tarefas)
            concluindo_tarefas = input(
                "Informe uma tarefa para marcar como concluida: "
            ).strip()
            tarefas_concluidas.append(concluindo_tarefas)
            tarefas.remove(concluindo_tarefas)
            print(f"A terefa {concluindo_tarefas} foi concluida, parabens!")
    except ValueError:
        print("Insira uma informacao valida, essa tarefa nao existe em sua lista!")


def ver_tarefas_concluidas():
    print(f"Essas sao suas tarefas que ja foram concluidas! {tarefas_concluidas}")


def saindo_do_sistema():
    while True:
        print("Saindo do programa...")
        break


def menu():
    print("=" * 50)
    print("Bem-vindo(a) ao gerenciador de tarefas")
    print()
    print("Escolha conforme a opcao desejada: ")
    print()
    print(
        " [1]Adicionar\n [2]Listar \n [3]Remover \n [4]Concluir \n [5]Sair [6]Ver tarefas concluidas"
    )
    print("=" * 50)


def limpar_tela():
    import os

    os.system("cls")
