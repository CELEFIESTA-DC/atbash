#!/usr/bin/python3
"""





#####################################################################
    

                        DO NOT EDIT THIS FILE


#####################################################################






"""
import unittest
from main import atbash
class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(atbash("abcdefghijklmnopqrstuvwxyz"),"zyxwvutsrqponmlkjihgfedcba")

        
if __name__=='__main__':
    unittest.main()
