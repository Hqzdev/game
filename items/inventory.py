class Inventory:
    def __init__(self, capacity=10):
        """
        Инициализация инвентаря.
        :param capacity: Максимальная вместимость инвентаря (по умолчанию 10).
        """
        self.capacity = capacity
        self.items = []  # Список предметов в инвентаре
        print(f"Инвентарь создан. Вместимость: {self.capacity}")

    def add_item(self, item):
        """
        Добавление предмета в инвентарь.
        :param item: Объект предмета, который добавляется в инвентарь.
        :return: True, если добавление прошло успешно, иначе False.
        """
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item.name} добавлен в инвентарь.")
            return True
        else:
            print("Инвентарь переполнен! Увеличьте вместимость или освободите место.")
            return False

    def remove_item(self, item_name):
        """
        Удаление предмета из инвентаря по имени.
        :param item_name: Имя предмета для удаления.
        :return: True, если удаление прошло успешно, иначе False.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} удалён из инвентаря.")
                return True
        print(f"Предмет с именем '{item_name}' не найден в инвентаре.")
        return False

    def display_inventory(self):
        """
        Вывод содержимого инвентаря.
        """
        if self.items:
            print("\n--- Инвентарь ---")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")
        else:
            print("\nИнвентарь пуст.")

    def is_full(self):
        """
        Проверка, заполнен ли инвентарь.
        :return: True, если инвентарь заполнен, иначе False.
        """
        return len(self.items) >= self.capacity
