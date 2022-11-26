salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

for _ in range(1, months + 1):  # прокручиваем все месяцы по 10-й включительно
    money_capital += spend - salary  # разница между тратами и зарплатой / копим подушку безопасности
    spend *= spend * increase  # учитываем рост цен

print(round(money_capital))
