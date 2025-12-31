# Source: https://learn.sparkfun.com/tutorials/lilypad-temperature-sensor-hookup-guide

## Introduction

The [LilyPad Temperature Sensor](https://www.sparkfun.com/products/8777) lets you detect temperature changes in the environment (or an object pressed against the sensor) on your wearable project.

[![LilyPad Temperature Sensor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/9/7/08777-01.jpg)](https://www.sparkfun.com/lilypad-temperature-sensor.html)

### [LilyPad Temperature Sensor](https://www.sparkfun.com/lilypad-temperature-sensor.html) 

[ DEV-08777 ]

The MCP9700 is a small thermistor type temperature sensor. LilyPad is a wearable e-textile technology developed cooperatively...

[ [\$5.95] ]

The temperature sensor board will output specific voltage at set temperatures - 10mV for every degree Celsius (°C), with 0 degrees C set at 0.5V. The current flowing through the signal tab can be read by an analog tab on a LilyPad Arduino board and converted through a formula to degrees in Celsius or Fahrenheit. Follow along to learn how to convert the voltage from the sensor into usable temperature data in your project.

You will need to connect the sensor to a LilyPad Arduino or other microcontroller to read the output values and use in your code.

### Required Materials

To follow along with the code examples, we recommend:

### Suggested Reading

To add this sensor to a project, you should be comfortable sewing with conductive thread and uploading code to your LilyPad Arduino. Here are some tutorials to review before working with this sensor:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

[](https://learn.sparkfun.com/tutorials/choosing-a-lilypad-arduino-for-your-project)

### Choosing a LilyPad Arduino for Your Project 

Not sure which LilyPad Arduino is right for you? We\'ll discuss the features of each and help you decide.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

## Attaching to a LilyPad Arduino

The LilyPad Temperature Sensor has three sew tabs - **Power** (+), **Ground** (-), and **Signal** (S). The signal tab will be connected to an analog tab (marked with an \'A\') on a LilyPad Arduino.

### LilyPad Arduino USB

To follow along with the code examples in this tutorial, connect the temperature sensor to a LilyPad Arduino as shown below. Use alligator clips to temporarily connect **Signal** to **A3** on a LilyPad Arduino, **(-)** to **(-)** on the LilyPad, and the **(+)** to **(A5)**. When you are finished prototyping, replace the alligator clips with conductive thread traces for permanent installation in your project.

To make our diagrams easier to follow, and to avoid any potential short circuits in our stitching, we\'ll be connecting the **Power** pin to A5, which we will then set to **HIGH** in our code. This will act as an additional power attachment.

[![Attaching Sensor to a LilyPad USB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/7/TemperatureSensorHookup_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/7/TemperatureSensorHookup_1.png)

### LilyPad ProtoSnap Plus

If following along with a [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346), clip the temperature sensor\'s signal sew tab to expansion port A9. Learn more about using the expansion ports in the [LilyPad ProtoSnap Plus Hookup Guide](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-hookup-guide#using-the-expansion-ports).

[![Attaching Sensor to a LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/7/TempSensor_ProtoSnapPlus.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/7/TempSensor_ProtoSnapPlus.png)

After clipping the sensor to A9, move the slide switch to the OFF position to keep the switch from interfering with your input signal.

[![Turn Switch OFF for A9](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)

#### Other LilyPad Connection Notes:

- If using the [ProtoSnap - LilyPad Development Simple](https://www.sparkfun.com/products/11201) - attach to the metal tab at the top right of the board, this connects to A3. You can also set pin A5 to HIGH in your code to use it as an additional power tab, as the LilyPad Simple\'s tab is hard to access in the ProtoSnap format.
- If using the the pre-wired temperature sensor on the [ProtoSnap - LilyPad Development Board](https://www.sparkfun.com/products/11262), it is attached to pin A1.

## Interpreting Sensor Readings

The sensor produces an analog voltage representing the temperature near it. In order to get readings in degrees, we\'ll have to do some math. The voltage output from the sensor is linearly proportional to the Celsius temperature. Once you know the output voltage of the sensor, you can calculate the temperature with this equation:

[![](http://latex.codecogs.com/gif.latex?\degree&space;Celsius=(voltage&space;-&space;0.5)\,*\,100 "temperature \degree Celsius=(voltage - 0.5) * 100")](http://www.codecogs.com/eqnedit.php?latex=\degree&space;Celsius=(voltage&space;-&space;0.5)\,*\,100)

\

To convert that reading to Fahrenheit, use this formula:

[![](http://latex.codecogs.com/gif.latex?\degree&space;Fahrenheit&space;=&space;(\degree&space;Celsius&space;*&space;9.0&space;/&space;5.0)&space;+&space;32.0 "temperature \degree Fahrenheit = (\degree Celsius * 9.0 / 5.0) + 32.0")](http://www.codecogs.com/eqnedit.php?latex=\degree&space;Fahrenheit&space;=&space;(\degree&space;Celsius&space;*&space;9.0&space;/&space;5.0)&space;+&space;32.0)

\

Next, we\'ll be use [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to read the values coming from the sensor and insert the formulas in our code to display the temperature in both Celcius and Farenheit.

**Note:** Upload the following code to your LilyPad Arduino, making sure to select the correct LilyPad board from the drop down menu below. Choose **LilyPad Arduino USB** if using a LilyPad Arduino USB. The LilyPad Arduino Simple, LilyPad Arduino, and LilyPad Development Board, and Development Board Simple all use a **LilyPad ATmega 328**. Select **LilyPad USB Plus** if following along with the LilyPad ProtoSnap Plus.\
\
Don\'t forget to select the Serial Port that your LilyPad is connected to.\
\
If prototyping with a LilyPad Development Board, change **`sensorPin`** to A1.

    language:c

    /*
    LilyPad Temperature Sensor Example
    SparkFun Electronics
    https://www.sparkfun.com/products/8777

    This code reads the input of the temperature sensor, converts it to Farenheit and Celsius
    and prints to the Serial Monitor.

    Temperature sensor connections:
       * S tab to A3
       * + tab to A5 (or +)
       * - tab to -

    Follow the tutorial at:
    https://learn.sparkfun.com/tutorials/lilypad-temperature-sensor-hookup-guide

    This code is released under the MIT License (http://opensource.org/licenses/MIT)
    ******************************************************************************/

    // Connect the S tab of the Temperature Sensor to A3
    // If using the LilyPad ProtoSnap Plus, change to A9
     int sensorPin = A3;  

    void setup()
    

    void loop()
    

After uploading the code to your LilyPad Arduino, click the magnifying glass icon at the top right of your Arduino window to open the Serial Monitor window. You should begin seeing some values from the sensor. Try placing your finger over the sensor to see the readings change.

[] Be careful not to place anything wet on the sensor circuit when trying to get readings from cold items, it could damage the circuit.

## Using Values to Trigger Behaviors

Next, we\'ll use some of the readings we gathered to trigger an action or behavior when the temperature is above or below a set threshold.

This example uses the built-in LED attached to pin 13 on the LilyPad Arduino.

    language:c
    /*
    LilyPad Temperature Trigger Example
    SparkFun Electronics
    https://www.sparkfun.com/products/8777

    This code reads the input of the temperature sensor and compares it to
    a set variable named 'threshold'. If temperature is above 
    the thermalAlert threshold, the built-in LED on the LilyPad Arduino will turn 
    on. If the temperature falls below the threshold, the LED will turn off. 

    Temperature sensor connections:
       * S tab to A3
       * + tab to A5 (or +)
       * - tab to -

    Follow the tutorial at:
    https://learn.sparkfun.com/tutorials/lilypad-temperature-sensor-hookup-guide

    This example is based on Thermal Alert! example in the Digital Sandbox:
    https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/12-thermal-alert
    This code is released under the MIT License (http://opensource.org/licenses/MIT)
    ******************************************************************************/

    // Connect the S tab of the Temperature Sensor to A3
    // If using the LilyPad ProtoSnap Plus, change to A9
     int sensorPin = A3;
     int alertLED = 13;

    // Set temperature threshold variable to check against. If the temperature reading is above
    // this number in degrees Fahrenheit, the LED will turn on
     int threshold =  80; // 80 degrees Fahrenheit

    void setup()
    

    void loop()
     else 
      // Wait 1 second between readings
      delay(1000);  
    }

In this code, we use an `if()` statement to compare the value of `threshold` to the converted analog readings from the temperature sensor stored in the `fahrenheit` variable. If the temperature is too hot (higher than the threshold\'s set value), then the LED will turn on. If the value is lower than the threshold, the LED will turn off.

If are having trouble getting temperatures that trigger the LED, check the output of the Serial Monitor to see if there\'s a better value for `threshold` than what is set in the example code.

## Project Examples

After prototyping and testing a project with the temperature sensor you can replace the connections with conductive thread in your project. Follow this guide for an introduction to connecting LilyPad pieces with conductive thread:

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

December 17, 2016

Learn how to use conductive thread with LilyPad components.

Need some inspiration for your next project? Check out some of the projects below from the community.

### Breathe 3.0 Scarf by Hilary Hayes

Hilary used a LilyPad Arduino, temperature sensor, conductive thread, bright white LEDs, purple wool yarn to create a scarf that illuminates with the wearer\'s breath.

[![Breathe 3.0 Scarf by Hilary Hayes](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/7/Breathe3_HilaryHayes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/7/Breathe3_HilaryHayes.jpg)

*Photo courtesy of [Fashioning Technology](http://fashioningtech.com/profiles/blogs/the-breathe-project)*

### Hands-on-Warm by Maria Julia Guimaraes

The Hands-on-Warm project uses a LilyPad Arduino, LilyPad Temperature Sensor, and heating pad to warm the hands of people who experience extreme cold sensitivity.

*[Hands-on-Warm](https://vimeo.com/214435041) from [Maria Julia Guimaraes](https://vimeo.com/mjguimaraes) on [Vimeo](https://vimeo.com).*