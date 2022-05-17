import random


class Monster:
    def __init__(
        self,
        name,
        challenge_rating,
        size,
        monster_type,
        hp_total,
        strenght,
        dexterity,
        intelligence,
        min_damage,
    ):
        self.name = name
        self.challenge_rating = challenge_rating
        self.size = size
        self.monster_type = monster_type
        self.hp_total = hp_total
        self.str = strenght
        self.dex = dexterity
        self.int = intelligence
        # valores dinâmicos
        self.hp_current = hp_total
        self.dead = False

        # valores de referência p/ attack
        self.base_attack = 10
        self.offset_attack = 0.06
        self.min_damage = min_damage

    def attack(self):
        damage = int(self.base_attack * self.str * self.offset_attack)
        return random.randint(self.min_damage, damage)

    def change_hp(self, damage):
        current_hp = self.hp_current - damage
        if current_hp <= 0:
            self.dead = True
            self.hp_current = 0
        else:
            self.hp_current = current_hp


all_monsters = [
    Monster(
        name="Orc",
        challenge_rating=6,
        size="huge",
        monster_type="giant",
        hp_total=120,
        strenght=16,
        dexterity=12,
        intelligence=5,
        min_damage=1,
    ),
    Monster(
        name="Goblin",
        challenge_rating=4,
        size="small",
        monster_type="humanoid",
        hp_total=50,
        strenght=8,
        dexterity=14,
        intelligence=10,
        min_damage=1,
    ),
    Monster(
        name="Wolf",
        challenge_rating=6,
        size="medium",
        monster_type="beast",
        hp_total=75,
        strenght=12,
        dexterity=15,
        intelligence=3,
        min_damage=1,
    )
]


