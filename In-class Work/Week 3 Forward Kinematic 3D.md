# Week 3: Forward Kinematics 3D

---------------
#### :dizzy: **Date :** Jan 30
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 0. Bind Python for CoppeliaSim Script (Optional)

- [ ] From the scene folder, open "simpleThreadedAndNonThreadedExample-python.ttt". Try to run it, you will typically get an error. This indicates that Python is not binded for the CoppeliaSim Script. You should also be able to see a line in the Console below:

```shell
The Python interpreter could not be called. It is currently set as: 'py'. You can specify it in C:\....../CoppeliaSim/usrset.txt with 'defaultPython', or via the named string parameter 'python' from the command line
```

- [] Now, you just need to find your python path in your local computer. Then write it into the "usrset.txt" file.

- [] For example, if you use Anaconda in Windows, open **Anaconda Prompt**  and type:
```shell
where python
```
(macOS will be `which python` )

Example output:
```shell
C:\Users\YC\anaconda3\python.exe
C:\Users\YC\AppData\Local\Microsoft\WindowsApps\python.exe
```
Copy the anaconda path to the specific lin in the txt file

Then try the scene again.,



## 1. Two-DoF planar manipulator

- [ ] Download the  provided ``Asset/week2_2DoF_planar.ttt`` scene file. 


--------
🎉 **Submit your worksheet**. Also let the instructor to verify your simulation result of the 3-DoF manipulator.
