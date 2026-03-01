# Source: https://gpiozero.readthedocs.io/en/stable/api_info.html

Title: Pi Information — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_info.html

Markdown Content:
23. API - Pi Information[](https://gpiozero.readthedocs.io/en/stable/api_info.html#module-gpiozero.pins.data "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The GPIO Zero library also contains a database of information about the various revisions of the Raspberry Pi computer. This is used internally to raise warnings when non-physical pins are used, or to raise exceptions when pull-downs are requested on pins with physical pull-up resistors attached. The following functions and classes can be used to query this database:

23.1. pi_info[](https://gpiozero.readthedocs.io/en/stable/api_info.html#pi-info "Link to this heading")
--------------------------------------------------------------------------------------------------------

gpiozero.pi_info(_revision=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/pins/pi.html#pi_info)[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "Link to this definition")
Deprecated function for retrieving information about a _revision_ of the Raspberry Pi. If you wish to retrieve information about the board that your script is running on, please query the [`Factory.board_info`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory.board_info "gpiozero.Factory.board_info") property like so:

>>> from gpiozero import Device
>>> Device.ensure_pin_factory()
>>> Device.pin_factory.board_info
PiBoardInfo(revision='a02082', model='3B', pcb_revision='1.2',
released='2016Q1', soc='BCM2837', manufacturer='Sony', memory=1024,
storage='MicroSD', usb=4, usb3=0, ethernet=1, eth_speed=100, wifi=True,
bluetooth=True, csi=1, dsi=1, headers=..., board=...)

To obtain information for a specific Raspberry Pi board revision, use the `PiBoardInfo.from_revision()` constructor.

Parameters:
**revision** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The revision of the Pi to return information about. If this is omitted or [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then the library will attempt to determine the model of Pi it is running on and return information about that.

23.2. PiBoardInfo[](https://gpiozero.readthedocs.io/en/stable/api_info.html#piboardinfo "Link to this heading")
----------------------------------------------------------------------------------------------------------------

_class_ gpiozero.PiBoardInfo(_revision_, _model_, _pcb\_revision_, _released_, _soc_, _manufacturer_, _memory_, _storage_, _usb_, _usb3_, _ethernet_, _eth\_speed_, _wifi_, _bluetooth_, _csi_, _dsi_, _headers_, _board_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/pins/pi.html#PiBoardInfo)[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PiBoardInfo "Link to this definition")
23.4. PinInfo[](https://gpiozero.readthedocs.io/en/stable/api_info.html#pininfo "Link to this heading")
--------------------------------------------------------------------------------------------------------

_class_ gpiozero.PinInfo(_number_, _name_, _names_, _pull_, _row_, _col_, _interfaces_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/pins.html#PinInfo)[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo "Link to this definition")
This class is a [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") derivative used to represent information about a pin present on a GPIO header. The following attributes are defined:

number[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.number "Link to this definition")
An integer containing the physical pin number on the header (starting from 1 in accordance with convention).

name[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.name "Link to this definition")
A string describing the function of the pin. Some common examples include “GND” (for pins connecting to ground), “3V3” (for pins which output 3.3 volts), “GPIO9” (for GPIO9 in the board’s numbering scheme), etc.

names[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.names "Link to this definition")
A set of all the names that can be used to identify this pin with `BoardInfo.find_pin()`. The [`name`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.name "gpiozero.PinInfo.name") attribute is the “typical” name for this pin, and will be one of the values in this set.

When “gpio” is in [`interfaces`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.interfaces "gpiozero.PinInfo.interfaces"), these names can be used with [`Factory.pin()`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory.pin "gpiozero.Factory.pin") to construct a [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") instance representing this pin.

pull[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.pull "Link to this definition")
A string indicating the fixed pull of the pin, if any. This is a blank string if the pin has no fixed pull, but may be “up” in the case of pins typically used for I2C such as GPIO2 and GPIO3 on a Raspberry Pi.

row[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.row "Link to this definition")
An integer indicating on which row the pin is physically located in the header (1-based)

col[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.col "Link to this definition")
An integer indicating in which column the pin is physically located in the header (1-based)

interfaces[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.interfaces "Link to this definition")
A [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)") mapping interfaces that this pin can be a part of to the description of that pin in that interface (e.g. “i2c” might map to “I2C0 SDA”). Typical keys are “gpio”, “spi”, “i2c”, “uart”, “pwm”, “smi”, and “dpi”.

pull_up[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.pull_up "Link to this definition")
Deprecated variant of [`pull`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.pull "gpiozero.PinInfo.pull").

function[](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.function "Link to this definition")
Deprecated alias of [`name`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PinInfo.name "gpiozero.PinInfo.name").
