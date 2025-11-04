
import math, pytest
from app import operations as ops
def test_add(): assert ops.add(2,3)==5
def test_subtract(): assert ops.subtract(7,2)==5
def test_multiply(): assert ops.multiply(3,4)==12
def test_divide(): assert ops.divide(9,3)==3
def test_divide_by_zero(): 
    with pytest.raises(ZeroDivisionError): ops.divide(1,0)
def test_float_precision(): assert math.isclose(ops.divide(1,4),0.25,rel_tol=1e-9)
