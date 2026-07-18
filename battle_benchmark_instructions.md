# Coding Benchmark: Python Classes — Build a Battle System

**Goal:** Build a small RPG-style battle system using regular Python classes to show you understand `__init__`, instance attributes, methods, and object interaction.

---

## Story

You're building the core combat engine for a simple RPG. Two characters fight until one runs out of health.

---

## Task

Create a file called `battle.py` that implements the following.

### 1. `Character` class

Write a class called `Character` with an `__init__` that takes:

| Parameter | Type | Notes |
|---|---|---|
| `name` | `str` | required |
| `health` | `int` | required (this is also the character's max health) |
| `attack_power` | `int` | required |

Store `health` as the character's **current** health, and also store the starting value separately as `max_health` (you'll need it later).

Add these methods:

- `is_alive(self)` — returns `True` if `health > 0`, else `False`.
- `take_damage(self, amount)` — subtracts `amount` from `health`. Health should never go below `0` (don't let it go negative).
- `attack(self, other)` — makes this character deal damage equal to `self.attack_power` to `other` (an instance of `Character`), by calling `other.take_damage(...)`. Also **print** a line describing the attack, e.g.:
  `"Aria attacks Goblin for 12 damage!"`
- `heal(self, amount)` — increases `health` by `amount`, but never above `max_health`.

### 2. `Weapon` class

Write a class called `Weapon` with an `__init__` that takes:

| Parameter | Type | Notes |
|---|---|---|
| `name` | `str` | required |
| `bonus_damage` | `int` | required |

### 3. Connect `Weapon` to `Character`

Add a method to `Character` called `equip(self, weapon)` that:
- Stores the weapon on the character (e.g. `self.weapon = weapon`)
- Increases `self.attack_power` by `weapon.bonus_damage`
- Prints a message, e.g. `"Aria equips Flaming Sword! Attack power is now 22."`

A `Character` should start with no weapon equipped (e.g. `self.weapon = None` in `__init__`).

### 4. `Battle` class

Write a class called `Battle` with an `__init__` that takes two `Character` instances: `fighter_one` and `fighter_two`.

Add a method `run(self)` that:
1. Alternates turns between the two fighters (fighter_one attacks first).
2. On each turn, the attacking character calls `.attack()` on the other.
3. Stops as soon as one character's `is_alive()` becomes `False`.
4. Prints a final line announcing the winner, e.g. `"Aria wins the battle!"`

### 5. Demo script

At the bottom of `battle.py`, under `if __name__ == "__main__":`, write code that:

1. Creates two `Character` instances with different stats.
2. Creates at least one `Weapon` and equips it to one character.
3. Creates a `Battle` with the two characters.
4. Calls `.run()` and lets the battle play out.

---

## Requirements Checklist (how you'll be graded)

- [ ] `Character`, `Weapon`, and `Battle` are all written as regular classes with `__init__`
- [ ] `health` never drops below `0` or heals above `max_health`
- [ ] `attack()` correctly reduces the target's health and prints a message
- [ ] `equip()` correctly increases `attack_power` and prints a message
- [ ] `Battle.run()` alternates turns and stops exactly when a character dies
- [ ] Demo script runs top to bottom with `python battle.py` and prints a full battle with a winner

---

## Starter Code

A starter file (`battle_starter.py`) is provided with class shells and TODOs — fill it in.

## Automated Check

A test file (`test_battle.py`) is provided. Once you've written `battle.py`, run:

```
python test_battle.py
```

All tests should print `PASS`.
