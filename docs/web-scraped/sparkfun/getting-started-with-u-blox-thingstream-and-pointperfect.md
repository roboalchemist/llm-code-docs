# Source: https://learn.sparkfun.com/tutorials/getting-started-with-u-blox-thingstream-and-pointperfect

## Introduction

Interested in high precision GNSS without setting up a base station? Try the u-blox Thingstream and PointPerfect via Internet Protocol (IP)! This tutorial will go over how to use an ESP32 microcontroller to connect to u-blox Thingstream and PointPerfect over Internet to push correction data to a high precision GNSS.

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Below is a wishlist of the parts that you need to get started.

### Arduino Microcontroller

You will need a microcontroller capable of connecting to WiFi. We recommend the ESP32. The IoT RedBoard ESP32 is a good start. There is also the Thing Plus - ESP32 for users looking for a smaller development board. Both of built in Qwiic connectors to easily connect to breakout board. For users following the MicroMod route, you could use the MicroMod ESP32 Processor Board.

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![SparkFun MicroMod ESP32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/8/0/16781-SparkFun_MicroMod_ESP32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html)

### [SparkFun MicroMod ESP32 Processor](https://www.sparkfun.com/sparkfun-micromod-esp32-processor.html) 

[ WRL-16781 ]

This board combines Espressif\'s ESP32 with our M.2 connector interface to bring a power-packed processor board into our Micro...

[ [\$19.95] ]

### u-blox High Precision GNSS (HPG) Module

You will need a compatible u-blox High Precision GNSS (HPG) Module capable of using the service. The following have been tested to work with u-blox Thing Stream and PointPerfect.

[![SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/5/2/16481-SparkFun_GPS-RTK-SMA_Breakout_-_ZED-F9P__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html)

### [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html) 

[ GPS-16481 ]

The SparkFun GPS-RTK-SMA raises the bar for high-precision GPS and is the latest in a line of powerful RTK boards featuring t...

[ [\$259.95] ]

[![SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/1/4/15136-SparkFun_GPS-RTK2_Board_-_ZED-F9P__Qwiic_-03.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html)

### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) 

[ GPS-15136 ]

The SparkFun GPS-RTK2 is a powerful breakout for the ZED-F9P module. The ZED-F9P is a top-of-the-line module for GNSS & GPS s...

[ [\$259.95] ]

[![SparkFun MicroMod GNSS Function Board - ZED-F9P](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/3/3/9/ZEDF9P_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-gnss-function-board-zed-f9p.html)

### [SparkFun MicroMod GNSS Function Board - ZED-F9P](https://www.sparkfun.com/sparkfun-micromod-gnss-function-board-zed-f9p.html) 

[ GPS-19663 ]

The SparkFun MicroMod GNSS Function Board takes everything we love about the ZED-F9P module from u-blox and combines it with ...

[\$274.95] [ [\$184.22] ]

[![SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/3/0/17722-SparkFun_MicroMod_GNSS_Carrier_Board__ZED-F9P_-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html)

### [SparkFun MicroMod GNSS Carrier Board (ZED-F9P)](https://www.sparkfun.com/sparkfun-micromod-gnss-carrier-board-zed-f9p.html) 

[ GPS-17722 ]

The SparkFun MicroMod GNSS carrier board has the accuracy of GNSS Real Time Kinematics (RTK) with the flexibility of the Micr...

[ [\$269.95] ]

#### Multi-band Antenna

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

You can use the GPS antenna ground plate to improve your GPS antenna\'s performance. If you are using the [GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106](https://www.sparkfun.com/products/17751), you\'ll need to grab the interface cable. You will also need an adapter depending on the connector that is populated on the GNSS board and the GNSS Antenna.

[![GPS Antenna Ground Plate](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/5/9/3/17519-GPS_Antenna_Ground_Plate-01.jpg)](https://www.sparkfun.com/gps-antenna-ground-plate.html)

### [GPS Antenna Ground Plate](https://www.sparkfun.com/gps-antenna-ground-plate.html) 

[ GPS-17519 ]

Using this simple steel plate effectively improves simple patch antenna performance to near professional level antenna setups...

[ [\$7.25] ]

[![Interface Cable SMA to U.FL - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/2/09145-01b.jpg)](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html)

### [Interface Cable SMA to U.FL - 100mm](https://www.sparkfun.com/interface-cable-sma-to-u-fl.html) 

[ WRL-09145 ]

This is a 4\" connector cable that interfaces U.FL RF connectors to regular SMA connectors. This cable is commonly used to con...

[ [\$5.75] ]

[![Interface Cable - SMA Male to TNC Male (300mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/9/8/0/17833-Interface_Cable_-_SMA_Male_to_TNC_Male__300mm_-01.jpg)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html)

### [Interface Cable - SMA Male to TNC Male (300mm)](https://www.sparkfun.com/interface-cable-sma-male-to-tnc-male-300mm.html) 

[ CAB-17833 ]

This is a 300mm long Male TNC to Male SMA cable. This is an excellent cable for connecting one of our RTK development boards ...

**Retired**

### Accessories

At a minimum, you will need a USB C cable to power and program the boards. Depending on your application, you may want to grab a Qwiic cable to connect to the breakout boards.

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

### Tools

For users using MicroMod, you will need a screw driver to tighten the screw between the processor/function board and carrier board.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

### You Will Also Need

You will also need Internet access and to purchase a pricing plan with the ThingStream PointPerfect Location-as-a-Service over Internet Protocol (IP).

[u-blox Thingstream IoT Location-as-a-Service: PointPerfect Pricing Options](https://portal.thingstream.io/pricing)

**Note:** If you are lucky and received a card insert with your board, there is a special referral/redemption code that is included with the purchase of the HPG board. This provides 1-month of free, unlimited access to Point Perfect for a single device! This **only applies to IP service** and not the L-band service.\
\

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Graphic of card insert (bottom) included with compatible u-blox high precision GNSS modules.](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Front.jpg) | [![Graphic of card insert (top) included with compatible u-blox high precision GNSS modules.](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Back.jpg) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Graphic of card insert (top and bottom) included with compatible u-blox high precision GNSS modules.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

As stated on the [coverage map from u-blox](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.jv0o1vz2wkn3), the service includes homogeneous coverage in the contiguous USA and Europe This includes up to 12 nautical miles (roughly 22 kilometers) off coastlines. Make sure to check back on the u-blox\'s website to see if there is additional coverage in your region. There are additional regions under consideration for the future.

[![PointPerfect Coverage over IP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/pointperfect_auexpansion.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/pointperfect_auexpansion.png)

*PointPerfect Service Coverage as of January 10, 2023. [Map provided courtesy of u-blox](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.jv0o1vz2wkn3). (Click to enlarge)*

### Suggested Reading

If you are using MicroMod, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. We will be using the IoT RedBoard with the ESP32 to connect to the Internet in this tutorial. If you are using another ESP32 development board or WiFi module, make sure to check out its associated tutorial. You may need to install a board definition or a different driver.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide)

### IoT RedBoard ESP32 Development Board Hookup Guide 

Delve into the functionality-rich world of the IoT RedBoard ESP32 Development Board!

Be sure to checkout our [What is GPS RTK?](https://learn.sparkfun.com/tutorials/what-is-gps-rtk) tutorial. Also, make sure to check out your respective breakout boards for more information.

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

[](https://learn.sparkfun.com/tutorials/micromod-gnss-carrier-board-zed-f9p-hookup-guide)

### MicroMod GNSS Carrier Board (ZED-F9P) Hookup Guide 

Easily switch between Processor Boards using the MicroMod ecosystem and get precision down to the diameter of a dime with the ZED-F9P from u-blox using the MicroMod GNSS Carrier Board!

[](https://learn.sparkfun.com/tutorials/micromod-gnss-function-board---zed-f9p-hookup-guide)

### MicroMod GNSS Function Board - ZED-F9P Hookup Guide 

Add millimeter precision location data to your MicroMod project with this guide for the SparkFun MicroMod GNSS Function Board - ZED-F9P.

## Hardware Hookup

**Note:** If you ordered a ZED-F9P breakout, you will need to make sure to [check and update the ZED-F9P module\'s firmware](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver/identifying-current-firmware-version) so that the module can interpret the correction data. We tested it using the \"[ZED-F9P FW 1.00 HPG 1.32](https://www.u-blox.com/en/product/zed-f9p-module).\"

To add GNSS correction data to your high precision GNSS receiver like the ZED-F9P, you can connect any of the serial ports between the two boards. If you are using SPI to connect, just make sure to enable the SPI port by adding a solder jumper to the SPI jumper pads. For an embedded application, we recommend adding an ESP32 to the setup. The ESP32 will allow you to use the Thingstream PointPerfect over Internet Protocol (IP) using MQTT.

Below is one example to connect using the I^2^C port and Qwiic. Simply insert a Qwiic cable between the ZED-F9P and Arduino microcontroller\'s Qwiic connectors. Plug in a compatible antenna with SMA connector to the ZED-F9P. For the ZED-F9P, you will need the multiband antenna that is capable of receiving L1/L2 bands. For boards that have a u.FL connector, make sure use a u.FL to SMA adapter cable. Secure the connection on both antennas using the hex nut until it is finger-tight. For power, we will use a USB-C cable to power the ESP32 development board. You can also use this cable to connect each breakout to your computer when using the u-blox u-center software.

[![ESP32 IoT RedBoard and ZED-F9P w/ u.FL connector connected via Qwiic Cables](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/GNSS__RTK_ESP32_u-blox_ZED-F9P_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/GNSS__RTK_ESP32_u-blox_ZED-F9P_Qwiic.jpg)

For users going the MicroMod route, you will just need to insert the board(s) into the M.2 socket and secure the boards with the screw. Then insert the USB cable and connect a multiband antenna into its respective connector. Note that you may need a second USB C cable to update the firmware on the ZED-F9P. For more information about connecting a MicroMod board to the M.2 connector, make sure to checkout their respective hookup guides.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod GNSS Carrier Board with MicroMod ESP32 GNSS Processor Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/8/7/MicroMod_GNSS_Carrier_Board_ZED-F9P_Processor_USB.jpg)   [![Image of completed MicroMod assembly with GNSS antenna connected.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/1/9/MM_ZED-F9P_FB-Full_Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/1/9/MM_ZED-F9P_FB-Full_Assembly.jpg)
  *MicroMod ESP32 Processor Board inserted into MicroMod GNSS Carrier Board.*                                                                                                                                                                                                                                         *MicroMod ESP32 Processor Board and MicroMod GNSS Function Board (ZED-F9P) inserted into MicroMod Main Board.*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For users with the [GNSS Multi-Band Magnetic Mount Antenna - 5M (SMA)](https://www.sparkfun.com/products/15192) or the [MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://www.sparkfun.com/products/17108), we suggest placing the antenna on the antenna ground plane to improve the GNSS antenna\'s perfomance. Of course, if users received the GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106, there is already a ground plane embedded in the antenna\'s design! Just make sure to secure the adapter cable on the GNSS Multi-Band Surveying Antenna to the SMA connector. When you are ready, mount the antenna to a monopod, tripod, or your preferred surface.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![GNSS Multiband Antenna on a ground plane and secured to a monopod](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/17519-GPS_Antenna_Ground_Plate-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/17519-GPS_Antenna_Ground_Plate-05.jpg)   [![GNSS Multi-Band L1/L2 Surveying Antenna (TNC) - TOP106 with embedded ground plane secured to monopod](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/17587-L1_L2_GNSS_antenna_TOP106-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/17587-L1_L2_GNSS_antenna_TOP106-09.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## u-blox Firmware Update

**Note:** Make sure that you are using a u-blox high precision GNSS (HPG) module that supports the SPARTN formatted corrections (i.e. `UBX-RXM-COR`). At the time of writing, the ZED-F9P supports the SPARTN formatted corrections sent with **FW 1.00 HPG 1.30** and above. We tested using the latest **FW 1.00 HPG 1.32+**. Check your module\'s firmware release notes if you are unsure if the version number supports the SPARTN formatted corrections.

We recommend checking the firmware on your high precision GNSS (HPG) module (in this case, the ZED-F9P). If the firmware is old, you will need to [upgrade the firmware on the HPG module](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver).

[](https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver)

### How to Upgrade Firmware of a u-blox GNSS Receiver 

March 26, 2021

A few steps and you\'ll upgrade to the latest features on a u-blox GNSS receiver.

You can download the latest firmware from u-blox. Below is a link to the ZED-F9P module\'s product page. Click the \"**Documentation & resources**\" tab and look for the latest firmware under the section **Firmware Update**. You may need to hit the **Load more** button a few times before you can see the firmware.

[u-blox: ZED-F9P Module Product Page](https://www.u-blox.com/en/product/zed-f9p-module)

**Note:** At the time of writing, the thingstream and PointPerfect works with the ZED-F9P. Other models with the u-blox F9 engine (such as the ZED-F9R) may work as long as the firmware supports the SPARTN formatted corrections (i.e. `UBX-RXM-COR`). Make sure to check the associated datasheets for your high precision GNSS module for more information.

## u-blox Thingstream Services

There are two key steps to be able to achieve centimeter positioning accuracy using the ZED-F9P through u-blox thingstream and PointPerfect services.

- Register with u-blox Thingstream and sign up for a PointPerfect IP (Internet Provider) plan (data stream)
- Configure the ZED-F9P with encryption key(s) so it can decrypt and use the correction data

By default, the ZED-F9P is configured such that the correction data is passed from a correction source to the ZED using the UART2 interface. However, it is also possible to read the correction data and push (write) it to the ZED using I^2^C. We just need to configure the modules so that the I^2^C port is enabled and set the protocol.

### Thingstream and PointPerfect Services

You will need to use u-blox Thingstream and PointPerfect service.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![u-blox Thingstream Service Logo](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/5/2/u-blox_thingstream.png "Click here to visit the u-blox Thingstream landing page!")](https://www.u-blox.com/en/product/thingstream)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

[Thingstream](https://www.u-blox.com/en/product/thingstream) is u-blox service delivery platform for IoT Communication-as-a-Service, IoT Security-as-a-Service and IoT Location-as-a-Service.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![u-blox Point Perfect GNSS Augmentation Logo](https://cdn.sparkfun.com//assets/learn_tutorials/2/3/5/2/u-blox_pointperfect-gnss-augmentation-ppp.png "Click here to visit the u-blox PointPerfect landing page!")](https://www.u-blox.com/en/product/pointperfect)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[PointPerfect](https://www.u-blox.com/sites/default/files/PointPerfect_ProductSummary_UBX-21024758.pdf) is u-blox GNSS augmentation service which is designed to provide high-precision GNSS corrections to suitable receivers with decimeter-level location accuracy. The following webinar from u-blox has an excellent explanation of the service and how the system works.

PointPerfect data is delivered through Thingstream. The first step is to register with Thingstream and then request an IP plan. You can find the current pricing on [u-blox portal](https://portal.thingstream.io/pricing/). Select **IoT Location-as-a-Service** and then **PointPerfect**.

[![PointPerfect Pricing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/u-blox_IoT_Location-as-a-Service_PointPerfect_IP_Payment_Plans_1-2023.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/u-blox_IoT_Location-as-a-Service_PointPerfect_IP_Payment_Plans_1-2023.JPG)

*PointPerfect pricing (correct at January 9, 2023). (Click to enlarge)*

You may need to [contact u-blox](support@thingstream.io) first, to enable the option to purchase the plan through your Thingstream account.

The **PointPerfect IP** plan provides unlimited access to the correction data stream via Internet Protocol (MQTT).

Once IP permissions are enabled on your Thingstream account, you will be able to add a new IP Location Thing and view its credentials:

- [Login to Thingstream](https://portal.thingstream.io/)
- Select **Location Services** and then **Location Things**
- The **Add Location Thing button** (top right) will allow you to select and activate an IP plan.
- Add **PointPerfect Thing**, enter a name for the thing, and hit the **Create** button.
- Once your IP plan is active, you will be able to monitor your **Activity** and view your **Credentials** via the appropriate tabs.

**Note:** If you are lucky and received a card insert with your board, there is a special referral/redemption code that is included with the purchase of the HPG board. This provides 1-month of free, unlimited access to Point Perfect for a single device! This **only applies to IP service** and not the L-band service.\
\

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Graphic of card insert (bottom) included with compatible u-blox high precision GNSS modules.](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Front.jpg) | [![Graphic of card insert (top) included with compatible u-blox high precision GNSS modules.](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/SparkFun_Card-PointPerfect-Card_Insert_Back.jpg) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Graphic of card insert (top and bottom) included with compatible u-blox high precision GNSS modules.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The steps to active the IP plan with the special redemption code are similar to the process listed above:\
\

- [Login to Thingstream](https://portal.thingstream.io/)
- Select **Location Services** and then **Location Things**
- The **Add Location Thing button** (top right) will allow you to select and activate an IP plan.
- Select the **Use a code** and then **Redeem your Thing**.
- Enter the code provided on the card (under \"Your Referral/Redemption Code:\") into the field and follow the prompts to activate the promotion code.
- Once your IP plan is active, you will be able to monitor your **Activity** and view your **Credentials** via the appropriate tabs.

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

\
If you\'ve never connected an CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

\
The SparkFun u-blox Arduino library enables the reading of all positional datums as well as sending binary UBX configuration commands over I^2^C. This is helpful for configuring advanced modules like the ZED-F9P but also the NEO-M8P-2, SAM-M8Q and any other u-blox module that use the u-blox binary protocol.

**Note:** We support two versions of the SparkFun u-blox GNSS library. [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) and [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) uses the u-blox Configuration Interface (VALSET and VALGET) to configure the module, instead of the deprecated UBX-CFG messages. For modules like the F9 and M10, we recommend upgrading to [Version 3](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3). However, older modules like the M8 do not support the Configuration Interface. For those you will need to keep using [Version 2](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) of the library. We will continue to support both.

The SparkFun u-blox Arduino library can be downloaded with the Arduino library manager by searching \'**SparkFun u-blox GNSS v3**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3) to manually install. Once the library is installed, you can take advantage of the examples for the ZED-F9P. For the scope of this tutorial, we will be using the PointPerfect Client example.

[SparkFun u-blox Arduino Library v3 (ZIP)](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/archive/main.zip)

\

**Note:** Some examples use the \'**MicroNMEA**\' library by **Steve Marple**. Make sure to install the library as well by searching for it in the Arduino library manager. You could also grab the zip here from the [GitHub repository](https://github.com/stevemarple/MicroNMEA) to manually install.\
\

[MicroNMEA Arduino Library (ZIP)](https://github.com/stevemarple/MicroNMEA/archive/master.zip)

## Arduino Example 18: PointPerfect Client

From the menu, select the following: **File** \> **Examples** \> [**SparkFun u-blox GNSS v3** \> **ZED-F9P** \> **Example18_PointPerfectClient**](https://github.com/sparkfun/SparkFun_u-blox_GNSS_v3/blob/main/examples/ZED-F9P/Example18_PointPerfectClient/Example18_PointPerfectClient.ino).

Once open, you will need to adjust the code based on your region, WiFi credentials, and decryption keys. Click on the **secrets.h** tab.

[![Arduino u-blox PointPerfect Client Secrets Tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_u-blox-PointPerfectClient_Secrets_Tab.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_u-blox-PointPerfectClient_Secrets_Tab.JPG)

### Adjust for Region

By default the example is set up for the US SPARTN 1.8 service. To adjust for Europe, simply adjust the topic provided for the `MQTT_TOPIC_SPARTN[]` array.

    language:c
    const char MQTT_TOPIC_SPARTN[]     = "/pp/ip/eu"; // This topic provides the SPARTN corrections for IP only: choice of 

At the time of writing, there were only three options for corrections. To view the available topics, head back to **Location Services** \> **Location Things** and select your Thing. Select the **Topics** tab. There will be a few topics available. Look for your region listed under \"`IP correction topic for _____ region`\" where \"`_____`\" is abbreviation for your region. You can also check out the available MQTT topics from [u-blox PointPerfect documentation](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.2f4n4dlzsc22).

### Add WiFi Credentials Decryption Keys

Enter your WiFi network name and password into the by replacing `<YOUR SSID>` and `<YOUR PASSWORD>`, respectively.

    language:c
    const char ssid[] = "<YOUR SSID>";
    const char password[] =  "<YOUR PASSWORD>";

### Add Decryption Keys

Under **Location Services** \> **Location Things** and select your Thing. Select the **Credentials** tab. There are four arrays that need to be configured. Replace the following values listed below. Note that the values below are listed with respect to thingstream.

- Client ID (e.g. `MQTT_CLIENT_ID[]`)
- Client Key (e.g. `AWS_CERT_PRIVATE[]`)
- Client Certificate (e.g. `AWS_CERT_CRT[]`)
- Root Certificate (e.g. `AWS_CERT_CA[]`)

The Arduino example code lists the Amazon Root Certificate first and the Client Key arrays last. Make sure that you are copying and pasting the values exactly as provided and not missing any characters within the quotes or parentheses.

    language:c
    // <Your PointPerfect Thing> -> Credentials -> Client Id
    static const char MQTT_CLIENT_ID[] = "<ADD YOUR CLIENT ID HERE>";

    // <Your PointPerfect Thing> -> Credentials -> Amazon Root Certificate
    static const char AWS_CERT_CA[] PROGMEM = R"EOF(
    -----BEGIN CERTIFICATE-----
    <ADD YOUR CERTICICATE HERE>
    -----END CERTIFICATE-----
    )EOF";

    // <Your PointPerfect Thing> -> Credentials -> Client Certificate
    static const char AWS_CERT_CRT[] PROGMEM = R"KEY(
    -----BEGIN CERTIFICATE-----
    <ADD YOUR CERTICICATE HERE>
    -----END CERTIFICATE-----
    )KEY";

    // Get this from Thingstream Portal 
    // <Your PointPerfect Thing> -> Credentials -> Client Key
    static const char AWS_CERT_PRIVATE[] PROGMEM = R"KEY(
    -----BEGIN RSA PRIVATE KEY-----
    <ADD YOUR KEY HERE>
    -----END RSA PRIVATE KEY-----
    )KEY";

### Upload Code

When ready, select the correct board definition from the menu (in this case, **Tools** \> **Boards** \> **SparkFun ESP32 IoT RedBoard**). The board definition will depend on the ESP32 development board that you purchased. Then select the correct COM port that the board enumerated to (in this case, it was **COM13**). Hit the upload button.

[![Uploading PointPerfect Client Exampl](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_Upload_Example18.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_Upload_Example18.JPG)

### What You Should See

Open the Arduino Serial Monitor at **115200** baud. The ESP32 will attempt to connect to your WiFi network. You will notice a period every second indicating that it is trying to connect to your WiFi network.

[![ESP32 Arduino Output: Connecting to local WiFi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_ZED-F9P.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_ZED-F9P.JPG)

Type a character to send a character to your Arduino and hit the **Send** button.

[![MQTT/SPARTN Client Started after sending a keyboard character](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_IP_Connected_WiFi_ZED-F9P.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_IP_Connected_WiFi_ZED-F9P.JPG)

If all is well, you should see the following output indicating that the correction data is being received! Data from the subscribed topic will be pushed to the ZED. The output will indicate if the correction data is successfully decrypted for the ZED. Watch the accuracy converge and decrease to a smaller number. Depending on what satellites are in view, it may take a little time before you reach the RTK floating or fixed solution.

[![Decrypted Correction Data Success](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_IP_Subscribe_Broker_ZED-F9P.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_Serial_Output_PointPerfect_IP_Subscribe_Broker_ZED-F9P.JPG)

*Click on the image for a closer look.*

Below is the output once the RTK Fixed Solution was achieved. You will notice that the values converged to a point with a horizontal accuracy of about 14mm! Your accuracy may vary depending on the satellites in view and Internet connection.

[![Converging to a point of 14mm with the RTK Fixed Solution achieved](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/Arduino_Thingstream_PointPerfectIP_ZED_F9P_Converged_RTK_Fixed_Solution.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/Arduino_Thingstream_PointPerfectIP_ZED_F9P_Converged_RTK_Fixed_Solution.JPG)

*Click on the image for a closer look.*

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) and [u-blox Forums](https://portal.u-blox.com/s/) are great places to find and ask for help. For specific questions about the u-blox service, we recommend heading over more to the u-blox Forums.\
\

[Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)   [Log Into u-blox Forums](https://portal.u-blox.com/s/)

### Thingstream PointPerfect Coverage

The PointPerfect GNSS augmentation service is available on a continental scale with seamless coverage in the \"contiguous USA, Canada, Europe, South Korea, and Australia New South Wales and Victoria regions.\" U-blox is continuously expanding their coverage according to market demand.

[![PointPerfect Coverage over IP](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/8/1/pointperfect_auexpansion.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/8/1/pointperfect_auexpansion.png)

*PointPerfect Service Coverage as of January 10, 2023. [Map provided courtesy of u-blox](https://developer.thingstream.io/guides/location-services/pointperfect-service-description#h.jv0o1vz2wkn3). (Click to enlarge)*

As stated earlier, make sure to check back on u-blox\'s website to see if there is additional coverage in your region. Note that while they recently updated the coverage to support South Korea, Canada, and Australia (New South Wales and Victoria regions), it seems to be available over IP only. There are additional regions under consideration for the future but they have not been included yet.