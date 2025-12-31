# Source: https://learn.sparkfun.com/tutorials/gps-mouse---gp-808g-hookup-guide

## Introduction

The [GPS Mouse](https://www.sparkfun.com/products/14198) is a combination GPS and compass in a self contained module perfect for UAV and autonomous vehicle enthusiasts. The GP-808G housed inside is a highly sensitive GPS module that can accurately provide position, velocity, and time readings. This module is highly accurate, easy to use, requires almost no set-up time, and is very easy to embed into your projects!

[![GPS Mouse - GP-808G (72 Channel)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/1/3/7/14198-01.jpg)](https://www.sparkfun.com/products/14198)

### [GPS Mouse - GP-808G (72 Channel)](https://www.sparkfun.com/products/14198) 

[ GPS-14198 ]

The GPS Mouse is a self contained module perfect for UAV and autonomous vehicle enthusiasts.

**Retired**

This 72-channel GPS receiver, that supports a standard NMEA-0183 and uBlox 8 protocol, has low power consumption of **40mA @ 3.3V-5.0V**, GPS/QZSS/GLONASS support, and -167dBm tracking sensitivity. The GP-808G has been terminated with two JST connectors (one 4-pin and one 2-pin) and includes their mating counterparts. The GPS Mouse has been a popular go-to GPS option for many of the entrants in our annual [Autonomous Vehicle Competition](https://avc.sparkfun.com/) (AVC) with great results!

### Required Materials

To follow along with this guide all you need is an Arduino compatible microcontroller, such as an Arduino Uno or SparkFun Redboard, a breadboard, and some jumper wires. This example uses a SparkFun RedBoard.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

### Suggested Reading

If you have never worked with GPS before, have a look at our [GPS Basics](https://learn.sparkfun.com/tutorials/gps-basics) tutorial.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

December 14, 2012

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

## Hardware Overview

Let\'s go over the GPS Mouse in detail.

Inside the enclosure, you\'ll find a normal looking GPS module with a few extra bits. On the underside, you\'ll find a backup battery for warm and hot starts as well as the onboard QMC-5883 Magnetometer.

[![GPS Mouse insides](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/1/GPS_Mouse3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS_Mouse3.jpg)

The pin out for the GPS connectors are as follows:

[![GPS_Mouse_Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS_Mouse_Pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS_Mouse_Pinout.png)

*GPS pin diagram via the [GP-808G datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPM-808G--UAV_GNSS_receiver_ublox8030_QMC5883.pdf).*

The I^2^C lines are for factory programming of the module. No register data is available in the device\'s datasheet. All communication with the device in this guide occurs over serial.

## Hardware Hookup

This GPS module is designed for pro makers who wish to have a GPS module attach to their custom PCB or hand-built prototype. However, you can easily connect the GPS unit to a breadboard with the included connectors and wire it up to a microcontroller of your choice. For a secure connection, you can also solder the wires to a custom PCB.

To connect the module to a breadboard, insert the 4-pin and 2-pin female JST connectors.

[![GPS Mouse Hookup 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/1/GPS_Mouse1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS_Mouse1.jpg)

Connect the GPS male JST connectors into the female connectors. You can now wire the GPS Mouse to the microcontroller using jumper wires.

[![GPS Mouse and RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/1/GPS_Mouse2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS_Mouse2.jpg)

For a more robust connection, you can also snip the JST connectors off and solder the bare wire ends to [straight male headers](https://www.sparkfun.com/products/116) or any other connector of your choosing.

The connections from the GPS Mouse to the SparkFun RedBoard used for this example are as follows:

  GPS Mouse Pin   SparkFun RedBoard Pin
  --------------- -----------------------
  TX (White)      Digital Pin 4
  RX (Green)      Digital Pin 3
  GND (Black)     Ground (GND)
  VCC (Red)       Power (5V)

## Arduino Example

Now that we have everything connected, lets get started with some code. Before we start writing code though, we do need to install a library to parse the GPS messages. If you haven\'t downloaded Arduino libraries before or you just need a quick refresh, check out our tutorial on [installing Arduino libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). The library we need is called [TinyGPSPlus](http://arduiniana.org/libraries/tinygpsplus/) from Mikal Hart. You can download and install the library from the link below.

[TinyGPS++ Library](https://github.com/mikalhart/TinyGPSPlus)

Now that we have the library installed, let\'s look at the code. In Arduino, open the example sketch by clicking **File -\> Examples -\> TinyGPSPlus-version -\> DeviceExample**.

In the example, you will need to change one line of code. Change the variable `GPSBaud` to 9600 with the following line:

    language:c
    static const uint32_t GPSBaud = 9600;

The rest of the example sketch should work as is. Upload the sketch to your Arduino board. Once uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) set to 115200 baud. You should see GPS serial data streaming by. If the location says INVALID, wait several minutes for the GPS unit to get a lock. If you do not see GPS data after several minutes, see the troubleshooting section below.

[![GPS data out](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS-data.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/1/GPS-data.png)

**Note:** While the GPS uses 9600 baud on the software serial pins, the serial UART for the serial monitor is set to 115200 baud.

### Troubleshooting Tips

- If you\'re testing your GPS inside, make sure you\'re next to a window. One of the problems with GPS is that radio waves have a difficult time passing through roofs and ceilings. So the closer the GPS is to being outside, the better. If you still aren\'t reading from enough satellites to get a position fix, try pointing the GPS antenna in a different direction.

- If you see this message print to the Serial Monitor: `No GPS detected: check wiring.` do just that. Check your wiring and make sure that you have the correct pins connected to the GPS connector.

- If you place the GPS mouse in a dark room, you will be able to see the onboard GPS LEDs blinking inside the enclosure. If you see a green LED, that means the GPS unit is getting power. If you see a blinking blue LED, the GPS unit has a lock. If you see the blinking blue LED and aren\'t getting any serial data printed to the Serial Terminal, check your wiring and check that you have the correct pins defined at the top of your code.