from game.game import Game

class GameConsole:
    def __init__(self):
        self.game = Game()
        self.is_battle_active = False
        self.ability_uses_left = 3

    def start(self):
        """Запуск игры через консоль."""
        while True:
            print("\n1. Сражение")
            print("2. Инвентарь")
            print("3. Магазин")
            print("4. Выбрать героя")
            print("5. Выйти из игры")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.start_battle()
            elif choice == "2":
                self.show_inventory()
            elif choice == "3":
                self.open_shop()
            elif choice == "4":
                self.choose_hero()
            elif choice == "5":
                print("Выход из игры.")
                break
            else:
                print("Некорректный ввод, попробуйте снова.")

    def choose_hero(self):
        """Позволяет выбрать героя."""
        print("\nВыберите героя:")
        for i, hero in enumerate(self.game.hero_options, start=1):
            print(f"{i}. {hero.name} {hero.last_name} (HP: {hero.hp}, Сила: {hero.power})")
        choice = input("Введите номер героя: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.game.hero_options):
            self.game.set_hero(self.game.hero_options[int(choice) - 1])
        else:
            print("Некорректный выбор героя.")

    def start_battle(self):
        """Начинает сражение."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        self.ability_uses_left = 3
        self.game.create_enemy()
        print(f"\nНачинается бой с врагом: {self.game.enemy.name} (HP: {self.game.enemy.hp})")

        while self.game.hero.hp > 0 and self.game.enemy.hp > 0:
            print("\n1. Ударить")
            print("2. Использовать способность")
            action = input("Выберите действие: ")

            if action == "1":
                self.attack()
            elif action == "2":
                self.use_ability()
            else:
                print("Некорректный ввод.")

            if self.game.enemy.hp > 0:
                self.enemy_turn()

        if self.game.hero.hp <= 0:
            print(f"К сожалению, {self.game.hero.name} был побеждён {self.game.enemy.name}.")
        else:
            print(f"Поздравляем! {self.game.hero.name} победил {self.game.enemy.name}.")

    def attack(self):
        """Атака героя."""
        hero_damage = self.game.hero.attack()
        self.game.enemy.hp -= hero_damage
        print(f"{self.game.hero.name} наносит {hero_damage} урона. У {self.game.enemy.name} осталось {self.game.enemy.hp} HP.")

    def use_ability(self):
        """Использование способности."""
        if self.ability_uses_left > 0:
            hero_damage = self.game.hero.use_ability()
            self.game.enemy.hp -= hero_damage
            self.ability_uses_left -= 1
            print(f"{self.game.hero.name} использует способность и наносит {hero_damage} урона! У {self.game.enemy.name} осталось {self.game.enemy.hp} HP.")
        else:
            print("Вы больше не можете использовать способность в этом бою!")

    def enemy_turn(self):
        """Ход врага."""
        enemy_damage = self.game.enemy.attack()
        self.game.hero.hp -= enemy_damage
        print(f"{self.game.enemy.name} наносит {enemy_damage} урона. У {self.game.hero.name} осталось {self.game.hero.hp} HP.")

    def show_inventory(self):
        """Отображение инвентаря героя."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        print(f"\nИнвентарь {self.game.hero.name}:")
        for item in self.game.hero.inventory.items:
            print(f"- {item}")

    def open_shop(self):
        """Открывает магазин."""
        if not self.game.hero:
            print("Сначала выберите героя!")
            return

        print("\nДобро пожаловать в магазин!")
        for i, item in enumerate(self.game.shop.items, start=1):
            print(f"{i}. {item.name} - {item.description} (Цена: {self.game.shop.prices[item.name]} золота)")

        choice = input("Выберите предмет для покупки (номер): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.game.shop.items):
            item = self.game.shop.items[int(choice) - 1]
            self.buy_item(item)
        else:
            print("Некорректный выбор.")

    def buy_item(self, item):
        """Покупка предмета."""
        if self.game.hero.gold >= self.game.shop.prices[item.name]:
            self.game.hero.gold -= self.game.shop.prices[item.name]
            self.game.hero.inventory.add_item(item)
            print(f"Вы купили {item.name}.")
        else:
            print("Недостаточно золота для покупки!")


if __name__ == "__main__":
    console_game = GameConsole()
    console_game.start()
