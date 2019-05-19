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





class RandomCoodinatesInCircle:
    # type: (Union[int, float], int)
    """
    Returns random coordinates point in space
    """
    def __init__(self, circleRadius, weight, dimension=2):
        self.circleRadius = circleRadius
        self.dimension = dimension

    def get_two_dimensional_coordinates(self):
        """Returns random coordinates in 2D"""
        x = randint(-1 * self.circleRadius, self.circleRadius)
        y = randint(-1 * self.circleRadius, self.circleRadius)


    def get_three_dimensional_coordinates(self):
        """
        Returns random coordinates in 3D
        """
        pass


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
