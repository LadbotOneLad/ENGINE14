from dataclasses import dataclass
from typing import Any, Dict, Protocol

@dataclass(frozen=True)
class WitnessContext:
    engine_id: str
    revision: str
    metadata: Dict[str, Any]

@dataclass(frozen=True)
class WitnessResult:
    layer: str
    ok: bool
    data: Dict[str, Any]

class WitnessLayer(Protocol):
    def evaluate(self, ctx: WitnessContext) -> WitnessResult:
        ...

