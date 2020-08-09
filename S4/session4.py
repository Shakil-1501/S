from typing import List
import time
import sys
import weakref
import random

class Qualean:
       
    def __init__(self,choice):
        self.choice = choice
        self.k = round(choice*(random.uniform(-1,1)))

    def __str__(self):
        return 'Qualean: choice={0}, k={1}'.format(self.choice, self.k)

    def __repr__(self):
        return 'Qualean({0}, {1})'.format(self.choice,self.k)

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.k < other.k
        else:
            print("I was called")
            raise NotImplementedError
        
    def __eq__(self,other):
        if  isinstance(other,Qualean):
            return self.k==self.k 
        else:
            return False


