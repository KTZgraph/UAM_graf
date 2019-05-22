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

from Graph import Graph2D
from point import Point2D
from sphere import Sphere2D

totalPointNumber = 10
cityRadius = 40
transmitterWeight = 3



def main():
    pointList = []
    for i in range(totalPointNumber):
        pointList.append(Point2D(i, i))

    sphere2D = Sphere2D(cityRadius)
    graph = Graph2D(sphere2D, transmitterWeight, pointList)
    graph.createGraphMatrix()



if __name__ == "__main__":
    main()
