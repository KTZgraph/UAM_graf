# coding=utf-8
"""
----------------------------- NADAJNIKI ------------------------------------
Trzeba wizualizowa� :<
[!] Python 2.7.11 [!]
Tutaj s� grafy nieskierowane, to nie interesuje nasz kierunek :)
Zak�adam �e m�j okr�g zaczyna sie w punkcie 0,0 - ca�e miasto

wiercho�ek jako nadajnik o odpowiendnim zasi�gu
"""
from random import randint
from typing import Union, List


class Point:
    """
    Punkt na p�aszczzynie dwuwymiarowej - okresla wierczholek
    """

    def __init__(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> None
        self._x = x
        self._y = y

    @property  # getter atrybut pseudoprywatny
    def x(self):
        # type: () -> int
        return self._x

    @x.setter  # setter atrybut pseudoprywatny
    def x(self, value):
        # type: (Union[int, float]) -> None
        self._x = value


    @property
    def y(self):  # setter atrybut pseudoprywatny
        # type: ()-> Union[int, float]
        return self._y

    @y.setter
    def y(self, value):  # getter atrybut pseudoprywatny
        # type: (Union[int, float]) -> None
        self._y = value

    def __str__(self):
        return f'Point: "x" : {self._x}, "y": {self._y}'

    @staticmethod  # TODO: rozdzielic na klasy randomPoint i ConcretePoint
    def fabricRandomPoint(circleRadius, weight):  # TODO: refaktor circleCalc
        # type: (Union[int, float]) -> Point
        """
        Fabryka tworząca losowy punkt znajdujący w przestrzeni miasta o zadanym okręgu
        """
        x = randint(-1 * circleRadius, circleRadius)
        y = randint(-1 * circleRadius, circleRadius)

        circleCalc = CircleCalculator(circleRadius, weight)  # uzyvie klasy w klasie - do refktoru
        while not circleCalc.checkCoordinatesOfPointInCircle(x, y):
            return Point(x, y)
        else: #TODO poprawic - zwraca czasem None
            Point.fabricRandomPoint(circleRadius, weight) # Rekurencja -  kolejny raz wywoluje funckje gdy �le wylosowano punkty


class CircleCalculator:
    """
    Obliczenia dla punktow
    """
    def __init__(self, circleRadius, weight):
        # type: (Union[int, float], Union[int, float]) -> None
        self.circleRadius = circleRadius
        self.weight = weight

    def checkCoordinatesOfPointInCircle(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> bool
        """
        Checks coordinates (x,y) are in circle

        # liczenie odleglosci od srodka
        # rownanie okregu ktorego srodek jest w punkcjie 0,0
        # to x**2 + y**2 = r **2; nierownosc sprawdza czy punkt P(x,y)
        # znajduje sie okregu
        """
        if ((x - 0) ** 2 + (y - 0) ** 2) <= (self.circleRadius ** 2):
            return True
        return False


    def checkPointIsInCircle(self, point):
        # type: (Point) -> bool
        """
        Checks Point is in area of circle
        """
        return self.checkCoordinatesOfPointInCircle(point.x, point.y)

    def checkEdgeBetweenPointsExists(self, pointA, pointB):
        # type: (Point, Point) -> bool
        """
        Sprawdzanie po��czenie miedzy wierzcho�kami - je�li obszary nadajniwko
        na siebie na chodz� wedy istieje kraw�d� miedzy nimi
        """
        if ((pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2) <= 4 * self.weight:  # klasycznaodleglosc
            return True

        return False

def main():


if __name__ == "__main__":
    main()
