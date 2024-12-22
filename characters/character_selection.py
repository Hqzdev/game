from characters.hero import Hero
from items.weapon import Weapon
from items.armor import Armor
from items.inventory import Inventory
import random

class CharacterSelection:
    @staticmethod
    def get_hero_options():
        # Создаём базовые предметы
        basic_weapon = Weapon("Меч", "Простой меч", attack=10)
        basic_armor = Armor("Кожаная броня", "Легкая защита", defense=15)

        # Создаём героев
        heroes = [
            Hero(lvl=1, name="Артур", last_name="Стрелок", lor="Лес", history="Рыцарь, защитник королевства",
                 hp=150, old=30, gender="Мужской", spells=['Критический удар'], radius=5, weaknesses={'Стрелок'},
                 speed=10, intelligence=8, power=12, agility=15, lucky=5, power_damage=random.randint(15, 25), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Маг", last_name="Волшебник", lor="Горы", history="Колдун, изучающий древнюю магию",
                 hp=75, old=67, gender="Мужской", spells=['Огненный шар'], radius=10, weaknesses={'Рыцарь'},
                 speed=10, intelligence=15, power=17, agility=15, lucky=7, power_damage=random.randint(30, 40), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Стрелок", last_name="Лучник", lor="Деревня", history="Лучник, мастер дальнего боя",
                 hp=95, old=18, gender="Мужской", spells=['Стрелы'], radius=25, weaknesses={'Маг'},
                 speed=10, intelligence=12, power=15, agility=13, lucky=3, power_damage=random.randint(20, 30), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Элайза", last_name="Тень", lor="Пустошь", history="Убийца, мастер скрытности",
                 hp=80, old=24, gender="Женский", spells=['Удар в спину'], radius=7, weaknesses={'Магия'},
                 speed=18, intelligence=10, power=20, agility=20, lucky=8, power_damage=random.randint(10, 20), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Тор", last_name="Громовержец", lor="Горы", history="Великан с молотом",
                 hp=200, old=150, gender="Мужской", spells=['Молния'], radius=4, weaknesses={'Магический урон'},
                 speed=8, intelligence=7, power=30, agility=10, lucky=2, power_damage=random.randint(35, 50), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Люциан", last_name="Охотник", lor="Тёмный лес", history="Охотник на нечисть",
                 hp=120, old=35, gender="Мужской", spells=['Освящённая стрела'], radius=15, weaknesses={'Тёмная магия'},
                 speed=12, intelligence=10, power=18, agility=16, lucky=6, power_damage=random.randint(25, 35), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Серафина", last_name="Светлая", lor="Горный монастырь", history="Целительница и маг света",
                 hp=90, old=29, gender="Женский", spells=['Луч света'], radius=10, weaknesses={'Тёмные существа'},
                 speed=9, intelligence=20, power=10, agility=8, lucky=5, power_damage=random.randint(10, 15), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Гроуг", last_name="Громила", lor="Орочье племя", history="Сильнейший орк племени",
                 hp=250, old=40, gender="Мужской", spells=['Землетрясение'], radius=6, weaknesses={'Магический урон'},
                 speed=7, intelligence=5, power=35, agility=5, lucky=3, power_damage=random.randint(40, 60), exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=777, name="Админ", last_name="Сильный", lor="Ошибка код", history="error",
                 hp=777777, old=777777, gender="Мужской", spells=['Землетрясение'], radius=777777, weaknesses={'Магический урон'},
                 speed=7777777, intelligence=777777, power=7777777, agility=7777777, lucky=777777, power_damage=7777777, exp=7777777,
                 inventory=Inventory(capacity=10))
        ]

        # Наполнение инвентаря каждого героя
        for hero in heroes:
            hero.add_item_to_inventory(basic_weapon)
            hero.add_item_to_inventory(basic_armor)

        return heroes
