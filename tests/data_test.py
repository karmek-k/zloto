import unittest
from datetime import date

from zloto.data import JSONParser


class JSONParserTest(unittest.TestCase):
    def setUp(self):
        self.json = b'[{"data":"2019-06-17","cena":163.89}]'
        self.parser = JSONParser(self.json)

    def test_parsing(self):
        self.assertEqual(self.parser.date, date(2019, 6, 17))
        self.assertEqual(self.parser.price, 163.89)

        self.assertRaises(ValueError, JSONParser, b"")


if __name__ == "__main__":
    unittest.main()