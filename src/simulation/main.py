import random
import matplotlib.pyplot as plt

class MabitKolSimulation:
    def __init__(self):
        self.streetlights = [f"Streetlight_{i}" for i in range(4)]
        self.objects = [f"Object_{i}" for i in range(6)]
        self.time = 0.0
        self.energy = 100.0
        self.alerts = []
        self.history = {"time": [], "energy": [], "alerts": []}

    def step(self, dt: float):
        self.time += dt
        self.energy -= dt * 0.5
        if random.random() < 0.2:
            self.alerts.append(f"Alert at {self.time:.2f}s")

        result = {"time": self.time, "energy": self.energy, "alerts": list(self.alerts)}
        self.history["time"].append(self.time)
        self.history["energy"].append(self.energy)
        self.history["alerts"].append(len(self.alerts))
        return result

    def run(self, duration: float, dt: float = 1.0):
        steps = int(duration / dt)
        for _ in range(steps):
            self.step(dt)
        return self.history

    def plot_results(self, save_path: str = None):
        plt.figure(figsize=(8, 4))
        plt.plot(self.history["time"], self.history["energy"], label="Energy")
        plt.plot(self.history["time"], self.history["alerts"], label="Alerts")
        plt.xlabel("Time (s)")
        plt.ylabel("Values")
        plt.title("MabitKol Simulation Results")
        plt.legend()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
