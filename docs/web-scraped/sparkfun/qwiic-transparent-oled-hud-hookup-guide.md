# Source: https://learn.sparkfun.com/tutorials/qwiic-transparent-oled-hud-hookup-guide

## Introduction

Clear screens are no longer a thing of the Sci-Fi world! The [Qwiic Transparent OLED HUD](https://www.sparkfun.com/products/15079) ([Head Up Display](https://en.wikipedia.org/wiki/Head-up_display)) is SparkFun\'s answer to all of your futuristic transparent HUD needs. While you can see through the display, each segment is **area colored**, meaning that while no one segment can change colors, there are different colored segments on the display.

[![SparkFun Transparent OLED HUD Breakout (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/2/7/15079-SparkFun_Transparent_OLED_Breakout__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-transparent-oled-hud-breakout-qwiic.html)

### [SparkFun Transparent OLED HUD Breakout (Qwiic)](https://www.sparkfun.com/sparkfun-transparent-oled-hud-breakout-qwiic.html) 

[ LCD-15079 ]

The Qwiic Transparent OLED HUD is SparkFun\'s answer to all of your futuristic transparent HUD needs.

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### Microcontroller

The Transparent OLED HUD requires quite a bit of RAM, so you\'ll need a microcontroller with at least 5500 bytes of RAM to control everything. Check out the below for some possible options.

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![SparkFun SAMD21 Mini Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html)

### [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html) 

[ DEV-13664 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Mini Breakout is ...

[ [\$24.95] ]

[![Arduino Mega 2560 R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/3/3/11061-01.jpg)](https://www.sparkfun.com/arduino-mega-2560-r3.html)

### [Arduino Mega 2560 R3](https://www.sparkfun.com/arduino-mega-2560-r3.html) 

[ DEV-11061 ]

Arduino is an open-source physical computing platform based on a simple i/o board and a development environment that implemen...

[ [\$48.40] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun ESP8266 Thing - Dev Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/9/7/13711-01.jpg)](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html)

### [SparkFun ESP8266 Thing - Dev Board](https://www.sparkfun.com/sparkfun-esp8266-thing-dev-board.html) 

[ WRL-13711 ]

The SparkFun ESP8266 Thing Dev Board is a development board that has been solely designed around the ESP8266, with an integra...

[ [\$19.95] ]

[![Teensy 3.6](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/7/14057-01.jpg)](https://www.sparkfun.com/products/14057)

### [Teensy 3.6](https://www.sparkfun.com/products/14057) 

[ DEV-14057 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port and upg...

**Retired**

**Warning!** The Arduino sketch required to drive this display requires quite a bit of dynamic memory, meaning that it is not going to fit on a smaller controller like an ATmega328. Any controller with larger RAM should have no problem. It has been tested to run very well on an Arduino Mega 2560. In addition, your 3.3v source should be robust enough to supply around 400mA to the display.

#### Cable

Now to get into the Qwiic ecosystem, the key will be using a Qwiic shields to match your preference of microcontroller. In this tutorial, we\'ll be using Qwiic-to-breadboard adapter cable. You will also need a cable to upload code to your microcontroller.

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![USB Cable A to B - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/7/00512-USB_Cable_A_to_B_-_6_Foot-01.jpg)](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html)

### [USB Cable A to B - 6 Foot](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html) 

[ CAB-00512 ]

This is a standard issue USB 2.0 cable. This is the most common A to B Male/Male type peripheral cable, the kind that\'s usual...

[ [\$5.50] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: text-center                                                                                                                                     |
| [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic) |
| :::                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

## Hardware Overview

First let\'s check out some of the characteristics of the Qwiic HUD we\'re dealing with, so we know what to expect out of the board.

  **Characteristic**   **Range**
  -------------------- ----------------
  Operating Voltage    **1.65V-3.3V**
  Supply Current       **400 mA**
  I^2^C Addresses      0x30, 0x31

Notice that the OLED can pull about 400 mA of current, so ensure you have a robust enough power supply, especially if the OLED isn\'t the only thing you\'re powering. Also notice that the OLED sits on two I^2^C addresses, so make sure that any other I^2^C devices don\'t take up addresses **0x30** and **0x31**.

### Pins

The following table lists all of the transparent OLED\'s pins and their functionality.

  Pin    Description   Direction
  ------ ------------- ----------------
  GND    Ground        In
  3.3V   Power         In
  SDA    Data          Bi-directional
  SCL    Clock         In

### Optional Features

The Transparent OLED breakout has pull-up resistors attached to the I^2^C bus; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull-up resistors they can be removed by [cutting the traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) on the corresponding jumpers highlighted below.

[![Pull-up Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/3/i2c.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/i2c.png)

*Pull-up Jumpers*

The onboard LED (highlighted below) will light up when the board is powered.

[![Power LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/3/pwr.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/pwr.png)

*Power LED*

## Hardware Assembly

The Transparent OLED HUD requires quite a little bit of RAM (Around 5500 bytes) so you\'ll need to connect to your I^2^C pins directly to devices without Qwiic Shields. Connect yellow to SCL, blue to SDA, red to 3.3V and black to ground using the Qwiic jumper adapter cable to the respective pins of your board. In this case, we connected the board to an [Arduino Mega 2560\'s I^2^C pins](https://www.arduino.cc/en/reference/wire).

[![Connected to Mega](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/3/OLED_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Hookup_Guide-03.jpg)

*Transparent OLED HUD Attached to Arduino Mega*

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you\'ll need the **SparkFun Transparent OLED HUD** Arduino library. You can obtain this library through the Arduino Library Manager. Search for **Sparkfun Wisechip HUD** to install the latest version. If you prefer downloading the libraries from the [GitHub repository](https://github.com/sparkfun/SparkFun_WiseChip_HUD_Library) and manually installing it, you can grab them here:

[DOWNLOAD THE SPARKFUN WISECHIP HUD LIBRARY (ZIP)](https://github.com/sparkfun/SparkFun_WiseChip_HUD_Library/archive/master.zip)

Before we get started developing a sketch, let\'s look at all of the functions we can use to control segments on the transparent HUD. The below code initializes the functions for the individual segments in the compass circle (`CCx()` functions), compass arrows (`D0x()` functions), tire pressure indication, destination distance(`H01()`, `K01()`, `M01()` for hours, kilometers, and meters), turn distance (`K02()` and `M03()` for kilometers and meters), the phone and TPMS icons (`P0x()` and `T0x()`) and finally, the **1**\'s on the speedometer and compass (`S01_BAR()` and `S15_BAR()`). You won\'t need to use most of these functions, as most are used in higher level functions like `setSpeedometer()`, but we\'ve given you access to these segments anyway. Turning any segmetn on is as simple as calling it with an argument of `1`. Calling with a `0` will turn it off.

    language:c
    void D01(uint8_t Action);
    void CC1(uint8_t Action);
    void D02(uint8_t Action);
    void CC2(uint8_t Action);
    void D03(uint8_t Action);
    void CC3(uint8_t Action);
    void D04(uint8_t Action);
    void CC4(uint8_t Action);
    void D05(uint8_t Action);
    void CC5(uint8_t Action);
    void D06(uint8_t Action);
    void CC6(uint8_t Action);
    void D07(uint8_t Action);
    void CC7(uint8_t Action);
    void D08(uint8_t Action);
    void CC8(uint8_t Action);
    void D0x(uint8_t Action);
    void C01(uint8_t Action);
    void C02(uint8_t Action);
    void H01(uint8_t Action);
    void K01(uint8_t Action);
    void M01(uint8_t Action);
    void C03(uint8_t Action);
    void K02(uint8_t Action);
    void M03(uint8_t Action);
    void P01(uint8_t Action);
    void P02(uint8_t Action);
    void P03(uint8_t Action);
    void T01(uint8_t Action);
    void T02(uint8_t Action);
    void S01_BAR(uint8_t Action);
    void S15_BAR(uint8_t Action);

### Higher Level Functions

The available functions for the transparent OLED can be more easily seen in the below photo.

[![Segment Map](https://cdn.sparkfun.com/assets/4/4/2/f/2/labeled_icons_hud.png)](https://cdn.sparkfun.com/assets/4/4/2/f/2/labeled_icons_hud.png)

*Segment Map. Click to enlarge.*

All of the below functions will set a group of segments based on the argument passed into them

- **`void compassCircle(uint8_t Select);`**
  - **0**: All Off
  - **1-8**: All Off Except Selected
  - **9**: All On
  - **10-17**: All On Except Selected
- **`void compassArrows(uint8_t Select);`** \-\-- Same as compass circle.
- **`void radarDistanceUnits(uint8_t Action);`** \-\-- turns on the **m** for radar distance.
- **`void flag(uint8_t Action);`** \-\-- Turns on the flag segment.
- **`void tirePressureAlert(uint8_t Action);`** \-\-- Displays TPMS text.
- **`void speedometerUnits(uint8_t Action);`** \-\-- Displays KM/H segments.
- **`void destinationDistanceUnits(uint8_t iconUnits);`**
  - **0**: Blank
  - **1**: h
  - **2**: m
  - **3**: km
- **`void turnDistanceUnits(uint8_t iconUnits);`**
  - **0**: Blank
  - **1**: m
  - **2**: km

The following functions display the road and tunnel segments, pass in a 1 to turn the segment on.

- **`void leftTunnel(uint8_t Action);`**
- **`void middleTunnel(uint8_t Action);`**
- **`void rightTunnel(uint8_t Action);`**
- **`void leftRoad(uint8_t Action);`**
- **`void middleRoad(uint8_t Action);`**
- **`void rightRoad(uint8_t Action);`**

The following functions turn on the corresponding segments for the navigation

- **`void nav_Group(uint8_t Action);`** \-\-- Triggers the whole nav group

- **`void nav_KeepLeft(uint8_t Action);`**

- **`void nav_TurnLeft(uint8_t Action);`**

- **`void nav_TurnRight(uint8_t Action);`**

- **`void nav_HardRight(uint8_t Action);`**

- **`void nav_HardLeft(uint8_t Action);`**

- **`void nav_UTurnLeft(uint8_t Action);`**

- **`void nav_UTurnRight(uint8_t Action);`**

- **`void nav_ContinueStraight(uint8_t Action);`**

- **`void nav_KeepRight(uint8_t Action);`**

- **`void radarDetector(uint8_t Level);`**

  - **0**: No Radar Gun Icon
  - **1**: Radar Gun Only
  - **2-8**: Distance Meter

- **`void setHeading(uint8_t SpeedNo);`** \-\-- Set\'s the compass heading. Maximum of 199.

- **`void setDestinationDistance(uint16_t SpeedNo, uint8_t Mode);`** \-\-- Set\'s the distance in the destination segments. Maximum of 999.

- **`void setRadarDistance(uint16_t SpeedNo, uint8_t Mode);`** \-\-- Set\'s the distance in the radar segments. Maximum of 999.

- **`void setTurnDistance(uint16_t SpeedNo, uint8_t Mode);`** \-\-- Set\'s the turn distance. Maximum of 999.

- **`void setTirePressure(uint8_t SpeedNo, uint8_t Mode);`** \-\-- Set the tire pressure. Maximum of 99

- **`void setSpeedometer(uint8_t SpeedNo);`** \-\-- Set the speedometer. Maximum of 199.

- **`void setCallIcon(uint8_t iconStatus);`**

  - **0**: Blank
  - **1**: Outline
  - **2**: Outline + Phone
  - **3**: All Segments

- **`void clearAll(void);`** \-\-- Clears all segments.

## Example Code

Now that we have our library installed and we understand the basic functions, let\'s run some examples for our Qwiic Transparent OLED HUD to see how it behaves.

### Example 1 - All Segments

To get started with the first example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun WiseChip HUD** \> **Example1_AllSegments**. In this example, we begin by creating a **`WiseChipHUD`** object called `myHUD` and then initializing our sensor object in the `setup()` loop. The code to do this is shown below.

    language:c
    #include <WiseChipHUD.h>

    WiseChipHUD myHUD;

    void setup() 

Once we\'ve initialized our HUD, we can start turning segments on. The main loop simply goes through and calls all of our available functions.

    language:c
    void loop() ;

    }

If you have not already, select the **Arduino/Genuino Mega 2560 or Mega2560** as the board, COM port that it enumerated on, and hit upload! The OLED should look something like the below GIF.

[![Example 1 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_1.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_1.gif)

*Example 1 Output*

### Example 2 - Animated Icons

In the second example, we\'ll animate our display segments. To get started with the second example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun WiseChip HUD** \> **Example2_AnimatedIcons**. We initialize our HUD the exact same as we do in the first example. Then, we go ahead and use `for` loops to loop through each possible state of a group of segments to animate it. Each loop starts at 0 and goes to the maximum number of options for that particular group of segments. There is a small delay in each loop to allow for some time between frames.. We do this for the compass, radar, phone and TPMS icons. We clear the entire HUD in between each animation of a group of segments to ensure that we are only displaying one group at a time. The code that accomplishes this is shown below.

    language:c
    void loop() 
      }

      for(int j = 0; j < 2; j++)
      }

      myHUD.compassCircle(0);

      for(int j = 0; j < 2; j++)
      }

      for(int j = 0; j < 2; j++)
      }

      myHUD.compassArrows(0); 

      for(int i = 0; i < 5; i++)

      myHUD.radarDistanceUnits(1);

      for(int j = 800; j >= 0; j = j - 10)

      myHUD.clearAll();

      for(int j = 0; j < 5; j++)
      }

      myHUD.setCallIcon(0); 

      myHUD.tirePressureAlert(3);
      myHUD.setTirePressure(30,1); 
      delay(2000);

      for(int j = 30; j > 14; j--)

      for(int j = 0; j < 10; j++)
      }
      myHUD.tirePressureAlert(3);

      myHUD.clearAll();

    while(1);

    }

If you have not already, select the **Arduino/Genuino Mega 2560 or Mega2560** as the board, COM port that it enumerated on, and hit upload! The transparent HUD should look something like the below GIF after uploading the code.

[![Example 2 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_2.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_2.gif)

*Example 2 Output*

### Example 3 - Counting

In the third example, we\'ll have each of the available number displays count up to 200. To get started with the third example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun WiseChip HUD** \> **Example2_AnimatedIcons**. In this example, we initialize the OLED the same way we have been doing in our previous two examples. Then, in our `void loop()`, we clear the HUD, then begin a `for` loop that counts by 5\'s. We write the value of the index variable to each of the segments. The code that accomplishes this is shown below.

    language:c
    void loop() 

        myHUD.clearAll();

      };

    }

If you have not already, select the **Arduino/Genuino Mega 2560 or Mega2560** as the board, COM port that it enumerated on, and hit upload! Uploading this code should make the OLED look like the below GIF. Notice how the number for the TPMS stops at 99. This is a demonstration of how these functions handle out of bounds numbers.

[![Example 3 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_3.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/3/OLED_Demo_3.gif)

*Example 3 Output*