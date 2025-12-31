# Source: https://learn.sparkfun.com/tutorials/qwiic-ultrasonic-distance-sensor-hc-sr04-hookup-guide

## Introduction

The [SparkFun Qwiic Ultrasonic Distance Sensor](https://www.sparkfun.com/products/17777) is great for providing non-contact distance readings from 2cm to 400cm. It improves on the classic HC-SR04 distance sensor by adding a pair of Qwiic connectors to it, so now you can communicate over I^2^C and daisy chain any other Qwiic product of your choosing.

If you prefer to bypass the Qwiic connector and I^2^C you can also access the VCC, Trigger, Echo, and Ground pins broken out on the edge of the board. Please be aware that this ultrasonic sensor comes uncalibrated and you will need manipulate the raw output for your specific application. Let\'s have a look at this fun board!

[![SparkFun Qwiic Ultrasonic Distance Sensor - HC-SR04](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/9/1/6/17777-SparkFun_Qwiic_Ultrasonic_Distance_Sensor_-_HC-SR04-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-ultrasonic-distance-sensor-hc-sr04.html)

### [SparkFun Qwiic Ultrasonic Distance Sensor - HC-SR04](https://www.sparkfun.com/sparkfun-qwiic-ultrasonic-distance-sensor-hc-sr04.html) 

[ SEN-17777 ]

The HC-SR04 distance sensor is great for non-contact distance readings from 2cm to 400cm. This unit adds a pair of Qwiic conn...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

Overall Features:

- Operating Voltage 3.3V
- Detecting Angle: 15 degrees
- Sensor range: 2cm to 400cm
- Accuracy: 3mm
- MCU on board: STM8L051
- Default I^2^C Address: 0x00
- Dimensions: 21.5 x 45.5mm
- Weight 9.2g

### STM8L051 MCU

The 8-bit ultra-low power STM8 MCU Core provides increased processing power (up to 16 MIPS at 16 MHz) while maintaining the advantages of a CISC architecture with improved code density, a 24-bit linear addressing space and an optimized architecture for low power operations. It also features embedded data EEPROM and low power, low-voltage, single-supply program Flash memory. The device incorporates an extensive range of enhanced I/Os and peripherals, a 12-bit ADC, a real-time clock, two 16-bit timers, one 8-bit timer, as well as standard communication interfaces such as an SPI, an I^2^C interface, and one USART. For more information, refer to the [datasheet](https://cdn.sparkfun.com/assets/a/5/2/f/2/STM8L051F3P6TR_PDF_C18088_2014-02-25.pdf).

[![Sensor with core highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-STM8-MCU-Core.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-STM8-MCU-Core.jpg)

### Qwiic Connectors

Our Qwiic Ecosystem makes sensors pretty much plug and play. There are two Qwiic connectors on the side of the Qwiic Distance Sensor board to provide power and I^2^C connectivity simultaneously.

[![Sensor with the Qwiic connectors highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-QwiicConnectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-QwiicConnectors.jpg)

### Power

Ideally, power will be supplied via the Qwiic connectors on either side of the board. Alternatively, power can be supplied through the pins along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **1.8**-**3.6V**.

[![Sensor with 3.3V and GND pins highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-PowerPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-PowerPins.jpg)

### Trigger and Echo Pins

If you (for some crazy reason) don\'t want to utilize the Qwiic connectors, we\'ve broken out the Trigger and Echo pins as PTH. We\'ve included headers that can be soldered in place.

[![Sensor with Trigger and Echo Pins Highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-TrigEchoPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-TrigEchoPins.jpg)

### I^2^C Jumpers

The Qwiic Ultrasonic Distance Sensor has built-in 2.2k pull-up resistors on the SDA and SCL lines. These are needed for normal I^2^C communication. The I^2^C jumper has two small traces connecting the pull-ups to 3.3V. **For general use you can leave this jumper unmodified.** If you have many (over 7) devices on the I^2^C bus, each with their own pull up resistors, then you may want to [cut the I^2^C jumpers](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) to disconnect the 2.2k resistors on each Qwiic board.

[![Sensor with I2C jumpers highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-I2CJumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-SparkFun-Qwiic-Ultrasonic-Distance-Sensor-I2CJumpers.jpg)

### Board Dimensions

Units below are in mm.

[![Board measures 45.06mm by 21.51mm](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-BoardDimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/17777-BoardDimensions.png)

## Hardware Hookup

Using the Qwiic system, assembling the hardware is simple. Connect the RedBoard to one of the Ultrasonic Distance Sensor Qwiic ports and the Qwiic OLED Display on the other Qwiic port using your Qwiic cables. Then connect the RedBoard to your computer via the MicroUSB cable and voila! You\'re ready to rock!

[![Image of all three boards hooked up via Qwiic cables](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/5/9/8/Ultrasonic_HC-SR04_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/Ultrasonic_HC-SR04_Hookup_Guide-01.jpg)

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

Our friends over at Zio have provided an example to get you started with this Ultrasonic Distance Sensor. In order to do so, you\'ll need to install a few libraries first.

To display the sensor readings on the connected Qwiic OLED, we will use three Adafruit libraries:

- [Adafruit BusIO GitHub](https://github.com/adafruit/Adafruit_BusIO)
- [Adafruit GFX GitHub](https://github.com/adafruit/Adafruit-GFX-Library)
- [Adafruit SSD1306 GitHub](https://github.com/adafruit/Adafruit_SSD1306)

#### Adafruit BusIO Library

You can install this library to automatically in the Arduino IDE\'s Library Manager by searching for \"**Adafruit BusIO**\". Or you can manually download it from the [GitHub repository](https://github.com/adafruit/Adafruit_BusIO).

[Download the Adafruit BusIO Library (ZIP)](https://github.com/adafruit/Adafruit_BusIO/archive/master.zip)

#### Adafruit GFX Library

You can install this library to automatically in the Arduino IDE\'s Library Manager by searching for \"**Adafruit GFX**\". Or you can manually download it from the [GitHub repository](https://github.com/adafruit/Adafruit-GFX-Library).

[Download the Adafruit GFX Library (ZIP)](https://github.com/adafruit/Adafruit-GFX-Library/archive/master.zip)

#### Adafruit SSD1306 Library

You can install this library to automatically in the Arduino IDE\'s Library Manager by searching for \"**Adafruit SSD1306 Library**\". Or you can manually download it from the [GitHub repository](https://github.com/adafruit/Adafruit_SSD1306).

[Download the Adafruit SSD1306 Library (ZIP)](https://github.com/adafruit/Adafruit_SSD1306/archive/master.zip)

\

[] **Pro tip:** Trying to do a search for the Adafruit libraries and not finding them? Make sure you have the Adafruit json link in your Preferences. After your SparkFun json link, of course.\
\
![Image of preferences dialog](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/AdafruitJSONinPreferences.png)

### Example 1

This example lives in the [GitHub Repo](https://github.com/sparkfun/Zio-Qwiic-Ultrasonic-Distance-Sensor) in the *Arduino* folder. Feel free to download the code, alternatively you can copy the code below into a blank Arduino sketch. Select your board (for this example we\'d select \"SparkFun RedBoard\") and the port your board has enumerated on. Go ahead and upload your code.

    language:c
    #include <Wire.h>
    #include <Adafruit_GFX.h>
    #include <Adafruit_SSD1306.h>
    #define SLAVE_BROADCAST_ADDR 0x00  //default address
    #define SLAVE_ADDR 0x00       //SLAVE_ADDR 0xA0-0xAF
    uint8_t distance_H = 0;
    uint8_t distance_L = 0;
    uint16_t distance = 0;

    #define SCREEN_WIDTH 128 // OLED display width, in pixels
    #define SCREEN_HEIGHT 32 // OLED display height, in pixels

    // Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
    #define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
    Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

    void setup() 

    void loop() 
    }

Try moving an object (like your hand or a dinosaur) closer to the sensor - notice the output of the OLED shows you how close the object is! Grr. Rawr!

[![Oh no! A dinosaur is approaching distance sensor and now it\'s only 61mm away!](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/Ultrasonic_HC-SR04.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/8/Ultrasonic_HC-SR04.gif)

*Curse your sudden but inevitable betrayal!*

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[Create New Forum Account](https://forum.sparkfun.com/ucp.php?mode=register)   [Log Into SparkFun Forums](https://forum.sparkfun.com/index.php)