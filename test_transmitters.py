from unittest import TestCase
from mock import Mock
from parameterized import parameterized

from grafy.api.transmitters import Point


class PointTest(TestCase):
    @parameterized([
        (1, 2),
        (3, 4),
        (-5, -6),
        (8, 20),
    ])
    def test_fabricRandomPoint(self, circleRadius, weight):
        p = Point.fabricRandomPoint(20, 10)
        print(p)
        expectedX = 20
        expectedY = 10

        self.assertEqual(p.x, expectedX)
        self.assertEqual(p.y, expectedY)




class CircleCalculatorTest(TestCase):
    def setUp(self):
        self.point = Mock() #type: Point
        self.point.x = 5
        self.point.y = 20



    def test_checkCoordinatesOfPointInCircle_shouldPass(self):
        pass

    def test_checkPointIsInCircle_shouldPass(self):
        pass

    def test_checkEdgeBetweenPointsExists_(self):
        pass