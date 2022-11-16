from django.test import SimpleTestCase
from app import calc


class Subtract(SimpleTestCase):
    """Test subtracting numbers."""

    def test_subtract_modules(self):
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)
