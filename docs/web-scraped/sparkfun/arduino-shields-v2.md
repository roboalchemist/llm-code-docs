# Source: https://learn.sparkfun.com/tutorials/arduino-shields-v2

## Introduction

**Update:** This is an updated version of our original Arduino Shields tutorial to expand and update on it as many of the shields highlighted in the original tutorial are no longer carried by SparkFun. If you are looking for the original tutorial it can be found here: [Arduino Shields](https://learn.sparkfun.com/tutorials/arduino-shields)

### What is a Shield?

Shields^[\[1\]](https://learn.sparkfun.com/tutorials/arduino-shields#footnote1)^ are modular circuit boards that piggyback onto your Arduino to instill it with extra functionality. Want to connect your Arduino to the Internet and post to Twitter? There\'s a shield for that. Want to make your Arduino an autonomous rover? There are shields for that. There are a LOT of shields out there, all of which can add all sorts of customizations to enhance your Arduino\'s functionality.

[![Instagram - Table Full of Shields](https://cdn.sparkfun.com/assets/3/3/0/9/3/52c5b2f9ce395fad7a8b4567.jpg)](https://cdn.sparkfun.com/assets/3/3/0/9/3/52c5b2f9ce395fad7a8b4567.jpg)

*A blast from the past! Former SparkFun catalog manager [RobertC.](https://www.sparkfun.com/users/93309) in awe of an extravagant platter of shields.*

Many Arduino shields are stackable. You can connect multiple shields together to create a stack of Arduino modules. You could, for example, combine a [SparkFun RedBoard](https://www.sparkfun.com/products/13975) with a [Weather Shield](https://www.sparkfun.com/products/13956) and a [WiFi Shield - ESP8266](https://www.sparkfun.com/products/13287) to create a wireless weather station similar to [this Weather Station project](https://learn.sparkfun.com/tutorials/weather-station-wirelessly-connected-to-wunderground).

Shields are often supplied with either an example sketch, or a [library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). So, not only do they just simply plug into your Arduino, but all you usually need to do to make them work is upload up some example code to the Arduino.

**[][\[1\]](#footnote1) Note:** In general, these are called \"daughter boards.\" The terminology and layout depends on the environment platform and form factor. Shields for Arduino typically use the Arduino Uno R3 footprint. However, shields can have a different layout depending on the architecture. Stackable PCBs for the Raspberry Pi are referred to as [HATs or pHATs](https://www.sparkfun.com/phats) while the BeagleBone refers to them as Capes. We\'ll focus on the Arduino shields with the R3 footprint throughout this tutorial.

## Shield Form Factor

Every Arduino shield must fit the same form factor as the Arduino it mates to.

In the past, this referred almost exclusively to the [Uno R3 (or RedBoard)](https://learn.sparkfun.com/tutorials/redboard-vs-uno) form factor but as more types of Arduinos and similar development boards have come out, the \"shield\" definition has become a bit more nebulous.

Shields designed to work on the Arduino Uno R3 form factor have power and ground pins on one eight (previously six) pin header, and analog pins on a six-pin header next to that. Digital pins cover the other edge on the opposite side, an eight-pin header separated from a 10-pin by that weird 0.5\" spacing. Some shields also require a connection to the Arduino\'s ICSP header (the 2x3 programming header on the end).

[![Shield Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/SparkFun-Arduino_Shield_Basics.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/SparkFun-Arduino_Shield_Basics.jpg)

### Pin Functionality

Some shields use nearly every available pin on the Arduino, while others only use a couple. Some shields communicate with the Arduino via [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi), [I^2^C](https://learn.sparkfun.com/tutorials/i2c), or [Serial](https://learn.sparkfun.com/tutorials/serial-communication). Other shields use the Arduino\'s [interrupts](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino), [analog inputs](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion), and [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation). When stacking shields it\'s important to make sure they don\'t use overlapping pins.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

Additionally, you will also want to ensure that shield pins are compatible with your development board. If a shield was designed with the ATmega328p in mind, the pin functionality may be in a different location. For example, the XBee shield was designed for the Arduino Uno R3 (an ATmega328P-based board). If you were to use the Arduino Leonardo (an ATmega32U4-based board) or the Arduino Mega 2560 (an ATmega2560-based board), you would need to reroute the connection and redefine the pin definitions. For more information, check out the [XBee Shield Hookup guide](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide#softwareserialpins).

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Pins Rerouted for Arduino Mega 2560 R3](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Mega_Fritzing_bb.png "Click to Enlarge Circuit")](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide#softwareserialpins)   [![Pins Rerouted for Arduino Leonardo w/ ATmega32U4](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Leonardo_Fritzing_bb_2.png "Click to Enlarge  Circuit")](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide#softwareserialpins)
  *XBee Shield Pins Rerouted for ATmega2560-Based Arduino*                                                                                                                                                                                                                                                                  *XBee Shield Pins Rerouted for ATmega32U4-Based Arduino*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Logic Levels

Also note that there are several Arduino development boards available now that fit the R3 form factor but run at a different [logic level](https://learn.sparkfun.com/tutorials/logic-levels) than the standard Uno/RedBoard. For example, the [Arduino Uno R3](https://www.sparkfun.com/products/11021) runs at **5V** logic where the [RedBoard Artemis](https://www.sparkfun.com/products/15444) runs at **3.3V**. Quite a few shields can function just fine with a board running at either logic level but you may run into some erratic behavior with level shifting circuits set up to work best with a **5V** system. Another potential issue you may run across with a **3.3V** logic Arduino is if the shield pulls any of the pins to a **5V** reference voltage through something like a pull up resistor.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

June 3, 2013

Learn the difference between 3.3V and 5V devices and logic levels.

------------------------------------------------------------------------

### Other Shield Form Factors

There is a great variety of Arduino shields out there \-- too many to ever include in this tutorial. While most adhere to the standard Arduino Uno R3 form factor, some shield designs can vary depending on the development board\'s footprint and environment. Some of these designs include the [Thing Plus](https://www.sparkfun.com/products/15663), [Pro Mini](https://www.sparkfun.com/products/11113), [Pro Micro](https://www.sparkfun.com/products/15795), [Arduino Nano](https://www.sparkfun.com/products/15590), [Arduino MKR](https://www.sparkfun.com/products/14870), and [Teensy](https://www.sparkfun.com/products/15583) footprints.

![](https://cdn.sparkfun.com//assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-02.jpg)

![](https://cdn.sparkfun.com//assets/parts/6/5/3/9/11113-02b.jpg)

![](https://cdn.sparkfun.com//assets/parts/1/4/4/0/4/15795-Pro_Micro_C-02.jpg)

![](https://cdn.sparkfun.com//assets/parts/1/4/1/9/6/15590-Arduino_Nano_Every-02.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/7/14870-Arduino_MKR_Vidor_4000-02_rotated.jpg)

![](https://cdn.sparkfun.com//assets/parts/1/4/1/8/9/15583-Teensy_4.0-02.jpg)

[[]](#carousel-6954f59d5660c) [[]](#carousel-6954f59d5660c)

1.  ::: 
    :::

2.  ::: 
    :::

3.  ::: 
    :::

4.  ::: 
    :::

5.  ::: 
    :::

6.  ::: 
    :::

In the next section, we\'ll go over a handful of the more popular and unique shields designed for the R3 form factor that SparkFun carries.

## A Plethora of Shields

The list below describes some of the R3 form factor shields SparkFun carries separated into some loose categories based on their unique functionality. This is not an exhaustive list of *all* Arduino shields but it will cover most of what SparkFun has to offer. If you want to browse all the shields SparkFun carries, check out the [Arduino Shields Category](https://www.sparkfun.com/categories/240).

[Click to Browse Arduino Shields!](https://www.sparkfun.com/categories/240)

### Prototyping & More

Prototyping shields usually do not augment the functionality of the Arduino like other shields but they help in other ways. Prototyping shields do things like breaking out various pins to screw terminals or create a space to build and test a circuit on the shield.

- [ProtoShield Kit](https://www.sparkfun.com/products/13820) - The self-titled star of this category. The ProtoShield includes a large prototyping area in the center. Half of this area has solder jumper pads on the bottom you can close to make it function more like a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) while the other half functions as a standard prototyping/perfboard area. There is quite a lot going on in this shield so for a full rundown on everything included in the ProtoShield Kit and how to use it, check out the [ProtoShield Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide)!

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Female_Headers_Mini_Breadboard.jpg "Customized with Mini-Breadboard and Headers")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Female_Headers_Mini_Breadboard.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Wires_Female_Header_Wires_Mini_Breadboard.jpg "Customized with Mini-Breadboard, Headers, and Hookup Wire")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Wires_Female_Header_Wires_Mini_Breadboard.jpg)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- [ProtoScrew Shield](https://www.sparkfun.com/products/9729) - Like the ProtoShield, but each pin is also broken out to a screw terminal. Handy for connecting to external motors, heavy-duty sensors or creating a strong connection to each pin that is not as permanent as a solder connection.
- [Qwiic Shield](https://www.sparkfun.com/products/14352) - The perfect way to integrate your Arduino with SparkFun\'s [Qwiic System](https://www.sparkfun.com/qwiic)! This shield has four Qwiic connectors on it along with a level-shifting circuit to easily connect to and communicate with Qwiic I^2^C breakouts. The shield also has a large prototyping area that includes a few neat features to help with prototyping. Take a look at the [Qwiic Shield Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide) to get started with this shield and the Qwiic system.

[![The Qwiic Shield in action with several Qwiic breakouts attached](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/4/qwiic_action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/4/qwiic_action.jpg)

- [Joystick Shield Kit](https://www.sparkfun.com/products/9760) - This makes your Arduino a bare-bones controller. With a joystick and four buttons added to it, this shield works great for a simple robot controller.
- [microSD Shield](https://www.sparkfun.com/products/9802) - A lot of Arduinos have limited storage space, but this easy-to-use shield (along with the [SD library](http://arduino.cc/en/Reference/SD)) allows for plenty of extra storage for things like data logging.
- [Mux Shield II](https://www.sparkfun.com/products/11723) - This shield from Mayhew Labs is a great way to add up to 48 analog and digital inputs or digital outputs to an Arduino using the R3 layout. Mayhew Labs also has an Arduino Library with built-in examples to help you get started. That, along with information on how to use the Mux Shield II can be found in their [user guide](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Shields/Mux_Shield_II_User_Guide.pdf).

### IoT and Wireless Technology Shields

These shields add different types of wireless technologies to your Arduino. They range from connecting to the Internet for your next IoT Arduino project to receiving and logging the GPS coordinates of your Arduino-based robot and much more!

- [WiFi Shield (ESP8266)](https://www.sparkfun.com/products/13287) - This shield uses Espressif\'s ESP8266 SoC to add WiFi connectivity to an Arduino using the R3 layout. The shield comes with pre-flashed AT-command firmware so it works as a serially-controlled WiFi gateway out of the box but it also breaks out the I/O pins of the ESP8266 so you can access those as well and even re-program the ESP8266 with your own custom firmware. To get started with the WiFi Shield (ESP8266) take a look through our [Hookup Guide](https://learn.sparkfun.com/tutorials/esp8266-wifi-shield-hookup-guide).

[![SparkFun WiFi Shield mounted on a RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/3/angled-action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/3/angled-action.jpg)

- [Arduino Ethernet Shield 2](https://www.sparkfun.com/products/11166) - Looking to access the Internet but would prefer a hard-wired option? The Ethernet Shield is for you! Getting started with the Ethernet Shield 2 is easy using the Arduino [Ethernet Library](https://www.arduino.cc/en/Reference/Ethernet). The shield also includes an on-board microSD slot to store larger files to send over your network.
- [LTE CAT M1/NB-IoT Shield (SARA-R4)](https://www.sparkfun.com/products/14997) - This shield adds wireless, high-bandwidth cellular functionality to your IoT project. We\'ve written an [Arduino Library](https://github.com/sparkfun/SparkFun_LTE_Shield_Arduino_Library) with some examples to get you started sending SMS messages or communicating with servers over a TCP/IP connection. All you need to get started is a compatible SIM card or you can get the version of this shield that includes a Hologram SIM card [here](https://www.sparkfun.com/products/15087). Check out the [Hookup Guide](https://learn.sparkfun.com/tutorials/lte-cat-m1nb-iot-shield-hookup-guide) for detailed information on how to get started with this shield.
- [XBee Shield](https://www.sparkfun.com/products/12847) - XBee\'s are great RF modules that work on multiple wireless protocols (802.15.4, Digi\'s Zigbee specification and BLE). Simply pair an XBee radio on the shield with another XBee and you\'re well on your way to creating a [robot controlled by gestures](https://learn.sparkfun.com/tutorials/wireless-gesture-controlled-robot)!
- [GPS Logger Shield](https://www.sparkfun.com/products/13750) - With this shield you can log the position, speed and altitude of your Arduino using the on-board GP3906-TLP GPS Module. Take a look at the [Hookup Guide](https://learn.sparkfun.com/tutorials/gps-logger-shield-hookup-guide) to start logging.

### Music and Sound

- [MP3 Player Shield](https://www.sparkfun.com/products/12660) - Turn your Arduino into an MP3 player. Just plug in a µSD card with some MP3 files on it, add some speakers, upload the example code, and you can make your very own [MP3 Playing Music Box](https://learn.sparkfun.com/tutorials/mp3-player-shield-music-box)!

[![Music Box Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/3/8/5/a/2/5150bf06ce395f4578000000.png)](https://cdn.sparkfun.com/assets/3/8/5/a/2/5150bf06ce395f4578000000.png)

- [MIDI Shield](https://www.sparkfun.com/products/10587) - Assemble this shield to give your Arduino access to the [MIDI communication protocol](https://en.wikipedia.org/wiki/MIDI). Along with MIDI-In and OUT ports, the shield also includes two potentiometers to control things like pitch, volume or tone. For assembly instructions and examples using the MIDI Shield, check out the [Hookup Guide](https://learn.sparkfun.com/tutorials/midi-shield-hookup-guide)!
- [Spectrum Shield](https://www.sparkfun.com/products/13116) - This takes an stereo audio input to the shield and splits it into 7-bands per channel and reads the amplitude of each channel using the ADC on your Arduino. Use that data to control anything from LEDs, motors or even [fire](https://youtu.be/A1VySF2Rd4I)!
- [EasyVR 3 Plus Shield](https://www.sparkfun.com/products/15453) - This shield adds voice recognition technology to your Arduino using the EasyVR module so you can create your own voice controlled project. You can download the Arduino Library as well as learn how to get started with the EasyVR 3 in the [User Guide](https://cdn.sparkfun.com/assets/learn_tutorials/9/3/1/EasyVR-3-User-Manual-1.0.17.pdf).

### Motor Drivers

- [Ardumoto Shield Kit](https://www.sparkfun.com/products/14180) - With this kit you can use the Ardumoto shield to create a basic robot with the included DC motors.

[![Ardumoto Robot using a SparkFun box.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/0/Marshall-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/0/Marshall-10.jpg)

- [Monster Moto Shield](https://www.sparkfun.com/products/10182) - If you need to drive beefier motors than the Ardumoto Shield can handle, this is the next step up.
- [Wireless Motor Driver Shield](https://www.sparkfun.com/products/14285) - Looking for something more versatile than the two shields above? The Wireless Motor Driver Shield can control two DC motors and also breaks out pins to power and control several servos and even has an XBee socket to easily add wireless control to your motor project! This shield has a lot going on so take a look through the [Hookup Guide](https://learn.sparkfun.com/tutorials/wireless-motor-driver-shield-hookup-guide) to get started.

### Miscellaneous Shields

These shields do not really fit into any of the above categories but we\'d still like to highlight them in this list as they add some neat, unique functionality to your Arduino.

- [CAN-Bus Shield](https://www.sparkfun.com/products/13262) - This allows your Arduino to talk to your car or other CAN application. It also has a µSD slot to log data and has connectors for a GPS connection and LCD to log and report data. Check out the [Hookup Guide](https://learn.sparkfun.com/tutorials/can-bus-shield-hookup-guide) for more info and example code to get started.
- [Vernier Interface Shield](https://www.sparkfun.com/products/12858) - This shield has four British Telecom connectors (2 Analog and 2 Digital) to interface with all sorts of [Vernier sensors](https://learn.sparkfun.com/tutorials/vernier-shield-hookup-guide#about-vernier).
- [Simultaneous RFID Reader](https://www.sparkfun.com/products/14066) - Add some item tracking to your Arduino using Radio Frequency Identification (RFID). The M6E Nano module on this board reads and writes to EPCglobal Gen 2 UHF RFID tags and can read multiple tags at the same time. Our [RFID Arduino Library](https://learn.sparkfun.com/tutorials/simultaneous-rfid-tag-reader-hookup-guide/using-the-arduino-library) has a bunch of examples to get your next RFID project started.
- [Weather Shield](https://www.sparkfun.com/products/13956) - Want to create your own [weather station](https://learn.sparkfun.com/tutorials/arduino-weather-shield-hookup-guide-v12#example-firmware---weather-station)? The Weather Shield is a great place to start. The shield has sensors to monitor temperature, humidity, barometric pressure and luminosity as well as ports to connect a GPS module along with [weather meters](https://www.sparkfun.com/products/15901) to monitor wind speed, direction and rainfall!
- [EL Escudo Dos](https://www.sparkfun.com/products/10878) - Electroluminescent wire is awesome! Use this shield to add up to eight strands of EL wire to your project. Check out these [EL Wire Tutorials](https://learn.sparkfun.com/tutorials/tags/el-wire) for some inspiration for your own EL project.
- [Cthulhu Shield](https://www.sparkfun.com/products/15897) - One of the most unique and nifty shields SparkFun carries. The Cthulhu Shield can output to and take input from an electrode array placed on your tongue! For some neat experiment ideas pairing this shield with some sensors, take a look at [this blog post](https://www.sparkfun.com/news/3244) and get started with some sensory substitution and augmentation.

[![Using the GridEYE IR sensor for some IR target practice.](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/4/Cthulhu_Shield_IR_sensor_Eagle_Eye.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/2/4/4/Cthulhu_Shield_IR_sensor_Eagle_Eye.gif)

*Pair the Cthulhu Shield with a [Grid-EYE IR Array Breakout](https://www.sparkfun.com/products/14607) for some IR target practice!*

## Installing Headers (Preparation)

Many shields come without any headers attached. This keeps their final fate open to your interpretation (maybe you\'d rather use straight male headers, instead of the usual stackable headers). The following pages will explain how you can turn your drab, header-less shield into a fully functional, ready-to-plug-in module.

[![Shield before and after headers](https://cdn.sparkfun.com/r/600-600/assets/e/e/c/7/0/51ddd727ce395f9064000001.png)](https://cdn.sparkfun.com/assets/e/e/c/7/0/51ddd727ce395f9064000001.png)

Shield assembly requires soldering. Solder helps make a good physical and electrical connection. Without solder, your shield and Arduino will almost certainly not work properly. If it manages to work at all it will be erratic and intermittent at best. If this is your first time soldering, consider checking out our [How to Solder: Through-Hole Soldering Tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) prior to assembling your shield:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

### Required Materials

With your shield (or shields) chosen, the only other required materials are a compatible Arduino development board and some headers. The SparkFun RedBoard and Arduino Uno R3 are great options that will work with nearly any Arduino shield with no issues:

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/600-600/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

And here are some recommended header options:

[![Arduino Stackable Header Kit - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/7/2/1/6/11417-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html)

### [Arduino Stackable Header Kit - R3](https://www.sparkfun.com/arduino-stackable-header-kit-r3.html) 

[ PRT-11417 ]

These headers are made to work with the Arduino Uno R3, Leonardo and new Arduino boards going forward. They are the perfect h...

[ [\$2.75] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Arduino Stackable Header Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/4/1/6/6/10007-01.jpg)](https://www.sparkfun.com/arduino-stackable-header-kit.html)

### [Arduino Stackable Header Kit](https://www.sparkfun.com/arduino-stackable-header-kit.html) 

[ PRT-10007 ]

These headers are made to work with the Arduino Main Board, Arduino Pro, and the Arduino Mega. They are the perfect height fo...

[ [\$2.50] ]

### Required Tools

You will also need at least a soldering iron and some solder to assemble your shield. Below are a few soldering iron and solder options along with a couple of kits that will have all the tools necessary to start soldering:

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Brass Sponge](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/6/8/08964-02-L.jpg)](https://www.sparkfun.com/brass-sponge.html)

### [Brass Sponge](https://www.sparkfun.com/brass-sponge.html) 

[ TOL-08964 ]

This is a brass sponge that will help clean your soldering iron tip. Use it to remove residue from your iron tip before solde...

[ [\$10.90] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

Along with these required tools, these accessories can help make your soldering experience a little easier:

[![SparkFun Third Hand Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/8/0/3/1/11784-05.jpg)](https://www.sparkfun.com/sparkfun-third-hand-kit.html)

### [SparkFun Third Hand Kit](https://www.sparkfun.com/sparkfun-third-hand-kit.html) 

[ TOL-11784 ]

Are you frustrated with the lack of dexterity from most third hands? The SparkFun Third Hand gives you the ability to hold a ...

[ [\$38.50] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

[![Solder Wick #2 Yellow - No Clean](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/5/09327-Chipquik-Feature.jpg)](https://www.sparkfun.com/solder-wick-2-5ft-generic.html)

### [Solder Wick #2 Yellow - No Clean](https://www.sparkfun.com/solder-wick-2-5ft-generic.html) 

[ TOL-09327 ]

Solder wick, coffee, and paper towels keep SparkFun running. You can steal someone\'s diagonal cutters for a minute, but you\'d...

[ [\$2.95] ]

[![Soldering Iron Stand](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/0/7/9477-BST-206-Soldering-Iron-Stand-Feature.jpg)](https://www.sparkfun.com/soldering-iron-stand.html)

### [Soldering Iron Stand](https://www.sparkfun.com/soldering-iron-stand.html) 

[ TOL-09477 ]

This is a simple soldering iron stand composed of a heavy-duty metal base and a reinforced spring holder. The base and holder...

[ [\$7.75] ]

### What Kind of Header Should You Use?

There are all kinds of headers, but there are only two that we recommend for installing on shields: stackable or male.

[![Header options - male or stackable](//cdn.sparkfun.com/assets/d/f/7/3/b/51193875ce395f424b000000.jpg)](//cdn.sparkfun.com/assets/d/f/7/3/b/51193875ce395f424b000000.jpg)

*A straight male header (left) and a stackable header (right).*

Stackable headers are especially great for stacking shields. They also maintain your ability to plug a jumper wire into any of the Arduino\'s pins. **This tutorial will primarily explain how to install stackable headers.** Stackable headers are available individually in [6-pin](https://www.sparkfun.com/products/9280), [8-pin](https://www.sparkfun.com/products/9279), and [10-pin](https://www.sparkfun.com/products/11376) varieties (there are other [stackable header options](https://www.sparkfun.com/categories/381) for development boards that use different footprints/form factors), or you can buy the headers in packs like the ones shown in the Required Materials section above.

[Click Here for More Header Options](https://www.sparkfun.com/categories/381)

Simple straight [male headers](https://www.sparkfun.com/products/116) are also an option for connecting a shield to an Arduino. Male headers are beneficial in that they create a **lower-profile stack** when connected to an Arduino. If you plan to stuff your Arduino/shield combo into an enclosure, you may need to consider using male headers. This tutorial focuses on stackable header installation, check the [Tips and Tricks](https://learn.sparkfun.com/tutorials/arduino-shields-v2#assembly-tricks) section for male header assembly instructions.

**Do not install** female headers, right-angle male headers, swiss machine-pinned headers, round headers, or a variety of other headers that may exist out there. You really should only use headers that have straight, rectangular, male pins.

------------------------------------------------------------------------

Now then, plug in and start warming up those soldering irons. It\'s time to get soldering!

## Installing Headers (Assembly)

### Step 1: Insert All Four Headers

Plug all four headers into the shield. Make sure you **insert them in the correct direction**. The male pins of the header should enter the top side of the shield and extend out the bottom. This orientation is of utmost importance. Don\'t solder anything until you\'ve got the headers going the right way!

[![Headers inserted, not yet soldered](https://cdn.sparkfun.com/r/600-600/assets/b/4/1/0/9/51dddfb8ce395f8e64000000.JPG)](https://cdn.sparkfun.com/assets/b/4/1/0/9/51dddfb8ce395f8e64000000.JPG)

*Headers inserted, aligned as well as possible, ready to solder.*

With the headers inserted, flip the shield on its top-side to rest on the black, female side of the headers. Hopefully you\'ve got a nice flat workspace to lay it on. Try to align all headers so they\'re **precisely perpendicular** to the shield PCB.

### Step 2: Solder **One** Pin On Each Header

Finally it\'s soldering time! It\'s important that each of the headers is at a nice, 90° angle to the PCB. This will ensure that the shield slides straight onto your Arduino and you won\'t have to bend any pins in doing so.

In order to guarantee that each header is straight **start by soldering just a single pin on each**. That way if they\'re at a weird angle it will be much easier to re-heat just a single pin while adjusting the alignment.

[![Soldering the first pins](//cdn.sparkfun.com/r/600-600/assets/6/f/8/5/e/51193957ce395fe84b000000.jpg)](//cdn.sparkfun.com/assets/6/f/8/5/e/51193957ce395fe84b000000.jpg)

*One pin down, one in progress, two to go. Soldering one pin on each header.*

Four solder joints down, only 24 (to 28) to go!

### Step 3: Check Header Alignment

With those four pins soldered, try plugging the shield partially into your Arduino to test the header\'s alignment. Make sure your Arduino is not powered while you do this alignment check.

[![Alignment check](//cdn.sparkfun.com/assets/d/f/7/f/2/51193a9ece395f3b4b000000.jpg)](//cdn.sparkfun.com/assets/d/f/7/f/2/51193a9ece395f3b4b000000.jpg)

*Temporarily plugging the shield in to check that all pins line up.*

Does everything line up? No pins bending? If not, find the guilty header and try to re-align it. Warm the joint back up with your iron, and slightly move and adjust the header alignment. Also, be careful when pulling the partially soldered shield out of the Arduino. Since all the headers are not soldered, you could easily bend them as you pull it out of the Arduino\'s female headers.

### Step 4: Solder All Remaining Pins

If your headers are all lined up, you can attack the remaining unsoldered header pins. When you\'re done, you should have 32 shiny volcanoes of solder.

[![Shield with all headers soldered](//cdn.sparkfun.com/assets/9/a/2/5/f/51193989ce395f5d4b000000.jpg)](//cdn.sparkfun.com/assets/9/a/2/5/f/51193989ce395f5d4b000000.jpg)

*That\'s a beautiful sight. Everything\'s soldered up.*

### Step 5: Check For Shorts or Cold Joints

With everything soldered, double check for bad solder joints. Did any of your joints stray into another creating a short? If so, you can take some [solder wick](https://www.sparkfun.com/products/9327) to the joint, or just try re-heating the short and \"pushing\" the solder where you want it.

[![Shorted solder joints](//cdn.sparkfun.com/r/600-600/assets/f/2/8/f/7/5115669cce395ff53c000002.jpg)](//cdn.sparkfun.com/assets/f/2/8/f/7/5115669cce395ff53c000002.jpg)

*Well, that\'s just egregious! Watch out for shorted solder joints like that.*

Also check for **cold solder joints** - a joint that\'s got some solder on it, but isn\'t quite connecting the two solder points together. Cold joints aren\'t always the easiest to see; look out for joints that aren\'t as shiny, or pins that still seem loose.

[![Cold solder joint](//cdn.sparkfun.com/r/600-600/assets/c/a/3/c/b/5115669cce395f973d000006.jpg)](//cdn.sparkfun.com/assets/c/a/3/c/b/5115669cce395f973d000006.jpg)

*That last pin could use a bit more solder. It doesn\'t quite look like a connection\'s been made.*

To fix a cold joint, re-heat the solder on the pin, and add just a bit more.

### Step 6: Plug It In!

It\'s usually best practice to power down (unplug) your Arduino before you connect a shield to it. Hopefully all of the pins are still well-aligned and the shield just slides right into the Arduino. Take care not to bend any pins while inserting, and make sure they all go into their mating female headers.

[![The Ardumoto Shield plugged into a SparkFun RedBoard.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/0/Marshall-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/0/Marshall-06.jpg)

*That satisfying feeling as the shield slides straight into your Arduino*

## Assembly Tricks

The previous assembly section should detail everything you need to know about simple shield header installation. There are, however, a few tricks we\'ve picked up along the way\...

### Use An Old Shield to Aid Alignment

The easiest place to mess up shield assembly is in aligning each of those headers. It\'s best to avoid soldering the stackable headers while the shield\'s connected to the Arduino, so the method described in the assembly section is usually best. If you\'ve got a spare shield lying around you can take advantage of another little trick by using it as a header-alignment-jig.

Begin by plugging all of the headers into your spare shield jig.

[![Stackable headers inserted into shield-jig](https://cdn.sparkfun.com/r/600-600/assets/1/0/7/3/3/51dde352ce395f0d65000000.png)](https://cdn.sparkfun.com/assets/1/0/7/3/3/51dde352ce395f0d65000000.png)

*The green shield will be used as our jig. First, insert the stackable headers into it.*

Then insert the headers into your to-be-soldered shield, and solder them all up. Assuming the spare shield is aligned properly (you may want to check that first), your headers will line up perfectly with your Arduino.

[![Shield to be soldered inserted into jig. Ready to solder.](https://cdn.sparkfun.com/r/600-600/assets/1/b/d/5/b/51dde3d9ce395f5665000002.JPG)](https://cdn.sparkfun.com/assets/1/b/d/5/b/51dde3d9ce395f5665000002.JPG)

*The jig should correctly align all of the headers. Solder away!*

### Installing Male Headers

If you value a smaller profile shield installation over the ability to stack shields and connect jumper wires, male headers are an option.

In a way, male headers are actually easier to align and install because you can use your Arduino as a jig. Begin by inserting the headers into your Arduino.

[![Redboard jigging male headers](https://cdn.sparkfun.com/r/600-600/assets/1/2/f/1/8/51dde46bce395f4965000000.JPG)](https://cdn.sparkfun.com/assets/1/2/f/1/8/51dde46bce395f4965000000.JPG)

*RedBoard\'s make an especially special jig for aligning male headers.*

Then line up and plug in the shield, and solder away.

[![Shield inserted into jig](https://cdn.sparkfun.com/r/600-600/assets/0/a/7/6/1/51dde46bce395f7164000000.JPG)](https://cdn.sparkfun.com/assets/0/a/7/6/1/51dde46bce395f7164000000.JPG)

*Shield with headers, ready for soldering. We can trust the RedBoard to line the male headers up for us.*

Be somewhat careful using this method. Don\'t leave the iron on the pins for too long or you risk burning the Arduino\'s headers underneath. If you\'re especially worried about burning your Arduino\'s female headers, you can solder just a single pin on each header, remove the shield, and solder the rest.

### Holding Headers Against the Shield

Don\'t have an extra shield around or your development board does not have any header pins soldered on yet? For those that have the dexterity, you can install a row of headers by holding the pins against the board! You can even try to use tape and sticky tack. Below is an example of [installing female headers on the ProtoShield](https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide#hardware-assembly). However, you can follow along with male headers or use this technique to solder headers on development boards as well.

Grab a female stackable header and slide it from the top side of a shield. With your soldering hand, pull the header with your index finger and thumb toward the edge of the board. Using your other hand, push against the header using your index finger and grip the board with your thumb. Hold the header down with your middle finger. Make sure to avoid touching any header pins where the soldering iron will touch.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg "Align Header to ProtoShield")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg "Hold Header Down")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Grab the soldering iron with your soldering hand and tack on one pin. Repeat for each header. After tacking one pin for each header, you will want to ensure that the pins are straight and perpendicular to your board. If they are not, you can try to reheat the header pin and adjust the header\'s alignment.

[![Tack on One Pin on the Header and Repeat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)

If the headers are aligned, you can solder the rest of the header pins on the board to finish installing the headers on the shield!

### Installing Headers on Other Shields with a Breadboard

If you are using a shield that does not use the R3 form factor, you may be able to use a breadboard to help solder headers. Below is an example with male headers being soldered on the TeensyView shield for a Teensy and MiniGen shield for a Pro Mini. The Teensy and Pro Mini form factors use breadboard compatible pins on the edge of the board without the weird 0.5\" spacing.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Installing male headers on TeensyView shield for the Teensy with a breadboard.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/2/Teensy_View_Hookup_Guide-07.jpg)](https://learn.sparkfun.com/tutorials/teensyview-hookup-guide#hardware-overview-and-assembly)   [![v](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/0/MiniGen_Hookup_Guide-04.jpg)](https://learn.sparkfun.com/tutorials/minigen-hookup-guide)
  *Installing male headers on [TeensyView shield](https://learn.sparkfun.com/tutorials/teensyview-hookup-guide#hardware-overview-and-assembly) for the Teensy with a breadboard.*                                                                                                     *Installing long male headers on the [MiniGen shield](https://learn.sparkfun.com/tutorials/minigen-hookup-guide) for the Pro Mini with a mini-breadboard.*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

When using a breadboard, you will also want to be careful soldering the pins to the shield. If you leave the iron on the pins for too long, you will also run the risk of melting the plastic breadboard holding the metal rails as well.