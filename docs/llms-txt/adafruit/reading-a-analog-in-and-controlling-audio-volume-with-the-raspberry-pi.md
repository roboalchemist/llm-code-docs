# Source: https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.md

# Analog Inputs for Raspberry Pi Using the MCP3008

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/187/medium800/raspberry_pi_twist.jpg?1396769834)

Teaching the Raspberry Pi how to read analog inputs is easier than you think! The Pi does not include a hardware [analog-to-digital converter](https://en.wikipedia.org/wiki/Analog-to-digital_converter), but an external ADC (such as the [MCP3008](https://www.adafruit.com/products/856)) can be used, along with some SPI code in Python to read external analog devices.

Here is a short list of some analog inputs that could be used with this setup:

- [potentiometer](http://www.adafruit.com/products/356)
- [photocell](http://www.adafruit.com/products/161)
- [force sensitive resistor (FSR)](http://www.adafruit.com/products/166)
- [temperature sensor](http://www.adafruit.com/products/165)
- [2-axis joystick](http://www.adafruit.com/products/512)

This guide uses a&nbsp;potentiometer to control the volume of an audio tone, but the code can be used as the basis for any kind of analog-input project.

- [Next Page](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/connecting-the-cobbler-to-a-mcp3008.md)

## Featured Products

### MCP3008 - 8-Channel 10-Bit ADC With SPI Interface

[MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://www.adafruit.com/product/856)
Need to add analog inputs? This chip will add 8 channels of 10-bit analog input to your microcontroller or microcomputer project. It's super easy to use and uses SPI so only 4 pins are required. We chose this chip as a great accompaniment to the Raspberry Pi computer because it's fun...

In Stock
[Buy Now](https://www.adafruit.com/product/856)
[Related Guides to the Product](https://learn.adafruit.com/products/856/guides)
### Breadboard trim potentiometer

[Breadboard trim potentiometer](https://www.adafruit.com/product/356)
These are our favorite trim pots, perfect for breadboarding and prototyping. They have a long grippy adjustment knob and with 0.1" spacing, they plug into breadboards or perfboards with ease.

This is the same pot that comes with our character LCDs and tutorial...

In Stock
[Buy Now](https://www.adafruit.com/product/356)
[Related Guides to the Product](https://learn.adafruit.com/products/356/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)

## Related Guides

- [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://learn.adafruit.com/mcp3008-spi-adc.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Large Pi-based Thermometer and Clock](https://learn.adafruit.com/large-pi-based-thermometer-and-clock.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
