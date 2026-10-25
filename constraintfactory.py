
import ast
from collections.abc import Callable
from typing import Any


class ConstraintFactory:
    """provides ConstraintFactory which allows to implement custom built validation checks on given constraints.
    Parses constraint strings once and compiles them into executable lambda functions.
    (built by Gemini (Google AI)"""

    def __init__(self) -> None:
        # Map constraint names to factory functions returning a lambda
        # PEP 585: Using built-in dict instead of typing.Dict
        # PEP 585: Using collections.abc.Callable instead of typing.Callable
        self._factories: dict[str, Callable[..., Callable[[Any], bool]]] = {
            "between": self._make_between,
            "in_list": self._make_in_list,
        }

    @staticmethod
    def _make_between(min_val: float, max_val: float) -> Callable[[Any], bool]:
        """Returns a lambda that evaluates min_val <= val <= max_val"""
        return lambda val: min_val <= val <= max_val

    @staticmethod
    def _make_in_list(*allowed_values: Any) -> Callable[[Any], bool]:
        """Returns a lambda that evaluates val in allowed_values"""
        # Converting allowed_values to a set gives O(1) lookup speed
        allowed_set = set(allowed_values)
        return lambda val: val in allowed_set

    def _parse_string(self, constraint_str: str) -> tuple[str, list[Any]]:
        """Safely extracts the function name and argument literals using AST."""
        try:
            tree = ast.parse(constraint_str, mode="eval")
            call_node = tree.body

            if not isinstance(call_node, ast.Call) or not isinstance(
                call_node.func, ast.Name
            ):
                raise TypeError(
                    "Expected a single function call e.g. 'between(a, b)'"
                )

            func_name = call_node.func.id
            args = [ast.literal_eval(arg) for arg in call_node.args]
            return func_name, args

        except Exception as err:
            raise ValueError(
                f"Malformed constraint string '{constraint_str}': {err}"
            ) from err

    def compile(self, constraint_str: str) -> Callable[[Any], bool]:
        """Compiles a constraint string into an executable lambda validator."""
        if not constraint_str or not constraint_str.strip():
            return lambda val: True  # No constraint -> always valid

        func_name, args = self._parse_string(constraint_str)

        if func_name not in self._factories:
            raise ValueError(f"Unsupported constraint rule: '{func_name}'")

        factory = self._factories[func_name]
        try:
            return factory(*args)
        except TypeError as err:
            raise ValueError(
                f"Argument count mismatch in constraint '{constraint_str}'"
            ) from err
