# Source: https://learn.sparkfun.com/tutorials/display-distance-measurements-on-an-oled

## Introduction

This tutorial will take your SparkFun Qwiic Ultrasonic Distance Sensor to the next level by adding a cool little OLED display. With this upgrade, your robot (or you!) won\'t just be able to measure distances, you\'ll be able to see them in real time on the screen!

[![SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/0/9/7/SEN-24805-Ultrasonic-Distance-Sensor-Feature_2.jpg)](https://www.sparkfun.com/sparkfun-ultrasonic-distance-sensor-tct40-qwiic.html)

### [SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic)](https://www.sparkfun.com/sparkfun-ultrasonic-distance-sensor-tct40-qwiic.html) 

[ SEN-24805 ]

The TCT40 distance sensor is great for non-contact distance readings from 2cm to 400cm. This unit adds a pair of Qwiic connec...

[ [\$11.50] ]

If you are looking for the full Hookup Guide for the SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic), click the button bellow. This guide only covers a simple project to get you started quickly, while the full Hookup Guide goes over every detail of the sensor.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_Ultrasonic_Distance_Sensor-Qwiic)

 

------------------------------------------------------------------------

## Hardware Needed

To follow this experiment, you will need the following materials. While this is a simple project we wanted to make sure that you have everything you need to get started before we get to the code. For this simple project we chose the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) but you could choose from many of our development boards such as the [Qwiic Pro Micro](https://www.sparkfun.com/products/15795) as well.

[![SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/0/9/7/SEN-24805-Ultrasonic-Distance-Sensor-Feature_2.jpg)](https://www.sparkfun.com/sparkfun-ultrasonic-distance-sensor-tct40-qwiic.html)

### [SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic)](https://www.sparkfun.com/sparkfun-ultrasonic-distance-sensor-tct40-qwiic.html) 

[ SEN-24805 ]

The TCT40 distance sensor is great for non-contact distance readings from 2cm to 400cm. This unit adds a pair of Qwiic connec...

[ [\$11.50] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Qwiic OLED Display (0.91 in., 128x32)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/9/6/3/LCD-24606-Qwiic-OLED-Display-Feature-Screen.jpg)](https://www.sparkfun.com/sparkfun-qwiic-oled-display-0-91-in-128x32-lcd-24606.html)

### [SparkFun Qwiic OLED Display (0.91 in., 128x32)](https://www.sparkfun.com/sparkfun-qwiic-oled-display-0-91-in-128x32-lcd-24606.html) 

[ LCD-24606 ]

The SparkFun Qwiic OLED Display can display up to four lines of text and features 128x32 pixels in a small 0.91in. (diagonal)...

[ [\$10.95] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/600-600/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

**Note:** This tutorial calls for two 100mm Qwiic Cables (which is why it\'s listed twice), but any Qwiic cable can be used instead of the 100mm version. Please be sure to have the correct amount in your cart before purchasing.

------------------------------------------------------------------------

## Software Setup

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the SparkFun Ultrasonic Distance Sensor Qwiic Board. You can obtain this library by clicking on the button below, or by downloading it from the [GitHub Repository](https://github.com/sparkfun/SparkFun_Qwiic_Ultrasonic_Arduino_Library/tree/v10).

[SparkFun Qwiic Ultrasonic Arduino Library GitHub](https://github.com/sparkfun/SparkFun_Qwiic_Ultrasonic_Arduino_Library)

 

------------------------------------------------------------------------

## Read Measurements with a Serial Monitor

Now that we\'ve installed the Arduino library, it\'s time to upload our first sketch to make sure everything is working properly and you are able to read basic measurements with your Serial Monitor in the Arduino IDE.

For this example you will need the [SparkFun Ultrasonic Distance Sensor - TCT40 (Qwiic)](https://www.sparkfun.com/products/24805), a [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123), a [Qwiic Cable](https://www.sparkfun.com/products/14427), and a [USB Micro-B Cable](https://www.sparkfun.com/products/10215).

Using the Qwiic system, assembling the hardware is simple. Connect the RedBoard to one of the Ultrasonic Distance Sensor Qwiic ports using your Qwiic cables (please remember to insert this cable in the correct orientation). Then connect the RedBoard to your computer via the MicroUSB cable and voila! You\'re ready to rock!

[![Ultrasonic Distance Sensor Connected to Programming](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/5/24805-Ultrasonic-Distance-Sensor-Action-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/24805-Ultrasonic-Distance-Sensor-Action-2.jpg)

*Ultrasonic Distance Sensor Connected to RedBoard*

 

To find Example 1, go to **File \> Examples \> SparkFun Qwiic Ultrasonic Arduino Library \> Example1_BasicReadings**:

[![Finding Example 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/5/Example1_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/Example1_Menu.jpg)

*Finding Basic Readings Sketch*

Alternatively, you can copy and paste the code below into a shiny new Arduino sketch:

    /* SparkFun Ulrasonic Distance Sensor - Example 1 Basic Distance Sensing
         * 
         * Product: 
         *  *  SparkFun Qwiic Ultrasonic Distance Sensor - HC-SR04 (SEN-1XXXX)
         *  *  https://www.sparkfun.com/1XXXX
         * 
         * Written By: Elias Santistevan
         * Date: 06/2024
         *
         * SPDX-License-Identifier: MIT
         *
         * Copyright (c) 2024 SparkFun Electronics
         */

        #include "SparkFun_Qwiic_Ultrasonic_Arduino_Library.h"

        // Create an ultrasonic sensor object
        QwiicUltrasonic myUltrasonic;

        // Here we set the device address. Note that an older version of the Qwiic
        // Ultrasonic firmware used a default address of 0x00. If yours uses 0x00,
        // you'll need to change the address below. It is also recommended to run
        // Example 2 to change the address to the new default.
        uint8_t deviceAddress = kQwiicUltrasonicDefaultAddress; // 0x2F
        // uint8_t deviceAddress = 0x00;

        void setup()
        

          Serial.println("Ultrasonic sensor connected!");
        }

        void loop()
        

Make sure you\'ve selected the correct board and port in the Tools menu and then hit the upload button. Once the code has finished uploading, go ahead and open a [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). You should see something similar to the following.

[![Example 1 Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/5/Example1_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/Example1_Output.jpg)

*Example distance measurements in millimeters*

Note: The code for changing the measurements to **inches** or **centimeters** is provided near the bottom of the sketch. You\'ll simply need to add/remove commenting syntax to change your output.

 

------------------------------------------------------------------------

## Display Measurements On an OLED

Let\'s add in an LCD screen to display our measurements. For this example you will need another [Qwiic Cable](https://www.sparkfun.com/products/14427) and the [SparkFun Qwiic OLED Display (0.91 in., 128x32)](https://www.sparkfun.com/products/24606). Again, the Qwiic system makes this example quite literally plug and play. Use Qwiic cables to make your hardware setup look like this:

[![Example 2 Hardware Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/5/24805-Ultrasonic-Distance-Sensor-Action-4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/24805-Ultrasonic-Distance-Sensor-Action-4.jpg)

*Hardware Hookup with OLED*

To display the sensor readings on the connected Qwiic OLED, we will need to install the SparkFun Qwiic OLED library. You can install this library to automatically in the Arduino IDE\'s Library Manager by searching for \"SparkFun Qwiic OLED\". Or you can manually download it from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_OLED_Arduino_Library).

[Download the SparkFun Qwiic OLED Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_OLED_Arduino_Library/archive/refs/heads/main.zip)

 

To find Example 2, go to **File \> Examples \> SparkFun Qwiic Ultrasonic Arduino Library \> Example2_OLED_Distance**:

[![Finding Example 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/5/Example2_Menu.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/Example2_Menu.jpg)

*Locating Arduino Library Example*

Alternatively, you can copy and paste the code below into a shiny new Arduino sketch:

    /* SparkFun Ulrasonic Distance Sensor - Example 2 Basic Distance Sensing on an OLED Display
      * 
       * Products: 
       *  *  SparkFun Qwiic Ultrasonic Distance Sensor - HC-SR04 (SEN-1XXXX)
       *  *  https://www.sparkfun.com/1XXXX
       *  *  SparkFun Qwiic Narrow OLED Display (LCD-1XXXX)
       *  *  https://www.sparkfun.com/1XXXX
       *
       * Link to OLED library: https://github.com/sparkfun/SparkFun_Qwiic_OLED_Arduino_Library
       * 
       * Written By: Elias Santistevan
       * Date: 06/2024
       *
       * SPDX-License-Identifier: MIT
       *
       * Copyright (c) 2024 SparkFun Electronics
       */

      #include "SparkFun_Qwiic_OLED.h"
      // For the narrow LED, I prefer the slightly larger font included in the OLED library.
      // This is completely optional and can be deleted or commented out. By default the font
      // is slightly smaller. 
      #include "res/qw_fnt_8x16.h"
      #include "SparkFun_Qwiic_Ultrasonic_Arduino_Library.h"

      // Create an ultrasonic sensor object
      QwiicUltrasonic myUltrasonic;
      // Creat an OLED object
      QwiicNarrowOLED myOLED;

      char distanceBuff[4] = ; 
      String distanceStr = "";
      int centerX; 
      int centerY; 

      // Here we set the device address. Note that an older version of the Qwiic
      // Ultrasonic firmware used a default address of 0x00. If yours uses 0x00,
      // you'll need to change the address below. It is also recommended to run
      // Example 2 to change the address to the new default.
      uint8_t deviceAddress = kQwiicUltrasonicDefaultAddress; // 0x2F
      // uint8_t deviceAddress = 0x00;

      void setup()
      
        while(myUltrasonic.begin(deviceAddress) == false)
        

        String hello = "Hello, Ultrasonic!";

        // This is good for the narrow OLED screen. You can also just remove this 
        // and it will default to a slightly smaller font. 
        myOLED.setFont(QW_FONT_8X16);

        // This will center the text onto the screen. 
        int x0 = (myOLED.getWidth() - myOLED.getStringWidth(hello)) / 2;
        int y0 = (myOLED.getHeight() - myOLED.getStringHeight(hello)) / 2;

        myOLED.text(x0, y0, hello);

        // There's nothing on the screen yet - Now send the graphics to the device
        myOLED.display();
        delay(2000);
      }

      void loop() 
      

Make sure you\'ve selected the correct board and port in the Tools menu and then hit the upload button. Once the code has finished uploading, you should see something similar to the following.

[![Run away!](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/SEN-24805-GIF.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/5/SEN-24805-GIF.gif)

*Run away!*

Try moving an object (like your hand or a dinosaur) closer to the sensor - notice the output of the OLED shows you how close the object is! Grr. Rawr!

 

------------------------------------------------------------------------