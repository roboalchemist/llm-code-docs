# Source: https://learn.adafruit.com/afmotor-library-reference/af-dcmotor.md

# AFMotor Library Reference

## AF_DCMotor Class

![](https://cdn-learn.adafruit.com/assets/assets/000/001/574/medium800/adafruit_products_DC_Motors.jpg?1396773984)

The AF\_DCMotor class provides speed and direction control for up to four DC motors when used with the Adafruit Motor Shield.&nbsp; To use this in a sketch you must first add the following line at the beginning of your sketch:

```
#include &lt;AFMotor.h&gt;

```

# **AF\_DCMotor _motorname_(_portnum_, _freq_)**

> This is the constructor for a DC motor.&nbsp; Call this constructor once for each motor in your sketch.&nbsp; Each motor instance must have a different name as in the example below.

**Parameters:**   

- **port num** - selects which channel (1-4) of the motor controller the motor will be connected to
- **freq** - selects the PWM frequency.&nbsp; If no frequency is specified, 1KHz is used by default.

> > Frequencies for channel 1 & 2 are:   
> > 
> > - MOTOR12\_64KHZ
> > - MOTOR12\_8KHZ 
> > - MOTOR12\_2KHZ 
> > - MOTOR12\_1KHZ 
> > 
> > Frequencies for channel 3 & 4 are:   
> > 
> > - MOTOR34\_64KHZ 
> > - MOTOR34\_8KHZ 
> > - MOTOR34\_1KHZ

**Example:**  
```
AF_DCMotor motor4(4); // define motor on channel 4 with 1KHz default PWM
AF_DCMotor left_motor(1, MOTOR12_64KHZ);  // define motor on channel 1 with 64KHz PWM
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/577/medium800/adafruit_products_DC_Motor_Ports.gif?1447864294)

_ **Note:** &nbsp; Higher frequencies will produce less audible hum in operation, but may result in lower torque with some motors._  
# **setSpeed(_speed_)**

> Sets the speed of the motor.

**Parameters:**  

- &nbsp; **speed** - Valid values for 'speed' are between 0 and 255 with 0 being off and 255 as full throttle.

**Example:**  
```
  motor1.setSpeed(255);  // Set motor 1 to maximum speed
  motor4.setSpeed(127);  // Set motor 4 to half speed 
```

_ **Note** _ **:** _DC Motor response is not typically linear, and so the actual RPM will not necessarily be proportional to the programmed speed._  
# **run(_cmd_)**

> Sets the run-mode of the motor.

**Parameters:**  

- **cmd** - the desired run mode for the motor  

> Valid values for cmd are:  
> 
> - **FORWARD** - run forward (actual direction of rotation will depend on motor wiring)
> - **BACKWARD** - run backwards (rotation will be in the opposite direction from FORWARD)
> - **RELEASE** - Stop the motor.&nbsp; This removes power from the motor and is equivalent to setSpeed(0).&nbsp; The motor shield does not implement dynamic breaking, so the motor may take some time to spin down

  
**Example:** ```
motor.run(FORWARD);
delay(1000);  // run forward for 1 second
motor.run(RELEASE);
delay(100);  // 'coast' for 1/10 second
motor.run(BACKWARDS);  // run in reverse
```

- [Next Page](https://learn.adafruit.com/afmotor-library-reference/af-stepper-class.md)

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
