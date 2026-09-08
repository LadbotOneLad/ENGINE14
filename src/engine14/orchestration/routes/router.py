from engine14.orchestration.state.engine_state import EngineState
from engine14.xyo.interfaces.witness import WitnessContext
from engine14.xyo.xyo_layer import run_xyo_stack

def handle(route: str, state: EngineState):
    if route == "xyo_witness":
        ctx = WitnessContext(
            engine_id="ENGINE14",
            revision=state.revision,
            metadata={"mode": state.flags.get("mode", "anchor")},
        )
        return run_xyo_stack(ctx)

    raise ValueError(f"Unknown route: {route}")

