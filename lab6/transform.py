data = input('Введите исходный список: ').split()
original_list = [int(x) for x in data]
transformed_list = [abs(x) for x in original_list]
print(f'Исходный список: {original_list}')
print(f'Преобразованный список: {transformed_list}')
