# Source: https://learn.sparkfun.com/tutorials/choosing-a-lilypad-arduino-for-your-project

## Introduction

You are ready for your first programmed LilyPad project, but which LilyPad Arduino do you choose? In this guide, we\'ll go over the features of each of the Arduinos in the LilyPad line and their strengths and weaknesses.

[![LilyPad Arduino Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/8/AllLilyPadsArduinos.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/AllLilyPadsArduinos.jpg)

We\'ve put together a quick feature comparison chart below. For more detailed technical specs, check out our [Arduino Comparison Guide for LilyPad](https://www.sparkfun.com/etextile_arduino_comparison_guide).

  Board                            Microcontroller   Digital I/O Pins   Analog Input Pins   Programming Interface   Battery Attachment
  -------------------------------- ----------------- ------------------ ------------------- ----------------------- --------------------
  LilyPad Arduino Simple           ATMega328         9                  4                   FTDI                    JST Connector
  LilyPad Arduino USB              ATmega32U4        9                  4                   USB                     JST Connector
  LilyPad Arduino SimpleSnap       ATMega328         9                  4                   FTDI                    Built in LiPo
  LilyPad USB Plus                 ATMega32U4        10                 7                   FTDI                    Built in LiPo
  LilyPad Arduino 328 Main Board   ATMega328         14                 6                   FTDI                    Sew Tabs

### Suggested Reading

If you have never worked with LilyPad or other wearable technology before, you may find the following resources useful.

- [Getting Started with LilyPad](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)
- [Planning a Wearable Electronics Project](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)
- [Insulation Techniques for E-Textiles](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles)

## LilyPad Arduino Simple Board

[![LilyPad Arduino Simple Board](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadSimple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadSimple.jpg)

**Features:**

- 5 Digital I/O pins
- 4 Analog pins
- ATmega328
- Built-in ON/OFF switch
- Built-in power supply socket (JST connector) for a 3.7V LiPo battery and charging circuit (no additional battery charger needed)
- Simplified layout with less pins, giving more space for sewing or less complex projects

The [LilyPad Arduino Simple Board](https://www.sparkfun.com/products/10274) is one of our most popular for beginner Arduino projects because of its spacious layout. It is easier to identify pins and has more room for stitching without the risk of accidentally touching other pins on the board. The built-in battery port makes it easy to choose a LiPo battery that suits the run time requirements of your project and recharge the battery by simply plugging the board into a USB port on your computer or [5V wall charger](https://www.sparkfun.com/products/11456).

The LilyPad Arduino Simple Board needs a [LilyPad FTDI Basic Breakout](https://www.sparkfun.com/products/10275) and [USB Mini-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.

## LilyPad Arduino USB - ATmega32U4 Board

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadUSB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadUSB.jpg)

**Features:**

- 5 Digital I/O pins
- 4 Analog pins
- ATMega32U4
- Built-in ON/OFF switch
- Built-in power supply socket (JST connector) for a 3.7v LiPo battery and charging circuit (no additional battery charger needed)
- Simplified layout with less pins, giving more space for sewing or less complex projects
- Micro USB connection instead of FTDI header pins

The [LilyPad Arduino USB](https://www.sparkfun.com/products/12049) is similar to the LilyPad Arduino Simple Board, but uses a different chip - the ATMega32U4, which has built-in USB support. If the FTDI header pins on other LilyPad Arduinos feel too bulky or FTDI Boards are often lost or misplaced, this board is a great alternative.

*Note: the digital I/O pin layout is slightly different than the LilyPad Arduino Simple - the USB uses pins 2 and 3 instead of 5 and 6.*

The LilyPad Arduino USB needs a [Micro USB Cable](https://www.sparkfun.com/products/10215) in order to connect to a computer and upload code.

## LilyPad Arduino SimpleSnap

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadSnap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadSnap.jpg)

**Features:**

- 5 Digital I/O pins
- 4 Analog pins
- ATmega328
- Built-in ON/OFF switch
- Built-in LiPo battery and charging circuit
- Simplified layout with less pins, giving more space for sewing or less complex projects
- Built-in snaps for quick attachment/detachment to multiple projects

[] Because the battery is soldered to this LilyPad Arduino, it cannot be washed. Unsnap the LilyPad from its base before washing.

The [LilyPad Arduino SimpleSnap](https://www.sparkfun.com/products/10941) is similar to the LilyPad Simple Board, except for two major differences: a built-in rechargeable 110mAh LiPo battery and female snap connectors. This board requires connection to a [SimpleSnap Protoboard](https://www.sparkfun.com/products/10940) or an arrangement of sew-on fabric snaps so that the board is removable from a project. This gives you the ability to swap out the LilyPad Arduino to reprogram and share in multiple projects.

The LilyPad Arduino Simple Board needs a [LilyPad FTDI Basic Breakout](https://www.sparkfun.com/products/10275) and [USB Mini-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.

## LilyPad USB Plus

[![LilyPad USB Plus](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/14631-Lilypad_USB_Plus-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/14631-Lilypad_USB_Plus-04.jpg)

**Features:**

- 10 Digital I/O pins
- 7 Analog pins
- ATMega32U4
- Built-in ON/OFF switch
- Built-in power supply socket (JST connector) for a 3.7v LiPo battery and charging circuit (no additional battery charger needed)
- Power and ground sew tabs accessible on opposite sides of the board, providing more connection options
- Micro USB connection

The [LilyPad USB Plus](https://www.sparkfun.com/products/14631) is an update to the LilyPad Arduino USB, with additiona tabs, labeling, and built-in features. The USB Plus includes an RGB LED at the center for quick prototyping without connecting additional parts, and a row of 6 white LEDs for indicator lights or simple data visualization.

*Note: the USB Plus is not currently supported on Windows 7 operating systems.*

The LilyPad Arduino USB needs a [Micro USB Cable](https://www.sparkfun.com/products/10215) in order to connect to a computer and upload code.

## LilyPad Arduino 328 Main Board

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadMainRev.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/LilyPadMainRev.jpg)

**Features:**

- 14 Digital I/O pins
- 6 Analog pins
- ATmega328

The [LilyPad Arduino 328 Main Board](https://www.sparkfun.com/products/13342) has all of the ATmega 328 pins available for connecting to a wearable project. This board is recommended if your project needs access to more analog input pins than the other LilyPad Arduino offerings. Unlike the others, it does not have a battery port \-- you will need to stitch a power supply to the **+** and **-** pins on the board. We recommend the [LilyPad Simple Power](https://www.sparkfun.com/products/11893) board to provide a LiPo connection and charging circuit to your project.

The LilyPad Arduino 328 Main Board needs a [LilyPad FTDI Basic Breakout](https://www.sparkfun.com/products/10275) and [USB Mini-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.

## LilyPad ProtoSnap Series

LilyPad ProtoSnap boards are a great way to get started learning about creating interactive e-textile circuits before you start sewing. Everything is wired together on a single board, which makes it easy to explore the possibilities of the components before snapping them apart and building the individual pieces into your project with conductive thread.

### LilyPad ProtoSnap Plus

The [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346) is a way to prototype with LilyPad Arduino and components that are pre-wired together. After uploading code to the LilyPad Arduino, you can easily snap apart the components and sew them into a project.

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/assets/parts/1/2/3/2/4/14346-04.jpg)](https://cdn.sparkfun.com/assets/parts/1/2/3/2/4/14346-04.jpg)

**Features:**

- LilyPad USB Plus with built-in RGB and six white LEDs

- Pre-wired components: light sensor, buzzer, button, 4 pairs of LEDs (yellow, red, green, and blue), slide switch, and 5 expansion ports for easy prototyping

The LilyPad ProtoSnap Plus needs a [USB Micro-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.

### ProtoSnap - LilyPad Development Board

The [ProtoSnap - LilyPad Development Board](https://www.sparkfun.com/products/retired/11262) is the classic LilyPad Arduino ProtoSnap kit with a LilyPad Simple Arduino and set of LilyPad pieces pre-connected. It also includes needles, conductive thread, and a battery to get started prototyping and building quickly.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/ProtosnapDev_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/ProtosnapDev_crop.jpg)

**Features:**

- LilyPad Arduino Simple Board
- FTDI Basic Breakout
- 3.7v LiPo Battery
- Pre-wired components: light sensor, temperature sensor, buzzer, vibe motor, 5 LEDs, tri-color LED, slide switch, button
- Conductive thread bobbin
- Needle set

The ProtoSnap - LilyPad Development Board needs a [USB Mini-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.

### ProtoSnap - LilyPad Development Board Simple

The [ProtoSnap - LilyPad Development Board Simple](https://www.sparkfun.com/products/11201) is similar to the Development Board, but with less components pre-wired to the Arduino.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/ProtosnapSimple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/8/ProtosnapSimple.jpg)

**Features:**

- LilyPad Arduino Simple Board
- FTDI Basic Breakout
- 3.7v LiPo Battery
- Pre-wired components: buzzer, 4 LEDs
- Conductive thread bobbin
- Needle set

The ProtoSnap - LilyPad Development Board Simple needs a [USB Mini-B Cable](https://www.sparkfun.com/products/598) in order to connect to a computer and upload code.