from src.algelin import vetores
import pytest

from src.types import Vector

def test_vector_add():
    assert vetores.add(v=[1,2,3], w=[5,3,4]) == [6,5,7]

def test_vector_subtract():
    assert vetores.subtract(v=[1,2,3], w=[3,2,1]) == [-2,0,2]


testdata = [
# Test 1
[
    [
        [1,2],
        [2,3],
        [2,2]
    ],
    [5, 7]
],
# Test 2
[
    [
        [8,15],
        [2,14]
    ],
    [10, 29]
],
]
@pytest.mark.parametrize("vectors_list, expected", testdata)
def test_vector_list_sum(vectors_list, expected):
    assert vetores.vector_sum(vectors_list) == expected

testdata = [
# Test 1
[[1,2,3], 5, [5,10,15]],
[[1,2,3], .5, [.5,1.0,1.5]]
]
@pytest.mark.parametrize("vetor, escalar, expected", testdata)
def test_scalar_multiply(vetor, escalar, expected):
    assert vetores.scalar_multiply(vetor, escalar) == expected

testdata = [
# Test 1
[
    [
    [1,2,3],
    [3,6,9]
    ],
    [2., 4., 6]
]
]
@pytest.mark.parametrize("vectors_list, expected", testdata)
def test_vector_mean(vectors_list, expected):
    assert vetores.vector_mean(vectors_list) == expected


def test_vector_dot():
    assert vetores.dot(v=[1,2,3], w=[5,3,4]) == (5+6+12)

def test_sum_of_squares():
    assert vetores.sum_of_squares(v=[1,2,3]) == (1+4+9)


def test_scalar_add():
    assert vetores.scalar_add(v=[1,2,3], scalar=5) == [6, 7, 8]


def test_squared_vector():
    assert vetores.squared_vector(v=[1,2,3]) == [1, 4, 9]

def test_modulo():
    assert vetores.modulo([3, 4]) == 5

def test_distance_between_vectors():
    u = (2,-4)
    v = (-4, 4)
    assert vetores.distance_between_vectors(u,v) == 10