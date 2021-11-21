
import pytest

from src.estatistica.basic_stats import mean

testdata = [
# Test 1
({'v':[1,1,1,1,1]}, 1),
# Test 2
({'v':[20,30,10,5,5]},14)
]
@pytest.mark.parametrize("args, expected", testdata)
def test_mean(args, expected):
    assert mean(**args) == expected
