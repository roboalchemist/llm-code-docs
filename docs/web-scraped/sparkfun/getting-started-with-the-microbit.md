# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit

## Introduction

So you bought this thing called a [micro:bit](https://www.sparkfun.com/products/14208)\...or even better, you\'ve purchased the updated version, the [micro:bit v2](https://www.sparkfun.com/products/17287). But what is it?

[![micro:bit Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/1/4/8/13988-01.jpg)](https://www.sparkfun.com/products/14208)

### [micro:bit Board](https://www.sparkfun.com/products/14208) 

[ DEV-14208 ]

The BBC micro:bit is a pocket-sized computer that lets you get creative with digital technology.

**Retired**

[![micro:bit v2 Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/3/0/7/17287-micro-bit_2.0_Board-01.jpg)](https://www.sparkfun.com/micro-bit-v2-board.html)

### [micro:bit v2 Board](https://www.sparkfun.com/micro-bit-v2-board.html) 

[ DEV-17287 ]

The BBC micro:bit v2 is a pocket-sized computer that has been updated with additional features that let you get creative with...

[ [\$16.50] ]

The BBC micro:bit is a pocket-sized computer that lets you get creative with digital technology. You can code, customize, and control your micro:bit from anywhere! You can use your micro:bit for all sorts of unique creations, from robots to musical instruments and more.

The micro:bit is a project by the BBC in an effort to bring computer science education and STEM topics to every student in the United Kingdom. It is an open development board that works in sync with other onboard hardware components to get you started down the path of programming hardware.

At half the size of a credit card, you will be surprised at the amount of hardware each board is equipped with, including 25 red LED lights that can flash messages. There are two programmable buttons that can be used to control games or pause and skip songs on a playlist. The micro:bit can even detect motion and tell you which direction you're heading. It can also use Bluetooth Low Energy (BLE) to interact with other devices and the Internet.

The micro:bit features an embedded compass, accelerometer, mobile, and web-based programming capabilities. The micro:bit v2 adds an onboard speaker and MEMS microphone, as well as a touch-sensitive logo. Both boards are compatible with a number of online code editors across a number of different languages. This guide will focus on [MakeCode](https://makecode.com), a block or JavaScript-based environment that was developed by Microsoft.

### Required Materials

To follow along with this tutorial, you will only need a micro:bit, and a [micro USB cable](https://www.sparkfun.com/products/10215). Pretty simple!

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

### Suggested Reading

We recommend checking out the tutorials below as well.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/microbit-breakout-board-hookup-guide)

### micro:bit Breakout Board Hookup Guide 

How to get started with the micro:bit breakout board.

## Hardware Overview

There are two versions of the BBC micro:bit and both have a lot to offer when it comes to onboard inputs and outputs. In fact, there are so many things packed onto these little boards that you would be hard pressed to really need anything else if you were looking at just exploring the basics of programming and hardware.

### Front

On the front of the board there are a number of components that are pretty visible right off the bat!

#### **LED Array**

The micro:bit has a 5x5 LED array that you can use as a tiny screen to draw on and display words, numbers and other information.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_LED_Array_Light_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_LED_Array_Light_Sensor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_LEDArray.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_LEDArray.jpg)\

  *LED Array on micro:bit*                                                                                                                                                                                                      *LED Array on micro:bit V2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **A/B Buttons**

Two buttons in all of their clicky glory: A is on the left, B is on the right, and both are prime for controlling a game of your design.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_Buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_Buttons.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_Buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_Buttons.jpg)\

  *A/B Buttons on micro:bit*                                                                                                                                                                      *A/B Buttons on micro:bit V2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **Edge \"Pins\"**

The gold tabs at the bottom of the board are for hooking up external components. The tabs with larger holes can be easily used with [alligator clips](https://www.sparkfun.com/products/12978) to prototype things quickly! To access all the pins, you will need a board with an edge connector. For breadboard prototyping, you\'ll want the [micro:bit breakout with headers](https://www.sparkfun.com/products/16446). In micro:bit v2, you will also notice that they are notched for easier connection with alligator clips.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_Edge_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_Edge_Connector.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_EdgePins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_EdgePins.jpg)\

  *Edge Pins on micro:bit*                                                                                                                                                                                      *Edge Pins on micro:bit V2*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** You can also be creative when connecting to the larger through holes. For certain boards, you can use flat-head or countersunk screws that taper along the shaft, nylon standoffs, and hex nuts to access the through holes. Below is an image with the Micro:bit connecting to the [Kitronik MI:power Board V2](https://www.sparkfun.com/products/17852) with countersunk screws.\
\

  ------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com//assets/parts/1/7/0/3/2/17852-Kitronik_MI-power_Board_V2-08.jpg)](https://www.sparkfun.com/products/17852)   [![](https://cdn.sparkfun.com//assets/parts/1/7/0/3/2/17852-Kitronik_MI-power_Board_V2-05.jpg)](https://www.sparkfun.com/products/17852)
  ------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------

Using countersunk screws is also an alternative to alligator clips that provides a secure connection. For more information, check out this blog post: [micro:bit - Hacking the GPIO - Updated!](https://bigl.es/micro-bit-hacking-the-gpio/)

#### **Light Sensor**

A bit of a hidden gem. The LED array doubles as a light sensor!

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_LED_Array_Light_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-05_micro_bit_Front_LED_Array_Light_Sensor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_LEDArray.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_LEDArray.jpg)\

  *Light Sensor on micro:bit*                                                                                                                                                                                                   *Light Sensor on micro:bit V2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **V2 Only - Microphone Input and LED Indicator**

[![Microphone input and LED indicator is on the right side of the touch sensitive logo at the top of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_MicInputandLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_MicInputandLED.jpg)

#### **V2 Only - Touch Sensitive Logo**

The gold logo is a capacitive touch sensor that works a bit like a touch screen on a mobile phone, measuring tiny changes in electricity.

[![Touch sensitive logo is at the top center of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_TouchSensitiveLogo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Front_TouchSensitiveLogo.jpg)

### Back

The back is where a lot of the magic happens. Check it out\...

#### **Microcontroller**

The brains of the outfit.

The micro:bit is powered by a 16MHz ARM Cortex-M0 microcontroller with 256KB Flash and 16KB RAM.

The micro:bit v2 is powered by Nordic Semiconductor\'s nRF52833 chip - a 64MHz ARM Cortex-M4 microcontroller with FPU, 512KB Flash, and 128KB RAM.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Microcontroller_Temperature_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Microcontroller_Temperature_Sensor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Processor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Processor.jpg)\

  *nRF51822 Processor on micro:bit*                                                                                                                                                                                                                           *nRF52833 Processor on micro:bit V2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **Accelerometer/Compass**

The micro:bit has an onboard accelerometer that measures gravitational force, as well as a compass (a.k.a. a magnetometer) that can detect its orientation using Earth\'s magnetic field.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/14028-micro-bit_Accelereometer_Magnetometer_Sensor-v1_5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/14028-micro-bit_Accelereometer_Magnetometer_Sensor-v1_5.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_AccelCompass.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_AccelCompass.jpg)
  *Accelerometer and Magnetometer on micro:bit*                                                                                                                                                                                                 *Accelerometer and Magnetometer on micro:bit v2*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **Bluetooth/Radio**

Communication is huge with the micro:bit. You can communicate with your phone or tablet using Bluetooth Low Energy (BLE) or between two or more micro:bits using the standard 2.4GHz \"radio\". Note that the micro:bit v1 uses BLE Bluetooth v4.0 while micro:bit v2 uses BLE Bluetooth v5.0.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Antenna.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_BLEAntenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_BLEAntenna.jpg)
  *Bluetooth / Radio Antenna on micro:bit*                                                                                                                                                              *Bluetooth / Radio Antenna on micro:bit v2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **Temperature Sensor**

No, the drawing is not highlighted incorrectly! The microcontroller doubles as a temperature sensor!

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Microcontroller_Temperature_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Microcontroller_Temperature_Sensor.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Processor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Processor.jpg)
  *Microcontroller as Temperature Sensor on micro:bit*                                                                                                                                                                                                        *Microcontroller as Temperature Sensor on micro:bit v2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **USB Port**

Used to upload code to your micro:bit or power from your computer or laptop. You can also send and receive serial data from the MakeCode Serial Console or a Serial Terminal.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_USB_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_USB_Connector.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_USB.jpg)
  *USB Port on micro:bit*                                                                                                                                                                                           *USB Port on micro:bit v2*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **USB Activity LED Indicator**

When there is activity on the USB pins, the LED on the right will light up.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![USB Activity LED Indicator on micro:bit](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-micro-bit_V1-Back_USB__Activity_LED_Indicator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-micro-bit_V1-Back_USB__Activity_LED_Indicator.jpg)   [![USB Activity LED Indicator on micro:bit v2](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/17287-micro-bit2-Back_USB_Activity_LED_Indicator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/17287-micro-bit2-Back_USB_Activity_LED_Indicator.jpg)
  *USB Activity LED Indicator on micro:bit*                                                                                                                                                                                                                                    *USB Activity LED Indicator on micro:bit v2*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### **V2 Only - Power LED**

V2 of the micro:bit also includes a power LED next to the USB connector to indicate power is available.

[![Power LED](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/17287-micro-bit2-Back_Power_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/17287-micro-bit2-Back_Power_LED.jpg)

#### **Reset Button**

A button to reset your micro:bit and start your code over from the beginning.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Reset_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_Reset_Button.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Reset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Reset.jpg)
  *Reset Button on micro:bit*                                                                                                                                                                                     *Reset/ Power Button on micro:bit v2*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** The reset button the micro:bit V2 also functions as a power button to turn the micro:bit \"off\". Technically, it will be in deep sleep mode when holding the button for 5 seconds. For more information, check out the [MakeCode article on the micro:bit V2\'s reset button](https://support.microbit.org/support/solutions/articles/19000106820-reset-the-micro-bit).

#### **JST Battery Connector**

A connector to hook up an external battery pack to your micro:bit.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_JST_Remote_Battery_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-03_microBit_Back_View_JST_Remote_Battery_Power.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Battery.jpg)
  *JST Connector on micro:bit*                                                                                                                                                                                                            *JST Connector on micro:bit v2*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Warning:** JST-PH connectors are usually used with LiPo batteries. These have a different battery chemistry and voltage compared to the batteries used with 2xAA and 2xAAA battery packs. Unless you have a voltage regulator to regulate the LiPo battery\'s voltage, make sure to only use AA or AAA batteries with the micro:bit\'s JST-PH connector.

#### **V2 Only - Microphone**

V2 of the micro:bit contains a MEMS microphone to allow sound-sensing without the need to attach another device. If you look back at the front of the board, you will notice that the microphone input leads to this component on the back.

[![The microphone is on the back of the board, just below and left of the USB port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Microphone.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Microphone.jpg)

#### **V2 Only - Speaker**

V2 of the micro:bit also includes a built-in speaker on the back of the board. For users using an external speaker on the edge pins, you will need to configure the built-in speaker in the programming language of your choice.

[![Speaker is smack center on the back of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Speaker.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/7/17287-micro-bit2-Back_Speaker.jpg)

Phew! That is a lot of bells and whistles\...a true Swiss army knife!

**Note:** Of course, for more in depth information on the hardware, check out the official micro:bit Foundation\'s Hardware Overview in the link below.\
\

[micro:bit Foundation: Hardware Overview](https://tech.microbit.org/hardware/)

## Hooking It Up

The micro:bit uses a microUSB cable to hook up to your computer or Chromebook. It is as simple as plugging the cable into your micro:bit and the other end into an open USB port.

[![USB Between MicroBit and Computer](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/13988-04.jpg)

Once you plug your board in, you should see the small yellow LED on the back of your micro:bit light up and possibly blink a few times. Then whatever existing program that was put on the micro:bit will start running. If this is your first time plugging your micro:bit in, go ahead and play around with it a bit \-\-- push buttons, shake it, and you will get a bit of an Easter egg.

Once your micro:bit boots up, check out your **Finder** if you are on a Mac, or your **My Computer Drives** if you are on a PC. The micro:bit should show up as an external storage device with two files stored in it.

[![MicroBit Showing up as External Storage Device](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-13_at_12.36.48_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-13_at_12.36.48_PM.png)

If you are on a Chromebook, when you plug your micro:bit in you will be greeted with a dialog box to open the drive. Feel free to do so to make sure it works!

Let\'s get programming!

## Using MakeCode

This guide and most of SparkFun\'s content around the micro:bit will use MakeCode by Microsoft for programming.

### What Is MakeCode?

MakeCode is an open programming environment built by Microsoft for the micro:bit, as well as [other boards](https://makecode.com). You can navigate to MakeCode for the micro:bit by following this link:

[Launch MakeCode!](https://makecode.microbit.org/)

Once you have launched MakeCode, you will be greeted by its basic layout with a simulator on the left and a block-based environment on the right when your browser\'s window is maximized, as shown here.

[![MakeCode Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/pxt.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/pxt.jpg)

*Click on the image above for a larger view.*

Let\'s take a quick tour and check out what is available to us!

1.  **Projects** \-\-- A cloud storage system connected to your computer with no account setup required.
2.  **Share** \-\-- Allows you to share your project code in a number of different ways with your friends!
3.  **Blocks/JavaScript/Python** \-\-- Choose your own adventure by programming in blocks (default) or in JavaScript. Not shown in the image, Microsoft also eventually added an additional option to use convert the code to MicroPython.
4.  **Program Space** \-\-- This is where the magic happens and where you build your program\...where you \"make code.\"
5.  **Zoom/Undo-Redo** \-\-- Sometimes you need to undo things, or zoom out and look around; these are the buttons for that.
6.  **Name & Save** \-\-- Name your program and save it (download it) to your computer.
7.  **Download** \-\-- Similar to Save, download your program as a .hex file and drag it into your micro:bit.
8.  **Simulator Hide/Show** \-\-- You can hide/show the simulator if you would like.
9.  **Block Library** \-\-- All of the options in terms of program building blocks, which are color-coded by function.
10. **Simulator** \-\-- You don\'t need hardware! MakeCode has a real-time simulator! As you change your program, you can see what it will do on this virtual micro:bit!

Phew! Now you have a choice - blocks or text-based programming?

### Blocks or Text

For this guide and the majority of the content that you will find on SparkFun for the micro:bit, we will be using block-based programming examples.

[![Toggle Switch for Drag and Drop Programming or JavaScript](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.03.08_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.03.08_PM.png)

But, if you so choose there is a JavaScript (and also MicroPython) option to use as well. The choice is yours, and the good news is that you can switch back and forth from one to the other in the same program; one will populate the other, which is really nice if you are new to programming!

### Simulator

MakeCode includes a simulator for the micro:bit, meaning if you don\'t have your micro:bit in hand you can still write code for it. Or if you want to try out an idea before you upload it to your micro:bit, you can do that too!

[![MakeCode Simulator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/smiley.screenshot.v1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/smiley.screenshot.v1.png)

The simulator will update as you build your code, and if you want to run it from the beginning you can click the stop and run buttons to start it over again!

Speaking of code, let\'s write a quick program and get it onto your micro:bit!

## Hello, World!

Now comes the good stuff \-\-- writing your first program for your micro:bit in the MakeCode programming environment!

*\"Hello World\"* is the term we use to define that first program you write in a programming language or on a new piece of hardware. Essentially it is a simple piece of code that gives you a quick win (fingers crossed) and a first step in learning. It also gives you a chance to make sure everything is up and running and A-OK.

For your first \"Hello World\" we are going to create a simple animation on the LED array that repeats forever. If you just want the complete program, you can see it [here](https://makecode.microbit.org/52659-35804-63742-17414). To see a step-by-step explanation of how we built the program, continue reading!

**Note:** You may need to disable your ad/pop blocker to interact with the MakeCode programming environment and simulated circuit!

### Building \'Hello World\'

A \"Hello World\" on the micro:bit is a little different than on a normal run-of-the-mill microcontroller. The micro:bit has no single LED to blink on its own, as you would find on the Arduino or similar boards. What the micro:bit does have is an LED array! So, the \"Hello World\" for the micro:bit is to draw something using the LED array!

When you open MakeCode you are greeted with two blocks: the `On Start` block and the `forever` block. The `On Start` block is all of your code that will execute at the very beginning of your program and only run once. The `forever` block is code that will loop over and over again\...forever.

We are going to use the `forever` block for building this \"Hello World.\" We now need to start adding blocks to `forever`.

[![forever code block](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-02-13_at_12.36.04_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-02-13_at_12.36.04_PM.png)

First, click on the Basics category. These blocks are, well, the basic building blocks of a BuildCode program. It will expand into a number of options. Click and drag the `show leds` block over and place it inside of your `forever` block. Notice that the block is keyed to fit inside of the `forever` block, and if you have the volume up on your computer you will hear a satisfying \'click\' noise when you let go of the block.

[![Basic Code Blocks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-13_at_12.48.52_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-13_at_12.48.52_PM.png)

The `show leds` block has an array of squares that symbolize the LED array. If you click on a square, it will turn red, which means that it is \'on\'. Draw a simple pixel art shape by turning different LEDs on or off; you should be able to see the outcome in your simulator on the lefthand side of your window.

[![LED Array Code Block with Smiley Face](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_smiley_codeblock.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_smiley_codeblock.png)

To turn this static image into an animation we need another `show leds` block to place just under the first block. You can then make a second drawing with this set of rectangles. In your simulator you will see the images switching really, really fast. We need to slow this down!

To slow your animation down you will use the `pause` block, which is under the basic block set. The `pause` block is just what it says; it tells the micro:bit to pause and wait for a certain amount of time. Place two `pause` blocks in the program as shown.

[![LED Array Code Blocks with Delay Between Animations](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/microbit-screenshot__angry-happy_smiley.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/microbit-screenshot__angry-happy_smiley.png)

The reason we are using two \'pause\' blocks and placing one at the end is that this program is a loop. Without the block at the end, the image in your animation will change really, really fast.

We have built up an example in the next section where you can download the file and try it out on your own micro:bit, or use the simulator. If you want to play around with the code and make some changes, go ahead and click the Edit button in the widget, and it will open a MakeCode editor for you to start hacking \"Hello World.\" Enjoy!

## Getting Your Program Onto Your micro:bit

You\'ve built your first program in MakeCode, and it works in your simulator. Now, how do you get it onto your micro:bit?

### Download Your Program

Once you are happy with your program, you can click the Download button in MakeCode.

[![MakeCode Download Button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.01.48_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.01.48_PM.png)

This will download your program file to your standard download location, probably the **Downloads** folder on your computer, or whatever location you have set in your download preference.

[![Window After Downloading](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.02.11_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Screen_Shot_2017-03-02_at_4.02.11_PM.png)

You then simply click and drag your program file from its download location to your micro:bit drive, which shows up as an external device.

That\'s it!

Your micro:bit will flash for a few seconds, and then your program will start automatically. Yes! Win!

**Note:** You may need to disable your ad/pop blocker to see the simulated circuit!

## MakeCode Extension

**Heads up!** Previously, these libraries were referred to as MakeCode packages. They are now referred to as [MakeCode extensions](https://makecode.com/extensions).

If you have used Arduino before, you probably know about a thing called a library; which is a collection of code that extends the functionality of the core programming language. MakeCode extensions work the same way.

There are some amazing differences between Arduino libraries and MakeCode extensions. One of them is that MakeCode extensions include JavaScript functions, which you can use when programming in text, as well as all of the blocks you need to program using the block method. This makes learning and using new extensions straightforward and shortens the time to awesome when setting out to build the project of your dreams.

There are several MakeCode extensions that are available. The following instructions takes advantage of the Controller:bit\'s MakeCode extension but you can follow along to add other extensions as well.

### [][Installing a MakeCode Extension](#installing)

To install or add a new extension to your MakeCode toolbox (the list of different block groups), click on \"**Advanced**\" and then on \"**Add Extension**.\"

[![MakeCode Extensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/5/MicroBitExtensions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/MicroBitExtensions.jpg)

From here you can search for \"**SparkFun**\" or \"**SparkFun gamer-bit**,\" and it should show up as a public extension in the list. Go ahead and click on it.

[![SparkFun Extensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/5/MicroBit_SparkFun_Extensions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/MicroBit_SparkFun_Extensions.jpg)

**Heads up!** Not able to find a certain extension? It could be that the extension has not been approved and published yet. It does take time to get an extension approved by the micro:bit Educational Foundation before it can be searchable by name. Part of the requirements for the approval process involves a live product page. Therefore, at the time of the launch for certain products, an extension may not have been approved and the only method of adding the extension is to use the link to the GitHub repository of the pxt-package and paste the URL in the extension search box. The MakeCode editor will find it and allow anyone to add it to their project.

This will add all of the blocks to your toolbox. In general, this is a bit tricky as, depending on how the extension was written, it may either have its own toolbox or just add blocks to the existing ones. Take a look at your toolbox; for the gamer:bit you should see\...

[![Screenshot gamer:bit installed](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Screen_Shot_2017-06-28_at_11.10.58_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Screen_Shot_2017-06-28_at_11.10.58_PM.png)

Great! You have now installed the gamer:bit extension! If you bought the micro:arcade kit, you are ready to use the board as well as the components that came in the kit. As a side note, for every new MakeCode project that you make, you will have to load extensions over again. Not a big deal, but noteworthy!

### [][Updating Extensions](#update)

Published example codes and **\*.hex** files that are saved use archived versions of extensions. Occasionally, there are updates to either MakeCode editor or the extensions. If you need to update an extension to the latest due to a compile error or new features, there are two methods of updating your extensions. One method is to remove all instances of the blocks provided by the extension and reinstalling the extension as outlined above. This can be tedious if there are several blocks sandwiched together and the length of your code. The second method is to update the version number in the Javascript View. The benefit is that users do not have to manually remove blocks that are sandwiched together.

Below is a published example where a previous gamer:bit extension was able to compile. An update to the MakeCode editor caused an error due to a bug in the gamer:bit extension that was ignored in previous versions of the MakeCode editor. A patch was eventually applied to the gamer:bit extension so we want to update the example to pull in the latest version to fix the error.

[![Error in MakeCode Example from gamer:bit extension](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_1.png)

Toggle the **JavaScript** button at the top to switch to the JavaScript view. On the left hand side, you will notice the **Explorer** Menu. Click on the arrow to expand the menu.

[![Switch to Javascript View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_2.png)

Scroll down to the MakeCode extension\'s version number. Here you can delete or update the extension version. We\'ll want to update the version number since the code relies on the gamer:bit extension. Click the button with the refresh symbol and version number.

[![Check out the Explorer Menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_3.png)

At this point, give it a few seconds to pull in the latest version number from the cloud. Then re-open the Explorer menu. If there was an update, this will refresh the extension and use the latest version. In this case, there was an update so it pulled in version v0.0.8! You\'ll notice that the red box with the number (which indicates the number of issues with the code) went away as well.

[![Hit the Refresh/Version Button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_4.png)

Just to make sure everything is going smoothly. Head back to the **Blocks** view, the error indicated by a triangle went away. Sweet! We have successfully updated the MakeCode extension so that we can get back to coding!

[![Head Back to Blocks View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Updating_MakeCode_Extension_5.png)

### Making an Extension

For developers and advanced programmers interesting in making your own custom extensions, [check out the following tutorial](https://learn.sparkfun.com/tutorials/how-to-create-a-makecode-package-for-microbit) for more information!

[](https://learn.sparkfun.com/tutorials/how-to-create-a-makecode-package-for-microbit)

### How to Create a MakeCode Package for Micro:Bit 

April 16, 2019

Learn how to develop code blocks for the Micro:bit in Microsoft MakeCode!

## Powering the micro:bit

You have your program running on your micro:bit, but it is still tethered to your computer. There are a number of ways to solve this problem\... batteries, batteries and more batteries!

⚡ **Oh snap!** Looking for more information about adding remote power to your micro:bit? Check out these application notes from the micro:bit Foundation!\
\

[micro:bit Foundation: Power Supply](https://tech.microbit.org/hardware/powersupply/)

### USB Battery Pack

USB battery packs are becoming pretty commonplace out there. You can use one to run your micro:bit project for quite a long time.

[![micro:bit powered with USB Power via the USB Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Getting_started_with_Micro_Bit-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/9/Getting_started_with_Micro_Bit-02.jpg)

It is handy to have a [shorter USB cable](https://www.sparkfun.com/products/13244) to keep from dragging a super-long wire around.

### 2xAA Battery Pack

**Warning:** JST-PH connectors are usually used with LiPo batteries. These have a different battery chemistry and voltage compared to the AA batteries used with 2xAA battery packs. Unless you have a voltage regulator to regulate the LiPo battery\'s voltage, make sure to only use AA batteries with the micro:bit\'s JST-PH connector.

The [2xAA battery holder with JST-PH connector](https://www.sparkfun.com/products/14299) is a great solution if you are looking to power a whole lot of micro:bits for a good amount of time, such as in a classroom setting.

[![micro:bit powered with 2xAA batteries via the JST connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/9/Getting_started_with_Micro_Bit-01.jpg)](https://www.sparkfun.com/products/14299)

These batteries can be purchased in bulk for pretty cheap.

### 2xAAA Battery Pack

**Warning:** JST-PH connectors are usually used with LiPo batteries. These have a different battery chemistry and voltage compared to the AAA batteries used with 2xAAA battery packs. Unless you have a voltage regulator to regulate the LiPo battery\'s voltage, make sure to only use AA batteries with the micro:bit\'s JST-PH connector.

Looking for a smaller battery holder? Try looking at the 2xAAA battery holder with JST-PH connector. There is one that is included in the micro:bit Go bundle!

[![micro:bit v2 Go Bundle ](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/3/0/8/17288-micro-bit_Go_Bundle-01.jpg)](https://www.sparkfun.com/micro-bit-v2-go-bundle.html)

### [micro:bit v2 Go Bundle ](https://www.sparkfun.com/micro-bit-v2-go-bundle.html) 

[ DEV-17288 ]

The micro:bit v2 is a pocket-sized computer and the Go Bundle provides you with everything you need to get hooked up and powe...

[ [\$24.95] ]

Or even check out the 2xAAA battery holder with JST-PH connector and power switch! The added switch makes it easy to turn on and off your micro:bit project without the need to wiggle the JST-PH connector off of your micro:bit.

[![micro:bit Battery Holder - 2xAAA (JST-PH)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/6/0/15101-micro-bit_Battery_Holder_-_2xAAA__JST-PH_-01.jpg)](https://www.sparkfun.com/micro-bit-battery-holder-2xaaa-jst-ph.html)

### [micro:bit Battery Holder - 2xAAA (JST-PH)](https://www.sparkfun.com/micro-bit-battery-holder-2xaaa-jst-ph.html) 

[ PRT-15101 ]

This is a unique two-cell AAA battery holder built specifically for the BBC micro:bit. The 6\" (\~150mm) cable has been termina...

[ [\$2.50] ]