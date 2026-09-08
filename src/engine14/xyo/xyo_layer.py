from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from engine14.xyo.interfaces.witness import WitnessContext, WitnessResult
from engine14.xyo.layers.origin import layer as origin_layer
from engine14.xyo.layers.invariant import layer as invariant_layer
from engine14.xyo.layers.structural import layer as structural_layer
from engine14.xyo.layers.surface import layer as surface_layer


def run_xyo_stack(ctx: WitnessContext) -> Dict[str, Any]:
    """Run all XYO layers in a fixed, deterministic order."""
    layers = [
        origin_layer,
        invariant_layer,
        structural_layer,
        surface_layer,
    ]

    results: List[WitnessResult] = [mod.evaluate(ctx) for mod in layers]

    return {
        "engine_id": ctx.engine_id,
        "revision": ctx.revision,
        "layers": [asdict(r) for r in results],
    }

