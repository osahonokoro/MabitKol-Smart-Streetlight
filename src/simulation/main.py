import random

class MabitKolSimulation:
    def __init__(self):
        self.streetlights = [f"Streetlight_{i}" for i in range(4)]
        self.objects = [f"Object_{i}" for i in range(6)]
        self.time = 0.0
        self.energy = 100.0
        self.alerts = []

    def step(self, dt: float):
        self.time += dt
        self.energy -= dt * 0.5
        if random.random() < 0.2:
            self.alerts.append(f"Alert at {self.time:.2f}s")
        return {"time": self.time, "energy": self.energy, "alerts": self.alerts}
