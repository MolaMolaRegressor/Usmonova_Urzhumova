import unittest
import orders

class Test_orders(unittest.TestCase):
    #wrong data
    def test_empty(self):
        self.assertFalse(orders.check(""))

    def test_letter(self):
        self.assertFalse(orders.check("8 (908) a89-78-78"))

    def test_more_digit(self):
        lot_digit = ["28 (908) 889-78-78","8 (1908) 889-78-78",
                     "8 (908) 7889-78-78", "8 (908) 889-78-788"]
        for i in lot_digit:
            self.assertFalse(orders.check(i))

    def test_without_marking(self):
        without_marking = ["8908897878","8(908)898-78-78",
                           "8 (908) 8978878","8 (908) 889 78 78"]
        for i in without_marking:
            self.assertFalse(orders.check(i))

    def test_seven(self):
        self.assertFalse(orders.check("+7 (908) 989-78-78"))

    #right data
    def test_right(self):
        self.assertTrue(orders.check("8 (908) 789-78-78"))

if __name__ == '__main__':
    unittest.main()
