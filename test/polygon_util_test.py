

import unittest

from shapely.geometry import Polygon, LineString

import polygon_util


# https://docs.python.org/3/library/unittest.html#module-unittest
class PolygonUtilTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup class")
        pass

    @classmethod
    def tearDownClass(cls):
        print("teardown class")
        pass

    def setUp(self):
        print("setup")
        pass

    def tearDown(self):
        print("teardown")
        pass

    def test_is_convex_not_polygon(self):
        """非凸多边形"""
        p = LineString([(0, 0), (1, 1)])
        with self.assertRaises(ValueError) as err:
            polygon_util.is_convex(p)

        exception = err.exception
        self.assertTrue("not a polygon" in str(exception))
        self.assertIn("not a polygon", str(exception))


    def test_is_convex_not_shapely_obj(self):
        """整型参数不是合法对象"""
        p = 123
        with self.assertRaises(ValueError) as err:
            polygon_util.is_convex(p)

        exception = err.exception
        self.assertTrue("not a shapely object" in str(exception))
        self.assertIn("not a shapely object", str(exception))


    def test_is_convext_convex(self):
        # Triangle
        """是凸多边形"""
        p = Polygon([(0, 0), (0, 1), (1, 1)])
        self.assertTrue(polygon_util.is_convex(p))

        p = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
        self.assertTrue(polygon_util.is_convex(p))

    def test_is_convext_not_convex(self):
        """顺时针和逆时针测试"""
        # 逆时针
        p = Polygon([(0, 0), (2, 0), (1, 1), (2, 2), (0, 2)])
        self.assertFalse(polygon_util.is_convex(p))

        # 顺时针
        p = Polygon([(0, 0), (0, 2), (2, 2), (1, 1), (2, 0)])
        self.assertFalse(polygon_util.is_convex(p))
