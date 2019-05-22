#coding=utf-8
"""
Nie da się zrobic fabryki [!]
bo każdy z punktów  przestrzeni ma inny interfejs
"""
from abc import ABCMeta, abstractmethod

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

    @staticmethod
    @abstractmethod
    def createRandomPointInSphere(sphere):
        """
        Tworzy punkt z losowymi współrzednymi znajdującymi się w przestrzeni
        """
        pass

    @abstractmethod
    def createConretePoint(self):
        """
        Tworzy punkt z zadanymi parametrami
        """
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

    def createConretePoint(self, x):
        """
        Tworzy punkt z zadanymi parametrami
        """
        pass

    def __str__(self):
        return f'"x" : {self._x}'

    def __eq__(self, other):
        # type (Point) -> bool
        if self.x == other.x:
            return True
        return False

    @staticmethod
    def createRandomPointInSphere(sphere):
        pass


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

    @staticmethod
    def createRandomPointInSphere(sphere):
        pass

    def __eq__(self, other):
        # type (Point) -> bool
        if self.x == other.x and self.y == other.y:
            return True
        return False


class Point3D(Point2D):
    """
    Punkt na plaszczzynie dwuwymiarowej - okresla wierczholek
    """
    _dimension = 3  # atrybut klasy

    def __init__(self, x=1, y=2, z=3):
        # type: (Union[int, float], Union[int, float], Union[int, float]) -> None
        self._z = z
        super(Point3D, self).__init__(z)

    @property  # getter atrybut pseudoprywatny
    def z(self):
        # type: () -> int
        return self._z

    @z.setter  # setter atrybut pseudoprywatny
    def z(self, value):
        # type: (Union[int, float]) -> None
        self._z = value

    def __str__(self):
        return super(Point3D, self).__str__() + f', "z": {self._z}'

    @staticmethod
    def createRandomPointInSphere(sphere):
        pass


