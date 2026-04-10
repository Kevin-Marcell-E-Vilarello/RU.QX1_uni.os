from ramanujan_convergence import RamanujanEngine
from tpu_mesh import Tens8rMesh

class TENS8R_TPU:
    def __init__(self):
        self.math_core = RamanujanEngine(precision=10)
        self.mesh = Tens8rMesh(size=4)
        self.sync_pulse = 0

    def cycle(self, rotation_axis='z'):
        # 1. Calculate the Ramanujan constant
        convergence_val = self.math_core.calculate_pi_series()
        
        # 2. Inject value into the 3D lattice
        self.mesh.inject_math(convergence_val)
        
        # 3. Rotate the block to maintain phase stability
        self.mesh.rotate_block(axis=rotation_axis)
        
        self.sync_pulse += 1
        print(f"Cycle {self.sync_pulse} | Value: {convergence_val:.15f} | Phase: {rotation_axis.upper()}-ROT")

if __name__ == "__main__":
    tpu_version = TENS8R_TPU()
    for axis in ['x', 'y', 'z']:
        tpu_version.cycle(rotation_axis=axis)
