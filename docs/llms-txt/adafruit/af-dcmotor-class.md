# Source: https://learn.adafruit.com/adafruit-motor-shield/af-dcmotor-class.md

# Adafruit Motor Shield

## AF_DCMotor Class

Warning: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/853/medium800/adafruit_products_DC_Motors.jpeg?1396776813)

The AF\_DCMotor class provides speed and direction control for up to four DC motors when used with the Adafruit Motor Shield.&nbsp; To use this in a sketch you must first add the following line at the beginning of your sketch:

```
#include &lt;AFMotor.h&gt;
```

# **AF\_DCMotor&nbsp;_motorname_(_portnum_,&nbsp;_freq_)**

> This is the constructor for a DC motor.&nbsp; Call this constructor once for each motor in your sketch.&nbsp; Each motor instance must have a different name as in the example below.

**Parameters:&nbsp;**  

- **port num&nbsp;** - selects which channel (1-4) of the motor controller the motor will be connected to
- **freq&nbsp;** - selects the PWM frequency.&nbsp; If no frequency is specified, 1KHz is used by default.

> > Frequencies for channel 1 & 2 are:&nbsp;  
> > 
> > - MOTOR12\_64KHZ
> > - MOTOR12\_8KHZ
> > - MOTOR12\_2KHZ
> > - MOTOR12\_1KHZ
> > 
> > Frequencies for channel 3 & 4 are:&nbsp;  
> > 
> > - MOTOR34\_64KHZ
> > - MOTOR34\_8KHZ
> > - MOTOR34\_1KHZ

**Example:** ```
AF_DCMotor motor4(4); // define motor on channel 4 with 1KHz default PWM
AF_DCMotor left_motor(1, MOTOR12_64KHZ);  // define motor on channel 1 with 64KHz PWM
```

![](https://cdn-learn.adafruit.com/assets/assets/000/001/854/medium800/adafruit_products_DC_Motor_Ports.gif?1447864310)

_ **Note:** &nbsp; Higher frequencies will produce less audible hum in operation, but may result in lower torque with some motors._# **setSpeed(_speed_)**

> Sets the speed of the motor.&nbsp;

**Parameters:**  

- &nbsp;&nbsp; **speed** - Valid values for 'speed' are between 0 and 255 with 0 being off and 255 as full throttle.

**Example:** _ **Note** _ **:** _&nbsp;DC Motor response is not typically linear, and so the actual RPM will not necessarily be proportional to the programmed speed._# **run(_cmd_)**

> Sets the run-mode of the motor.

**Parameters:**  

- **cmd&nbsp;** - the desired run mode for the motor  

> Valid values for cmd are:  
> 
> - **FORWARD&nbsp;** - run forward (actual direction of rotation will depend on motor wiring)
> - **BACKWARD&nbsp;** - run backwards (rotation will be in the opposite direction from FORWARD)
> - **RELEASE&nbsp;** - Stop the motor.&nbsp; This removes power from the motor and is equivalent to setSpeed(0).&nbsp; The motor shield does not implement dynamic breaking, so the motor may take some time to spin down

  
**Example:** ```
motor.run(FORWARD);
delay(1000);  // run forward for 1 second
motor.run(RELEASE);
delay(100);  // 'coast' for 1/10 second
motor.run(BACKWARDS);  // run in reverse
```

- [Previous Page](https://learn.adafruit.com/adafruit-motor-shield/using-dc-motors.md)
- [Next Page](https://learn.adafruit.com/adafruit-motor-shield/af-stepper-class.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
