import unittest

from iterable_wrapper import IterableAPI

class WrapperTestCase(unittest.TestCase):
    """Tests for `iterable_wrapper.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
