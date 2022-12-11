import random
import string

n = 8


def get_random_password(n) -> str:
    allowedChars = string.ascii_letters + string.digits  # TODO написать функцию генерации случайных паролей
    password = ''.join(random.sample(allowedChars, n))
    return password


print(get_random_password(15))
print(get_random_password(3))
