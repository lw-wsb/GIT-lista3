import unittest
from kalkulator import dodawanie, dzielenie, mnozenie, odejmowanie

class TestCalculator(unittest.TestCase):

    def test_dodawanie(self):
        self.assertEqual(dodawanie(2, 3), 5)
        self.assertEqual(dodawanie(-1, 1), 0)
        self.assertEqual(dodawanie(-1, -1), -2)

    def test_odejmowanie(self):
        self.assertEqual(odejmowanie(10, 5), 5)
        self.assertEqual(odejmowanie(-1, 1), -2)
        self.assertEqual(odejmowanie(-1, -1), 0)

    def test_mnozenie(self):
        self.assertEqual(mnozenie(3, 7), 21)
        self.assertEqual(mnozenie(-1, 1), -1)
        self.assertEqual(mnozenie(-1, -1), 1)

    def test_dzielenie(self):
        self.assertEqual(dzielenie(10, 2), 5)
        self.assertEqual(dzielenie(-1, 1), -1)
        self.assertEqual(dzielenie(-1, -1), 1)
        with self.assertRaises(ValueError):
            dzielenie(10, 0)

if __name__ == '__main__':
    unittest.main()
