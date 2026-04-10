import numpy as np

class Tens8rMesh:
    def __init__(self, size=4):
        self.size = size
        # Initialize a 4x4x4 grid. Each cell is a coordinate [x, y, z]
        self.grid = np.empty((size, size, size), dtype=object)
        for z in range(size):
            for y in range(size):
                for x in range(size):
                    self.grid[x, y, z] = {"id": f"{x}{y}{z}", "val": 0.0}

    def get_neighbors(self, x, y, z):
        """Calculates 6-way connectivity (NSEW-UD) with Toroidal wrapping."""
        s = self.size
        return {
            "NORTH": self.grid[x, (y+1)%s, z],
            "SOUTH": self.grid[x, (y-1)%s, z],
            "EAST":  self.grid[(x+1)%s, y, z],
            "WEST":  self.grid[(x-1)%s, y, z],
            "UP":    self.grid[x, y, (z+1)%s],
            "DOWN":  self.grid[x, y, (z-1)%s]
        }

    def rotate_block(self, axis='z'):
        """Performs a full 90-degree spatial rotation of the 4x4x4 tensor block."""
        if axis == 'x':
            self.grid = np.rot90(self.grid, k=1, axes=(1, 2))
        elif axis == 'y':
            self.grid = np.rot90(self.grid, k=1, axes=(0, 2))
        elif axis == 'z':
            self.grid = np.rot90(self.grid, k=1, axes=(0, 1))
        return f"Rotation on {axis.upper()} axis complete."

    def inject_math(self, value):
        """Distributes the Ramanujan convergence value across the lattice."""
        for node in self.grid.flat:
            node["val"] = value

if __name__ == "__main__":
    mesh = Tens8rMesh()
    print(f"Lattice initialized: {mesh.size}^3 nodes.")
    print(mesh.rotate_block(axis='z'))
