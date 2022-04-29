from rpg.combat import start_fight
from rpg.monster import all_monsters
from rpg.player import Player
from rpg.vocation import get_vocation



# Rodar o nosso projeto:
# python -m rpg
def main():
    menu()

    player_name = input("What's your name? ")
    player_vocation = get_vocation()
    player = Player(name=player_name, vocation=player_vocation)
    start_fight(player, all_monsters[0])

    # -------- TAREFA, MEU IRMÃO, 1 --------
    # e por fim, uma opção de passar o turno (sem ação nenhuma por hora (NOOP))
    # como alternativa, pode seguir o exemplo da opção Exit do menu do jogo.

    # -------- TAREFA, MEU IRMÃO, 2 --------
    # Corrigir os prints do jogo e deixar mais apresentável
    # todos os prints, T O D O S
    # T
    # O
    # D
    # O
    # S

    # -------- TAREFA, MEU BROTHER, OPCIONAL --------
    # Lê aí: https://docs.python.org/3/tutorial/classes.html
    # Lê aqui tb: https://cbea.ms/git-commit/


def menu():
    print("Welcome to the RPG\n")
    print("Select the options:")
    print("1. Start the game")
    print("2. Exit\n")

    while True:
        choice = int(input("Select the number: "))

        if choice == 2:
            print("Bye bye")
            exit()

        if choice == 1:
            print("Starting the game...\n\n")
            break

        # verificando se a opção do usuário está entre 1 e 2
        #                 () <- tuplas (compara o valor)
        #                 [] <- listas (compara o valor)
        #                 {} <- dicionários (somente a chave, não o valor)
        if choice not in (1, 2):
            print("Invalid option")
    return


if __name__ == "__main__":
    main()
