# Source: https://learn.sparkfun.com/tutorials/qwiic-digital-indoor-thermometer

## Introduction

Qwiic-ly build a digital indoor thermometer to measure the ambient temperature of the room and display it using an OLED!

[![Qwiic Digital Indoor Thermometer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor_Demo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor_Demo.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. This tutorial\'s code was can be used with either the TMP117 or TMP102!

### Tools

To create your tower of sensing power, you will need a screw driver. If you do not have one already, add it to your cart.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/qwiic-tmp117-high-precision-digital-temperature-sensor-hookup-guide)

### Qwiic TMP117 High Precision Digital Temperature Sensor Hookup Guide 

Add a high precision, digital temperature sensor to your projects using the TMP117 over the I2C!

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micro-samd21e-hookup-guide)

### SparkFun Qwiic Micro (SAMD21E) Hookup Guide 

An introduction to the Qwiic Micro SAMD21E. Level up your Arduino-skills with the powerful SAMD21 ARM Cortex M0+ processor!

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-digital-temperature-sensor---tmp102-hookup-guide)

### SparkFun Qwiic Digital Temperature Sensor - TMP102 Hookup Guide 

Get started using your SparkFun Digital Temperature Sensor - TMP102 (Qwiic) with this Hookup Guide!

[](https://learn.sparkfun.com/tutorials/temperature-sensor-comparison)

### Temperature Sensor Comparison 

A comparison of analog and digital temperature sensors. Which is better?

## Hardware Hookup

The Qwiic ecosystem has made it easier and faster to prototype. You simply connect a Qwiic device to an Arduino using a Qwiic cable. We can add additional Qwiic devices to the I^2^C bus with ease. The original tutorials use a RedBoard Qwiic with an ATmega328P to connect to each device. In this project tutorial, we\'ll use the Qwiic Micro with SAMD21 to make it as small as possible.

We will use the Qwiic TMP117 to measure the ambient room temperature. However, if you do not require such precision, you can also use the Qwiic TMP102. We will use the Qwiic micro OLED to display the temperature.

[![Qwiic Cable Connecting the Qwiic micro, Qwiic TMP117, and Qwiic micro OLED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor.jpg)

Once the boards are daisy chained, there is an option to mount the boards using the mounting holes located on the standard 1.0\"x1.0\" sized Qwiic boards. We\'ll be stacking the Qwiic boards on top of each other using standoffs and any available mounting holes with the Qwiic micro OLED on top, Qwiic TMP117 in the middle, and the Qwiic micro on the bottom. Note that the top of the Qwiic Micro in this tutorial will face away from the other boards so that we can easily access the reset button. However, you can face it however you would like based on your personal preference. When you are ready, connect the USB cable to Qwiic Micro. We will use this to power and program the board.

[![USB Cable connecting to the Qwiic Micro to Power and Program the Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/1/USB_Cable_Qwiic_Micro.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/1/USB_Cable_Qwiic_Micro.jpg)

## Installing Arduino Libraries

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

You\'ll need to need to download and install a two Arduino libraries for this project tutorial.

### Qwiic Micro OLED Library

To display the sensor readings, we will use the **SparkFun Micro OLED library**. You can install this library to automatically in the Arduino IDE\'s Library Manager by searching for \"**Micro OLED Breakout**\". Or you can manually download it from the [GitHub repository](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library).

[Download the SparkFun Micro OLED Library (ZIP)](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library/archive/master.zip)

### Qwiic TMP117 [Option 1]

To measure temperature from the TMP117, we will use the **SparkFUN TMP117 Arduino Library**. We\'ll install this library automatically by using the Library Manager again by searching for **Qwiic TMP117**. If you prefer downloading the libraries manually you can grab them from the [GitHub repository](https://github.com/sparkfun/SparkFun_TMP117_Arduino_Library).

[Download the SparkFun TMP117 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_TMP117_Arduino_Library/archive/master.zip)

### Qwiic TMP102 [Option 2]

If you do not require such high precision opted for the Qwiic TMP102, you can also use the Qwiic TMP102. If you chose this route, you will need to use teh **SparkFUN TMP102 Arduino Library**. We\'ll install this library automatically by using the Library Manager by searching for **SparkFun TMP102**. If you prefer downloading libraries manually, you can grab it from the [GitHub Repository](https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library).

[TMP102 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library/archive/master.zip)

## Installing Board Add On

Since we are using the Qwiic Micro with the SAMD21, we will need to install the board files. Make sure to check out the section in the Qwiic Micro Hookup Guide to [install the appropriate board add on](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micro-samd21e-hookup-guide#setting-up-arduino).

[Installing Arduino SAMD Board Add-Ons](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micro-samd21e-hookup-guide#setting-up-arduino)

## Example Code

Below is the example code for the Qwiic TMP117 and Qwiic TMP102. You can use either example to read the ambient temperature of the room. Since we are using the Qwiic Micro, you will need to select the correct board. Head to **Tools** \> **Boards** \> **SparkFun Qwiic Micro**. Then select the COM port that the board enumerated to before uploading.

### Qwiic TMP117 [Option 1]

If you opted to use the Qwiic TMP117, copy and paste the following code to your Arduino IDE. Make sure the switch is flipped to the ON position on the board before hitting the upload button.

    language:c
    /******************************************************************************
      Digital Indoor Temperature Monitor with the TMP117
      Written by: Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: Mar 6, 2019

      Description: This sketch configures temperature sensors and prints the
      temperature in degrees celsius and fahrenheit to the Qwiic microOLED.
      Simply adjust the `output_select` to view the °C, °F, or both. You can
      also output the values to the SerialUSB Monitor or Plotter at 115200 baud
      to view the data. There is also a demo mode that displays each output
      on the microOLED with a progress bar at the bottom.

      Resources/Libraries:
      Wire.h (included with Arduino IDE)
      SparkFunTMP117.h (included in the src folder) http://librarymanager/All#SparkFun_TMP117
      SFE_MicroOLED.h (included in the src folder)  http://librarymanager/All#SparkFun_micro_OLED

      Development Environment Specifics:
      Arduino 1.8.10+

      License:
      This code is released under the MIT License (http://opensource.org/licenses/MIT)
      Distributed as-is; no warranty is given.

    ******************************************************************************/

    /*
      NOTE: For the most accurate readings using the TMP117:
      - Avoid heavy bypass traffic on the I2C bus
      - Use the highest available communication speeds
      - Use the minimal supply voltage acceptable for the system
      - Place device horizontally and out of any airflow when storing
      For more information on reaching the most accurate readings from the sensor,
      reference the "Precise Temperature Measurements with TMP116" datasheet that is
      linked on Page 35 of the TMP117's datasheet
    */

    #include <Wire.h>            // Used to establish Serial communication on the I2C bus
    #include <SparkFun_TMP117.h> // Used to send and recieve specific information from our sensor
    #include <SFE_MicroOLED.h>   // Include the SFE_MicroOLED library

    //#define SerialUSB Serial     //Uncomment if you are not using a native USB like the Atmega32U4 or SAMD21

    ///////////////////////////////
    ///////// micro OLED //////////
    ///////////////////////////////

    #define PIN_RESET 7          // A pin needs to be declared even though we are not physically connecting to the Qwiic micro OLED via I2C
    #define DC_JUMPER 1
    MicroOLED oled(PIN_RESET, DC_JUMPER);    // I2C declaration

    ///////////////////////////////
    /////////// TMP117 ////////////
    ///////////////////////////////

    // The default address of the device is 0x48 = (GND)
    TMP117 sensor; // Initalize sensor

    float tempC = 0;
    float tempF = 0;

    //0 = output degrees °C
    //1 = output degrees °F
    //2 or any other number = output degrees °C and °F
    int output_select = 3; //select output

    ///////////////////////////////
    // Display Mode Page Control //
    ///////////////////////////////
    // This enum defines all of our display modes and their order.
    enum t_displayModes ;

    const int NUM_DISPLAY_MODES = 4; // Number of values defined in enum above
    volatile int displayMode = NUM_DISPLAY_MODES - 1; // Keeps track of current display page

    const unsigned long DISPLAY_UPDATE_RATE = 4000; // Cycle display every 5 seconds
    unsigned long lastDisplayUpdate = 0; // Stores time of last display update
    unsigned long currentMillis = 0; // Stores time of last display update

    float percentage = 0; //store percent for progress bar
    int progressWidth = 0; // Width of progress bar depends on the [% * (64 pixels wide)]
    int progressY = 0;     //location of the progress bar at the botton of the microOLED

    ///////////////////////////////
    /////// Initialize Cube ///////
    ///////////////////////////////

    int SCREEN_WIDTH = oled.getLCDWidth();
    int SCREEN_HEIGHT = oled.getLCDHeight();

    float d = 3;
    float px[] = ;
    float py[] = ;
    float pz[] = ;

    float p2x[] = ;
    float p2y[] = ;

    float r[] = ;

    #define SHAPE_SIZE 600
    // Define how fast the cube rotates. Smaller numbers are faster.
    // This is the number of ms between draws.
    //#define ROTATION_SPEED 0

    void setup() 
        else if (output_select == 1) 
        else 
      }
      else
      

    }//end setup

    void loop() 

      //get time based on how long the Arduino has been running
      currentMillis = millis();

      if (output_select == 0 ) 
      else if (output_select == 1) 
      else if (output_select == 2) 
      else 

        oled.clear(PAGE);            // Clear the display
        updateDisplay();
        displayProgressBar(); // Draws a progress bar at the bottom of the screen
        oled.display();

        //TMP117 temperature with comma delimiter for graphing or datalogging
        SerialUSB.print(tempC);
        SerialUSB.print(",");  //seperator
        SerialUSB.println(tempF);

      }

      //delay(5); // Delay added for easier readings
    }//end loop

    //This function updates the display if we are scrolling through all displays with a progress bar.
    void updateDisplay() 

    }

    // This function displays the temperature in °C as big digits.
    void displayC() 

    // This function displays the temperature in °F as big digits.
    void displayF() 

    // This function animates a cube. This is used as a quick screensaver.
    void drawCube()
    

      for (int i = 0; i < 3; i++)
      
      oled.line(p2x[3], p2y[3], p2x[0], p2y[0]);
      oled.line(p2x[7], p2y[7], p2x[4], p2y[4]);
      oled.line(p2x[3], p2y[3], p2x[7], p2y[7]);
    }

    // This function displays both °C and °F on the microOLED
    void displayC_F() 

    // This function draws a line at the very bottom of the screen showing how long
    // it'll be before the screen updates.
    // Based on Jim's micro OLED code used in the Photon SIK KIT => [ https://github.com/sparkfun/Inventors_Kit_For_Photon_Experiments/blob/master/11-OLEDApps/Code/02-WeatherForecast/WeatherApp.ino ]
    void displayProgressBar() 

### Qwiic TMP102 [Option 2]

If you opted to use the Qwiic TMP102, copy and paste the following code to your Arduino IDE. Make sure the switch is flipped to the ON position on the board before hitting the upload button.

    language:c
    /******************************************************************************
      Digital Indoor Temperature Monitor with the TMP102
      Written by: Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: Mar 26, 2019

      Description: This sketch configures temperature sensors and prints the
      temperature in degrees celsius and fahrenheit to the Qwiic microOLED.
      Simply adjust the `output_select` to view the °C, °F, or both. You can
      also output the values to the Serial Monitor or Plotter at 115200 baud
      to view the data. There is also a demo mode that displays each output
      on the microOLED with a progress bar at the bottom.

      Resources/Libraries:
      Wire.h (included with Arduino IDE)
      SparkFunTMP102.h (included in the src folder) http://librarymanager/All#SparkFun_TMP102
      SFE_MicroOLED.h (included in the src folder)  http://librarymanager/All#SparkFun_micro_OLED

      Development Environment Specifics:
      Arduino 1.8.10+

      License:
      This code is released under the MIT License (http://opensource.org/licenses/MIT)
      Distributed as-is; no warranty is given.

    ******************************************************************************/

    #include <Wire.h>           // Used to establish SerialUSB communication on the I2C bus
    #include <SparkFunTMP102.h> // Used to send and recieve specific information from our sensor
    #include <SFE_MicroOLED.h>  // Include the SFE_MicroOLED library

    //#define SerialUSB Serial     //Uncomment if you are not using a native USB like the Atmega32U4 or SAMD21

    ///////////////////////////////
    ///////// micro OLED //////////
    ///////////////////////////////

    #define PIN_RESET 7         // A pin needs to be declared even though we are not physically connecting to the Qwiic micro OLED via I2C
    #define DC_JUMPER 1
    MicroOLED oled(PIN_RESET, DC_JUMPER);    // I2C declaration

    ///////////////////////////////
    /////////// TMP102 ////////////
    ///////////////////////////////

    // The default address of the device is 0x48 = (GND)
    TMP102 sensor; // Initalize sensor

    //Set up variables to hold temperature
    float tempC = 0;
    float tempF = 0;

    //0 = output degrees °C
    //1 = output degrees °F
    //2 or any other number = output degrees °C and °F
    int output_select = 3; //select output

    ///////////////////////////////
    // Display Mode Page Control //
    ///////////////////////////////
    // This enum defines all of our display modes and their order.
    enum t_displayModes ;

    const int NUM_DISPLAY_MODES = 4; // Number of values defined in enum above
    volatile int displayMode = NUM_DISPLAY_MODES - 1; // Keeps track of current display page

    const unsigned long DISPLAY_UPDATE_RATE = 4000; // Cycle display every 5 seconds
    unsigned long lastDisplayUpdate = 0; // Stores time of last display update
    unsigned long currentMillis = 0; // Stores time of last display update

    float percentage = 0; //store percent for progress bar
    int progressWidth = 0; // Width of progress bar depends on the [% * (64 pixels wide)]
    int progressY = 0;     //location of the progress bar at the botton of the microOLED

    ///////////////////////////////
    /////// Initialize Cube ///////
    ///////////////////////////////

    int SCREEN_WIDTH = oled.getLCDWidth();
    int SCREEN_HEIGHT = oled.getLCDHeight();

    float d = 3;
    float px[] = ;
    float py[] = ;
    float pz[] = ;

    float p2x[] = ;
    float p2y[] = ;

    float r[] = ;

    #define SHAPE_SIZE 600
    // Define how fast the cube rotates. Smaller numbers are faster.
    // This is the number of ms between draws.
    //#define ROTATION_SPEED 0

    void setup() 
        else if (output_select == 1) 
        else 
      }
      else
      

      sensor.wakeup(); // wake the sensor up, we do not care about low power mode since we will constantly be reading the temperature

    }//end setup

    void loop() 
      else if (output_select == 1) 
      else if (output_select == 2) 
      else 

        oled.clear(PAGE);            // Clear the display
        updateDisplay();
        displayProgressBar(); // Draws a progress bar at the bottom of the screen
        oled.display();

        //TMP102 temperature with comma delimiter for graphing or datalogging
        SerialUSB.print(tempC);
        SerialUSB.print(",");  //seperator
        SerialUSB.println(tempF);

      }

      //delay(5); // Delay added for easier readings

    }//end loop

    //This function updates the display if we are scrolling through all displays with a progress bar.
    void updateDisplay() 

    }

    // This function displays the temperature in °C as big digits.
    void displayC() 

    // This function displays the temperature in °F as big digits.
    void displayF() 

    // This function animates a cube. This is used as a quick screensaver.
    void drawCube() 

      for (int i = 0; i < 3; i++)
      
      oled.line(p2x[3], p2y[3], p2x[0], p2y[0]);
      oled.line(p2x[7], p2y[7], p2x[4], p2y[4]);
      oled.line(p2x[3], p2y[3], p2x[7], p2y[7]);
    }

    // This function displays both °C and °F on the microOLED
    void displayC_F() 

    // This function draws a line at the very bottom of the screen showing how long
    // it'll be before the screen updates.
    // Based on Jim's micro OLED code used in the Photon SIK KIT => [ https://github.com/sparkfun/Inventors_Kit_For_Photon_Experiments/blob/master/11-OLEDApps/Code/02-WeatherForecast/WeatherApp.ino ]
    void displayProgressBar() 

------------------------------------------------------------------------

After uploading the appropriate code for your temperature sensor, the Qwiic microOLED will begin displaying the temperature with different views. There should be an option to just display the temperature in degrees Celsius, Fahrenheit, or both temperatures at the same time depending on your personal preference. Just make sure to adjust the `output_select` as `0`, `1`, or `2`, respectively. When finished, insert the USB cable to a USB power supply to power the board using a wall outlet.

[![Temperature being read by the Qwiic TMP117 and Displayed on the micro OLED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor_Demo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/1/Qwiic_Micro_Ambient_Room_Temperature_Sensor_Demo.jpg)