from game.battle_log import BattleLog


def display_statistics():
    print("\n--- Общая статистика ---")
    stats = BattleLog.stats()
    print(f"Победы: {stats['victories']}")
    print(f"Поражения: {stats['defeats']}")
    print(f"Ничьи: {stats['draws']}")
    print("-------------------------")