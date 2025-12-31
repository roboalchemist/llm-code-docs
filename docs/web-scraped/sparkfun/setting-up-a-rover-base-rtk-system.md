# Source: https://learn.sparkfun.com/tutorials/setting-up-a-rover-base-rtk-system

## Introduction

This tutorial will walk you through setting up a base and rover so that your rover can have the \~14mm accuracy that surveyors use! This can be useful for all sorts of projects including agriculture, drones, mapping, and even some extreme geocaching.

[![ZED-F9P connected via USB to SW Maps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/SWMaps_-_USB_Radio_Combined.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/SWMaps_-_USB_Radio_Combined.jpg)

*The [SW Maps](https://play.google.com/store/apps/details?id=np.com.softwel.swmaps) app for Android connected to a ZED-F9P over USB C using RTK and a serial radio*

We've been using the [ZED-F9P](https://www.sparkfun.com/products/16481) from u-blox for a few years now. While it is a bit pricey (\~\$200) it is a fraction of the cost of other RTK systems ranging from \$3,000 to \$20,000 or more! The ZED-F9P is as impressively powerful as it is configurable. We will also be making liberal use of [u-center](https://www.u-blox.com/en/product/u-center) from u-blox - don't worry, we've got a [tutorial for that](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox/all). Unfortunately u-center is currently only for Windows. For the more adventurous, SparkFun has created a popular and powerful [u-blox Arduino library](https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library) that can do *everything* u-center can from an Arduino.

**Quick note:** You will see the terms *GPS* and *GNSS* used interchangeably throughout this tutorial. GNSS, or Global Navigation Satellite System, is the collective term for all GPS (USA), GLONASS (Russia), BeiDou (China), and Galileo (EU) satellites. GPS was the predominant constellation up to about 2017. After this time enough BeiDou satellites were functional and enough GLONASS satellites were transmitting additional bands (L2, etc) that advanced receivers are now designed to receive signals from a variety of constellations rather than *just* GPS. This is a very good thing. With more satellites and more frequencies we can improve accuracies greatly. Said differently, you don't own a *GPS* receiver, you own a *GNSS* receiver. Congrats!

**Do I really need RTK?**

Great question. With a [ZED-F9P](https://www.sparkfun.com/products/16481) and a [u-blox L1/L2 antenna](https://www.sparkfun.com/products/15192) (and no RTK correction data) we've seen 30 or more satellites and horizontal positional accuracies better than 300mm. This is incredibly precise for a single receiver and should be adequate for many projects. RTK is a challenge to setup but once complete you should be able to obtain an RTK fix which has 14mm of *accuracy* (the precision is sub millimeter). To put the ZED-F9P in perspective, the [SAM-M8Q](https://www.sparkfun.com/products/15210) is a great receiver, but can only receive L1 frequencies and has horizontal accuracy of 2.5m (2500mm). The ZED-F9P is far more accurate.

**Note:** It\'s best to get an RTK system worked out from the comfort of your desk. Don\'t go into the field with a laptop and try to get everything working outside.

### Suggested Reading

Before getting started, be sure you are comfortable with [Getting Started with U-Center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center) and be sure to checkout our [What is GPS RTK?](https://learn.sparkfun.com/tutorials/what-is-gps-rtk) tutorial.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/what-is-gps-rtk)

### What is GPS RTK? 

Learn about the latest generation of GPS and GNSS receivers to get 14mm positional accuracy!

[](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox)

### Getting Started with U-Center for u-blox 

Learn the tips and tricks to use the u-blox software tool to configure your GPS receiver.

[](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

### GPS-RTK2 Hookup Guide 

Get precision down to the diameter of a dime with the new ZED-F9P from u-blox.

## Updating the Receiver Firmware

Please make sure both base and rover receivers have the most up to date firmware from u-blox. As of writing, there has been a new v1.30 firmware release. u-blox provides a simple to use upgrade tool inside of u-center. You can find the latest firmware for all u-blox receivers on their website under the [documentation and resources](https://www.u-blox.com/en/product/zed-f9p-module#tab-documentation-resources) tab. u-blox has been making some good improvements for the ZED-F9P from v1.12, to v1.13, to v1.30. We can now receive from [EGNOS](https://en.wikipedia.org/wiki/European_Geostationary_Navigation_Overlay_Service)!

[![Lots of satellites being received](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Firmware_Version_Update_-_New_EGNOS.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Firmware_Version_Update_-_New_EGNOS.jpg)

*Look at all those satellites!*

[![Checking u-blox firmware version using u-center](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Firmware_Version.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Firmware_Version.jpg)

*Firmware version 1.13*

To check your firmware, open the messages window. Shrink the NMEA branch by double clicking on 'NMEA'. Expand the UBX branch and look for 'MON' or monitor. Expand MON and look for VER (last on the list). FWVER will indicate your current firmware version.

[![Using the firmware update tool in u-center](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/Firmware_Update_-_u-center.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Firmware_Update_-_u-center.jpg)

If you have an older version of firmware download the latest binary from u-blox. Open the Tools-\>Firmware Update menu and follow the prompts. Note: We had to uncheck '*Enter safeboot before update*' to get our module to update.

## Setting Up a Temporary Base

[![GPS RTK antenna on camera tripod](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/1/4/SparkFun_GPS_RTK_Antenna_on_a_camera_tripod.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/4/SparkFun_GPS_RTK_Antenna_on_a_camera_tripod.jpg)

*A basic GNSS antenna on a tripod*

The first step in a base/rover setup is setting up a base station. There are a few ways to set up a base station: a temporary base station is faster but less precise. A static base station takes more time to set up and configure but provides the greatest precision. There is a third option and that is getting your correction data from a public feed. That option is covered in [this tutorial](https://learn.sparkfun.com/tutorials/gps-rtk-hookup-guide/all#connecting-the-gps-rtk-to-a-correction-source) and so we will not cover public correction data in this tutorial.

We've covered setting up a temporary base station in a [previous tutorial](https://learn.sparkfun.com/tutorials/gps-rtk-hookup-guide/all#setting-up-a-base-station) but we will go a bit more in depth here. Additionally, this tutorial will cover the settings required for the ZED-F9P (rather than the previous generation [NEO-M8P](https://www.sparkfun.com/products/15005)).

Above is the u-blox antenna attached to the ground plate, on top of a tripod, with SMA cable running indoors to the receiver. This is a great setup for experimenting and for short trips to the field. The purpose of a GNSS RTK base is to not move. Once you tell a receiver that it is a base station (ie, not moving) it will begin to look at the satellites zooming overhead and calculate its position. As the environment changes the signals from the GNSS (Global Navigation Satellite System - the collective term for GPS, GLONASS, Beidou, Galileo satellites) network change and morph. Because the base knows it is motionless, it can determine the disturbances in the ionosphere and troposphere (as well as other error sources) and begin to calculate the values needed to correct the location that the satellites are reporting to the actual location of the base station. These values are unsurprisingly called 'correction values' and are encoded into a format called RTCM. (RTCM stands for Radio Technical Commission for Maritime but is just a name for a standard akin to "802.11". Don't worry about it.). You will often see the term RTCM3 being used; this is simply correction data being transmitted using version 3 of the RTCM format.

Ok, so how do we set up a base? You'll need the following:

Things you will need:

- A [ZED-F9P receiver](https://www.sparkfun.com/products/16481) with a [USB cable](https://www.sparkfun.com/products/15092) connected to your computer.
- A clear view of the sky. Not indoors, not near a window, outside with nothing around. The accuracy of the entire system depends on the ability to see as many satellites as possible.
- An antenna. We enjoy and promote the use of low-cost antennas and gear. You can easily spend \>\$2,000 on a commercial grade GNSS antenna but we've had great success with the [u-blox L1/L2 antenna](https://www.sparkfun.com/products/15192). You must absolutely have an antenna that is L1/L2 compatible. A simple [magnetic GPS antenna](https://www.sparkfun.com/products/14986) will receive L1 frequencies but RTK will be very inaccurate if it's even possible.
- If your antenna does not have a built in ground plane (the u-blox antenna does not) you will need to add a metal [ground plate](https://www.sparkfun.com/products/15004). A car's roof will act as a ground plate as well.
- A tripod or car roof to mount the antenna. We've found cheap camera tripods work fine. We designed the ground plates to have a compatible 1/4\"-20 hole so they screw directly onto the tripod.
- A way to get the RTCM correction data to the rover: computer with internet connection, serial point to point radio, XBee modules, etc. We will be using the [915MHz Serial Telemetry Radio kit](https://www.sparkfun.com/products/19032).
- An SMA extension cable (\~10m or whatever you need to get from outside to your work computer).

**Note:** The accuracy of the base's location will be reflected in the accuracy of the rover's position. Said differently, if the base is incorrectly recorded 1m away from its actual location than all the rover readings will be exactly 1m wrong. It's really important to locate the antenna with a clear view of the sky and to obtain an accurate base station location.

[![SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/1/4/15136-SparkFun_GPS-RTK2_Board_-_ZED-F9P__Qwiic_-03.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html)

### [SparkFun GPS-RTK2 Board - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk2-board-zed-f9p-qwiic-gps-15136.html) 

[ GPS-15136 ]

The SparkFun GPS-RTK2 is a powerful breakout for the ZED-F9P module. The ZED-F9P is a top-of-the-line module for GNSS & GPS s...

[ [\$259.95] ]

[![SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/5/2/16481-SparkFun_GPS-RTK-SMA_Breakout_-_ZED-F9P__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html)

### [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html) 

[ GPS-16481 ]

The SparkFun GPS-RTK-SMA raises the bar for high-precision GPS and is the latest in a line of powerful RTK boards featuring t...

[ [\$259.95] ]

Once you've got the antenna in place, connect the ZED-F9P to USB and to the antenna. We offer two variants of the Qwiic RTK. If you've got the [SparkFun GPS-RTK2](https://www.sparkfun.com/products/15136) with U.FL antenna connection, you'll need to connect the [U.FL to SMA adapter](https://www.sparkfun.com/products/9145). Here are some good pictures to show you [how to correctly connect a U.FL cable](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl/all). If you've got the [SparkFun GPS-RTK-SMA](https://www.sparkfun.com/products/16481) simply screw the antenna onto the SMA connector.

Open [u-center](https://www.u-blox.com/en/product/u-center) and connect to the corresponding COM port that Windows created when the board was connected.

[![Opening the COM port in u-center](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/5/ublox_module_as_Location_Sensor-6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/5/ublox_module_as_Location_Sensor-6.jpg)

**Having Problems With COM Ports?** Please checkout our [tutorial on u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox) specifically. It will walk you through driver install and determining which COM port is the receiver.

[![u-center with GNSS data](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/u-center_-_initial_data1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_initial_data1.jpg)

You should begin to see things change and data flowing through. Above shows the ZED-F9P running for a few minutes obtaining a heap of satellites and achieving 0.9m horizontal accuracy. Let's open the Messages window and begin configuring the module.

[![Messages window showing many branches](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_CFG_branch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_CFG_branch.jpg)

First, close the NMEA branch to get it out of the way. Open the UBX branch and then the CFG configuration branch. The number of configuration options can be overwhelming at first but over time they can become quite helpful. We are looking for **MSG**.

Take this moment and ask yourself how you will be transmitting the correction data from the base to the rover. The correction data, or RTCM, varies in size but is approximately 1 to 2k bytes per second. Tiny compared to downloading a song or video, but just large enough that LoRa and smaller packet radios may not be able to handle it. We recommend using a [Serial Telemetry Radio](https://www.sparkfun.com/products/19032). Running at 915MHz, these radios can hit \~300m out of the box at 100mW with a 2km/500mW option available as well. The radios act as a transparent serial passthrough at 57600bps (out of the box). We've found them to be just about perfect for Base to Rover RTCM communication with the only limitation being distance. If you need miles of range, you will need to get your HAM radio license and crank the power. But if you're just getting started with RTK, these radios are great!

[![Enabling RTCM messages](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_CFG_branch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_CFG_branch.jpg)

We are going to assume a telemetry radio will be attached to UART2 of the ZED-F9P. From u-center Messages window, enable the following messages for both UART2 and USB.

- RTCM3.3 1005
- RTCM3.3 1074
- RTCM3.3 1084
- RTCM3.3 1094
- RTCM3.3 1124
- RTCM3.3 1230 x 5 (Enable message every 5 seconds)

As you set each setting, you will need to press the 'Send' button. It doesn't hurt to press the 'Poll' button to verify the setting has stuck.

We recommend enabling these messages for both USB and UART2 as shown in the photo. This will tell the module to begin transmitting just these RTCM sentences (message types) once the module has completed its survey. UART2 is best used for sending serial RTCM in/out. USB is enabled so that we will be able to see and verify that RTCM messages are actually being output by the module.

[![Set UART2 baud to 57600bps](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_set_UART2_baud.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_set_UART2_baud.jpg)

Next, set UART2 to the appropriate baud rate. Scroll down to the 'PRT' or port settings. Select UART2. By default it is 38400bps and the radios expect 57600bps. Increase the speed. Remember to press 'Send'.

[![Save settings to BBR/Flash](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_save_configuration.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_save_configuration.jpg)

Now scroll up to the CFG or config option. This menu allows us to save the current settings. When you plug in your module again, you won't have to re-do all these settings. *BBR* is battery backed RAM. There is a small battery on the SparkFun GPS-RTK boards that should maintain the settings for over a week. The *Flash* setting records the settings to flash memory as well so if the battery loses power, flash will maintain the settings (also called non-volatile memory or NVM).

[![Starting the Survey In with settings](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Survey-In.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Survey-In.jpg)

The last thing to do is to initiate a survey in. Navigate to the TMODE3 menu, set the mode to \'1 - Survey-In\', set the observation time to 60s, and required accuracy to 5m. These are the settings that u-blox recommends. Press 'Send' and sit back. It can take many minutes for the module to obtain enough fixes to have a standard deviation less than 5m.

**Note:** You *can* enter the observation time and required accuracy values *then* save the current settings to BBR/Flash. This will effectively tell your module to survey-in at every power-on. This can be handy in many field deployments where u-center is not available but use it with caution. I have been very confused a few times when my device stopped updating its position because I had left it in survey-in mode and didn't realize it.

[![Enable the SVIN message](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_enable_survey_in_message.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_enable_survey_in_message.jpg)

To monitor the status of the survey, scroll down, exiting the CFG section and enter the NAV section. Right click on 'SVIN' and click on *Enable Message*. This will tell the module to send the status of this register every second. Once the module has gotten 60s of data *and* the mean standard deviation is less than 5m then the survey will report 'Complete!'. This module's lat/long/height will no longer change because it has been fixed.

[![Checking the PVT Fix Type](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/u-center_-_Fix_Type_TIME.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Fix_Type_TIME.jpg)

You can verify the survey in is complete by checking the PVT message. If the Fix Type is 'TIME' then you know you have successfully setup a base. Congrats!

[![Viewing the packet console](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_RTCM_messages_in_packet_console.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_RTCM_messages_in_packet_console.jpg)

Furthermore, we can view the RTCM messages. Open the packet console. If the RTCM messages have been enabled *and* the survey-in is complete, we should see the RTCM messages scroll by. **Note:** The RTCM messages are not visible ASCII like NMEA sentences, they are encoded bytes of data. You can\'t \'see\' them in the Text Console but they are shown in the Packet Console.

**What about fast update rates?** The ZED-F9P is capable of outputting up to 30Hz fix rates. This is an astounding amount of math. "Isn't moar, better?"™ Not really for RTK. The base is transmitting correction values once per second. We could increase the output of the module to 4 or 10Hz, but because the conditions between you and the satellites are not changing that quickly, it really only bogs down your radio link.

[![The Radio connected to UART2 of the GPS-RTK-SMA](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/Radio_attached_to_ZED-F9P.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Radio_attached_to_ZED-F9P.jpg)

The last thing we need to do is attach our radio. Cut the 6 pin JST-GH cable that came with the [Serial Radio Telemetry kit](https://www.sparkfun.com/products/19032) in half. Plug the cable into one radio and note where the TX, RX, 5V and GND pins fall. **Go slow**. I wired TX/RX backwards and caused myself an hour's worth of grief. I recommend stripping one wire at a time as this makes it clear which wire I'm working on. Solder the wires as follows:

- Radio 5V - RTK 5V
- Radio TX - RTK RX2
- Radio RX - RTK TX2
- Radio GND - RTK GND

For the advanced readers of this tutorial, go ahead and wire solder the second radio cable to your rover module in *exactly* the same way.

Shown above, I wired the radio to the 6-pin UART2 header. This space is normally used for the 6-pin connection to a Bluetooth module so if you'd like to leave those pins open (for future potential Bluetooth) you can also solder the radio to the TX2/RX2 pins on the side of the GPS-RTK board. We wired the radio to 5V instead of 3.3V on the 6-pin header. We have seen the radios work at 3.3V but a high voltage should get you the maximum transmit distance.

Now is a good time to mark your module with a sharpie or a 'BASE' label so you know which module is which.

### Advanced User Trick

[![Saving a configuration file](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_configuration_file.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_configuration_file.jpg)

Rather than hunting and pecking each individual setting it can be handy to have various configuration files at the ready to configure a given module. Click on Tools-\>Receiver Configuration. This will allow you to save the current configuration to a file and load it onto a new unit. [Here is](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Basic-Survey-In-Config.txt) the survey-in prep configuration that I use (RTCM messages enabled, UART2 set to 57600, no survey-in settings). Save the link as \'survey-in-config.txt\' and load using u-center. Once you load the config be sure to record it to BBR/Flash.

## Rover Setup

We\'re going to assume you\'ve got a base station setup, either as a temporary base or with ECEF coordinates (we'll go into that advanced topic later). u-blox has some good documents on how to set up the ZED-F9P in rover mode but it\'s surprisingly easy. The rover simply needs to be fed RTCM corrections and it will enter RTK Float, then RTK Fix.

Open u-center and connect to the rover module. Multiple instances of u-center can be started if you have multiple modules connected to one computer.

[![Set UART2 baud to 57600bps](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_set_UART2_baud.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_set_UART2_baud.jpg)

Navigate to the CFG / PRT message and configure UART2. We want to set UART2 to 57600bps to match the base and the telemetry radio kit we will be using.

[![Save settings to BBR/Flash](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_save_configuration.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_save_configuration.jpg)

Now save these port settings so they get loaded at each power-on.

**Note:** If you ever run into problems with the configuration of a module you can always select \'Revert to default configuration\' and hit send. This should give your module a good brainwash returning it to the default factory settings. This command will also reset the BBR/Flash settings.

[![Serial Telemetry Radio attached to SparkFun ZED-F9P](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/Radio_attached_to_ZED-F9P.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/Radio_attached_to_ZED-F9P.jpg)

Solder the other half of the radio cable to the UART2 on the rover receiver. The setup is *exactly* the same as before with the base receiver:

- Radio 5V - RTK 5V
- Radio TX - RTK RX2
- Radio RX - RTK TX2
- Radio GND - RTK GND

Time for a test! Power up the rover and base and you should see the green LED on the radios go from blinking to solid indicating the radios detect each other and are passing serial data between them. A blinking red LED on the radios indicates serial data being transmitted.

That's it! This rover module is now ready for the field. It is still recommended to have u-center handy to view the status of the rover as it receives RTCM corrections. As the rover receives RTCM it will quickly move from a 3D fix, to RTK Float, to RTK Fix.

[![u-center showing positional accuracy](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_Positional_Accuracy.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_Positional_Accuracy.jpg)

There are a few messages to watch while the rover achieves RTK Fix. NAV/HPPOSECEF will show overall positional accuracy, NAV/HPPOSLLH will show the horizontal accuracy. NAV/PVT will show the fix type as it progresses from 3D, to RTK Float, to RTK Fixed.

**PSST:** We messed up. The RTK LED on the GPS-RTK boards is wired to ground instead of 3.3V. This means the RTK LED will be on in normal non-RTK mode. Once RTCM is being received and the module enters RTK Float the LED will blink. Once enough corrections are received, the RTK LED will turn off indicating RTK Fixed mode which is the best, 14mm horizontal accuracy situation.

- RTK LED On = Regular Satellite Mode
- RTK LED Blinking = RTK Float, \~\<500mm accuracy
- RTK LED Off = RTK Fix, 14mm acurracy

[![SW Maps app](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/SW_Maps_-_Buffalo_on_Pearl_St.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/SW_Maps_-_Buffalo_on_Pearl_St.jpg) [![SW Maps showing 14mm horizontal accuracy](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/SW_Maps_-_RTK_Fix_on_Pearl_St.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/SW_Maps_-_RTK_Fix_on_Pearl_St.jpg)

*SW Maps is a great way to view and use the positional information from the ZED-F9P*

Once the rover has achieved RTK fixes, what next? The ZED-F9P will be outputting high-precision coordinates UART1 and USB. Any microcontroller that can parse serial can figure out where it is in the world with millimeter accuracy. For surveying applications, we have been blown away with the android app [SW Maps](https://play.google.com/store/apps/details?id=np.com.softwel.swmaps). Made by an impressive team in Nepal, SW Maps is a superb app to connect to ZED-F9Ps and record various GIS and surveying points of interest (POI).

[![Phone connected to ZED-F9P over USB C](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/SW_Maps_-_USBC_Connection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/SW_Maps_-_USBC_Connection.jpg)

Connecting a ZED-F9P to SW Maps is as simple as a [USB C to C](https://www.sparkfun.com/products/16905) cable (assuming your cell phone is USB-C, microB OTG also works). The ZED-F9P will show up as a serial device on Android. SW Maps will connect and display all the position data, RTK status, give the user the ability to record waypoints, tracks, survey information, and notes; perfect for DIY surveying of infrastructure and properties.

In the image above we are using a camera monopod with a bolt on cell phone holder and have been really pleased with the setup (be sure to get a holder capable of 1\" / 27mm diameter in order to bolt to the monopd).

**Note:** If you plan to use SW Maps there are two additional settings that we recommend setting with u-center before going into the field.

1.  Enable GxGST messages

[![Enable GxGST message for USB](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Enable_GST.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Enable_GST.jpg)

*Turning on GxGST for USB interface*

Turning on the GxGST NMEA sentence will transmit the various, lat, long, horizontal, and vertical positional errors. This sentence is needed to see the values in SW Maps GNSS Status window.

[![Enabling SV numbering and high precision NMEA](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/u-center_-_Enable_Extended_NMEA_Settings.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Enable_Extended_NMEA_Settings.jpg)

*Enable High Precision NMEA and SV numbering*

2.  Enable High Precision mode

This will extend the decimals of Lat/Long and setting the Numbering used for SVs will get around a NMEA limit for satellites in view. And High precision NMEA increases the number of decimal places from 5 to 7.

> \$GNGLL,4005.42027,N,10511.08674,W,180753.00,A,D\*63
>
> \$GNGLL,4005.4202248,N,10511.0867652,W,180817.00,A,D\*60

Again, if you plan to use these settings on a regular basis consider saving them to BBR/Flash so that they will be loaded at each power-on.

[![SW Maps built in NTRIP client](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/6/2/SW_Maps_-_NTRIP_Client.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/SW_Maps_-_NTRIP_Client.jpg)

In addition to being able to connect directly to u-blox receivers, when you select a *u-blox RTK* receiver inside SW Maps and connect, you will be able to enable an NTRIP Client. Once logged in to an NTRIP caster, your phone will download the correction data from the server over its cellular connection and pass the RTCM to the GNSS receiver over USB. SW Map is just amazing! Note: In this example we are using the 915MHz Serial Telemetry Radios to transmit the RTCM correction data so you **do not** need to connect an NTRIP Client for corrections\... But you can see where we are headed in the next tutorial!

### Troubleshooting RTCM

[![Viewing RTCM messages from the radio in packet console](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Connecting_directly_to_Radio.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/6/2/u-center_-_Connecting_directly_to_Radio.jpg)

If you're unsure RTCM messages are coming through the RF link, disconnect the JST cable from the radio on the rover and attach a microB USB cable into the 915MHz radio. This will create a COM port. Open u-center and connect to the radio at 57600bps as if it were a GNSS receiver. Then open the packet console. If RTCM messages are being received from the base, u-center will correctly interpret the incoming RTCM messages and display them in the packet console.