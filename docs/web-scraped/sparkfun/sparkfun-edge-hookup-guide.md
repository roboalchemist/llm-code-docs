# Source: https://learn.sparkfun.com/tutorials/sparkfun-edge-hookup-guide

## Introduction

With the [SparkFun Edge Development Board](https://www.sparkfun.com/products/15170), edge computing is here! You\'ve probably heard of this latest entry to the long lineage of tech buzzwords like \"IoT,\" \"LoRa,\" and \"cloud\" before it, but what is the edge and why does it matter? The cloud is impressively powerful but all-the-time connections require power and connectivity that may not be available. Edge computing handles discrete tasks such as determining if someone said \'start washer\' and responding accordingly. The audio analysis is done at the \"edge\" rather than on the web. This dramatically reduces costs and complexity while limiting potential data privacy leaks.

[![SparkFun Edge Development Board - Apollo3 Blue](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/6/7/15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg)](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html)

### [SparkFun Edge Development Board - Apollo3 Blue](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html) 

[ DEV-15170 ]

The SparkFun Edge Development Board powered by TensorFlow is perfect begin using voice recognition without relying on the ser...

**Retired**

So now that you\'ve embarked upon the journey to the Edge, let\'s take a moment to get off on the right foot. In this hookup guide we will get familiar with the hardware available and how to connect to your computer, then we\'ll point you in the right direction to begin writing awesome applications using machine learning!

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

### Suggested Viewing

## Hardware Overview

### Microcontroller

The Edge uses the Apollo3 Blue - the cutting-edge of high efficiency microcontrollers. This small BGA package *packs* quite a punch!

- 32-bit ARM Cortex-M4F processor with Direct Memory Access
- 48MHz CPU clock, 96MHz with TurboSPOT™
- Extremely low-power usage: 6uA/MHz
- 1MB Flash
- 384KB SRAM

[![Apollo3 IC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Apollo3_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Apollo3_HighRes.jpg)

### Sensors

Such a formidable microcontroller would be wasted without a suite of cool sensors to use with it - that\'s why we\'ve included two microphones, a 3-axis accelerometer, and a camera connector.

#### Microphones

The Edge board contains Micro Electro-Mechanical microphones that are hooked up to an operational amplifier with 75x gain to make the best use of the Apollo3\'s built-in 14-bit analog to digital converter.

The Apollo3 microcontroller can use Direct Memory Access to take audio recordings without using processor cycles - that means you can process audio while you record the next sample!

[![Microphones](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Microphones_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Microphones_HighRes.jpg)

#### Accelerometer

Dynamic interaction with the Edge is included right out of the gate with the onboard ST Microelectronics LIS2DH12 3-axis accelerometer. The accelerometer is on its very own dedicated I^2^C bus so there\'s no need to worry about address conflicts.

[![Accelerometer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Accelerometer_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Accelerometer_HighRes.jpg)

#### [][Camera Connector](#camera)

At the top of the board, we\'ve included a camera connector to connect the Himax CMOS imaging camera.

[![Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/6/5/15570-Himax_Imaging_Camera-01.jpg)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html)

### [Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html) 

[ SEN-15570 ]

An ultra low power CMOS Image Sensor that enables the integration of an "Always On" camera for computer vision applicatio...

[ [\$10.95] ]

[![Camera Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Camera_Connector_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Camera_Connector_HighRes.jpg)

### Connections

If you need anything else to complete your application there are plenty of ways to connect to the Edge board. Among these are the FTDI UART header, a Qwiic connector, four GPIO pins, four LEDs, and last (but not least) a CR2032 coin cell holder.

#### Serial UART Connection

You\'ll use this connector to program the Edge board, but after that you can also use it to talk to other systems that use a UART interface such as [GPS](https://www.sparkfun.com/products/15106) or [Serial LCD](https://www.sparkfun.com/products/14074).

[![Serial UART Header Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_FTDI_Connector_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_FTDI_Connector_HighRes.jpg)

If you connect via UART, you\'ll likely use the CH340E driver. The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

#### Qwiic Connector

The Apollo3 can have up to 6 independent I^2^C ports. We\'ve taken advantage of that fact by exposing a fresh I^2^C port through a Qwiic connector, allowing you to add a chain of I^2^C sensors without soldering.

[![Qwiic Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Qwiic_HighRes.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Qwiic_HighRes.jpg)

#### Bluetooth Radio

The Apollo3 comes with hardware support for a Bluetooth Low-Energy (BLE) radio. The Edge board pairs that up with a surface mount antenna. The BLE controller and host can be configured to support up to eight simultaneous connections \-- security and extended packet length are also supported.

[![Bluetooth Antenna](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Bluetooth_Antenna_HighRes.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_Bluetooth_Antenna_HighRes.jpg)

#### Inputs/Outputs

If all that wasn\'t enough there were still more pins available on the Apollo3, so we broke them out to four LEDs and four GPIO connections along the bottom edge. These are good for addition additional simple input or output capabilities to a project.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_GPIO_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_GPIO_HighRes.jpg)

#### CR2032 Coin Cell Holder

To demonstrate just how efficient this microcontroller is we included a coin cell battery holder on the bottom. That means that once your application is all ready you can take it to school on a key-chain and show it off to your best friend!

[![Coin Cell Holder](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_CoinCell_HighRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_CoinCell_HighRes.jpg)

#### JTAG Connector

For anyone who wants the utmost performance out of the Edge board during the development process you can use the JTAG MIPI 10 standard 1.27mm pitch 2x5 connector to hook up your debugger/programmer.

**Heads up!** You should connect your JTAG programmer/debugger from the bottom (coin-cell) side of the board. Look for a small white bar in silkscreen that indicates pin 1

[![JTAG Connector](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_JTAG.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/15170-Edge_Dev_Board_JTAG.jpg)

### Board Dimensions

SparkFun Edge development board is measures 1.80\"x1.57\" and includes has four mounting holes

[![SparkFun Edge Development Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/EdgeDimensions_Updated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/EdgeDimensions_Updated.png)

*SparkFun Edge Development Board*

## Hardware Hookup

It\'s very easy to get started using the Edge board - all you need to do is provide power! Right off the bat you can try out the AI voice recognition by seeing the yellow LED light up for \'Yes\' and the red LED light up for \'No.\'

### Power + Programming

**Note:** Due to the assembly of these boards, we used **no-clean flux** to reflow the components to the board. What does that mean? Well, it means that the boards are not washed to reduce the possibility of damaging certain components. The flux residue is inactive so it is safe for the board. However, you will need to clean the mound of solder on the pad located under the battery connector in order to make an electrical connection. To remove, you will need a dedicated flux removing solvent and a Q-tip. An alternative to using flux remover is 91% isopropyl alcohol (IPA). With the Q-tip soaked in the solvent, carefully scrub the pad back and forth and clean with the dry tip. Avoid scrubbing at an angle to prevent mechanical stress on the battery connector. To test, grab a [multimeter to test the continuity](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#continuity) of the mound of solder for the battery\'s pad and the GND pin.\
\

![](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue-Isopropyl-Alcohol-Cleaning.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge-Cleaned-Testing.jpg)

[[]](#carousel-6954f844bf49d) [[]](#carousel-6954f844bf49d)

1.  ::: 
    :::

2.  ::: 
    :::

3.  ::: 
    :::

To power the board either place a charged CR2031 3V battery into the coin cell holder or plug in your USB-serial converter.

[![Inserting a Coin Cell Battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/SparkFun_Edge_Development_Board_-_Apollo3_Blue_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge_Development_Board_-_Apollo3_Blue_Hookup_Guide-01.jpg)

If you want to upload new code or see what the Edge board has to say to you then you\'ll need to be able to read the UART pins which are broken out just above the coin cell holder. The pinout is compatible with SparkFun serial breakouts like the [Serial Basic Breakout](https://www.sparkfun.com/products/14050) or the new [Serial Basic Breakout with USB C](https://www.sparkfun.com/products/15096). The ability to toggle the DTR line from USB is required for bootloading.

[![FTDI connector plugged into the Edge Board and powered via USB-C](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/SparkFun_Edge_Development_Board_-_Apollo3_Blue_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge_Development_Board_-_Apollo3_Blue_Hookup_Guide-03.jpg)

⚡ **Warning!** The Edge does not have an onboard regulator to provide **3.3V** and will be damaged if exposed to **5V**. Make sure that your USB-serial bridge is set to output **3.3V** power and logic. Check out the voltage selection jumper in the [Serial Basic Hookup Guide](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide).

With your chosen method of connection at hand begin making the connections with care. If you have USB-serial bridge with the compatible pinout (order DTR, RXI, TXO, VCC, CTS, GND from the perspective of the bridge) you can simply make sure that the GRN and BLK labels match up between the bridge and the Edge board. If you are using some other way to view/send UART data then make sure to connect the TX of the bridge to the RX of the Edge and vice-versa. Also make sure to connect GND (closest to the BLK label on the Edge) and DTR (closest to the GRN label) pins. From the bridge\'s perspective RXI is next to DTR and TXO is next to RXI.

### [][Camera](#insert_camera)

To connect the camera, you\'ll need to carefully slide the flexible ribbon cable connector\'s locking tab out. The locking tab slides out parallel to the board so you\'ll need to push each side of the tab with your fingernails. The image below highlights where you would need to place your fingernails to slide the tab out.

[![Locking Tabs Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Slide_Locking_Tabs_Parallel_to_Edge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Slide_Locking_Tabs_Parallel_to_Edge.jpg)

Once the locking tab is out, you can insert the camera connector into the slot. Face the camera\'s exposed contacts toward the PCB in order to make a connection with the connector\'s pins. Then insert the cable until it is firmly into the connector. Care must be taken to ensure that the ribbon cable does not have any sharp bends when installing the camera.

[![inserting camera module into the camera connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/Himax_CMOS_Imaging_Camera__HM01B0_Inserted_SparkFun_Edge_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Himax_CMOS_Imaging_Camera__HM01B0_Inserted_SparkFun_Edge_Connector.jpg)

When ready, carefully slide the tab back into the locking position using your fingernails.

[![tab locking position](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/Tab_Locking_Position_SparkFun_Edge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Tab_Locking_Position_SparkFun_Edge.jpg)

Your camera should look similar to the images below.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Edge with Camera](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/Top_View_of_Edge_with_Camera.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Top_View_of_Edge_with_Camera.jpg)   [![Bottom View of Edge with Camera](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/Bottom_View_of_Edge_with_Camera.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/Bottom_View_of_Edge_with_Camera.jpg)
  *Top View of Edge with Camera*                                                                                                                                                                                                *Bottom View of Edge with Camera*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Click images for a closer view.*

### Extensions

With the Edge boards you can add additional I^2^C sensors with the Qwiic connector and have access to four GPIO pins.

Connecting Qwiic sensors is as simple as chaining them together with [Qwiic Cables](https://www.sparkfun.com/products/15081) and then linking that chain to the Edge board. Note, if you have many sensors (5 or more is a good rule of thumb) then you\'ll need to disconnect the I^2^C pullup resistors from a few of the boards.

The four available GPIO pins are pads 1, 3, 36, and 38 of the Apollo3. In addition to GPIO functionality some have additional special functions:

  Apollo3 Pad   Special Functions
  ------------- ----------------------------------------------------------------------------------------
  1             UART0 TX
  3             ADC Trigger1
  36            ADC Trigger1, UART1 RX, UART1 CTS, UART0 CTS, PDM Microphone DATA, 32 kHz Clock Output
  38            ADC Trigger3, UART0 CTS, UART1 RX

⚡ **Warning!** The GPIO of the Apollo3 are not **5V** tolerant. To interface with a 5V sensor or controller use a [bi-directional logic level converter](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide).

## Software Setup

### Ambiq Suite SDK

The Edge board takes advantage of the cutting-edge Apollo3 Blue microcontroller from Ambiq for incredibly high efficiency which allows AI applications to run on a coin cell power source. The cost of using the latest and greatest technology. In order to start developing your own applications you\'ll need to follow along with our extensive [Ambiq Apollo3 Software Development Kit Setup Guide](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk).

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

March 28, 2019

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

### Arduino IDE

At the time of writing, support was only provided for the Ambiq Suite SDK. However, support is now included in the Arduino IDE. Check out the following for [Programming the SparkFun Edge with Arduino](https://learn.sparkfun.com/tutorials/programming-the-sparkfun-edge-with-arduino)!

[](https://learn.sparkfun.com/tutorials/programming-the-sparkfun-edge-with-arduino)

### Programming the SparkFun Edge with Arduino 

December 9, 2019

Running low-power machine learning examples on the SparkFun Edge can now be done using the familiar Arduino IDE. In this follow-up to the initial Edge tutorial, we\'ll look at how to get three examples up and running without the need to learn an entirely new SDK.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\
[SparkFun Edge Board Forum](https://forum.sparkfun.com/viewforum.php?f=153)