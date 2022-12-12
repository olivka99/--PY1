from random import sample
from string import ascii_letters, digits


def get_random_password(n=8) -> str:
    password = ''.join(sample(ascii_letters + digits, n))  # TODO написать функцию генерации случайных паролей
    return password


print(get_random_password(9))
print(get_random_password(7))
print(get_random_password(20))
print(get_random_password())
