# coding=utf-8
"""
----------------------------- NADAJNIKI ------------------------------------
Trzeba wizualizowa� :<
Tutaj s� grafy nieskierowane, to nie interesuje nasz kierunek :)
Zak�adam �e m�j okr�g zaczyna sie w punkcie 0,0 - ca�e miasto

wiercho�ek jako nadajnik o odpowiendnim zasi�gu
"""
from typing import Union, List
from abc import ABCMeta, abstractmethod

from Graph import Graph2D, GraphBase

totalPointNumber = 10
cityRadius = 20
transmitterWeight = 10


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
        super(Transmitters2D, self).__init__(totalPoints, cityRadius, weight)

    def createRandomGraphMatrix(self):
        # type:() -> Graph2D
        graph2D = Graph2D.fromEmptyPointsAndEmptySphere(self.cityRadius, self.totalPoints)
        return graph2D.createGraphMatrix(self.weight)

def main():
    transmitters2D = Transmitters2D(totalPointNumber, cityRadius, transmitterWeight)
    graphMatrix = transmitters2D.createRandomGraphMatrix()
    print(graphMatrix)

if __name__ == "__main__":
    main()

