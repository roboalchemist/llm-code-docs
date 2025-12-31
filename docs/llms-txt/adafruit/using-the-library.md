# Source: https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/using-the-library.md

# MCP230xx GPIO Expander on the Raspberry Pi

## Using the library

Danger: 

Never one to leave you with just a breakout board or an IC and a goodbye, Adafruit provides a library for the MCP23008 and MCP23017 in our [Pi repository on github](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/legacy "Link: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code"). &nbsp;The easiest way to use it is with our convenient [WebIDE](http://learn.adafruit.com/webide), which will automatically point to the Adafruit github repository.  
  
Once you've opened up the WebIDE in the browser, you simply need to click in the left-hand navigation on the following folders and filenames:

- Adafruit-Raspberry-Pi-Python-Code
- Adafruit\_MCP230xx
- Adafruit\_MCP230xx.py

This should give you something similar to the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/468/medium800/raspberry_pi_WebIDE.jpg?1396783426)

```
# Use busnum = 0 for older Raspberry Pi's (256MB)
mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)
# Use busnum = 1 for new Raspberry Pi's (512MB with mounting holes)
# mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

# Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
mcp.config(0, OUTPUT)
mcp.config(1, OUTPUT)
mcp.config(2, OUTPUT)

# Set pin 3 to input with the pullup resistor enabled
mcp.pullup(3, 1)
# Read pin 3 and display the results
print "%d: %x" % (3, mcp.input(3) &gt;&gt; 3)

# Python speed test on output 0 toggling at max speed
while (True):
  mcp.output(0, 1)  # Pin 0 High
  mcp.output(0, 0)  # Pin 1 Low
```

This file contains both the base MCP230xx class that makes it easy to use the chip, along with a very simple demo that will toggle a single pin as fast as possible. &nbsp;The example code shows how you can set pins to both input and output:

# Instantiating an instance of Adafruit\_MCP230xx
To instantiate an instance of the wrapper class that allows you to access the MCP230xx, you need to uncomment one of the two lines at the top of the above code. &nbsp;There are two options because earlier versions of the Pi Model B (pre 512MB SDRAM) used I2C0, whereas the latest Model B devices (with 512MB SDRAM) use I2C1.  
  
The address assumes you are using an MCP23017 with all three address pins set to GND. &nbsp;If you are using a different address pin configuration, you can open up the datasheet to see how the address scheme works ([MCP23017 datasheet](http://ww1.microchip.com/downloads/en/devicedoc/21952b.pdf) or&nbsp;.the [MCP23008 datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21919e.pdf).)  
  
```
# Use busnum = 0 for older Raspberry Pi's (pre 512MB)
mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)
  
# Use busnum = 1 for new Raspberry Pi's (512MB)
# mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
```

# Pin Numbering
  
The MCP23008 has 8 pins - A0 thru A7. **A0** is called **0** in the library, and **A7** is called **7** &nbsp; (the rest follow the same pattern)  
  
The MCP23017 has 16 pins - A0 thru A7 + B0 thru B7. **A0** is called **0** in the library, and **A7** is called **7** , then&nbsp; **B0** continues from there as is called&nbsp; **8** and finally&nbsp; **B7** is pin **15** # Setting a pin as Input
You can enable or disable the internal pullup resistor and set the pins as input with the following lines of code: ```
# Set pin 3 to input with the pullup resistor enabled
mcp.pullup(3, 1)

# Read pin 3 and display the results
print "%d: %x" % (3, mcp.input(3) &gt;&gt; 3)
```

The second line reads pin 3, and shifts the value left 3 bits so that it will equal 0 or 1 depending on whether the pin is high or low when it is sampled. &nbsp;This will results in output similar to the following: "3: 0" or "3: 1" (depending on the pin state).

# Setting a pin as Output
To set &nbsp;a pin as output, you also need two lines of code: ```
# Set pin 0 to output (you can set pins 0..15 this way)
mcp.config(0, OUTPUT)

# Set pin 0 High
mcp.output(0, 1)  

# Set pin 0 Low
mcp.output(0, 0)
```

That's all there is to it! &nbsp;The default sample code will toggle the GPIO pin as fast as possible, and if you hooked it up to an oscilloscope you'd end up with something similar to the following:

http://youtu.be/zBuMJ-R40N0

# Interrupts & Callbacks
  
As it currently stands, the library does not support any sort of interrupt or call back functionality (there is a hardware interrupt pin on the MCP but we don't use it in this code). Only polling is currently supported!  
- [Previous Page](https://learn.adafruit.com/mcp230xx-gpio-expander-on-the-raspberry-pi/hooking-it-all-up.md)

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
