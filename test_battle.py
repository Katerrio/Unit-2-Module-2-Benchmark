"""
Automated checks for battle.py
Run with: python test_battle.py
(battle.py must be in the same folder)
"""

import io
import contextlib

try:
    from battle import Character, Weapon, Battle
except ImportError:
    print("FAIL: Could not import Character/Weapon/Battle from battle.py")
    raise SystemExit(1)


def check(label, condition):
    print(f"{'PASS' if condition else 'FAIL'}: {label}")


def run_tests():
    # 1. Character basic setup
    hero = Character(name="Aria", health=30, attack_power=10)
    check("Character stores name/health/attack_power",
          hero.name == "Aria" and hero.health == 30 and hero.attack_power == 10)
    check("Character starts alive", hero.is_alive() is True)
    check("Character starts with no weapon (self.weapon is None)",
          getattr(hero, "weapon", "MISSING") is None)

    # 2. take_damage
    hero.take_damage(10)
    check("take_damage reduces health correctly", hero.health == 20)

    hero.take_damage(100)
    check("take_damage does not go below 0", hero.health == 0)
    check("is_alive is False at 0 health", hero.is_alive() is False)

    # 3. heal
    hero2 = Character(name="Bram", health=30, attack_power=8)
    hero2.take_damage(20)
    hero2.heal(5)
    check("heal increases health correctly", hero2.health == 15)

    hero2.heal(1000)
    check("heal does not exceed max_health", hero2.health == 30)

    # 4. Weapon + equip
    sword = Weapon(name="Flaming Sword", bonus_damage=12)
    check("Weapon stores name/bonus_damage",
          sword.name == "Flaming Sword" and sword.bonus_damage == 12)

    fighter = Character(name="Kess", health=25, attack_power=10)
    fighter.equip(sword)
    check("equip increases attack_power", fighter.attack_power == 22)
    check("equip stores the weapon on the character", fighter.weapon is sword)

    # 5. attack() reduces target health and prints something
    attacker = Character(name="Fen", health=20, attack_power=7)
    target = Character(name="Orc", health=20, attack_power=5)

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        attacker.attack(target)
    output = buf.getvalue()

    check("attack() reduces target health by attack_power", target.health == 13)
    check("attack() prints a message", len(output.strip()) > 0)

    # 6. Battle.run() alternates turns and ends with a winner printed
    f1 = Character(name="Champion", health=20, attack_power=10)
    f2 = Character(name="Rival", health=15, attack_power=3)
    battle = Battle(f1, f2)

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        battle.run()
    output = buf.getvalue()

    check("Battle.run() ends with exactly one fighter alive",
          f1.is_alive() != f2.is_alive())
    check("Battle.run() announces a winner by name",
          ("Champion" in output and "wins" in output) or
          ("Rival" in output and "wins" in output))


if __name__ == "__main__":
    run_tests()
