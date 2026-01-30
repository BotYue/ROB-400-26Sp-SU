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

## 1. Two-DoF planar manipulator

- [ ] Download the  provided ``Asset/week2_2DoF_planar.ttt`` scene file. 


--------
🎉 **Submit your worksheet**. Also let the instructor to verify your simulation result of the 3-DoF manipulator.
