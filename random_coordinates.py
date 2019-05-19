#coding=utf-8
from abc import ABCMeta, abstractmethod

class RandomCoordinatesBase(metaclass=ABCMeta):
    """
    Zwraca randomowe współrzędne punktów
    """
    @abstractmethod
    def get_random_coordinates(self):
        pass



class RandomCoordinates2D(RandomCoordinatesBase):
    """
    Zwraca losowe współrzędne dla punktów w drugim wymiarze
    """

    def __init__(self, circleRadius):
        self.circleRadius = circleRadius

    def get_random_coordinates(self):
        return 1, 2.0

class RandomCoordinates3D(RandomCoordinatesBase):
    """
    Zwraca losowe współrzędne dla punktów w trzecim wymiarze
    """
    def __init__(self, sphereRadius):

        self.sphereRadius= sphereRadius

    def get_random_coordinates(self):
        # type() -> Tuple(Union[int, float])
        return 1.0, 2, 3.1
