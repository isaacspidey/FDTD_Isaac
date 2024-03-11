import Source.gauss_1D_methods as g1d
import numpy as np

def test_gauss_equal ():
    assert g1d.gauss(1,1,1) == g1d.gauss(1,1,1)

def test_gauss_suma ():
    assert g1d.gauss(1,1,1)+1 == g1d.gauss(1,1,1)+2-1