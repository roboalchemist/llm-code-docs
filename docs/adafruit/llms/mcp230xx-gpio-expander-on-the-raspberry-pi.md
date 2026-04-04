# Source: https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi.md

# MCP230xx GPIO Expander on the Raspberry Pi

## Overview

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/462/medium800/raspberry_pi__MG_0481.jpg?1396783360)

While the Raspberry Pi packs and awful lot of punch for the price, and it's fairly flexible where HW expandability is concerned, there are situations where you might want a bit more basic digital&nbsp;IO. &nbsp;Thankfully, it's an easy problem to solve with an I2C-enabled device like the MCP23008 (for an extra 8 GPIO pins) or the MCP23017 (for an extra 16 GPIO pins). &nbsp;This tutorial will show you how you can get up and running quickly with either of these chips.

# What You'll Need

- A [Raspberry Pi](http://adafruit.com/products/998) Model B
- A [Pi Cobbler Breakout](http://adafruit.com/products/914)
- An [MCP23017](http://adafruit.com/products/732) or [MCP23008](http://adafruit.com/products/593)
- And LED and a resistor to test with if you don't have a DMM or an oscilloscope
- If you're **not** using [Occidentalis](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2), Adafruit's own Raspberry Pi distro, you'll also need to [make sure your Pi is configured for I2C](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) before running through this tutorial. (If you're using Occidentalis, I2C is already enabled, though, and you're ready to go!)

Danger: 

- [Next Page](https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/hooking-it-all-up.md)

## Featured Products

### MCP23017 - i2c 16 input/output port expander

[MCP23017 - i2c 16 input/output port expander](https://www.adafruit.com/product/732)
Add another 16 pins to your microcontroller using an MCP23017 port expander. The MCP23017 uses two i2c pins (these can be shared with other i2c devices), and in exchange gives you 16 general purpose pins. You can set each of 16 pins to be input, output, or input with a pullup. There's even...

In Stock
[Buy Now](https://www.adafruit.com/product/732)
[Related Guides to the Product](https://learn.adafruit.com/products/732/guides)
### MCP23008 - i2c 8 input/output port expander

[MCP23008 - i2c 8 input/output port expander](https://www.adafruit.com/product/593)
Add another 8 pins to your microcontroller using an MCP23008 port expander. The MCP23008 uses two i2c pins (these can be shared with other i2c devices), and in exchange gives you 8 general purpose pins. You can set each of 8 pins to be input, output, or input with a pullup. There's even...

In Stock
[Buy Now](https://www.adafruit.com/product/593)
[Related Guides to the Product](https://learn.adafruit.com/products/593/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)

## Related Guides

- [Animated Snake Eyes Bonnet for Raspberry Pi](https://learn.adafruit.com/animated-snake-eyes-bonnet-for-raspberry-pi.md)
- [Bluefruit LE Python Library](https://learn.adafruit.com/bluefruit-le-python-library.md)
- [Running Minecraft on a Raspberry Pi](https://learn.adafruit.com/running-minecraft-on-a-raspberry-pi.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Connecting a 16x32 RGB LED Matrix Panel to a Raspberry Pi](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi.md)
- [Battery Powered Raspberry Pi Displays w/RaspiRobot Shield](https://learn.adafruit.com/raspirobot-battery-powered-raspberry-pi-displays.md)
- [Trellis Python Library](https://learn.adafruit.com/trellis-python-library.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [A Sillier Mousetrap: Logging Mouse Data to Adafruit IO with the Raspberry Pi](https://learn.adafruit.com/a-sillier-mousetrap-logging-mouse-data-to-adafruit-io-with-the-raspberry-pi.md)
- [Raspberry Pi Pygame UI basics](https://learn.adafruit.com/raspberry-pi-pygame-ui-basics.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Bonjour (Zeroconf) Networking for Windows and Linux](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux.md)
- [Using a Mini PAL/NTSC Display with a Raspberry Pi](https://learn.adafruit.com/using-a-mini-pal-ntsc-display-with-a-raspberry-pi.md)
- [TMP006 Temperature Sensor Python Library](https://learn.adafruit.com/tmp006-temperature-sensor-python-library.md)
- [Controlling Motors using the Raspberry Pi and RasPiRobot Board V2](https://learn.adafruit.com/controlling-motors-using-the-raspberry-pi-and-raspirobot-board-v2.md)
