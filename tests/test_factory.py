""" unittest factory module """
import unittest

from ming_p1.simple_factory import PhoneFactory, Phone, Samsung, AppleIPhone

class TestFactory(unittest.TestCase):
    """ TestFactory class """
    def setUp(self):
        """ TestFactory class setUp function  """
        self.factory = PhoneFactory()


class TestIphone(TestFactory):
    """ TestIphone class """
    def test_difference_id(self):
        """ TestIphone class test_difference_id function  """
        self.assertFalse(
            self.factory.create_type('iphone') is self.factory.create_type(
                'iphone'))

    def test_is_a_phone(self):
        """ TestIphone class test_a_phone function  """
        self.assertTrue(
            isinstance(self.factory.create_type('iphone'), Phone))
        self.assertTrue(
            isinstance(self.factory.create_type('iphone'), AppleIPhone))
        self.assertFalse(
            isinstance(self.factory.create_type('iphone'), Samsung))


if __name__ == '__main__':
    unittest.main()
