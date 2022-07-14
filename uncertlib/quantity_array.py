import numpy as np
from typing import List
from typing import Tuple
from uncertlib.quantity import Quantity


# Temp fix - very slow
def quantity_array(*, v: np.ndarray, u: np.ndarray) -> List[Quantity]:
    v_list, u_list = v.tolist(), u.tolist()
    if len(v_list) != len(u_list):
            raise ValueError(f"Input arrays are not the same size - got {len(v)} and {len(u)}.")
    return [Quantity(v=v_list[i], u=u_list[i]) for i in range(len(v_list))]



def extract_vu_arrays(quant_list: List[Quantity]) -> Tuple[List[float], List[float]]:
    v_list, u_list = [], []
    for q in quant_list:
        v_list.append(q.v)
        u_list.append(q.u)

    return v_list, u_list



class QuantityArray:
    __slots__ = ("_v", "_u")

    def __init__(self, *, v: np.ndarray, u: np.ndarray) -> None:
        """Creates a Quantity object - only accepts kwargs

        Args:
            v (np.ndarray): Value array
            u (np.ndarray): Associated uncertainty array
        """
        if len(v) != len(u):
            raise ValueError(f"Input arrays are not the same size - got {len(v)} and {len(u)}.")

        self._v = v
        self._u = u

    @property
    def v(self) -> np.ndarray:
        return self._v

    @property
    def u(self) -> np.ndarray:
        return self._u

    def __getitem__(self, index: int) -> Quantity:
        """Get the item stored at a particular index

        Args:
            index (int): Index

        Returns:
            Quantity: Quantity stored at that index
        """
        return Quantity(v=self.v[index], u=self.u[index])

    def __str__(self) -> str:
        # Returns a pretty string
        return f"[{self[0]},...,{self[-1]}]"

    def __repr__(self) -> str:
        return f"<QuantityArray>"

