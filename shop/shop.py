from items.weapon import Weapon
from items.armor import Armor
from items.boots import Boots
from items.item import Item


class Shop:
    def __init__(self):
        self.items = []
        self.prices = {}
        self.generate_items()

    def generate_items(self):
        rarities = ["Обычная", "Редкая", "Эпическая", "Легендарная"]

        for rarity in rarities:
            # Шлем
            self.add_item(Armor(
                name=f"{rarity} Шлем",
                description=f"Шлем с бонусом ({rarity})",
                defense=2 * (rarities.index(rarity) + 1)
            ), price=40 * (rarities.index(rarity) + 1))
            
            # Броня
            self.add_item(Armor(
                name=f"{rarity} Броня",
                description=f"Броня с бонусом ({rarity})",
                defense=3 * (rarities.index(rarity) + 1)
            ), price=60 * (rarities.index(rarity) + 1))

            # Ботинки
            self.add_item(Boots(
                name=f"{rarity} Ботинки",
                description=f"Ботинки с бонусом ({rarity})",
                speed=2 * (rarities.index(rarity) + 1)
            ), price=30 * (rarities.index(rarity) + 1))
            
            # Оружие
            self.add_item(Weapon(
                name=f"{rarity} Меч",
                description=f"Меч с бонусом ({rarity})",
                attack=5 * (rarities.index(rarity) + 1)
            ), price=70 * (rarities.index(rarity) + 1))

    def add_item(self, item, price):
        """Добавление предмета в магазин."""
        self.items.append(item)
        self.prices[item.name] = price

    def display_items(self):
        """Вывод всех предметов магазина с ценами."""
        print("\n--- Магазин ---")
        for i, item in enumerate(self.items, 1):
            price = self.prices[item.name]
            print(f"{i}. {item.name} - {item.description} (Цена: {price} золота)")

    def buy_item(self, hero, item_number):
        """Покупка предмета героем."""
        if 1 <= item_number <= len(self.items):
            item = self.items[item_number - 1]
            price = self.prices[item.name]

            if hero.gold >= price:
                if hero.inventory.add_item(item):  
                    hero.gold -= price
                    print(f"\n{hero.name} купил {item.name} за {price} золота!")
                else:
                    print("\nНевозможно добавить этот предмет в инвентарь.")
            else:
                print("\nНедостаточно золота для покупки.")
        else:
            print("\nНекорректный выбор предмета.")
