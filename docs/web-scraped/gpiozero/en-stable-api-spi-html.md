# Source: https://gpiozero.readthedocs.io/en/stable/api_spi.html

Title: SPI Devices — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_spi.html

Markdown Content:
16. API - SPI Devices[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#module-gpiozero.spi_devices "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

SPI stands for [Serial Peripheral Interface](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) and is a mechanism allowing compatible devices to communicate with the Pi. SPI is a four-wire protocol meaning it usually requires four pins to operate:

*   A “clock” pin which provides timing information.

*   A “MOSI” pin (Master Out, Slave In) which the Pi uses to send information to the device.

*   A “MISO” pin (Master In, Slave Out) which the Pi uses to receive information from the device.

*   A “select” pin which the Pi uses to indicate which device it’s talking to. This last pin is necessary because multiple devices can share the clock, MOSI, and MISO pins, but only one device can be connected to each select pin.

The gpiozero library provides two SPI implementations:

*   A software based implementation. This is always available, can use any four GPIO pins for SPI communication, but is rather slow and won’t work with all devices.

*   A hardware based implementation. This is only available when the SPI kernel module is loaded, and the Python spidev library is available. It can only use specific pins for SPI communication (GPIO11=clock, GPIO10=MOSI, GPIO9=MISO, while GPIO8 is select for device 0 and GPIO7 is select for device 1). However, it is extremely fast and works with all devices.

16.1. SPI keyword args[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#spi-keyword-args "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

When constructing an SPI device there are two schemes for specifying which pins it is connected to:

*   You can specify _port_ and _device_ keyword arguments. The _port_ parameter must be 0 (there is only one user-accessible hardware SPI interface on the Pi using GPIO11 as the clock pin, GPIO10 as the MOSI pin, and GPIO9 as the MISO pin), while the _device_ parameter must be 0 or 1. If _device_ is 0, the select pin will be GPIO8. If _device_ is 1, the select pin will be GPIO7.

*   Alternatively you can specify _clock\_pin_, _mosi\_pin_, _miso\_pin_, and _select\_pin_ keyword arguments. In this case the pins can be any 4 GPIO pins (remember that SPI devices can share clock, MOSI, and MISO pins, but not select pins - the gpiozero library will enforce this restriction).

You cannot mix these two schemes, i.e. attempting to specify _port_ and _clock\_pin_ will result in [`SPIBadArgs`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.SPIBadArgs "gpiozero.SPIBadArgs") being raised. However, you can omit any arguments from either scheme. The defaults are:

*   _port_ and _device_ both default to 0.

*   _clock\_pin_ defaults to 11, _mosi\_pin_ defaults to 10, _miso\_pin_ defaults to 9, and _select\_pin_ defaults to 8.

*   As with other GPIO based devices you can optionally specify a _pin\_factory_ argument overriding the default pin factory (see [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information).

Hence the following constructors are all equivalent:

from gpiozero import MCP3008

MCP3008(channel=0)
MCP3008(channel=0, device=0)
MCP3008(channel=0, port=0, device=0)
MCP3008(channel=0, select_pin=8)
MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)

Note that the defaults describe equivalent sets of pins and that these pins are compatible with the hardware implementation. Regardless of which scheme you use, gpiozero will attempt to use the hardware implementation if it is available and if the selected pins are compatible, falling back to the software implementation if not.

16.2. Analog to Digital Converters (ADC)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#analog-to-digital-converters-adc "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The following classes are intended for general use with the integrated circuits they are named after. All classes in this section are concrete (not abstract).

### 16.2.1. MCP3001[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3001 "Link to this heading")

_class_ gpiozero.MCP3001(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3001)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3001 "Link to this definition")
The [MCP3001](http://www.farnell.com/datasheets/630400.pdf) is a 10-bit analog to digital converter with 1 channel. Please note that the MCP3001 always operates in differential mode, measuring the value of IN+ relative to IN-.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3001.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.2. MCP3002[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3002 "Link to this heading")

_class_ gpiozero.MCP3002(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3002)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3002 "Link to this definition")
The [MCP3002](http://www.farnell.com/datasheets/1599363.pdf) is a 10-bit analog to digital converter with 2 channels (0-1).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3002.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3002.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3002.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.3. MCP3004[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3004 "Link to this heading")

_class_ gpiozero.MCP3004(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3004)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004 "Link to this definition")
The [MCP3004](http://www.farnell.com/datasheets/808965.pdf) is a 10-bit analog to digital converter with 4 channels (0-3).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.4. MCP3008[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3008 "Link to this heading")

_class_ gpiozero.MCP3008(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3008)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "Link to this definition")
The [MCP3008](http://www.farnell.com/datasheets/808965.pdf) is a 10-bit analog to digital converter with 8 channels (0-7).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.5. MCP3201[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3201 "Link to this heading")

_class_ gpiozero.MCP3201(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3201)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3201 "Link to this definition")
The [MCP3201](http://www.farnell.com/datasheets/1669366.pdf) is a 12-bit analog to digital converter with 1 channel. Please note that the MCP3201 always operates in differential mode, measuring the value of IN+ relative to IN-.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3201.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.6. MCP3202[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3202 "Link to this heading")

_class_ gpiozero.MCP3202(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3202)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3202 "Link to this definition")
The [MCP3202](http://www.farnell.com/datasheets/1669376.pdf) is a 12-bit analog to digital converter with 2 channels (0-1).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3202.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3202.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3202.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.7. MCP3204[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3204 "Link to this heading")

_class_ gpiozero.MCP3204(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3204)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3204 "Link to this definition")
The [MCP3204](http://www.farnell.com/datasheets/808967.pdf) is a 12-bit analog to digital converter with 4 channels (0-3).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3204.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3204.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3204.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.8. MCP3208[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3208 "Link to this heading")

_class_ gpiozero.MCP3208(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3208)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3208 "Link to this definition")
The [MCP3208](http://www.farnell.com/datasheets/808967.pdf) is a 12-bit analog to digital converter with 8 channels (0-7).

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3208.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3208.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3208.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

### 16.2.9. MCP3301[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3301 "Link to this heading")

_class_ gpiozero.MCP3301(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3301)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3301 "Link to this definition")
The [MCP3301](http://www.farnell.com/datasheets/1669397.pdf) is a signed 13-bit analog to digital converter. Please note that the MCP3301 always operates in differential mode measuring the difference between IN+ and IN-. Its output value is scaled from -1 to +1.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3301.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for devices operating in differential mode).

### 16.2.10. MCP3302[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3302 "Link to this heading")

_class_ gpiozero.MCP3302(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3302)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3302 "Link to this definition")
The [MCP3302](http://www.farnell.com/datasheets/1486116.pdf) is a 12/13-bit analog to digital converter with 4 channels (0-3). When operated in differential mode, the device outputs a signed 13-bit value which is scaled from -1 to +1. When operated in single-ended mode (the default), the device outputs an unsigned 12-bit value scaled from 0 to 1.

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3302.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3302.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3304`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304 "gpiozero.MCP3304") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3302.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for devices operating in differential mode).

### 16.2.11. MCP3304[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#mcp3304 "Link to this heading")

_class_ gpiozero.MCP3304(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#MCP3304)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304 "Link to this definition")
The [MCP3304](http://www.farnell.com/datasheets/1486116.pdf) is a 12/13-bit analog to digital converter with 8 channels (0-7). When operated in differential mode, the device outputs a signed 13-bit value which is scaled from -1 to +1. When operated in single-ended mode (the default), the device outputs an unsigned 12-bit value scaled from 0 to 1.

_property_ channel[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304.channel "Link to this definition")
The channel to read data from. The MCP3008/3208/3304 have 8 channels (0-7), while the MCP3004/3204/3302 have 4 channels (0-3), the MCP3002/3202 have 2 channels (0-1), and the MCP3001/3201/3301 only have 1 channel.

_property_ differential[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304.differential "Link to this definition")
If `True`, the device is operated in differential mode. In this mode one channel (specified by the channel attribute) is read relative to the value of a second channel (implied by the chip’s design).

Please refer to the device data-sheet to determine which channel is used as the relative base value (for example, when using an [`MCP3304`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304 "gpiozero.MCP3304") in differential mode, channel 0 is read relative to channel 1).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3304.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for devices operating in differential mode).

16.3. Base Classes[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#base-classes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

The classes in the sections above are derived from a series of base classes, some of which are effectively abstract. The classes form the (partial) hierarchy displayed in the graph below (abstract classes are shaded lighter than concrete classes):

![Image 1: _images/spi_device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/spi_device_hierarchy.svg)
The following sections document these base classes for advanced users that wish to construct classes for their own devices.

### 16.3.1. AnalogInputDevice[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#analoginputdevice "Link to this heading")

_class_ gpiozero.AnalogInputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#AnalogInputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice "Link to this definition")
Represents an analog input device connected to SPI (serial interface).

Typical analog input devices are [analog to digital converters](https://en.wikipedia.org/wiki/Analog-to-digital_converter) (ADCs). Several classes are provided for specific ADC chips, including [`MCP3004`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3004 "gpiozero.MCP3004"), [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008"), [`MCP3204`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3204 "gpiozero.MCP3204"), and [`MCP3208`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3208 "gpiozero.MCP3208").

The following code demonstrates reading the first channel of an MCP3008 chip attached to the Pi’s SPI pins:

from gpiozero import MCP3008

pot = MCP3008(0)
print(pot.value)

The [`value`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.value "gpiozero.AnalogInputDevice.value") attribute is normalized such that its value is always between 0.0 and 1.0 (or in special cases, such as differential sampling, -1 to +1). Hence, you can use an analog input to control the brightness of a [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") like so:

from gpiozero import MCP3008, PWMLED

pot = MCP3008(0)
led = PWMLED(17)
led.source = pot

The [`voltage`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.voltage "gpiozero.AnalogInputDevice.voltage") attribute reports values between 0.0 and _max\_voltage_ (which defaults to 3.3, the logic level of the GPIO pins).

_property_ bits[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.bits "Link to this definition")
The bit-resolution of the device/channel.

_property_ max_voltage[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.max_voltage "Link to this definition")
The voltage required to set the device’s value to 1.

_property_ raw_value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.raw_value "Link to this definition")
The raw value as read from the device.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.value "Link to this definition")
The current value read from the device, scaled to a value between 0 and 1 (or -1 to +1 for certain devices operating in differential mode).

_property_ voltage[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.AnalogInputDevice.voltage "Link to this definition")
The current voltage read from the device. This will be a value between 0 and the _max\_voltage_ parameter specified in the constructor.

### 16.3.2. SPIDevice[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#spidevice "Link to this heading")

_class_ gpiozero.SPIDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#SPIDevice)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.SPIDevice "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device"). Represents a device that communicates via the SPI protocol.

See [SPI keyword args](https://gpiozero.readthedocs.io/en/stable/api_spi.html#spi-args) for information on the keyword arguments that can be specified with the constructor.

close()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/spi_devices.html#SPIDevice.close)[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.SPIDevice.close "Link to this definition")
Shut down the device and release all associated resources (such as GPIO pins).

This method is idempotent (can be called on an already closed device without any side-effects). It is primarily intended for interactive use at the command line. It disables the device and releases its pin(s) for use by another device.

You can attempt to do this simply by deleting an object, but unless you’ve cleaned up all references to the object this may not work (even if you’ve cleaned up all references, there’s still no guarantee the garbage collector will actually delete the object at that point). By contrast, the close method provides a means of ensuring that the object is shut down.

For example, if you have a breadboard with a buzzer connected to pin 16, but then wish to attach an LED instead:

>>> from gpiozero import *
>>> bz = Buzzer(16)
>>> bz.on()
>>> bz.off()
>>> bz.close()
>>> led = LED(16)
>>> led.blink()

[`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") descendents can also be used as context managers using the [`with`](https://docs.python.org/3.9/reference/compound_stmts.html#with "(in Python v3.9)") statement. For example:

>>> from gpiozero import *
>>> with Buzzer(16) as bz:
...     bz.on()
...
>>> with LED(16) as led:
...     led.on()
...

_property_ closed[](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.SPIDevice.closed "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.SPIDevice.close "gpiozero.SPIDevice.close") method). Once a device is closed you can no longer use any other methods or properties to control or query the device.
