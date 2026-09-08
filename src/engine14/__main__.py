from engine14.orchestration.controller import Engine14Controller

def main():
    controller = Engine14Controller()
    snapshot = controller.xyo_witness_snapshot()

    print("\n=== ENGINE14 XYO + SymPy + Satellite Snapshot ===\n")

    for layer in snapshot["layers"]:
        print(f"[{layer['layer']}]")
        for key, value in layer["data"].items():
            print(f"  {key}: {value}")
        print()

if __name__ == "__main__":
    main()
