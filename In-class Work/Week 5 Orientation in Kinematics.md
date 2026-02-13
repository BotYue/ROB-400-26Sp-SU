# Week 5: Orientation in kinematics

---------------
#### :dizzy: **Date :** Feb 13
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 1. Visualize a Framein CoppeliaSim

- [ ] Open a new scene in CoppeliaSim

- [ ] From the left-side "Model Browser", go to "Others" folder, select "Reference frame"

- [ ] Drag and place the "Reference frame" into the new scene

- [ ] Set the item at world origin and align with world frame (x-y-z frame in bottom right corner). To do so, we need to:

 * Go to "Object Shift", In "Position" → "Relative to World", set all X, Y, Z to be 0
 * Go to "Object Rotation", In "Orientation" → "Relative to World", set all Alpha, Beta, Gamma to be 0

- [ ] Once done, you should get the same looking as this picture
      
<img src="Pic/euler_1.png" width="650"/>


------------------
## 2. Rotate a Framein CoppeliaSim

Next, we will perform Euler-angle rotation to this reference frame. 
<br>Specifically, we will perform System I Euler-angle rotation (or called z-x′-z″)
<br>We are about to rotate in this sequence: 
* 20 deg about the OZ axis (or called z axis)
* 30 deg about the rotated OU axis (or called x' axis)
* 60 deg about the rotated OW axis (or called z'' axis)

- [ ] Go to "Object Rotation", In "Rotation", firstly set to "Relative to own frame"


---
