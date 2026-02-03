import unittest

from country_codes import get_country_code


class TestGetCountryCode(unittest.TestCase):
    def test_get_country_code(self):
        self.assertEqual(get_country_code("United States"), "us")
        self.assertEqual(get_country_code("Bolivia"), "bo")
        self.assertEqual(get_country_code("Congo, Dem. Rep."), "cd")
        self.assertEqual(get_country_code("Nonexistent Country"), None)
        self.assertEqual(get_country_code("Arab World"), None)


unittest.main()
