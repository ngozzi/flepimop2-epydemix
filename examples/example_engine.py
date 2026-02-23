from typing import Any

import numpy as np

from flepimop2.system.abc import SystemProtocol
from flepimop2.typing import Float64NDArray
from flepimop2.configuration import IdentifierString


def runner(
    stepper: SystemProtocol,
    times: Float64NDArray,
    state: Float64NDArray,
    params: dict[IdentifierString, Any],
    **kwargs: Any,  # noqa: ARG001
) -> Float64NDArray:
    """
    Simple Euler runner for the SIR model.

    Args:
        stepper: The system stepper function.
        times: Array of time points.
        state: The current state array.
        params: Additional parameters for the stepper.
        **kwargs: Additional keyword arguments for the engine. Unused by this runner.

    Returns:
        The evolved time x state array.
    """
    output = np.zeros((len(times), len(state)), dtype=float)
    output[0] = state
    for i, t in enumerate(times[1:]):
        if i == 0:
            continue
        dt = t - times[i - 1]
        dydt = stepper(times[i - 1], output[i - 1], **params)
        output[i] = output[i - 1] + (dydt * dt)
    return np.hstack((times.reshape(-1, 1), output))
