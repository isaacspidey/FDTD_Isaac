import Source.algebra_methods as am
import numpy as np
    
def test_addition_method():
    assert am.addition(1,2)==3

    assert not am.addition(1.35,1.25) == 2.61

def test_substraction_method():
    assert am.substraction(10,7)==3