# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_numbers = []
for number in range(16):
    list_numbers.append({'bin': bin(number), 'dec': number, 'hex':hex(number), 'oct': oct(number)})

pprint(list_numbers)
