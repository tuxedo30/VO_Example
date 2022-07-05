from compileall import compile_file
from unittest import TestCase
from money_ObjectValue import money
import pytest

class test_money_VO(TestCase):
    
    #Sum and subtract just if is the same currency
    #Cannot multiply money with money, just with a number
    
    five= money('us',5)
    ten = money('us',10)
    colmil= money('col',1000)
    
    def test_adding_and_subtract_money_same_currency(self):
        ten2=self.five+self.five
        five2=self.ten-self.five
        assert ten2 == self.ten & five2 == self.five

    def test_adding_and_subtract_money_different_currency(self):
        with pytest.raises(ValueError):
            self.five + self.colmil
        with pytest.raises(ValueError):
            self.five - self.colmil
    
    def test_money_can_multiply_number(self):
        assert self.five*2==money('us',10)

    def test_money_cannot_multiply_money(self):
        with pytest.raises(TypeError):
            self.five*self.ten

