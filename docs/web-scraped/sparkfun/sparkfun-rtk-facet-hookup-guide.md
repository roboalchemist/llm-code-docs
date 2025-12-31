# Source: https://learn.sparkfun.com/tutorials/sparkfun-rtk-facet-hookup-guide

## Introduction

The [RTK Facet](https://www.sparkfun.com/products/19984) from SparkFun is our most advanced GNSS receiver to date. It\'s your one stop shop for high precision geolocation and surveying needs. For basic users, it's incredibly easy to get up and running and for advanced users, the RTK Facet is a flexible and powerful tool.

[![SparkFun RTK Facet](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/7/2/7/19984-SparkFun_RTK_Facet_Kit-02-1.png)](https://www.sparkfun.com/sparkfun-rtk-facet.html)

### [SparkFun RTK Facet](https://www.sparkfun.com/sparkfun-rtk-facet.html) 

[ GPS-19984 ]

The SparkFun RTK Facet is a fully enclosed GNSS receiver for centimeter-level positioning. Perfect for high precision geoloca...

[ [\$739.95] ]

With just a few minutes of setup, the RTK Facet is one of the fastest ways to take centimeter grade measurements.

[![Image of Nate getting measurements](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Surveying_Monopod.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Surveying_Monopod.jpg)

*Surveying with a monopod and SW Maps*

[![RTK Fix in SW Maps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/5/7/RTK_Express_-_SW_Maps_Status.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/RTK_Express_-_SW_Maps_Status.jpg)

*An RTK Fix with 14mm accuracy in SW Maps*

By connecting your phone to the RTK Facet over Bluetooth, your phone can act as the radio link to provide correction data as well as receive the NMEA output from the device. It's how \$10,000 surveying devices have been operating for the past decade - we just made it easier, smaller, and a lot more economical.

### Watch A Quick Setup

### Required Materials

The RTK Facet has all you need built into one small unit. In addition, the [RTK Facet Kit](https://www.sparkfun.com/products/19984) includes everything you *might* need as well. The only thing you need to add is your own tablet or cell phone (Andriod and iOS are supported).

Depending on your setup you may want to use your phone for RTCM correction data. If a source is not available online, you will need a 2nd RTK Facet setup in base mode and a radio link connecting the Base to the Rover. We\'ll go into details but we designed RTK Facet to work with these 100mW 915MHz telemetry radios out of the box.

[![SiK Telemetry Radio V3 - 915MHz, 100mW](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/6/3/4/19032-SiK_Telemetry_Radio_V3_-_915MHz__100mW-01.jpg)](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html)

### [SiK Telemetry Radio V3 - 915MHz, 100mW](https://www.sparkfun.com/sik-telemetry-radio-v3-915mhz-100mw.html) 

[ WRL-19032 ]

The 915MHz SiK Telemetry Radio V3 is a lightweight and inexpensive open source radio platform that can allow for ranges of 30...

[ [\$149.95] ]

To charge the RTK Facet you will need a USB C cable and a power supply. These are included with the kit but any USB C port should charge the Facet at a maximum rate of 1A per hour.

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

GNSS RTK is an incredible feat of engineering that has been made easy to use by powerful GNSS receivers such as the ZED-F9P by u-blox (the receiver inside RTK Facet). The process of setting up an RTK system will be covered in this tutorial but if you want to know more about RTK here are some good tutorials to brush up on:

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

The RTK Facet is a fully enclosed, preprogrammed device. There are very few things to worry about or configure but we will cover the basics.

### **Power/Setup Button**

[![RTK Facet Front Face](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Front_Face_All.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Front_Face_All.jpg)

The RTK Facet has one button used for both **Power** and **Setup** for in-field configuration changes. Pressing and holding the Power button will cause it to power on or off. Short pressing the button will cause the RTK Facet to change modes.

This device can be used in four modes:

- GNSS Positioning (\~30cm accuracy) - also known as \'Rover\'
- GNSS Positioning with RTK (1.4cm accuracy) - also known as \'Rover with RTK Fix\'
- GNSS Base Station
- GNSS Base Station NTRIP Server

At *Power On* the device will enter Rover or Base mode; whichever state the device was in at the last power down. When the POWER/SETUP button is pressed momentarily, a menu is presented to change the RTK Facet to *Rover* or *Base* mode. The display will indicate the change with a small car or flag icon.

In *Rover* mode the RTK Facet will receive L1 and L2 GNSS signals from the four constellations (GPS, GLONASS, Galileo, and BeiDou) and calculate the position based on these signals. Similar to a standard grade GPS receiver, the RTK Facet will output industry standard NMEA sentences at 4Hz and broadcast them over any paired Bluetooth device. The end user will need to parse the NMEA sentences using commonly available mobile apps, GIS products, or embedded devices (there are many open source libraries). Unlike standard grade GPS receivers that have 2500m accuracy, the accuracy in this mode is approximately 300mm horizontal positional accuracy with a good grade L1/L2 antenna.

When the device is in *Rover* mode and RTCM correction data is sent over Bluetooth or into the radio port, the device will automatically enter **Positioning with RTK** mode. In this mode RTK Facet will receive L1/L2 signals from the antenna and correction data from a base station. The receiver will quickly (within a second) obtain RTK float, then fix. The NMEA sentences will have increased accuracy of 14mm horizontal and 10mm vertical accuracy. The RTCM correction data is most easily obtained over the internet using a free app on your phone (see SW Maps or Lefebure NTRIP) and sent over Bluetooth to the RTK Facet but RTCM can also be delivered over an external cellular or radio link to a 2nd RTK Facet setup as a base station.

In *Base* mode the device will enter *Base Station* mode. This is used when the device is mounted to a fixed position (like a tripod or roof). The RTK Facet will initiate a survey. After 60 to 120 seconds the survey will complete and the RTK Facet will begin transmitting RTCM correction data out the radio port. A base is often used in conjunction with a second RTK Facet (or RTK Surveyor) unit set to \'Rover\' to obtain the 14mm accuracy. Said differently, the Base sits still and sends correction data to the Rover so that the Rover can output a really accurate position. You'll create an RTK system without any other setup.

#### **Power**

[![RTK Facet startup display with firmware version number](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Display_On_Off.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Display_On_Off.jpg)

*RTK Facet startup display with firmware version number*

The Power button turns on and off the unit. Press and hold the power button until the display illuminates. Press and hold the power button at any time to turn the unit off.

[![RTK Facet showing the battery level](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_Fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_Fixed.jpg)

*RTK Facet showing the battery level*

The RTK Facet has a large, built-in 6000mAh lithium polymer battery that will enable over 25 hours of field use between charging. If more time is needed a common USB power bank can be attached boosting the field time to any amount needed.

### **Charge LED**

[![RTK Facet Charge LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Front_Face_-_Charge_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Front_Face_-_Charge_LED.jpg)

The Charge LED is located on the front face. It will illuminate any time there is an external power source and will turn off when the internal battery is charged. With the unit fully powered down, charging takes approximately 6 hours from a 1A wall supply or 12 hours from a standard USB port. The RTK Facet can run while being charged but it increases the charge time. Using an external USB battery bank to run the device for extended periods or running the device on a permanent wall power source is supported.

### **Connectors**

[![RTK Facet Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports.jpg)

*The SparkFun RTK Facet connectors shown with the dust cover removed*

There are a variety of connectors protected by a dust flap.

#### **USB:**

[![RTK Facet USB C Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_USB.jpg)

This USB C connector is used for three purposes:

- Charging the device
- Configuring the RTK Facet, and reprogramming the ESP32
- Directly configuring and inspecting the ZED-F9P GNSS receiver

There is a USB hub built into the RTK Facet. When you attach the device to your computer it will enumerate as two COM ports.

[![Two COM ports from one USB device](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Multiple_COM_Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Multiple_COM_Ports.jpg)

In the image above, the `USB Serial Device` is the ZED-F9P and the `USB-SERIAL CH340` is the ESP32.

**Don\'t See \'USB-Serial CH340\'?** If you\'ve never connected a CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [\"How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

**Don\'t See \'USB Serial Device\'?** The first time a u-blox module is connected to a computer you may need to adjust the COM driver. Check out our section on [\"How to Install u-blox Drivers\"](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox#install-drivers) for help with the installation.

Configuring the RTK Facet can be done over the *USB-Serial CH340* COM port via serial text menu. Various debug messages are printed to this port at 115200bps and a serial menu can be opened to configure advanced settings.

Configuring the ZED-F9P can be configured over the *USB Serial Device* port using [u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox/all). It's not necessary in normal operation but is handy for tailoring the receiver to specific applications. As an added perk, the ZED-F9P can be detected automatically by some mobile phones and tablets. If desired, the receiver can be directly connected to a compatible phone or tablet removing the need for a Bluetooth connection.

#### **Radio:**

[![RTK Facet Radio Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Radio.jpg)

This port is used when an external cellular or radio link is needed. This port is *not* used if you transfer RTCM from your phone to the RTK Facet over Bluetooth.

This 4-pin JST connector can be used to allow RTCM correction data to flow into the device when it is acting as a rover or out of the device when it is acting as a base. The connector is a 4-pin locking 1.25mm JST SMD connector (part#: SM04B-GHS-TB, mating connector part#: GHR-04V-S). The RTK Facet comes with a cable to interface to this connector but [additional cables](https://www.sparkfun.com/products/17239) can be purchased. You will most likely connect this port to one of our [Serial Telemetry Radios](https://www.sparkfun.com/products/19032) if you don't have access to a correction source on the internet. The pinout is **3.5-5.5V** / TX / RX / GND from left to right as pictured. **3.5V to 5.5V** is provided by this connector to power a radio with a voltage that depends on the power source. If USB is connected to the RTK Facet then voltage on this port will be **5V** (+/-10%). If running off of the internal battery then voltage on this port will vary with the battery voltage (**3.5V** to **4.2V** depending on the state of charge). This port is capable of sourcing up to 600mA and is protected by a PTC (resettable fuse). This port should not be connected to a power source.

#### **Data:**

[![RTK Facet Data Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Data.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Data.jpg)

This port is used when an external system is connected such as a rover, car, timing equipment, camera triggers, etc. This port is *not* used if you transfer NMEA positional data to your phone from the RTK Facet over Bluetooth.

This 4-pin JST connector is used to output and input a variety of data to the RTK Facet. The connector is a 4-pin locking 1.25mm JST SMD connector (part#: SM04B-GHS-TB, mating connector part#: GHR-04V-S). The RTK Facet comes with a cable to interface to this connector but [additional cables](https://www.sparkfun.com/products/17240) can be purchased.

Internally the Data connector is connected to a digital mux allowing one of four software selectable setups:

- **NMEA** - The TX pin outputs any enabled messages (NMEA, UBX, and RTCM) at a default of 460,800bps (configurable 9600 to 921600bps). The RX pin can receive RTCM for RTK and can also receive UBX configuration commands if desired.
- **PPS/Trigger** - The TX pin outputs the pulse-per-second signal that is accurate to 30ns RMS. The RX pin is connected to the EXTINT pin on the ZED-F9P allowing for events to be measured with incredibly accurate nano-second resolution. Useful for things like audio triangulation. See the Timemark section of the ZED-F9P integration for more information.
- **I2C** - The TX pin operates as SCL, RX pin as SDA on the I2C bus. This allows additional sensors to be connected to the I2C bus.
- **GPIO** - The TX pin operates as a DAC capable GPIO on the ESP32. The RX pin operates as a ADC capable input on the ESP32. This is useful for custom applications.

Most applications do not need to utilize this port and will send the NMEA position data over Bluetooth. This port can be useful for sending position data to an embedded microcontroller or single board computer. The pinout is **3.3V** / TX / RX / GND. **3.3V** from left to right as pictured, which is provided by this connector to power a remote device if needed. While the port is capable of sourcing up to 600mA, we do not recommend more than 300mA. This port should not be connected to a power source.

#### **microSD:**

[![RTK Facet microSD connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_microSD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_microSD.jpg)

This slot accepts standard microSD cards up to 32GB formatted for FAT16 or FAT32. Logging any of 67 messages at up to 4Hz is supported for all constellations.

The following 67 messages are supported for logging:

  ----------------- ---------------- -----------------
  • NMEA-GSA        • NMEA-GST       • NMEA-GSV
  • NMEA-RMC        • NMEA-VLW       • NMEA-VTG
  • NMEA-ZDA        • NAV-CLOCK      • NAV-DOP
  • NAV-EOE         • NAV-GEOFENCE   • NAV-HPPOSECEF
  • NAV-HPPOSLLH    • NAV-ODO        • NAV-ORB
  • NAV-POSECEF     • NAV-POSLLH     • NAV-PVT
  • NAV-RELPOSNED   • NAV-SAT        • NAV-SIG
  • NAV-STATUS      • NAV-SVIN       • NAV-TIMEBDS
  • NAV-TIMEGAL     • NAV-TIMEGLO    • NAV-TIMEGPS
  • NAV-TIMELS      • NAV-TIMEUTC    • NAV-VELECEF
  • NAV-VELNED      • RXM-MEASX      • RXM-RAWX
  • RXM-RLM         • RXM-RTCM       • RXM-SFRBX
  • MON-COMMS       • MON-HW2        • MON-HW3
  • MON-HW          • MON-IO         • MON-MSGPP
  • MON-RF          • MON-RXBUF      • MON-RXR
  • MON-TXBUF       • TIM-TM2        • TIM-TP
  • TIM-VRFY        • RTCM3x-1005    • RTCM3x-1074
  • RTCM3x-1077     • RTCM3x-1084    • RTCM3x-1087
  • RTCM3x-1094     • RTCM3x-1097    • RTCM3x-1124
  • RTCM3x-1127     • RTCM3x-1230    • RTCM3x-4072-0
  • RTCM3x-4072-1                    
  ----------------- ---------------- -----------------

#### **Qwiic:**

[![RTK Facet Qwiic connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Ports_-_Qwiic.jpg)

This 4-pin [Qwiic connector](https://www.sparkfun.com/qwiic) exposes the I2C bus of the ESP32 WROOM module. Currently, there is no firmware support for adding I^2^C devices to the RTK Facet but support may be added in the future.

#### **Antenna:**

[![Internal RTK Facet Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_L1_L2_Antenna_-_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_L1_L2_Antenna_-_1.jpg)

It\'s built in! Housed under the dome of the RTK Facet is a surveyor grade L1/L2 antenna. It is the same element found within our [GNSS Multi-Band L1/L2 Surveying Antenna](https://www.sparkfun.com/products/17751). Its datasheet is available [here](https://cdn.sparkfun.com/assets/b/4/6/d/e/TOP106_GNSS_Antenna.pdf).

[![SparkFun RTK Facet Antenna Reference Point](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_ARP-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_ARP-1.jpg)

*SparkFun RTK Facet Antenna Reference Points*

The built in antenna has an antenna phase center (APC) of 61.4mm from the base if the device to the measuring point of the L1 antenna and an APC of 57.4mm to the measuring point of the L2 antenna.

### **Power**

[![RTK Facet Display showing three battery bars](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_RTK_Fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/5/7/SparkFun_RTK_Express_-_Display_-_Rover_RTK_Fixed.jpg)

*RTK Facet Display showing three battery bars*

The RTK Facet has a built in 6000mAh battery and consumes approximately 240mA worst case with Bluetooth connection active and GNSS fully tracking. This will allow for around 25 hours of use in the field. If more time is needed in the field a standard USB power bank can be attached. If a 10,000mAh bank is attached one can estimate 56 hours of run time assuming 25% is lost to efficiencies of the power bank and charge circuit within RTK Facet.

The RTK Facet can be charged from any USB port or adapter. The charge circuit is rated for 1000mA so USB 2.0 ports will charge at 500mA and USB 3.0+ ports will charge at 1A.

To quickly view the state of charge, turn on the unit. The battery icon will indicate the following:

- 3 bars: \>75% capacity remain
- 2 bars: \>50% capacity remain
- 1 bar: \>25% capacity remain
- 0 bars: \<25% capacity remain

## Hardware Overview - Advanced Features

[![RTK Facet Circuit Boards](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/RTK_Facet_Photos-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/RTK_Facet_Photos-07.jpg)

*The boards that make up the RTK Facet*

The RTK Facet is a hacker's delight. Under the hood of the RTK Facet is an ESP32 WROOM connected to a ZED-F9P as well as some peripheral hardware (LiPo fuel gauge, microSD, etc). It is programmed in Arduino and can be tailored by the end user to fit their needs.

[![RTK Facet Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Main_Board_Schematic_Image.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Main_Schematic.pdf)

*Click on the image to get a closer look at the Schematic!*

[![Internal RTK Facet Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_L1_L2_Antenna_-_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_L1_L2_Antenna_-_1.jpg)

*The Facet with three sub boards, the battery, and antenna*

### ZED-F9P GNSS Receiver

The [ZED-F9P GNSS receiver](https://www.sparkfun.com/products/16481) is configured over I^2^C and uses two UARTs to output NMEA (UART1) and input/output RTCM (UART2). In general, the ESP32 harvests the data from the ZED-F9Ps UART1 for Bluetooth transmission and logging to SD.

### ESP32

The [ESP32](https://www.sparkfun.com/products/15663) uses a standard USB to serial conversion IC ([CH340](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)) to program the device. You can use the ESP32 core for Arduino or Espressif's [IoT Development Framework (IDF)](https://www.espressif.com/en/support/download/all).

The CH340 automatically resets and puts the ESP32 into bootload mode as needed. However, the reset pin of the ESP32 is brought out to an external 2-pin 0.1" footprint if an external reset button is needed.

**Note:** If you\'ve never connected a CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [\"How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

### LiPo and Charging

The RTK Facet houses a standard [6000mAh 3.7V LiPo](https://www.sparkfun.com/products/13856). The charge circuit is set to 1A so with an appropriate power source, charging an empty battery should take a little over six hours. USB C on the RTK Facet is configured for 2A draw so if the user attaches to a USB 3.0 port, the charge circuit should operate near the 1A max. If a user attaches to a USB 2.0 port, the charge circuit will operate at 500mA. This charge circuit also incorporates a 42C upper temperature cutoff to insure the LiPo cannot be charged in dangerous conditions.

### Fuel Gauge

The [MAX17048](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/MAX17048-MAX17049.pdf) is a simple to use fuel gauge IC that gives the user a statement of charge (SOC) that is basically a 0 to 100% report. The MAX17048 has a sophisticated algorithm to figure out what the SOC is based on cell voltage that is beyond the scope of this tutorial but for our purposes, allows us to reliably view the battery level when the unit is on.

### Qwiic

An internal [Qwiic connector](https://www.sparkfun.com/qwiic) is included in the unit for future expansion. Currently the stock RTK Facet does not support any additional Qwiic sensors or display but users may add support for their own application.

### microSD

A microSD socket is situated on the ESP32 SPI bus. Any microSD up to 32GB is supported. RTK Facet supports RAWX and NMEA logging to the SD card. Max logging time can also be set (default is 24 hours) to avoid multi-gigabyte text files. For more information about RAWX and doing PPP please see [this tutorial](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#gather-raw-gnss-data).

### Data Port and Digital Mux

The 74HC4052 analog mux controls which digital signals route to the external Data port. This allows a variety of custom end user applications. The most interesting of which is event logging. Because the ZED-F9P has microsecond accuracy of the incoming digital signal, custom firmware can be created to triangulate an event based on the receiver\'s position and the time delay between multiple captured events. Currently, TM2 event logging is supported.

Additionally, this mux can be configured to connect ESP pin 26 (DAC capable) and pin 39 (ADC capable) for end user custom applications.

## Hardware Assembly

The RTK Facet was designed to work with low-cost, off the shelf equipment. Here we'll describe how to assemble a Rover and Base.

### Surveying (Rover Mode)

[![Basic RTK Facet setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_On_Monopod.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_On_Monopod.jpg)

*Basic RTK Facet Rover setup with RTCM over Bluetooth*

Shown above is the most common RTK Rover setup. A monopole designed for cameras is used. The ¼" camera thread of the monopole is [adapted to ⅝" 11-TPI](https://www.sparkfun.com/products/17546) and the RTK Facet is mounted on top. No radio is needed because RTCM correction data is provided by a phone over Bluetooth.

If you're shopping for a monopole (aka monopod), get one that is 65" in length or greater to ensure that the antenna will be above your head. We've had good luck with the [Amazon Basics](https://www.amazon.com/AmazonBasics-WT1003-67-Inch-Monopod/dp/B00FAYL1YU) brand.

If you prefer to mount your tablet or cell phone to the monopole be sure to get a clamp that is compatible with the diameter of your monopole and has a knob to increase clamp pressure. Our monopole is 27mm in diameter so a device clamp would need to be able to handle that diameter.

[![RTK Facet setup with radio](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_External_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_External_Radio.jpg)

*2nd most common setup with a 915MHz Radio providing RTCM*

If you are receiving RTCM correction data over a radio link it's recommended that you attach a radio to the bottom of the RTK Facet.

[![Serial Telemetry Radio mounted to the back of RTK Facet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_External_Radio_Positioning.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_External_Radio_Positioning.jpg)

[Picture hanging strips](https://www.amazon.com/gp/product/B073XS3CHW) from 3M make a nice semi-permanent mount. Plug the 4-pin to 6-pin JST cable included with the RTK Facet from the **Radio** port to either of the [Serial Telemetry Radios](https://www.sparkfun.com/products/19032) (shipped in pairs). We really love these radios because they are paired out of the box, either can send or receive (so it doesn\'t matter which radio is attached to base or rover) and they have remarkable range. We achieved over a mile range (nearly 1.5 miles or 2.4km) with the 100mW radios and a [big 915MHz antenna](https://www.sparkfun.com/products/retired/14868) on the base (see [this tutorial](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#mini-computer-setup) for more info).

### Temporary Base

A temporary or mobile base setup is needed when you are in the field too far away from a correction source and/or cellular reception. A 2nd RTK Facet is mounted to a tripod and it is configured to complete a survey-in (aka, locate itself), then begin broadcasting RTCM correction data. This data (\~1000 bytes a second) is sent to the user\'s connected radio of choice. For our purposes, the 915MHz 100mW telemetry radios are used because they provide what is basically a serial cable between our base and rover.

[![Temporary RTK Facet Base setup](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Base_Tripod.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/SparkFun_RTK_Facet_-_Base_Tripod.jpg)

*Temporary RTK Facet Base setup*

Any tripod with a ¼" camera thread will work. The [Amazon Basics tripod](https://www.amazon.com/AmazonBasics-Lightweight-Camera-Mount-Tripod/dp/B00XI87KV8) works well enough but is a bit light weight and rickety. The ¼" camera thread is [adapted to ⅝" 11-TPI](https://www.sparkfun.com/products/17546) and the RTK Facet is attached on top.

Once the base has been setup with a clear view of the sky, turn on the RTK Facet. Once on, press the *Setup* button to put the device in Base mode. The display will show the Survey-In screen for 60-120 seconds. Once the survey is complete the display will show the \'Xmitting\' display and begin producing RTCM correction data. You can verify this by viewing the LEDs on the telemetry radio (a small red LED will blink when serial data is received from the RTK Facet). The RTK Facet is designed to follow the u-blox recommended survey-in of 60s and a mean 3D standard deviation of 5m of all fixes. If a survey fails to achieve these requirements it will auto-restart after 10 minutes.

**Note:** A mobile base station works well for quick trips to the field. However, the survey-in method is not recommended for the highest accuracy measurements because the positional accuracy of the base will directly translate to the accuracy of the rover. Said differently, if your base\'s calculated position is off by 100cm, so will every reading your rover makes. If you're looking for maximum accuracy consider installing a [static base with fixed antenna](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station#static-base-setup--lasers). We were able to pinpoint the antenna on the top of SparkFun with an incredible accuracy [+/-2mm of accuracy](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/6/3/SparkFun_PPP_Results.png) using PPP!

## Bluetooth and NTRIP

The RTK Facet transmits full NMEA sentences over Bluetooth serial port profile (SPP) at 4Hz and 115200bps. This means that nearly any GIS application that can receive NMEA data over serial port (almost all do) can be used with the RTK Facet. As long as your device can open a serial port over Bluetooth (also known as SPP) your device can retrieve industry standard NMEA positional data. The following steps show how to use SW Maps but the same steps can be followed to connect any serial port based GIS application.

Please see the [SparkFun RTK Product Manual](https://sparkfun.github.io/SparkFun_RTK_Firmware/connecting_bluetooth/) for step by step instructions.

## Display

The RTK Facet has a 0.96\" high-contrast OLED display. While small, it packs various situational data that can be helpful in the field. We will walk you through each display.

Please see the [SparkFun RTK Product Manual](https://sparkfun.github.io/SparkFun_RTK_Firmware/displays/) for a description of each display.

## System Configuration

Out of the box, the SparkFun RTK products are exceptional GNSS receivers out-of-box and can be used with little or no configuration. Additionally, the line of RTK products from SparkFun are immensely configurable. Please see the [SparkFun RTK Product Manual](https://docs.sparkfun.com/SparkFun_RTK_Firmware/) for detailed descriptions of all the available features on the RTK products.

## Firmware Updates and Customization

The RTK Facet is open source hardware meaning you have total access to the [firmware](https://github.com/sparkfun/SparkFun_RTK_Firmware) and [hardware](https://github.com/sparkfun/SparkFun_RTK_Facet).

From time to time SparkFun will release new firmware for the RTK product line to add and improve functionality. We\'ve made updating the firmware as easy as possible. Please see [Updating RTK Firmware](https://sparkfun.github.io/SparkFun_RTK_Firmware/firmware_update/) for a step by step tutorial.

## Troubleshooting

### Can\'t connect to SWMaps

Are you seeing **The GNSS instrument connection failed!**?

The wrong instrument is set. Please select \'SparkFun RTK Surveyor\' from the instrument drop down list.

[![Select SparkFun RTK Surveyor before clicking \'Connect](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/8/List_of_Instruments_in_SWMaps.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/8/List_of_Instruments_in_SWMaps.jpg)

*Select SparkFun RTK Surveyor before clicking \'Connect\'*

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. The best place to ask about the RTK product range is the [Global Positioning Forum](https://forum.sparkfun.com/viewforum.php?f=116). If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)