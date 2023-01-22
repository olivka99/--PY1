import doctest


class Microclimate:
    def __init__(self, temperature: float, humidity: int, fug: float):
        """
        Создание и подготовка к работе объекта "Микроклимат"
        :param temperature: Температура воздуха в градусах
        :param humidity: Влажность воздуха в процентах
        :param fug: Запыленность воздуха в мг/м3
        Примеры:
        >>> microclimate = Microclimate(21.5, 70, 0.01)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура воздуха должна быть типа int или float")
        self.temperature = temperature

        if not isinstance(humidity, (int)):
            raise TypeError("Влажность воздуха должна быть int")
        if 0 > humidity > 100:
            raise ValueError("Влажность воздуха в процентах не может быть меньше 0 и больше 100")
        self.humidity = humidity

        if not isinstance(fug, (int, float)):
            raise TypeError("Запыленность воздуха должна быть int или float")
        if fug < 0:
            raise ValueError("Запыленность воздуха должны быть положительным числом")
        self.fug = fug

    def optimal_microclimate(self) -> bool:
        """
        Функция, которая проверяет соответсвуют параметры микроклимата оптимальным значениям
        :return: Оптимальны ли параметры микроклимата
        Примеры:
        >>> microclimate = Microclimate(21.5, 70, 0.01)
        >>> microclimate.optimal_microclimate()
        """
        ...

    def changing_values(self, temperature_change: float, humidity_change: int, fug_change: float) -> None:
        """
        Изменение параметров микроклимата.
        :param temperature_change: Значение на которое повысится или понизится температура
        :param humidity_change: Значение на которое повысится или понизится влажность
        :param fug_change: Значение на которое понизится запыленность помещения
        :raise ValueError: Если значения параметров микроклимата превышают допустимые, то вызываем ошибку
        Примеры:
        >>> microclimate = Microclimate(21.5, 70, 0.01)
        >>> microclimate.changing_values(100, 100, 100)
        """
        if not isinstance(temperature_change, (int, float)):
            raise TypeError("Температура воздуха должна быть типа int или float")

        if not isinstance(humidity_change, (int)):
            raise TypeError("Влажность воздуха должна быть типа int")
        if 100 < humidity_change < - 100:
            raise ValueError("Влажность воздуха в процентах не может быть меньше 0 и больше 100")

        if not isinstance(fug_change, (int, float)):
            raise TypeError("Запыленность воздуха должна быть int или float")
        if fug_change > 0:
            raise ValueError("Невозможно увеличить значение запыленности")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
