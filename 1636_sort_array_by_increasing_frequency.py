# Problem: 1636. Sort Array by Increasing Frequency
# Easy
# Source: https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Description:
# Given an array of integers nums, sort the array in increasing order based on
# the frequency of the values. If multiple values have the same frequency,
# sort them in decreasing order.

import unittest
from typing import List


def frequencySort(nums: List[int]) -> List[int]:
    frequency_dict = {}

    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    frequency_entries = sorted(
        frequency_dict.items(), key=lambda x: (x[1], -x[0]))

    frequency_array = []

    for num, frequency in frequency_entries:
        frequency_array.extend([num] * frequency)

    return frequency_array


class TestFrequencySort(unittest.TestCase):
    def test_frequency_sort(self):
        self.assertEqual(frequencySort([1, 1, 2, 2, 2, 3]), [
                         3, 1, 1, 2, 2, 2])
        self.assertEqual(frequencySort([2, 3, 1, 3, 2]), [1, 3, 3, 2, 2])
        self.assertEqual(frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]), [
                         5, -1, 4, 4, -6, -6, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
