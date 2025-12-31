# Source: https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial/using-with-arduino.md

# MCP4725 12-Bit DAC Tutorial

## Arduino Code

## Library Installation

Once wired up, to start using the MCP4725, you'll need to install the [Adafruit\_MCP4725 library](https://github.com/adafruit/Adafruit_MCP4725). The library is available through the Arduino library manager so we recommend taking that approach.

From the Arduino IDE, open up the Library Manager:

![Library](https://cdn-learn.adafruit.com/assets/assets/000/085/942/medium640/adafruit_products_library_manager_menu.png?1576653625 )

Click the&nbsp; **Manage Libraries ...** &nbsp;menu item, search for&nbsp; **Adafruit MCP4725** ,&nbsp;and select the&nbsp; **Adafruit MCP4725** library and click **Install** :

![](https://cdn-learn.adafruit.com/assets/assets/000/115/469/medium800/adafruit_products_libman.png?1664474067)

Next up, download the Adafruit MCP4725 library. This library does all of the interfacing, so you can just "set and forget" the DAC&nbsp;output. It also has some examples to get you started

[The library is available on GitHub](https://github.com/adafruit/Adafruit_MCP4725). You can download it by clicking the button below.

[Download Adafruit_MCP4725 Library](https://github.com/adafruit/Adafruit_MCP4725/archive/master.zip)
## Triangle Wave Example

Open up the **File→Examples→Adafruit\_MCP4725→trianglewave** sketch and upload it to the Arduino. Then connect your oscilloscope (or an LED + resistor if you don't have access to an oscilloscope)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/016/medium800/components_ID935trace_LRG.jpg?1396778266)

We also have a sine wave version showing how to use a lookup table to create a more complex waveform.

## Using the library
The library is very simple, so you can adapt it very quickly.  
  
First, be sure to call **begin(addr)** where **addr** is the i2c address (default is 0x62, if A0 is connected to VCC its 0x63). Then call **setVoltage(value, storeflag****) **to set the DAC output.** value **should range from 0 to 0x0FFF.** storeflag** indicates to the DAC whether it should store the value in EEPROM so that next time it starts, it'll have that same value output. You shouldn't set the flag to true unless you require it as it will take longer to do, and you could wear out the EEPROM if you write it over 20,000 times.  
  

# Increasing the speed
One thing thats a little annoying about the Arduino Wire library in this case is it is set for 100KHz transfer speed. In the MCP4725 library we update the speed to 400KHz by setting the TWBR  

> TWBR = 12; // 400 khz

You can speed this up a bit more, if you'd like, check the ATmega328 datasheet for how to calculate the **TWBR** register.  
- [Previous Page](https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial/wiring.md)
- [Next Page](https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial/python-circuitpython.md)

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
