# Source: https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun GPS-RTK Dead Reckoning ZED-F9R Hookup Guide

# SparkFun GPS-RTK Dead Reckoning ZED-F9R Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho], [![](https://cdn.sparkfun.com/avatar/5c320824995fcd6990beaf7a3d3f6037?d=retro&s=20&r=pg) Elias The Sparkiest]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1172&name=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1172 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1172&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1172&t=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1172&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F2%2FGPS_ZED-F9R_Orientation_GNSS_2.jpg&description=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Pin It")

## Introduction

The SparkFun GPS ZED-F9R is the next iteration of u-blox\'s GPS offerings! This version takes advantage of dead reckoning for navigation. The u-blox ZED-F9R is a powerful GPS-RTK unit that uses a fusion of IMU, wheel ticks, a vehicle dynamics model, correction data, and GNSS measurements to provide highly accurate and continuous position for navigation in the difficult conditions. We will quickly get you set up using the Qwiic ecosystem through Arduino and Python so that you can start reading the output!

[![SparkFun GPS-RTK Dead Reckoning Breakout - ZED-F9R (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/2/8/5/2/22693-_GPS_SparkFun_RTK_Dead_Reckoning_Breakout_ZED-F9R-_01.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-breakout-zed-f9r-qwiic-gps-22693.html)

### [SparkFun GPS-RTK Dead Reckoning Breakout - ZED-F9R (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-breakout-zed-f9r-qwiic-gps-22693.html) 

[ GPS-22693 ]

The SparkFun ZED-F9R GPS-RTK Breakout is a high precision, Automotive Dead Reckoning board with equally impressive configurat...

[ [\$299.95] ]

[![SparkFun GPS-RTK Dead Reckoning Breakout - ZED-F9R, SMA (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/2/8/1/9/22660-_GPS-_01.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-breakout-zed-f9r-sma-qwiic.html)

### [SparkFun GPS-RTK Dead Reckoning Breakout - ZED-F9R, SMA (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-breakout-zed-f9r-sma-qwiic.html) 

[ GPS-22660 ]

The SparkFun ZED-F9R GPS-RTK Breakout is a high-precision Automotive Dead Reckoning board with equally impressive configurati...

[ [\$299.95] ]

[![SparkFun GPS-RTK Dead Reckoning pHAT for Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/9/6/21305-GPS-RTK-Dead-Reckoning-pHAT-Feature.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-phat-for-raspberry-pi-gps-21305.html)

### [SparkFun GPS-RTK Dead Reckoning pHAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-phat-for-raspberry-pi-gps-21305.html) 

[ GPS-21305 ]

The SparkFun ZED-F9R GPS-RTK pHAT is a high-precision Automotive Dead Reckoning board with equally impressive configuration o...

[ [\$299.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. The wishlist on the left is for the ZED-F9R breakout board. The wishlist on the right includes parts for the ZED-F9R pHAT. Both include parts at a minimum to get the ZED-F9R up and running. Depending on your application, you may need additional parts for a correction source or connecting to you a vehicle to obtain heel tick/direction information. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** For those looking for the bare minimum without a microcontroller, check out the [GPS-RTK Dead Reckoning Kit](https://www.sparkfun.com/products/18294). This includes the GNSS multi-band antenna, USB cable, ZED-F9R breakout board, and u.FL to SMA adapter. We also have the version with the SMA connector as well.\
\

[![SparkFun GPS-RTK Dead Reckoning Kit (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/7/5/7/23452-GPS-RTK-Dead-Reckoning-Kit-Feature.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-kit-sma.html)

### [SparkFun GPS-RTK Dead Reckoning Kit (SMA)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-kit-sma.html) 

[ KIT-23452 ]

The SparkFun GPS-RTK Dead Reckoning Kit provides you with what you need to start with GPS Real Time Kinematics and the u-blox...

[ [\$379.95] ]

[![SparkFun GPS-RTK Dead Reckoning Kit (U.FL)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/5/4/9/KIT-23323-GPS-RTK-Dead-Reckoning-Kit-Feature.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-kit-u-fl.html)

### [SparkFun GPS-RTK Dead Reckoning Kit (U.FL)](https://www.sparkfun.com/sparkfun-gps-rtk-dead-reckoning-kit-u-fl.html) 

[ KIT-23323 ]

The SparkFun GPS-RTK Dead Reckoning Kit gives you just what you need to get started with GPS Real Time Kinematics and the u-b...

**Retired**

#### Microcontroller

**Note:** When this tutorial was originally written, a RedBoard Qwiic with ATmega328P was used. Since then, the Arduino Library has grown. Depending on the sketch (including the Arduino Library version) that you use, you may run the ATmega328P\'s limitations when compiling and uploading. We recommend using a more powerful microcontroller like the **RedBoard IoT - ESP32 Development Board**.

If you are using the breakout board and programming in Arduino, we recommend the IoT RedBoard ESP32 with the associated USB cable to start.

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Reversible USB A to Reversible Micro-B Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/6/15427-Reversible_USB_A_to_Reversible_Micro-B_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-2m.html)

### [Reversible USB A to Reversible Micro-B Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-reversible-micro-b-cable-2m.html) 

[ CAB-15427 ]

These 2m cables have minor, yet genius modifications that allow both ends (the A & Micro-B) to be plugged into their ports re...

[ [\$7.75] ]

### Single Board Computer

If you are using the pHAT and programming in Python, we recommend the desktop kit as it includes all the parts at a minimum to get started. Note that the Raspberry Pi 4 is power hungry so make sure that you have a sufficient power supply when using the GPS remotely. An alternative is using the Raspberry Pi Zero but it\'s not fast as the Raspberry Pi 4.

[![SparkFun Raspberry Pi Zero 2 W Basic Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/2/9/0/RPIKit_1.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-2-w-basic-kit.html)

### [SparkFun Raspberry Pi Zero 2 W Basic Kit](https://www.sparkfun.com/sparkfun-raspberry-pi-zero-2-w-basic-kit.html) 

[ KIT-18735 ]

The SparkFun Raspberry Pi Zero 2 W Basic Kit provides you with everything you need to get started with this successive Pi, al...

[ [\$54.95] ]

[![PiJuice HAT - Raspberry Pi Portable Power Platform](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/6/2/14803-PiJuice_HAT_-_Raspberry_Pi_Portable_Power_Platform-02.jpg)](https://www.sparkfun.com/pijuice-hat-raspberry-pi-portable-power-platform.html)

### [PiJuice HAT - Raspberry Pi Portable Power Platform](https://www.sparkfun.com/pijuice-hat-raspberry-pi-portable-power-platform.html) 

[ PRT-14803 ]

The PiJuice is a fully uninterruptible power supply HAT that will always keep your Raspberry Pi powered.

**Retired**

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

#### Antenna

We recommend using the [multi-band magnetic mount antenna](https://www.sparkfun.com/products/15192) for the full RF reception and mounting it on top of a vehicle. The antenna uses an SMA connector, so make sure to get the u.FL to SMA cable if you decide to use those. Link for that is below in the antenna accessories. The length of the antenna cable was also useful in mounting it.

[![GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/1/15192-GNSS_Multi-band_Magnetic_Mount_Antenna_SMA_-_5m-01.jpg)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html)

### [GNSS L1/L2 Multi-Band Magnetic Mount Antenna - 5m (SMA)](https://www.sparkfun.com/gnss-multi-band-magnetic-mount-antenna-5m-sma.html) 

[ GPS-15192 ]

The ANN-MB-00 GNSS multi-band antenna is extremely unique from other GNSS/GPS antennas in that it is designed to receive both...

[ [\$109.95] ]

[![MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/0/7/0/17108-AA.200_____MagmaX2_Active_Multiband_GNSS_Magnetic_Mount_Antenna-01A.jpg)](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html)

### [MagmaX2 Active Multiband GNSS Magnetic Mount Antenna - AA.200](https://www.sparkfun.com/magmax2-active-multiband-gnss-magnetic-mount-antenna-aa-200.html) 

[ GPS-17108 ]

The AA.200 antenna is an active multiband GNSS magnetic mount antenna that exhibits excellent gain and good radiation pattern...

**Retired**

**Note:** If you want to try different chip antennas, you can try the [GNSS Antenna Evalutation Board](https://www.sparkfun.com/products/15247) listed below and make sure to get the u.FL to u.FL connector in the accessories. However, these antennas will not provide the full RF reception for the ZED-F9R. Additionally, if you are using a GNSS Antennas from the Evaluation Board, you will need to disconnect the inductor on the GPS breakout since they are passive antennas.\
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

[![SparkFun GNSS Chip Antenna Evaluation Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/7/1/2/15247-SparkFun_GNSS_Chip_Antenna_Evaluation_Board-01.jpg)](https://www.sparkfun.com/sparkfun-gnss-chip-antenna-evaluation-board.html)

### [SparkFun GNSS Chip Antenna Evaluation Board](https://www.sparkfun.com/sparkfun-gnss-chip-antenna-evaluation-board.html) 

[ GPS-15247 ]

The SparkFun GNSS Chip Antenna Evaluation Board makes it easy to test out various sized GPS antennas and geometries.

**Retired**

#### GPS Antenna Accessories

Depending on your antenna, you will need an adapter to connect to the GPS-RTK\'s u.FL connector. If you need more than the metal from the top of a vehicle or are mounting it on a robot that does not have the necessary ground plane, you can use the GPS antenna ground plate to improve your GPS antenna\'s performance.

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

#### Other Qwiic Cable Accessories

There are different Qwiic cable lengths available. Depending on your application, you can adjust it to your project\'s specifications.

[![Flexible Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/5/17258-Flexible_Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html)

### [Flexible Qwiic Cable - 200mm](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html) 

[ PRT-17258 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

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

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

**Heads up!** If you are using the [RedBoard **without** a Qwiic connector](https://www.sparkfun.com/products/13975), we recommend getting the Qwiic Shield for Arduino.\
\

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1172&name=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1172 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1172&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1172&t=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1172&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F2%2FGPS_ZED-F9R_Orientation_GNSS_2.jpg&description=SparkFun+GPS-RTK+Dead+Reckoning+ZED-F9R+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/all) [Next Page →\
[What is Dead Reckoning?]](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/what-is-dead-reckoning)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/introduction) [What is Dead Reckoning?](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/what-is-dead-reckoning) [Dead Reckoning Overview](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/dead-reckoning-overview) [Hardware Overview (Breakout)](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/hardware-overview-breakout) [Hardware Assembly (Breakout)](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/hardware-assembly-breakout) [SparkFun u-blox Arduino Library](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/sparkfun-u-blox-arduino-library) [Arduino Example Code](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/arduino-example-code) [Hardware Overview (pHAT)](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/hardware-overview-phat) [Hardware Assembly (pHAT)](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/hardware-assembly-phat) [Configure Your Pi](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/configure-your-pi) [U-Blox Python Package](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/u-blox-python-package) [Python Example Code](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/python-example-code) [Connecting the GPS-RTK to a Correction Source](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/connecting-the-gps-rtk-to-a-correction-source) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/resources-and-going-further)

[Comments [7]](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Navigation](https://learn.sparkfun.com/tutorials/tags/navigation)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]