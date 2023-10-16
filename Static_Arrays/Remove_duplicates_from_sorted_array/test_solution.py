import unittest
from my_solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums = [1,1,2]
        expected_length = 2
        actual_length = self.solver.removeDuplicates(nums)
        self.assertEqual(actual_length, expected_length)
        self.assertEqual(nums[:actual_length], [1, 2])

    def test_example_2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_length = 5
        actual_length = self.solver.removeDuplicates(nums)
        self.assertEqual(actual_length, expected_length)
        self.assertEqual(nums[:actual_length], [0, 1, 2, 3, 4])

    # You can add more test methods as needed

if __name__ == '__main__':
    unittest.main()
