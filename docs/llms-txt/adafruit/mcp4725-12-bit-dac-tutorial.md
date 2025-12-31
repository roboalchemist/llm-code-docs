# Source: https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial.md

# MCP4725 12-Bit DAC Tutorial

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/108/811/medium800/adafruit_products_MCP4725_top.jpg?1644356800)

Your microcontroller probably has an ADC (analog -\> digital converter) but does it have a DAC (digital -\> analog converter)??? Now it can! This breakout board features the easy-to-use MCP4725 12-bit DAC. Control it via I2C and send it the value you want it to output, and the VOUT pin will have it. Great for audio / analog projects, such as when you can't use PWM but need a sine wave or adjustable bias point.  
  
We break out the ADDR/A0 pin so you can connect two of these DACs on one I2C bus, just tie that pin of one high (or close the jumper on the back) to keep it from conflicting. Also included is a 6-pin header, for use in a breadboard. Works with both 3.3V or 5V logic.

![](https://cdn-learn.adafruit.com/assets/assets/000/108/814/medium800/adafruit_products_MCP4725_back.jpg?1644357350)

Some nice extras with this chip: for chips that have 3.4Mbps Fast Mode I2C (Arduino's don't) you can update the Vout at ~200 KHz. There's an EEPROM so if you write the output voltage, you can 'store it' so if the device is power cycled it will restore that voltage. The output voltage is rail-to-rail and proportional to the power pin so if you run it from 3.3V, the output range is 0-3.3V. If you run it from 5V the output range is 0-5V.  
  
[We have an easy-to-use Arduino and CircuitPython/Python library and tutorial with a triangle-wave and sine-wave output example](http://learn.adafruit.com/mcp4725-12-bit-dac-tutorial) that can be used with just about any microcontroller or microcomputer with I2C host.

![](https://cdn-learn.adafruit.com/assets/assets/000/108/813/medium800/adafruit_products_MCP4725_top_header.jpg?1644357341)

Comes with a bit of 0.1" standard header in case you want to use it with a breadboard or perfboard.&nbsp; Four mounting holes for easy attachment. There's an _optional_ 3.5mm terminal block spot on the PCB - [we don't include a 3.5mm terminal block but they're both common and stocked in the shop](https://www.adafruit.com/product/724) - that you can solder in place if you like.

![](https://cdn-learn.adafruit.com/assets/assets/000/108/812/medium800/adafruit_products_MCP4725_STEMMA_side.jpg?1644357334)

To get you going fast, we spun up a custom-made PCB in the[&nbsp; **STEMMA QT** &nbsp;form factor](https://www.adafruit.com/?q=stemma%20qt%20sensor "STEMMA QT form factor"), making it easy to interface with. The&nbsp;[STEMMA QT connectors](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt)&nbsp;on either side are compatible with the&nbsp;[SparkFun Qwiic](https://www.sparkfun.com/qwiic)&nbsp;I2C connectors. This allows you to make solderless connections between your development board and the MCP4725 or to chain it with a wide range of other sensors and accessories using a&nbsp;[**compatible cable**](https://www.adafruit.com/?q=stemma%20qt%20cable).

[**QT Cable is not included** , but we have a variety in the shop](https://www.adafruit.com/?q=stemma+qt+cable&sort=BestMatch).&nbsp;

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/036/264/medium800/components_935-04.jpg?1475857965)

- [Next Page](https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial/pinouts.md)

## Featured Products

### MCP4725 Breakout Board - 12-Bit DAC with I2C Interface

[MCP4725 Breakout Board - 12-Bit DAC with I2C Interface](https://www.adafruit.com/product/935)
Your microcontroller probably has an ADC (analog -\> digital converter) but does it have a DAC (digital -\> analog converter)??? Now it can! This breakout board features the easy-to-use MCP4725 12-bit DAC. Control it via I2C and send it the value you want it to output, and the VOUT pin...

In Stock
[Buy Now](https://www.adafruit.com/product/935)
[Related Guides to the Product](https://learn.adafruit.com/products/935/guides)

## Related Guides

- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [MCP4725 12-Bit DAC with Raspberry Pi](https://learn.adafruit.com/mcp4725-12-bit-dac-with-raspberry-pi.md)
- [CircuitPython MIDI to CV Skull](https://learn.adafruit.com/circuitpython-midi-to-cv-skull.md)
- [NeoPixel Manicure](https://learn.adafruit.com/neopixel-manicure.md)
- [Adafruit TPS61169 Constant Current Boost Converter for LEDs](https://learn.adafruit.com/adafruit-tps61169-constant-current-boost-converter-for-leds.md)
- [Adafruit Floppy FeatherWing with 34-Pin IDC Connector](https://learn.adafruit.com/adafruit-floppy-featherwing-with-34-pin-idc-connector.md)
- [Remote Control with the Huzzah + Adafruit.io](https://learn.adafruit.com/remote-control-with-the-huzzah-plus-adafruit-io.md)
- [Adafruit ENS160 MOX Gas Sensor](https://learn.adafruit.com/adafruit-ens160-mox-gas-sensor.md)
- [Hallowing Minotaur Maze](https://learn.adafruit.com/hallowing-minotaur-maze.md)
- [DIY Google's "Physical Web" UriBeacons with the Bluefruit LE Friend](https://learn.adafruit.com/google-physical-web-uribeacon-with-the-bluefruit-le-friend.md)
- [Larsio Paint Music](https://learn.adafruit.com/larsio-paint-music.md)
- [Make It Talk](https://learn.adafruit.com/make-it-talk.md)
- [Introducing Gemma](https://learn.adafruit.com/introducing-gemma.md)
- [3D-Printed Bionic Eye](https://learn.adafruit.com/3d-printed-bionic-eye.md)
- [Adafruit PCF8591 Basic 4 x ADC + DAC Breakout](https://learn.adafruit.com/adafruit-pcf8591-adc-dac.md)
