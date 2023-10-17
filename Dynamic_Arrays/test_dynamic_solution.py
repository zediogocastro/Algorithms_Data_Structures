import unittest
from dynamic_solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        nums = [1,2,1]
        expected_nums = [1,2,1,1,2,1]
        actual_solution = self.solver.getConcatenation(nums)
        self.assertEqual(actual_solution, expected_nums)

    def test_example_2(self):
        nums = [1,3,2,1]
        expected_nums = [1,3,2,1,1,3,2,1]
        actual_solution = self.solver.getConcatenation(nums)
        self.assertEqual(actual_solution, expected_nums)

if __name__ == '__main__':
    unittest.main()
