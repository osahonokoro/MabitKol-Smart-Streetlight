#!/usr/bin/env python3
import sys
sys.path.append('..')
from src.simulation.main import MabitKolSimulation

def test_simulation_init():
    sim = MabitKolSimulation()
    assert len(sim.streetlights) == 4
    assert len(sim.objects) == 6
    print("✅ Test passed: Initialization")

def test_simulation_step():
    sim = MabitKolSimulation()
    result = sim.step(0.1)
    assert 'time' in result
    assert 'energy' in result
    assert 'alerts' in result
    print("✅ Test passed: Step function")

if __name__ == "__main__":
    test_simulation_init()
    test_simulation_step()
    print("\n🎉 All tests passed!")
