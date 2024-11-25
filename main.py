import tkinter as tk
from game.game import Game


class GameWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра - Герой против врагов")
        self.game = Game()
        self.is_battle_active = False
        self.ability_uses_left = 3  # Ограничение на использование способности

        self.create_main_menu()

    def create_main_menu(self):
        """Создаёт главное меню с выбором действий."""
        self.clear_window()

        self.main_menu_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_menu_frame.pack()

        # Текстовая область
        self.text_area = tk.Text(self.main_menu_frame, width=60, height=20, state=tk.DISABLED, wrap=tk.WORD)
        self.text_area.pack()

        # Кнопки для главного меню
        tk.Button(self.main_menu_frame, text="1. Сражение", command=self.start_battle).pack(pady=5)
        tk.Button(self.main_menu_frame, text="2. Инвентарь", command=self.show_inventory).pack(pady=5)
        tk.Button(self.main_menu_frame, text="3. Магазин", command=self.open_shop).pack(pady=5)
        tk.Button(self.main_menu_frame, text="4. Выбрать героя", command=self.choose_hero).pack(pady=5)

    def choose_hero(self):
        """Позволяет игроку выбрать героя."""
        self.clear_window()
        self.hero_selection_frame = tk.Frame(self.root, padx=20, pady=20)
        self.hero_selection_frame.pack()

        # Заголовок
        tk.Label(self.hero_selection_frame, text="Выберите героя:", font=("Arial", 14)).pack(pady=10)

        # Отображение героев для выбора
        for i, hero in enumerate(self.game.hero_options, start=1):
            tk.Button(
                self.hero_selection_frame,
                text=f"{i}. {hero.name} {hero.last_name} (HP: {hero.hp}, Сила: {hero.power})",
                command=lambda h=hero: self.select_hero(h)
            ).pack(pady=5)

    def select_hero(self, hero):
        """Выбирает героя и возвращает в главное меню."""
        self.game.set_hero(hero)
        self.log_to_text_area(f"Герой выбран: {hero.name} {hero.last_name}")
        self.create_main_menu()

    def start_battle(self):
        """Начинает сражение."""
        if not self.game.hero:
            self.log_to_text_area("Сначала выберите героя!")
            return

        self.clear_window()
        self.battle_frame = tk.Frame(self.root, padx=20, pady=20)
        self.battle_frame.pack()

        self.is_battle_active = True
        self.ability_uses_left = 3
        self.game.create_enemy()

        # Поле вывода текста
        self.text_area = tk.Text(self.battle_frame, width=60, height=20, state=tk.DISABLED, wrap=tk.WORD)
        self.text_area.pack()

        # Логи боя
        self.log_to_text_area(f"Начинается бой с врагом: {self.game.enemy.name} (HP: {self.game.enemy.hp}).")

        # Кнопки для действий
        self.attack_button = tk.Button(self.battle_frame, text="Ударить", command=self.attack)
        self.attack_button.pack(pady=5)

        self.ability_button = tk.Button(self.battle_frame, text="Использовать способность", command=self.use_ability)
        self.ability_button.pack(pady=5)

        self.return_button = tk.Button(self.battle_frame, text="Вернуться в меню", command=self.create_main_menu)
        self.return_button.pack(pady=5)

    def attack(self):
        """Атака героя."""
        hero_damage = self.game.hero.attack()
        self.game.enemy.hp -= hero_damage
        self.log_to_text_area(f"{self.game.hero.name} наносит {hero_damage} урона. У {self.game.enemy.name} осталось {self.game.enemy.hp} HP.")

        if self.game.enemy.hp <= 0:
            self.end_battle(victory=True)
            return

        self.enemy_turn()

    def use_ability(self):
        """Использование способности."""
        if self.ability_uses_left > 0:
            hero_damage = self.game.hero.use_ability()
            self.game.enemy.hp -= hero_damage
            self.ability_uses_left -= 1
            self.log_to_text_area(f"{self.game.hero.name} использует способность и наносит {hero_damage} урона! У {self.game.enemy.name} осталось {self.game.enemy.hp} HP.")
        else:
            self.log_to_text_area("Вы больше не можете использовать способность в этом бою!")

        if self.game.enemy.hp <= 0:
            self.end_battle(victory=True)
            return

        self.enemy_turn()

    def enemy_turn(self):
        """Ход врага."""
        enemy_damage = self.game.enemy.attack()
        self.game.hero.hp -= enemy_damage
        self.log_to_text_area(f"{self.game.enemy.name} наносит {enemy_damage} урона. У {self.game.hero.name} осталось {self.game.hero.hp} HP.")

        if self.game.hero.hp <= 0:
            self.end_battle(victory=False)

    def end_battle(self, victory):
        """Завершение боя."""
        self.is_battle_active = False

        if victory:
            self.log_to_text_area(f"Поздравляем! {self.game.hero.name} победил {self.game.enemy.name}.")
        else:
            self.log_to_text_area(f"К сожалению, {self.game.hero.name} был побеждён {self.game.enemy.name}.")

    def show_inventory(self):
        """Отображение инвентаря героя."""
        if not self.game.hero:
            self.log_to_text_area("Сначала выберите героя!")
            return

        self.clear_window()
        self.inventory_frame = tk.Frame(self.root, padx=20, pady=20)
        self.inventory_frame.pack()

        tk.Label(self.inventory_frame, text=f"Инвентарь {self.game.hero.name}:", font=("Arial", 14)).pack(pady=10)
        for item in self.game.hero.inventory.items:
            tk.Label(self.inventory_frame, text=f"- {item}").pack()

        tk.Button(self.inventory_frame, text="Вернуться в меню", command=self.create_main_menu).pack(pady=10)

    def open_shop(self):
        """Открывает магазин."""
        self.clear_window()
        self.shop_frame = tk.Frame(self.root, padx=20, pady=20)
        self.shop_frame.pack()

        tk.Label(self.shop_frame, text="Добро пожаловать в магазин!", font=("Arial", 14)).pack(pady=10)
        for i, item in enumerate(self.game.shop.items, start=1):
            tk.Button(
                self.shop_frame,
                text=f"{i}. {item.name} - {item.description} (Цена: {self.game.shop.prices[item.name]} золота)",
                command=lambda it=item: self.buy_item(it)
            ).pack(pady=5)

        tk.Button(self.shop_frame, text="Вернуться в меню", command=self.create_main_menu).pack(pady=10)

    def buy_item(self, item):
        """Покупка предмета."""
        if self.game.hero.gold >= self.game.shop.prices[item.name]:
            self.game.hero.gold -= self.game.shop.prices[item.name]
            self.game.hero.inventory.add_item(item)
            self.log_to_text_area(f"Вы купили {item.name}.")
        else:
            self.log_to_text_area("Недостаточно золота для покупки!")

    def log_to_text_area(self, text):
        """Выводит текст в текстовое поле."""
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)

    def clear_window(self):
        """Очищает окно."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game_window = GameWindow(root)
    root.mainloop()
