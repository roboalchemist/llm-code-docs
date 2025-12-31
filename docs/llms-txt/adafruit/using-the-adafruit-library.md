# Source: https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi/using-the-adafruit-library.md

# Source: https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi/using-the-adafruit-library.md

# Source: https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library.md

# Adafruit 16 Channel Servo Driver with Raspberry Pi

## Using the Adafruit Library

It's easy to control servos with the Adafruit 16-channel servo driver. There are multiple CircuitPython libraries available to work with the different features of this board including [Adafruit CircuitPython PCA9685](https://github.com/adafruit/Adafruit_CircuitPython_PCA9685), and [Adafruit CircuitPython ServoKit](https://github.com/adafruit/Adafruit_CircuitPython_ServoKit). These libraries make it easy to write Python code to control servo motors.

You can use this breakout with your Raspberry Pi and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

# Python Installation of ServoKit Library

You'll need to install the Adafruit\_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

- `sudo pip3 install adafruit-circuitpython-servokit`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

# Controlling Servos

We've written a handy CircuitPython library for the various PWM/Servo boards called [Adafruit CircuitPython ServoKit](https://github.com/adafruit/Adafruit_CircuitPython_ServoKit) that handles all the complicated setup for you. All you need to do is import the appropriate class from the library, and then all the features of that class are available for use. We're going to show you how to import the `ServoKit` class and use it to control servo motors with the Adafruit 16-chanel servo driver breakout.

First you'll need to import and initialize the `ServoKit` class. You must specify the number of channels available on your board. The breakout has 16 channels, so when you create the class object, you will specify `16`.

```
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
```

Now you're ready to control both standard and continuous rotation servos.

# Standard Servos

To control a standard servo, you need to specify the channel the servo is connected to. You can then control movement by setting `angle` to the number of degrees.

For example to move the servo connected to channel `0` to `180` degrees:

```
kit.servo[0].angle = 180
```

To return the servo to `0` degrees:

```
kit.servo[0].angle = 0
```

With a standard servo, you specify the position as an angle. The angle will always be between 0 and the actuation range. The default is 180 degrees but your servo may have a smaller sweep. You can change the total angle by setting `actuation_range`.

For example, to set the actuation range to 160 degrees:

```
kit.servo[0].actuation_range = 160
```

Often the range an individual servo recognises varies a bit from other servos. If the servo didn't sweep the full expected range, then try adjusting the minimum and maximum pulse widths using `set_pulse_width_range(min_pulse, max_pulse)`.

To set the pulse width range to a minimum of 1000 and a maximum of 2000:

```
kit.servo[0].set_pulse_width_range(1000, 2000)
```

That's all there is to controlling standard servos with the PWM/Servo HAT or Bonnet, Python and `ServoKit`!

# Continuous Rotation Servos

To control a continuous rotation servo, you must specify the channel the servo is on. Then you can control movement using `throttle`.

For example, to start the continuous rotation servo connected to channel `1` to full throttle forwards:

```
kit.continuous_servo[1].throttle = 1
```

To start the continuous rotation servo connected to channel `1` to full reverse throttle:

```
kit.continuous_servo[1].throttle = -1
```

To set half throttle, use a decimal:

```
kit.continuous_servo[1].throttle = 0.5
```

And, to stop continuous rotation servo movement set `throttle` to `0`:

```
kit.continuous_servo[1].throttle = 0
```

That's all there is to controlling continuous rotation servos with the PWM/Servo breakout, Python and `ServoKit`!

http://www.youtube.com/watch?v=3Rj1Fep9Ap0

- [Previous Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/hooking-it-up.md)
- [Next Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/library-reference.md)

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
