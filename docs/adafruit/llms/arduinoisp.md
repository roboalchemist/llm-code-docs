# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduinoisp.md

# Arduino Tips, Tricks, and Techniques

## ArduinoISP

## Introduction
A lot of people start learning about microcontrollers with an Arduino but then want to build their own projects without having to sacrifice their dev board. Or maybe they want to make their own Arduino variant, that is compatible with the IDE. Either way, a common problem is how to burn the bootloader onto the fresh AVR chip. Since AVRs come blank, they need to be set up to be Arduino IDE compatible but to do that you need an AVR programmer (like the USBtinyISP).  
  
[The good news is that you can burn bootloader using your existing Arduino with only a little bit of work. There's even a minitutorial on the arduino.cc site](http://arduino.cc/en/Tutorial/ArduinoISP).  
  
This tutorial is an extention of that tutorial. First we'll show how you can make a permanent bootloader-burner by soldering a [28-pin ZIF socket](https://www.adafruit.com/products/382) to a [proto shield](https://www.adafruit.com/products/51)and use the PWM output line of the Arduino to generate a clock. This will let you 'rescue' many chips that have been set to the wrong type of oscillator, or change ones that are set from external oscillator (most Arduino bootloaders) to internal (such as the lilypad).  
## Parts
You will need…
- [An Arduino](http://www.adafruit.com/products/50)
- [A proto shield kit](https://www.adafruit.com/products/51)
- [28-pin ZIF (zero-insertion force) socket](https://www.adafruit.com/products/382 "Link: https://www.adafruit.com/products/382") (you can use a plain socket but ZIF is ideal)
- [Some wire](https://www.adafruit.com/products/289)
- [Blank ATmega328P](http://www.adafruit.com/partfinder/microcontroller?s%5B%5D=atmega328p)

If you bought the kit from Adafruit, you'll have an extra few items such as a Piezo beeper, LEDs, buttons, etc. that you can use for the [Standalone version of this project](http://learn.adafruit.com/standalone-avr-chip-programmer "Link: http://learn.adafruit.com/standalone-avr-chip-programmer"), just ignore them for now!  
## Assemble
First up, place the ZIF socket on the proto shield like so:  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/542/medium800/learn_arduino_zifplace.jpg?1396798173)

Solder all 28 pins for a solid connection!![](https://cdn-learn.adafruit.com/assets/assets/000/003/543/medium800/learn_arduino_zifsolder.jpg?1396798180)

Solder the following wires to the ZIF socket  

- Pin 1 to digital 10 - Blue **Don't forget to bend the wire over underneath to connect to the ZIF socket pin when soldering!!!**
- Pin 7 to 5V - Red
- Pin 8 to Ground - Black
- Pin 9 to digital 9 - Gray
- Pin 17 to digital 11 - Brown
- Pin 18 to digital 12 - Orange
- Pin 19 to digital 13 - Yellow
- Pin 20 to +5V - Red
- Pin 22 to Ground - Black

![](https://cdn-learn.adafruit.com/assets/assets/000/003/544/medium800/learn_arduino_ispwiring.jpg?1396798190)

Follow the protoshield tutorial to solder in the Red LED into **LED1** position, Green LED into **LED2** position. Also solder in the two 1.0K resistors next to the LEDs. We'll use the LEDs as indicators. Then solder a wire from the LED2 breakout (white) to analog 0 and a wire from LED1 breakout (white) to digital 8.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/545/medium800/learn_arduino_extras.jpg?1396798201)

Finally, you'll need to solder on the header to allow the shield to be placed on, break the 0.1" male header and place it into the Arduino sockets. Then place the shield above on top to solder it in place.![](https://cdn-learn.adafruit.com/assets/assets/000/003/546/medium800/learn_arduino_diecheader.jpg?1396798208)

## Load the Code

Time to load the sketch! [Grab the code from our Github repository and paste it into a new sketch](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/ArduinoISP/ArduinoISP/ArduinoISP.ino). Then upload it to the Arduino.

Danger: 

Plug the shield on top, lift the latch, pop in the chip and then lower the latch. Make sure the chip orientation is like so (so with the lever on the left side you can read the text):

![](https://cdn-learn.adafruit.com/assets/assets/000/003/547/medium800/learn_arduino_extras.jpg?1396798214)

With the USB cable still plugged in (and the same Serial port selected as before) Select **Tools→Burn Bootloader→w/Arduino as ISP**

![](https://cdn-learn.adafruit.com/assets/assets/000/003/548/medium800/learn_arduino_burnbootloader.gif?1448059448)

On newer versions of the Arduino IDE, select **Arduino as ISP** from the **Tools→Programmer** menu, then select **Burn Bootloader** from the Tools menu.

![](https://cdn-learn.adafruit.com/assets/assets/000/010/430/medium800/learn_arduino_Arduino_ISP_menu.png?1396905627)

The Green LED will be on during the programming, when its done you'll see this message and the LED will turn off.![](https://cdn-learn.adafruit.com/assets/assets/000/003/549/medium800/learn_arduino_done.gif?1448059443)

Thats it! Don't forget, you can burn a few different **kinds** of bootloaders, such as Uno, Duemilanove, Lilypad so depending on your situation you may want to use one over the other.

## Bonus! Using with AVRdude
You can use ArduinoISP from the command line very easily, with AVRdude which is the standard program used to program AVRs by running:  
```
avrdude -c arduino -p atmega328 -P COMPORT -b 19200 -U flash:w:filetoburn.hex
```

Instead of **atmega328** you can also program **atmega8**  **atmega88**  **atmega48**  **atmega168,** etc.

- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-hacks.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Arduino bootloader-programmed chip (Atmega328P)

[Arduino bootloader-programmed chip (Atmega328P)](https://www.adafruit.com/product/123)
This is a preprogrammed Atmega328P chip, useful if you want to make your own Arduino-compatible or repair a damaged chip on an exisiting Arduino UNO, Duemilanove, Diecimila, or NG!  
  
This chip is programmed with 'ADAboot', my version of the bootloader that is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/123)
[Related Guides to the Product](https://learn.adafruit.com/products/123/guides)

## Related Guides

- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
