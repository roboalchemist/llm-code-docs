# Source: https://learn.adafruit.com/16-channel-pwm-servo-driver/chaining-drivers.md

# Adafruit  PCA9685 16-Channel Servo Driver

## Chaining Drivers

Multiple Drivers (up to 62)&nbsp;can be chained to control still more servos. &nbsp;With headers at both ends of the board, the wiring&nbsp;is as simple as connecting a [6-pin parallel cable](https://www.adafruit.com/products/206) from one board to the next.&nbsp;

![](https://cdn-learn.adafruit.com/assets/assets/000/002/223/medium800/adafruit_products_MultiBoard_bb-1024.jpg?1396780621)

## Addressing&nbsp;the Boards
Each board in the chain&nbsp;must be assigned&nbsp;a unique address. &nbsp;This is done with the address jumpers on the upper right edge of the board. &nbsp;The I2C base address for each board is 0x40. &nbsp;The binary address that you program with the address jumpers is added to the base I2C address.  
  
To program the address offset, use a drop of solder to bridge the corresponding address jumper for each binary '1' in the address. ![](https://cdn-learn.adafruit.com/assets/assets/000/002/263/medium800/adafruit_products_2012_10_13_IMG_0692-1024.jpg?1396781108)

Board 0: &nbsp;Address = 0x40 &nbsp;Offset = binary 00000 (no jumpers required)  
Board 1: &nbsp;Address = 0x41 &nbsp;Offset = binary 00001 (bridge A0 as in the photo above)  
Board 2: &nbsp;Address = 0x42 &nbsp;Offset = binary 00010 (bridge A1)  
Board 3: &nbsp;Address = 0x43 &nbsp;Offset = binary 00011 (bridge A0 &&nbsp;A1)  
Board 4: &nbsp;Address = 0x44 &nbsp;Offset = binary 00100 (bridge A2)  
  
etc.

In your sketch, you'll need to declare a separate pobject for each board. Call begin on each object, and control each servo through the object it's attached to. &nbsp;For example:

```
#include &lt;Wire.h&gt;
#include &lt;Adafruit_PWMServoDriver.h&gt;

Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm2 = Adafruit_PWMServoDriver(0x41);

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel PWM test!");

  pwm1.begin();
  pwm1.setPWMFreq(1600);  // This is the maximum PWM frequency

  pwm2.begin();
  pwm2.setPWMFreq(1600);  // This is the maximum PWM frequency
}


```

- [Previous Page](https://learn.adafruit.com/16-channel-pwm-servo-driver/hooking-it-up.md)
- [Next Page](https://learn.adafruit.com/16-channel-pwm-servo-driver/using-the-adafruit-library.md)

## Featured Products

### Micro servo

[Micro servo](https://www.adafruit.com/product/169)
Tiny little servo can rotate approximately 180 degrees (90 in each direction) and works just like the standard kinds you're used to but _smaller_. You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without...

In Stock
[Buy Now](https://www.adafruit.com/product/169)
[Related Guides to the Product](https://learn.adafruit.com/products/169/guides)
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
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [LED Tricks: Gamma Correction](https://learn.adafruit.com/led-tricks-gamma-correction.md)
- [MIDI Controlled Robot Lyre with CircuitPython](https://learn.adafruit.com/midi-controlled-robot-lyre-with-circuitpython.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Programming Arduino with Android and Windows Tablets](https://learn.adafruit.com/programming-arduino-with-android-and-windows-tablets.md)
- [DS1307 Real Time Clock Breakout Board Kit](https://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit.md)
