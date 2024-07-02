import unittest
from io import StringIO
import sys
from bleatrix_trotter import solve_case, solve_cases

class TestBleatrixTrotter(unittest.TestCase):

    def test_insomnia(self):
        self.assertEqual(solve_case(0), "INSOMNIA")

    def test_case_1(self):
        self.assertEqual(solve_case(1), "10")

    def test_case_2(self):
        self.assertEqual(solve_case(2), "90")

    def test_case_11(self):
        self.assertEqual(solve_case(11), "110")

    def test_case_100(self):
        self.assertEqual(solve_case(100), "900")

    def test_case_200(self):
        self.assertEqual(solve_case(200), "9000")

    def test_N_greater_than_200(self):
        with self.assertRaises(ValueError):
            solve_case(201)

    def test_N_less_than_0(self):
        with self.assertRaises(ValueError):
            solve_case(-1)


    def test_solve_cases_sample(self):
        input_data = "4\n0\n1\n2\n11\n"
        expected_output = """Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
"""
        # Redirect stdout to capture print output
        sys.stdout = mystdout = StringIO()

        # input test file
        with open('c-input_test.in', 'w') as f:
            f.write(input_data)

        solve_cases('c-input_test.in')

        # Verify the output
        self.assertEqual(mystdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()