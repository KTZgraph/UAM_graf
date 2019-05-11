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
import typing



promien_miasta = 100 # promien plaszczyny bedacy przestzrenia/obszarem wystapienia nadajnikow na sztywno
zasieg_nadajniku = 10 # waga na sztywno
liczba_nadajnikow = 20 # liczba wierzcholkow na sztywno


class Point:
    """
    Punkt na p�aszczzynie dwuwymiarowej - okresla wierczholek
    """

    def __init__(self, x, y):
        self.x = x # type: int
        self.y = y # type: int

    @property  # getter
    def x(self):
        return self.x

    @x.setter  # setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.y = value




def check_x_y_in_city_circle(x, y, city_circle_radius):
    """
    Sprawdza czy wylosowany wps�rz�dne x,y, rzeczywi�cie eznajduj� si� w okregu miasta
    """
    if ((x - 0) ** 2 + (y - 0) ** 2) <= (city_circle_radius**2):
        return True

    return False


def create_random_point(circle_radius):
    #  circle_radius type: int
    #@return type: Point
    """
    Losowanie a potem sprawdza czy sa punkty w okregu
    - sprawdza odleglosci od �rodka
    """
    x = randint(-1 * circle_radius, circle_radius)
    y = randint(-1 * circle_radius, circle_radius)
    # liczenie odleglosci od srodka
    # rownanie okregu ktorego srodek jest w punkcjie 0,0
    # to x**2 + y**2 = r **2; nierownosc sprawdza czy punkt P(x,y)
    # znajduje sie okregu
    if check_x_y_in_city_circle(x, y, circle_radius):
        # punkt sie dobrze wyloswal - w okregu
        p = Point(x, y)
        return p  # obiekt klasy Point
    else:
        create_random_point(circle_radius)  # Rekurencja -  kolejny raz wywoluje funckje gdy �le wylosowano punkty


def check_edge_between_vertices_exists(weight, A, B):
    """
    Sprawdzanie po��czenie miedzy wierzcho�kami - je�li obszary nadajniwko
    na siebie na chodz� wedy istieje kraw�d� miedzy nimi
    """
    if ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) <= 4 * weight:  # klasycznaodleglosc
        return True

    return False


def create_graph_matrix_from_points(points_list):  # TODO
    """"Tworzy macierz sasiedztwa albo liste albo nie wiem co jeszcze
    tworz�c graf ju� z kraw�dziamy mi�dzy punktami, a potem przekazuje to �eby zrobi� GXML
    """
    pass

def make_GXML():  # TODO: nie mam pomys�u
    """Tworzy GCMl do innego programu"""
    pass


def main():
    print("--------------- Grafy1 ---------------")


if __name__ == "__main__":
    main()