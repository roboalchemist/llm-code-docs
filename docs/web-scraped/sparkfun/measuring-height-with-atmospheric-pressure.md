# Source: https://learn.sparkfun.com/tutorials/measuring-height-with-atmospheric-pressure

## Introduction

It can be easy to forget that we are constantly under pressure (although Freddie and Bowie tried to tell us) from the atmosphere around us. Not only that, it's a bit counterintuitive: the higher up you go, the less pressure there is, and vice versa. There are a few ways we encounter this in our day to day, like maintaining cabin pressure on a plane at 30,000 feet or water boiling just a little bit faster out here in the Rockies! With this project, we're going to play around with the atmosphere around us, and do a little bit of math, to create a **pressure sensor-based height measuring tool**!

The powerhouse of this project is the [Qwiic MicroPressure Sensor](https://www.sparkfun.com/products/16476). This sensor has an onboard Honeywell 25psi piezoresistive silicon pressure sensor which gives the ability to measure very minute differences in absolute pressure. We\'ll take those pressure measurements, apply some math inside the code and translate the change in pressure from a bottom and top reading into a height measurement.

[![Qwiic MicroPressure Sensor](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/3/micropressure.jpg)](https://www.sparkfun.com/products/16476)

## Required Materials 

Here are all of the parts you'll need to follow along with this tutorial! You can add what you need or, if you don't have any of these parts already, you can click to the wishlist provided and purchase it all in one go!

 

 

## Hardware Hookup 

Luckily, the hardware is pretty easy to hookup; simply connect one end of your Qwiic cable to your Thing Plus, and the other end to your sensor. Boom! You're done! The parts list below includes a USB cable for power but this project could also be used with a battery for maximum portability.

[![Hook Up Micropressure Sensor to ESP32 Thing Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/3/height_demo_hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/3/height_demo_hookup.jpg)

## Software Setup and Programming

To run this project, you'll need to install the [SparkFun MicroPressure Library](https://github.com/sparkfun/SparkFun_MicroPressure_Arduino_Library/archive/main.zip) (for more information on how to install this library, and take advantage of its example sketches, check out our [SparkFun Qwiic MicroPressure Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micropressure-hookup-guide?_ga=2.5718067.1228778160.1661805429-474297639.1657643598)!).

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micropressure-hookup-guide)

### SparkFun Qwiic MicroPressure Hookup Guide 

July 23, 2020

Get started using your Qwiic MicroPressure breakout board with this hookup guide.

## Height Demo Code

Once the library is installed, go ahead and open up a blank sketch. Make sure to select your board (SparkFun ESP32 Thing Plus) and COM port before uploading, and to hold down the boot button on your Thing Plus during the upload! The boot button is also what we'll be using to tell the system when we'd like to take a reading; let us away to the code!

    //SparkFun Qwiic MicroPressure Height Measuring Demo
    //Original Demo by: Dryw Wade, Adapted for Qwiic MicroPressure by: Mariah Kelly

    #include <Wire.h>
    #include <SparkFun_MicroPressure.h>  // Click here to get the library: https://github.com/sparkfun/SparkFun_MicroPressure_Arduino_Library/archive/main.zip

    #define EOC_PIN  -1
    #define RST_PIN  -1
    #define MIN_PSI   0
    #define MAX_PSI   25

    SparkFun_MicroPressure mpr(EOC_PIN, RST_PIN, MIN_PSI, MAX_PSI);

    // Button pin (using boot button on board)
    int buttonPin = 0;

    // Interrupt flag for button presses
    volatile bool buttonPressed = false;

    // Time to wait after a button press before reading the next button press (helps with debouncing)
    unsigned long timerDelay = 500;

    // Measured pressure at the bottom and top of the measurement
    int bottomPressure = 0;
    int topPressure;

    // Calibrated number of inches per Pascal of pressure difference. Note that it's negative, because lower altitude results in higher pressure
    float inchesPerPascal = -3.3;

    // Using arrays to take multiple readings and display average
    #define numReadings 500
    int bottomReadings[numReadings];
    int topReadings[numReadings];

    // Breaking up array calculations
    boolean measuring = true;
    boolean showData = true;

    void setup() 

    // Configure button pin as interrupt
    attachInterrupt(digitalPinToInterrupt(buttonPin), myISR, FALLING);
    }

    void loop() 
        measuring = false;
      } 
      if (showData) 
        bottomPressure = bottomPressure / numReadings;
        // Print out the bottom pressure
        Serial.print("Bottom pressure: ");
        Serial.print(bottomPressure);
        Serial.print(" Pa        ");
        showData = false;
      }
      measuring = true;
      showData = true;
    } else 
        measuring = false;
      } 
      if (showData) 
        topPressure = topPressure / numReadings;
        Serial.print("Top pressure: ");
        Serial.print(topPressure);
        Serial.print(" Pa        ");
        showData = false;
      }
      // Compute the difference in pressure
      int pressureDifference = topPressure - bottomPressure;

      // Compute total height in inches using known inches per Pascal
      int inches = pressureDifference * inchesPerPascal;

      // Compute number of feet in this height
      int feet = inches / 12;

      // Subtract that many feet from the total number of inches
      inches -= feet * 12;

      // Print computed height in ft'in"
      Serial.print("Height: ");
      Serial.print(feet);
      Serial.print("' ");
      Serial.print(inches, 1);
      Serial.print("\"");
      Serial.println();

      // Reset bottom pressure for next measurement
      bottomPressure = 0;
    }
    // Wait for button to stop bouncing
    delay(timerDelay);

    // Reset flags
    buttonPressed = false;
    measuring = true;
    showData = true;
     }
    }

    void myISR() 

Now that we've uploaded our code, we can find something to measure! I used my desk--including a tape measure for reference--which is about 29 inches tall. Start by placing your system at the lowest point; this is where we'll take our reading for the bottom pressure (we measure bottom to top, since a lower altitude results in a higher pressure, and vise-versa). The code has a built-in sampling system to help stabilize the sensor readings, so it'll take a second or two after pressing the boot button to pop up on the serial monitor; it takes our 'numReadings' value of readings, which is 500 to start, but feel free to change that up as you see fit! Then, all there's left to do is the same series of steps for our top pressure:

[![Measuring Bottom Pressure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/3/bottompress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/3/bottompress.jpg)

[![Measuring Top Pressure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/3/toppress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/3/toppress.jpg)

Now that we have our readings, let's see how we did!

[![Height Demo Serial Monitor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/3/heightdemo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/3/heightdemo.png)

*Readings (in Pascals) and height calculations (feet & inches)*

Not too shabby! We're a few inches off, but that's to be expected with this project. Now the super fun part is experimenting with how you might be able to tweak it to be even more accurate! I tried lots of different things and managed to get the margin of error down to a few inches, rather than feet.