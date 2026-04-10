import math

class RamanujanEngine:
    def __init__(self, precision=100):
        self.precision = precision
        self.pi_approximation = None

    def calculate_pi_series(self):
        """Standard 1/pi Ramanujan series for convergence testing."""
        total_sum = 0
        for k in range(self.precision):
            numerator = math.factorial(4 * k) * (1103 + 26390 * k)
            denominator = (math.factorial(k)**4) * (396**(4 * k))
            total_sum += numerator / denominator
        
        result = (2 * math.sqrt(2) / 9801) * total_sum
        self.pi_approximation = 1 / result
        return self.pi_approximation

if __name__ == "__main__":
    engine = RamanujanEngine(precision=2)
    print(f"Convergence Test: {engine.calculate_pi_series()}")
