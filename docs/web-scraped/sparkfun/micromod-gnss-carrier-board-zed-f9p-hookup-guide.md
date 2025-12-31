# Source: https://learn.sparkfun.com/tutorials/micromod-gnss-carrier-board-zed-f9p-hookup-guide

## Introduction

The [SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://www.sparkfun.com/products/17722) combines high-precision GPS and the flexibility of MicroMod onto one board. Utilizing u-blox\'s ZED-F9P module, MicroMod GNSS Carrier Board is capable of 10mm 3 dimensional accuracy. Yes, you read that right, these boards can output your X, Y, and Z location that is roughly the width of your fingernail. With great power comes a few requirements: high precision GPS requires a clear view of the sky (sorry, no indoor location) and a stream of correction data from an RTCM source. We'll get into this more in a later section but as long as you have two ZED-F9P breakout boards, or access to an online correction source, your ZED-F9P can output lat, long, and altitude with centimeter grade accuracy.

[![SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/3/0/17722-SparkFun_MicroMod_GNSS_Carrier_Board__ZED-F9P_-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html)

### [SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html) 

[ GPS-17722 ]

The SparkFun MicroMod GNSS carrier board has the accuracy of GNSS Real Time Kinematics (RTK) with the flexibility of the Micr...

[ [\$269.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum to get started. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. To get the most out of the ZED-F9P, you will need a correction source. Depending on your setup, you may need a second ZED-F9P or access to an online correction source.

### MicroMod Processor Board

You\'ll need a Processor Board with the MicroMod GNSS Carrier Board. We recommend using the MicroMod ESP32 Processor to connect to the cloud. Depending on your setup, you may need a transceiver to pass the correction data.

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

#### Antenna

We recommend using a GNSS multi-band [magnetic mount antenna](https://www.sparkfun.com/products/15192) for the full RF reception. The length of the antenna cable was also useful in mounting it.

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/4/17587-L1_L2_GNSS_antenna_TOP106-09-1.png)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html)

### [GNSS Multi-Band L1/L2 Surveying Antenna - TNC (TOP106)](https://www.sparkfun.com/gnss-multi-band-l1-l2-surveying-antenna-tnc-top106.html) 

[ GPS-17751 ]

The TOP106 from TOPGNSS is a certified GNSS/GPS surveying antenna capable of receiving the L1/L2 bands for GPS, GLONASS, Gali...

[ [\$199.95] ]

[![MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/7/0/17108-AA.200_____MagmaX2_Active_Multiband_GNSS_Magnetic_Mount_Antenna-01A.jpg)](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html)

### [MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html) 

[ GPS-17108 ]

The AA.200 antenna is an active multiband GNSS magnetic mount antenna that exhibits excellent gain and good radiation pattern...

**Retired**

[![GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/4/1/9/17383-GNSS_Multi-Band_L1_L2_Helical_Antenna__SMA__BT-560-01a.jpg)](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html)

### [GNSS Multi-Band L1/L2 Helical Antenna (SMA) BT-560](https://www.sparkfun.com/gnss-multi-band-l1-l2-helical-antenna-sma-bt-560.html) 

[ GPS-17383 ]

The BT-560 antenna is a small, very light weight GNSS/GPS L1/L2 multiband antenna for GPS, GLONASS, Galileo, and BeiDou const...

**Retired**

**Note:** If you want to try different GNSS antennas, the following antennas will work but are limited to L1 frequencies so they will not enable the full L1/L2 capabilities of the ZED-F9P.\
\

[![GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/0/14986-GPS_GNSS_Magnetic_Mount_Antenna_SMA_-_3m-01.jpg)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html)

### [GPS/GNSS Magnetic Mount Antenna - 3m (SMA)](https://www.sparkfun.com/gps-gnss-magnetic-mount-antenna-3m-sma.html) 

[ GPS-14986 ]

This exceptional GPS/GNSS antenna is designed for both GPS and GLONASS reception.

[ [\$16.50] ]

[![GPS/GNSS Embedded Antenna - 1m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/1/14987-GPS_GNSS_Embedded_Antenna_SMA_-_1m-01a.jpg)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html)

### [GPS/GNSS Embedded Antenna - 1m (SMA)](https://www.sparkfun.com/gps-gnss-embedded-antenna-1m-sma.html) 

[ GPS-14987 ]

This tri-band GNSS antenna is ideal for GPS L1, GLONASS L1, and Beidou B2 reception.

[ [\$95.95] ]

#### GPS Antenna Accessories

You can use the GPS antenna ground plate to improve your GPS antenna\'s performance. If you are using the [GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106](https://www.sparkfun.com/products/17751), you\'ll need to grab the interface cable.

[![GPS Antenna Ground Plate](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-01.jpg)](https://www.sparkfun.com/gps-antenna-ground-plate.html)

### [GPS Antenna Ground Plate](https://www.sparkfun.com/gps-antenna-ground-plate.html) 

[ GPS-17519 ]

Using this simple steel plate effectively improves simple patch antenna performance to near professional level antenna setups...

[ [\$7.25] ]

[![Interface Cable - SMA Male to TNC Male (300mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/9/8/0/17833-Interface_Cable_-_SMA_Male_to_TNC_Male__300mm_-01.jpg)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html)

### [Interface Cable - SMA Male to TNC Male (300mm)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html) 

[ CAB-17833 ]

This is a 300mm long Male TNC to Male SMA cable. This is an excellent cable for connecting one of our RTK development boards ...

**Retired**

### Accessories

At a minimum, you will need a USB C cable to power and program the boards. Depending on your application, you may want to grab a Qwiic cable to connect a Qwiic-enabled device.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

### Tools

You will need a screw driver to tighten the screw between the processor board and carrier board.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[](https://learn.sparkfun.com/tutorials/micromod-esp32-processor-board-hookup-guide)

### MicroMod ESP32 Processor Board Hookup Guide 

A short hookup guide to get started with the SparkFun MicroMod ESP32 Processor Board.

This tutorial is based on the GPS-RTK2\'s ZED-F9P. Make sure to check out the breakout boards for more information on GPS-RTK. Be sure to checkout our [What is GPS RTK?](https://learn.sparkfun.com/tutorials/what-is-gps-rtk) tutorial.

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

September 14, 2018

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/gps-rtk-hookup-guide)

### GPS-RTK Hookup Guide 

September 13, 2018

Find out where you are! Use this easy hook-up guide to get up and running with the SparkFun high precision GPS-RTK NEO-M8P-2 breakout board.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

January 14, 2019

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

## Hardware Overview

One of the key differentiators between the ZED-F9P and almost all other low-cost RTK solutions is the ZED-F9P is capable of receiving both L1 and L2 bands.

[![L1 and L2 GNSS reception on the ZED-F9P](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/6/GPS_RTK_L1_and_L2_bands.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/6/GPS_RTK_L1_and_L2_bands.jpg)

### MicroMod Processor Board Socket

The MicroMod GNSS Carrier Board (ZED-F9P) includes a location for a MicroMod Processor Board. Here is where your chosen Processor Board will reside.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_Mdot2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_Mdot2.jpg)

### MicroMod Processor General Pins

Next to the MicroMod Processor Board are extra pins if you need to use a digital or analog pin.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_General_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_General_Pins.jpg)

### Power

There are a few ways to power the board. Voltage is regulated down to 3.3V with the AP7361 voltage regulator. The square IC next to the USB C labeled as processor is where you will find the AP7361.

- **USB C Connector** - You can connect a USB Type C cable from your computer\'s USB port to the board through either of the USB Type C connectors labeled as **u-center** and **processor**. There are protection diodes connected to the voltage lines so you can connect two USB cables at the same time to power the board. The AP7361 voltage regulator will regulate the **5V** from the USB port down to 3.3V for the system voltage.
- **VIN** - If you decide to connect to the VIN pin, we recommend a voltage between **3.3V** to **6.0V**. The AP7361 voltage regulator will regulate the voltage down to 3.3V for the system voltage.
- **3V3** - If you decide to power the board through the 3.3V pin, you could connect a regulated 3.3V to this pin. Otherwise, you could use this to power any peripherals attached to the board.
- **Qwiic Connector** - The Qwiic connector connects to 3.3V and GND to power any Qwiic-enabled devices. Depending on your application, you could connect a regulated 3.3V through this port as well.
- **GND** - Of course, you\'ll need to connect the ground plane to your power source. This pin is available should you decide to power the board through the any of the PTH pins.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Power_Net.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Power_Net.jpg)

### Backup Batteries

There are two built-in backup batteries (ML414H) on the board. The backup battery has a 1mAh capacity and requires 20 minute to charge. The battery near the SMA connector is for the Processor Board\'s RTC and helps keep the RTC running when the external power is removed. Depending on the processor, it may not be connected.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Batteries.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Batteries.jpg)

The other one that is closest to the USB C connector labeled as u-center is for the ZED-F9P module. The rechargeable battery maintains the battery backed RAM (BBR) on the GNSS module. This allows for much faster position locks (a.k.a. hot start). The BBR is also used for module configuration retention. The battery is automatically trickle charged when power is applied and should maintain settings and GNSS orbit data for up to two weeks without power.

### Reset and Boot Buttons

The reset button will reset the processor. The boot button will put the processor into a special boot mode. Depending on the processor board, this boot pin may not be connected.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Reset_Boot_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Reset_Boot_Button.jpg)

### SWD Programming Pins

For advanced users, we broke out the SWD programming pins to connect to a MicroMod Processor Board. Note that this is not populated so you will need a [compatible header and compatible JTAG programmer](https://www.sparkfun.com/categories/tags/jtag) to connect.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SWD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SWD.jpg)

### Communication Ports

The ZED-F9P is unique in that it has *five* communication ports which are all active simultaneously. You can read NMEA data over I^2^C while you send configuration commands over the UART and vice/versa. The only limit is that the SPI pins are mapped onto the I^2^C and UART pins so it's either SPI or I^2^C+UART. The USB port is available at all times.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_View.jpg)

**Note:** With the MicroMod M.2 connector, the ZED-F9P\'s UART1, UART2, SPI, I^2^C ports are available without soldering! Other SparkFun ZED-F9P offerings have this capability, but only after you solder hookup wires appropriately.

### USB

As stated earlier, there are two USB ports: one for **u-center** and another for **processor**. The USB C connector labeled as **u-center** makes it easy to connect the ZED-F9P to u-center for configuration and quick viewing of NMEA sentences. It is also possible to connect a Raspberry Pi or other single board computer over USB. The ZED-F9P enumerates as a serial COM port and it is a separate serial port from the UART interface. See [Getting Started with U-Center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox) for more information about getting the USB port to be a serial COM port. The USB connector labeled as **processor** is available to program your MicroMod Processor Board. Make sure to check your respective Processor Board to install the USB-to-serial drivers.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_USB_Ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_USB_Ports.jpg)

A 3.3V regulator is provided to regulate the 5V USB down to **3.3V** the module requires. External 5V can be applied or a direct feed of 3.3V can be provided. Note that if you're provide the board with 3.3V directly it should be a clean supply with minimal noise (less than 50mV VPP ripple is ideal for precision locating).

The 3.3V regulator is capable of sourcing 600mA from a 5V input and the USB C connection is capable of sourcing 2A.

### I^2^C (a.k.a DDC)

The u-blox ZED-F9P has a "DDC" port which is really just an I^2^C port (without all the fuss of trademark issues). These pins are shared with the SPI pins. By default, the I^2^C pins are enabled. Be sure the SPI jumper on the rear of the board is open. The MicroMod GNSS Carrier Board also includes one Qwiic connector to make daisy chaining this GPS receiver with a large variety of I^2^C devices. Checkout [Qwiic](https://www.sparkfun.com/qwiic) for your next project.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_I2C_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_I2C_Qwiic.jpg)

The only I^2^C address for this and all u-Blox GPS products is **0x42**, though each can have their address changed through software.

### UART/Serial

The classic serial pins are available on the ZED-F9P but are shared with the SPI pins. By default, the UART pins are enabled. Be sure the SPI jumper on the rear of the board is open.

- TXO/SDO = TX out from ZED-F9P
- RXI/SDI = RX into ZED-F9P

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_UARTs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_UARTs.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Bottom_UARTs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Bottom_UARTs.jpg)
  *Top View*                                                                                                                                                                                                                                                  *Bottom View*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There is a second serial port (UART2) available on the ZED-F9P that is primarily used for RTCM3 correction data. By default, this port will automatically receive and parse incoming RTCM3 strings enabling RTK mode on the board. In addition to the TXO2/RXI2 pins we have added an additional 'RTCM Correction' port where we arranged the pins to match the industry standard serial connection (aka the \'FTDI\' pinout). While we label this as \"**Bluetooth**\" on the back of the board, you can still connect any transceiver or serial-to-USB converter to this port. This pinout is compatible with our [Bluetooth Mate](https://www.sparkfun.com/products/12576) and [Serial Basic](https://www.sparkfun.com/products/15096) so you can send RTCM correction data from a cell phone or computer. Note that RTCM3 data can also be sent over I^2^C, UART1, SPI, or USB if desired.

The RTCM correction port (UART2) defaults to **38400bps** serial but can be configured via software commands (checkout our Arduino library) or over USB using u-center. Keep in mind our Bluetooth Mate defaults to **115200bps**. If you plan to use Bluetooth for correction data (we found it to be easiest), we recommend you increase this port speed to 115200bps using u-center. Additionally, but less often needed, the UART2 can be configured for NMEA output. In general, we don't use UART2 for anything but RTCM correction data, so we recommend leaving the in/out protocols as RTCM.

[![UART2 configuration inside u-center](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/6/ZED-F9P_UART2_Configuration.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/6/ZED-F9P_UART2_Configuration.jpg)

If you've got the ZED-F9P setup for base station mode (also called *survey-in* mode) the UART2 will *output* RTCM3 correction data. This means you can connect a radio or wired link to UART2 and the board will automatically send *just* RTCM bytes over the link (no NMEA data taking up bandwidth).

### SPI

The ZED-F9P can also be configured for SPI communication. By default, the SPI port is disabled. To enable SPI close the SPI jumper on the rear of the board. Closing this jumper will disable the UART1 and I^2^C interfaces (UART2 will continue to operate as normal).

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SPI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SPI.jpg)

### Antenna

The ZED-F9P requires a good quality GPS or GNSS (preferred) antenna. For a secure connection, we include an [SMA female connector](https://learn.sparkfun.com/tutorials/connector-basics#sma-antenna-connectors). To make the most out of the ZED-F9P, you\'ll need a multi-band GNSS antenna and an SMA male connector to mate.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SMA_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_SMA_Antenna.jpg)

Low-cost magnetic [GPS/GNSS antennas](https://www.sparkfun.com/categories/18) can be used (checkout the [u-blox white paper](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/4/AntennasForRTK_WhitePaper__UBX-16010559_.pdf)) but a 4" / 10cm metal disc is required to be placed under the antenna as a [metal ground plane](https://www.sparkfun.com/products/15004).

[![GPS Antenna with Ground Plane](https://cdn.sparkfun.com//assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-05.jpg)](https://cdn.sparkfun.com//assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-05.jpg)

### LEDs

The board includes five status LEDs as indicated in the image below.

- **PPS:** The pulse per second LED will illuminate each second once a position lock has been achieved.
- **GEO:** The GEO LED can be configured to turn on/off for geofencing applications.
- **RTK:** The RTK LED will be illuminated constantly upon power up. Once RTCM data has been successfully received it will begin to blink. This is a good way to see if the ZED-F9P is getting RTCM from various sources. Once an RTK fix is obtained, the LED will turn off.
- **VIN:** The VIN LED will illuminate when there is voltage applied to the VIN pin or over USB.
- **3V3:** The power LED will illuminate when 3.3V is activated either over USB or via the Qwiic bus.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_LEDs.jpg)

### Jumpers

**Note:** If this is your first time working with jumpers, check out the [How to Work with Jumper Pads and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all) tutorial for more information.

There are jumpers located throughout the board. Below are the jumpers on the top side of the board.

- **Bypass (BYP):** By default, the BYP is left open. Adding a solder jumper bypasses the 2A resettable fuse on the back of the board should you decide to pull more than 2A from your USB source. Proceed with caution should you decide to bypass the jumper.
- **Enable (EN):** By default, the EN jumper is left open. This jumper is connected to a processor board\'s GPIO pin. The processor board can control the ATP\'s voltage regulator. Depending on the processor, this may not be connected.
- **Current Measurement (MEAS):** By default, the MEAS is closed. Cutting the jumper and soldering to the PTH pads will allows you to insert a current meter and precisely monitor the how much current your application is consuming.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Top_Jumpers.jpg)

Below are the jumpers on the bottom side of the board.

- **3V3 LED:** By default, the 3V3 LED is closed. Cutting this jumper will disable the LED when there is 3.3V.
- **VIN LED:** By default, the VIN LED is closed. Cutting this jumper will disable the LED whenever there is an input voltage.
- **RTK:** By default, the RTK is closed. Cutting this jumper will disable the RTK LED. This LED indicates when there is an RTK fix.
- **GEO:** By default, the GEO is closed. Cutting this jumper will disable the GEO LED. This LED is used for geofencing applications.
- **PPS:** By default, the PPS is closed. Cutting this jumper will disable the PPS LED whenever a position lock has been achieved.
- **SPI:** By default, the SPI is open. Closing SPI with solder enables the SPI interface and disables the UART and I^2^C interfaces. USB will still function.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Bottom_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Bottom_Jumpers.jpg)

**Note:** The MEAS jumper has PTH pins. You will need to disconnect the PTH pads on the top side of the board before you are able to measure the current from the bottom of the board effectively.

### Control Pins

These pins are used for various extra control of the ZED-F9P:

- **TX READY:** Transmit ready output pin. Can be configured using U-Center to indicate that the transmit buffer is full and ready to be transmitted. This is connected to D0 on the MicroMod Processor Board.
- **ZED RESET:** Reset input pin. Pull this line low to reset the module.
- **SFBOOT:** Safeboot input pin. This is required for firmware updates to the module and generally should not be used or connected.
- **INT:** Interrupt input/output pin. Can be configured using U-Center to bring the module out of deep sleep or to output an interrupt for various module states.
- **PPS:** Pulse-per-second output pin. Begins blinking at 1Hz when module gets basic GPS/GNSS position lock.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Control_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/17722-SparkFun_MicroMod_GNSS_Carrier_Board_ZED-F9P_Control_Pins.jpg)

**Note:** For those that need to connect a SMA connector to the PPS pin, the RTK-SMA includes a footprint so that you can [manually solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the connector to the board for your application. The PPS output is helpful as a clock source correction when synchronizing equipment (not 1 Hz but in many MHz). The PPS output can be configured to output a very accurate clock which scientists use to correct less accurate, but much faster clocks. To configure, you can use the u-center to adjust The NEO-F9P\'s setting under **View** \> **Conviguration View** \> **TP (TimePulse)**.\
\

[![SMA Connector](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/1/4/00593-SMA_Connector-01.jpg)](https://www.sparkfun.com/sma-connector.html)

### [SMA Connector](https://www.sparkfun.com/sma-connector.html) 

[ WRL-00593 ]

PCB edge mount - SMA RF connector. Perfect for prototyping with the GPS and Cellular devices that require an antenna connecti...

[ [\$2.75] ]

### Hardware Pinout

- [GNSS ZED-F9P Carrier Pinout Table](#ZED-F9P)
- [MicroMod General Pinout Table](#MMGen)
- [MicroMod General Pin Descriptions](#MMDescript)

**AUDIO**

**UART**

**GPIO/BUS**

**I^2^C**

**SDIO**

**SPI**

**Dedicated**

+-----------------------------------------------------------+---------+------------+---------------------------------------------------------------+
| Function                                                  | Bottom\ |    Top   \ | Function                                                      |
|                                                           | Pin     | Pin        |                                                               |
+==========+==========+===========+=========================+=========+============+====================================+=========+===========+====+
|          |          |           | (Not Connected)         |         | **75**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V                    | **74**  | **73**     | G5 / BUS5                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | RTC_3V_BATT             | **72**  | **71**     | G6 / BUS6                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI_CS1#  | SDIO_DATA3 (I/O)        | **70**  | **69**     | G7 / BUS7                          |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | SDIO_DATA2 (I/O)        | **68**  | **67**     | G8                                 |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | SDIO_DATA1 (I/O)        | **66**  | **65**     | G9                                 | ADC_D-  | CAM_HSYNC |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI_CIPO1 | SDIO_DATA0 (I/O)        | **64**  | **63**     | G10                                | ADC_D+  | CAM_VSYNC |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI COPI1 | SDIO_CMD (I/O)          | **62**  | **61**     | SPI_CIPO (I)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SPI SCK1  | SDIO_SCK (O)            | **60**  | **59**     | SPI_COPI (O)                       | LED_DAT |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | AUD_MCLK (O)            | **58**  | **57**     | SPI_SCK (O)                        | LED_CLK |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| CAM_MCLK | PCM_OUT  | I2S_OUT   | AUD_OUT                 | **56**  | **55**     | SPI_CS#                            |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| CAM_PCLK | PCM_IN   | I2S_IN    | AUD_IN                  | **54**  | **53**     | I2C_SCL1 (I/O)                     |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| PDM_DATA | PCM_SYNC | I2S_WS    | AUD_LRCLK               | **52**  | **51**     | I2C_SDA1 (I/O)                     |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
| PDM_CLK  | PCM_CLK  | I2S_SCK   | AUD_BCLK                | **50**  | **49**     | BATT_VIN / 3 (I - ADC) (0 to 3.3V) |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G4 / BUS4               | **48**  | **47**     | PWM1                               |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G3 / BUS3               | **46**  | **45**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G2 / BUS2               | **44**  | **43**     | CAN_TX                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G1 / BUS1               | **42**  | **41**     | CAN_RX                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | G0 / BUS0               | **40**  | **39**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | A1                      | **38**  | **37**     | USBHOST_D-                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | GND                     | **36**  | **35**     | USBHOST_D+                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | A0                      | **34**  | **33**     | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | PWM0                    | **32**  | **31**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **30**  | **29**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **28**  | **27**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **26**  | **25**     | Module Key                         |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | Module Key              | **24**  | **23**     | SWDIO                              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | UART_TX2 (O)            | **22**  | **21**     | SWDCK                              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | UART_RX2 (I)            | **20**  | **19**     | UART_RX1 (I)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | CAM_TRIG  | D1                      | **18**  | **17**     | UART_TX1 (0)                       |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_INT#                | **16**  | **15**     | UART_CTS1 (I)                      |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_SCL (I/0)           | **14**  | **13**     | UART_RTS1 (O)                      |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | I2C_SDA (I/0)           | **12**  | **11**     | BOOT (I - Open Drain)              |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | D0                      | **10**  | **9**      | USB_VIN                            |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          | SWO       | G11                     | **8**   | **7**      | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | RESET# (I - Open Drain) | **6**   | **5**      | USB_D-                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V_EN                 | **4**   | **3**      | USB_D+                             |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+
|          |          |           | 3.3V                    | **2**   | **1**      | GND                                |         |           |    |
+----------+----------+-----------+-------------------------+---------+------------+------------------------------------+---------+-----------+----+

+-----------------------------------------------------------+---------+------------+--------------------------------------------------+
| Function                                                  | Bottom\ |    Top   \ | Function                                         |
|                                                           | Pin     | Pin        |                                                  |
+=========================================+=================+=========+============+========+=========================================+
|                                         | (Not Connected) |         | **75**     | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | 3.3V            | **74**  | **73**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | RTC_3V          | **72**  | **71**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **70**  | **69**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **66**  | **65**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **64**  | **63**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **62**  | **61**     | TXO    | SDO                                     |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **60**  | **59**     | RXI    | SDI                                     |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **58**  | **57**     | SCL    | SCK                                     |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **56**  | **55**     | SDA    | [CS] |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **54**  | **53**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **52**  | **51**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **50**  | **49**     | VIN/3  |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **48**  | **47**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **46**  | **45**     | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **44**  | **43**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **42**  | **41**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
| D2                                      | G0              | **40**  | **39**     | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | A1              | **38**  | **37**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | GND             | **36**  | **35**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | A0              | **34**  | **33**     | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **32**  | **31**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **30**  | **29**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **28**  | **27**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **26**  | **25**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **24**  | **23**     | SWDIO  |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | RXI2            | **22**  | **21**     | SWDCK  |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | TXO2            | **20**  | **19**     | TXO    | SDO                                     |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | D1              | **18**  | **17**     | RXI    | SDI                                     |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | INT             | **16**  | **15**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
| SCK                                     | SCL             | **14**  | **13**     |        |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
| [CS] | SDA             | **12**  | **11**     | BOOT   |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | TX_READY        | **10**  | **9**      | VIN    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         |                 | **8**   | **7**      | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | RESET           | **6**   | **5**      | USB_D- |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | 3.3V_EN         | **4**   | **3**      | USB_D+ |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+
|                                         | 3.3V            | **2**   | **1**      | GND    |                                         |
+-----------------------------------------+-----------------+---------+------------+--------+-----------------------------------------+

Signal Group

Signal

I/O

Description

Voltage

Power

3.3V

I

3.3V Source

3.3V

GND

Return current path

0V

USB_VIN

I

USB VIN compliant to USB 2.0 specification. Connect to pins on processor board that require 5V for USB functionality

4.8-5.2V

RTC_3V_BATT

I

3V provided by external coin cell or mini battery. Max draw=100μA. Connect to pins maintaining an RTC during power loss. Can be left NC.

3V

3.3V_EN

O

Controls the carrier board\'s main voltage regulator. Voltage above 1V will enable 3.3V power path.

3.3V

BATT_VIN/3

I

Carrier board raw voltage over 3. 1/3 resistor divider is implemented on carrier board. Amplify the analog signal as needed for full 0-3.3V range

3.3V

Reset

Reset

I

Input to processor. Open drain with pullup on processor board. Pulling low resets processor.

3.3V

Boot

I

Input to processor. Open drain with pullup on processor board. Pulling low puts processor into special boot mode. Can be left NC.

3.3V

USB

USB_D±

I/O

USB Data ±. Differential serial data interface compliant to USB 2.0 specification. If UART is required for programming, USB± must be routed to a USB-to-serial conversion IC on the processor board.

USB Host

USBHOST_D±

I/O

For processors that support USB Host Mode. USB Data±. Differential serial data interface compliant to USB 2.0 specification. Can be left NC.

CAN

CAN_RX

I

CAN Bus receive data.

3.3V

CAN_TX

O

CAN Bus transmit data.

3.3V

UART

UART_RX1

I

UART receive data.

3.3V

UART_TX1

O

UART transmit data.

3.3V

UART_RTS1

O

UART ready to send.

3.3V

UART_CTS1

I

UART clear to send.

3.3V

UART_RX2

I

2nd UART receive data.

3.3V

UART_TX2

O

2nd UART transmit data.

3.3V

I2C

I2C_SCL

I/O

I^2^C clock. Open drain with pullup on carrier board.

3.3V

I2C_SDA

I/O

I^2^C data. Open drain with pullup on carrier board

3.3V

I2C_INT#

I

Interrupt notification from carrier board to processor. Open drain with pullup on carrier board. Active LOW

3.3V

I2C_SCL1

I/O

2nd I^2^C clock. Open drain with pullup on carrier board.

3.3V

I2C_SDA1

I/O

2nd I^2^C data. Open drain with pullup on carrier board.

3.3V

SPI

SPI_COPI

O

SPI Controller Output/Peripheral Input.

3.3V

SPI_CIPO

I

SPI Controller Input/Peripheral Output.

3.3V

SPI_SCK

O

SPI Clock.

3.3V

SPI_CS#

O

SPI Chip Select. Active LOW. Can be routed to GPIO if hardware CS is unused.

3.3V

SPI/SDIO

SPI_SCK1/SDIO_CLK

O

2nd SPI Clock. Secondary use is SDIO Clock.

3.3V

SPI_COPI1/SDIO_CMD

I/O

2nd SPI Controller Output/Peripheral Input. Secondary use is SDIO command interface.

3.3V

SPI_CIPO1/SDIO_DATA0

I/O

2nd SPI Peripheral Input/Controller Output. Secondary use is SDIO data exchange bit 0.

3.3V

SDIO_DATA1

I/O

SDIO data exchange bit 1.

3.3V

SDIO_DATA2

I/O

SDIO data exchange bit 2.

3.3V

SPI_CS1/SDIO_DATA3

I/O

2nd SPI Chip Select. Secondary use is SDIO data exchange bit 3.

3.3V

Audio

AUD_MCLK

O

Audio master clock.

3.3V

AUD_OUT/PCM_OUT/I2S_OUT/CAM_MCLK

O

Audio data output. PCM synchronous data output. I2S serial data out. Camera master clock.

3.3V

AUD_IN/PCM_IN/I2S_IN/CAM_PCLK

I

Audio data input. PCM syncrhonous data input. I2S serial data in. Camera periphperal clock.

3.3V

AUD_LRCLK/PCM_SYNC/I2S_WS/PDM_DATA

I/O

Audio left/right clock. PCM syncrhonous data SYNC. I2S word select. PDM data.

3.3V

AUD_BCLK/PCM_CLK/I2S_CLK/PDM_CLK

O

Audio bit clock. PCM clock. I2S continuous serial clock. PDM clock.

3.3V

SWD

SWDIO

I/O

Serial Wire Debug I/O. Connect if processor board supports SWD. Can be left NC.

3.3V

SWDCK

I

Serial Wire Debug clock. Connect if processor board supports SWD. Can be left NC.

3.3V

ADC

A0

I

Analog to digital converter 0. Amplify the analog signal as needed to enable full 0-3.3V range.

3.3V

A1

I

Analog to digital converter 1. Amplify the analog signal as needed to enable full 0-3.3V range.

3.3V

PWM

PWM0

O

Pulse width modulated output 0.

3.3V

PWM1

O

Pulse width modulated output 1.

3.3V

Digital

D0

I/O

General digital input/output pin.

3.3V

D1/CAM_TRIG

I/O

General digital input/output pin. Camera trigger.

3.3V

General/Bus

G0/BUS0

I/O

General purpose pins. Any unused processor pins should be assigned to Gx with ADC + PWM capable pins given priority (0, 1, 2, etc.) positions. The intent is to guarantee PWM, ADC and Digital Pin functionality on respective ADC/PWM/Digital pins. Gx pins do not guarantee ADC/PWM function. Alternative use is pins can support a fast read/write 8-bit or 4-bit wide bus.

3.3V

G1/BUS1

I/O

3.3V

G2/BUS2

I/O

3.3V

G3/BUS3

I/O

3.3V

G4/BUS4

I/O

3.3V

G5/BUS5

I/O

3.3V

G6/BUS6

I/O

3.3V

G7/BUS7

I/O

3.3V

G8

I/O

General purpose pin

3.3V

G9/ADC_D-/CAM_HSYNC

I/O

Differential ADC input if available. Camera horizontal sync.

3.3V

G10/ADC_D+/CAM_VSYNC

I/O

Differential ADC input if available. Camera vertical sync.

3.3V

G11/SWO

I/O

General purpose pin. Serial Wire Output

3.3V

### Board Dimension

The board is about 2.24\"x2.60\" and includes four mounting holes on each corner. If you include the length of the connectors sticking out from the edge of the board, the overall size of the board is about 2.52\"x2.60\".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/5/5/1/c/MicroMod_GNSS_Carrier_Board_ZED-F9P.png)](https://cdn.sparkfun.com/assets/e/5/5/1/c/MicroMod_GNSS_Carrier_Board_ZED-F9P.png)

## Hardware Assembly

If you have not already, make sure to check out the [Getting Started with MicroMod: Hardware Hookup](https://learn.sparkfun.com/tutorials/getting-started-with-micromod#hardware-hookup) for information on inserting your Processor Board to your Carrier Board. Just insert the MicroMod Processor Board at an angle of about 25° into the M.2 socket, push down, and secure with the screw.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

October 21, 2020

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

At a minimum, your setup should look like the image below. In this case, we had the MicroMod ESP32 Processor Board secured in the M.2 connector.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_ESP32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_ESP32.jpg)

### GNSS Multi-band Antenna

As stated earlier, you\'ll need a multi-band antenna and a metal ground plate to make the best use of the ZED-F9P. Connect the two SMA connectors together and tighten the nut. You\'ll simply need the nut to be finger tight.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_GNSS_Antenna_SMA.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_GNSS_Antenna_SMA.jpg)

If you're indoors you *must* run a SMA extension cable long enough to locate the antenna where it has a clear view of the sky. That means no trees, buildings, walls, vehicles, or concrete metally things between the antenna and the sky. Be sure to mount the antenna on a 4"/10cm [metal ground plate](https://www.sparkfun.com/products/15004) to increase reception.

[![GPS antenna in grass](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/4/GPS_RTK_Antenna_with_clear_view_of_sky.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/4/GPS_RTK_Antenna_with_clear_view_of_sky.jpg)

Of course, you could also attach the ground plate on a camera tripod. Just make sure to secure it with weights if there are heavy winds when using the ZED-F9P.

[![GPS Antenna with Ground Plane](https://cdn.sparkfun.com//assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-05.jpg)](https://cdn.sparkfun.com//assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-05.jpg)

### USB-C Cable

To program and power the microcontroller, insert the USB-C cable into the USB-C connector labeled as **Processor**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_USB.jpg)

To update the ZED-F9P\'s firmware or configure the module, insert the USB-C cable into the USB-C connector labeled as **u-center**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_U-center_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_U-center_USB.jpg)

You can have both USB cables connected at the same time since there are protection diodes connected on the voltage lines.

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The SparkFun u-blox Arduino library enables the reading of all positional datums as well as sending binary UBX configuration commands over I^2^C. This is helpful for configuring advanced modules like the ZED-F9P but also the NEO-M8P-2, SAM-M8Q and any other u-blox module that use the u-blox binary protocol.

**Note:** We support two versions of the SparkFun u-blox GNSS library. [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) and [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) uses the u-blox Configuration Interface (VALSET and VALGET) to configure the module, instead of the deprecated UBX-CFG messages. For modules like the F9 and M10, we recommend upgrading to [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). However, older modules like the M8 do not support the Configuration Interface. For those you will need to keep using [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) of the library. We will continue to support both.

The SparkFun u-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun u-blox GNSS v3**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) to manually install.

[SparkFun u-blox Arduino Library v3 (ZIP)](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/archive/main.zip)

Once you have the library installed checkout the various Basics examples.

- **Example1:** Read NMEA sentences over I^2^C using u-blox module SAM-M8Q, NEO-M8P, etc
- **Example2:** Parse NMEA sentences using MicroNMEA library. This example also demonstrates how to overwrite the `processNMEA` function so that you can direct the incoming NMEA characters from the u-blox module to any library, display, radio, etc that you prefer.
- **Example3:** Get latitude, longitude, altitude, and satellites in view (SIV). This example also demonstrates how to turn off NMEA messages being sent out of the I^2^C port. You'll still see NMEA on UART1 and USB, but not on I^2^C. Using only UBX binary messages helps reduce I^2^C traffic and is a *much* lighter weight protocol.
- **Example4:** Displays what type of a fix you have the two most common being none and a full 3D fix. This sketch also shows how to find out if you have an RTK fix and what type (floating vs. fixed).
- **Example5:** Shows how to get the current speed, heading, and dilution of precision.
- **Example7:** Demonstrates how to increase the output rate from the default 1 per second to many per second; up to 30Hz on some modules!
- **Example8:** Older modules like the SAM-M8Q utilize an older protocol (version 18) whereas the newer modules like the ZED-F9P depricate some commands using the latest protocol (version 27). This sketch shows how to query the module to get the protocol version.
- **Example9:** u-blox modules use I^2^C address 0x42 but this is configurable via software. This sketch will allow you to change the module's I^2^C address.
- **Example10:** Altitude is not a simple measurement. This sketch shows how to get both the ellipsoid based altitude and the MSL (mean sea level) based altitude readings.
- **Example11:** Sometimes you just need to do a hard reset of the hardware. This sketch shows how to set your u-blox module back to factory default settings.
- **ZED-F9P**
  - **ZED-F9P Example1:** This module is capable of high precision solutions. This sketch shows how to inspect the accuracy of the solution. It's fun to watch our location accuracy drop into the millimeter scale.
  - **ZED-F9P Example2:** The ZED-F9P uses a new u-blox configuration system of VALGET/VALSET/VALDEL. This sketch demonstrates the basics of these methods.
  - **ZED-F9P Example3:** Setting up the ZED-F9P as a base station and outputting RTCM data.
  - **ZED-F9P Example4:** This is the same example as ZED-F9P\'s Example3. However, the data is sent to a serial LCD via I^2^C.

This SparkFun u-blox library really focuses on I^2^C because it\'s faster than serial and supports daisy-chaining. The library also uses the UBX protocol because it requires far less overhead than NMEA parsing and does not have the precision limitations that NMEA has.

## Arduino Examples

### Example 1: Positional Accuracy

As a quick test, we will be using the first example in the **ZED-F9P** folder (located in **File Examples \> SparkFun u-blox GNSS Arduino Library** \> **ZED-F9P** \> **Example1_GetPositionAccuracy**).

If you have not already, select your Board (in this case the **SparkFun ESP32 MicroMod**), and associated COM port. Upload the code to the board and set the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/all#arduino-serial-monitor-windows-mac-linux) to **115200 baud.** Give the ZED-F9P a few minutes to get a satellite lock. The GPS coordinates and the accuracy will be output in the Serial Monitor.

### More Examples!

Now that you got it up and running, check out the other examples located in the ZED-F9P folder!

[SparkFun u-blox GNSS Arduino Library: ZED-F9P](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library/tree/main/examples/ZED-F9P)

Of course, to get the most out of the ZED-F9P, you will need an RTCM correction source. Depending on your setup, you will probably need a second ZED-F9P for a correction source. The following project tutorials allow you to set up the ZED-F9P as a reference station or rover.

[](https://learn.sparkfun.com/tutorials/how-to-build-a-diy-gnss-reference-station)

### How to Build a DIY GNSS Reference Station 

October 15, 2020

Learn how to affix a GNSS antenna, use PPP to get its ECEF coordinates and then broadcast your own RTCM data over the internet and cellular using NTRIP to increase rover reception to 10km!

[](https://learn.sparkfun.com/tutorials/setting-up-a-rover-base-rtk-system)

### Setting up a Rover Base RTK System 

October 14, 2020

Getting GNSS RTCM correction data from a base to a rover is easy with a serial telemetry radio! We\'ll show you how to get your high precision RTK GNSS system setup and running.

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)