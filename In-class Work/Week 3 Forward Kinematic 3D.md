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

<img src="Pic/week3_DH extract.png" width="700"/>

- [ ] Open the Scipt (under base in the tree list). There are 2 incomplete parts for you to fill (the ``?`` part)

* ```local function dh_T(a,d,alpha,theta)``` Use the math equation of DH to complete.
* ```local DH = {...}``` Use the numbers from Denavit–Hartenberg Extractor to fill.

- [ ] Once complete coding, run the simulation. You should see the numbers matching in the Console output. Such as:

```Sim Tip: [-1.509 2.066 -0.000] | DH Tip: [-1.509 2.066 0.000]```

The Sim Tip is the end-effector position from the Simulation. The DH Top is the end-effector position based on the calculation you implemented in code.
    
### :page_facing_up: Task to complete:
- [ ] Use the given rotating angles in the worksheet. Do:
      
  * **Analytical calculation**
Using DH parameter-based forward kinematics from lecture, write out the linear algebra calculation steps in the provided worksheet. Clearly show each matrix.

  * **Simulation verification**
Apply the given joint angles in CoppeliaSim by rotating the joints. Write down the simulated end-effector ("Sim Tip") position in the provided worksheet.  Write down the code-calculated end-effector ("DH Tip") position in the provided worksheet.

* *Note: Due to coordinate-frame conventions in CoppeliaSim, the x–y position computed from DH parameters may appear sign-flipped or mirrored relative to the simulation display.*


## 2. UR10 Robot DH & FK

- [ ] Download the  provided ``Asset/week3_UR10_FK.ttt`` scene file.
      
- [ ] The DH parameters of the UR10 robot (Universal Robots) is provided on its official manual:
https://www.universal-robots.com/articles/ur/application-installation/dh-parameters-for-calculations-of-kinematics-and-dynamics/

Or I listed as a table here:

| Joint | a (m)  | d (m)   | α (rad) |
|------:|:------:|:-------:|:-------:|
| 1 | 0       | 0.1273   | π/2  |
| 2 | -0.612  | 0        | 0    |
| 3 | -0.5723 | 0        | 0    |
| 4 | 0       | 0.163941 | π/2  |
| 5 | 0       | 0.1157   | -π/2 |
| 6 | 0       | 0.0922   | 0    |

- [ ] Similarly, In the Script, there are 2 incomplete parts for you to fill (the ``?`` part)

* ```local function dh_T(a,d,alpha,theta)``` Use the math equation of DH to complete.
* ```local DH = {...}``` Use the data from UR10 robot official manual. The theta_offset is already entered.

- [ ] Once complete coding, run the simulation. You should see the numbers closely matching in the Console output. (The will be some minor off due to simulator shapes or calculation rounding). For example:

<img src="Pic/week3_UR10.png" width="700"/>

### :page_facing_up: Task to complete:
- [ ] Use the given rotating angles in the worksheet. Do:
      
  * **Simulation verification**
Apply the given joint angles in CoppeliaSim by rotating the joints. Write down the simulated end-effector ("Sim Tip") position in the provided worksheet.  Write down the code-calculated end-effector ("DH Tip") position in the provided worksheet.

  * **Code**
Write down the complete code for ```local function dh_T(a,d,alpha,theta)```

--------
🎉 **Submit your worksheet**. Also let the instructor to verify your simulation result.
