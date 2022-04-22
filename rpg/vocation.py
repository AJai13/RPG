class Spells:
    def __init__(self, name, sp_cost, damage):
        self.name = name
        self.sp_cost = sp_cost
        self.damage = damage


# Vocation são classes
class Vocation:
    def __init__(
        self,
        name,
        hp_total,
        sp_total,
        strenght,
        dexterity,
        intelligence,
        spells,
        base_attack,
        min_damage,
    ):
        # Atributo
        self.name = name
        self.hp_total = hp_total
        self.sp_total = sp_total
        self.str = strenght
        self.dex = dexterity
        self.int = intelligence
        self.spells = spells

        self.base_attack = base_attack
        self.offset_attack = 0.06
        self.min_damage = min_damage


# Singletons
all_vocations = [
    # Inicializando a classe Vocation com valores para um Mage.
    Vocation(
        name="Mage",
        hp_total=50,
        sp_total=3,
        strenght=5,
        dexterity=6,
        intelligence=15,
        spells=[Spells(name="Fireball", sp_cost=2, damage=10)],
        base_attack=2,
        min_damage=0,
    ),
    Vocation(
        name="Necromancer",
        hp_total=50,
        sp_total=3,
        strenght=5,
        dexterity=6,
        intelligence=15,
        spells=[Spells(name="Fireball", sp_cost=2, damage=10)],
        base_attack=2,
        min_damage=0,
    )
]

def get_vocation():
    print("These are the vocations:")
    for index, vocation in enumerate(all_vocations):
        print("{idx}. {vocation_name}".format(idx=index, vocation_name=vocation.name))

    final_vocation = None  # ou ''

    while True:
        choice = int(input("Now choose one: "))
        if choice in range(0, len(all_vocations)):
            final_vocation = all_vocations[choice]
            break
        else:
            print("Invalid option")
    return final_vocation
