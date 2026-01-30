# Week 3: Forward Kinematics 3D

---------------
#### :dizzy: **Date :** Jan 30
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 0. Bind Python for CoppeliaSim Script (Optional)

- [ ] From the scene folder, open "simpleThreadedAndNonThreadedExample-python.ttt". Try to run it. You should see an error message in the Console as below:

> The Python interpreter could not be called. It is currently set as: 'py'. You can specify it in ....../CoppeliaSim/usrset.txt with 'defaultPython', or via the named string parameter 'python' from the command line

<img src="Pic/python bind1.png" width="700"/>
    
- [ ] Now, you just need to find your python path in your local computer. Then modify the "usrset.txt" file.

- [ ] For example, if you use Anaconda in Windows, open **Anaconda Prompt**  and type:
```shell
where python
```
(macOS will be `which python` )

Example output:
```shell
C:\Users\YC\anaconda3\python.exe
C:\Users\YC\AppData\Local\Microsoft\WindowsApps\python.exe
```

- [ ] Copy the anaconda path, then modify the specific line with `defaultPython` in the "usrset.txt" file.

<img src="Pic/python bind2.png" width="700"/>

- [ ] Reopen CoppeliaSim, run the same scene again. Your Python will work now.

------

## 1. Three-DoF manipulator DH & FK

- [ ] Download the  provided ``Asset/week3_3DOF_FK.ttt`` scene file. 
- [ ] In the Scene hierarchy (left panel), click "tip". Then go to "Modules -> Kinematics -> Denavit–Hartenberg Extractor". You will see a list of DH parameters in the Console.

- [ ] Open the Scipt (under base in the tree list). There are 2 incomplete parts for you to fill (the ``?`` part)

* ```local function dh_T(a,d,alpha,theta)```
* ```local DH = {...}```

Use what you learned in class to complete

- [ ] Once complete coding, run the simulation. You should see the numbers matching in the Console output. Such as:

```Sim Tip: [-1.509 2.066 -0.000] | DH Tip: [-1.509 2.066 0.000]```

The Sim Tip is the end-effector position from the Simulation. The DH Top is the end-effector position based on the calculation you implemented in code.
    
- [ ] Use the given rotating angles (theta) in the worksheet. Based on the DH parameters Do:
 Analytical calculation Using the forward kinematics derived in lecture, write out the linear algebra calculation steps in the provided worksheet. Clearly show how the joint angles are used to compute the end-effector position.


--------
🎉 **Submit your worksheet**. Also let the instructor to verify your simulation result of the 3-DoF manipulator.
