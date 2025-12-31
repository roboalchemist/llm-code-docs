# Source: https://learn.adafruit.com/adafruit-motor-shield/af-stepper-class.md

# Source: https://learn.adafruit.com/afmotor-library-reference/af-stepper-class.md

# AFMotor Library Reference

## AF_Stepper Class

![](https://cdn-learn.adafruit.com/assets/assets/000/001/575/medium800/adafruit_products_Stepper_Motors.jpg?1396773989)

The AF\_Stepper class provides single and multi-step control for up to 2 stepper motors when used with the Adafruit Motor Shield.&nbsp; To use this in a sketch you must first add the following line at the beginning of your sketch:

```
#include &lt;AFMotor.h&gt;
```

# AF\_Stepper _steppername_(_steps_, _portnumber_)
The AF\_Stepper constructor defines a stepper motor.&nbsp; Call this once for each stepper motor in your sketch.&nbsp; Each stepper motor instance must have a unique name as in the example below.  
  
**Parameters:**  

- **steps** - declare the number of steps per revolution for your motor.
- **num** - declare how the motor will be wired to the shield.&nbsp; 

> Valid values for 'num' are 1 (channels 1 & 2) and 2 (channels 3 & 4).

**Example:**  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/570/medium800/adafruit_products_Stepper_Ports.gif?1447864293)

```
AF_Stepper Stepper1(48, 1);  // A 48-step-per-revolution motor on channels 1 &amp; 2
AF_Stepper Stepper2(200, 2);   // A 200-step-per-revolution motor on channels 3 &amp; 4
```

# step(_steps, direction, style_)
Step the motor.  
  
**Parameters:**  

- **steps** - the number of steps to turn
- **direction** - the direction of rotation ( **FORWARD** or **BACKWARD** )
- **style** - the style of stepping:

> Valid values for 'style' are:

> - **SINGLE** - One coil is energized at a time.
> - **DOUBLE** - Two coils are energized at a time for more torque.
> - **INTERLEAVE** - Alternate between single and double to create a half-step in between.&nbsp; This can result in smoother operation, but because of the extra half-step, the speed is reduced by half too.
> - **MICROSTEP** - Adjacent coils are ramped up and down to create a number of 'micro-steps' between each full step.&nbsp; This results in finer resolution and smoother rotation, but with a loss in torque.

_ **Note:** Step is a synchronous command and will not return until all steps have completed.&nbsp; For concurrent motion of two motors, you must handle the step timing for both motors and use the "onestep()" function below._  
  
**Example:**  
  
  
```
Stepper1.step(100, FORWARD, DOUBLE); // 100 steps forward using double coil stepping
Stepper2.step(100, BACKWARD, MICROSTEP);   // 100 steps backward using double microstepping
```

# **setSpeed(_RPMspeed_)**
set the speed of the motor  
  
**Parameters:**  

- Speed - the speed in RPM

  
_ **Note:** The resulting step speed is based on the 'steps' parameter in the constructor.&nbsp; If this does not match the number of steps for your motor, you actual speed will be off as well._  
  
**Example:**  
```
Stepper1.setSpeed(10);  // Set motor 1 speed to 10 rpm  
Stepper2.setSpeed(30);  // Set motor 2 speed to 30 rpm  
```

# onestep(_direction, stepstyle_)
Single step the motor.  
  
**Parameters:**  

- **direction** - the direction of rotation ( **FORWARD** or **BACKWARD** )
- **stepstyle** - the style of stepping:

> Valid values for 'style' are:

> - **SINGLE** - One coil is energized at a time.
> - **DOUBLE** - Two coils are energized at a time for more torque.
> - **INTERLEAVE** - Alternate between single and double to create a half-step in between.&nbsp; This can result in smoother operation, but because of the extra half-step, the speed is reduced by half too.
> - **MICROSTEP** - Adjacent coils are ramped up and down to create a number of 'micro-steps' between each full step.&nbsp; This results in finer resolution and smoother rotation, but with a loss in torque.

**Example:**  
```
Stepper1.onestep(FORWARD, DOUBLE);  // take one step forward using double coil stepping
```

# release()
Release the holding torque on the motor.&nbsp; This reduces heating and current demand, but the motor will not actively resist rotation.  
  
**Example:**  
```
Stepper1.release(); // stop rotation and turn off holding torque.
```

- [Previous Page](https://learn.adafruit.com/afmotor-library-reference/af-dcmotor.md)

## Related Guides

- [MCP4725 12-Bit DAC Tutorial](https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial.md)
- [Adafruit 1.14" 240x135 Color Newxie TFT Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-newxie-tft-display.md)
- [Adafruit MEMENTO Camera Board](https://learn.adafruit.com/adafruit-memento-camera-board.md)
- [Adafruit LTR390 UV Sensor](https://learn.adafruit.com/adafruit-ltr390-uv-sensor.md)
- [DC & USB Boarduino Kits](https://learn.adafruit.com/boarduino-kits.md)
- [Adafruit STM32F405 Feather Express](https://learn.adafruit.com/adafruit-stm32f405-feather-express.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [CircuitPython BLE Crickit Rover](https://learn.adafruit.com/circuitpython-ble-crickit-rover.md)
- [Adafruit Audio FX Sound Board](https://learn.adafruit.com/adafruit-audio-fx-sound-board.md)
- [Adafruit NeoPixel FeatherWing](https://learn.adafruit.com/adafruit-neopixel-featherwing.md)
- [TMP006 Infrared Sensor Breakout](https://learn.adafruit.com/infrared-thermopile-sensor-breakout.md)
- [Adafruit VEML7700 Ambient Light Sensor](https://learn.adafruit.com/adafruit-veml7700.md)
- [Adafruit Wiz5500 Ethernet Co-Processor Breakout Board](https://learn.adafruit.com/adafruit-wiz5500-ethernet-co-processor-breakout-board.md)
- [Adafruit ItsyBitsy nRF52840 Express](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express.md)
- [Cam Follower Automaton](https://learn.adafruit.com/cam-follower-automaton.md)
