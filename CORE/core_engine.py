from ramanujan_convergence import RamanujanEngine

class Tens8rCore:
    def __init__(self, identifier="Original"):
        self.id = identifier
        self.engine = RamanujanEngine(precision=5)
        self.state = None

    def synchronize(self):
        """Syncs the tensor state with the Ramanujan convergence constant."""
        self.state = self.engine.calculate_pi_series()
        return self.state

    def report(self):
        status = "STABLE" if self.state else "INITIALIZING"
        print(f"TENS8R_{self.id} | Status: {status} | Value: {self.state}")

if __name__ == "__main__":
    t_core = Tens8rCore()
    t_core.synchronize()
    t_core.report()
