from typing import List, Union
from src.errors import VectorWithDifferenceSizes
from src.types import Vector
from functools import reduce


def add(v: Vector, w: Vector) -> Vector:
    """
    Soma os valores de dois vetores

    Parameters
    ----------
    v : Vector
        Vetor 1
    w : Vector
        Vetor 2

    Returns
    -------
    Vector
        Vetor somado
    """
    assert len(v) == len(w), VectorWithDifferenceSizes(v, w)
    return [v_i + w_i for (v_i, w_i) in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """
    Subtrai os valores de dois vetores

    Parameters
    ----------
    v : Vector
        Vetor 1
    w : Vector
        Vetor 2

    Returns
    -------
    Vector
        Vetor subtraido
    """
    assert len(v) == len(w), VectorWithDifferenceSizes(v, w)
    return [v_i - w_i for (v_i, w_i) in zip(v, w)]


def vector_sum(vectores: List[Vector]) -> Vector:
    """
    Dado uma lista de Vetores, retorna a soma de todos.

    Parameters
    ----------
    vectores : List[Vector]
        Lista de Vetores

    Returns
    -------
    Vector
        Resultado da soma vetorial.
    """
    return reduce(lambda x, y: add(v=x, w=y), vectores)


def scalar_add(v: Vector, scalar: Union[int, float]) -> Vector:
    """
    Given a vector, return then acrescented by a scalar.
    v = v_i + scalar

    Parameters
    ----------
    v : Vector
        [description]
    scalar : Union[int, float]
        [description]

    Returns
    -------
    Vector
        return vector acrescented by a scalar.
    """
    return [vi + scalar for vi in v]


def scalar_multiply(v: Vector, scalar: Union[int, float]) -> Vector:
    """
    Dado um número escalar, multiplica o vetor pelo mesmo.

    Parameters
    ----------
    v : Vector
        Vetor a ser multiplicado
    scalar : Union[int, float]
        Escalar.

    Returns
    -------
    Vector
        Vetor escalado.
    """
    return [x * scalar for x in v]


def vector_mean(vectores: List[Vector]) -> Vector:
    """
    Dado dois vetores, retorna sua média.

    Parameters
    ----------
    vectores : List[Vector]
        Lista de vetores.

    Returns
    -------
    Vector
        Retorna a média dos vetores.
    """
    n = len(vectores)
    soma = vector_sum(vectores)
    return scalar_multiply(soma, 1 / n)


def dot(v: Vector, w: Vector) -> Union[int, float]:
    """
    Computa o produto interno
    v_1*w_1 + v_2*w_2 + ... + v_n*w_n

    Parameters
    ----------
    v : Vector
        Vetor 1
    w : Vector
        Vetor 2

    Returns
    -------
    Union[int,float]
        Resultado do produto interno.
    """
    assert len(v) == len(w), "v e w precisam ter o mesmo tamanho"
    return sum(v_i * w_i for (v_i, w_i) in zip(v, w))


def sum_of_squares(v: Vector) -> Union[int, float]:
    """
    Retorna a soma dos quadrados de um vetor
    v_1*v_1 + v_2*v_2 + ... + v_n*v_n

    Parameters
    ----------
    v : Vector

    Returns
    -------
    Union[int,float]
        Resultado da soma dos quadrados de um vetor
    """
    return dot(v, v)


def squared_vector(v: Vector) -> Vector:
    return [vi ** 2 for vi in v]


def modulo(v: Vector) -> Union[int, float]:
    """
    Retorna a magnitude do array
    modulo([3, 4]) = (3^2 + 4^2)^1/2 = 5

    Parameters
    ----------
    v : Vector
        [description]

    Returns
    -------
    Union[int,float]
        [description]
    """
    return sum(squared_vector(v)) ** (1 / 2)


def distance_between_vectors(v: Vector, w: Vector) -> Union[int, float]:
    """
    Computa ((v_1-w_1)**2 + ... + (v_i-w_i)**2)**(1/2)

    Parameters
    ----------
    v : Vector
        [description]
    w : Vector
        [description]

    Returns
    -------
    Vector
        [description]
    """
    return modulo(subtract(v, w))
