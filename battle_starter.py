"""
RPG Battle System - Starter Code
Fill in the TODOs to complete the classes benchmark.
"""


class Character:
    def __init__(self, name, health, attack_power):
        # TODO: store name, health (current), max_health, attack_power
        # TODO: set self.weapon = None
        pass

    def is_alive(self):
        # TODO: return True if health > 0
        pass

    def take_damage(self, amount):
        # TODO: subtract amount from health, don't let it go below 0
        pass

    def attack(self, other):
        # TODO: deal self.attack_power damage to other, print a message
        pass

    def heal(self, amount):
        # TODO: increase health by amount, don't exceed max_health
        pass

    def equip(self, weapon):
        # TODO: store the weapon, increase attack_power by weapon.bonus_damage,
        # print a message
        pass


class Weapon:
    def __init__(self, name, bonus_damage):
        # TODO: store name and bonus_damage
        pass


class Battle:
    def __init__(self, fighter_one, fighter_two):
        # TODO: store both fighters
        pass

    def run(self):
        # TODO: alternate turns (fighter_one attacks first),
        # stop when one fighter's is_alive() is False,
        # print the winner
        pass


if __name__ == "__main__":
    # TODO:
    # 1. Create two Character instances with different stats
    # 2. Create at least one Weapon and equip it to one character
    # 3. Create a Battle with the two characters
    # 4. Call .run()
    pass
