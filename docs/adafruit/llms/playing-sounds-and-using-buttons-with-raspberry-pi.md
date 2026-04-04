# Source: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md

# Playing sounds and using buttons with Raspberry Pi

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/000/877/medium800/raspberry_pi_IMG_4926.jpg?1396766100)

This guide describes how to use CircuitPython on a Raspberry Pi to trigger audio file playback using tactile button presses. This tutorial works will all versions of Raspberry Pi hardware to date (v1, v2, v3, Zero, etc.) If you have not already used the Raspberry Pi as a input device this guide will show you how to wire up the buttons to the GPIO pins and access their state from a python script.&nbsp;

## To Follow This Tutorial You Will Need
- [A Raspberry Pi](https://www.adafruit.com/?q=raspberry%20pi)&nbsp;(compatible with all 26pin and 40pin Pi releases to date)
- [Pi T-Cobbler Plus,](https://www.adafruit.com/product/2028)&nbsp;[Pi Cobbler Plus for Model B+ / Pi 2](https://www.adafruit.com/products/2029)&nbsp;or the original&nbsp;[Pi Cobbler](https://www.adafruit.com/product/914)
- [(1) Half size breadboard](https://www.adafruit.com/products/64)
- [Hook-up Wire](https://www.adafruit.com/index.php?main_page=adasearch&q=hook-up+wire+spool "Link: https://www.adafruit.com/index.php?main\_page=adasearch&q=hook-up+wire+spool")
- [(3) Tactile Button Switches](https://www.adafruit.com/product/367)
- [(1) 5v 2.5A Switching Power Supply](https://www.adafruit.com/product/1995)

- [Next Page](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/prerequisite-pi-setup.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Tactile Button switch (6mm) x 20 pack

[Tactile Button switch (6mm) x 20 pack](https://www.adafruit.com/product/367)
Little clicky switches are standard input "buttons" on electronic projects. These work best in a PCB but [can be used on a solderless breadboard as shown in this tutorial](https://learn.adafruit.com/adafruit-arduino-lesson-6-digital-inputs?view=all). The pins are normally...

In Stock
[Buy Now](https://www.adafruit.com/product/367)
[Related Guides to the Product](https://learn.adafruit.com/products/367/guides)
### Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base

[Adafruit Raspberry Pi B+ / Pi 2 / Pi 3 Case - Smoke Base](https://www.adafruit.com/product/2258)
It took awhile to perfect&nbsp;-&nbsp;but that's okay&nbsp;since we can now safely say that the Adafruit case for Raspberry Pi Model B+ / Pi 2 / Pi 3&nbsp;is The Single&nbsp;Greatest Raspberry Pi Model B+ Case Ever.

This enclosure&nbsp;was designed by Mike Doell - just like our...

In Stock
[Buy Now](https://www.adafruit.com/product/2258)
[Related Guides to the Product](https://learn.adafruit.com/products/2258/guides)
### 5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable

[5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable](https://www.adafruit.com/product/1995)
Our all-in-one 5V 2.5 Amp + MicroUSB cable power adapter is the perfect choice for powering single-board computers like Raspberry Pi, BeagleBone, or anything else that's power-hungry!

This adapter was specifically designed to provide 5.25V, not 5V, but we still call it a 5V USB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1995)
[Related Guides to the Product](https://learn.adafruit.com/products/1995/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)
### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)

## Related Guides

- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 13. Power Control](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Analog Inputs for Raspberry Pi Using the MCP3008](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Raspberry Pi WiFi Radio](https://learn.adafruit.com/pi-wifi-radio.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [USB Rechargeable Cordless Soldering Iron](https://learn.adafruit.com/usb-rechargeable-cordless-soldering-iron.md)
