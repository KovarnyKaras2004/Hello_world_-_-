print('=== Анализ последовательности ДНК ===\n')

dnk = input('Введите последовательность ДНК:\n')

dnk = dnk.upper()
print(f'Последовательность в верхнем регистре: {dnk}\n')

print(f"Подсчёт нуклеотидов:\nA:{dnk.count('A')}\nT:{dnk.count('T')}\nG:{dnk.count('G')}\nC:{dnk.count('C')}\n\nОбщая длина: {len(dnk)} нуклеотидов")

