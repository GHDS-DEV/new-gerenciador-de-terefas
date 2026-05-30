from app import adicionar_tarefa
from app import listando_tarefas
from app import removendo_tarefa
from app import concluindo_tarefas
from app import ver_tarefas_concluidas
from app import saindo_do_sistema
from app import menu
from app import limpar_tela

opcoes_validas = ["1", "2", "3", "4", "5"]

while True:
    menu()
    escolha = input("Oque voce deseja fazer? ").strip()

    if escolha == "1":
        adicionar_tarefa()

    elif escolha == "2":
        listando_tarefas()

    elif escolha == "3":
        removendo_tarefa()

    elif escolha == "4":
        concluindo_tarefas()

    elif escolha == "5":
        saindo_do_sistema()
        break

    elif escolha == "6":
        ver_tarefas_concluidas()


limpar_tela()
