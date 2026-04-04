# Source: https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c.md

# Adafruit 16 Channel Servo Driver with Raspberry Pi

## Configuring Your Pi for I2C

Before you can get started with I2C on the Pi, you'll need to run through a couple quick steps from the console. &nbsp;  
  
If you are running Rasbian and are familiar with Terminal commands, then the description below will be sufficient.  
  
If not, then to learn more about how to setup I2C with Raspbian, then take a minor diversion to this Adafruit Tutorial: [http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)  
  
When you are ready to continue,&nbsp;enter the following commands to add SMBus support&nbsp;(which includes I2C) to Python:

```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```

 **i2c-tools** isn't strictly required, but it's a useful package since you can use it to scan for any I2C or SMBus devices connected to your board. If you know something is connected, but you don't know it's 7-bit I2C address, this library has a great little tool to help you find it. **python-smbus** is required, it adds the I2C support for python!  
  
If you have an Original Raspberry Pi (Sold before October 2012) - the I2C is port 0:

```
sudo i2cdetect -y 0
```

If you have a second rev Raspberry Pi, the I2C is on port 1:

```
sudo i2cdetect -y 1
```

This will search /dev/i2c-0 or /dev/i2c-1 for all address, and if an Adafruit&nbsp;PWM breakout is properly connected and it's set to it's default address -- meaning&nbsp;none of the 6 address solder jumpers at the top of the board&nbsp;have been soldered shut --&nbsp;it should show up at 0x40 (binary 1000000) as follows:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/700/medium800/raspberry_pi_i2cdetect.png?1396775470)

Once both of these packages have been installed, you have everything you need to get started accessing I2C and SMBus devices in&nbsp;Python.

- [Previous Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/hooking-it-up.md)

## Featured Products

### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

In Stock
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

- [Raspberry Pi Wifi-Controlled Cat Laser Toy](https://learn.adafruit.com/raspberry-pi-wifi-controlled-cat-laser-toy.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [CircuitPython Hardware: PCA9685 PWM & Servo Driver](https://learn.adafruit.com/micropython-hardware-pca9685-pwm-and-servo-driver.md)
- [LED Tricks: Gamma Correction](https://learn.adafruit.com/led-tricks-gamma-correction.md)
- [Adafruit Motor Selection Guide](https://learn.adafruit.com/adafruit-motor-selection-guide.md)
- [Adafruit IO Basics: Analog Output](https://learn.adafruit.com/adafruit-io-basics-analog-output.md)
- [MIDI Controlled Robot Lyre with CircuitPython](https://learn.adafruit.com/midi-controlled-robot-lyre-with-circuitpython.md)
- [Digital Circuits 4: Sequential Circuits](https://learn.adafruit.com/digital-circuits-4-sequential-circuits.md)
- [MASLOW: an Open WiFi Detector with Adafruit Pro Trinket and CC3000](https://learn.adafruit.com/wifi-hotspot-finder-adafruit-pro-trinket-cc3000.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
- [CRICKIT Flippy Robot](https://learn.adafruit.com/crickit-flippy-robot.md)
- [Adafruit NFC/RFID on Raspberry Pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi.md)
- [Stumble-Bot](https://learn.adafruit.com/stumble-bot-with-circuit-playground-and-crickit.md)
- [Adabot Toy Robot Friend](https://learn.adafruit.com/adabot-rp2040.md)
- [Making PCB Jewelry & Art with Gingerbread and KiCad](https://learn.adafruit.com/making-pcb-art-with-gingerbread-and-kicad.md)
