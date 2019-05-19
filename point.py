#coding=utf-8
from abc import ABCMeta, abstractmethod

class PointBase(metaclass=ABCMeta):
    """
    Klasa abstrakcyjna ~= Shape z przykłaów
    """
    _dimension = None  # atrybut klasy

    def get_dimension(self):
        return self._dimension

    @abstractmethod
    def get_distance_from_center(self):
        """
        Zwraca odlełosć od środka przestrzeni
        """
        pass

    @abstractmethod
    def create_random_point(self):
        """
        Tworzy punkt z losowymi współrzednymi znajdującymi się w przestrzeni
        """
        pass

    @abstractmethod
    def create_conrete_point(self):
        """
        Tworzy punkt z zadanymi parametrami
        """
        pass


class Point1D(PointBase):
    """
    Punkt na plaszczzynie jednoymiarowej
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

    def get_distance_from_center(self):
        """
        Zwraca odlełosć od środka przestrzeni
        """
        pass

    def create_random_point(self):
        """
        Tworzy punkt z losowymi współrzednymi znajdującymi się w przestrzeni
        """
        pass

    def create_conrete_point(self):
        """
        Tworzy punkt z zadanymi parametrami
        """
        pass

    def __str__(self):
        return f'Point1D: "x" : {self._x}'


class Point2D(Point1D):
    """
    Punkt na plaszczzynie dwuwymiarowej
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
        return f'Point2D: "x" : {self._x}, "y": {self._y}'


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
        return f'Point3D: "x" : {self._x}, "y": {self._y},  "z": {self._z}'


class RandomPointFactory(object):
    """
    Fabryka punktów w odpowiedniej przestrzeni
    """
    @staticmethod
    def createRandomPoint(dimension):
        if dimension == 1:
            return Point1D()
        if dimension == 2:
            return Point2D()
        if dimension == 3:
            return Point3D()
        else:
            print(f"Brak obsługi wymiaru: {dimension}")


if __name__ == "__main__":
    for i in range(1, 5):
        p = RandomPointFactory.createRandomPoint(i)
        print(p)
