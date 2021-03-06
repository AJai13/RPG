import random
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
    
    victory_condition = 5
    defeated_monsters = 0
    
    while defeated_monsters < victory_condition:
        monster = random.choice(all_monsters)
        is_winnable = start_fight(player, monster)
        
        if not is_winnable:
            print("You lose")
            exit(0)

        defeated_monsters += 1
    print("You win \(シ)/")
    
   

def menu():
    print("Welcome to the RPG\n")
    print("Select the options:")
    print("1. Start the game")
    print("2. Exit\n")

    while True:
        choice = int(input("Select the number:"))

        if choice == 2:
            print("Bye bye")
            exit()

        if choice == 1:
            print("\nStarting the game...\n")
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
