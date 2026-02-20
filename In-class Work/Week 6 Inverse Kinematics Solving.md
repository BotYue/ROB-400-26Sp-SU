# Week 6: Inverse Kinematics Solving

---------------
#### :dizzy: **Date :** Feb 20
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 0. Scene File

- [ ] Download the  provided ``Asset/week6_IK_worksheet.ttt`` scene file.

- [ ] The length of three links are: **0.5 m, 1 m, 0.6 m**
<br> You can double click each link, In "Shape -> Geometry -> Bounding box size -> Z [m]" to view the length of each link


<img src="Pic/week6_viewlength.png" width="600"/>

- [ ] In this work, we want to solve such IK problem:
* Desired Position: $(x, y, z) = (1.3, 0.6, 0)$
* Desired Oretation: $(row, pitch, yaw)= (0, 0, 40 deg)$


## 1. Analytic Inverse Kinematics

Firstly, let us using analytic IK to solve it.


$$
{}^{0}_{3}T =
\begin{bmatrix}
C_{123} & -S_{123} & 0 & 0.5C_1 + C_{12} + 0.6C_{123} \\
S_{123} & \ \ C_{123} & 0 & 0.5S_1 + S_{12} + 0.6S_{123} \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}=
\begin{bmatrix}
\cos 40^\circ & -\sin 40^\circ & 0 & 1.3 \\
\sin 40^\circ & \ \cos 40^\circ & 0 & 0.6 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

------------------
## 2. Optimization-Based Inverse Kinematics



