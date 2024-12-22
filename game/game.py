from characters.character_selection import CharacterSelection
from shop.shop import Shop
from characters.enemy import Enemy
import random
from characters.enemy import StreetThug, Killer, DarkMage, DarkLord, AncientDragon

class Game:
    def __init__(self):
        self.hero = None
        self.enemy = None
        self.hero_options = CharacterSelection.get_hero_options()
        self.shop = Shop()

    def set_hero(self, hero):
        self.hero = hero
        print(f"Герой {self.hero.name} выбран!")

    def create_enemy(self):
        enemy_classes = [StreetThug, Killer, DarkMage, DarkLord, AncientDragon]
        self.enemy = random.choice(enemy_classes)()  # Случайный враг
        print(f"Создан враг: {self.enemy.name} (HP: {self.enemy.hp}).")

    def visit_shop(self):
        if self.hero:
            self.shop.display_items(self.hero)
        else:
            print("Сначала выберите героя!")

    def buy_item(self, item_number):
        if self.hero:
            self.shop.buy_item(self.hero, item_number)
        else:
            print("Сначала выберите героя!")

    def show_inventory(self):
        if self.hero:
            self.hero.show_inventory()
        else:
            print("Сначала выберите героя!")

    def use_item(self, item_name):
        if self.hero:
            self.hero.use_item(item_name)
        else:
            print("Сначала выберите героя!")

    def calculate_gold_reward(self):
        if isinstance(self.enemy, StreetThug):
            return random.randint(50, 100)
        elif isinstance(self.enemy, Killer):
            return random.randint(100, 200)
        elif isinstance(self.enemy, DarkMage):
            return random.randint(200, 300)
        elif isinstance(self.enemy, DarkLord):
            return random.randint(300, 500)
        elif isinstance(self.enemy, AncientDragon):
            return random.randint(500, 750)
        return 0

    def battle(self):
        if not self.hero:
            print("Сначала выберите героя!")
            return

        if not self.enemy:
            self.create_enemy()

        print(f"\nБитва между {self.hero.name} и {self.enemy.name} начинается!")
        while self.hero.hp > 0 and self.enemy.hp > 0:
            print("\n1. Ударить")
            print("2. Использовать способность")
            action = input("Выберите действие: ")

            if action == "1":
                hero_damage = self.hero.attack()
                self.enemy.hp = max(0, self.enemy.hp - hero_damage)
                print(f"{self.hero.name} наносит {hero_damage} урона. У {self.enemy.name} осталось {self.enemy.hp} HP.")
            elif action == "2":
                hero_damage = self.hero.use_ability()
                self.enemy.hp = max(0, self.enemy.hp - hero_damage)
                print(f"{self.hero.name} использует способность и наносит {hero_damage} урона. У {self.enemy.name} осталось {self.enemy.hp} HP.")
            else:
                print("Некорректный ввод.")

            if self.enemy.hp > 0:
                enemy_damage = self.enemy.attack()
                self.hero.hp = max(0, self.hero.hp - enemy_damage)
                print(f"{self.enemy.name} наносит {enemy_damage} урона. У {self.hero.name} осталось {self.hero.hp} HP.")

        if self.hero.hp > 0:
            gold_reward = self.calculate_gold_reward()
            self.hero.gold += gold_reward
            print("\n**********************************************")
            print(f"ПОБЕДА! {self.hero.name} победил {self.enemy.name} и получил {gold_reward} золота!")
            print(f"Ваш текущий баланс: {self.hero.gold} золота.")
            print("**********************************************")
        else:
            print(f"{self.hero.name} был побеждён {self.enemy.name}.")

    def play(self):
        self.choose_hero()  # Выбор героя перед началом игры
        while True:
            print("\n--- Меню ---")
            print("1. Посмотреть инвентарь")
            print("2. Использовать предмет")
            print("3. Посетить магазин")
            print("4. Сражение")
            print("0. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.show_inventory()
            elif choice == "2":
                item_name = input("Введите название предмета для использования: ")
                self.use_item(item_name)
            elif choice == "3":
                self.visit_shop()
            elif choice == "4":
                self.battle()
            elif choice == "0":
                print("Выход из игры.")
                break
            else:
                print("Некорректный ввод, попробуйте снова.")

    def choose_hero(self):
        print("\nВыберите героя:")
        for idx, hero in enumerate(self.hero_options, start=1):
            print(f"{idx}. {hero.name} {hero.last_name} (HP: {hero.hp}, Сила: {hero.power})")
        choice = input("Введите номер героя: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.hero_options):
            self.set_hero(self.hero_options[int(choice) - 1])
        else:
            print("Некорректный выбор героя.")
            self.choose_hero()
