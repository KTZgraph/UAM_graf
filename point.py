#coding=utf-8
"""
Nie da się zrobic fabryki [!]
bo każdy z punktów  przestrzeni ma inny interfejs
"""
from abc import ABCMeta, abstractmethod
from random import uniform

from sphere import Sphere2D


class PointBase(metaclass=ABCMeta):
    """
    Klasa abstrakcyjna ~= Shape z przykłaów
    """
    _dimension = None  # atrybut klasy

    def getDimension(self):
        """
        Zwraca wymiar w jakim znajduje się punkt
        """
        return self._dimension

    @abstractmethod
    def getDistanceFromCenter(self):
        """
        Zwraca odlełosć od środka przestrzeni
        """
        pass

    @classmethod
    def fromRandom(cls, sphereRadius): #Kontruktor alternatywny
        # type:(Union[int, float]) -> PointBase
        pass

    @abstractmethod
    def __eq__(self, other):
        # type (Point) -> bool
        pass

class Point1D(PointBase):
    """
    Punkt na plaszczzynie jednoymiarowej

    ¯\_(ツ)_/¯
    @note: w sumie jednowymiarowy punkt też może znaleźć się w 2D i 3D sferze #TODO
    """
    _dimension = 1  # atrybut klasy

    def __init__(self, x=1):
        # type: (Union[int, float]) -> None
        self._x = x
        super(Point1D, self).__init__()

    @property  # getter atrybut pseudoprywatny
    def x(self):
        # type: () -> int
        return self._x

    @x.setter  # setter atrybut pseudoprywatny
    def x(self, value):
        # type: (Union[int, float]) -> None
        self._x = value

    def getDistanceFromCenter(self):
        """
        Zwraca odlełosć od środka przestrzeni
        """
        pass

    @classmethod
    def fromRandom(cls, sphereRadius): # Kontruktor alternatywny
        # type:(Union[int, float]) -> PointBase
        pass

    def __str__(self):
        return f'"x" : {self._x}'

    def __eq__(self, other):
        # type (Point) -> bool
        if self.x == other.x:
            return True
        return False


class Point2D(Point1D):
    """
    Punkt na plaszczzynie dwuwymiarowej

    ¯\_(ツ)_/¯
    @note: w sumie dwuwymiarowy punkt też może znaleźć się w 2D i 3D sferze #TODO
    """
    _dimension = 2  # atrybut klasy


    def __init__(self, x=1, y=2):
        # type: (Union[int, float], Union[int, float]) -> None
        self._y = y
        super(Point2D, self).__init__(x)

    @property
    def y(self):  # setter atrybut pseudoprywatny
        # type: ()-> Union[int, float]
        return self._y

    @y.setter
    def y(self, value):  # getter atrybut pseudoprywatny
        # type: (Union[int, float]) -> None
        self._y = value

    def __str__(self):
        return super(Point2D, self).__str__() + f', "y": {self._y}'

    @classmethod
    def fromRandom(cls, sphereRadius):
        # type:(UInion[int, float]) -> Point2D
        """
        Losowy punkt w przestrzeni
        """
        sphere2D = Sphere2D(sphereRadius)
        x, y = None, None
        circleRange = sphereRadius**2

        while not (sphere2D.isCoordinatesInSphere(x, y)):
            x = uniform((-1*circleRange), circleRange)
            y = uniform((-1*circleRange), circleRange)

        return cls(x, y)

    def __eq__(self, other):
        # type (Point) -> bool
        if self.x == other.x and self.y == other.y:
            return True
        return False



