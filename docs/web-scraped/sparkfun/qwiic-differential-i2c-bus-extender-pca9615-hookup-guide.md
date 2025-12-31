# Source: https://learn.sparkfun.com/tutorials/qwiic-differential-i2c-bus-extender-pca9615-hookup-guide

## Introduction 

The [Qwiic Differential I^2^C Breakout](https://www.sparkfun.com/products/14589) is the fastest and easiest way to extend the range of your I^2^C communication bus. The breakout uses NXP\'s PCA9615 IC, which converts the two default I^2^C signals into four differential signals: two for SCL and two for SDA. Coupled with the ease of [SparkFun\'s Qwiic connection system](https://www.sparkfun.com/qwiic), the differential I^2^C breakout board makes it easier to connect it to the rest of your system. The differential signals are sent over an Ethernet cable, which attaches to the breakouts through the on-board RJ-45 connectors. The differential signaling allows the I^2^C signals to reach distances of up to 100ft. while still maintaining their signal integrity!

[![SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/4/5/14589-SparkFun_Differential_I2C_Breakout_-_PCA9615__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14589)

### [SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://www.sparkfun.com/products/14589) 

[ BOB-14589 ]

The SparkFun Differential I2C Breakout is the fastest and easiest way to extend the range of your I2C communication bus.

**Retired**

Whether you need to extend the range of an I^2^C sensor on an autonomous vehicle plagued with noise from motors or want to create a vast sensor network in your home or office, the Qwiic differential I^2^C breakout is a great solution to extend distance and reduce noise susceptibility.

### Required Materials

To follow along with this project tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

- 2x [Qwiic Differential I^2^C breakouts](https://www.sparkfun.com/products/14589).
- A straight-through Ethernet cable (up to 100ft in length).
- A [microcontroller](https://www.sparkfun.com/categories/300) or [single board computer](https://www.sparkfun.com/categories/394) capable of I^2^C.
- An [I^2^C sensor](https://www.sparkfun.com/categories/tags/i2c) to communicate with on the other end of the I^2^C bus.
- If using the Qwiic connectors, two [Qwiic cables](https://www.sparkfun.com/search/results?term=qwiic+cable).

### Tools

You may need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), and a hobby knife depending on your setup.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[](https://learn.sparkfun.com/tutorials/qwiic-hat-for-raspberry-pi-hookup-guide)

### Qwiic HAT for Raspberry Pi Hookup Guide 

Get started interfacing your Qwiic enabled boards with your Raspberry Pi. This Qwiic connects the I2C bus (GND, 3.3V, SDA, and SCL) on your Raspberry Pi to an array of Qwiic connectors.

## Hardware Overview

The simplicity of the Qwiic differential I^2^C breakout is one of its biggest appeals. Other I^2^C communication methods require packetizing I^2^C communication into another protocol, be it [RS-485](https://en.wikipedia.org/wiki/RS-485) or [1-Wire](https://en.wikipedia.org/wiki/1-Wire). However, the PCA9615 keeps the I^2^C protocol by utilizing a differential transceiver. In this section, we\'ll take a closer look at the board to better understand how it works.

### Pinout

Below are the plated through hole pins that are broken out on the board. The I^2^C pins are connected to the two Qwiic connectors on the sides.

[![Highlight of PTH Pins](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Pin_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Pin_Highlight.jpg)

#### PTH Connections

- **GND** - Ground
- **VDDA** - **2.3VDC to 5.5VDC**. I^2^C-bus side power supply.
- **VDDB** - **3.0VDC to 5.5VDC**. Differential side power supply. If jumper \"**VDD A-B**\" is not shorted, then VDDB will need to be powered for the differential I^2^C bus to operate.
- **SDA** - I^2^C data signal.
- **SCL** - I^2^C clock signal.
- **EN (optional)** - PCA9615 enable (active high, internally pulled up). This is used to disable the bus buffer, and is useful for fault finding, power-up sequencing, or reconfiguration of a large bus system by isolating sections not needed at all times.

#### Qwiic Connections

- **GND** - Ground.
- **VDDA** - **2.3VDC to 5.5VDC**. I^2^C-bus side power supply. If \"**VDD A-B**\" is not shorted, VDDB will need to powered separately for the differential I^2^C bus to operate.
- **SDA** - I^2^C data signal.
- **SCL** - I^2^C clock signal.

### VDDA vs VDDB

To power the board, VDDA must be present and be the same logic voltage as the SDA/SCL lines, while VDDB is used to power the differential I^2^C bus. By default, the jumper labeled \"**VDD A-B**\" is closed, which connects the VDDA rail to the VDDB rail. By cutting the jumper you can separate the two rails which would allow for one rail to operate at 3.3V while the other can operate at 5V.

[![Highlight of VDDA,VDDB,VDD Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_VDD_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_VDD_Highlight.jpg)

#### VDDB and Ground Jumpers

If the number of sensors connected on the other side of the extended I^2^C bus is minimal, you can power them over the Ethernet cable. However, if there are numerous sensors connected, it is advised that both ends be powered separately. To isolate the power supplies at both ends of the Ethernet cable, use a sharp blade to cut the small traces betweens the pads of the jumpers labeled \"**VDDB**\" and \"**GND**\". VDDB will still be present on each board, but the Ethernet cable will not carry any current to power a device at the other end of the cable.

[![Bottom Jumper Highlight](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Bottom_Jumper_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Bottom_Jumper_Highlight.jpg)

### Differential Signals

From the bottom of the board, we can see which pins the RJ-45 connector uses for the differential signaling. The board has been designed to use a standard Ethernet cable. If a custom cable is made, make sure to connect a twisted pair for pins 1 and 2 (**DSCL-**, **DSCL+**) and pins 7 and 8 (**DSDA-**, **DSDA+**).

[![Highlight of RJ-45 Differential Signals](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Differential_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_Differential_Highlight.jpg)

### I^2^C Pull-Up Resistors

As with most SparkFun I^2^C products, there is a jumper for the pull-up resistors on the I^2^C bus. If multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but **one** pair of pull-up resistors if multiple devices are connected to the bus.

[![I2C Pull-Up Resistor Jumper Highlight](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_I2C_PU_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_I2C_PU_Highlight.jpg)

## Hardware Assembly

Ethernet cables used must be straight-through (i.e. Pin 1 on one side of the cable is connect to pin 1 on the other side. The same for pin 2 and so on.).

[![Differential Boards Connected via I2C](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-01.jpg)

### I^2^C Pull-Up Resistors

Remember, each individual non-differential I^2^C bus needs at least one set of pull-up resistors enabled. Make sure you keep track of which devices have their I^2^C pull-ups enabled and which do not.

### Power Schemes

With two power supply rails and quite a few jumpers, it\'s easy to feel confused about how to power the differential I^2^C bus extender. In this section, we\'ll go over the different ways you can power your project.

#### VDD_A == VDD, [Power Whole Bus (Default)]

[![Highlight of VDD Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_VDD_Highlight_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/14589-I2CBusExtender_PCA9615_VDD_Highlight_2.jpg)

- VDD_A and VDD_B are connected.
- Both are powered at 3.3V.
- Power is connected to a twisted pair of the Ethernet cable and sent to the peripheral nodes.
- No power is required at the peripheral nodes.

------------------------------------------------------------------------

#### VDD_A != VDD_B, [Power Whole Bus]

[![VDD Jumper Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-06.jpg)

 

- VDD A-B jumper trace has been cut.
- Separate power supply (3.0-5.5V) is supplied to VDD_B, while VDD_A remains at 3.3V.
- VDD_B voltage is connected to a twisted pair of the Ethernet cable and sent to the peripheral nodes.
- No power is required at the peripheral nodes.

------------------------------------------------------------------------

#### VDD_A == VDD\_ B, [Power Each Node Separately]

 

[![Bottom Jumpers Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-04.jpg)

 

- VDD_A and VDD_B are connected.
- Both are powered at 3.3V.
- Jumpers underneath board (VDDB and GND) are cut and power is **NOT** connected to the Ethernet cable.
- Each peripheral node is powered individually with 3.3V only. Differential I^2^C signals are the only connections on the bus.

------------------------------------------------------------------------

#### VDD_A != VDD\_ B, [Power Each Node Separately]

 

[![VDD_A != VDD\_ B, Powering Each Node Separately by cutting VDD, VDDB, and GND](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-56.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-56.jpg)

 

- VDD A-B jumper trace has been cut on the top of the board.
- Separate power supply (3.0-5.5V) is supplied to VDD_B, while VDD_A remains at 3.3V.
- Jumpers underneath board (VDDB and GND) are cut and power is **NOT** connected to the Ethernet cable.
- Each peripheral node is powered individually with 3.3V only. Differential I^2^C signals are the only connections on the bus.

------------------------------------------------------------------------

#### VDD_A == VDD\_ B, [Power Whole Bus (Non-Qwiic Option)]

[![Non-Qwiic Default](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-07_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-07_2.jpg)

- VDD_A and VDD_B are connected.
- Both are powered at 5V.
- Power is connected to a twisted pair of the Ethernet cable and sent to the peripheral nodes.
- No power is required at the peripheral nodes.

------------------------------------------------------------------------

#### VDD_A == VDD\_ B, [Power Each Node Separately (Non-Qwiic Option)]

 

[![Bottom Jumpers Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-04.jpg)

 

- VDD_A and VDD_B are connected.
- Both are powered at 5V.
- Jumpers underneath board (VDDB and GND) are cut and power is **NOT** connected to the Ethernet cable.
- Each peripheral node is powered individually with 5V only. Differential I^2^C signals are the only connections on the bus.

## I2C Bus Extender Example

For this example, we\'re going to use our [Environmental Combo Breakout](https://www.sparkfun.com/products/14348) using the Differential I^2^C Bus Extender. To follow along in this example, you\'ll need the following:

You\'ll also need a straight-through Ethernet cable (up to 100ft).

### Hardware Hookup

You\'ll first need to [solder the headers](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) on to the Qwiic shield and then connect the shield to the Redboard. Once that\'s done, you can connect one of the differential I^2^C to your Redboard as shown below using one of the Qwiic cables.

[![Redboard Connected to Differential I2C using Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-02.jpg)

On the other end, all that\'s needed is to connect the environmental combo sensor to the other differential I^2^C using another Qwiic cable as shown below.

[![Sensor Connected to Differential I2C using Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Qwiic_Differential_I2C_Bus_Extender_PCA9615_Hookup_Guide-03.jpg)

### Arduino Library Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'re going to use the code from the [environmental combo sensor\'s hookup guide](https://learn.sparkfun.com/tutorials/ccs811bme280-qwiic-environmental-combo-breakout-hookup-guide#library-overview).

[](https://learn.sparkfun.com/tutorials/ccs811bme280-qwiic-environmental-combo-breakout-hookup-guide)

### CCS811/BME280 (Qwiic) Environmental Combo Breakout Hookup Guide 

September 8, 2017

Sense various environmental conditions such as temperature, humidity, barometric pressure, eCO2 and tVOCs with the CCS811 and BME280 combo breakout board.

Since we are using the environmental combo sensor, the BME280 and CCS811 libraries need to be installed. SparkFun has written libraries to control both the CCS811 and the BME280. You can obtain these libraries through the Arduino Library Manager. Search for **SparkFun BME280** and **SparkFun CCS811** to install the latest version. If you prefer downloading the libraries, you can grab them here to manually install:

[Download the SparkFun BME280 Library (ZIP)](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/master.zip)

[Download the SparkFun CCS811 Library (ZIP)](https://github.com/sparkfun/SparkFun_CCS811_Arduino_Library/archive/master.zip)

### Example Code

With the sensor connected via the I^2^C bus extender, we will use example 2 of the environmental combo breakout. Assuming that you have installed the library for both sensors, copy the code below and paste it into your Arduino IDE and upload the sketch to your board.

    language:c
    #include <SparkFunBME280.h>  //https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/
    #include <SparkFunCCS811.h>  //https://github.com/sparkfun/SparkFun_CCS811_Arduino_Library/

    #define CCS811_ADDR 0x5B //Default I2C Address
    //#define CCS811_ADDR 0x5A //Alternate I2C Address

    //Global sensor objects
    CCS811 myCCS811(CCS811_ADDR);
    BME280 myBME280;

    void printData()
    

    void printDriverError( CCS811Core::status errorCode )
    
    }

    void setup()
    
      else
      

      //Initialize BME280
      //For I2C, enable the following and disable the SPI section
      myBME280.settings.commInterface = I2C_MODE;
      myBME280.settings.I2CAddress = 0x77;
      myBME280.settings.runMode = 3; //Normal mode
      myBME280.settings.tStandby = 0;
      myBME280.settings.filter = 4;
      myBME280.settings.tempOverSample = 5;
      myBME280.settings.pressOverSample = 5;
      myBME280.settings.humidOverSample = 5;

      //Calling .begin() causes the settings to be loaded
      delay(10);  //Make sure sensor had enough time to turn on. BME280 requires 2ms to start up.
      byte id = myBME280.begin(); //Returns ID of 0x60 if successful
      if (id != 0x60)
      
      else
      
    }

    void loop()
    
      else if (myCCS811.checkForStatusError()) //Check to see if CCS811 has thrown an error
      

      delay(2000); //Wait for next reading
    }

Once uploaded, open your favorite [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/) to the port assigned to the Arduino. You should see something like similar to the output below:

[![Serial Monitor Output Window](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/2/Environmental_Combo_Serial_Window.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/2/Environmental_Combo_Serial_Window.PNG)