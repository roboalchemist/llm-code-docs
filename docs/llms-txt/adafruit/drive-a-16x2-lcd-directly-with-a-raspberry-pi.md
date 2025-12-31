# Source: https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md

# Drive a 16x2 LCD with the Raspberry Pi

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/726/medium800/raspberry_pi_IMG_5694.jpg?1396775762)

Adding a LCD to any project immediately kicks it up a notch. This tutorial explains how to connect an inexpensive HDD44780 compatible LCD to the Raspberry Pi using 6 GPIO pins. While there are other ways to connect using I2C or the UART, this is the most direct method that gets right down to the bare metal.   
  
This technique:

- allows for&nbsp; **inexpensive LCDs** to be used
- does not require any **i2c drivers**
- won't steal the only **serial port** on the Pi.

The example Python code sends date,&nbsp;time, and the Pi's IP address&nbsp;to the display. If you are running a Pi in headless mode, being able to determine the IP address at a glance is really handy.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/756/medium800/raspberry_pi_timeip.jpg?1396776081)

# To Follow This Tutorial You Will Need
- [Standard LCD 16x2 + extras](http://adafruit.com/products/181 "Link: http://adafruit.com/products/181")
- [Pi T-Cobbler Plus,](https://www.adafruit.com/product/2028)&nbsp;[Pi Cobbler Plus for Model B+ / Pi 2](https://www.adafruit.com/products/2029)&nbsp;or the original [Pi Cobbler](https://www.adafruit.com/product/914)
- [(2) Half size breadboards](https://www.adafruit.com/products/64)&nbsp;
- [Hook-up Wire](https://www.adafruit.com/index.php?main_page=adasearch&q=hook-up+wire+spool "Link: https://www.adafruit.com/index.php?main\_page=adasearch&q=hook-up+wire+spool")
- [A Raspberry Pi](https://www.adafruit.com/?q=raspberry%20pi) (compatible with all 26pin and 40pin Pi releases to date)

Info: 

- [Next Page](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/wiring.md)

## Featured Products

### Standard LCD 16x2 + extras

[Standard LCD 16x2 + extras](https://www.adafruit.com/product/181)
Standard HD44780 LCDs are useful for creating standalone projects.

- 16 characters wide, 2 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Pins are documented on the back of the LCD to assist...

In Stock
[Buy Now](https://www.adafruit.com/product/181)
[Related Guides to the Product](https://learn.adafruit.com/products/181/guides)
### Raspberry Pi 3 - Model B - ARMv8 with 1G RAM

[Raspberry Pi 3 - Model B - ARMv8 with 1G RAM](https://www.adafruit.com/product/3055)
Did you really think the Raspberry Pi would stop getting better? At this point, we sound like a broken record, extolling on the new Pi’s myriad improvements like we’re surprised that the folks at the Raspberry Pi Foundation are continuously making their flagship board better.&nbsp;...

In Stock
[Buy Now](https://www.adafruit.com/product/3055)
[Related Guides to the Product](https://learn.adafruit.com/products/3055/guides)
### Adafruit Assembled Pi T-Cobbler Breakout for Raspberry Pi

[Adafruit Assembled Pi T-Cobbler Breakout for Raspberry Pi](https://www.adafruit.com/product/1754)
Now that you've finally got your hands on a [Raspberry Pi®](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an **assembled** add on prototyping Pi T-Cobbler from Adafruit, which can...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1754)
[Related Guides to the Product](https://learn.adafruit.com/products/1754/guides)
### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Speech Synthesis on the Raspberry Pi](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [Raspberry Pi Analog to Digital Converters](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Getting Started With Windows IoT Core on Raspberry Pi](https://learn.adafruit.com/getting-started-with-windows-iot-on-raspberry-pi.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
