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




def main():


if __name__ == "__main__":
    main()
