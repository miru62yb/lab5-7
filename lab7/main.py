from functions import average, normalize_text, select_numbers, sum_digits
def main():
    num = int(input("Введите число для суммы цифр: "))
    print("Результат:", sum_digits(num))
    raw_nums = input("Введите числа через пробел: ")
    nums = [float(x) for x in raw_nums.split()] if raw_nums.strip() else []
    avg = average(nums)
    print("Среднее:", avg if avg is not None else "Нет данных")
    text = input("Введите текст: ")
    print("Нормализованный текст:", repr(normalize_text(text)))
    threshold = int(input("Введите порог: "))
    print(f"Числа больше {threshold}:", select_numbers(nums, threshold))
if __name__ == "__main__":
    main()
