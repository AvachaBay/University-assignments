from Newtone import *
import unittest

class TestNewtone(unittest.TestCase):
    """docstring for TestNewtone"""
    def test_Newtone_cycle(self):
        self.assertEqual(round(calculating_xn(1),2),0.68,"Should be 0.68")

if __name__=="__main__":

    unittest.main()