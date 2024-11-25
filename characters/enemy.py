class Enemy:
    def __init__(self, name, description, strenght, abilities, hp, old, last_name, lor, lvl, history, gender, spells, weaknesses, speed, intelligence, power, agility, radius, lucky, power_damage, exp):
        self.name = name
        self.description = description
        self.strenght = strenght
        self.abilities = abilities
        self.hp = hp
        self.old = old
        self.lvl = lvl
        self.last_name = last_name
        self.lor = lor
        self.history = history
        self.gender = gender
        self.spells = spells
        self.radius = radius
        self.weaknesses = weaknesses
        self.speed = speed
        self.intelligence = intelligence
        self.power = power
        self.agility = agility
        self.lucky = lucky
        self.power_damage = power_damage
        self.exp = exp

    def attack(self):
        print(f'Наносит удар')
        return self.power_damage

    def __str__(self):
        return f"{self.name} - {self.description} (Сила: {self.strenght})"

class StreetThug(Enemy):
    def __init__(self):
        super().__init__(
            name='Бандит',
            description='Уличный бандит',
            strenght='Слабая',
            abilities=['Скрытный удар'],
            hp=140,
            old=20,
            lvl=1,
            last_name='Бандос',
            lor='город',
            history='ff',
            gender='ede',
            spells=[],
            radius=135,
            weaknesses=45,
            speed=10,
            intelligence=5, 
            power=3, 
            agility=3, 
            lucky=3, 
            power_damage=3, 
            exp=3, 
        )

class Killer(Enemy):
    def __init__(self):
        super().__init__(
            name='Наемник',
            description='Наемный убийца',
            strenght='Средняя',
            abilities=['Уклонение'],
            hp=100,
            old=32,
            lvl=1,
            last_name='Бандос',
            lor='город',
            history='ff',
            gender='ede',
            spells=[],
            radius=135,
            weaknesses=45,
            speed=10,
            intelligence=5, 
            power=3, 
            agility=3, 
            lucky=3, 
            power_damage=3, 
            exp=3, 
        )

class DarkMage(Enemy):
    def __init__(self):
        super().__init__(
            name='Темный маг',
            description='Темный маг',
            strenght='Сильняя',
            abilities=['Огненный шар'],
            hp=75,
            old=450,
            last_name='Бандос',
            lor='город',
            lvl=1,
            history='ff',
            gender='ede',
            spells=[],
            radius=135,
            weaknesses=45,
            speed=10,
            intelligence=5, 
            power=3, 
            agility=3, 
            lucky=3, 
            power_damage=3, 
            exp=3, 
        )

class DarkLord(Enemy):
    def __init__(self):
        super().__init__(
            name='Темный лорд',
            description='Могучий волшебник',
            strenght='Эпическая',
            abilities=['Ужасные заклинания'],
            hp=1000,
            old=3465,
            last_name='Бандос',
            lor='город',
            history='ff',
            gender='ede',
            lvl=1,
            spells=[],
            radius=135,
            weaknesses=45,
            speed=10,
            intelligence=5, 
            power=3, 
            agility=3, 
            lucky=3, 
            power_damage=3, 
            exp=3,
        )

class AncientDragon(Enemy):
    def __init__(self):
        super().__init__(
            name='Древний дракон',
            description='Древний дракон',
            strenght='Мифическая',
            abilities=['Удар лапой'],
            hp=10000,
            old=32167,
            last_name='Бандос',
            lor='город',
            history='ff',
            gender='ede',
            spells=[],
            radius=135,
            weaknesses=45,
            speed=10,
            lvl=1,
            intelligence=5, 
            power=3, 
            agility=3, 
            lucky=3, 
            power_damage=3, 
            exp=3,
        )
