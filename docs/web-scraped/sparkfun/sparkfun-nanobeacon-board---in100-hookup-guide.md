# Source: https://learn.sparkfun.com/tutorials/sparkfun-nanobeacon-board---in100-hookup-guide

## Introduction

The [SparkFun NanoBeacon Board - IN100](https://www.sparkfun.com/products/21327) and [SparkFun NanoBeacon Lite Board - IN100](https://www.sparkfun.com/products/21293) offer a 2.4 GHz wireless low energy beacon breakout with exceptional low power consumption features and minimal programming required. The two versions allow for you to prototype with the Lite (Development) version and then employ the Standard (Production) version in large installations once your hardware and software design is complete. The board features the IN100 NanoBeacon^™^ from InPlay^™^. The NanoBeacon Config Tool allows for software-free programming of the modules removing any need to perform any tricky programming for advertising settings to send and receive packets.

[![SparkFun NanoBeacon Lite Board - IN100](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/0/7/8/21293-SparkFun_NanoBeacon_Lite_Board_-_IN100-01.jpg)](https://www.sparkfun.com/sparkfun-nanobeacon-lite-board-in100.html)

### [SparkFun NanoBeacon Lite Board - IN100](https://www.sparkfun.com/sparkfun-nanobeacon-lite-board-in100.html) 

[ WRL-21293 ]

The SparkFun IN100 NanoBeacon Lite Board offers a 2.4 GHz wireless low energy BT beacon breakout with exceptional low power c...

[ [\$6.10] ]

[![SparkFun NanoBeacon Board - IN100](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/1/2/3/21327-SparkFun_NanoBeacon_Board_-_IN100-01.jpg)](https://www.sparkfun.com/sparkfun-nanobeacon-board-in100.html)

### [SparkFun NanoBeacon Board - IN100](https://www.sparkfun.com/sparkfun-nanobeacon-board-in100.html) 

[ WRL-21327 ]

The SparkFun IN100 NanoBeacon Board offers a 2.4 GHz wireless low energy BT beacon breakout with exceptionally low-power cons...

[ [\$6.10] ]

While both versions of this board use the same design, there are a few minor differences between them. The Lite version of this breakout is intended for prototyping and includes a reset button and power LED. The standard version is designed with rapid implementation requiring minimal assembly and modification so it does not have the reset button or power LED populated and has male headers soldered to board\'s through-hole pins.

In this guide we\'ll take a look at the IN100 and other hardware present on these boards, how to assemble and configure them using the NanoBeacon Config Tool as well as an example demonstrating how to use these beacons with the Qwiic BMA400.

**Important!** When programming the IN100 with the InPlay NanoBeacon Config Tool, the **\"Burn/Program\"** option uploads the settings and locks the module. Before selecting this option make sure everything is set up and working as you intend as you *cannot undo this step* and you may brick your IN100.\
\
The Config Tool offers a testing **\"Run in RAM\"** mode for many settings but I^2^C is *not* available in the RAM testing mode. Users connecting I^2^C devices to the board should ensure their code works before clicking the **\"Burn/Program\"** button.

### Required Materials

Along with either version of the beacon, you\'ll need a serial-to-UART converter for initial device configuration. After configuring the IN100 you\'ll want something to pair it with like a development board. The beacon also requires a coin cell battery for power.

[![SparkFun Serial Basic Breakout - CH340C and USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/2/15096-SparkFun_Serial_Basic_Breakout_-_CH340C_and_USB-C-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html)

### [SparkFun Serial Basic Breakout - CH340C and USB-C](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html) 

[ DEV-15096 ]

This SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G and takes advantage of the ha...

[ [\$10.50] ]

[![SparkFun FTDI Basic Breakout - 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/9/5/8/09873-01a.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html)

### [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html) 

[ DEV-09873 ]

This is the newest revision of our \[FTDI Basic\](https://www.sparkfun.com/products/retired/8772). We now use a SMD 6-pin heade...

[ [\$18.50] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![Coin Cell Battery - 12mm (CR1225)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/3/00337-01.jpg)](https://www.sparkfun.com/coin-cell-battery-12mm-cr1225.html)

### [Coin Cell Battery - 12mm (CR1225)](https://www.sparkfun.com/coin-cell-battery-12mm-cr1225.html) 

[ PRT-00337 ]

CR1225 lithium metal 3V 12mm 47mAh coin cell batteries. Perfect small battery for miniature sensor node applications. Thes...

[ [\$2.25] ]

### Required Tools

Some soldering may be required if you\'re using the Lite version. In case you need some soldering tools or components, check out the products below:

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

### Additional Materials

In the examples section of this guide we\'ll show how to send motion data recorded by the BMA400 on the SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic) to a SparkFun RedBoard IoT. If you want to follow along with this example, you\'ll want to pick one up:

[![SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/9/7/1/21208_SEN-_01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html) 

[ SEN-21208 ]

he SparkFun Qwiic BMA400 Triple Axis Accelerometer Breakout offers a 3-axis acceleration sensor perfect for ultra-low-power a...

[ [\$10.50] ]

### Suggested Reading

This board features a Qwiic connector for use with our ever-expanding Qwiic ecosystem. If you\'re not familiar with Qwiic, we recommend you head over to [this page](https://www.sparkfun.com/qwiic) for more information.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

You may also want to read through the tutorials below if you are not familiar with the concepts covered in them or would like a refresher:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/bluetooth-basics)

### Bluetooth Basics 

An overview of the Bluetooth wireless technology.

[](https://learn.sparkfun.com/tutorials/hexadecimal)

### Hexadecimal 

How to interpret hex numbers, and how to convert them to/from decimal and binary.

## Hardware Overview

Let\'s take a closer look at the IN100 and other hardware on these NanoBeacon boards.

### IN100 NanoBeacon

The NanoBeacon IN100 SoC from InPlay is an ultra low power BT beacon module compatible with common 2.4 GHz protocols.

[![Photo highlighting the IN100 NanoBeacon.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_IN100.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_IN100.jpg)

The IN100 boasts impressive features to reduce power consumption of the module to well below a microamp allowing it to be left in the field sending data packets for multiple years on a single coin cell battery. The IN100 accepts a supply voltage from **1.1-3.6V** so it can be reliably powered by a 3V CR1225 and has three power modes: Sleep, Active and Shut Down. The 2.4 GHz radio has programmable TX output power up to +5 dBm.

The module can also be configured to act as a Google^™^ Eddystone^™^ and Apple^®^ iBeacon^®^ compliant device. For a complete overview of the IN100, refer to the module\'s [datasheet](https://cdn.sparkfun.com/assets/3/d/5/5/1/IN100-Datasheet.pdf).

The IN100 includes the following peripheral options:

- One UART,
- Eight GPIO pins (four with multiple function options including I^2^C and ADC)
- 11-bit ADC for measuring chip temperature and Vcc voltage with four channels available on GPIOs
- Two load switches for controlling power to peripheral devices
- Pulse count interface compatible with one-wire sensors.

These options let users connect a wide assortment of peripheral devices to the NanoBeacon and then broadcast the data wirelessly to other devices.

### Through Hole Headers

The breakouts route most of the IN100\'s pins to a pair of 0.1\"-spaced plated through hole (PTH) headers. The standard version comes with two male headers soldered to these pins.

[![Photo highlighting the through-hole headers.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_PTHs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_PTHs.jpg)

One side has a UART interface to mate with a 3.3V Serial Basic (or similar UART to Serial converter) for USB communication and configuring the IN100 through the Config Tool.

The other side breaks out four of the IN100\'s GPIO pins (pins 4-7) as well as the two I/O power switches (SW0 and SW1).

### Qwiic Connector

The Qwiic connector on the board uses I/O pins 2 and 3 for SCL and SDA, respectively. Using this connector requires enabling I^2^C on the IN100 in the Config Tool.

[![Photo highlighting the Qwiic connector.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Qwiic.jpg)

The board design allows for the IN100 to control both communication and power to a connected Qwiic device so you can configure the IN100 to toggle power a device on for a quick measurement and back off to conserve power. By default, power to the Qwiic connector is controlled by the Switch 0 (SW0) pin allowing users to toggle power on and off to a connected Qwiic device. Users who prefer to have a Qwiic device continuously powered from Vcc can adjust the BUS jumper. Read on to the Solder Jumpers section for more information.

### Power Options

The NanoBeacon Boards have two power options: coin cell battery or Vcc on the UART header.

[![Photo highlighting the Battery holder and UART Header.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Power.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Power.jpg)

**Important!** Only power the NanoBeacon Board through one of the two power inputs (VBATT or VCC) as they both connect to the IN100\'s Vcc and are netted together.

#### Battery Holder

The breakout includes a 12mm coin cell battery holder to power the board. Use only 3V CR1225 batteries in this holder. The IN100 supply voltage range goes all the way down to 1.1V so, with the right settings, the board can run off a coin cell battery until it is essentially completely drained.

#### UART Header

The IN100 can also be powered directly through the **VCC** pin from a dedicated power supply or over USB when connected to a USB to Serial converter like the Serial Basic. Make sure the voltage here falls into the IN100\'s supply voltage range (**1.1-3.6V**).

### Reset Button

The Lite version includes a Reset button for quickly resetting the board during prototyping.

### LED

The sole LED on this board is the Power LED indicating power to the board. The Production version of this breakout does not include this LED to help conserve power and reduce customization time.

[![Photo highlighting Power LED.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Power_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Power_LED.jpg)

### Solder Jumpers

The Beacon Breakout includes three solder jumpers labeled: **PWR**, **I2C**, and **BUS**. The table below outlines their labels, default state, function and any notes on their use.

[![Photo highlighting solder jumpers.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Jumpers.jpg)

  Label   Default State   Function                                                   Notes
  ------- --------------- ---------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PWR     CLOSED          Completes Power LED circuit                                Open to disable the Power LED
  I2C     CLOSED          Three-way jumper that pulls IO3 and IO4 (SDA/SCL) to Vcc   Open completely to disable the pull up resistors on these lines
  BUS     SEE NOTE        Three-way jumper controlling IO power source               By default, this nets Qwiic Vcc to SW0 to toggle power to the connector. Sever the trace connecting the center and \"SW\" pad and solder the center and \"VCC\" pad together to switch to Qwiic power supply to Vcc (always on).

### Notes Pad

Last but not least, the NanoBeacon boards include a \"Notes\" pad for users to write on. This lets you quickly differentiate between NanoBeacon boards to help keep track of them without needing to plug them into your computer.

[![Highlighting the Notes pad.](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Notes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Board_-_Notes.jpg)

### Board Dimensions

We designed the NanoBeacon boards to match our 1\"x1\"(25.4mm x 25.4mm) Qwiic standard and has two mounting holes that fit a [4-40 screw](https://www.sparkfun.com/products/10453).

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/e/3/1/f/a/SparkFun_NanoBeacon_Board_-_IN100_-_Dimensions.png)](https://cdn.sparkfun.com/assets/e/3/1/f/a/SparkFun_NanoBeacon_Board_-_IN100_-_Dimensions.png)

## Hardware Assembly

Now that we\'re familiar with the hardware present on these NanoBeacon boards, we\'ll assemble our circuit for the Qwiic BMA400 example.

### Solder

For this demo, we\'re using the Lite version of the NanoBeacon Board so we need to solder headers to the UART pins to connect a Serial Basic to for configuring the IN100 through the Config Tool.

[![Photo showing headers soldered to NanoBeacon Lite.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_-_Headers_Soldered_Top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_-_Headers_Soldered_Top.jpg)

### Qwiic BMA400 Circuit

With headers soldered in place, connect the Serial Basic to them taking care to match the pins. At this point, you can also connect the Qwiic BMA400 to the Qwiic connector on the NanoBeacon Board. With everything connected, your circuit should be nearly identical to the one pictured below:

[![Completed NanoBeacon circuit with Qwiic BMA400](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_-_Qwiic_Circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_-_Qwiic_Circuit.jpg)

With our NanoBeacon Board assembled and connected to a Serial Basic, we can move on to plugging it into our computer and configuring the IN100 to test basic functionality and later upload the BMA400 data configuration file.

## NanoBeacon Config Tool

InPlay\'s NanoBeacon Config Tool provides an easy, software-free GUI to configure and program the IN100. In this section we\'ll take a closer look at the features of the tool and a quick look at the basic set up required to have the beacon begin to advertise and transmit data packets.

This is just a quick overview of the Config Tool so for complete information on everything the tool offers, refer to InPlay\'s [NanoBeacon Config Tool User Guide](https://cdn.sparkfun.com/assets/b/e/d/a/f/NanoBeacon_Config_Tool_User_Guide_EN.pdf).

**Important!** When programming the IN100 with the InPlay NanoBeacon Config Tool, the **\"Burn/Program\"** option uploads the settings and locks the module. Before selecting this option make sure everything is set up and working as you intend as you *cannot undo this step* and it is possible to brick your IN100.\
\
The Config Tool offers a testing **\"Run in RAM\"** mode for many settings but I^2^C is *not* available in the RAM testing mode. Users connecting I^2^C devices to the board should ensure their code works before clicking the **\"Burn/Program\"** button.

### Download and Installation

You can get the Config Tool from InPlay\'s website:

[NanoBeacon Config Tool](https://inplay-tech.com/nanobeacon-config-tool)

If you want to use the InPlay scanner app on your phone, you can download it here as well. Depending on your operating system, you may need to install an unzipping tool. The Windows version is a 7-Zip file so users may need to install the [7-Zip Tool](https://www.7-zip.org/).

After downloading and uncompressing the files, navigate to the location you set, open the \"NanoBeacon Tools\" folder, and search for the **\"NanoBeaconConfigTool\"** application to open the program.

### Config Tool GUI

With the Config Tool open, let\'s take a quick look at some of the features of the Config Tool:

[![Screenshot of the basic Config Tool GUI window.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Interface.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Interface.jpg)

*Having trouble seeing the detail in this image? Click on it for a larger view.*

The first thing you want to take note of is the UART box in the top-right of the GUI. This is where you\'ll select the Port your Serial Basic or other Serial-to-UART is connected to. Click the **\"Probe\"** button, select the correct port and click **\"Connect\"** (If you\'re not sure which port is correct, disconnect and reconnect the Serial Basic and check which port disappears/appears).

[![Screenshot showing successful connection in Config Tool.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Connected.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Connected.jpg)

*Having trouble seeing the detail in this image? Click on it for a larger view.*

From here you can configure all sorts of settings and enable different features in the tabs on the left labeled **\"Application Settings\"**. For now, we\'re going to move on to a basic, \"Hello World\" functionality test to make sure the IN100 is working properly.

### \"Hello World\" Test

As a simple functionality test, we\'ll perform a basic configuration of the IN100 to set it up as an Eddystone device we can scan for using the InPlay scanner app (or other scanner app such as nRF Connect).

For this test we\'re going to set up the IN100 to operate as a bare-bones Eddystone device but you can select a different option if you prefer. For this test, select the **\"Advertising\"** tab under **\"Application Settings\"** and click the **\"Edit\"** button for **\"Advertising Set #1\"**. In the **\"Advertising Data\"** tab select **\"Eddystone\"** and then click **\"Ok\"**. This default setting works fine for our quick functionality test but if you do use the NanoBeacon as an Eddystone device in a more permanent setting, make sure to follow their guidelines linked in the note below.

[![Screenshot of Eddystone settings selected for advertising data.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Eddystone.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_Eddystone.jpg)

*Having trouble seeing the detail in this image? Click on it for a larger view.*

With the advertising settings confirmed, click the **\"Run in RAM\"** button and open the InPlay scanner app or your chosen alternate application and the NanoBeacon should show up as an Eddystone device with the name \"**N/A**\".

**Note:** Make sure to follow the guidelines and regulations for your selected mode when configuring the advertising data and settings to avoid using reserved UUIDs and other settings. Guidelines for Eddystone devices can be found [here](https://github.com/google/eddystone/blob/master/protocol-specification.md) and iBeacon [here](https://developer.apple.com/ibeacon/). For the Custom mode, ensure you follow the related specifications and regulations. [This page](https://www.bluetooth.com/specifications/) offers a good starting place for using the Custom mode.

## BMA400 Qwiic Example

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Now that we know the IN100 is working and advertising, let\'s use a custom config file to send acceleration data from the SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic) to a RedBoard IoT running code to convert the values into a serial printout.

### Required Libraries & Board Tools

This example assumes the use of the [SparkFun IoT RedBoard](https://www.sparkfun.com/products/19177) board file as well as several libraries that do not come pre-installed with Arduino. Make sure to install both the board files and libraries prior to using this example. The SparkFun IoT RedBoard uses the ESP32 Dev Module board definition included in the **\"esp32\"** boards package. For detailed information on installing and using the IoT RedBoard, check out [this section](https://learn.sparkfun.com/tutorials/iot-redboard-esp32-development-board-hookup-guide/software-setup-and-programming) of our Hookup Guide for the board. Install the libraries used in this example with the Arduino Library Manager tool by searching for **\"ESP32 BLE Arduino\"**.

### Qwiic BMA400 Config File

With the board files and libraries installed we can move on to loading the Qwiic BMA400 config file from the Examples folder in the GitHub repository. This also contains the Arduino code so go ahead and download both (or the whole repository).

[SparkFun NanoBeacon Board - IN100 GitHub Repository (ZIP)](https://github.com/sparkfun/SparkFun_NanoBeacon_Board_-_IN100/archive/refs/heads/main.zip)

This config file contains all of the I^2^C commands as well as custom advertising data settings to name the NanoBeacon **\"BMA400_Data\"** and have it send voltage and I^2^C data. You can modify this if necessary but for a quick personal test, these settings should be just fine. You can view the I^2^C commands in the **\"I2C\"** window as shown below:

[![Screenshot showing I2C settings in Config Tool for BMA400 example.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_I2C_Settings.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/8/4/7/NanoBeacon_Config_Tool_I2C_Settings.jpg)

*Having trouble seeing the detail in this image? Click on it for a larger view.*

After loading the config file and adjusting anything you see fit, click the **\"Burn/Program\"** button. Reminder, this is a **one-time** use button and there is **no** confirmation prompt. Any settings here are saved permanently to the IN100 so if you do change anything here, make sure it works before clicking this button.

### Arduino Code

With just the config file loaded on the NanoBeacon, you can open up a scanner app and watch the acceleration data print out in hex but that isn\'t very human-readable. To convert this hex data to a serial print, we wrote a quick Arduino sketch that connects to a NanoBeacon board running the config file we just uploaded and then parses the hex data into a serial print to easily ready acceleration data from all three of the BMA400\'s axes.

Open the sketch file or copy the code below into a blank Arduino sketch. Select your board (in our case **\"ESP32 Dev Module\"**) and Port and click the upload button.

    language:c
    #include <BLEDevice.h>
    #include <BLEUtils.h>
    #include <BLEScan.h>
    #include <BLEAdvertisedDevice.h>
    #include <BLEEddystoneURL.h>
    #include <BLEEddystoneTLM.h>
    #include <BLEBeacon.h>

    int scanTime = 1;
    BLEScan *pBLEScan;

    // This class is used for the onResult() callback function
    class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks
    
        }
      }
    };

    void setup()
    

    void loop()
    

After uploading, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the baud set to **115200**. The code will start to scan for the matching NanoBeacon device (BMA400_Data) and when it succeeds, prints out the data sent by the beacon including Manufacturer ID, voltage measured on Vcc and the acceleration data of the x/y/z axes.

### Additional Config Tests

For those who want to go beyond this example or prefer to send I^2^C data from different devices, InPlay has a growing list of other config tests for other sensors, like the [BME280 atmospheric sensor](https://www.sparkfun.com/products/15440), available from the GitHub repository below:

[InPlay Config Examples](https://github.com/NanoBeacon/config-files)

## Troubleshooting

### NanoBeacon and NanoBeacon Lite Version Differences

As we covered before, the two versions of the NanoBeacon board share the same design but with a few different features.

**NanoBeacon**

- Pre-Soldered Male Headers
- Power LED not included
- Reset Button not included

**NanoBeacon Lite**

No Male Headers

Power LED

Reset Button

### NanoBeacon Config Tool Tips

Here are a couple of tips we found useful while working with the NanoBeacon Config Tool

#### One-Time Burn/Program

One final reminder, the **\"Burn/Program\"** button is a permanent action and does **NOT** have a confirm prompt. Make sure to test any settings you can in the **\"Run in RAM\"** option to confirm everything is working and configured properly before pressing the **\"Burn/Program\"** button.

#### Reset Button

Sometimes the Config Tool will not be able to connect to the IN100 after running things in RAM. We found disconnecting the device in the program and reconnecting works in most cases. If it still gets stuck, push the Reset button on the Lite version or power cycle the standard version and it should resolve the issue.

#### NanoBeacon Advertising Settings Guidelines

All three advertising setting options (Eddystone, iBeacon, and Custom) should adhere to the protocol guidelines for each mode. Make sure to follow the guidelines for your selected mode by referring to their documentation linked below:

- [Eddystone](https://github.com/google/eddystone/blob/master/protocol-specification.md)
- [iBeacon](https://developer.apple.com/ibeacon/)
- [Custom](https://www.bluetooth.com/specifications/)

#### Increasing NanoBeacon Performance and Range

If you really need to squeeze out a little more performance from this board, InPlay suggests adjusting a couple of settings in the **\"XO\"** option under **\"Global Settings\"**. First, changing the Internal Capacitor Code from **8** to **11** can add roughly 5-10dB performance which can help increase the range of the IN100. Second, changing the Strength Code from 16 to 19 should also help with overall performance.