from items.item import Item


class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense  
    
    def use(self, hero):
        hero.defense += self.defense
        print(f"{hero.name} теперь имеет увеличенную защиту на {self.defense}.")

    def __str__(self):
        return f"{self.name} (Броня): {self.description}, Защита: {self.defense}"
