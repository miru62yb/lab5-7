data = input('Введите числа через пробел: ').split()
if not data:
    print("Нет данных")
else:
    numbers = [int(x) for x in data]
    max_value = max(numbers)
    max_indices = [index for index, value in enumerate(numbers) if value == max_value]
    print(f"Индексы максимального значения: {max_indices}")