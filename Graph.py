#coding=utf-8

"""
Graf w przestrzeni
"""

from abc import ABCMeta, abstractmethod

class GraphBase(metaclass=ABCMeta):
    """
    Wierzchołki w przestrzeni
    Kompozycja
    """
    _dimension = None  # atrybut klasy

    @abstractmethod
    def __init__(self, spaceObj, weight, point_list):
        # type: (Union[Sphere, Any], Union[int, float], List[Point]) -> None

        self.space = spaceObj  # przestrzeń
        self.weight = weight
        self.point_list = point_list

    @abstractmethod
    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        """
        Sprawdzanie czy pomiędzy punktami istnieje krawędź
        """
        pass

    @abstractmethod
    def createGraphMatrix(self):
        """
        Zwraca mapę sąsiedztwa między punktami
        """
        pass


class Graph1D(GraphBase):

    def __init__(self, spaceObj, weight, point_list):
        # type: (Union[Sphere, Any], Union[int, float], List[Point]) -> None
        super(Graph1D, self).__init__(spaceObj, weight, point_list)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        pass

    def createGraphMatrix(self):
        pass


class Graph2D(Graph1D):

    def __init__(self, spaceObj, weight, point_list):
        # type: (Union[Sphere, Any], Union[int, float], List[Point]) -> None
        # kompozycja
        super(Graph2D, self).__init__(spaceObj, weight, point_list)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        pass

    def createGraphMatrix(self):
        pass


class Graph3D:

    def __init__(self, spaceObj, weight, point_list):
        # type: (Union[Sphere, Any], Union[int, float], List[Point]) -> None
        # kompozycja
        super(Graph2D, self).__init__(spaceObj, weight, point_list)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        pass

    def createGraphMatrix(self):
        pass
