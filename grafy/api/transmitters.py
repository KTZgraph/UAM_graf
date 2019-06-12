# coding=utf-8
"""
----------------------------- NADAJNIKI ------------------------------------
Trzeba wizualizowa� :<
Tutaj s� grafy nieskierowane, to nie interesuje nasz kierunek :)
Zak�adam �e m�j okr�g zaczyna sie w punkcie 0,0 - ca�e miasto

wiercho�ek jako nadajnik o odpowiendnim zasi�gu
"""
from typing import Union
from abc import ABCMeta, abstractmethod

from api.Graph import Graph2D, GraphBase
from api.global_sight_xml_converter import GlobalSightXMLConverter

# totalPointNumber = 2
# cityRadius = 10
# transmitterWeight = 5


class TransmittersBase(metaclass=ABCMeta):
    def __init__(self, totalPoints, cityRadius, weight):
        self.totalPoints = totalPoints
        self.cityRadius = cityRadius
        self.weight = weight

    @abstractmethod
    def createRandomGraphMatrix(self):
        # type:()->GraphBase
        """Tworzy losowy graf"""
        pass


class Transmitters1D(TransmittersBase):
    def __init__(self, totalPoints, cityRadius, weight):
        # type:(int, Union[int, float], Union[int, float])
        super(Transmitters1D, self).__init__(totalPoints, cityRadius, weight)

    def createRandomGraphMatrix(self):
        pass


class Transmitters2D(Transmitters1D):
    def __init__(self, totalPoints, cityRadius, weight):
        self.point_list = None
        self.grapnMatrix = None
        self.weight = None
        super(Transmitters2D, self).__init__(totalPoints, cityRadius, weight)
        self.createRandomGraphMatrix()


    def createRandomGraphMatrix(self):
        # type:() -> Graph2D
        graph2D = Graph2D.fromEmptyPointsAndEmptySphere(self.cityRadius, self.totalPoints, self.weight)
        self.weight = graph2D.weight
        self.grapnMatrix = graph2D.createGraphMatrix()
        self.point_list = graph2D.point_list

    def convertToXML(self):
        """Zwraca macierz grafu z punnktami wierzchołków w postaci XML"""
        return GlobalSightXMLConverter.converToXml(self.grapnMatrix, self.point_list, self.weight, self.cityRadius)
