from engine14.xyo.interfaces.witness import WitnessContext, WitnessResult

LAYER_NAME = "origin"

def evaluate(ctx: WitnessContext) -> WitnessResult:
    return WitnessResult(
        layer=LAYER_NAME,
        ok=True,
        data={
            "engine_id": ctx.engine_id,
            "revision": ctx.revision,
            "origin_tag": "engine14-anchor",
        },
    )

