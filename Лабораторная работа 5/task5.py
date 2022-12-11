import random
import string


ef get_random_password(n=8) -> str:
    allowed_chars = ascii_letters + digits  # TODO написать функцию генерации случайных паролей
    if not n:
        password = ''.join(sample(allowed_chars, 8))
    else:
        password = ''.join(sample(allowed_chars, n))
    return password


print(get_random_password(9))
print(get_random_password(7))
print(get_random_password(20))
print(get_random_password())
