class BattleLog:
    log = []
    victories = 0
    defeats = 0
    draws = 0

    @classmethod
    def log_victory(cls) -> None:
        cls.victories += 1
        cls.log.append('Победа!')

    @classmethod
    def log_defeat(cls) -> None:
        cls.defeats += 1
        cls.log.append('Поражение!')

    @classmethod
    def log_draw(cls) -> None:
        cls.draws += 1
        cls.log.append('Ничья!')

    @classmethod
    def log_battle(cls, hero_action: str, enemy_action: str) -> None:
        cls.log.append(hero_action)
        cls.log.append(enemy_action)

    @classmethod
    def stats(cls) -> dict:
        return {
            'victories': cls.victories,
            'defeats': cls.defeats,
            'draws': cls.draws,
            'log': cls.log
        }
