# Source: https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide

## Introduction

The [latest iteration of the SparkFun Serial Basic Breakout](https://www.sparkfun.com/products/15096) takes advantage of USB-C and is an easy-to-use USB-to-Serial adapter based on the *CH340C* IC from WCH. With USB-C you can get up to three times the power delivery over the previous USB generation and has the convenient feature of being *reversible*. The product works with 5V and 3.3V systems and should auto install on most operating systems without the need for additional drivers. The Serial Basic uses the CH340C IC to quickly and easily convert serial signals to USB. It's a great **lower-cost** alternative to the extremely popular [FTDI Basic](https://www.sparkfun.com/products/9716).

[![SparkFun Serial Basic Breakout - CH340C and USB-C](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/5/2/15096-SparkFun_Serial_Basic_Breakout_-_CH340C_and_USB-C-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html)

### [SparkFun Serial Basic Breakout - CH340C and USB-C](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html) 

[ DEV-15096 ]

This SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G and takes advantage of the ha...

[ [\$10.50] ]

### Required Materials

At a minimum, you will need the following materials to follow along with the tutorial. You may not need everything though depending on what you have and your setup. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Jumper Wires - Connected 6\" (M/M, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/3/12795-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)

### [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html) 

[ PRT-12795 ]

These are 6\" long jumper wires with male connectors on both ends. Use these to jumper from any female header on any board, to...

[ [\$2.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

### Suggested Reading

Before you begin it may be worth looking at the basics of Serial Communication. Do you have a favorite terminal program yet? No? Take a look at the Serial Terminal Basics tutorial which will give you a brief introduction to popular Terminal programs.

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

  Pin Label                                  Input/Output    Description
  ------------------------------------------ --------------- ---------------------------------------
  [DTR]   Output          Data Terminal Ready, Active Low
  RXI                                        Input           Serial Receive
  TXO                                        Output          Serial Transmit
  VCC                                        Supply Output   Power supply **3.3V (Default)** or 5V
  [CTS]   Input           Clear To Send, Active Low
  GND                                        Supply Output   Ground (0V) supply

### USB-C

USB-C gives you the potential of more power than the previous generation of USB. USB-C is used to power everything from laptops to low powered micro controllers and has the amazing capability of being reversible.

[![This image shows the topside of the product with the USB-C connector highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/USB-C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/USB-C.jpg)

### LEDs

The two LEDs on the board are connected to TX (Green) and RX (Yellow) and are correctly aligned to the silk header labels: `RXI` and `TXO` . This is a quick and handy way to see the serial traffic.

[![An image of the Serial Basic with the RX and TX LEDs highlighted.](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/LEDs.jpg)

### Alignment Markers

The `GRN` and `BLK` silk in the corners opposite of the USB-C connector, is there to help you align the board properly with products that use these same orientation indicators.

[![This picture shows the alignment silk at the two corners of the board nearest the female header labeled \'Black\' and \'Green\'. ](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/Alignment_Markers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/Alignment_Markers.jpg)

The Serial Basic mates seamlessly with products that use the standard serial connection. If you see a board with the `BLK` and `GRN` labels, then you know it will be compatible with the **Serial Basic**.

![nRF52832 Breakout](https://cdn.sparkfun.com//assets/parts/1/1/7/5/2/13990-01.jpg "nrf52832 Breakout")

*See the GRN and BLK labels on this [nRF52832 Breakout](https://www.sparkfun.com/products/13990)?*

**Where did GRN and BLK come from?** Way back in 2008, when we created the [Arduino Pro Mini](https://www.sparkfun.com/products/11113), we needed to have a pinout to allow serial bootloading. At the time, the best USB to TTL Serial device was the FT232 Cable. Its unpolarized connector could be flipped either way so we added the words **GRN** and **BLK** to the PCB to let folks know how to line up the colored wires. The practice stuck! Now, many boards use this standard.\
\

[![The old FTDI Cable](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/FTDI_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/FTDI_Cable.jpg)

\

*The cable with colored wires*

### Voltage Selection Jumper

There is a jumper on the underside of the board that controls the output voltage on the VCC pin. By default, the board outputs **3.3V** and has **3.3V signals**.

[![This image shows the underside of the product with the USB-C facing right. It highlights the three way jumper near the right edge where the top jumper is labeled 3.3V and the bottom jumper is labeled 5V.](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/Serial_Basic_IO_Logic_SelectionJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/Serial_Basic_IO_Logic_SelectionJumpers.jpg)

*There is a small trace connecting the middle pad and the top pad labeled `3.3V`.*

When the jumper is set to 3.3V, the board uses an on board 3.3V regulator capable of sourcing 600mA. If you attempt to pull more than 600mA, the regulator will go into short-circuit shutdown where it will only output 150mA.

You can change the board\'s output and signal to 5V by [cutting the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) between the center and `3.3V` labeled pad and [putting solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) on the center and `5V` labeled pad. This will change the board\'s output to **5V** on the VCC pin with **5V signals**.

[![This image shows the same jumper but the small trace connecting 3.3V is cut and solder has been added to the 5V side of the three way jumper.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/7/Serial_Basic_CH340C-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/Serial_Basic_CH340C-02.jpg)

When the jumper is set to 5V, the board will source as much power as your USB port will provide. With USB-C this can be up to 1.5Amps but depending on what is providing the power and the capabilities of your cable, you can get up to 3 Amps.

## Hardware Test

To connect the board to a computer, you will need a [USB-C](https://www.sparkfun.com/products/14743) cable. Plug the USB-C cable into a USB port on your computer and the other end into the Serial Basic. Your computer should automatically install the necessary drivers and create a COM port on your computer. If you are prompted for drivers, please see the [Drivers](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) section.

The quickest and easiest way to make sure everything is working is to do a TX/RX loop-back. To do this, insert a [jumper wire](https://www.sparkfun.com/products/12795) between **TX** and **RX** as shown below. Anything that is transmitted from the TX pin will be *echoed* back to the RX pin.

[![This image shows a picture of product plugged into a USB-C cable and a single jumper wire connecting RX and TX through the female header on the underside.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/7/USB-C_and_Jumper_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/7/USB-C_and_Jumper_Wire.jpg)

Now that you\'ve got that plugged in, open your favorite [terminal program](https://learn.sparkfun.com/tutorials/terminal-basics). Select the COM port that the Serial Basic is assigned to, and connect. When you type a character, you should see each character you type echoed back in the terminal and the RX and TX LEDs will flash as you type.

[![Terminal window showing echoed characters](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Terminal_Window_with_Echoed_Characters.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/Terminal_Window_with_Echoed_Characters.jpg)

*Success!*

## Which COM Port Do I Need?

Most programs will show you a description of the USB device that created the port. To verify that your driver is working, you can use a serial terminal, Arduino IDE, device manager, or command line.

### Serial Terminal

Look for the port associated with **CH340C**. The image below shows the Serial Basic enumerating on a COM port within a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows).

[![Serial port with CH340G named](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-3.jpg)

### Arduino IDE Ports

If you\'re using the Arduino IDE, figuring out which COM port is the one you want is more difficult. Here\'s the quick way to figure it out: attach the Serial Basic to your computer, and check which COM ports are listed. In the image below, we have two ports. Now close the **Tools** menu by clicking on the main Arduino IDE window.

[![Arduino serial com port sub menu](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/7/SerialPort_Name-1.jpg)

*Which COM port should I select?*

Unplug the Serial Basic, and re-open the **Tools** -\> **Ports** submenu. You will see one of the serial ports is missing. That\'s the one you want! Plug your Serial Basic back in, and use that COM port.

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

## Drivers (If You Need Them)

The driver should automatically install on most operating systems. However, there is a wide range of operating systems out there. You may need to install drivers the first time you connect the chip to your computer\'s USB port or when there are operating system updates. For more information, check out our [How to Install CH340 Drivers Tutorial](https://www.sparkfun.com/ch340).

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.