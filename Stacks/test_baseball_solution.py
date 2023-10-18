import unittest
from baseball_solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        input = ["5","2","C","D","+"]
        expected_output = 30
        actual_output = self.solver.calPoints(input)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        input = ["5","-2","4","C","D","9","+","+"]
        expected_output = 27
        actual_output = self.solver.calPoints(input)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
