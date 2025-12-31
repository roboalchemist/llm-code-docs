# Source: https://learn.sparkfun.com/tutorials/using-the-usb-logic-analyzer-with-sigrok-pulseview

## Introduction

An [8-channel, 24MHz USB logic analyzer](https://www.sparkfun.com/products/18627) for under \$20. What a deal!

This USB Logic Analyzer has been updated to a new model with USB-C! If you have the previous version with micro-B, please view [TOL-15033](https://www.sparkfun.com/products/15033); now retired.

[![USB Logic Analyzer - 24MHz/8-Channel](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/1/3/5/18627-USB_Logic_Analyzer_-_24MHz_8-Channel-01.jpg)](https://www.sparkfun.com/usb-logic-analyzer-24mhz-8-channel.html)

### [USB Logic Analyzer - 24MHz/8-Channel](https://www.sparkfun.com/usb-logic-analyzer-24mhz-8-channel.html) 

[ TOL-18627 ]

This 8-channel USB Logic Analyzer with support for sampling rates of up to 24MHz provides a good while economic option making...

[ [\$26.95] ]

But a USB logic analyzer (LA) is only as useful as the software required to configure and monitor the tool. There are a few software options available for this USB logic analyzer; in this tutorial we aim to familiarize you with sigrok\'s PulseView.

[![PulseView](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/PulseView-I2C-Example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/PulseView-I2C-Example.png)

sigrok is an open-source suite of software projects \-- all focused on supporting signal analysis tools. The project includes:

- [PulseView](https://sigrok.org/wiki/PulseView) \-- A logic analyzer front end with a simple GUI.
- [sigrok-cli](https://sigrok.org/wiki/Sigrok-cli) \-- A command line interface for sigrok \-- useful for scripting tests or running on a headless machine.
- [fx2grok](https://sigrok.org/wiki/Fx2grok) \-- A collection of open-source hardware LA layouts, schematics, and BOM\'s.

With an eye towards logic analyzers, this tutorial will focus mostly on PulseView.

## Get the Software

Download the latest PulseView release from [sigrok\'s Downloads page](https://sigrok.org/wiki/Downloads). Here are direct links for the latest Windows, Mac, and Linux downloads:

- [Windows](https://sigrok.org/wiki/Windows#Windows_installers)
- [Mac OS X](https://sigrok.org/wiki/Mac_OS_X)
- [Linux](https://sigrok.org/wiki/Downloads#Binaries_and_distribution_packages)

Windows users can run the installer executable (**pulseview-NIGHTLY-32bit-static-release-installer.exe**) to install the software on your machine. The Mac installer is a binary disk image (**DMG**), which can be dragged into your Applications folder, for example.

**Heads up!** You may need to install drivers before using the USB logic analyzer. If you are using a Windows OS, check out the drivers section:\
\

[Windows Drivers for the USB Logic Analyzer](https://sigrok.org/wiki/Windows#Drivers)

Once installed open PulseView \-- the GUI frontend for sigrok.

## Setting up the Software/Hardware

With PulseView open, plug in your USB Logic Analyzer. You should see faint red and green LEDs illuminate under the sticker.

[![Logic analyzer plugged in](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/IMG_6916-1000w.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/IMG_6916-1000w.JPG)

If PulseView does not automatically detect your logic analyzer, you\'ll need to set it manually:

1.  Click the \"\\\" dropdown menu.
2.  Select **fx2lafw (generic driver for FX2 based LAs)** from the dropdown.
3.  Select USB for the interface
4.  Click **Scan for devices using driver above**
5.  Select \"Logic with 8 channels\" and click \"OK\"

[![Connecting to the USB logic analyzer](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/connect-to-device-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/connect-to-device-2.png)

You\'ll be greeted with a blank slate of eight colorful bands of logic channels, numbered D0 to D7 (these match the CH0-CH7 labels on the LA).

Click the **Run** button in the top-left of the window to beginning scanning.

[![Run button location](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/run-stop.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/run-stop.png)

With the sampling parameters set as default \-- 1M samples, 20kHz \-- it\'ll take almost a minute to gather all million samples. You can hit \"Stop\" to end the scan early.

Unless you\'ve already connected a few channels and grounds, this first scan will probably not be that interesting.

## Exploring the Capabilities

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Here\'s a fun, tormenting Arduino sketch you can load to help familiarize yourself with PulseView\'s capabilities:

    language:c
    void setup() 

    void loop() 

Load that onto an Arduino, then connect the logic analyzers \"CH0\" to your Arduino\'s TX pin (pin 1). Also connect on of the GND wires to GND.

[![Hardware connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/IMG_6914-1000w.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/IMG_6914-1000w.jpg)

Before scanning, bump up the sample rate to **1MHz** and change the sample quantity to **1 M samples**. Depending on what you\'re trying to analyze, these dropdowns may get a lot of use. With those values set, hit **Run**.

You should be greeted with a seconds worth of samples, and a few blips on the D0 channel every 250ms.

[![Results of our mystery baud scan](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/mystery-baud-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/mystery-baud-01.png)

You can use your mouse\'s scroll wheel to zoom in and out, or use the \"+\" and \"-\" buttons on the toolbar. Zoom into one of the blips. Now it\'s your job to guess the baud rate!

The **Show cursors** (pair of blue flags icon) tool can be useful for measuring time. Click that, then try to place the cursors around one bit of the transmission. The measured frequency should be our mystery baud rate!

[![Mystery baud measurement](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/mystery-baud-02-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/mystery-baud-02-2.png)

To decode the string, use the **Add low-level, non-stacked protocol decoder** tool (looks like yellow and green decoded signals). Then select **UART** \-- note that a huge list of protocols pops up here, including I^2^C, I^2^S, SDIO, and SPI.

[![Assortment of protocol analyzers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/protocl-analyzers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/protocl-analyzers.png)

Click the green \"UART\" icon that appears towards the bottom-left and change the baud rate to your measured frequency. You can also change the data format to **ascii** to make the data easier to parse.

[![Decoding the UART traffic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/3/mystery-baud-05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/3/mystery-baud-05.png)

Now if you zoom out you should see your serial prints decoded!