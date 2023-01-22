import doctest


class CreditCard:
    def __init__(self, creditcard_volume: int, credit_volume: float):
        """
        Создание и подготовка к работе объекта "Кредитная карта"
        :param creditcard_volume: Одобренный размер кредита
        :param credit_volume: Размер долга
        Примеры:
        >>> credit_card = CreditCard(20000, 0)  # инициализация экземпляра класса
        """
        if not isinstance(creditcard_volume, (int)):
            raise TypeError("Размер одобренного кредита должен быть типа int")
        if creditcard_volume <= 0:
            raise ValueError("Размер одобренного кредита должен быть положительным числом")
        self.creditcard_volume = creditcard_volume

        if not isinstance(credit_volume, (int, float)):
            raise TypeError("Размер долга должен быть int или float")
        if credit_volume < 0:
            raise ValueError("Размер долга не может быть отрицательным числом")
        self.credit_volume = credit_volume

    def is_empty_credit_card(self) -> bool:
        """
        Функция, которая проверяет исчерпан ли лимит кредита
        :return: Исчерпан ли лимит кредита
        Примеры:
        >>> credit_card = CreditCard(20000, 0)
        >>> credit_card.is_empty_credit_card()
        """
        ...

    def make_a_payment(self, payment: float) -> None:
        """
        Внесение платежа в кредит.
        :param payment: Размер внесенного платежа
        :raise ValueError: Если размер внесенного платежа превышает размер долга, то вызываем ошибку
        Примеры:
        >>> credit_card = CreditCard(20000, 0)
        >>> credit_card.make_a_payment(3000)
        """
        if not isinstance(payment, (int, float)):
            raise TypeError("Размер платежа должен быть типа int или float")
        if payment < 0:
            raise ValueError("Размер платежа должен быть положительным числом")
        ...

    def credit_spending(self, spending_volume: float) -> None:
        """
        Траты по кредиту.
        :param spending_volume: Размер потраченных денег
        :raise ValueError: Если размер потраченных денег превышает остаток по кредиту,
        то возвращается ошибка.
        :return: Объем реально потраченных денег
        Примеры:
        >>> credit_card = CreditCard(20000, 20000)
        >>> credit_card.credit_spending(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
