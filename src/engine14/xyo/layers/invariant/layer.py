from engine14.xyo.interfaces.witness import WitnessContext, WitnessResult
from engine14.sympy.constraints.solver import evaluate_invariants

LAYER_NAME = "invariant"

def evaluate(ctx: WitnessContext) -> WitnessResult:
    data = evaluate_invariants()
    return WitnessResult(layer=LAYER_NAME, ok=True, data=data)

