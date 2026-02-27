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

### :page_facing_up: Task 1 to complete:
- [ ] Use the given traj generation settings in the Worksheet.
- [ ] Use Ruckig Library to generate trajectory.
- [ ] Report in Worksheet
1. Sketch the Position vs Time figure
2. Sketch the Velocity vs Time figure
3. Sketch the Acceleration vs Time figure


------------------
## 2. Trajectory Generation in CoppeliaSim

- [ ] Open the given scene file in "Asset -> week7_in_class.ttt"


Feel free to ask the instructor for questions.
