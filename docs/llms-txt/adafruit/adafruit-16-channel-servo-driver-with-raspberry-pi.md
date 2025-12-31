# Source: https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi.md

# Adafruit 16 Channel Servo Driver with Raspberry Pi

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/695/medium800/raspberry_pi__MG_0389_resize.jpg?1396775432)

Servo motors are often driven using the PWM outputs available on most embedded MCUs. But while the Pi does have native HW support for PWM, there is only one PWM channel available to users at GPIO18. That kind of limits your options if you need to drive more than one servo or if you also want to dim an LED or do some sort of other PWM goodness as well. Thankfully ... the PI **does** have HW I2C available, which we can use to communicate with a PWM driver like the PCA9685, used on Adafruit's 16-channel 12-bit PWM/Servo Driver!  
  
Using this breakout, you can easily drive up to 16 servo motors on your Raspberry Pi using our painless Python library and this tutorial.   
  
Note this cannot be used for driving anything other than analog (1-2 millisecond pulse drive) servos. DC motors, AC motors and 100% digital servos are not going to work. (Note that most 'digital servos' still use the analog pulse interface and are suitable for use with this controller.)

Danger: 

# What you'll need

We'll be using the following items in this tutorial:

- [Adafruit 16-Channel 12-bit PWM/Servo Driver](http://adafruit.com/products/815 "Link: http://adafruit.com/products/815")
- Servo Motor: [Standard Servo](http://www.adafruit.com/products/155 "Link: http://www.adafruit.com/products/155") or [Continuous Rotation Servo](http://www.adafruit.com/products/154 "Link: http://www.adafruit.com/products/154")
- [Female 2.1mm DC Power Adapter](http://www.adafruit.com/products/368 "Link: http://www.adafruit.com/products/368")
- [5V 2A Power Supply](http://www.adafruit.com/products/276)

- [Next Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c.md)

## Featured Products

### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### Standard servo - TowerPro SG-5010

[Standard servo - TowerPro SG-5010](https://www.adafruit.com/product/155)
This high-torque standard servo can rotate approximately 180 degrees (90 in each direction). You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without building a motor controller with feedback & gearbox. Comes with 3...

In Stock
[Buy Now](https://www.adafruit.com/product/155)
[Related Guides to the Product](https://learn.adafruit.com/products/155/guides)
### Continuous Rotation Servo

[Continuous Rotation Servo](https://www.adafruit.com/product/154)
This servo rotates fully forward or backward instead of moving to a position. You can use any servo code, hardware, or library to control these servos. Good for making simple moving robots. Comes with four different horns, as shown.

To control with an Arduino, we suggest connecting...

In Stock
[Buy Now](https://www.adafruit.com/product/154)
[Related Guides to the Product](https://learn.adafruit.com/products/154/guides)
### Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface

[Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface](https://www.adafruit.com/product/815)
You want to make a cool robot, maybe a hexapod walker, or maybe just a piece of art with a lot of moving parts. Or maybe you want to drive a lot of LEDs with precise PWM output. Then you realize that your microcontroller has a limited number of PWM outputs! What now? You could give up OR you...

In Stock
[Buy Now](https://www.adafruit.com/product/815)
[Related Guides to the Product](https://learn.adafruit.com/products/815/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [MIDI Controlled Robot Lyre with CircuitPython](https://learn.adafruit.com/midi-controlled-robot-lyre-with-circuitpython.md)
- [Raspberry Pi Wifi-Controlled Cat Laser Toy](https://learn.adafruit.com/raspberry-pi-wifi-controlled-cat-laser-toy.md)
- [CircuitPython Hardware: PCA9685 PWM & Servo Driver](https://learn.adafruit.com/micropython-hardware-pca9685-pwm-and-servo-driver.md)
- [Adafruit IO Basics: Analog Output](https://learn.adafruit.com/adafruit-io-basics-analog-output.md)
- [Adafruit Motor Selection Guide](https://learn.adafruit.com/adafruit-motor-selection-guide.md)
- [LED Tricks: Gamma Correction](https://learn.adafruit.com/led-tricks-gamma-correction.md)
- [PiGRRL 2](https://learn.adafruit.com/pigrrl-2.md)
- [Retro Gaming with Raspberry Pi](https://learn.adafruit.com/retro-gaming-with-raspberry-pi.md)
- [Arduino Lesson 6. Digital Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [ Adafruit DRV8833 DC/Stepper Motor Driver Breakout Board](https://learn.adafruit.com/adafruit-drv8833-dc-stepper-motor-driver-breakout-board.md)
- [Arduino Yun Temboo Twitter Tracker](https://learn.adafruit.com/arduino-yun-temboo-twitter-tracker.md)
- [Adafruit 16-Channel PWM/Servo HAT & Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi.md)
