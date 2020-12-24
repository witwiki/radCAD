import pytest

import pandas as pd

import output.rad_cad as rc
from output.rad_cad import Model, Simulation

from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from cadCAD.engine import ExecutionMode, ExecutionContext
from cadCAD.engine import Executor
from cadCAD import configs

from test_cases import basic

states = basic.states
psubs = basic.psubs
params = basic.params
TIMESTEPS = 10_000
RUNS = 10

model = Model(initial_state=states, psubs=psubs, params=params)
simulation_radcad = Simulation(model=model, timesteps=TIMESTEPS, runs=RUNS)

def test_benchmark_radcad(benchmark):
    benchmark.pedantic(radcad_simulation, iterations=1, rounds=10)

def radcad_simulation():
    data_radcad = rc.run([simulation_radcad])