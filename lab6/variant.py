data = input('Введите числа через пробел: ').split()
if not data:
    filtered = []
else:
    numbers = [int(x) for x in data]
    filtered = [x for x in numbers if x % 2 == 0]
count = len(filtered)
total_sum = sum(filtered)
sorted_copy = sorted(filtered)
print(f'Чётные числа: {filtered}')
print(f'Количество: {count}')
print(f'Сумма: {total_sum}')
print(f'Отсортированные числа: {sorted_copy}')