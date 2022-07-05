from dataclasses import dataclass
import typing

@dataclass(frozen=True)
class money():
    curr: str
    qty: int

    def __add__(self, m):
        if (self.curr == m.curr):
            sum = self.qty + m.qty
            return money(self.curr, sum)

    def __mul__(self, m):
        if (m is not money):
            mult = self.qty*m
            return money(self.curr, mult)
    
    def __eq__(self,m):
        if (self.curr==m.curr & self.qty==m.qty):
            return True
        return False
    #__ne__() is implemented kindly by python3

