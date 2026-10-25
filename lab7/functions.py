def sum_digits(number):
    total = 0
    n = abs(number)
    while n > 0:
        total += n % 10
        n //= 10
    return total
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
def normalize_text(text):
    return " ".join(text.lower().split())
def select_numbers(numbers, threshold):
    return [x for x in numbers if x > threshold]
