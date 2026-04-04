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

- [Adafruit NeoKey 5x6 Ortho Snap-Apart](https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart.md)
- [Adafruit Stepper + DC Motor FeatherWing](https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Adafruit Pro Trinket LiPoly/LiIon Backpack](https://learn.adafruit.com/adafruit-pro-trinket-lipoly-slash-liion-backpack.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [LOVE Light](https://learn.adafruit.com/love-light.md)
- [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://learn.adafruit.com/mcp3008-spi-adc.md)
- [Adafruit 16-Channel PWM/Servo HAT & Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi.md)
- [Adafruit TPS61169 Constant Current Boost Converter for LEDs](https://learn.adafruit.com/adafruit-tps61169-constant-current-boost-converter-for-leds.md)
- [Makey Paper Craft ](https://learn.adafruit.com/makey-paper-craft.md)
- [Adafruit Chainable DS18B20 Extender Breakout](https://learn.adafruit.com/adafruit-chainable-ds18b20-extender-breakout.md)
- [TSL2561 Luminosity Sensor](https://learn.adafruit.com/tsl2561.md)
- [Adafruit PowerBoost 500 Shield](https://learn.adafruit.com/adafruit-powerboost-500-shield-rechargeable-battery-pack.md)
- [Circuit Playground: R is for Robots](https://learn.adafruit.com/circuit-playground-r-is-for-robots.md)
