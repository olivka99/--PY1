import doctest


class Plane:
    def __init__(self, capacity: int, sold_tickets: int):
        """
        Создание и подготовка к работе объекта "Самолет"
        :param capacity: Вместимость самолета
        :param sold_tickets: Количество проданных блетов
        Примеры:
        >>> plane = Plane(174, 50)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int)):
            raise TypeError("Вместимость самолета должна быть типа int")
        if capacity < 0:
            raise ValueError("Вместимость самолета должна быть положительным числом")
        self.capacity = capacity

        if not isinstance(sold_tickets, (int)):
            raise TypeError("Количество проданных билетов должен быть int")
        if sold_tickets < 0:
            raise ValueError("Количество проданных билетов не может быть отрицательным числом")
        self.sold_tickets = sold_tickets

    def is_sold_out(self) -> bool:
        """
        Функция, которая проверяет проданы ли все билеты
        :return: Проданы ли все билеты
        Примеры:
        >>> plane = Plane(174, 174)
        >>> plane.is_sold_out()
        """
        ...

    def buy_tickets(self, buy_numbers: int) -> None:
        """
        Покупка билетов.
        :param buy_numbers: Количество приобретаемых билетов
        :raise ValueError: Если количество приобретаемых билетов превышает количество имеющихся в продаже, то вызываем ошибку
        Примеры:
        >>> plane = Plane(174, 174)
        >>> plane.buy_tickets(1)
        """
        if not isinstance(buy_numbers, (int)):
            raise TypeError("Количество приобретаемых билетов должно быть типа int")
        if buy_numbers < 0:
            raise ValueError("Количество приобретаемых билетов должно быть положительным числом")
        ...

    def refund_tickets(self, refund_numbers: int) -> None:
        """
        Возврат билетов.
        :param refund_numbers: Количество возвращаемых билетов
        :raise ValueError: Если количество возвращаемых билетов превышает количество купленных,
        то возвращается ошибка.
        :return: Количество реально возвращаемых билетов
        Примеры:
        >>> plane = Plane(174, 1)
        >>> plane.refund_tickets(2)
        """
        if not isinstance(refund_numbers, (int)):
            raise TypeError("Количество возвращаемых билетов должно быть типа int")
        if refund_numbers < 0:
            raise ValueError("Количество возвращаемых билетов должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
