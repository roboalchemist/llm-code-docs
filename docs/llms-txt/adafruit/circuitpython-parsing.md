# Source: https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-parsing.md

# Adafruit Ultimate GPS

## CircuitPython & Python Setup

You can easily use a GPS module with Python or CircuitPython code in addition to Arduino.&nbsp; Python code is well suited for parsing and processing the text output from GPS modules, and this [Adafruit CircuitPython GPS](https://github.com/adafruit/Adafruit_CircuitPython_GPS)&nbsp;module handles most of the work for you!

# CircuitPython MicroController Wiring
First make sure to wire up the GPS module to your CircuitPython board so that the hardware UART pins are used.&nbsp; Here's an example with the Metro M0 Express:

- **Board 5V** or **3.3V** to **GPS module VIN**.
- **Board GND** to **GPS module GND**.
- **Board serial TX** to **GPS module RX**.
- **Board serial RX** to **GPS module TX**.

![adafruit_products_m0_express_gps_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/076/818/medium640/adafruit_products_m0_express_gps_bb.png?1560221862)

# Python Computer Wiring
Since there's _dozens_ of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

Here you have two options: An external USB-to-serial converter, or the built-in UART on the Pi's TX/RX pins. Here's an example of wiring up the [USB-to-serial converter](https://www.adafruit.com/product/954):

- **GPS Vin** &nbsp; to **USB**  **5V** or **3V** (red wire on USB console cable)
- **GPS Ground** to **USB Ground** (black wire)
- **GPS RX** to **USB TX** (green wire)
- **GPS TX** to **USB RX** (white wire)

![adafruit_products_sensors_usbgps_bb_narrow.png](https://cdn-learn.adafruit.com/assets/assets/000/062/854/medium640/adafruit_products_sensors_usbgps_bb_narrow.png?1538431002)

Warning: 

You can also skip the USB console cable, and just plug a USB C or Micro B cable directly from your computer to the **Ultimate GPS USB**

![adafruit_products_UGPS_USB_C.jpg](https://cdn-learn.adafruit.com/assets/assets/000/109/804/medium640/adafruit_products_UGPS_USB_C.jpg?1647549840)

![adafruit_products_UGPS_USB_micro_B.jpg](https://cdn-learn.adafruit.com/assets/assets/000/109/805/medium640/adafruit_products_UGPS_USB_micro_B.jpg?1647549888)

Here's an example using the Pi's built-in UART:

- **GPS Vin** &nbsp; to **3.**** 3V** (red wire)
- **GPS Ground** to **Ground** (black wire)
- **GPS RX** to **TX** (green wire)
- **GPS TX** to **RX** (white wire)

![adafruit_products_sensors_uartgps_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/062/852/medium640/adafruit_products_sensors_uartgps_bb.png?1538430197)

If you want to use the built-in UART, you'll need to disable the serial console and enable the serial port hardware in **raspi-config**. See [the UART/Serial section of the CircuitPython on Raspberry Pi guide](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/uart-serial) for detailed instructions on how to do this.

# CircuitPython Installation of GPS Library
Next you'll&nbsp;need to install the&nbsp;[Adafruit CircuitPython GPS](https://github.com/adafruit/Adafruit_CircuitPython_GPS)&nbsp;library on your CircuitPython board.&nbsp;&nbsp; **Remember this module is for Adafruit CircuitPython firmware and not MicroPython.org firmware!**

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://github.com/adafruit/circuitpython/releases)&nbsp;for your board.

Next you'll need to install the necessary libraries to use the hardware. Carefully follow [the steps to find and install this library](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries) from [Adafruit's CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).

- **adafruit\_gps.mpy**

You can also download the&nbsp; **adafruit\_gps.mpy** &nbsp;file from the&nbsp;[Adafruit CircuitPython GPS releases page](https://github.com/adafruit/Adafruit_CircuitPython_GPS/releases).

Before continuing make sure your board's **lib** folder has the **adafruit\_gps.mpy** file copied over.

# Python Installation of GPS Library
You'll need to install the **Adafruit\_Blinka** library that provides the CircuitPython support in Python. This may require verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

```
sudo pip3 install adafruit-circuitpython-gps
```

- [Previous Page](https://learn.adafruit.com/adafruit-ultimate-gps/parsed-data-output.md)
- [Next Page](https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates

[Adafruit Ultimate GPS GNSS with USB - 99 channel w/10 Hz updates](https://www.adafruit.com/product/4279)
The Ultimate GPS module you know and love has a _glow-up_ to let it be easily used with any computer, not just microcontrollers! With the built-in USB-to-Serial converter, you can now plug-n-play the Ultimate GPS into your computer, laptop, embedded Linux computer, and more. Power and...

In Stock
[Buy Now](https://www.adafruit.com/product/4279)
[Related Guides to the Product](https://learn.adafruit.com/products/4279/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA

[GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA](https://www.adafruit.com/product/960)
Give your Ultimate GPS V3 a boost with this external active antenna. This GPS antenna draws about 10mA and will give you an additional 28 dB of gain. It's got a 5 meter long cable so it will easily reach wherever you need it to. The antenna is magnetic so it will stick to the top of a car...

In Stock
[Buy Now](https://www.adafruit.com/product/960)
[Related Guides to the Product](https://learn.adafruit.com/products/960/guides)
### SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable

[SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable](https://www.adafruit.com/product/851)
This RF adapter cable is super handy for anyone doing RF work. Often times, small electronics save space by having a pick-and-placeable u.FL connector (also called uFL, IPEX, IPAX, IPX, MHF, and AM). But most antennas have SMA or RP-SMA connectors on them. This little cable will bridge the...

In Stock
[Buy Now](https://www.adafruit.com/product/851)
[Related Guides to the Product](https://learn.adafruit.com/products/851/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

In Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [2.8" TFT Touch Shield](https://learn.adafruit.com/2-8-tft-touch-shield.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [CircuitPython Libraries on Linux and the 96Boards DragonBoard 410c](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-96boards-dragonboard-410c.md)
- [Arduino Lesson 3. RGB LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-3-rgb-leds.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [Let’s Put LEDs in Things!](https://learn.adafruit.com/lets-put-leds-in-things.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [CircuitPython Libraries on Linux and the NVIDIA Jetson Nano](https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano.md)
- [Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [IR Sensor](https://learn.adafruit.com/ir-sensor.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Adafruit Proto Screw Shield](https://learn.adafruit.com/adafruit-proto-screw-shield.md)
