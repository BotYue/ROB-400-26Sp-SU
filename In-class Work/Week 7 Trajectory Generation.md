# Week 7: Trajectory Generation

---------------
#### :dizzy: **Date :** Feb 27
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 1. Ruckig Library for Trajectory Generation

- [ ] Install the Ruckig Library (Python). https://github.com/pantor/ruckig
      <br> You can directly use Google Colab to work with it

<img src="Pic/week7 colab_ruckig.png" width="600"/>

- [ ] After installation, run the provided Sample code to do trajectory generation for 3 DoF end-effector (assume only x,y,z position).
<br> The Sample code is provided in "Asset -> week7_traj_gen.py"

You can add extra piece to visulize it. For example, position:

```python
plt.figure()
plt.plot(time_data, pos_data[:,0], label='DOF 1')
plt.plot(time_data, pos_data[:,1], label='DOF 2')
plt.plot(time_data, pos_data[:,2], label='DOF 3')
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()
```

- [ ] Try to visulize 3 items related with trajectory in 3 Figures: 
* Position.
* Velocity.
* Acceleration

Example of a velocity figure:

<img src="Pic/week7 sample_plot.png" width="450"/>

### :page_facing_up: Task 1 to complete:
- [ ] Use the given traj generation settings in the Worksheet.
- [ ] Use Ruckig Library to generate trajectory.
- [ ] Report in Worksheet
1. Sketch the Position vs Time figure
2. Sketch the Velocity vs Time figure
3. Sketch the Acceleration vs Time figure


------------------
## 2. Trajectory Generation in CoppeliaSim

- [ ] Open the given scene file in "Asset -> week7_in_class.ttt". Run it to see what is going on.


<img src="Pic/week7 UR_simulation.png" width="450"/>

- [ ] One core function in the lua code is:

```lua
sim.moveToPose({
        pose = sim.getObjectPose(auxData.tip, sim.handle_world),
        targetPose = targetPose,
        maxVel = maxVel,
        maxAccel = maxAccel,
        maxJerk = maxJerk,
        callback = moveToPoseCallback,
        auxData = auxData
    })
```
This function performs trajectory generation using Ruckig library.
<br> https://manual.coppeliarobotics.com/en/sim/simMoveToPose.htm

- [ ] The traj generation paramaeters that your can tune are the main function `sysCall_thread()`

```lua
-- Motion limits (vx,vy,vz, vRot):
    local maxVel   = {0.45, 0.45, 0.45, 4.5}
    local maxAccel = {0.13, 0.13, 0.13, 1.24}
    local maxJerk  = {0.1,  0.1,  0.1,  0.2}
```

For example, you can make them 10x larger or 10x smaller, and observe the simulated movement.

### :page_facing_up: Task 2 to complete:
- [ ] Play with the traj generation paramaeters. Observe the differences.
- [ ] Use Ruckig Library to generate trajectory.
- [ ] No need to report in Worksheet
- [ ] Show a Simulation with different parameter settings to the intructor to get checked.

Feel free to ask the instructor for questions.
