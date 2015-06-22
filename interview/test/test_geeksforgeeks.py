# -*- coding: utf-8 -*-

import unittest

from geeksforgeeks import *


class TestGeeksForGeeks(unittest.TestCase):

    def test_towers_holding_water(self):
        heights = [1, 5, 3, 7, 2]
        expected = 2
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'one small gap')

        heights = [5, 1, 2, 3, 4]
        expected = 6
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large ascending gap')

        heights = [5, 4, 3, 2, 1, 6]
        expected = 10
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large descending gap')

        heights = [1, 3, 4, 2]
        expected = 0
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'no gap')

        heights = [5, 3, 3, 3, 4]
        expected = 3
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, multiple minima')

        heights = [5, 5, 5, 3, 4, 4]
        expected = 1
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, multiple minima')

        heights = [5, 1, 2, 3, 2, 1, 4]
        expected = 11
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, both descending and ascending')

        heights = [5, 1, 5, 2, 5, 3, 5]
        expected = 9
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'multiple small gaps')

        heights = [4, 2, 3, 1, 2, 1, 2, 1, 3, 2, 4]
        expected = 19
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'multiple small gaps')

    def test_largest_group_of_intersecting_intervals(self):
        intervals = [(1,2), (3,4), (5,6), (7,8)]
        expected = (1,2)
        actual = largest_group_of_intersecting_intervals(intervals)
        self.assertEqual(actual, expected, 'should produce the correct intersection')

        intervals = [(1,3), (2,4), (5,7), (7,8)]
        expected = (2,3)
        actual = largest_group_of_intersecting_intervals(intervals)
        self.assertEqual(actual, expected, 'should produce the correct intersection')

        intervals = [(1,4), (3,6), (5,8)]
        expected = (3,4)
        actual = largest_group_of_intersecting_intervals(intervals)
        self.assertEqual(actual, expected, 'should produce the correct intersection')

        intervals = [(1,5), (2,6), (3,7), (6,8)]
        expected = (3,5)
        actual = largest_group_of_intersecting_intervals(intervals)
        self.assertEqual(actual, expected, 'should produce the correct intersection')

    def test_nearest_smallest_left_element(self):
        arr = [1, 6, 4, 10, 2, 5]
        expected = [None, 1, 1,  4, 1, 2]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [1, 3, 0, 2, 5]
        expected = [None, 1, None, 0, 2]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [5, 4, 3, 2, 1]
        expected = [None, None, None, None, None]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [0, 4, 3, 2, 1]
        expected = [None, 0, 0, 0, 0]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [1, 2, 3, 4, 5]
        expected = [None, 1, 2, 3, 4]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [1, 5, 5, 5, 5]
        expected = [None, 1, 1, 1, 1]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)

        arr = [3, 2, 1, 0, 0]
        expected = [None, None, None, None, None]
        actual = nearest_smallest_left_element(arr)
        self.assertEqual(expected, actual)
