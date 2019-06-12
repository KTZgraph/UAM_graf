#coding=utf-8
"""
Przestrzenie miast
np. przestzeń 2D to okrąg gdzie znajdując się obkeity klasy Point2D
"""

from abc import ABCMeta, abstractmethod

class SphereBase(metaclass=ABCMeta):
    """
    Klasa abstrakcyjna ~= Sphere z przykłaów
    """
    _dimension = None  # atrybut klasy

    @abstractmethod
    def __init__(self, radius):
        #type: (Union[float, int]) -> None
        self._radius = radius

    def getRadius(self):
        return self._radius

    def getDimension(self):
        # type: () -> Union[int, float]
        """
        Zwraca wymiar sfery
        """
        return self._dimension

    @abstractmethod
    def isCoordinatesInSphere(self, point):
        # type: (Point) -> bool
        """
        Sprawdza czy punkt znajduje się w sferze
        """
        pass


class Sphere1D(SphereBase):
    """
    Przestrzen jednowymiarowa
    """
    _dimension = 1  # atrybut klasy

    def __init__(self, radius):
        super(Sphere1D, self).__init__(radius)

    def isCoordinatesInSphere(self, point):
        # type: (Point) -> bool
        """
        Sprawdza czy punkt znajduje się w sferze
        """
        pass


class Sphere2D(SphereBase):
    """
    Przestrzen jednowymiarowa
    """
    _dimension = 2  # atrybut klasy

    def __init__(self, radius):
        super(Sphere2D, self).__init__(radius)

    def isCoordinatesInSphere(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> bool
        """
        Sprawdza czy punkt znajduje się w sferze

        # liczenie odleglosci od srodka
        # rownanie okregu ktorego srodek jest w punkcjie 0,0
        # to x**2 + y**2 = r **2; nierownosc sprawdza czy punkt P(x,y)
        # znajduje sie okregu o środku w punkcie (0,0)
        """
        if x is None or y is None:
            return False

        if (((x - 0) ** 2) + ((y - 0) ** 2)) <= (self._radius ** 2):
            return True

        return False

