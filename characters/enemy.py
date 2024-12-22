import random

class Enemy:
    def __init__(self, name, description, strength, abilities, hp, lvl, power_damage, exp):
        self.name = name
        self.description = description
        self.strength = strength
        self.abilities = abilities
        self.hp = hp
        self.lvl = lvl
        self.power_damage = power_damage
        self.exp = exp

    def attack(self):
        print(f'{self.name} атакует!')
        return self.power_damage

    def __str__(self):
        return f"{self.name} - {self.description} (Сила: {self.strength})"

class StreetThug(Enemy):
    def __init__(self):
        super().__init__(
            name='Бандит',
            description='Уличный бандит',
            strength='Слабая',
            abilities=['Скрытный удар'],
            hp=140,
            lvl=1,
            power_damage=random.randint(1, 5),
            exp=3
        )

class Killer(Enemy):
    def __init__(self):
        super().__init__(
            name='Наемник',
            description='Наемный убийца',
            strength='Средняя',
            abilities=['Уклонение'],
            hp=100,
            lvl=2,
            power_damage=random.randint(3, 8),
            exp=10
        )

class DarkMage(Enemy):
    def __init__(self):
        super().__init__(
            name='Темный маг',
            description='Могущественный маг',
            strength='Сильная',
            abilities=['Огненный шар'],
            hp=75,
            lvl=3,
            power_damage=random.randint(10, 17),
            exp=20
        )

class DarkLord(Enemy):
    def __init__(self):
        super().__init__(
            name='Темный лорд',
            description='Повелитель зла',
            strength='Эпическая',
            abilities=['Тёмная магия'],
            hp=1000,
            lvl=5,
            power_damage=random.randint(20, 35),
            exp=100
        )

class AncientDragon(Enemy):
    def __init__(self):
        super().__init__(
            name='Древний дракон',
            description='Мифический зверь',
            strength='Мифическая',
            abilities=['Огненное дыхание'],
            hp=10000,
            lvl=10,
            power_damage=random.randint(40, 70),
            exp=500
        )
