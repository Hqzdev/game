from characters.hero import Hero
from items.weapon import Weapon
from items.armor import Armor
from items.inventory import Inventory  # Подключаем класс инвентаря

class CharacterSelection:
    @staticmethod
    def get_hero_options():
        print('Выбор персонажа: ')

        # Создание героев
        heroes = [
            Hero(lvl=1, name="Артур", last_name="Стрелок", lor="Лес", history="Рыцарь, защитник королевства",
                 hp=150, old=30, gender="Мужской", spells=['Критический удар'], radius=5, weaknesses={'Стрелок'},
                 speed=10, intelligence=8, power=12, agility=15, lucky=5, power_damage=20, exp=0,
                 inventory=Inventory(capacity=10)),
            
            Hero(lvl=1, name="Маг", last_name="Волшебник", lor="Горы", history="Колдун, изучающий древнюю магию",
                 hp=75, old=67, gender="Мужской", spells=['Огненный шар'], radius=10, weaknesses={'Рыцарь'},
                 speed=10, intelligence=15, power=17, agility=15, lucky=7, power_damage=35, exp=0,
                 inventory=Inventory(capacity=10)),
            
            Hero(lvl=1, name="Стрелок", last_name="Лучник", lor="Деревня", history="Лучник, мастер дальнего боя",
                 hp=95, old=18, gender="Мужской", spells=['Стрелы'], radius=25, weaknesses={'Маг'},
                 speed=10, intelligence=12, power=15, agility=13, lucky=3, power_damage=23, exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Элайза", last_name="Тень", lor="Пустошь", history="Убийца, мастер скрытности",
                 hp=80, old=24, gender="Женский", spells=['Удар в спину'], radius=7, weaknesses={'Магия'},
                 speed=18, intelligence=10, power=20, agility=20, lucky=8, power_damage=15, exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Тор", last_name="Громовержец", lor="Горы", history="Великан с молотом",
                 hp=200, old=150, gender="Мужской", spells=['Молния'], radius=4, weaknesses={'Магический урон'},
                 speed=8, intelligence=7, power=30, agility=10, lucky=2, power_damage=40, exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Люциан", last_name="Охотник", lor="Тёмный лес", history="Охотник на нечисть",
                 hp=120, old=35, gender="Мужской", spells=['Освящённая стрела'], radius=15, weaknesses={'Тёмная магия'},
                 speed=12, intelligence=10, power=18, agility=16, lucky=6, power_damage=25, exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Серафина", last_name="Светлая", lor="Горный монастырь", history="Целительница и маг света",
                 hp=90, old=29, gender="Женский", spells=['Луч света'], radius=10, weaknesses={'Тёмные существа'},
                 speed=9, intelligence=20, power=10, agility=8, lucky=5, power_damage=15, exp=0,
                 inventory=Inventory(capacity=10)),

            Hero(lvl=1, name="Гроуг", last_name="Громила", lor="Орочье племя", history="Сильнейший орк племени",
                 hp=250, old=40, gender="Мужской", spells=['Землетрясение'], radius=6, weaknesses={'Магический урон'},
                 speed=7, intelligence=5, power=35, agility=5, lucky=3, power_damage=50, exp=0,
                 inventory=Inventory(capacity=10))
        ]

        # Базовые предметы
        basic_weapon = Weapon("Меч", "Простой меч", attack=10)
        basic_armor = Armor("Кожаная броня", "Легкая защита", defense=15)
        
        # Наполнение инвентаря каждого героя
        for hero in heroes:
            hero.add_item_to_inventory(basic_weapon)
            hero.add_item_to_inventory(basic_armor)

        # Отображение списка героев для выбора
        for index, hero in enumerate(heroes):
            print(f'{index + 1}. {hero.name} {hero.last_name} (Здоровье: {hero.hp}, '
                  f'Сила: {hero.power}, Интеллект: {hero.intelligence}, История: {hero.history})')

        # Выбор персонажа
        try:
            choice = int(input('Введите номер персонажа: '))
            if 1 <= choice <= len(heroes):
                return heroes[choice - 1]
            else:
                print('Некорректный выбор.')
                return None
        except ValueError:
            print('Введите число.')
            return None
