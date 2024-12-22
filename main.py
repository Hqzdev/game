from game.game import Game

class GameConsole:
    def __init__(self):
        self.game = Game()

    def start(self):
        """Запуск игры с выбором героя и дальнейшим игровым меню."""
        self.choose_hero()
        while True:
            print("\n--- Меню ---")
            print("1. Сражение")
            print("2. Инвентарь")
            print("3. Магазин")
            print("4. Выйти из игры")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.start_battle()
            elif choice == "2":
                self.show_inventory()
            elif choice == "3":
                self.open_shop()
            elif choice == "4":
                print("Выход из игры.")
                break
            else:
                print("Некорректный ввод, попробуйте снова.")

    def choose_hero(self):
        """Позволяет выбрать героя перед началом игры."""
        print("\nВыберите героя:")
        for i, hero in enumerate(self.game.hero_options, start=1):
            print(f"{i}. {hero.name} {hero.last_name} (HP: {hero.hp}, Сила: {hero.power})")
        choice = input("Введите номер героя: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.game.hero_options):
            self.game.set_hero(self.game.hero_options[int(choice) - 1])
            print(f"Герой выбран: {self.game.hero.name} {self.game.hero.last_name}")
        else:
            print("Некорректный выбор героя.")
            self.choose_hero()

    def start_battle(self):
        """Начинает сражение."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        self.game.battle()

    def show_inventory(self):
        """Отображение инвентаря героя."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        self.game.show_inventory()

    def open_shop(self):
        """Открывает магазин."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        self.game.visit_shop()

if __name__ == "__main__":
    console_game = GameConsole()
    console_game.start()
