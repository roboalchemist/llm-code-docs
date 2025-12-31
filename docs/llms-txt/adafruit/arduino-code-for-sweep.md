# Source: https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/arduino-code-for-sweep.md

# Arduino Lesson 14. Servo Motors

## Arduino Code for 'Sweep'

Load up the following sketch onto your Arduino. You should find that the servo immediately begins to turn first in one direction and then back in the other.

The sketch is based on the standard 'sweep' sketch that you can find in the Arduino Examples under the folder 'servo'. You can if you prefer just run that sketch.

```
/*
Adafruit Arduino - Lesson 14. Sweep
*/

#include &lt;Servo.h&gt; 

int servoPin = 9;
 
Servo servo;  
 
int angle = 0;   // servo position in degrees 
 
void setup() 
{ 
  servo.attach(servoPin); 
} 
 
 
void loop() 
{ 
  // scan from 0 to 180 degrees
  for(angle = 0; angle &lt; 180; angle++)  
  {                                  
    servo.write(angle);               
    delay(15);                   
  } 
  // now scan back from 180 to 0 degrees
  for(angle = 180; angle &gt; 0; angle--)    
  {                                
    servo.write(angle);           
    delay(15);       
  } 
} 
```

Servo motors are controlled by a series of pulses and to make it easy to use them, an Arduino library has been created so that you can just instruct the servo to turn to a particular angle.

The commands for using a servo are like built-in Arduino commands, but because you are not always going to be using a servo in your projects, they are kept in something called a library. If you are going to use commands in the servo library, you need to tell the Arduino IDE that you are using the library with this command:

```
#include &lt;Servo.h&gt; 
```

As usual, we then use a variable 'servoPin' to define the pin that is to control the servo.

This line:

```
Servo servo;  
```

defines a new variable 'servo' of type 'Servo'. The library has provided us with a new type, like 'int' or 'float' that represents a servo. You can actually define up to eight servos in this way, so if we had two servos, then we could write something like this:

```
Servo servo1;
Servo servo2;
```

&nbsp;In the 'setup' function we need to link the 'servo' variable to the pin that will control the servo using this command:

```
  servo.attach(servoPin); 
```

The variable 'angle' is used to contain the current angle of the servo in degrees. In the 'loop' function, we use two 'for' loops to first increase the angle in one direction and then back in the other when it gets to 180 degrees.

The command:

```
    servo.write(angle);   
```

tells the servo to update its position to the angle supplied as a parameter.

- [Previous Page](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/if-the-servo-misbehaves.md)
- [Next Page](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/the-breadboard-layout-for-knob.md)

## Featured Products

### Standard servo - TowerPro SG-5010

[Standard servo - TowerPro SG-5010](https://www.adafruit.com/product/155)
This high-torque standard servo can rotate approximately 180 degrees (90 in each direction). You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without building a motor controller with feedback & gearbox. Comes with 3...

In Stock
[Buy Now](https://www.adafruit.com/product/155)
[Related Guides to the Product](https://learn.adafruit.com/products/155/guides)
### Premium Male/Male Jumper Wires - 40 x 6" (150mm)

[Premium Male/Male Jumper Wires - 40 x 6" (150mm)](https://www.adafruit.com/product/758)
Handy for making wire harnesses or jumpering between headers on PCB's. These premium jumper wires are 6" (150mm) long and come in a 'strip' of 40 (4 pieces of each of ten rainbow colors). They have 0.1" male header contacts on either end and fit cleanly next to each other...

In Stock
[Buy Now](https://www.adafruit.com/product/758)
[Related Guides to the Product](https://learn.adafruit.com/products/758/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Micro servo

[Micro servo](https://www.adafruit.com/product/169)
Tiny little servo can rotate approximately 180 degrees (90 in each direction) and works just like the standard kinds you're used to but _smaller_. You can use any servo code, hardware, or library to control these servos. Good for beginners who want to make stuff move without...

In Stock
[Buy Now](https://www.adafruit.com/product/169)
[Related Guides to the Product](https://learn.adafruit.com/products/169/guides)
### Standard Size - High Torque - Metal Gear Servo

[Standard Size - High Torque - Metal Gear Servo](https://www.adafruit.com/product/1142)
This high-torque standard servo now comes in a metal-gear flavor, for extra-high torque (10 kg\*cm!) and reliability! It can rotate at least 120 degrees (60 in each direction) with a classic 1.5-2.5ms pulse, but if you can extend your pulses it can go up to about 170 degrees - it varies a bit...

In Stock
[Buy Now](https://www.adafruit.com/product/1142)
[Related Guides to the Product](https://learn.adafruit.com/products/1142/guides)
### Micro Servo - MG90D High Torque Metal Gear

[Micro Servo - MG90D High Torque Metal Gear](https://www.adafruit.com/product/1143)
Add more power to your robot with this metal-geared MG90D&nbsp;servo. The tiny little servo can rotate approximately 90 degrees (45 in each direction) and works just like the standard kinds you're used to but _smaller_. You can use any servo code, hardware, or library to control...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1143)
[Related Guides to the Product](https://learn.adafruit.com/products/1143/guides)

## Related Guides

- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Arduino Lesson 4. Eight LEDs and a Shift Register](https://learn.adafruit.com/adafruit-arduino-lesson-4-eight-leds.md)
- [Adafruit Arduino Selection Guide](https://learn.adafruit.com/adafruit-arduino-selection-guide.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Photocells](https://learn.adafruit.com/photocells.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [Arduino Lesson 7. Make an RGB LED Fader](https://learn.adafruit.com/adafruit-arduino-lesson-7-make-an-rgb-led-fader.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
