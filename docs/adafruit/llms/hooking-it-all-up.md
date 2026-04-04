# Source: https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/hooking-it-all-up.md

# MCP230xx GPIO Expander on the Raspberry Pi

## Hooking it all up

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/467/medium800/raspberry_pi_MCP23017_bb.jpg?1396783409)

The way that you hook the chip up to your breadboard will depend on the package you use (8-pin MCP23008 or 16-pin MCP23017). The pinouts are quite different between the two chips, so check the datasheet carefully first.  
  
The MCP23017 is shown above with two LEDs connected, on GPA0 and GPA1.

1. The yellow line is SDA
2. The green line is SCL
3. The three black lines on top are the address pins
4. The brown pin is RESET which must be pulled high for normal operation
5. Red is 3.3V
6. Black is GND.

Since these io expander chips use i2c to communiate, you _can_ theoretically power them from 5V while still connecting the i2c data lines to a 3.3V device like the pi. That's because the Pi has two i2c resistors that pull up SDA/SCL to 3.3V. Just make sure not to connect any resistors to SDA/SCL to 5V and you can power the chip from 5V (and have 5V input/output on the MCP chip). Its also fine of course to power the MCP chip from 3.3V but the 5V line on the Pi has more current capability so you might find its better to go that way.

**BUT** if your Pi power supply drifts a little higher than 5V, it might stop being able to register the 3.3V signal. So we recommend starting with 3.3V, and if you need 5V GPIO signalling on the MCP expander, try swapping the red wire to 5.0V  
  
You can compare the two pinouts below to figure out how the 8-pin package should be hooked up depending on the pin names:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/464/medium800/raspberry_pi_DIP8.jpg?1396783391)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/466/medium800/raspberry_pi_MCP23017.jpg?1396783400)

You're free to hook anything you want up to the 8 or 16 GPIO pins, but LEDs are used here since most people have one or two laying around and it's an easy way to verify the pin outputs. &nbsp;Be sure to connect a resistor in series to GND, though, to prevent the LED from burning out (if you don't know what value or the details of your LED try something large like 1K to start with).  
  
Here's a quick video of the setup I was using during testing and development. &nbsp;An MCP23017 is used here, running out to a mixed-signal&nbsp;oscilloscope with an 8-channel logic analyzer (ergo the white clip-ons on all the GPIO pins).

http://youtu.be/DfnOYQY4AEI

- [Previous Page](https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/using-the-library.md)

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
