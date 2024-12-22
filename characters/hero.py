class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, gender, spells, radius, weaknesses,
                 speed, intelligence, power, agility, lucky, power_damage, exp, inventory, gold=100):
        self.lvl = lvl
        self.name = name
        self.last_name = last_name
        self.lor = lor
        self.history = history
        self.hp = hp
        self.old = old
        self.gender = gender
        self.spells = spells
        self.radius = radius
        self.weaknesses = weaknesses
        self.speed = speed
        self.intelligence = intelligence
        self.power = power
        self.agility = agility
        self.lucky = lucky
        self.power_damage = power_damage
        self.exp = exp
        self.inventory = inventory
        self.gold = gold
    def __str__(self):
        return f"{self.name} {self.last_name} (Уровень: {self.lvl}, Золото: {self.gold})"

    def attack(self):

        
        return self.power_damage

    def add_item_to_inventory(self, item):
        """
        Добавляет предмет в инвентарь героя.
        :param item: Объект предмета.
        """
        if self.inventory.add_item(item):
            pass

    def use_item(self, item_name):
        """
        Использует предмет из инвентаря.
        :param item_name: Название предмета.
        """
        for item in self.inventory.items:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove_item(item_name)
                return


    def show_inventory(self):
        """
        Отображает содержимое инвентаря.
        """
        print(f"\nИнвентарь {self.name}:")
        self.inventory.display_inventory()
