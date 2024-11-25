from items.item import Item

class Boots(Item):
    def __init__(self, name, description, speed):
        super().__init__(name, "низ")  # Устанавливаем тип "низ" для обуви
        self.description = description
        self.speed_bonus = speed # Добавляем атрибут для бонуса к скорости

    def use(self, hero):
        hero.speed += self.speed  # Увеличиваем скорость героя на значение бонуса
        print(f'{hero.name} теперь имеет увеличенную скорость на {self.speed}.')

    def __str__(self):
        return f"{self.name} (Ботинки): {self.description}, Бонус к скорости: {self.speed}"
