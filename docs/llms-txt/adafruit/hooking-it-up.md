# Source: https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi/hooking-it-up.md

# Source: https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/hooking-it-up.md

# Adafruit 16 Channel Servo Driver with Raspberry Pi

## Hooking it Up

The easiest way to hook the servo breakout up to your Pi is using a breadboard and connecting it to the Pi using I2C:

- **Pi 3V3** to **breakout VCC**
- **Pi GND** to **breakout GND**
- **Pi SCL** to **breakout SCL**
- **Pi SDA** to **breakout SDA**
- **Servo orange wire** to **breakout PWM on channel 0**
- **Servo red wire** to **breakout V+ on channel 0**
- **Servo brown wire** to **breakout Gnd on channel 0**

**Check your servo's datasheet to verify which wires go to which pin!**

![components_raspi_pca9685_i2c_with_servo.jpg](https://cdn-learn.adafruit.com/assets/assets/000/069/564/medium640/components_raspi_pca9685_i2c_with_servo.jpg?1547757668)

Danger: 

Danger: 

The PCA9685 (the actual chip that drives the servos) is powered by the 3.3V supply on the Pi (labelled **VCC** on the servo breakout). Because the servos have different power requirements -- typically a 5V supply and as much as a couple hundred mA per servo -- they're powered from a separate power supply, labelled **V+**.  
  
In the example image above with a single servo motor, we are powering the motor from an external 5V power supply connected to the terminal block on the breakout board via a [DC power adapter](http://www.adafruit.com/products/368). Make sure you connect the wires correctly, with +/+ and GND/GND.

## Why not use the +5V supply on the Raspberry Pi?
Switching directions on the servo can cause a lot of noise on the supply, and the servo(s) will cause the voltage to fluctuate significantly, which is a bad situation for the Pi. It's highly recommended to use an external 5V supply with servo motors to avoid problems caused by voltage drops on the Pi's 5V line.  
  

## When to add an optional Capacitor to the driver board
We have a spot on the PCB for soldering in an electrolytic capacitor. Based on your usage, you may or may not need a capacitor. If you are driving a lot of servos from a power supply that dips a lot when the servos move, **n \* 100uF** where **n** is the number of servos is a good place to start - eg **470uF** or more for 5 servos. Since its so dependent on servo current draw, the torque on each motor, and what power supply, there is no "one magic capacitor value" we can suggest which is why we don't include a capacitor in the kit.   
- [Previous Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c.md)
- [Next Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library.md)

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
