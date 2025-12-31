# Source: https://learn.sparkfun.com/tutorials/re-programming-the-lilytiny--lilytwinkle

## Introduction

The [LilyTiny](https://www.sparkfun.com/products/10899) (and [LilyTwinkle](https://www.sparkfun.com/products/11364)) are both great, low-cost, sew-able microcontrollers for eTextile projects. For most projects that only need to interface to a small number of LEDs or sensors, the LilyTiny is a great option.

[![LilyTiny](https://cdn.sparkfun.com/r/600-600/assets/parts/5/9/9/7/11364-Twinkie-01.jpg)](https://www.sparkfun.com/lilytiny.html)

### [LilyTiny](https://www.sparkfun.com/lilytiny.html) 

[ DEV-10899 ]

The LilyTiny is a tiny little LilyPad board designed to add flashy functionality to your project without taking up a lot of r...

[ [\$6.95] ]

The LilyTiny has 6 petals. Two are reserved for power(+) and ground(-). The other four are general purpose I/O pins (GPIOs). The LilyTiny is pre-loaded with a sample sketch which shows a variety of LED patterns on each of the pins:

- \"breathing\" pattern (pin 0)
- heartbeat pattern (pin 1)
- simple on-off blink (pin 2)
- random fade (pin 3)

**Note:**You can also use this tutorial to reprogram the ATtiny85 on the LilyTwinkle and LilyTwinkle ProtoSnap. The only difference is how the microcontroller is programmed. Each of the four pins are programmed to randomly fade.\
\

[![LilyTwinkle](https://cdn.sparkfun.com/r/600-600/assets/parts/7/0/9/0/11364-Twinkie-01.jpg)](https://www.sparkfun.com/lilytwinkle.html)

### [LilyTwinkle](https://www.sparkfun.com/lilytwinkle.html) 

[ DEV-11364 ]

The LilyTwinkle is a tiny little LilyPad board designed to add some twinkle to your project. Even though it\'s as small as som...

[ [\$6.95] ]

[![LilyTwinkle ProtoSnap](https://cdn.sparkfun.com/r/600-600/assets/parts/7/5/9/3/11590-01.jpg)](https://www.sparkfun.com/lilytwinkle-protosnap.html)

### [LilyTwinkle ProtoSnap](https://www.sparkfun.com/lilytwinkle-protosnap.html) 

[ DEV-11590 ]

The ProtoSnap series is a new way to prototype your project without a breadboard. Everything is wired together on a single bo...

**Retired**

This is a great place to start, but the only way to re-program one of these boards is to use an [AVR Programmer](https://www.sparkfun.com/products/9825) and an [ISP Pogo Pin Adapter](https://www.sparkfun.com/products/11591) to connect to the 6 exposed pins on the bottom of the LilyTiny board.

This is okay if you haven\'t already sewn your board into your project. If you have, we can still re-program your board. This tutorial will show you exactly how to accomplish this.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

- 1x [8-Pin SOIC IC Test Clip](https://www.sparkfun.com/products/13153)
- 8x [Male to Female Jumper Wires](https://www.sparkfun.com/products/9385)
- 1x [Tiny AVR ISP Programmer](https://www.sparkfun.com/products/11801)
- 1x [LilyTiny](https://www.sparkfun.com/products/10899) (or [LilyTwinkle](https://www.sparkfun.com/products/11364)) to reprogram. The [Protosnap LilyTwinkle Kit](https://www.sparkfun.com/products/11590) is a great option for beginners!
- *1x [USB Extension Cable](https://www.sparkfun.com/products/13309) (Optional, but recommended)*

[![Tiny AVR Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/1/1/11801-01.jpg)](https://www.sparkfun.com/tiny-avr-programmer.html)

### [Tiny AVR Programmer](https://www.sparkfun.com/tiny-avr-programmer.html) 

[ PGM-11801 ]

The ATtiny45 and 85 are a couple of really cool little MCUs but did you know you can program them in Arduino? That\'s right, n...

[ [\$18.95] ]

[![LilyTiny](https://cdn.sparkfun.com/r/140-140/assets/parts/5/9/9/7/11364-Twinkie-01.jpg)](https://www.sparkfun.com/lilytiny.html)

### [LilyTiny](https://www.sparkfun.com/lilytiny.html) 

[ DEV-10899 ]

The LilyTiny is a tiny little LilyPad board designed to add flashy functionality to your project without taking up a lot of r...

[ [\$6.95] ]

[![IC Test Clip - SOIC 8-Pin](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/2/3/7/13153-01.jpg)](https://www.sparkfun.com/ic-test-clip-soic-8-pin.html)

### [IC Test Clip - SOIC 8-Pin](https://www.sparkfun.com/ic-test-clip-soic-8-pin.html) 

[ COM-13153 ]

This is an IC Test Clip for 8-pin small outline integrated circuits (SOIC). This test clip assures a secure connection to all...

[ [\$41.50] ]

[![Jumper Wires Premium 12\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/8/7/09385-03.jpg)](https://www.sparkfun.com/jumper-wires-premium-12-m-f-pack-of-10.html)

### [Jumper Wires Premium 12\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-12-m-f-pack-of-10.html) 

[ PRT-09385 ]

This is a SparkFun exclusive! These are 12\" long, 26 AWG jumper wires terminated as male to female. Use these to jumper from ...

[ [\$4.95] ]

[![USB Cable Extension - 1.5 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/5/4/13309-01.jpg)](https://www.sparkfun.com/products/13309)

### [USB Cable Extension - 1.5 Foot](https://www.sparkfun.com/products/13309) 

[ CAB-13309 ]

This is a 1.5\' long USB extension cable equipped with type A male connector on one end to plug into your computer and a type ...

**Retired**

There are a couple of ways to re-program your board. We will focus on one of the easiest methods here \-- using the [Tiny AVR Programming stick](https://www.sparkfun.com/products/11801).

[![Tiny AVR Programmer Connected to a ProtoSnap LilyTwinkle\'s ATtiny85 via a SOIC IC Test Clip](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-02.jpg)

*Tiny AVR Programming Stick with Pomona 5250 SOIC Clip used to re-rogram the ATtiny85 on the LilyTwinkle.*

## ATTiny Board Add-On Files

Before we start, we need to setup the Arduino programming environment to handle the ATTiny hardware. The ATTiny is not part of the \"default\" board files that comes with Arduino IDE v1.x. You will need to \"install\" these board files to your Arduino environment in order to re-program your LilyTiny.

📌 **Tip:** For beginners, you can **automatically** install using the Arduino boards manager by following the directions in \"Installing the ATtiny Support in Arduino v1.6.4+.\" The instructions also include information about manually installing the files for older versions of Arduino like the directions provided in this tutorial.\
\

[High-Low Tech: Installing ATtiny Support in Arduino 1.6.4](http://highlowtech.org/?p=1695)

### Manually Installing the ATtiny hardware files

If you prefer to manually install the files, we will first need to install the ATtiny hardware board files. Download the zipped files from the GitHub repository to manually install the files.

[attiny-master (ZIP)](https://github.com/damellis/attiny/archive/master.zip)

Create a folder under your Arduino sketchbook called \"**hardware**.\"

- Locate your Arduino sketchbook folder (you can find its location in the preferences dialog in the Arduino software) - this is typically under **Documents** \> **Arduino**

- Create a new sub-folder called "**hardware**" in the sketchbook folder, if it doesn't exist already.

- Open (unzip) the **attiny-master.zip** file and copy the "**attiny**" folder (not the attiny-master folder) from the unzipped **attiny-master.zip** file to your new "**hardware**" folder.

You should end up with folder structure like **Documents** \> **Arduino** \> **hardware** \> **attiny** that contains the **boards.txt** file and another folder called **variants.h**.

- Restart the Arduino IDE.

- You should see ATtiny entries in the **Tools** \> **Board menu**.

## Tiny AVR Programmer 

### Drivers

Follow the hook-up guide for the Tiny AVR programmer. For Windows / PC users, there are a few driver files that you\'ll need. For Mac / OS X users, the Tiny AVR Programmer should be plug-and-play ready.

[](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide)

### Tiny AVR Programmer Hookup Guide 

October 28, 2013

A how-to on the Tiny AVR Programmer. How to install drivers, hook it up, and program your favorite Tiny AVRs using AVRDUDE!

### Hardware Hookup

While the photos show us using the 4-wire ribbon cables and the straight pin break-away headers to connect the SOIC clip to the Tiny AVR Programmer, we have found that the straight pin break-away headers (or any square pins) do not sit into the Tiny AVR Programmer very well. Instead, we recommend using the [12\" Male-to-Female jumper wires](https://www.sparkfun.com/products/9385) to connect the SOIC clip to the Tiny AVR Programmer.

[![Wires](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/Zoom_of_TinyAVR.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/Zoom_of_TinyAVR.jpg)

Make sure that the left side pins on the programmer are wired to the left side of the clip and the right side pins are wired to the right side of the clip. When you clip this onto the LilyTiny, make sure that the chip is right-side up. There are a few distinguishing marks to identify which way is up. On the programmer, there is a notch where an 8-pin chip would go. This should be up. And, on the LilyTiny, the Lilypad script \"L\" should be on the bottom.

[![Close up of tiny AVR programmer ATtiny85 socket and the LilyPad with an ATtiny85 surface mountfacing the same orientation](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/alignment_up.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/alignment_up.png)

When you are finished connecting the Tiny AVR Programmer to the ATtiny85, it should look similar to the image below.

[![Tiny AVR Programmer Connected to ATtiny85](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/Reprogramming_the_Lily_Tiny-01.jpg)

You are now ready to re-program the LilyTiny or LilyTwinkle! The last step is to insert the Tiny AVR Programmer to your computer\'s USB port to begin programming.

**Tip:** We recommend using a USB extension cable with the Tiny AVR Programmer so you have a little more movement from your computer when re-programming.\
\

[![USB Cable Extension - 1.5 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/5/4/13309-01.jpg)](https://www.sparkfun.com/products/13309)

### [USB Cable Extension - 1.5 Foot](https://www.sparkfun.com/products/13309) 

[ CAB-13309 ]

This is a 1.5\' long USB extension cable equipped with type A male connector on one end to plug into your computer and a type ...

**Retired**

## Test Code - \"Hello World!\"

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

As with nearly every introductory Arduino project, we test our system with a \"blink\" program \-- the equivalent to \"Hello World!\" in most other programming environments. First, we need to make sure the configuration is set properly in the Arduino IDE.

### Step 0 - Open up the Arduino IDE

Open the Arduino IDE if you have not already.

### Step 1 - Setting the Board Type

The LilyTiny has an ATtiny85 microcontroller on it. Change the board type in the Arduino IDE to correspond with this. The ATtiny85 can be set with either a 1 MHz internal clock or an 8 MHz internal clock. Be sure to select 8 MHz. Select: **Tools** \--\> **Board** \--\> **ATtiny85 (internal 8 MHz clock)**

[![Board Selection](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/BoardTypeSetting.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/BoardTypeSetting.jpg)

### Step 2 - Setting the Programmer

Because we are using the Tiny AVR as our programmer, we need the change the default programmer. This settings is also under the **Tools** \> **Programmer** \> **USBtinyISP**.

[![Select Programmer](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/USBtinyISP.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/USBtinyISP.jpg)

### Step 3 - Upload Code

Copy the code below and paste this into your Arduino window.

    language:c
    int blinkPin = 0;
    void setup()
    

    void loop()
    

Click the upload button. You may see a few warning messages such as:

    language:bash
    avrdude: please define PAGEL and BS2 signals in the configuration file for part ATtiny85

You can ignore this one. If everything is working, you should be able to see a blinking LED on GPIO 0 (pin 5 of the ATtiny). This can be on the Tiny AVR Programmer, the ProtoSnap LilyTwinkle Kit, or an LED that is attached to the ATtiny 85.

## Notes on Programming the ATtiny85

The ATtiny85 isn't your everyday Arduino microcontroller. It packs a lot of punch for its small size.

[![ATmega85 Pin Reference](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/7/2/ATTinyPins.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/2/ATTinyPins.png)

The following Arduino commands should be supported:

- [pinMode()](http://arduino.cc/en/Reference/PinMode)
- [digitalWrite()](http://arduino.cc/en/Reference/digitalWrite)
- [digitalRead()](http://arduino.cc/en/Reference/digitalRead)
- [analogRead()](http://arduino.cc/en/Reference/analogRead)
- [analogWrite()](http://arduino.cc/en/Reference/analogWrite)
- [shiftOut()](http://arduino.cc/en/Reference/shiftOut)
- [pulseIn()](http://arduino.cc/en/Reference/pulseIn)
- [millis()](http://arduino.cc/en/Reference/millis)
- [micros()](http://arduino.cc/en/Reference/micros)
- [delay()](http://arduino.cc/en/Reference/delay)
- [delayMicroseconds()](http://arduino.cc/en/Reference/delayMicroseconds)
- [SoftwareSerial](http://arduino.cc/en/Reference/softwareSerial)

All 5 pins are general purpose digital I/Os (GPIO). This means that they can be used with both digitalWrite() and digitalRead().

Pins 0 and 1 support PWM output (analogWrite).

Pins 2, 3, & 4 are tied to A/D on the chip (analogRead).

While the ATtiny85 supports most of the things you need, there are some things it can't do.

### No Hardware Serial (UART)

The ATtiny85 does not have a built in [hardware UART](https://learn.sparkfun.com/tutorials/serial-communication/uarts). If you try to compile any Arduino code with `Serial.begin()` or `Serial.print()` you'll get an error. However, there is a work around for this \-- using Software Serial. This [tutorial](http://projectsfromtech.blogspot.com/2013/06/serial-communication-on-attiny85-with.html) shows an example of how to do this:

[Projects from Tech: Serial Communication on a ATtiny85 with the SoftwareSerial Library](http://projectsfromtech.blogspot.com/2013/06/serial-communication-on-attiny85-with.html)

**Tip:** Looking for a quick reference guide for the ATtiny85? Click on the link below to download an image or PDF version from our resources!\
\

[![ATTiny85 Quick Reference](https://cdn.sparkfun.com/assets/0/4/1/4/a/Tiny_QuickRef_v2_2_1.png)](https://learn.sparkfun.com/resources/96)