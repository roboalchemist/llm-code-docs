# Source: https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide

## Introduction

The [Serial Basic](https://www.sparkfun.com/products/14050) is an easy to use USB to Serial adapter based on the CH340G IC from [WCH](http://www.wch.cn). It works with 5V and 3.3V systems and should auto install on most operating systems without the need for additional drivers. It\'s a great lower cost option to the extremely popular [FTDI Basic](https://www.sparkfun.com/products/9716).

[![SparkFun Serial Basic Breakout - CH340G](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/8/8/14050-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html)

### [SparkFun Serial Basic Breakout - CH340G](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html) 

[ DEV-14050 ]

The SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G IC from WCH.

[ [\$9.25] ]

The Serial Basic uses the CH340G IC to quickly and easily convert serial signals to USB. It works great with all of our products including the [Arduino Pro Mini](https://www.sparkfun.com/products/11113), our [GPS modules](https://www.sparkfun.com/categories/17), [cellular modules](https://www.sparkfun.com/products/13120), and many other devices that uses serial communication.

### Required Materials

At a minimum, you will need the following materials to follow along with the tutorial. You may not need everything though depending on what you have and your setup. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

### Suggested Reading

This is an easy board to get started with, but, if you are not sure how serial works or have not used a terminal program before, you may want to checkout the following tutorials.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

## Serial Basic Overview

The pinout of the Serial Basic mimics the common [DTR]/RX/TX/VCC/[CTS]/GND pinout found on hundreds of FTDI-to-USB derivatives.

[![Top of Serial Basic CH340G](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Top_of_Serial_Basic_CH340G.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Top_of_Serial_Basic_CH340G.jpg)

  Pin Label                                  Input/Output    Description
  ------------------------------------------ --------------- ---------------------------------------
  [DTR]   Output          Data Terminal Ready, Active Low
  RXI                                        Input           Serial Receive
  TXO                                        Output          Serial Transmit
  VCC                                        Supply Output   Power supply **3.3V (default)** or 5V
  [CTS]   Input           Clear To Send, Active Low
  GND                                        Supply Output   Ground (0V) supply

### Alignment Markers

These `GRN` and `BLK` indicators are there to help you align the board properly with products that use this same pinout.

[![Alignment markers on Serial Basic](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Alignment_Markers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Alignment_Markers.jpg)

The Serial Basic mates seamlessly with products that use the standard serial connection. If you see a board with the `BLK` and `GRN` labels, then you know it will be compatible with the **Serial Basic**.

![nRF52832 Breakout](https://cdn.sparkfun.com//assets/parts/1/1/7/5/2/13990-01.jpg "nrf52832 Breakout")

*See the GRN and BLK labels on this [nRF52832 Breakout](https://www.sparkfun.com/products/13990)?*

**Where did GRN and BLK come from?** Way back in 2008, when we created the [Arduino Pro Mini](https://www.sparkfun.com/products/11113), we needed to have a pinout to allow serial bootloading. At the time, the best USB to TTL Serial device was the FT232 Cable. Its unpolarized connector could be flipped either way so we added the words **GRN** and **BLK** to the PCB to let folks know how to line up the colored wires. The practice stuck! Now, many boards use this standard.\
\

[![The old FTDI Cable](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/FTDI_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/FTDI_Cable.jpg)

\

*The cable with colored wires*

### Voltage Selection Jumper

There is a jumper on the rear of the board that controls the output voltage on the VCC pin. By default, the board outputs **3.3V** and has **3.3V signals**. Changing this jumper to 5V will cause the board to output 5V on the VCC pin with 5V signals.

[![Jumper to select between 3.3V and 5V](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Voltage_Jumper_CH340G.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Voltage_Jumper_CH340G.jpg)

*Jumper is default to 3.3V VCC and I/O*

When the jumper is set to 3.3V, the board uses an onboard 3.3V regulator capable of sourcing 600mA. If you attempt to pull more than 600mA, the regulator will go into short-circuit shutdown where it will only output 150mA.

When the jumper is set to 5V, the board will source as much power as your USB port will provide.

### LEDs

There are two LEDs on the board connected to TX (Green) and RX (Yellow). This is a quick and handy way to see the serial traffic.

[![LEDs on CH340G Serial Basic](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Serial_Basic_CH340G_LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Serial_Basic_CH340G_LEDs.jpg)

## Hardware Test

To connect the board to a computer, you will need a standard [A to micro-B USB cable](https://www.sparkfun.com/products/10215). Plug the micro-B USB cable into a USB port on your computer and the other end into the Serial Basic. Your computer should automatically install the necessary drivers and create a COM port on your computer. If you are prompted for drivers, please see the [Drivers](https://learn.sparkfun.com/tutorials/serial-basic-hookup-guide/all#drivers-if-you-need-them) section.

The quickest and easiest way to make sure everything is working is to do a TX/RX loop-back. To do this, insert a [jumper wire](https://www.sparkfun.com/products/12795) between TX and RX. Anything that is transmitted from the TX pin will be *echoed* back to the RX pin.

[![Jumper wire connecting TX to RX](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/7/Serial_Basic_Post-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Serial_Basic_Post-02.jpg)

Open your favorite [terminal program](https://learn.sparkfun.com/tutorials/terminal-basics). Select the COM port that the Serial Basic is assigned to, and connect. When you type a character, you should see each character you type echoed back in the terminal.

[![Terminal window showing echoed characters](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Terminal_Window_with_Echoed_Characters.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Terminal_Window_with_Echoed_Characters.jpg)

*Success!*

## Which COM Port Do I Need?

Most programs will show you a description of the USB device that created the port. To verify that your driver is working, you can use a serial terminal, Arduino IDE, device manager, or command line.

### Serial Terminal

Look for the port associated with **CH340**.

[![Serial port with CH340G named](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-3.jpg)

### Arduino IDE Ports

If you\'re using the Arduino IDE, figuring out which COM port is the one you want is more difficult. Here\'s the quick way to figure it out: attach the Serial Basic to your computer, and check which COM ports are listed. In the image below, we have two ports. Now close the **Tool** menu by clicking on the main Arduino IDE window.

[![Arduino serial com port sub menu](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-1.jpg)

*Which COM port should I select?*

Unplug the Serial Basic, and re-open the **Tools**-\>**Ports** submenu. You will see one of the serial ports is missing. That\'s the one you want! Plug your Serial Basic back in, and use that COM port.

[![Missing COM port in Arduino IDE Tools -\> Ports Menu](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-2.jpg)

**Note:** You need to close and re-open the tools menu before Arduino will refresh the port list. If you have the tool menu open simply click on the main window, then click back on **Tools** -\> **Port**.

#### Windows: Device Manager

You can also verify that the board is installed if it shows up in your device manager. You can click the **Start** or [⊞] (**Windows**) button and type \"device\" to quickly search for the application. (\*On Windows 10, the quick search function is picky on the spelling of the application you are searching for. For example, you may get results using \"\_devi\_\" and none for \"\_device\_\".)

[![Windows 10 Device Manager Window](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Win7_10_Device_Check.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/Win7_10_Device_Check.PNG)\
*Screenshot of Window 10 Device Manager with Serial Basic on COM42. **Click** to enlarge.*

#### Mac OSX: Command Line

To verify on a Mac via the command line. To open a command line window, head to your **Applications** folder, **Utilities** folder, then double-click on **Terminal**. Otherwise, press [⌘] (**Command**) + [space bar] (**Space Bar**) to launch Spotlight and type \"Terminal,\" then double-click the search result.

Run the following command \"`ls /dev/cu*`\" in a Terminal and check for the following changes (your board may show up under a different device name).

    language:bash
    ls /dev/cu*

You should get something similar as shown in the image below.

[![Mac OSX CLI Command Entry](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/MacOSX_Device_Check.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/4/MacOSX_Device_Check.png)\
*Screenshot of Mac OSX terminal with Serial Basic on cu.wchusbserialfd1410. **Click** to enlarge.*

**Note:** If you are still unsure of how to access the Terminal, [watch this video](https://www.youtube.com/watch?v=zw7Nd67_aFw) or read this [Apple support article](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).

#### Raspbian: Command Line

Run the following command \"`ls /dev/ttyUSB*`\" in the CLI/Terminal and check for the following changes (your board may show up under a different device name).

    language:bash
    ls /dev/ttyUSB*

You should get something similar as shown in the image below.

[![Raspbian CLI Command Entry](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Raspbian_Stretch_Device_Check.png)](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/4/4/Raspbian_Stretch_Device_Check.png)\
*Screenshot of Raspberry Pi CLI with Serial Basic on ttyUSB0. **Click** to enlarge*

\

## Drivers If You Need Them

The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.