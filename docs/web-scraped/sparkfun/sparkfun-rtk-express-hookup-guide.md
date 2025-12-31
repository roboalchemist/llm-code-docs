# Source: https://learn.sparkfun.com/tutorials/sparkfun-rtk-express-hookup-guide

## Introduction

The [RTK Express](https://www.sparkfun.com/products/18442) from SparkFun is your one stop shop for high precision geolocation and surveying needs. For basic users, it's incredibly easy to get up and running and for advanced users, the RTK Express is a flexible and powerful tool.

[![SparkFun RTK Express](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/8/7/7/18019-SparkFun_RTK_Express-09.jpg)](https://www.sparkfun.com/sparkfun-rtk-express.html)

### [SparkFun RTK Express](https://www.sparkfun.com/sparkfun-rtk-express.html) 

[ GPS-18442 ]

The SparkFun RTK Express is an easy to use GNSS receiver for centimeter-level positioning. Perfect for surveying, logging, an...

[ [\$534.95] ]

With just a few minutes of setup, the RTK Express is one of the fastest ways to take centimeter grade measurements.

[![RTK Fix in SW Maps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/RTK_Express_-_SW_Maps_Status.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/RTK_Express_-_SW_Maps_Status.jpg)

*An RTK Fix with 14mm accuracy in SW Maps*

By connecting your phone to the RTK Express over Bluetooth, your phone can act as the radio link to provide correction data as well as receive the NMEA output from the device. It's how \$10,000 surveying devices have been operating for the past decade - we just made it easier, smaller, and a lot cheaper.

### Required Materials

While the RTK Express is nicely enclosed you will need a few cables and antennas to make everything work. We\'ll go into the specifics of how to hook things together but in general you will need to get a good quality L1/L2 antenna:

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

[![Antenna Thread Adapter - 1/4in. to 5/8in.](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/4/2/7/17546-1_4in._to_5_8in._Adapter_for_5_8in._Thread-01.jpg)](https://www.sparkfun.com/antenna-thread-adapter-1-4in-to-5-8in.html)

### [Antenna Thread Adapter - 1/4in. to 5/8in.](https://www.sparkfun.com/antenna-thread-adapter-1-4in-to-5-8in.html) 

[ PRT-17546 ]

This aluminum adapter converts the very common 1/4\" thread found on camera tri-pods and mono-pods to the 5/8\" 11-TPI (threads...

[ [\$6.50] ]

[![Interface Cable - SMA Male to TNC Male (300mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/9/8/0/17833-Interface_Cable_-_SMA_Male_to_TNC_Male__300mm_-01.jpg)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html)

### [Interface Cable - SMA Male to TNC Male (300mm)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html) 

[ CAB-17833 ]

This is a 300mm long Male TNC to Male SMA cable. This is an excellent cable for connecting one of our RTK development boards ...

**Retired**

Depending on your setup you may want to use your phone for RTCM correction data. If a source is not available online, you will need a 2nd RTK Facet setup in base mode and a radio link connecting the Base to the Rover. We\'ll go into details but we designed RTK Facet to work with these 100mW 915MHz telemetry radios out of the box.

[![SiK Telemetry Radio V3 - 915MHz, 100mW](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/6/3/4/19032-SiK_Telemetry_Radio_V3_-_915MHz__100mW-01.jpg)](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html)

### [SiK Telemetry Radio V3 - 915MHz, 100mW](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html) 

[ WRL-19032 ]

The 915MHz SiK Telemetry Radio V3 is a lightweight and inexpensive open source radio platform that can allow for ranges of 30...

[ [\$149.95] ]

To charge the RTK Express you will need a USB C cable and a power supply. SparkFun carries a few options:

[![USB 2.0 Type-C Cable - 1 Meter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/3/4/16905-USB_-_C_to_C_cable-01.jpg)](https://www.sparkfun.com/usb-2-0-type-c-cable-1-meter.html)

### [USB 2.0 Type-C Cable - 1 Meter](https://www.sparkfun.com/usb-2-0-type-c-cable-1-meter.html) 

[ CAB-16905 ]

1 Meter USB Type C to Type C cable USB 2.0 data transfer capabilities.

[ [\$6.50] ]

[![Reversible USB A to C Cable - 0.8m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/4/15425-Reversible_USB_A_to_C_Cable_-_0.8m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html)

### [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-0-8m.html) 

[ CAB-15425 ]

These 0.8m cables have minor modifications that allow them to be plugged into their ports regardless of orientation on the US...

[ [\$6.50] ]

[![USB Wall Charger - 5V, 2A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/2/0/16893-USB_Wall_Charger_-_5V__2A-03.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-2a.html)

### [USB Wall Charger - 5V, 2A](https://www.sparkfun.com/usb-wall-charger-5v-2a.html) 

[ TOL-16893 ]

This USB AC to DC power supply will do 5V at 2A!

[ [\$9.50] ]

[![USB-C Wall Adapter - 5.1V, 3A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/4/7/16272-USB-C_Wall_Adapter_-_5.1V__3A__Black_-01.jpg)](https://www.sparkfun.com/usb-c-wall-adapter-5-1v-3a-black.html)

### [USB-C Wall Adapter - 5.1V, 3A (Black)](https://www.sparkfun.com/usb-c-wall-adapter-5-1v-3a-black.html) 

[ TOL-16272 ]

This is a USB Type-C Power Supply that is compatible with the Raspberry Pi 4.

[ [\$4.50] ]

### Suggested Reading

GNSS RTK is an incredible feat of engineering that has been made easy to use by powerful GNSS receivers such as the ZED-F9P by u-blox (the receiver inside RTK Express). The process of setting up an RTK system will be covered in this tutorial but if you want to know more about RTK here are some good tutorials to brush up on:

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

[](https://learn.sparkfun.com/tutorials/setting-up-a-rover-base-rtk-system)

### Setting up a Rover Base RTK System 

Getting GNSS RTCM correction data from a base to a rover is easy with a serial telemetry radio! We\'ll show you how to get your high precision RTK GNSS system setup and running.

[](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station)

### How to Build a DIY GNSS Reference Station 

Learn how to affix a GNSS antenna, use PPP to get its ECEF coordinates and then broadcast your own RTCM data over the internet and cellular using NTRIP to increase rover reception to 10km!

## Hardware Overview

The RTK Express is a fully enclosed, preprogrammed device. There are very few things to worry about or configure but we will cover the basics.

### **Buttons**

[![RTK Express Buttons](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/RTK_Express_-_Buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/RTK_Express_-_Buttons.jpg)

The RTK Express uses two buttons, **Power** and **Setup** for in-field configuration.

#### **Setup**

This device can be used in four modes:

- GNSS Positioning (\~30cm accuracy) - also known as \'Rover\'
- GNSS Positioning with RTK (1.4cm accuracy) - also known as \'Rover with RTK Fix\'
- GNSS Base Station
- GNSS Base Station NTRIP Server

At power on the device will enter Rover or Base mode; whichever state the device was in at the last power down. When the SETUP button is pressed the RTK Express will toggle between *Rover* and *Base* mode. The display will indicate the change with a small car or flag icon.

In *Rover* mode the RTK Express will receive L1 and L2 GNSS signals from the four constellations (GPS, GLONASS, Galileo, and BeiDou) and calculate the position based on these signals. Similar to a standard grade GPS receiver, the RTK Express will output industry standard NMEA sentences at 4Hz and broadcast them over any paired Bluetooth device. The end user will need to parse the NMEA sentences using commonly available mobile apps, GIS products, or embedded devices (there are many open source libraries). Unlike standard grade GPS receivers that have 2500m accuracy, the accuracy in this mode is approximately 300mm horizontal positional accuracy with a good grade L1/L2 antenna.

When the device is in *Rover* mode and RTCM correction data is sent into the radio port or over Bluetooth, the device will automatically enter **Positioning with RTK** mode. In this mode RTK Express will receive L1/L2 signals from the antenna and correction data from a base station. The receiver will quickly (within a few seconds) obtain RTK float, then fix. The NMEA sentences will have increased accuracy of 14mm horizontal and 10mm vertical accuracy. The RTCM correction data can be obtained from a cellular link to online correction sources or over a radio link to a 2nd RTK Express setup as a base station.

In *Base* mode the device will enter *Base Station* mode. This is used when the device is mounted to a fixed position (like a tripod or roof). The RTK Express will initiate a survey. After 60 to 120 seconds the survey will complete and the RTK Express will begin transmitting RTCM correction data out the radio port. A base is often used in conjunction with a second RTK Express (or RTK Surveyor) unit set to \'Rover\' to obtain the 14mm accuracy. Said differently, the Base sits still and sends correction data to the Rover so that the Rover can output a really accurate position. You'll create an RTK system without any other setup.

#### **Power**

[![RTK Express startup display with firmware version number](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Startup_Shut_Down.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Startup_Shut_Down.jpg)

*RTK Express startup display with firmware version number*

The Power button turns on and off the unit. Press and hold the power button until the display illuminates. Press and hold the power button at any time to turn the unit off.

[![RTK Express showing the battery level](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_Fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_Fixed.jpg)

*RTK Express showing the battery level*

The RTK Express has a built-in 1300mAh lithium polymer battery that will enable over 5 hours of field use between charging. If more time is needed a common USB power bank can be attached boosting the field time to 40 hours.

### **Charge LED**

[![RTK Express Charge LED](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Charge_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Charge_LED.jpg)

The Charge LED is located above the **Power** button. It will illuminate any time there is an external power source and will turn off when the internal battery is charged. With the unit fully powered down, charging takes approximately 1.5 hours from a 1A wall supply or 3 hours from a standard USB port. The RTK Express can run while being charged but it increases the charge time. Using an external USB battery bank to run the device for extended periods or running the device on a permanent wall power source is supported.

### **Connectors**

[![RTK Express Connectors and label](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors.jpg)

*The SparkFun RTK Express has a variety of connectors*

#### **Antenna:**

This SMA connector is used to connect an L1/L2 type GNSS antenna to the RTK Express. Please realize that a standard GPS antenna does not receive the L2 band signals and will greatly impede the performance of the RTK Express (RTK fixes are nearly impossible). Be sure to use a proper [L1/L2 antenna](https://www.sparkfun.com/products/17751).

[![RTK Express SMA connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-SMA.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-SMA.jpg)

#### **Configure u-blox:**

This USB C connector is used for charging the device and/or directly configuring and inspecting the ZED-F9P GNSS receiver using [u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox/all). It's not necessary in normal operation but is handy for tailoring the receiver to specific applications. As an added perk, the ZED-F9P can be detected automatically by some mobile phones and tablets. If desired, the receiver can be directly connected to a compatible phone or tablet removing the need for a Bluetooth connection.

[![RTK Express u-blox connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-u-blox.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-u-blox.jpg)

#### **Configure ESP32:**

This USB C connector is used for charging the device, configuring the device, and reprogramming the ESP32. Various debug messages are printed to this port at 115200bps and a serial menu can be opened to configure advanced settings.

[![RTK Express ESP32 connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-ESP32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-ESP32.jpg)

#### **Radio:**

This 4-pin JST connector is used to allow RTCM correction data to flow into the device when it is acting as a rover or out of the device when it is acting as a base. The connector is a 4-pin locking 1.25mm JST SMD connector (part#: SM04B-GHS-TB, mating connector part#: GHR-04V-S). The RTK Express comes with a cable to interface to this connector but [additional cables](https://www.sparkfun.com/products/17239) can be purchased. You will most likely connect this port to one of our [Serial Telemetry Radios](https://www.sparkfun.com/products/19032) if you don't have access to a correction source on the internet. The pinout is **3.5-5.5V** / TX / RX / GND from left to right as pictured ([pin labels are shown on the board itself](https://learn.sparkfun.com/tutorials/sparkfun-rtk-express-hookup-guide#hardware-overview---advanced-features)). **3.5V to 5.5V** is provided by this connector to power a radio with a voltage that depends on the power source. If USB is connected to the RTK Express then voltage on this port will be **5V** (+/-10%). If running off of the internal battery then voltage on this port will vary with the battery voltage (**3.5V** to **4.2V** depending on the state of charge). While the port is capable of sourcing up to 2 amps, we do not recommend more than 500mA. This port should not be connected to a power source.

[![RTK Express Radio connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Radio.jpg)

#### **Data:**

This 4-pin JST connector is used to output and input a variety of data to the RTK Express. The connector is a 4-pin locking 1.25mm JST SMD connector (part#: SM04B-GHS-TB, mating connector part#: GHR-04V-S). The RTK Express comes with a cable to interface to this connector but [additional cables](https://www.sparkfun.com/products/17240) can be purchased.

Internally the Data connector is connected to a digital mux allowing one of four software selectable setups:

- **NMEA** - The TX pin outputs any enabled messages (NMEA, UBX, and RTCM) at a default of 460,800bps (configurable 9600 to 921600bps). The RX pin can receive RTCM for RTK and can also receive UBX configuration commands if desired.
- **PPS/Trigger** - The TX pin outputs the pulse-per-second signal that is accurate to 30ns RMS. The RX pin is connected to the EXTINT pin on the ZED-F9P allowing for events to be measured with incredibly accurate nano-second resolution. Useful for things like audio triangulation. See the Timemark section of the ZED-F9P integration for more information.
- **I2C** - The TX pin operates as SCL, RX pin as SDA on the I2C bus. This allows additional sensors to be connected to the I2C bus.
- **GPIO** - The TX pin operates as a DAC capable GPIO on the ESP32. The RX pin operates as a ADC capable input on the ESP32. This is useful for custom applications.

Most applications do not need to utilize this port and will send the NMEA position data over Bluetooth. This port can be useful for sending position data to an embedded microcontroller or single board computer. The pinout is **3.3V** / TX / RX / GND. **3.3V** from left to right as pictured ([pin labels are shown on the board itself](https://learn.sparkfun.com/tutorials/sparkfun-rtk-express-hookup-guide#hardware-overview---advanced-features)), which is provided by this connector to power a remote device if needed. While the port is capable of sourcing up to 600mA, we do not recommend more than 300mA. This port should not be connected to a power source.

[![RTK Express Data connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Data.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Data.jpg)

#### **microSD:**

This slot accepts standard microSD cards up to 32GB formatted for FAT16 or FAT32. Logging any of 67 messages at up to 4Hz is supported for all constellations.

[![RTK Express microSD connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-microSD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-microSD.jpg)

The following 67 messages are supported for logging:

- NMEA-DTM
- NMEA-GBS
- NMEA-GGA
- NMEA-GLL
- NMEA-GNS
- NMEA-GRS
- NMEA-GSA
- NMEA-GST
- NMEA-GSV
- NMEA-RMC
- NMEA-VLW
- NMEA-VTG
- NMEA-ZDA
- NAV-CLOCK
- NAV-DOP
- NAV-EOE
- NAV-GEOFENCE
- NAV-HPPOSECEF
- NAV-HPPOSLLH
- NAV-ODO
- NAV-ORB
- NAV-POSECEF
- NAV-POSLLH
- NAV-PVT
- NAV-RELPOSNED
- NAV-SAT
- NAV-SIG
- NAV-STATUS
- NAV-SVIN
- NAV-TIMEBDS
- NAV-TIMEGAL
- NAV-TIMEGLO
- NAV-TIMEGPS
- NAV-TIMELS
- NAV-TIMEUTC
- NAV-VELECEF
- NAV-VELNED
- RXM-MEASX
- RXM-RAWX
- RXM-RLM
- RXM-RTCM
- RXM-SFRBX
- MON-COMMS
- MON-HW2
- MON-HW3
- MON-HW
- MON-IO
- MON-MSGPP
- MON-RF
- MON-RXBUF
- MON-RXR
- MON-TXBUF
- TIM-TM2
- TIM-TP
- TIM-VRFY
- RTCM3x-1005
- RTCM3x-1074
- RTCM3x-1077
- RTCM3x-1084
- RTCM3x-1087
- RTCM3x-1094
- RTCM3x-1097
- RTCM3x-1124
- RTCM3x-1127
- RTCM3x-1230
- RTCM3x-4072-0
- RTCM3x-4072-1

#### **Qwiic:**

This 4-pin [Qwiic connector](https://www.sparkfun.com/qwiic) exposes the I2C bus of the ESP32 WROOM module. Currently, there is no firmware support for adding I2C devices to the RTK Express but support may be added in the future.

[![RTK Surveyor Qwiic connector](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Connectors-Qwiic.jpg)

### **Power**

The RTK Express has a built in 1300mAh battery and consumes approximately 240mA worst case with Bluetooth connection active, GNSS fully tracking, and a 500mW radio broadcasting. This will allow for around 5.5 hours of use in the field. If more time is needed in the field a standard USB power bank can be attached. If a 10,000mAh bank is attached one can estimate 30 hours of run time assuming 25% is lost to efficiencies of the power bank and charge circuit within RTK Express.

The RTK Express can be charged from any USB port or adapter. The charge circuit is rated for 1000mA so USB 2.0 ports will charge at 500mA and USB 3.0+ ports will charge at 1A.

To quickly view the state of charge, turn on the unit. The battery icon will indicate the following:

- 3 bars: \>75% capacity remain
- 2 bars: \>50% capacity remain
- 1 bar: \>25% capacity remain
- 0 bars: \<25% capacity remain

[![RTK Express Display showing three battery bars](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_RTK_Fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_RTK_Fixed.jpg)

*RTK Express Display showing three battery bars*

## Hardware Overview - Advanced Features

The RTK Express is a hacker's delight. Under the hood of the RTK Express is an ESP32 WROOM connected to a ZED-F9P as well as some peripheral hardware (LiPo fuel gauge, microSD, etc). It is programmed in Arduino and can be tailored by the end user to fit their needs.

[![RTK Express Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Schematic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Schematic.pdf)

*Click on the image to get a closer look at the Schematic!*

### ZED-F9P GNSS Receiver

The [ZED-F9P GNSS receiver](https://www.sparkfun.com/products/16481) is configured over I^2^C and uses two UARTs to output NMEA (UART1) and input/output RTCM (UART2). In general, the ESP32 harvests the data from the ZED-F9Ps UART1 for Bluetooth transmission and logging to SD.

[![ZED-F9P GNSS Receiver](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_ZED-F9P.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_ZED-F9P.jpg)

### ESP32

The [ESP32](https://www.sparkfun.com/products/15663) uses a standard USB to serial conversion IC ([CH340](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)) to program the device. You can use the ESP32 core for Arduino or Espressif's [IoT Development Framework (IDF)](https://www.espressif.com/en/support/download/all).

The CH340 automatically resets and puts the ESP32 into bootload mode as needed. However, the reset pin of the ESP32 is brought out to an external 2-pin 0.1" footprint if an external reset button is needed.

**Note:** If you\'ve never connected a CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [\"How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

[![ESP32 on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_ESP32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_ESP32.jpg)

### Measurement Jumpers

To facilitate the measurement of run, charge, and quiescent currents, two measurement jumpers are included. These are normally closed jumpers combined with a 2-pin 0.1" footprint. To take a measurement, cut the jumper and install a 2-pin header and use [banana to IC hook](https://www.sparkfun.com/products/506) cables to a DMM. These can then be closed with a [2-pin jumper](https://www.sparkfun.com/products/9044).

[![Measurement Jumpers on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Measurement_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Measurement_Jumpers.jpg)

### LiPo and Charging

The RTK Express houses a standard [1300mAh 3.7V LiPo](https://www.sparkfun.com/products/17748). The charge circuit is set to 1A so with an appropriate power source, charging an empty battery should take a little over one hour. USB C on the RTK Express is configured for 2A draw so if the user attaches to a USB 3.0 port, the charge circuit should operate near the 1A max. If a user attaches to a USB 2.0 port, the charge circuit will operate at 500mA. This charge circuit also incorporates a 42C upper temperature cutoff to insure the LiPo cannot be charged in dangerous conditions.

[![LiPo and Charging on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_LiPo_Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_LiPo_Battery.jpg)

### Fuel Gauge

The [MAX17048](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/MAX17048-MAX17049.pdf) is a simple to use fuel gauge IC that gives the user a statement of charge (SOC) that is basically a 0 to 100% report. The MAX17048 has a sophisticated algorithm to figure out what the SOC is based on cell voltage that is beyond the scope of this tutorial but for our purposes, allows us to reliably view the battery level when the unit is on.

[![Fuel Gauge on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Accel_Fuel_Gauge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Accel_Fuel_Gauge.jpg)

### Qwiic

Two [Qwiic connectors](https://www.sparkfun.com/qwiic) are included in the unit. The internal Qwiic connector connects to the OLED display attached to the upper lid. The lower Qwiic connector is exposed on the end of the unit. These allow connection to the I^2^C bus on the ESP32. Currently the stock RTK Express does not support any additional Qwiic sensors or display but users may add support for their own application.

[![Dual Qwiic Connector on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Qwiic.jpg)

### microSD

A microSD socket is situated on the ESP32 SPI bus. Any microSD up to 32GB is supported. RTK Express supports RAWX and NMEA logging to the SD card. Max logging time can also be set (default is 10 hours) to avoid multi-gigabyte text files. For more information about RAWX and doing PPP please see [this tutorial](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#gather-raw-gnss-data).

[![microSD socket on SparkFun RTK Express](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_microSD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_microSD.jpg)

### Data Port and Digital Mux

The 74HC4052 analog mux controls which digital signals route to the external Data port. This allows a variety of custom end user applications. The most interesting of which is event logging. Because the ZED-F9P has microsecond accuracy of the incoming digital signal, custom firmware can be created to triangulate an event based on the receiver\'s position and the time delay between multiple captured events. Currently, TM2 event logging is supported.

Additionally, this mux can be configured to connect ESP pin 26 (DAC capable) and pin 39 (ADC capable) for end user custom applications.

[![SparkFun RTK Express Data port and mux](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Data_Port.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Internal_-_Data_Port.jpg)

## Hardware Assembly

The RTK Express was designed to work with low-cost, off the shelf equipment. Here we'll describe how to assemble a Rover and Base.

### Rover

Shown here is the most common RTK Rover setup. A monopole designed for cameras is used. A cell phone holder is clamped to the monopod and the RTK Express is mounted. The ¼" camera thread of the monopole is [adapted to ⅝" 11-TPI](https://www.sparkfun.com/products/17546) and a [L1/L2 antenna](https://www.sparkfun.com/products/17751) is attached. A [Male TNC to Male SMA cable](https://www.sparkfun.com/products/17833) connects the antenna to the RTK Express. No radio is needed because RTCM correction data is provided by a phone over Bluetooth.

[![Basic RTK Express setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Stick.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Stick.jpg)

*Basic RTK Express Rover setup with RTCM over Bluetooth*

If you're shopping for a monopole (aka monopod), get one that is 65" in length or greater to ensure that the antenna will be above your head. We've had good luck with the [Amazon Basics](https://www.amazon.com/AmazonBasics-WT1003-67-Inch-Monopod/dp/B00FAYL1YU) brand.

We have done lots of testing with the [u-blox L1/L2 antenna](https://www.sparkfun.com/products/15192) and it\'s very good for the price and size. Mounted to a ground plate you will get good results. It\'s just a bit ungainly when mounted to the top of a monopole. We recommend the \'ufo\' style L1/L2 antennas because they have a larger antenna element and a slightly larger ground plane than the u-blox antenna.

[![u-blox L1/L2 antenna with ground plate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/3/SparkFun_RTK_Surveyor_-_u-blox_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/SparkFun_RTK_Surveyor_-_u-blox_Antenna.jpg)

*u-blox L1/L2 antenna with ground plate*

We strongly recommend against using a rigid helical antenna configuration as shown below. The RTK Express is not designed for such configurations and can lead to permanent damage to the antenna connector. The helical antenna becomes a large lever arm. If the unit is dropped this lever is capable of damaging both the SMA connector and where the connector is soldered to the PCB.

[![RTK Express with Helical Antenna](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/RTK_Express_-_Bad_Helical_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/RTK_Express_-_Bad_Helical_Antenna.jpg)

*Dangerous Antenna Configuration*

If you're shopping for a cell phone clamp be sure to get one that is compatible with the diameter of your monopole and has a knob to increase clamp pressure. Our monopole is 27mm in diameter and we've had a good experience with [this clamp](https://www.amazon.com/gp/product/B07VF4H6KW) and [this clamp](https://www.amazon.com/gp/product/B072DSRF3J). Your mileage may vary.

[![SparkFun RTK Express mounted in clamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Clamp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Clamp.jpg)

If you are receiving RTCM correction data over a radio link it's recommended that you attach a radio to the back of the RTK Express.

[![RTK Express setup with radio](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Stick_and_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Stick_and_Radio.jpg)

*2nd most common setup with a 915MHz Radio providing RTCM*

[Picture hanging strips](https://www.amazon.com/gp/product/B073XS3CHW) from 3M make a nice semi-permanent mount. Plug the 4-pin to 6-pin JST cable included with the RTK Express from the **Radio** port to either of the [Serial Telemetry Radios](https://www.sparkfun.com/products/19032) (shipped in pairs). We really love these radios because they are paired out of the box, either can send or receive (so it doesn\'t matter which radio is attached to base or rover) and they have remarkable range. We achieved over a mile range (nearly 1.5 miles or 2.4km) with the 500mW radios and a [big 915MHz antenna](https://www.sparkfun.com/products/retired/14868) on the base (see [this tutorial](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#mini-computer-setup) for more info).

[![Serial Telemetry Radio mounted to the back of RTK Express](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/6/3/SparkFun_RTK_Surveyor_-_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/SparkFun_RTK_Surveyor_-_Radio.jpg)

### Temporary Base

A temporary or mobile base setup is needed when you are in the field too far away from a correction source and/or cellular reception. A 2nd RTK Express is mounted to a tripod and it is configured to complete a survey-in (aka, locate itself), then begin broadcasting RTCM correction data. This data (\~1000 bytes a second) is sent to the user\'s connected radio of choice. For our purposes, the 915MHz 500mW telemetry radios are used because they provide what is basically a serial cable between our base and rover.

[![Temporary RTK Express Base setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Base_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Base_Radio.jpg)

*Temporary RTK Express Base setup*

Any tripod with a ¼" camera thread will work. The [Amazon Basics tripod](https://www.amazon.com/AmazonBasics-Lightweight-Camera-Mount-Tripod/dp/B00XI87KV8) works well enough but is a bit light weight and rickety. A cell phone holder is clamped to the tripod and the RTK Express is held in the clamp. The ¼" camera thread is [adapted to ⅝" 11-TPI](https://www.sparkfun.com/products/17546) and a [L1/L2 antenna](https://www.sparkfun.com/products/17751) is attached. A [Male TNC to Male SMA adapter](https://www.sparkfun.com/products/17833) connects the antenna to the RTK Express.

Once the base has been setup with a clear view of the sky, turn on the RTK Express. Once on, press the *Setup* button to put the device in Base mode. The display will show the Survey-In screen for 60-120 seconds. Once the survey is complete the display will show the \'Xmitting\' display and begin producing RTCM correction data. You can verify this by viewing the LEDs on the telemetry radio (a small red LED will blink when serial data is received from the RTK Express). The RTK Express is designed to follow the u-blox recommended survey-in of 60s and a mean 3D standard deviation of 5m of all fixes. If a survey fails to achieve these requirements it will auto-restart after 10 minutes.

More expensive surveyor bases have a ⅝" 11-TPI thread but the top of the surveyor base will often interfere with the antenna's TNC connector. If you chose to use a surveyor's 'stick' be sure to obtain a ⅝" extender plate to raise the antenna at least an inch.

If you're shopping for a cell phone clamp be sure to get one that is compatible with the diameter of your tripod and has a knob to increase clamp pressure. Our tripod is 18mm in diameter and we've had a good experience with [this clamp](https://www.amazon.com/gp/product/B072DSRF3J). Your mileage may vary.

Note: A mobile base station works well for quick trips to the field. However, the survey-in method is not recommended for the highest accuracy measurements because the positional accuracy of the base will directly translate to the accuracy of the rover. Said differently, if your base\'s calulcated position is off by 100cm, so will every reading your rover makes. If you're looking for maximum accuracy consider installing a [static base with fixed antenna](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#static-base-setup--lasers). We were able to pinpoint the antenna on the top of SparkFun with an incredible accuracy [+/-2mm of accuracy](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/SparkFun_PPP_Results.png) using PPP!

## Bluetooth and NTRIP

The RTK Express transmits full NMEA sentences over Bluetooth serial port profile (SPP) at 4Hz and 115200bps. This means that nearly any GIS application that can receive NMEA data over serial port (almost all do) can be used with the RTK Express. As long as your device can open a serial port over Bluetooth (also known as SPP) your device can retrieve industry standard NMEA positional data. The following steps show how to use SW Maps but the same steps can be followed to connect any serial port based GIS application.

Please see the [SparkFun RTK Product Manual](https://sparkfun.github.io/SparkFun_RTK_Firmware/connecting_bluetooth/) for step by step instructions.

## Display

The RTK Express has a 0.96\" high-contrast OLED display. While small, it packs various situational data that can be helpful in the field. We will walk you through each display.

Please see the [SparkFun RTK Product Manual](https://sparkfun.github.io/SparkFun_RTK_Firmware/displays/) for a description of each display.

## System Configuration

Out of the box, the SparkFun RTK products are exceptional GNSS receivers out-of-box and can be used with little or no configuration. Additionally, the line of RTK products from SparkFun are immensely configurable. Please see the [SparkFun RTK Product Manual](https://docs.sparkfun.com/SparkFun_RTK_Firmware/) for detailed descriptions of all the available features on the RTK products.

## Firmware Updates and Customization

The RTK Express is open source hardware meaning you have total access to the [firmware](https://github.com/sparkfun/SparkFun_RTK_Firmware) and [hardware](https://github.com/sparkfun/SparkFun_RTK_Express).

From time to time SparkFun will release new firmware for the RTK product line to add and improve functionality. We\'ve made updating the firmware as easy as possible. Please see [Updating RTK Firmware](https://sparkfun.github.io/SparkFun_RTK_Firmware/firmware_update/) for a step by step tutorial.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)