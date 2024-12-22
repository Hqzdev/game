from items.weapon import Weapon
from items.armor import Armor
from items.boots import Boots

class Shop:
    def __init__(self):
        self.items = []
        self.prices = {}
        self.generate_items()

    def generate_items(self):
        rarities = ["Обычная", "Редкая", "Эпическая", "Легендарная"]
        for rarity in rarities:
            self.add_item(Armor(f"{rarity} Броня", "", defense=3 * (rarities.index(rarity) + 1)), price=60 * (rarities.index(rarity) + 1))
            self.add_item(Weapon(f"{rarity} Меч", "", attack=5 * (rarities.index(rarity) + 1)), price=70 * (rarities.index(rarity) + 1))

    def add_item(self, item, price):
        self.items.append(item)
        self.prices[item.name] = price

    def display_items(self, hero):
        print(f"\n--- Магазин ---\nБаланс: {hero.gold} золота")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item.name} (Цена: {self.prices[item.name]} золота)")

    def buy_item(self, hero, item_idx):
        if 0 <= item_idx < len(self.items):
            item = self.items[item_idx]
            price = self.prices[item.name]
            if hero.gold >= price:
                hero.gold -= price
                hero.inventory.add_item(item)
                print(f"Вы купили {item.name} за {price} золота!")
            else:
                print("Недостаточно золота!")
        else:
            print("Некорректный выбор.")