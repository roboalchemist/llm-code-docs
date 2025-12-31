# Source: https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis-nano

## Introduction

We like to joke that the [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/products/15443) is a party on the front and all business on the rear! A light weight, 0.8mm thick PCB, with on board lipo-battery charging and a Qwiic connector, this board is easy to implement into very small projects. A dual row of ground connections make it easy to add lots of buttons, LEDs, and anything that requires its own GND connection. At the same time, the board is breadboard compatible if you solder the inner rows of pins. Add into that all the bells and whistles of the Artemis module and you\'ve got one heck of a party going on. Let\'s check it out!

[![SparkFun RedBoard Artemis Nano](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/1/8/15443-SparkFun_RedBoard_Artemis_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html)

### [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html) 

[ DEV-15443 ]

The RedBoard Artemis Nano is a miniature extremely versatile implementation of the Artemis module.

[ [\$19.95] ]

### Required Materials

You\'ll need a USB C cable for programming. Any USB C cable should work including the one that probably came with your phone charger. If you don\'t already have a USB C cable you can pick one up [here](https://www.sparkfun.com/products/15092) or you can get a fancy [reversible one](https://www.sparkfun.com/products/15424).

[![SparkFun RedBoard Artemis Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/8/15443-SparkFun_RedBoard_Artemis_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html)

### [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html) 

[ DEV-15443 ]

The RedBoard Artemis Nano is a miniature extremely versatile implementation of the Artemis module.

[ [\$19.95] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

### Suggested Reading

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

[](https://learn.sparkfun.com/tutorials/designing-with-the-sparkfun-artemis)

### Designing with the SparkFun Artemis 

Let\'s chat about layout and design considerations when using the Artemis module.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

## Hardware Overview

### Power, GPIOs and GND Connections

The Nano breaks out 17 GPIO to PTH holes. Each GPIO is paired with a ground connection. We found the extra grounds immeasurably useful when wiring up projects; you\'ll often need a separate ground for each LED, button, or sensor. The Nano makes it that much easier to prototype an idea.

⚡ **Warning:** All pins are **3.3V**. DO NOT expose the pins to 5V.\
\
The Nano *is* breadboard compatible if you solder headers into only the inner rows of PTH holes. This will give your breadboard access to all GPIO, RST, 3.3V, VIN, and 1 ground pin.

[![Pin Rails on the front and back of the Artemis Nano](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-GPIO_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-GPIO_Pins.jpg)

Power is automatically selected between USB, LiPo, and Vin (Vin takes precedence). The VIN pin can handle up to **6V** and will be regulated down to 3.3V using the AP2112 voltage regulator (600mA max output). The **3.3V** pin can be used to power various 3.3V devices up to 600mA.

[] **Advanced Trick:** If you need two more GPIO the Qwiic connector can be used to gain access to D17 and D18.

### USB C and Serial Bootloading

We\'ve designed the Nano with a reversible USB C connector and the CH340E USB to serial IC. This is an amazing IC that is small enough to fit under the USB C connector.

[![SparkFun Artemis Nano with USB highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-USB-to-Serial_USBC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-USB-to-Serial_USBC.jpg)

The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

The current USB C configuration is with two 5.1k Ohm resistors. This will allow up to 2 amps at 5 volts from your USB source. Nearly all modern computers and battery packs have short circuit protection but just be aware that the Nano does not have any short circuit protection.

⚡ **Warning:** The Nano **does not** have a resettable fuse. In the rare event that your design shorts out the board may begin to consume more than 2 amps causing damage to the board or to your USB source.

### JTAG Programming

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/RedBoard-Nano-JTAG.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/RedBoard-Nano-JTAG.jpg)

*JTAG Connection*

An unpopulated JTAG footprint is available for more advanced users who need breakpoint level debugging. We recommend checking out our [JTAG section](https://www.sparkfun.com/categories/tags/jtag) for the compatible male header and a compatible JTAG programmer and debugger.

### Reset and Power Control

The Nano is a great device to embed in a project. But if it\'s embedded, it is often impossible to access the reset and power switches on a board. We\'ve exposed the reset pin and a *Power Switch* pin. This is a perfect place to solder a big external power switch. The **PSWC** pin controls the enable line on the 3.3V regulator. Pull this line low and the board will turn off. Release the PSWC line and the board will run normally. The enable line is pulled high with a resistor so if you don\'t hookup anything the board will operate normally.

[![SparkFun Artemis reset and power switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-Reset_And_Power_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-Reset_And_Power_Switch.jpg)

### RTC and PDM Microphone

The Artemis has built in RTC capabilities if it is given a 32kHz source so we\'ve added a 32kHz crystal to the Nano. Additionally, one of the main applications of the Artemis is voice recognition so we\'ve added a MEMS digital PDM microphone to the board so that you can capture and analyze audio.

[![SparkFun Artemis Nano mic and RTC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-RTC_MicroPhone.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-RTC_MicroPhone.jpg)

### LiPo Battery and Charging

The Nano has integrated LiPo power and charging. Any one of our [LiPo batteries](https://www.sparkfun.com/categories/54) with work great with the Nano. The *CHG* LED will illuminate while the battery is charging via USB and will turn off when the battery is at peak voltage. Charge rate is set to 500mA. The general rule of thumb is charge no faster than 1C so the minimum recommended battery size is a 500mAh battery, but any of the larger batteries will work just fine.

[![LiPo Battery and Charging highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-JSTConnector_ChargeLED_ChargeCircuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/2/6/15443-SparkFun-Artemis-Nano-JSTConnector_ChargeLED_ChargeCircuit.jpg)

## Software Setup

The RedBoard Artemis Nano runs both Arduino and the more advanced [Ambiq](https://ambiq.com/) HAL/SDK. Checkout these tutorials to get you up and blinking in 5 minutes!

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

June 20, 2019

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

[](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk)

### Using SparkFun Edge Board with Ambiq Apollo3 SDK 

March 28, 2019

We will demonstrate how to get started with your SparkFun Edge Board by setting up the toolchain on your computer, examining an example program, and using the serial uploader tool to flash the chip.

## Troubleshooting

### My Nano is not showing up as a COM port?!

Most Artemis carrier boards use the CH340C IC which is not affected by this issue. This issue is only for the Nano that uses the much smaller CH340E.

[![CH340E showing up as weird USB serial device](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device.jpg)

We\'ve had some issues with the CH340E having an incorrect Vendor ID. If your PC is showing the above as an unknown **USB2.0-Serial** device you may have this issue.

[![CH340E showing VID of 0x9986](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Incorrect_VID_9986.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Incorrect_VID_9986.jpg)

*Device showing Vendor ID of 0x9986 when it should be 0x1A86*

For the Nano we needed to use the much smaller CH340E that has only RTS. The CH340E and RTS work fine to reset the Artemis module and activate the SparkFun variable bootloader with one exception: according to the company when the RTS pin has too much load resistance the IC will enumerate incorrectly with VID 0x9986 (correct VID is 0x1A86). It\'s a very weird failure mode that is not documented. We\'ll be working closely with the CH340 manufacturer WCH to get this resolved on future Nano boards.

There are two solutions if you experience this:

**Option 1:** Unplugging and re-plugging USB will cause the IC to properly enumerate under the correct VID/PID and the drivers will work as expected. This works well if you remember to do it but if you\'re like me, I\'ll forget two weeks from now and wonder why the COM port isn\'t coming up.

**Option 2:** Force Windows to use the correct drivers. WCH (the company behind the CH340) has good drivers but the INF for Windows is expecting the PID of 0x1A86. Here are the steps to make the drivers work even with a VID of 0x9986:

[![Unknown serial device in windows manager](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device.jpg)

Step 1: Step 5: Be sure to download and install the [Windows driver](http://www.wch.cn/downloads/CH341SER_EXE.html) from the WCH website.

Step 2: Open device manager and locate the problem serial device.

[![Update CH340 device driver](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix1.jpg)

Step 3: Right click on the device and update driver

[![Select from available list of drivers](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix2.jpg)

Step 4: Select the driver from the available list of drivers

[![Select ports](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix4.jpg)

Step 5: Navigate to the Ports.

[![Select wch.cn from the mfg list](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix5.jpg)

Step 6: Scroll to the bottom of the manufacturer\'s list and select *wch.cn*. Select CH340 in the right hand window. If you do not see *wch.cn* on the list then download and install the [Windows driver](http://www.wch.cn/downloads/CH341SER_EXE.html) from the WCH website and repeat the above steps.

[![Tell windows you are sure](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix6.jpg)

Step 7: Tell Windows you are sure.

[![COM port is correctly listed](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/3/CH340E_as_a_unknown_serial_device-Fix7.jpg)

Step 8: Verify the COM port is appearing correctly.

Once you have the driver installed for both VIDs you computer will correctly enumerate a COM port regardless of how cranky the CH340E is feeling that day.

As mentioned above, we\'ll get this sorted out with WCH soon.

### Need more help?

**Technical Help**\
\
If your product is still not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\
[**SparkFun Artemis Forums**](https://forum.sparkfun.com/viewforum.php?f=167)