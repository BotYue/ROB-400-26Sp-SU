# Week 4: URDF

---------------
#### :dizzy: **Date :** Feb 6
#### :alarm_clock: Finish Check Points and Submit sheet to obtain grade.


------------------
## 1. Load a URDF to CoppeliaSim

* [ ] Go to the URDF dataset repo: [https://github.com/Daniella1/urdf_files_dataset](https://github.com/Daniella1/urdf_files_dataset)
  This repo contains URDF files for many different robots.

* [ ] Find the **folder that corresponds to the robot assigned in your Worksheet - Task 1**.

* [ ] Download the URDF files using **one** of the options below:

  **Option 1 — Download the full repository**

  * [ ] Download/clone the entire GitHub repo (unzip ~1.7 GB). Then delete all after class to free storage.

  **Option 2 — Download only your robot folder**

  * [ ] Manually download the URDF + any related files inside your robot’s folder (such as `.stl`, `.dae`).

-------
Here, I use a KR 5 ARC robot as an example to explain:

* [ ] Find the robot URDF in the dataset repo.
* [ ] Navigate to its upper level folder. You should see: One URDF (.urdf) folder; One mesh folder. You should get all files in these 2 folders.

<img src="Pic/urdf_1.png" width="600"/>

* [ ] Most URDF files are originally designed for ROS. When using the URDF in other simulators (e.g., CoppeliaSim), some file paths inside the URDF may not work correctly.
<br> For example, in my example https://github.com/Daniella1/urdf_files_dataset/blob/main/urdf_files/ros-industrial/xacro_generated/kuka/kuka_kr5_support/urdf/kr5_arc.urdf 
<br> You can see file path such as 
<br> ```<mesh filename="package://kuka_kr5_support/meshes/kr5_arc/visual/base_link.dae"/>```
<br> ```<mesh filename="package://kuka_kr5_support/meshes/kr5_arc/collision/base_link.stl"/>```
<br> ```<mesh filename="package://kuka_kr5_support/meshes/..."/>``` 
<br> You need to modify all these to be your location file location.
<br> For example, I download the full repo. Folder structure will look like this:
```
kuka_kr5_support/
 ├── urdf/
 │    └── kr5_arc.urdf
 └── meshes/
      └── kr5_arc/
           ├── visual/
           │    ├── base_link.dae
           │    └── ...
           └── collision/
                ├── base_link.stl
                └── ...
```
* [ ] Thus, I open the ```kr5_arc.urdf``` (use any text editor or code IDE). Replace all as such:
<br> ```<mesh filename="../meshes/kr5_arc/visual/base_link.dae"/>```
<br> ```<mesh filename="../meshes/kr5_arc/collision/base_link.stl"/>```
<br> ```<mesh filename="../meshes/..."/>``` 

<img src="Pic/urdf_2.png" width="500"/>

* [ ] Once done, save it. Then go to CopperliaSim, Open a new scene.
* [ ] Go to "Modules -> Importers -> URDF Importer". Use the default import setting.
* [ ] You should see the robot in the simulator now!

---
