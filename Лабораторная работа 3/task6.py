list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_index = 0
max_number = list_numbers[0]

for i, current_number in enumerate(list_numbers):  # перебираем числа
    if current_number >= max_number:  # если текущее число больше того, что встречали ранее
        max_index = i  # то перезаписываем индекс максимального числа
        max_number = current_number  # и перезаписываем число

list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]  # меняем местами максимальное и последнее число

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
