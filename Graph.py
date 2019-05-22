#coding=utf-8

"""
Graf w przestrzeni
"""

from abc import ABCMeta, abstractmethod
import numpy as np

from point import PointBase, Point1D, Point2D
from sphere import Sphere2D, SphereBase


class GraphBase(metaclass=ABCMeta):
    """
    Wierzchołki w przestrzeni
    Kompozycja
    """
    _dimension = None  # atrybut klasy

    @abstractmethod
    def __init__(self, spaceObj, weight, point_list):
        # type: (Union[SphereBase, Any], Union[int, float], List[PointBase]) -> None

        self.spaceObj = spaceObj  # przestrzeń
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
    def isPointInSphere(self, point):
        # type(Point) -> None
        """
        Sprawdza czy punkt znjaduje się w przestzeni
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
        # type: (Sphere, Union[int, float], List[Point1D]) -> None
        super(Graph1D, self).__init__(spaceObj, weight, point_list)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        pass

    def createGraphMatrix(self):
        pass

    def isPointInSphere(self, point):
        # type(Point) -> None
        pass


class Graph2D(Graph1D):

    def __init__(self, spaceObj, weight, point_list):
        # type: (Sphere2D, Union[int, float], List[Point]) -> None
        # kompozycja
        super(Graph2D, self).__init__(spaceObj, weight, point_list)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point2D) -> bool
        """
        Krawędź miedzy wierzchołkami jest wtedy, gdy odległośc między nimi <= (2*waga)**2
        """
        if (abs(pointA.x - pointB.x)**2 + abs(pointA.y - pointB.y)**2) <= 4*(self.weight**2):
            return True

        return False

    def isPointInSphere(self, point):
        # type(Point2D) -> bool
        """
        Z równania okręgu
        x**2 + y**2 <= r**
        """
        if ((point.x**2) + (point.y**2)) <= self.spaceObj.getRadius():
            return True
        return False

    def createGraphMatrix(self):
        matrixSize = len(self.point_list)
        graphMatrix = np.zeros((matrixSize, matrixSize))


        for index1, point1 in enumerate(self.point_list):
            for index2, point2 in enumerate(self.point_list):
                if self.checkEdgeBetweenPointsExists(point1, point2):
                    graphMatrix[index1][index2] = 1


        print("------- graphMatrix -------")
        print(graphMatrix)
        return graphMatrix



    def __str__(self):
        return "Graf na płaszczyźnie 2D"


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

    def isPointInSphere(self, point):
        # type(Point) -> None
        """
        """
        pass
