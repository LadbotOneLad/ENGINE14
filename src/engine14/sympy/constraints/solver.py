from __future__ import annotations

from sympy.logic.boolalg import Boolean
from engine14.sympy.constraints.invariants import invariant_constraints


def evaluate_invariants() -> dict:
    expr = invariant_constraints()

    # If the invariant is already a SymPy Boolean, convert directly.
    if isinstance(expr, Boolean):
        simplified_bool = bool(expr)
        return {
            "expression": str(expr),
            "simplified": simplified_bool,
        }

    # If it's not a Boolean (rare), fall back to string conversion.
    return {
        "expression": str(expr),
        "simplified": bool(expr),
    }

