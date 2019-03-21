import pytest 
from principal import soma

from principal import mult


def test_soma():
    assert soma(2,4)==6 

def test_mult():

    assert mult(2,2)==5