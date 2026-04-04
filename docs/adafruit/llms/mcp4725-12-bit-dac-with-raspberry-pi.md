# Source: https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi.md

# MCP4725 12-Bit DAC with Raspberry Pi

## Overview

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/738/medium800/raspberry_pi_DAC_Scope.png?1396775912)

Already mastered&nbsp;[Analog Inputs with the Pi](http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi), and looking for a new challenge? &nbsp;How about:&nbsp;How can&nbsp;I&nbsp;generate an analog output on the Pi?!  
  
There are several ways you can accomplish this, but one of the easiest and most flexible is to use a dedicated IC called a **Digital to Analog Convertor** &nbsp;(or DAC).&nbsp;&nbsp;A DAC allows you to specify a numeric value (0..255 for an 8-bit DAC, 0..4095 for a 12-bit DAC, etc.), and the IC will output a voltage based on the supply voltage, and relative to that numeric value. &nbsp;For example, using a 12-bit DAC like the [MCP4725](http://www.adafruit.com/products/935) we'll be using here, setting the value to 2048 on a 3.3V system will results in ~1.65V output on the DAC.  
  
This guide will show you everything you need to know to be able to generate precise analog outputs using your Pi and the MCP4725 12-Bit I2C DAC, from connecting everything up, to how to use our easy Python library.

# What You'll Need
The following products are used in&nbsp;this tutorial:  

- [Adafruit MCP4725 12-Bit DAC](http://www.adafruit.com/products/935 "Link: http://www.adafruit.com/products/935")
- [Pi Cobbler](https://www.adafruit.com/products/914)

- [Next Page](https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi/configuring-your-pi-for-i2c.md)

## Featured Products

### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### MCP4725 Breakout Board - 12-Bit DAC with I2C Interface

[MCP4725 Breakout Board - 12-Bit DAC with I2C Interface](https://www.adafruit.com/product/935)
Your microcontroller probably has an ADC (analog -\> digital converter) but does it have a DAC (digital -\> analog converter)??? Now it can! This breakout board features the easy-to-use MCP4725 12-bit DAC. Control it via I2C and send it the value you want it to output, and the VOUT pin...

In Stock
[Buy Now](https://www.adafruit.com/product/935)
[Related Guides to the Product](https://learn.adafruit.com/products/935/guides)

## Related Guides

- [MCP4725 12-Bit DAC Tutorial](https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial.md)
- [CircuitPython MIDI to CV Skull](https://learn.adafruit.com/circuitpython-midi-to-cv-skull.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Read-Only Raspberry Pi](https://learn.adafruit.com/read-only-raspberry-pi.md)
- [Using a 5V Stepper Motor with the RasPiRobot Board V2](https://learn.adafruit.com/using-a-5v-stepper-motor-with-the-raspirobot-board-v2.md)
- [Soundboard Speaker for Bikes & Scooters](https://learn.adafruit.com/soundboard-speaker-for-bikes-scooters.md)
- [Adafruit's Raspberry Pi Lesson 7. Remote Control with VNC](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc.md)
- [Fruit Jam Video Music](https://learn.adafruit.com/fruit-jam-video-music.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Adafruit PiTFT - 2.8" Touchscreen Display for Raspberry Pi](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi.md)
- [apt.adafruit.com](https://learn.adafruit.com/apt-adafruit-com.md)
- [Raspberry Pi Thermal Printer One Time Pads](https://learn.adafruit.com/raspberry-pi-thermal-printer-one-time-pads.md)
- [CLUE Text Telephone Transmitter](https://learn.adafruit.com/clue-teletype-transmitter.md)
- [Adafruit MAX31865 RTD PT100 or PT1000 Amplifier](https://learn.adafruit.com/adafruit-max31865-rtd-pt100-amplifier.md)
