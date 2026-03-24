# Week 11: ROS 2 Essentials Part B – Motor Control

---------------
#### :dizzy: **Date :** March 27
#### :ballot_box_with_check: Please be generous to help others when possible.


## ROS 2 with Motor Control
## Use Open RB150 Starter Kit with Dynamixel Motor

----------
### Step 1. OpenRB Arduino Set-up
- [ ] In Arduino IDE, do the previous settings (see the final part of Slides Week 7 Trajectory Generation.pptx)

Make sure board i OpenRB-150, Port is properly selected.

- [ ] Run this code in Arduino IDE

```c
#include <Dynamixel2Arduino.h>

#if defined(ARDUINO_OpenRB)
#define DXL_SERIAL Serial1
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = -1;
#endif

const uint8_t DXL_ID = 1;
const float DXL_PROTOCOL_VERSION = 2.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);
using namespace ControlTableItem;

void setup() {

  DEBUG_SERIAL.begin(115200);

  dxl.begin(57600);
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  dxl.torqueOff(DXL_ID);
  dxl.setOperatingMode(DXL_ID, OP_POSITION);
  dxl.torqueOn(DXL_ID);

  DEBUG_SERIAL.println("READY");
}

void loop() {

  if (DEBUG_SERIAL.available()) {

    String s = DEBUG_SERIAL.readStringUntil('\n');
    s.trim();

    int goal = s.toInt();

    dxl.setGoalPosition(DXL_ID, goal);

    DEBUG_SERIAL.print("Goal=");
    DEBUG_SERIAL.println(goal);
  }
}
```

-----------
### Step 2. ROS 2 Communication Set-up

- [ ] Now, enter pixi-based ROS env in your PowerShell..<br>
Note, every newly-opened PowerShell window needs to do this first.

```bash
cd C:\Users\YourName\roswin
pixi shell
```

- [ ] Install the Python serial port access library `pyerial` in this env. https://github.com/pyserial/pyserial

```bash
pixi add pyserial
pixi shell
```

- [ ] Create a Python code and place it under the roswin folder. Suppose it is named `motor_test.py`

You should adjust the `COM15` to be your own port name.

```python
import serial
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class SerialMotorNode(Node):

    def __init__(self):

        super().__init__("serial_motor_node")

        self.ser = serial.Serial("COM15", 115200, timeout=1)
        time.sleep(2)

        self.create_subscription(
            Int32,
            "goal_position",
            self.callback,
            10,
        )

        self.get_logger().info("Serial motor node ready")

    def callback(self, msg):

        goal = msg.data
        cmd = f"{goal}\n"

        self.ser.write(cmd.encode())

        self.get_logger().info(f"Sent {goal}")


def main():

    rclpy.init()

    node = SerialMotorNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
```
- [ ] In the same PowerShell, run this Python.

```bash
python motor_test.py
```

-----------
### Step 3. ROS 2 Publish

- [ ] Now, open a **Second PowerShell window**, do this again first:

```bash
cd C:\Users\YourName\roswin
pixi shell
```

- [ ] In this second PowerShell, do this first

```bash
ros2 topic list
```

- [ ] In this second PowerShell, do this second

```bash
ros2 topic pub /goal_position std_msgs/msg/Int32 "{data: 2048}"
```
