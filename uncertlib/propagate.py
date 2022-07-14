import numpy as np
from functools import wraps
from uncertlib.quantity import Quantity


# Array size - determines the precision of the derivative
ARRAY_SIZE = 1_000


def propagate(func: callable) -> callable:
    @wraps(func)
    def wrapper(**kw) -> Quantity:
        # Gets data from the keyword arguments
        _items = kw.items()
        q_kwargs = [kwarg for kwarg, _ in _items]
        q_values = [quantity.v for _, quantity in _items]
        q_uncert = [quantity.u for _, quantity in _items]
        # Calculates the output value of the function
        calc_v = float(func(**dict(zip(q_kwargs, q_values))))
        # Propagates the uncertainties of the calculation
        pd_times_uncert = []
        for i in range(len(_items)):
            in_values = q_values.copy()
            # Creates a small array for the test variable
            variable_arr = np.linspace(q_values[i] - 0.1, q_values[i] + 0.1, ARRAY_SIZE)
            dx = variable_arr[1] - variable_arr[0]
            # Calculates the function output using the variable array
            in_values[i] = variable_arr
            y = func(**dict(zip(q_kwargs, in_values)))
            # Evaluates the partial derivative at that variable
            pd = np.gradient(y, dx)[ARRAY_SIZE // 2]
            pd_times_uncert.append(pd * q_uncert[i])
        calc_u = np.linalg.norm(np.array(pd_times_uncert))
        return Quantity(v=calc_v, u=calc_u)

    return wrapper