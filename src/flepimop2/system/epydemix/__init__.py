"""Stepper function for SIR model integration tests."""

from typing import Any

import numpy as np

from flepimop2.configuration import ModuleModel
from flepimop2.system.abc import SystemABC
from flepimop2.typing import Float64NDArray, StateChangeEnum


def stepper(
    time: np.float64,  # noqa: ARG001
    state: Float64NDArray,
    **kwargs: Any,  # noqa: ARG001
) -> Float64NDArray:
    """
    ODE for an SIR model.

    Args:
        time: Current time (not used in this model).
        state: Current state array [S, I, R].
        **kwargs: Additional parameters (e.g. beta, gamma, etc.).

    Returns:
        The change in state.
    """
    # Implementors add their own logic here
    pass


class EpydemixSystem(SystemABC):
    """Epydemix model system."""

    module = "flepimop2.system.epydemix"
    state_change = StateChangeEnum.FLOW

    def __init__(self, test_phrase: str) -> None:
        """Initialize the Epydemix system with the Epydemix stepper."""
        self._stepper = stepper
        print(test_phrase)
        raise NotImplementedError


def build(config: dict[str, Any] | ModuleModel) -> EpydemixSystem:  # noqa: ARG001
    """
    Build an Epydemix system.

    Returns:
        An instance of the Epydemix system.
    """
    return EpydemixSystem(test_phrase=config.get("test-phrase", "No test phrase provided"))
