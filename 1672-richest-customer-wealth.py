# 1672. Richest Customer Wealth
# Difficulty: Easy
# Source: https://leetcode.com/problems/richest-customer-wealth/

from typing import List
import unittest


def maximum_wealth(accounts: List[List[int]]) -> int:
    max_wealth = 0

    for customer in accounts:
        current_wealth = 0

        for bank in customer:
            current_wealth += bank

        if current_wealth > max_wealth:
            max_wealth = current_wealth

    return max_wealth

# one-liner solution
# def maximum_wealth(accounts: List[List[int]]) -> int:
#     return max([sum(account) for account in accounts])


class TestMaximumWealth(unittest.TestCase):
    def test_maximum_wealth_1(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        self.assertEqual(maximum_wealth(accounts), 6)

    def test_maximum_wealth_2(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        self.assertEqual(maximum_wealth(accounts), 10)

    def test_maximum_wealth_3(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        self.assertEqual(maximum_wealth(accounts), 17)


if __name__ == '__main__':
    unittest.main()
