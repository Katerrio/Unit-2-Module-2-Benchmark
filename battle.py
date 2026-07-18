class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.maxhealth = self.health        
        self.attack_power = attack_power
        self.weapon = None
        

    def is_alive(self):
        if self.health > 0:
            return True

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        other.take_damage(self.attack_power)
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        

    def heal(self, amount):
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        

    def equip(self, weapon):
        self.weapon = weapon
        self.attack_power += weapon.bonus_damage
        print(f"{self.name} equips {weapon.weapon_name}. Attack power is now {self.attack_power}!")
        


class Weapon:
    def __init__(self, name: str, bonus_damage: int):
        self.weapon_name = name
        self.bonus_damage = bonus_damage


class Battle:
    def __init__(self, fighter_one, fighter_two):
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

    def run(self):
        while self.fighter_one.is_alive() and self.fighter_two.is_alive():
            self.fighter_one.attack(self.fighter_two)
            if self.fighter_two.is_alive():
                self.fighter_two.attack(self.fighter_one)
        if self.fighter_one.is_alive():
            print(f"{self.fighter_one.name} wins the battle!")
        else:
            print(f"{self.fighter_two.name} wins the battle!")
def main():
    fighter_one = Character("John Wick", 100, 30)
    fighter_two = Character("Corvo", 200, 50)
    folding_blade = Weapon("Folding Blade", 20)  
    pencil = Weapon("Pencil", 24)
    fighter_one.equip(pencil)
    fighter_two.equip(folding_blade)
    battle = Battle(fighter_one=fighter_one, fighter_two=fighter_two)
    battle.run()
          


if __name__ == "__main__":
    main()