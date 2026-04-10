from tpu_engine import TENS8R_TPU
import numpy as np

def run_diagnostic():
    tpu = TENS8R_TPU()
    print("--- TENS8R SPATIAL DIAGNOSTIC ---")
    
    # Run a full XYZ cycle
    for axis in ['x', 'y', 'z']:
        tpu.cycle(rotation_axis=axis)
    
    # Extract values to check for 'voids' or desync
    values = [node["val"] for node in tpu.mesh.grid.flat]
    mean_val = np.mean(values)
    std_dev = np.std(values)
    
    print(f"\nLattice Node Count: {len(values)}")
    print(f"Mean Convergence: {mean_val:.15f}")
    print(f"Standard Deviation: {std_dev}")
    
    if std_dev == 0:
        print("RESULT: 100% PHASE SYNC ACHIEVED. READY FOR GASEOUS SIMULATION.")
    else:
        print("RESULT: PHASE DRIFT DETECTED. CHECK ROTATION LOGIC.")

if __name__ == "__main__":
    run_diagnostic()
