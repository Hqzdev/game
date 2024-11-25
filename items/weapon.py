from items.item import Item


class Weapon(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack

    def use(self, hero):
        hero.power_damage += self.attack
        print(f"{hero.name} теперь имеет увеличенный урон на {self.attack}.")

    def __str__(self):
        return f"{self.name} (Оружие): {self.description}, Урон: {self.attack}"
