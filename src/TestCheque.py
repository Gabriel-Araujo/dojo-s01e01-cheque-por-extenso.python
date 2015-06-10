#!/usr/bin/python
# -*- coding: utf-8 -*-

from Cheque import Cheque

import unittest

class TestCheque(unittest.TestCase):
    
    def test_humanize_1(self):
        cheque = Cheque(1.00)
        result = cheque.humanize()
        print("1 = " + result)
        self.assertEqual(result, 'um real')
    
    def test_humanize_10(self):
        cheque = Cheque(10.00)
        result = cheque.humanize()
        print("10 = " + result)
        self.assertEqual(result, 'dez reais')
        
    def test_humanize_15(self):
        cheque = Cheque(15.00)
        result = cheque.humanize()
        print("15 = " + result)
        self.assertEqual(result, 'quinze reais')
        
    def test_humanize_21(self):
        cheque = Cheque(21.00)
        result = cheque.humanize()
        print("21 = " + result)
        self.assertEqual(result, 'vinte e um reais')
    
    def test_humanize_100(self):
        cheque = Cheque(100.00)
        result = cheque.humanize()
        print("100 = " + result)
        self.assertEqual(result, 'cem reais')
        
    def test_humanize_101(self):
        cheque = Cheque(101.00)
        result = cheque.humanize()
        print("101 = " + result)
        self.assertEqual(result, 'cento e um reais')
        
    def test_humanize_133(self):
        cheque = Cheque(133.00)
        result = cheque.humanize()
        print("133 = " + result)
        self.assertEqual(result, 'cento e trinta e tres reais')
        
    def test_humanize_182(self):
        cheque = Cheque(182.00)
        result = cheque.humanize()
        print("182 = " + result)
        self.assertEqual(result, 'cento e oitenta e dois reais')
    
    def test_humanize_599(self):
        cheque = Cheque(599.00)
        result = cheque.humanize()
        print("599 = " + result)
        self.assertEqual(result, 'quinhentos e noventa e nove reais')
        
    def test_humanize_1000(self):
        cheque = Cheque(1000.00)
        result = cheque.humanize()
        print("1000 = " + result)
        self.assertEqual(result, 'mil reais')
        
    def test_humanize_2_32(self):
        cheque = Cheque(2.32)
        result = cheque.humanize()
        print("2.32 = " + result)
        self.assertEqual(result, 'dois reais e trinta e dois centavos')
        
    def test_humanize_3_02(self):
        cheque = Cheque(3.02)
        result = cheque.humanize()
        print("3.02 = " + result)
        self.assertEqual(result, 'tres reais e dois centavos')
        
    def test_humanize_3_14(self):
        cheque = Cheque(3.14)
        result = cheque.humanize()
        print("3.14 = " + result)
        self.assertEqual(result, 'tres reais e quatorze centavos')

    def test_humanize_1234(self):
        cheque = Cheque(1234.00)
        result = cheque.humanize()
        print("1234 = " + result)
        self.assertEqual(result, 'mil, duzentos e trinta e quatro reais')

    def test_humanize_1985(self):
        cheque = Cheque(1985.00)
        result = cheque.humanize()
        print("1985 = " + result)
        self.assertEqual(result, 'mil, novecentos e oitenta e cinco reais')
        
    def test_humanize_33450(self):
        cheque = Cheque(33450.00)
        result = cheque.humanize()
        print("33450 = " + result)
        self.assertEqual(result, 'trinta e tres mil, quatrocentos e cinquenta reais')

if __name__ == '__main__':
    unittest.main()
    

