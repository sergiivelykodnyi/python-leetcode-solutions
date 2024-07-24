# Problem: 2191. Sort the Jumbled Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-the-jumbled-numbers

import unittest
from typing import List


def transform_number_to_digits(num: int) -> List[int]:
    if num == 0:
        return [0]

    digits = []

    while num:
        digits.append(num % 10)
        num //= 10

    digits.reverse()

    return digits


def transform_digits_to_number(digits: List[int]) -> int:
    num = 0

    for digit in digits:
        num = num * 10 + digit

    return num


def transform_number_to_mapped_number(num: int, mapping: List[int]) -> int:
    digits = transform_number_to_digits(num)

    for i in range(len(digits)):
        digits[i] = mapping[digits[i]]

    return transform_digits_to_number(digits)


def sort_jumbled(mapping: List[int], nums: List[int]) -> List[int]:
    mapped_nums = []
    result = []

    for num in nums:
        mapped_nums.append(
            (num, transform_number_to_mapped_number(num, mapping)))

    mapped_nums.sort(key=lambda x: x[1])

    for i in mapped_nums:
        result.append(i[0])

    return result


class TestSortJumbled(unittest.TestCase):
    def test_sort_jumbled_1(self):
        mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
        nums = [991, 338, 38]
        self.assertEqual(sort_jumbled(mapping, nums), [338, 38, 991])

    def test_sort_jumbled_2(self):
        mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums = [789, 456, 123]
        self.assertEqual(sort_jumbled(mapping, nums), [123, 456, 789])

    def test_sort_jumbled_3(self):
        mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        nums = [9, 99, 999, 9999, 99999]
        self.assertEqual(sort_jumbled(mapping, nums),
                         [9, 99, 999, 9999, 99999])

    def test_sort_jumbled_4(self):
        mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(sort_jumbled(mapping, nums),
                         [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
    # mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    # nums = [991, 338, 38]
    # print(sort_jumbled(mapping, nums))
