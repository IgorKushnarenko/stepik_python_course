import unittest


class Test_abs(unittest.TestCase):
    def test_abs(self):
        self.assertEquals(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEquals(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()