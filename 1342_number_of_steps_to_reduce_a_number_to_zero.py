
# Problem: 1342. Number of Steps to Reduce a Number to Zero
# Difficulty: Easy
# Source: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
# Description:
# Given a non-negative integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise,
# you have to subtract 1 from it.


import unittest


def numberOfSteps(num) -> int:
    steps = 0

    while num > 0:
        # if (num % 2) == 0:
        if (num & 1) == 0:
            # num /= 2
            num >>= 1
        else:
            num -= 1

        steps += 1

    return steps

# Time complexity: O(log n)
# Space complexity: O(1)


class TestNumberOfSteps(unittest.TestCase):
    def test_number_of_steps_1(self):
        self.assertEqual(numberOfSteps(14), 6)

    def test_number_of_steps_2(self):
        self.assertEqual(numberOfSteps(8), 4)

    def test_number_of_steps_3(self):
        self.assertEqual(numberOfSteps(123), 12)


if __name__ == '__main__':
    unittest.main()
