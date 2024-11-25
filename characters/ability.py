class Ability:
    def __init__(self, name: str, damage: int, cooldown: int):
        self.name = name
        self.damage = damage
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self) -> int:
        if self.current_cooldown == 0:
            self.current_cooldown = self.cooldown
            return self.damage
        else:
            print(f'Способность {self.name} на перезарядке')
            return 0

    def update(self) -> None:
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
