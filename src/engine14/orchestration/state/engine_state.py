from dataclasses import dataclass, field

@dataclass
class EngineState:
    revision: str = "v0.1.0"
    flags: dict = field(default_factory=lambda: {
        "mode": "anchor",
        "xyo_enabled": True,
    })
