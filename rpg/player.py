import random


class Player:
    def __init__(self, name, vocation):
        self.name = name
        self.vocation = vocation
        self.hp_current = vocation.hp_total
        self.sp_current = vocation.sp_total
        self.dead = False

    def attack(self):
        # Este método é um método de return statement
        # Entende-se nesse momento que método = função

        # base attack
        damage = int(self.vocation.base_attack * self.vocation.str * self.vocation.offset_attack)
        return random.randint(self.vocation.min_damage, damage)

    def attack_spells(self):
        # Este método é um método de return statement
        # Entende-se nesse momento que método = função
        usable_spells = []

        for index, spell in enumerate(self.vocation.spells):
            # validar se o sp_current é menor que o spell.sp_cost
            # caso for, mostrar a spell pra ser usada. Caso contrário, se fodeu
            if self.sp_current >= spell.sp_cost:                
                print("{idx}. {spell_name}".format(idx=index, spell_name=spell.name))
                usable_spells.append(index) # Vamos atualizar a lista nessa linha

        final_damage = 0

        while True:
            # Selecionar a spell que será utilizada, baseado no número do index
            choice = int(input("Select the spell: "))
            if choice in usable_spells:
                # Calcular o dano da spell
                final_damage = self.vocation.spells[choice].damage

                # -------- TAREFA, MEU IRMÃO, 1 --------
                # Consumir sp da classe 
                # Sempre diminuir o sp_current subtraindo do sp_cost da spell
                # Case o sp_current for <= 0, não fazer nada.
                break
            else:
                # Caso o número selecionado não estiver dentro da lista de spells, pular o turno
                # fazendo com que o player não de dano no inimigo.
                final_damage = 0

                # -------- TAREFA, MEU IRMÃO, 2 --------
                # Incrementar o sp_current da classe em 1 toda vez que nenhuma spell for selecionada.

        # Retornar o dano causado pela spell
        return final_damage


    def change_hp(self, damage):
        # Este método é um método de side effect
        # Entende-se nesse momento que método = função
        current_hp = self.hp_current - damage
        if current_hp <= 0:
            self.dead = True
            self.hp_current = 0
        else:
            self.hp_current = current_hp
