from typing import List, Tuple

from types import Vector, Matriz


def shape(A: Matriz) -> Tuple[int, int]:
    """
    Retorna o shape de uma matriz

    Parameters
    ----------
    A : Matriz
        Uma lista de Vetores.

    Returns
    -------
    Tuple[int, int]
        Returns n_rows and n_cols
    """
    n_rows = len(A)
    # TODO: Validate array =! Matrix
    n_cols = len(A[0]) if A else 0
    return n_rows, n_cols
