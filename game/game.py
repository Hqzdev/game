from characters.character_selection import CharacterSelection
from shop.shop import Shop


class Game:
    def __init__(self):
        self.hero = None
        self.enemy = None
        self.enemies = []
        self.shop = Shop()

    def create_hero(self):
        """Создание героя"""
        self.hero = CharacterSelection.choose_character()

    def visit_shop(self):
        """Посещение магазина"""
        if self.hero:
            while True:
                self.shop.display_items()
                print("\n0. Выйти из магазина")
                choice = input("Введите номер предмета для покупки: ")

                if choice.isdigit():
                    choice = int(choice)
                    if choice == 0:
                        break
                    self.shop.buy_item(self.hero, choice)
                else:
                    print("Некорректный ввод. Попробуйте ещё раз.")
        else:
            print("Сначала создайте героя.")

    def show_inventory(self):
        """Отображение инвентаря героя"""
        if self.hero:
            print("\n--- Инвентарь ---")
            self.hero.show_inventory()
        else:
            print("Герой не выбран.")

    def use_item(self, item_name):
        """Использование предмета из инвентаря"""
        if self.hero:
            self.hero.use_item(item_name)
        else:
            print("Герой не выбран.")

    def battle(self):
        """Логика сражений (заглушка для расширения)"""
        print("Сражение начинается! (пока не реализовано)")

    def play(self):
        """Основной цикл игры"""
        while True:
            print("\n--- Меню ---")
            print("1. Создать героя")
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
