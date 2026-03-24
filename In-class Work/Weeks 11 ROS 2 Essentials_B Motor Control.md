# Week 11: ROS 2 Essentials B Motor Control

---------------
#### :dizzy: **Date :** March 27
#### :ballot_box_with_check: Please be generous to help others when possible.


## ROS 2 with Motor Control
## Use Open RB150 Starter Kit with Dynamixel Motor

In Arduino IDE, do the previous settings (see the final part of Slides Week 7 Trajectory Generation.pptx)

Make sure board i OpenRB-150, Port is properly selected.

Run this code in Arduino IDE

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

