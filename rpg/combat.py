import random

def menu_combat():
    print("1. Attack")
    print("2. Spell Attack")

    choice = 0

    while True:
        choice = int(input("Select the number: "))

        if choice not in (1, 2):
            print("Invalid option")
        break
    return choice

def start_fight(player, monster):
    print("\nThe monster to be faced is: {}".format(monster.name))
    print("The monster's total hp is: {}".format(monster.hp_total))
    print("Its size is: {}".format(monster.size))

    
    player_win = False
    
    while True: 
        # 1 = player e 2 = monster
        if player.dead: 
            break
        if monster.dead:
            player_win = True
            break

        print("\nThe player's hp is: {}".format(player.hp_current))
        print("The monster's hp is: {}\n".format(monster.hp_current))

        who_is_attacking = random.randint(1, 2)

        if who_is_attacking == 2:
            damage = monster.attack()
            player.change_hp(damage)
            print("Player took {} damage\n".format(damage))

        elif who_is_attacking == 1:
            choice = menu_combat()
            damage = 0

            if choice == 1:
                damage = player.attack()
            elif choice == 2:
                damage = player.attack_spells()

            monster.change_hp(damage)
            print("\nMonster took {} damage\n".format(damage))
    
    return player_win