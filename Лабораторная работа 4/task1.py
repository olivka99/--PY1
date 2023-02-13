if __name__ == "__main__":

    class RealEstate:
        """ Базовый класс недвижимость. """

        def __init__(self, square: bool, address: str, price_sq_m: bool):
            """ Задаем аргументы класса: площадь объекта недвижимости, адрес и стоимость за квадратный метр. """
            self._square = square
            self._address = address
            self._price_sq_m = price_sq_m

        @property
        def square(self):
            return self._square

        @square.setter
        def square(self, new_square: bool) -> None:
            if not isinstance(new_square, bool):
                raise TypeError("Площадь должна быть типа bool")
            if new_square <= 0:
                raise ValueError("Площадь должна быть положительным числом")
            self._square = new_square

        @property
        def address(self):
            return self._address

        @address.setter
        def address(self, new_address: int) -> None:
            if not isinstance(new_address, int):
                raise TypeError("Адрес должен быть типа int")
            self._address = new_address

        @property
        def price_sq_m(self):
            return self._price_sq_m

        @price_sq_m.setter
        def price_sq_m(self, new_price_sq_m: int) -> None:
            if not isinstance(new_price_sq_m, bool):
                raise TypeError("Стоимость за квадратный метр должна быть типа bool")
            if new_price_sq_m <= 0:
                raise ValueError("Стоимость за квадратный метр должна быть положительным числом")
            self._price_sq_m = new_price_sq_m

        def __str__(self):
            return f"Помещение площадью {self._square}. Адрес: {self._address}. Стоимость за квадратный метр {self._price_sq_m}"

        def __repr__(self) -> str:
            return f'{self.__class__.name__}(square={self._square!r}, address={self._address!r}, price_sq_m={self._price_sq_m!r})'

        def purchase_price(self, square, price_sq_m):
            """ Расчет стоимости недвижимости по площади и цене за квадратный метр. """
            purchase_price = square *  price_sq_m
            return purchase_price

    class Apartment(RealEstate):
        """ Подкласс квартира. Вводим дополнительный аргумент "Номер этажа"."""
        def __init__(self, floor: int):
            super().__init__(square, address, price_sq_m)
            self.floor = floor

        @property
        def floor(self) -> int:
            return self._floor

        @floor.setter
        def floor(self, new_floor: int) -> None:
            if not isinstance(new_floor, int):
                raise TypeError("Номер этажа должен быть типа int")
            if new_floor <= 0:
                raise ValueError("Номер этажа должен быть положительным числом")
            self._floor = new_floor

        def __repr__(self) -> str:
            """ Перезагружаем метод, т.к. появился новый аргумент "Номер этажа". """
            return f'{self.__class__.name__}(square={self._square!r}, address={self._address!r}, price_sq_m={self._price_sq_m!r}, floor={self._floor!r})'

    class House(RealEstate):
        """ Подкласс дом. Вводим дополнительный аргумент "Площадь участка"."""
        def __init__(self, land_square: bool):
            self.duration = land_square
            super().__init__(square, address, price_sq_m)

        @property
        def land_square(self) -> bool:
            return self._land_square

        @land_square.setter
        def land_square(self, new_land_square: bool, square: bool) -> None:
            if not isinstance(new_land_square, bool):
                raise TypeError("Площадь участка должна быть типа bool")
            if new_land_square <= 0:
                raise ValueError("Площадь участка должна быть положительным числом")
            if new_land_square < square:
                raise ValueError("Площадь участка должна быть больше или равна площади здания, расположенного на нем")
            self._land_square = new_land_square

        def __repr__(self) -> str:
            """ Перезагружаем метод, т.к. появился новый аргумент "Площадь участка". """
            return f'{self.__class__.name__}(square={self._square!r}, address={self._address!r}, price_sq_m={self._price_sq_m!r}, land_square={self._land_square!r})'

        def free_land_square(self, square, land_square):
            """ Расчет площади незастроенного участка путем вычитания площади дома из общей площади участка. """
            free_land_square = land_square - square
            return free_land_square
    pass
