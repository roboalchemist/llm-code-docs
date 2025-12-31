# Source: https://learn.sparkfun.com/tutorials/getting-started-with-walabot

## Introduction

See through walls, track objects, monitor breathing patterns, and more using the power of radio frequency with the Walabot!

[![Walabot Starter](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/2/4/14534-01.jpg)](https://www.sparkfun.com/products/14534)

### [Walabot Starter](https://www.sparkfun.com/products/14534) 

[ SEN-14534 ]

The Walabot Starter is a small, programmable sensor tool that looks into objects using radio frequency technology sense the e...

**Retired**

[![Walabot Developer](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/2/5/14535-01.jpg)](https://www.sparkfun.com/products/14535)

### [Walabot Developer](https://www.sparkfun.com/products/14535) 

[ SEN-14535 ]

The Walabot Developer is a programmable 3D sensor inside a protective enclosure that looks into objects using radio frequency...

**Retired**

In this tutorial, we will explore Walabot\'s features using the Software Demo Kit (SDK) on Windows and the Application Programming Interface (API) on Linux-based OS for embedded projects.

### Required Materials

To follow along with this tutorial, you will need the following materials to get started. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary:

\* Walabot (Starter or Developer) \* Computer (Windows, Linux) w/ USB Port \* [micro-B to type A USB cable](https://www.sparkfun.com/products/10215)

For more embedded applications with a Raspberry Pi, you will need the following materials:

- [Raspberry Pi 3 Starter Kit](https://www.sparkfun.com/products/13826)
- [LCD 7\"](https://www.sparkfun.com/products/13733) or Monitor w/ HDMI Cable
- [Keyboard and Mouse](https://www.sparkfun.com/products/14271)

### Suggested Reading

If you aren\'t familiar with the following concepts when using a Raspberry Pi, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/sd-cards-and-writing-images)

### SD Cards and Writing Images 

How to upload images to an SD card for Raspberry Pi, PCDuino, or your favorite SBC.

## Hardware Overview

### Features

The Walabot utilizes radio frequency technology to sense the environment. An image of the environment is reconstructed using an array of linearly polarized broadband antennas to transmit, receive, and record signals. The data is processed and sent through a USB cable to a host device. The host device can be your computer, single board computer, or even a smartphone!

[![Walabot Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDiagram.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDiagram.jpg)

Depending on the Walabot model, here are a few possible applications:

- In-Room Imaging
- Object Detection, Location, and Tracking
- Motion Sensing (i.e. Breathing Patterns, Gestures)
- Speed Measurement
- In-Wall Imaging
- Dialectric Properties of Materials

### Starter vs Developer

There are three models of the Walabot. For the scope of the tutorial, we will be using the starter and developer to begin. The starter uses 3x antennas as opposed to 18x antennas to detect the environment. The starter is capable of basic range measurements and monitoring breathing patterns. Due to the amount of antennas it has available, it will not be able to sense objects behind a material. The starter also does not come with an enclosure.

The developer has a higher resolution with the 18x antennas. It\'s capable of the applications listed earlier. However, the developer can consume more power depending on the configuration and it requires a little bit more time to process the data. Below is a comparison taken from the datasheet.

+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Capability \\ Model             | Walabot Starter                                                                | Walabot Developer                                                               |
+=================================+================================================================================+=================================================================================+
| Physical Specifications                                                                                                                                                                            |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Number of Antennas*            | 3                                                                              | 18                                                                              |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Board Size*                    | [72 mm \* 48 mm](https://cdn.sparkfun.com/assets/parts/1/2/6/2/4/14534-02.jpg) | [72 mm \* 140 mm](https://cdn.sparkfun.com/assets/parts/1/2/6/2/5/14535-03.jpg) |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| External Powering Option        |                                                                                | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Enclosure                       |                                                                                | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Software API Capabilities                                                                                                                                                                          |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Basic API functions*           | ✓                                                                              | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *2D Acquisition*                | ✓                                                                              | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *3D Acquisition*                |                                                                                | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Multiport Recorder (Raw Data)* |                                                                                | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Software Application Capabilities                                                                                                                                                                  |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Breathing Detection*           | ✓                                                                              | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Object Detection*              | ✓                                                                              | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Short Range Imaging*           |                                                                                | ✓                                                                               |
+---------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

### Enclosure

The Walabot Starter does not come in an enclosure. To protect the bare board, you could:

- [Cut Out a Cardboard Housing](https://www.hackster.io/kuzma/cardboard-housing-for-walabot-pro-a99496)
- [Laser Cut Acrylic](https://www.hackster.io/user5016473805/drone-race-practice-companion-7c368a)
- [3D Print a Case](https://www.thingiverse.com/thing:2754128)

Just make sure to adjust the size of the enclosure for the Walabot Starter.

### Walabot w/ Other Wireless Devices

As stated in the [datasheet on page 8](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/walabot-tech-brief-416.pdf), the Walabot operates over a range of frequencies. Make sure to configure your device so that it does not interfere with other wireless devices used in projects. The operating frequency of the Walabot is above the following range so there should not be any inteference:

- Bluetooth
- Zigbee
- Cellular

### Antennas

The side with the antennas should be facing out to sense the environment. The image below shows the Walabot Starter\'s 3x antennas.

[![Walabot Starter Antennas](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/14534-03_WalabotStaterAntennas.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/14534-03_WalabotStaterAntennas.jpg)

The image below shows the Walabot Developer\'s 18x antennas populated on the board. Make sure the flat side of the enclosure is facing out to sense the environment.

[![Walabot Developer Antennas](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDeveloperFront.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDeveloperFront.jpg)

### Power Consumption

The Walabot requires a **5V (+/-10%)** power supply. The board can be powered using a USB port. Depending on the application and operation profile, the Walabot may consume up to **0.4A to 0.9A**. You may need an additional power source for the Walabot Developer. If necessary, open the Walabot enclosure with a Phillips precision screw driver.

[![Inside Walabot Developer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDeveloperBack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDeveloperBack.jpg)

Highlighted in red is the default jumper position for data transfer and powering the Walabot. To power the board with an external power supply, move the jumper to the left side and connect an additional power source to the USB port highlighted in green. The USB connector is only for power so you would still need a USB cable connected on the right connector.

[![Walabot Developer Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDeveloperBackJumpers3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDeveloperBackJumpers3.png)

## Hardware Assembly

### Walabot Starter

**Note:** The micro-B cable included with the Walabot Starter is an OTG cable. You will need to an additional cable to connect the device to a computer for development.\
\
If are using a USB cable that is not included with the Walabot, make sure that the data lines are connected when using the cable with the Walabot! Certain cables are designed to be charging cables, so there might not be any data lines connected in the USB cable.

To connect the Walabot Starter, you will need to align the \"D\" shape of the micro-B USB cable with the port.

[![Connect Walabot Starter to to your Computer with a micro-B Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotStartermicroBUSB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotStartermicroBUSB.jpg)

Once the cable is connected to the Walabot, connect the other end to a computer\'s USB port.

### Walabot Developer

**Note:** If are using a USB cable that is not included with the Walabot, make sure that the data lines are connected when using the cable with the Walabot! Certain cables are designed to be charging cables, so there might not be any data lines connected in the USB cable.

To connect the Walabot Developer, insert the USB cable\'s micro-B end to the Walabot\'s USB port. You can use a separate micro-B USB 2.0 cable or the included micro-B USB 3.0 cable. By default, there is a jumper that uses the port closest to the edge of the Walabot.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-2_0.jpg "Connecting with a separate micro-B USB 2.0 cable.")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-2_0.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-3_0.jpg "Connecting with the included micro-B USB 3.0 cable.")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-3_0.jpg)
  *Connecting with a separate micro-B USB 2.0 cable.*                                                                                                                                                                                                     *Connecting with the included micro-B USB 3.0 cable.*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you decide to use a separate micro-B USB 2.0 cable to your computer, you will be aligning it with the \"D\" shape of the micro-B USB 3.0 connector as shown in the image below.

[![Close up of micro-B USB 2.0 Cable to micro-B USB 3.0 Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-2_0PartiallyConnected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotDevelopermicroBUSB-2_0PartiallyConnected.jpg)

Once the cable is connected to the Walabot, connect the other end to a computer\'s USB port.

### Mounting

You may want to mount the board during testing. Grab some electrical tape or mount the Walabot Starter to a box using standoffs. The Walabot Developer includes a magnetic disk that is able to stick to a surface such as a robot, smartphone, or wall. With the magnetic mount, it is able to attach and detach easily from the surface. In the examples provided, the starter and developer were mounted on a red box or resting on a table for testing.

## Software Installation (Windows)

To get started with the Walabot, the easiest would be to use the Walabot demo on Windows to visualize the sensor data. It\'s a nice GUI that is able to display the sensor data. Head over to the download section for the Walabot Software Development Kit (SDK) to begin.

[Walabot (SDK) Installation for Windows](https://walabot.com/getting-started)

Click on the button for the **Windows Installer** to download the latest, stable version of the demo software. After downloading, open the executable to install the software.

**Note:** When installing the Windows SDK, a window may pop up with the following question for User Account Control:\
\
`Do you want to allow the following program from an unknown publisher to make changes to this computer?`\
\
To install the **WalabotSDK_1.0.35.exe**, click **Yes** button.

## Example SDK

Once you install the Walabot SDK, there should be a shortcut on the desktop. Click on the \"*WalabotSDK.WalabotAPItutorial.exe*\" icon on your desktop to open the program. If you have not already, plug the device to your computer\'s COM port.

### Sensor - Target Detection

The first demo application looks for objects in front of the Walabot. Before we start, make sure that there are no moving objects in front of the sensor. The sensor was mounted to a box in the following example.

[![Walbot Target Detection Calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotCalibration.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotCalibration.jpg)

*Walabot Starter or Developer Calibration*

Click on the tab labeled \"**Sensor - Target Detection**\" in the SDK. The Walabot will begin calibrating. The range seemed a bit small so the arena size for **R \[cm\]** was increased to 200cm. Once adjusted, click on the **Apply&Calibrate** button to recalibrate.

[![Walabot SDK Target Detection Calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionCalibration.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionCalibration.png)

Once calibrated, try moving an object in front of the sensor. For this example, try testing the Walabot by standing at a distance away from the sensor. For simplicity, stand directly in front of the Walabot until the sensor detects you.

[![Walbot Target Detection at a Distance](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotTargetDetection1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotTargetDetection1.jpg)

Here\'s how it may look when an object is at a distance in the SDK.

[![Walabot SDK Target Detection at a Distance](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionFar.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionFar.png)

Then try moving closer to the Walabot.

[![Walabot Target Detection Closer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotTargetDetection2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotTargetDetection2.jpg)

Here\'s how it may look when an object is closer in the SDK.

[![Walabot SDK Target Dection Closer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionClose.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-TargetDetectionClose.png)

By comparison, you will notice that the SDK will update in real time with any object in range. Try adjusting the range to see how far the sensor can detect targets! You can also adjust the amount of targets to view!

**Tip:!** To help in visualizing the arena size, grab a tape measure.

### Sensor - Breathing

The second demo application monitors breathing patterns and graphs the readings. You need to be at a certain distance away from the sensor to read. The default is between 20cm to 80cm. Click on the tab labeled \"**Sensor - Breathing**\" in the SDK.

[![Walabot SDK Sensor - Breathing Tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-Breathing_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-Breathing_2.png)

Stand in front of the sensor and inhale some air.

[![Walabot Breathing Inhale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotBreathing_Inhale.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotBreathing_Inhale.jpg)

The graph will update in real time as you inhale. As you breathe, the graph should rise. Here\'s how it may look when you take a deep breath in the SDK.

[![Walabot SDK Breathing Inhale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-BreathingInhale.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-BreathingInhale.png)

While still standing in front, exhale the air that you gathered in your lungs.

[![Walabot Breathing Exhale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotBreathing_Exhale.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotBreathing_Exhale.jpg)

As you exhale, the graph will dip. Here\'s how it may look when you exhale in the SDK.

[![Walabot SDK Breathing Exhale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-BreathingExhale.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Sensor-BreathingExhale.png)

Try adjusting the range to see how far the Walabot can sense your breathing!

### Imaging - Short Range

**Note:** Due to the limitations of the Walabot Starter, it is not able view objects behind walls.

The third demo lets you view objects behind a wall. Since we are dealing with RF signals, make sure that the wall is not made of metal. For a quick test, let\'s try viewing a material behind a flat table. Grab a wooden yard stick, metal pipe, a PVC, or a piece of wire to test.

[![Walabot Wall Detection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotWallDetectionMaterials.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotWallDetectionMaterials.jpg)

The sensor will need to view the material that it is looking through. Place the Walabot on a flat table.

[![Walabot Developer Scanning Table](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImaging_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImaging_1.jpg)

Click on the tab labeled \"**Imaging - Short Range**\".

[![Walabot SDK Short Range Imaging Calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangeCalibration.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangeCalibration.png)

The sensor will begin calibrating. It is recommended to move the Walabot slowly in a circular motion for this calibration.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_1.jpg "Walabot Calibration 1")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_1.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_2.jpg "Walabot Calibration 2")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_2.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_3.jpg "Walabot Calibration 3")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingCalibration_3.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once calibrated, try placing the material behind the table.

[![Place Pipe Behind Table](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingNoObject_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingNoObject_1.jpg)

Move the Walabot over the material.

[![Move Walabot Developer Parallel To Pipe](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingParallelObject_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingParallelObject_1.jpg)

The In-Wall Pipe Detector should display a graphic and indicate the orientation of the pipe behind the table. The material thickness of the wall (in this case it is a table) and probability that there is an object there is displayed as the *Depth* and *Confidence Level*.

[![Walabot Developer SDK Short Range Imaging Parallel ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangePipeParallel.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangePipeParallel.png)

Rotate the Walabot.

[![Rotate the Walabot Developer Perpendicular to Pipe](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingPerpendicularObject_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotShortRangeImagingPerpendicularObject_1.jpg)

The In-Wall Pipe Detector will respond by showing the material rotated.

[![Walabot Developer SDK Short Range Imaging Perpendicular](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangePipePerpendicular.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_Imaging-ShortRangePipePerpendicular.png)

Now try testing it with a wall to see if you can find a stud or a bundle of wires leading to a wall outlet! The Walabot Developer can see up to about \~4 inches (\~10cm) behind a material!

### Raw Signals

**Note:** Due to the limitations of the Walabot Starter, you will not be able to control and view the raw signals with the SDK.

The fourth demo controls the antenna arrays. It is useful for visualizing a waveform for specific applications. Click on the tab labeled "**Raw Signals**".

Using the default antenna pairs in open air, the signals will look like the graph on the right.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotRawSignal_NoObject.jpg "Walabot Sensing the Open Air")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotRawSignal_NoObject.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal.png "SDK Raw Signal in Open Air")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal.png)
  *Walabot measuring in open air*                                                                                                                                                                                            *Raw signal with antenna pairs 7 -\> 6 in open air.*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let\'s try a little paper, rock, scissors to see how well the Walabot can recognize small changes in gestures. By placing your hand directly over the Walabot in the shape of a rock, the signal should look like the graph on the right.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotRawSignal_Rock.jpg "Walabot Sensing Rock")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotRawSignal_Rock.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Rock.png "SDK Raw Signal with Rock")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Rock.png)
  *Walabot measuring rock.*                                                                                                                                                                                  *Raw signal with antenna pairs 7 -\> 6 with rock.*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Opening your had in the shape of a paper, you will notice a significant change in the graph.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotRawSignal_Paper.jpg "Walabot Sensing Paper")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotRawSignal_Paper.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Paper.png "SDK Raw Signal with Paper")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Paper.png)
  *Walabot measuring paper.*                                                                                                                                                                                    *Raw signal with antenna pairs 7 -\> 6 with paper.*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Changing the shape of your hand to scissors, you should notice small changes in amplitude throughout the signal.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotRawSignal_Scissors.jpg "Walabot Sensing Scissors")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotRawSignal_Scissors.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Scissors.png "SDK Raw Signal with Scissors")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotSDK_RawSignal_Scissors.png)
  *Walabot measuring scissors.*                                                                                                                                                                                          *Raw signal with antenna pairs 7 -\> 6 with scissors.*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Try experimenting with different antenna pairs to see what works best when writing code for your custom application!

------------------------------------------------------------------------

### Walabot\'s Demo Video

Here\'s an explanation using the Walabot with the SDK for Windows.

### Walabot API Library

The pseudocode for each example used in the Walabot SDK can be viewed by pressing the **Show Code** button. There is also a **tutorial** button that offers an explanation about the graphs relative to the Walabot. Head over to the Walabot API library for more information on the functions, parameters, and error codes when developing applications for Windows.

[Walabot API library](http://api.walabot.com/_install.html#_windowsInstall)

## Software Installation (Linux)

### Walabot API Library

**Note:** Make sure that you have Python version 2 or 3 installed. Raspberry Pi should have it installed already. To verify, open a serial terminal and type `python -V` in the command line. Pressing the `Enter` key should notify you if Python is installed. If Python is not currently installed, head over to [Python\'s download page](https://www.python.org/downloads/).

The process to install the Walabot API for Linux and Raspberry Pi are the same. The only difference is the package to download. Head over to Walabot\'s site to download the package.

[Walabot\'s Download Page](https://walabot.com/getting-started)

Scroll down the page and click on the package for your distribution. For the scope of this tutorial, we will choose the package for Raspberry Pi.

Once downloaded, you may get the following warning:

[] This type of file can harm your computer. Do you want to keep \"*walabot_maker_1.0.34_raspberry_arm32.deb* anyway?

Click on the \"**Keep**\" button to confirm the download.

[![Walabot RPI API Download](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotRaspberryPiDownload_Warning.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotRaspberryPiDownload_Warning.png)

Open a command line as indicated by the green arrow and highlighted icon in the image below.

[![Command Line](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/RaspberryPiCommandLine.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/RaspberryPiCommandLine.png)

Head to the location where the package was downloaded. Most likely this was placed in the \"*Downloads*\" folder. Type this command and hit the \"**Enter** key.\"

    cd Downloads

**Note:** This tutorial was written with the \"*walabot_maker_1.0.34_raspberry_arm32.deb*\" package. You may need to adjust the package name depending when on the package that was downloaded.\"

To view the contents, feel free to type this command:

    ls

In the command line, type this command based on the \***.deb** package that was downloaded:

    sudo dpkg -i walabot_maker_1.0.34_raspberry_arm32.deb

Once the command is ready and matches the downloaded package, hit the \"**Enter**\" key.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotCommandLine_dpkg.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotCommandLine_dpkg.png)

While installing, you may be prompted with an End User License Agreement. Read through it, press the \"→\" button on your keyboard, and hit \"**Enter**.\"

[![Walabot EULA](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotAPI_EULA.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotAPI_EULA.png)

You will be prompted again with another question. Read through the brief message, navigate to \"**\<Yes\>**\", and hit \"**Enter**.\"

[![Walabot EULA Verify](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotAPI_EULA_Accept.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotAPI_EULA_Accept.png)

The following paths and files will be installed in these locations:

- **/usr/lib/libWalabotAPI.so** - The Walabot library.
- **/usr/include/WalabotAPI.h** - The Walabot library header file.
- **/var/lib/walabot/\...** - The Walabot database and configuration files. Give this path to Walabot_SetSettingsFolder.
- **/usr/share/doc/walabot/\...** - Example code, license, and README.
- **/etc/udev/rules.d/\...** - Special udev rule for Walabot device, so it could be accessed without root privileges.

------------------------------------------------------------------------

For more information about the Walabot API Library, head over to Walabot\'s documentation.

[Walabot API Library](http://api.walabot.com/)

## Example API

Let\'s try out the examples in Python! The examples enable the user to utilize the sensor data for embedded projects. There a few methods of running the examples. Since we still have the command line open, we\'ll open the Python example through the terminal. Navigate to the examples using this command:

    cd /usr/share/doc/walabot/examples/python

Typing this command will list the three examples in that path:

    ls

Connect the Walabot to the USB port to start testing the Walabot examples.

[![Walabot Examples via Command LIne](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotCommandLine_listExamples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotCommandLine_listExamples.png)

### Target Detection w/ *SensorApp.py*

To run the *SensorApp.py* example, type this command once you are in the directory.

    python SensorApp.py

Again, make sure there are no moving objects in front of the sensor when the program begins. The *SensorApp.py* is just like the target detection example that was demonstrated in the SDK for Windows. The sensor data will be output in the terminal as shown below.

[![Walabot SensorApp.py Running](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_SensorApp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_SensorApp.png)

Try moving your hand in front of the sensor to get a feel for the sensor values. Type **Ctrl**+**c** in the command line to stop the program.

### Breathing w/ *BreathingApp.py*

To run the *BreathingApp.py* example, type this command:

    python BreathingApp.py

This is just like the breathing example that was demonstrated in the SDK for Windows. With nothing in front of the Walabot, the output should be a very small value.

[![Walabot BreathingApp.py with No Person](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppNoPerson.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppNoPerson.png)

Stand in front of the Walablot and take a deep breath in. As you inhale, the value may look like the output below. The value may be different depending on how far you are from the Walalbot.

[![Walabot BreathingApp.py Inhaling](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppInhale.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppInhale.png)

As you exhale, the value should decrease. The output may look similar to the output below.

[![Walabot BreathingApp.py Exhaling](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppExhale.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_BreathingAppExhale.png)

Type **Ctrl**+**c** in the command line to stop the program.

### Detecting Objects Behind Materials w/ *InWallApp.py*

**Note:** Due to the limitations of the Walabot Starter, it is not able view objects behind walls.

To run the *InWallApp.py* example, type this command:

    python InWallApp.py

Again, move the Walabot slowly a circular motion on a flat surface once the program begins. Here\'s what the output may look like when there are no objects behind a wall or table.

[![InWallApp.py Nothing in Wall](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppNothing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppNothing.png)

Here\'s what the output may look like when there is a metal pipe behind the surface.

[![InWallApp.py Pipe Parallel](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppPipeParallel.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppPipeParallel.png)

Rotating the Walabot, here\'s what the output may look like with the metal pipe behind the surface.

[![InWallApp.py Pipe Perpendicular](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppPipePerpendicular.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_InWallAppPipePerpendicular.png)

Type **Ctrl**+**c** in the command line to stop the program.

### Displaying Targets w/ *SensorTargets.py*

Let\'s try one more example from Walabot\'s GitHub repository:

[Walabot Projects GitHub Repository](https://github.com/Walabot-Projects)

For simplicity, we will head to the **Walabot-SensorTargets** repository. The other examples may require you to adjust the code and hardware to run the the examples. Download the example by clicking on the **Clone or download** button. Click again on **Download ZIP**. Head to the directory where the files were downloaded by typing the following command:

    cd Downloads

Unzip the **.zip** with this command:

    unzip Walabot-SensorTargets-master.zip

In the command line, type the following:

    pip install WalabotAPI --no-index --find-links="/usr/share/walabot/python/"

Change the current directory where the example was unzipped:

    cd Walabot-SensorTargets-master

Run the example by typing:

    python SensorTargets.py

The program will begin running and open a separate window. Click on the **Start** button to begin reading and ensure that there is nothing moving in front of the Walabot.

[![Walabot SensorTargets.py](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotPython_SensorTargetWindow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_SensorTargetWindow.png)

An object should display in the arena when in front of the Walabot. In this example, I just placed my hand in front of the Walabot.

[![Walabot SensorTargets.py with Hand](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/4/WalabotPython_SensorTarget_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/WalabotPython_SensorTarget_1.png)

Now that we have tested the *SensorTargets.py*, try the other examples listed in the GitHub repository! The *SeeThroughDemo.py* is a neat example that visually notifies you if there is an object behind a wall instead of just the output values in the *InWallApp.py* . The *RawImage.py* graphically displays the image of objects in view just like the SDK in Windows.

### Troubleshooting

Here are a few troubleshooting tips when using the Walabot on a Raspberry Pi.

#### • Missing Walabot API

If you are having issues running the Python examples from GitHub, the Python packages for the Walabot API may not be installed. You may receive an error similar to the output below.

    language:emacs
    Traceback (most recent call last):
      File "sensorTargets.py, line 3, in <module>
        import WalabotAPI
    ImportError:NoModule named WalabotAPI

Try using the `pip` command as explained earlier.

#### • Suspended Program

If you typed **Ctrl**+**z**, the program is suspended. You may get an error similar to the output below.

    language:emacs
    ^Z
    [1]+  Stopped                 python SensorApp.py
    pi@raspberrypi:/usr/share/doc/walabot/examples/python $ python SensorApp.py
    Traceback (most recent call last):
      File "SensorApp.py", line 74, in <module>
        SensorApp()
      File "SensorApp.py", line 38, in SensorApp
        wlbt.ConnectAny()
      File "/usr/share/walabot/python/WalabotAPI.py", line 186, in ConnectAny
        _RaiseIfErr(_wlbt.Walabot_ConnectAny())
      File "/usr/share/walabot/python/WalabotAPI.py", line 122, in _RaiseIfErr
        raise WalabotError(message, res, extended)
    WalabotAPI.WalabotError: WALABOT_INSTRUMENT_NOT_FOUND
    pi@raspberrypi:/usr/share/doc/walabot/examples/python $ 
    Traceback (most recent call last):
      File "SensorApp.py", line 74, in <module>
        SensorApp()
      File "SensorApp.py", line 38, in SensorApp
        wlbt.ConnectAny()
      File "/usr/share/walabot/python/WalabotAPI.py", line 186, in ConnectAny
        _RaiseIfErr(_wlbt.Walabot_ConnectAny())
      File "/usr/share/walabot/python/WalabotAPI.py", line 122, in _RaiseIfErr
        raise WalabotError(message, res, extended)
    WalabotAPI.WalabotError: WALABOT_INSTRUMENT_NOT_FOUND

You could try closing the command line and restarting the program.