#coding=utf-8

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import json

from api.transmitters import Transmitters2D

from api.hungarian_algorithm import Hungarian


class TransmitterDataWrapper:
    def __init__(self, request):
        # type: (Dict) -> None
        self.body = json.loads(request.body.decode('utf-8'))

    @property
    def totalPoints(self):
        try:
            return int(self.body["totalPoints"])
        except ValueError:
            raise ValueError("Nieprawidłowa wartość dla liczby punktów")

    @property
    def cityRadius(self):
        try:
            return float(self.body["cityRadius"])
        except ValueError:
            raise ValueError("Nieprawidłowa wartość dla promienia miasta")

    @property
    def transmittersWeight(self):
        try:
            return float(self.body["transmittersWeight"])
        except ValueError:
            raise ValueError("Nieprawidłowa wartość dla zasięgu nadajnika")


class TransmittersDrawView(View):
    """Zwraca macierz grafu w postaci XML"""
    template_name = 'api\\transmittersSVG.html'

    def get(self, request):
        """Return html file with input for user GET requests"""
        return render(request, self.template_name, {"info": "Podaj dane dla grafu"})

    def post(self, request):
        """Return keywords frequency, for webpage from user url"""
        if not request.body:
            return JsonResponse({"message": "Empty request.body"})

        try:
            transmitterDataWrapper = TransmitterDataWrapper(request)

            print(transmitterDataWrapper.cityRadius)
            print(transmitterDataWrapper.totalPoints)
            print(transmitterDataWrapper.transmittersWeight)

            transmitters2D = Transmitters2D(
                transmitterDataWrapper.totalPoints,
                transmitterDataWrapper.cityRadius,
                transmitterDataWrapper.transmittersWeight)

            matrixXML = transmitters2D.convertToXML()
            point_list = [[p.x, p.y] for p in transmitters2D.point_list]

            return JsonResponse({
                "matrixXML": matrixXML.decode('utf-8'),
                "errorMessage": '',
                "pointList": point_list
            })


        except ValueError as excpetion:
            return JsonResponse({
                "errorMessage":  str(excpetion)
            })


class HungarianView(View):
    """Algorytm węgierski - jedyna MASAKARA to to radosne zaznaczanie zer"""
    template_name = 'api\hungarianAlgorithmSVG.html'

    def get(self, request=None):
        cost_matrix = [
            [5, 1, 6, 4],
            [4, 8, 5, 3],
            [7, 2, 5, 6]]
        hungarian = Hungarian(cost_matrix)
        hungarian.calculate()
        print("Wynik:\n\t", hungarian.get_results())
        print("-" * 80)

        return render(request, self.template_name,
                      {"inputMatrix": cost_matrix,
                       "pairs": hungarian.get_results()
                       })

