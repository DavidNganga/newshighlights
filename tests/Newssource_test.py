import unittest
from app.models import Newssource
Newssource = Newssource.Newssource

class NewssourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Newssource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Newssource = Newssource(1234,'ABC.com','Tom')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Newssource,Newssource))

