from characters.character_selection import CharacterSelection
from shop.shop import Shop
from characters.enemy import Enemy


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
        """Создает врага для сражения."""
        self.enemy = Enemy(
            name="Гоблин",
            description="Простой враг",
            strenght="Средний",
            hp=100,
            power_damage=10,
        )
        print(f"Создан враг: {self.enemy.name} (HP: {self.enemy.hp}).")

    def visit_shop(self):
        """Посещение магазина."""
        if self.hero:
            print("\n--- Магазин ---")
            self.shop.display_items()
        else:
            print("Сначала выберите героя!")

    def buy_item(self, item_number):
        """Покупка предмета из магазина."""
        if self.hero:
            success = self.shop.buy_item(self.hero, item_number)
            if success:
                print(f"{self.hero.name} купил предмет!")
            else:
                print("Покупка не удалась.")
        else:
            print("Сначала выберите героя!")

    def show_inventory(self):
        """Отображение инвентаря героя."""
        if self.hero:
            print("\n--- Инвентарь ---")
            self.hero.show_inventory()
        else:
            print("Сначала выберите героя!")

    def use_item(self, item_name):
        """Использование предмета из инвентаря."""
        if self.hero:
            self.hero.use_item(item_name)
        else:
            print("Сначала выберите героя!")

    def battle(self):
        """Начало сражения."""
        if not self.hero:
            print("Сначала выберите героя!")
            return

        if not self.enemy:
            self.create_enemy()

        print(f"\nБитва между {self.hero.name} и {self.enemy.name} начинается!")
        while self.hero.hp > 0 and self.enemy.hp > 0:
            # Ход героя
            hero_damage = self.hero.attack()
            self.enemy.hp -= hero_damage
            print(f"{self.hero.name} нанес {hero_damage} урона. У {self.enemy.name} осталось {self.enemy.hp} HP.")
            if self.enemy.hp <= 0:
                print(f"{self.hero.name} победил {self.enemy.name}!")
                break

            # Ход врага
            enemy_damage = self.enemy.attack()
            self.hero.hp -= enemy_damage
            print(f"{self.enemy.name} нанес {enemy_damage} урона. У {self.hero.name} осталось {self.hero.hp} HP.")
            if self.hero.hp <= 0:
                print(f"{self.hero.name} был побежден {self.enemy.name}.")
                break

    def play(self):
        """Основной цикл игры."""
        while True:
            print("\n--- Меню ---")
            print("1. Выбрать героя")
            print("2. Посмотреть инвентарь")
            print("3. Использовать предмет")
            print("4. Посетить магазин")
            print("5. Сражение")
            print("0. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_hero()
            elif choice == "2":
                self.show_inventory()
            elif choice == "3":
                item_name = input("Введите название предмета для использования: ")
                self.use_item(item_name)
            elif choice == "4":
                self.visit_shop()
            elif choice == "5":
                self.battle()
            elif choice == "0":
                print("Выход из игры.")
                break
            else:
                print("Некорректный ввод. Попробуйте ещё раз.")
