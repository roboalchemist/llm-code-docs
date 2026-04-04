# Source: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/adafruit-pi-code.md

# Adafruit's Raspberry Pi Lesson 4. GPIO Setup

## Adafruit Pi Code

To make life easy for those wishing to experiment with attaching electronics to their Pi, Adafruit have produced an extensive and extremely useful collection of code. This includes simple [CircuitPython Libraries](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview) for a large number of modules, including displays, sensors, actuators and more.&nbsp;

To fetch this code, you need to use some software called 'git'. . &nbsp;

You will find the icon for a Terminal on your desktop.

![](https://cdn-learn.adafruit.com/assets/assets/000/075/733/medium800/learn_raspberry_pi_6E51465C-3122-4E8B-B500-A4403A1FBC5C.jpeg?1558115205)

Before we go any further, issue the following commands in a Terminal. This will ensure your packages are up to date. It does not matter which directory you are in.

```
sudo apt-get update
sudo apt-get upgrade -y 
sudo apt-get dist-upgrade -y
```

![](https://cdn-learn.adafruit.com/assets/assets/000/075/735/medium800/learn_raspberry_pi_00E025F2-605E-40D8-B98D-8298C909C325.jpeg?1558116856)

Run the following command to install the&nbsp; **adafruit\_blinka** CircuitPython Libraries.

```auto
sudo apt install python3-pip
pip3 install adafruit-blinka
```

![](https://cdn-learn.adafruit.com/assets/assets/000/075/738/medium800/learn_raspberry_pi_8A525F5B-ABE3-4C64-9433-DBC3BDC33E13.jpeg?1558117184)

- [Previous Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/the-gpio-connector.md)
- [Next Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c.md)

## Featured Products

### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)
### Raspberry Pi 3 Model B Starter Pack - Includes a Raspberry Pi 3

[Raspberry Pi 3 Model B Starter Pack - Includes a Raspberry Pi 3](https://www.adafruit.com/product/3058)
Gotta say - this new Pi 3 is fly. &nbsp;All the cool kids are going to have it - but all the coolest kids are also going to have a big pack of super cool accessories.

We've hand chosen these accessories as the perfect accompaniment to your new Raspberry Pi 3 - Model B. &nbsp;It's...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/3058)
[Related Guides to the Product](https://learn.adafruit.com/products/3058/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)

[Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)](https://www.adafruit.com/product/965)
An optimized collection of parts and pieces to experiment with Raspberry Pi at home, school or work. Great for students and those that want to get their feet wet, no soldering required! **THIS PACK DOES NOT INCLUDE A RASPBERRY PI 1 MODEL B and is NOT compatible with Model B+ or Raspberry Pi...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/965)
[Related Guides to the Product](https://learn.adafruit.com/products/965/guides)
### GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin

[GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin](https://www.adafruit.com/product/862)
That new Raspberry Pi® Model A or B computer you just got has a row of 2x13 pin headers soldered on - those are the GPIO (general purpose input/output) pins and for those of us who like to hack electronics they are where the real fun is. By programming the Pi, you can twiddle those pins...

In Stock
[Buy Now](https://www.adafruit.com/product/862)
[Related Guides to the Product](https://learn.adafruit.com/products/862/guides)
### Programming the Raspberry Pi: Getting Started with Python

[Programming the Raspberry Pi: Getting Started with Python](https://www.adafruit.com/product/1089)
 **Program your own Raspberry Pi projects!**

An updated guide to programming your own Raspberry Pi projects. Learn to create inventive programs and fun games on your powerful Raspberry Pi--with no programming experience required. **This practical book has been revised...**

In Stock
[Buy Now](https://www.adafruit.com/product/1089)
[Related Guides to the Product](https://learn.adafruit.com/products/1089/guides)

## Related Guides

- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Drive a 16x2 LCD with the Raspberry Pi](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 13. Power Control](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Setting up a Raspberry Pi with NOOBS](https://learn.adafruit.com/setting-up-a-raspberry-pi-with-noobs.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
