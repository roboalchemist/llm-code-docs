# Source: https://learn.sparkfun.com/tutorials/wireless-joystick-hookup-guide

## Introduction

**Heads up!** Originally, this tutorial was written to configure an XBee Series 1 to communicate in transparency mode. However, this can apply to the XBee Series 3 module as long as you configure the firmware to the legacy 802.15.4 protocol. For more information, check out the [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) tutorial.

The [Wireless Joystick Kit](https://www.sparkfun.com/products/14051) provides an easy way to control your next XBee project. Before the Wireless Joystick, radio controlled projects used hobby RC transmitters, the same that are used for RC cars, boats, and planes. The problem with these transmitters is many aren\'t customizable, and the ones that are, tend to be too expensive for many of us. The Wireless Joystick aims to bring a custom wireless solution for those that want to control their project the way they want to, not the way they\'re forced to.

[![SparkFun Wireless Joystick Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/9/0/14051-02.jpg)](https://www.sparkfun.com/sparkfun-wireless-joystick-kit.html)

### [SparkFun Wireless Joystick Kit](https://www.sparkfun.com/sparkfun-wireless-joystick-kit.html) 

[ KIT-14051 ]

The SparkFun Wireless Joystick Kit provides an easy way to control your next XBee project.

[ [\$44.95] ]

### Suggested Reading

Before getting started, you may find the following links useful:

- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [SAMD21 Mini/Dev Breakout Hookup Guide](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)
- [XBee Buying Guide](https://www.sparkfun.com/pages/xbee_guide)
- [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [I^2^C Protocol](https://learn.sparkfun.com/tutorials/i2c)
- [LiPo Charging Guide](https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide)

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide)

### LiPo USB Charger Hookup Guide 

How to charge your LiPo batteries with the USB LiPo charger. Plus how to modify your charger to set the charge current.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

[](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)

### SAMD21 Mini/Dev Breakout Hookup Guide 

An introduction to the Atmel ATSAMD21G18 microprocessor and our Mini and Pro R3 breakout boards. Level up your Arduino-skills with the powerful ARM Cortex M0+ processor.

## Kit Overview

Let\'s go over the Wireless Joystick Kit in detail. The kit comes with the following:

- 1 - Wireless Joystick board
- 2 - [Right Angle Tactile Buttons](https://www.sparkfun.com/products/10791)
- 2 - [Thumb Joysticks](https://www.sparkfun.com/products/9032)
- 4 - [Momentary Pushbutton Switches](https://www.sparkfun.com/products/9190)

The following is not provided in the kit and will need to be purchased separately.

Picking the right [battery](https://www.sparkfun.com/categories/54) depends on the use, but we recommend using at least a 400 mAh battery. If you\'ve never used [Xbee](https://www.sparkfun.com/categories/111) before, it\'s also recommended to use a pair of Series 1 XBees, or check out our [XBee buying guide](https://www.sparkfun.com/pages/xbee_guide).

### Wireless Joystick Board Overview

The Wireless Joystick board comes with the following:

- SAMD21 Microcontroller
- Adjustable battery charger (**Default 500mA max charge rate**)
- MAX17043G LiPo fuel gauge
- Programmable LED connected to D13
- Two trigger buttons
- Room for 2 Thumb Joysticks, or 1 Thumb Joystick and 4 push buttons

## Hardware Hookup

The first step is to solder in the right angle tactile buttons. These are meant to inserted from the bottom the board and soldered to the top layer of PCB. This will look like the image below.

[![Bottom view close up of trigger buttons](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-03.jpg)

The way the rest of the board is soldered really depends on what it will be used for. There are few different configurations for the joystick(s) and buttons. Read on to see he different configurations.

### Dual Joysticks

In this configuration, the Wireless Joystick uses both joysticks and is perfect for tank steering robots. Tank steering maps the vertical position of the left and right joysticks to the speed and direction of the left and right motors of a robot. After soldering in the joysticks, the board should look like this:

[![Dual Joysticks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-02.jpg)

### Single Joystick

In this configuration, the Wireless Joystick uses a single joystick on the left and 4 of our 12mm momentary pushbuttons on the right. This setup is similar to what older console game consoles used. After soldering in the joystick and switches, the Wireless Joystick board will look like the image below.

[![Gamepad configuration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-01.jpg)

**A quick tip about soldering the joystick(s):** Sometimes during shipping, the pins on the joystick can be bend slightly. Before trying to insert the pins to the board, make sure all of the pins look straight and run parallel with the others. When soldering the joysticks, start with the pins on the vertical and horizontal potentiometers, and use a pair of tweezers to motivate the pins into place and work my way to the select button.

### Mounting the LiPo Battery

To secure the battery to the board, we recommend using a small piece of foam double sided tape. We\'ve found the easiest place to put the battery is under the right joystick. Before mounting the battery, make sure to **trim the the joystick solder joints to avoid puncturing the battery!**

[![trimmed solder joints](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-04.jpg)

*Trimmed Solder Joints For LiPo Battery*

[![Battery taped](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-05.jpg)

*LiPo Battery with Double Sided Foam Tape*

[![Battery mounted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-06.jpg)

*Attached LiPo Battery*

### Setting the Battery Charge Rate

By default, the charge rate is set to the **maximum rate of 500mA**. If you\'re battery is larger than 500mAh, you can skip ahead to the Arduino Examples section. If you\'re using less than a 500mAh battery, you should solder in the appropriate resistor that we\'ll determine below.

The life of a lithium battery is dependent on a few factors: number of charge/discharge cycles, charge/discharge rate, battery temperature, as well as a few others. When charging a lithium battery, it\'s recommended not to exceed a 1C charge rate. For example, if you have a 400mAh battery, your current to charge the battery should not exceed 400mA. To change the rate, move the solder jumper so that the middle and R_PROG pads are shorted. Then solder in the appropriate resistor. To calculate the right resistor, use the equation below:

**R_PROG = 1000 / I_PROG**

R_PROG = Resistor value in kohms

I_PROG = Desired current value in mA

To charge the battery, simply plug in the micro USB cable, and move the switch to the **OFF** position. If your charge rate is below 200mA, the board should charge without issue regardless of the power switch position. Faster charge rates may require the switch to be off to cut current to everything but the charging circuit if charging from a computer\'s USB port or small USB chargers.

## Installing SAMD21 Board Add-Ons

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Now that the hardware is all set, lets look at some software examples. Before we get started though, make sure you have both the Arduino SAMD and the Sparkfun SAMD board definitions installed. If you need some help with this, check out the [SAMD21 Mini/Dev Breakout Hookup Guide](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/setting-up-arduino).

[](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)

### SAMD21 Mini/Dev Breakout Hookup Guide 

November 12, 2015

An introduction to the Atmel ATSAMD21G18 microprocessor and our Mini and Pro R3 breakout boards. Level up your Arduino-skills with the powerful ARM Cortex M0+ processor.

### Drivers

**Heads up!** Please be aware that the SparkFun Wireless Joystick Kit is **NOT currently supported on Windows 8** due to a lack of support drivers for those specific OS\'s.

The wireless joystick shows up on your computer as a USB storage device **without having to install drivers** for Windows 10, Mac, and Linux! They should automatically install for Windows 10 without any issues.

### Windows 7

For Windows 7, you will need to install the SAMD drivers using the [SAMD Windows 7 Installer](https://github.com/sparkfun/samd_windows7_installer/releases). Click on the link below to download and follow the prompts to install.

[SAMD Windows 7 Installer](https://github.com/sparkfun/samd_windows7_installer/releases)

For help installing the drivers, refer to our [instructions in the SAMD21 Breakout hookup guide](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/drivers-if-you-need-them#windows-7).

## Arduino Examples

**Heads up!** We\'ve found that certain XBee Series 3 Modules require the reset pin to be toggled at startup. For more information, check out the application note under [Compatibility with XBee 3\'s](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu#xbee3compatibility).

### Example 1: Remote Tank Steering Motor Controller

For our first example, let\'s try controlling a robot using tank steering. To use tank steering, you\'ll need to solder in both joysticks. This examples uses the following parts.

To connect everything, start by soldering the \"+\" pin of the male deans connector to the motor driver pin that says \"MAX 11V\" as well as to the 5V pin on the XBee Explorer. Connect the \"-\" pin of the male deans connector to \"GND\" on both the motor driver, and XBee Explorer. Next we\'ll connect the \"DOUT\" pin of the explorer to the \"RX\" pin of the motor driver. Solder the motors to the B1/B2 and A1/A2, but be sure the solder the second motor opposite of the first, so that they\'ll both be spinning in the same direction. The wheels attach to the motors with a friction fit, so carefully push those onto the motor\'s D-shaft. Finally, attach the XBees to the Wireless Joystick, as well as the to the XBee Explorer.

#### Adding the Code to the Wireless Joystick

Now that we have everything wired up and soldered together, let\'s put some code on the Wireless Joystick! To use this example, copy the code below to the Arduino IDE. Make sure you **select the SparkFun SAMD21 Dev Breakout as your board**.

    language:c
    /* Wireless Joystick Tank Steering Robot Example
     * by: Alex Wende
     * SparkFun Electronics
     * date: 9/28/16
     * 
     * license: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
     * Do whatever you'd like with this code, use it for any purpose.
     * Please attribute and keep this license.
     * 
     * This is example code for the Wireless Joystick to control a robot
     * using XBee. Plug the first Xbee into the Wireless Joystick board,
     * and connect the second to the SparkFun Serial Motor Driver.
     * 
     * Moving the left and right joystick up and down will change the
     * speed and direction of motor 0 and motor 1. The left trigger will
     * reduce the maximum speed by 5%, while the right trigger button
     * will increase the maximum speed by 5%.
     * 
     * Connections to the motor driver is as follows:
     * XBee - Motor Driver
     *   5V - VCC
     *  GND - GND
     * DOUT - RX
     * 
     * Power the motor driver with no higher than 11V!
     */

    #define L_TRIG 6        // Pin used for left trigger
    #define R_TRIG 3        // Pin used for right trigger
    #define L_JOYSTICK A3   // Pin used for left joystick
    #define R_JOYSTICK A0   // Pin used for right joystick

    int8_t speedLevel = 20; //Maximum speed (%) = speedLevel * 5 (units are percent)

    void setup() 

    void loop() 
      }
      // Increase top speed
      if(digitalRead(R_TRIG) == 0)
      
      }

      // Read joysticks
      // Convert analog value range to motor speeds (in %)
      leftStick = (5-(analogRead(L_JOYSTICK)/93))*speedLevel;
      rightStick = (5-(analogRead(R_JOYSTICK)/93))*speedLevel;

      // Build motor 0 buffer
      if(leftStick > 0)
      
      else
      

      // Build motor 1 buffer
      if(rightStick > 0)
      
      else
      

      // Send motor speeds
      delay(5);
      Serial1.print(buf0);
      delay(5);
      Serial1.print(buf1);
    }

Plug in the battery to power the motor driver and receiving XBee and turn on the Wireless Joystick. Moving the left stick should move the left motor, and the right stick should move the right motor. If your left stick is controlling the right motor (or visa versa), swap the pin values for the `L_JOYSTICK` and `R_JOYSTICK` at the top of the sketch.

You can slow down the speed of the motors by pressing the left trigger button, and speed up the motor by pressing the right trigger button.

### Example 2: USB Game Controller

In order to program a microcontroller from a computer, many microcontrollers like the ATMega328, require another IC to bridge USB to the microcontroller\'s UART. Other microcontrollers, like the SAMD21 used on the Wireless Joystick, come with native USB, which means there isn\'t any need for the bridge IC. Having native USB allows us to program the microcontroller and imitate USB devices like keyboards, mice, and gaming joysticks.

In this example, we\'ll program the Wireless Joystick to help us play a classic game, Asteroids. This example can use either the dual joystick or the single joystick configuration. Let\'s first upload the code below to our board by copying and pasting it into the Arduino IDE. Make sure you **select the SparkFun SAMD21 Dev Breakout as your board**. After the code has finished transferring to board, go back to the webpage that has the game on it. Click start and try it out!

    language:c
    /* Not So Wireless Wireless Joystick USB Example
     * by: Alex Wende
     * SparkFun Electronics
     * date: 9/28/16
     * 
     * license: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
     * Do whatever you'd like with this code, use it for any purpose.
     * Please attribute and keep this license.
     * 
     * This example sends ASCII arrow key characters over USB when the left
     * joystick is moved or a space character when right trigger button is pressed.
     */

    #include "Keyboard.h"

    #define H_JOYSTICK    A2
    #define V_JOYSTICK    A3
    #define R_TRIGGER     3

    void setup() 

    void loop() 

      if(vStick > 766) Keyboard.press(KEY_UP_ARROW);
      else

      if(digitalRead(R_TRIGGER) == LOW)
      else
    }

You can find a free version of Asteroids [here](http://www.freeasteroids.org/). The controls are pretty simple, you can use the left joystick to rotate your rocketship left and right as well as to accelerate forward. To destroy the asteroids, you press the right trigger button.

### [][Example 3: LiPo Battery Monitoring](#MAX17043)

In this example we\'ll program the Wireless Joystick to print out information about our battery, such as the remaining charge and the current battery voltage. This example also makes use of the programmable LED to indicate when our battery is running low and it\'s time to recharge. To use this example, copy the code below to the Arduino IDE. Make sure you **select the SparkFun SAMD21 Dev Breakout as your board**.

    language:c
    /* Wireless Joystick battery monitoring Example Code
      by: Jim Lindblom and modified by Alex Wende
      SparkFun Electronics
      date: 9/28/16

      license: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
      Do whatever you'd like with this code, use it for any purpose.
      Please attribute and keep this license.

      This is example code for the MAX17043G chip on the Wireless Joystick.
      The MAX17043G+U is a compact, low-cost 1S LiPo fuel gauge.
      The SAMD21 talks with the MAX17043 over an I2C (two-wire) interface,
      so we'll use the Wire.h library to talk with it.

      It's a silly example. It reads the battery voltage, and its percentage
      full and prints it out over SerialUSB. You probably wouldn't care about
      the battery voltage if you had the Wireless Joystick connected via USB.
      But this code does show you how to configure the MAX17043G, and how to
      read and manipulate the voltage values.
    */
    #include <Wire.h>

    #define MAX17043_ADDRESS 0x36  // R/W =~ 0x6D/0x6C

    // Pin definitions
    int alertPin = 7;  // This is the alert interrupt pin, connected to pin 7 on the Wireless Joystick

    // Global Variables
    float batVoltage;
    float batPercentage;
    int alertStatus;

    void setup()
    

    void loop()
    

    /*
    vcellMAX17043() returns a 12-bit ADC reading of the battery voltage,
    as reported by the MAX17043's VCELL register.
    This does not return a voltage value. To convert this to a voltage,
    multiply by 5 and divide by 4096.
    */
    unsigned int vcellMAX17043()
    

    /*
    percentMAX17043() returns a float value of the battery percentage
    reported from the SOC register of the MAX17043.
    */
    float percentMAX17043()
    

    /* 
    configMAX17043(byte percent) configures the config register of
    the MAX170143, specifically the alert threshold therein. Pass a 
    value between 1 and 32 to set the alert threshold to a value between
    1 and 32%. Any other values will set the threshold to 32%.
    */
    void configMAX17043(byte percent)
    
    }

    /* 
    qsMAX17043() issues a quick-start command to the MAX17043.
    A quick start allows the MAX17043 to restart fuel-gauge calculations
    in the same manner as initial power-up of the IC. If an application's
    power-up sequence is very noisy, such that excess error is introduced
    into the IC's first guess of SOC, the Arduino can issue a quick-start
    to reduce the error.
    */
    void qsMAX17043()
    

    /* 
    i2cRead16(unsigned char address) reads a 16-bit value beginning
    at the 8-bit address, and continuing to the next address. A 16-bit
    value is returned.
    */
    unsigned int i2cRead16(unsigned char address)
    

    /*
    i2cWrite16(unsigned int data, unsigned char address) writes 16 bits
    of data beginning at an 8-bit address, and continuing to the next.
    */
    void i2cWrite16(unsigned int data, unsigned char address)
    

### Example 4: Using the Extra GPIO

You may have noticed that the SPI, I^2^C, and other GPIO pins have been broken out. We wanted to breakout the unused pins to allow for any customization that you may want. In this final example, we\'ll use the OLED screen to display battery information from the MAX17043 fuel gauge.

Before we look at the code, let\'s wire up the OLED Breakout. You\'ll need seven wires to connect the OLED Breakout to the Wireless Joystick, their connections are:

Wireless Joystick - OLED Breakout

- 3.3V - 3V3
- GND - GND
- MOSI - SDI
- SCK - SCK
- D10 - CS
- D11 - RST
- D12 - D/C

Where you place the OLED screen is up to you, but I personally like to use foam doubled sided tape to mount the display on the top of the board by the USB connector.

[![OLED Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/0/Joystick_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/0/Joystick_Tutorial-07.jpg)

To use the code below, you\'ll want to download the MicroOLED Arduino library first. To download the libary, click the button below, or grab the latest version from our [GitHub repository](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library). For more information on how to use the libary, visit the [Micro OLED Breakout Hookup Guide](https://learn.sparkfun.com/tutorials/micro-oled-breakout-hookup-guide#arduino-library-download-install-and-test).

[Download the Arduino Library!](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library/archive/master.zip)

After installing the library, copy the code below to the Arduino IDE. Make sure you **select the SparkFun SAMD21 Dev Breakout as your board**.

    language:c
    /* GPIO Example For the Wireless Joystick
     * by: Alex Wende
     * SparkFun Electronics
     * date: 9/28/16
     * 
     * license: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
     * Do whatever you'd like with this code, use it for any purpose.
     * Please attribute and keep this license.
     * 
     * This example the SparkFun OLED Breakout (LCD-13003) to display
     * the battery's voltage and remaining charge.
     * 
     * Connections:
     * Wireless Joystick - OLED
     * 3.3V - 3V3
     *  GND - GND
     * MOSI - SDI
     *  SCK - SCK
     *  D12 - D/C
     *  D11 - RST
     *  D10 - CS
     */

    #include <SPI.h>
    #include <Wire.h>
    #include <SFE_MicroOLED.h>

    #define PIN_RESET 11  // Connect RST to pin 9 (req. for SPI and I2C)
    #define PIN_DC    12  // Connect DC to pin 8 (required for SPI)
    #define PIN_CS    10 // Connect CS to pin 10 (required for SPI)
    #define DC_JUMPER 0

    #define MAX17043_ADDRESS 0x36

    // Pin definitions
    int alertPin = 7;  // This is the alert interrupt pin, connected to pin 7 on the Wireless Joystick
    int ledPin = 13;   // This is the pin the led is connected to

    // Global Variables
    float batVoltage;
    float batPercentage;
    int alertStatus;

    MicroOLED oled(PIN_RESET, PIN_DC, PIN_CS);

    void setup()
    

    void loop()
    
      else
      oled.display();
      delay(10);  
    }

    /*
    vcellMAX17043() returns a 12-bit ADC reading of the battery voltage,
    as reported by the MAX17043's VCELL register.
    This does not return a voltage value. To convert this to a voltage,
    multiply by 5 and divide by 4096.
    */
    unsigned int vcellMAX17043()
    

    /*
    percentMAX17043() returns a float value of the battery percentage
    reported from the SOC register of the MAX17043.
    */
    float percentMAX17043()
    

    /* 
    configMAX17043(byte percent) configures the config register of
    the MAX170143, specifically the alert threshold therein. Pass a 
    value between 1 and 32 to set the alert threshold to a value between
    1 and 32%. Any other values will set the threshold to 32%.
    */
    void configMAX17043(byte percent)
    
    }

    /* 
    qsMAX17043() issues a quick-start command to the MAX17043.
    A quick start allows the MAX17043 to restart fuel-gauge calculations
    in the same manner as initial power-up of the IC. If an application's
    power-up sequence is very noisy, such that excess error is introduced
    into the IC's first guess of SOC, the Arduino can issue a quick-start
    to reduce the error.
    */
    void qsMAX17043()
    

    /* 
    i2cRead16(unsigned char address) reads a 16-bit value beginning
    at the 8-bit address, and continuing to the next address. A 16-bit
    value is returned.
    */
    unsigned int i2cRead16(unsigned char address)
    

    /*
    i2cWrite16(unsigned int data, unsigned char address) writes 16 bits
    of data beginning at an 8-bit address, and continuing to the next.
    */
    void i2cWrite16(unsigned int data, unsigned char address)