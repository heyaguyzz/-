result = []

def divider(a, b):
    if a < b:
        raise ValueError("a повинно бути >= b")
    if b > 100:
        raise IndexError("b не повинно бути > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # Видалено некоректний ключ (список)

for key, value in data.items():
    try:
        res = divider(int(key), int(value))  # Конвертуємо ключ та значення у int
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Помилка: {e}")

print(result)
