# 1480. Running Sum of 1d Array
# Difficulty: Easy
# Source: https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List
import unittest


def running_sum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


class TestRunningSum(unittest.TestCase):
    def test_running_sum(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(running_sum(nums), [1, 3, 6, 10])

    def test_running_sum_2(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(running_sum(nums), [1, 2, 3, 4, 5])

    def test_running_sum_3(self):
        nums = [3, 1, 2, 10, 1]
        self.assertEqual(running_sum(nums), [3, 4, 6, 16, 17])


if __name__ == '__main__':
    unittest.main()
