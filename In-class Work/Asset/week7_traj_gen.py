import numpy as np
import matplotlib.pyplot as plt
from ruckig import Ruckig, InputParameter, OutputParameter, Result

# ===== System setup =====
dt = 0.01
otg = Ruckig(3, dt)   # 3 DOF system

inp = InputParameter(3)
out = OutputParameter(3)

# ===== Initial state =====
inp.current_position = [0.0, 0.0, 0.0]
inp.current_velocity = [0.0, 0.0, 0.0]
inp.current_acceleration = [0.0, 0.0, 0.0]

# ===== Target state =====
inp.target_position = [1.0, -0.5, 0.8]
inp.target_velocity = [0.0, 0.0, 0.0]
inp.target_acceleration = [0.0, 0.0, 0.0]

# ===== Limits =====
inp.max_velocity = [1.0, 1.0, 1.0]
inp.max_acceleration = [2.0, 2.0, 2.0]
inp.max_jerk = [10.0, 10.0, 10.0]

# ===== Storage =====
time_data = []
pos_data = []
vel_data = []
acc_data = []

t = 0.0

# ===== Generate trajectory =====
while True:
    res = otg.update(inp, out)

    time_data.append(t)
    pos_data.append(out.new_position.copy())
    vel_data.append(out.new_velocity.copy())
    acc_data.append(out.new_acceleration.copy())

    inp.current_position = out.new_position
    inp.current_velocity = out.new_velocity
    inp.current_acceleration = out.new_acceleration

    t += dt

    if res == Result.Finished:
        break

# Convert to NumPy arrays
time_data = np.array(time_data)
pos_data = np.array(pos_data)
vel_data = np.array(vel_data)
acc_data = np.array(acc_data)