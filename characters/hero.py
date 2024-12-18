class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, gender, spells, radius, weaknesses,
                 speed, intelligence, power, agility, lucky, power_damage, exp, inventory, gold=100):
        """
        Инициализация героя.
        :param lvl: Уровень героя.
        :param name: Имя героя.
        :param last_name: Фамилия героя.
        :param lor: Лор героя.
        :param history: История героя.
        :param hp: Очки здоровья героя.
        :param old: Возраст героя.
        :param gender: Пол героя.
        :param spells: Заклинания героя.
        :param radius: Радиус атак или эффектов героя.
        :param weaknesses: Слабости героя.
        :param speed: Скорость героя.
        :param intelligence: Интеллект героя.
        :param power: Сила героя.
        :param agility: Ловкость героя.
        :param lucky: Удача героя.
        :param power_damage: Урон героя.
        :param exp: Опыт героя.
        :param inventory: Инвентарь героя.
        :param gold: Золото героя.
        """
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
        print(f"Герой {self.name} {self.last_name} создан! Уровень: {self.lvl}, Золото: {self.gold}")

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
