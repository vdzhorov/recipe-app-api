from django.test import SimpleTestCase
from app import calc


class Add(SimpleTestCase):
    """Test the calc add function."""

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
