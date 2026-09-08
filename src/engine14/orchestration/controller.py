from engine14.orchestration.state.engine_state import EngineState
from engine14.orchestration.routes.router import handle

class Engine14Controller:
    def __init__(self, state: EngineState | None = None) -> None:
        self.state = state or EngineState()

    def xyo_witness_snapshot(self):
        return handle("xyo_witness", self.state)
