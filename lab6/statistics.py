data = input('Введите числа: ').split()
if not data:
 print("Нет данных")
else:
    nums = [int(x) for x in data]
    nums.sort()
    print(f"Количество чисел: {len(nums)}")
    print(f"Сумма чисел: {sum(nums)}")
    print(f"Минимальное значение: {nums[0]}")
    print(f"Максимальное значение: {nums[-1]}")
    print(f"Среднее значение: {sum(nums) / len(nums):.2f}")
