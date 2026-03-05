# Week 8_B: LeRobot First Trial

---------------
#### :dizzy: **Date :** March 5
#### :ballot_box_with_check: Please work collaboratively within your team. Also be generous to help other teams when possible.

------------------
## 1. LeRobot Installation

- [ ] Follow the install guide on the Robotis webpage https://ai.robotis.com/omx/setup_guide_lerobot.html 

	* Note, If you already installed Anaconda (used in ELE 251), you do not need to install Miniconda. Directly start from `Create a Virtual Environment` from that webapge.

	* In Anaconda, you can open "Anaconda Prompt" for command-line based installation.

<img src="Pic/conda_promtp.png" width="450"/>

## 2. Verify Installation 

- [ ] Use a USB cable to connect the robot to your computer. We will check with basic communication with lerobot.

In the virtual environment you created, run the command:

```bash
lerobot-find-port
```

You should see a port listed. To verify that this port corresponds to the robot: 
1. Disconnect the USB cable from the robot; 
2. Run the same command again: `lerobot-find-port`; 
3. Check whether the port disappears.

Here is my example print-out in Terminal in a Windows machine..

```bash
(lerobot) C:\Users\YC>(lerobot) C:\Users\Ramos>lerobot-find-port
Finding all available ports for the MotorsBus.
Ports before disconnecting: ['COM14']
Remove the USB cable from your MotorsBus and press Enter when done.
```

## 3. Verify Python Connection

- [ ] After checking communication to the robot, we will now verify if Python can connect to the robot..

- [ ] Make sure the Python  you are using comes from the virtual environment you just created. For example,

 	* if you prefer Anaconda, select the enviroment in Anaconda Navigator and then lanuch a Spyder Python IDE;
 	* if you prefer VSCode, make sure you choose the correct Python kernel within th IDE.

<img src="Pic/anaconda_lerobot.png" width="700"/>

- [ ] First, check the basic Python package with this code:

```python
import lerobot
import pkgutil

print("LeRobot modules:")
print([m.name for m in pkgutil.iter_modules(lerobot.__path__)])
```

- [ ] Leader Test. Connect Leader with you computer via USB. Try this code.
<br> You should modify the PORT = r"\\.\..." based on your own computer.

```python
import time
from pprint import pprint

from lerobot.teleoperators.omx_leader.config_omx_leader import OmxLeaderConfig
from lerobot.teleoperators.omx_leader.omx_leader import OmxLeader

PORT = r"\\.\COM14"

cfg = OmxLeaderConfig(port=PORT, id="omx_leader_arm")
leader = OmxLeader(cfg)

leader.connect()
print("Leader connected on", PORT)

# Show what LeRobot thinks the leader outputs
print("action_features =", getattr(leader, "action_features", None))
print("\nPrinting leader.get_action()... Move the leader arm. Ctrl+C to stop.\n")

try:
    while True:
        a = leader.get_action()   
        print("keys:", list(a.keys()))
        pprint(a)
        time.sleep(1.0)
except KeyboardInterrupt:
    print("\nStopping...")
finally:
    leader.disconnect()
    print("Disconnected.")
```


## Follower Test

!!!Must place your follow in a large table in case falling down!

If you get error message `[RxPacketError] The data value exceeds the limit value!`, just the value `- 15` to other.

`- 15` means one direction by 15 degrees. for example change to `+ 15`


```python
import time
from lerobot.robots.omx_follower.config_omx_follower import OmxFollowerConfig
from lerobot.robots.omx_follower.omx_follower import OmxFollower

PORT = "COM12"

follower = OmxFollower(OmxFollowerConfig(port=PORT, id="omx_follower_arm"))
follower.connect()
print("Connected.")

# pick the first motor key (you can change which one)
k = list(follower.bus.motors.keys())[0]
print("Testing motor key:", k)

# read current position (raw ticks)
p0 = follower.bus.read("Present_Position", k)
print("Present_Position =", p0)

# enable torque (method name varies by branch)
if hasattr(follower.bus, "enable_torque"):
    follower.bus.enable_torque(k)

# command a small move (+100 ticks) then come back
try:
    follower.bus.write("Goal_Position", k, p0 - 15)
    time.sleep(3.0)
    follower.bus.write("Goal_Position", k, p0)
    time.sleep(3.0)
finally:
    # optional: disable torque
    if hasattr(follower.bus, "disable_torque"):
        follower.bus.disable_torque(k)
    follower.disconnect()
    print("Disconnected.")
```
