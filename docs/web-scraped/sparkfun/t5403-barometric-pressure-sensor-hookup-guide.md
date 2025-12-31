# Source: https://learn.sparkfun.com/tutorials/t5403-barometric-pressure-sensor-hookup-guide

## Introduction 

The [T5403](https://www.sparkfun.com/products/12039) is a barometric pressure sensor with an I^2^C (\"Wire\") interface. Barometric pressure sensors measure the absolute pressure of the air around them. This pressure varies with both the weather and altitude. Depending on how you interpret the data, you can monitor changes in the weather, measure altitude, or any other tasks that require an accurate pressure reading.

[![SparkFun Barometric Sensor Breakout - T5403](https://cdn.sparkfun.com/r/600-600/assets/parts/8/6/0/0/12039-01.jpg)](https://www.sparkfun.com/products/12039)

### [SparkFun Barometric Sensor Breakout - T5403](https://www.sparkfun.com/products/12039) 

[ SEN-12039 ]

This is the T5403 breakout board, a fully calibrated barometric pressure sensor with an I2C interface. The T5403 sensor measu...

**Retired**

### Covered in This Tutorial

We will show you how to connect this sensor to an Arduino microcontroller and use the included software library to get measurements out of the sensor. We\'ll also show you how to interpret the readings for both monitoring the weather and showing changes in altitude.

### Suggested Reading

This part is easy to use. But before you start, we recommend the following background knowledge:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Connecting the Hardware

In this example, we will communicate with the T5403 using the I2C interface. While there are connections for SPI, they are currently unsupported.

### Connection Names

The T5403 Breakout Board breaks out eight connections from the IC. We traditionally call these connections \"pins\" because they come from the pins on the IC, but they are actually holes that you can solder [wires](https://www.sparkfun.com/products/11367) or [header pins](https://www.sparkfun.com/products/116) to.

[![T5403 breakout board](https://cdn.sparkfun.com/assets/parts/8/6/0/0/12039-02.jpg)](https://cdn.sparkfun.com/assets/parts/8/6/0/0/12039-02.jpg)

We\'ll connect four of the eight pins on the board to your Arduino. The four pins you need are labeled **GND**, **VCC**, **SCL**, and **SDA**.

### Connecting Headers to the Board

You can use any method you like to make your connections to the board. For this example, we\'ll solder on a eight-pin length of [male-male header strip](https://www.sparkfun.com/products/116), and use [male-female jumper wires](https://www.sparkfun.com/products/9385) to connect the T5403 to your Arduino.

Solder a 8-pin length of male-male header to the board. You can solder it to either side. The bottom is more useful for breadboards, and the top is more useful for jumper wires.

[![T5403 Sensor with Headers](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/5/T5403-Barometric-Sensor-with-Headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/5/T5403-Barometric-Sensor-with-Headers.jpg)

*Note that the T5403 is sensitive to moisture. When you\'re done soldering, do not clean off the flux by rinsing the board in water or other fluids.*

### Connecting the Board to your Arduino

When you\'re done soldering, connect the VCC, GND, SCL, and SDA pins to your Arduino. Different Arduino models use different pins for the I^2^C interface; use the following chart to determine where to plug everything in.

IMPORTANT: Connect the power pins (VCC and GND) **ONLY** to a 3.3V supply. Larger voltages will permanently damage the part. Note that because I^2^C uses [open drain drivers](https://learn.sparkfun.com/tutorials/i2c/i2c-at-the-hardware-level), it is safe to connect the I^2^C pins (DA and CL) to an I^2^C port on a 5V microprocessor.

T5403 label

Pin function

Arduino connection

**GND**

ground

**GND**

**VCC**

3.3V power supply

**3.3V**

**SDA**

I^2^C data

Any pin labeled SDA, or:

  ------------------------------- --------
  Uno, Redboard, Pro / Pro Mini   **A4**
  Mega, Due                       **20**
  Leonardo, Pro Micro             **2**
  ------------------------------- --------

**SCL**

I^2^C clock

Any pin labeled SCL, or:

  ------------------------------- --------
  Uno, Redboard, Pro / Pro Mini   **A5**
  Mega, Due                       **21**
  Leonardo, Pro Micro             **3**
  ------------------------------- --------

**MISO**

Unsupported

**Unsupported**

**Reset/&SS**

Device Reset

**Any I/O - Logic \"LOW\" to reset**

**SEL**

I2C/SPI mode select

**Any I/O - Logic \"LOW\" for SPI mode (Unsupported)**

**EOC**

End Of Conversion Interrupt

**Any I/O or interrupt enabled pin - Outputs \"HIGH\" when measurement is complete**

[![T5403 Frtizing Diagram](https://cdn.sparkfun.com/r/500-500/assets/d/f/8/d/7/T5400_Frtizing_Diagram.png)](https://cdn.sparkfun.com/assets/d/f/8/d/7/T5400_Frtizing_Diagram.png)

Once you have the T5403 connected to your Arduino, we\'re ready to play with the software.

## Installing the Arduino Library

Libraries are collections of software functions geared towards a single purpose, such as communicating with a specific device. Arduino comes with a number of built-in libraries that help you do advanced tasks. We\'ve written an Arduino library called SFE_T5403 that allows you to easily talk to the T5403 sensor. This library is not included with the stock Arduino software, but don\'t worry, installing new libraries is easy.

If you\'d like to interface the T5403 to a microcontroller other than an Arduino, the C++ source code in the [library](https://github.com/sparkfun/SparkFun_T5403_Barometric_Sensor_Arduino_Library/tree/V_1.0) and the information in the [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/5/T5400_1.pdf) may be helpful when writing your own code.

**1. Install the Arduino IDE**

If you don\'t already have the Arduino IDE (Integrated Development Environment) installed, download the version for your system (Windows, Mac, Linux) from <http://arduino.cc/en/Main/Software> and install it following the instructions on that site.

If you need help installing the IDE, check out our [tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide/introduction).

**2. Install the SFE_T5403 Library**

User-installed libraries live in a \"libraries\" folder within your personal Arduino sketch folder. On Windows systems your personal sketch folder is located in \"My Documents/Arduino\". On Mac computers, it\'s \"\~/Documents/Arduino\". On Linux it is usually \"\~/Arduino/sketchbook\". **Locate your personal Arduino sketch folder and open it so you can drag new files into it**.

Now **download the latest T5403 software archive** from this link: <https://github.com/sparkfun/SparkFun_T5403_Barometric_Sensor_Arduino_Library/archive/V_1.0.zip>. You can either save the file to your system and open it later, or open it directly.

(Note that you can find the .zip file for any Github repository by looking for the \"Download ZIP\" button on the main page:)

[![alt text](https://cdn.sparkfun.com/assets/c/5/1/7/3/52bca9fcce395f03498b4569.png)](https://cdn.sparkfun.com/assets/c/5/1/7/3/52bca9fcce395f03498b4569.png)

Open the .zip file you just downloaded. (On most systems you should be able to double-click it to show the included files.) Open the folder called \"T5403_Barometric_Breakout-master\", then \"software\", then \"Arduino\". You should now see a folder called \"libraries\". **Drag the \"libraries\" folder from the .zip folder into your personal Arduino sketch folder**. If you get a warning that there is already a libraries folder there, that\'s fine. It just means you\'ve already installed some libraries, which is great! Just tell your system to go ahead and overwrite them, which sounds alarming but will only add the new library to the existing folder.

[![alt text](https://cdn.sparkfun.com/assets/8/8/2/0/6/52bcd399ce395f2b628b4568.png)](https://cdn.sparkfun.com/assets/8/8/2/0/6/52bcd399ce395f2b628b4568.png)

That\'s it! Now restart the Arduino IDE and you should be ready to go.

If any of these instructions are unclear, you can find more detailed instructions in our [installing an arduino library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial.

## Running the Example Sketches

### Running the Example Sketch

The library you just installed includes an example sketch that show basic operation of the T5403. This are designed to be a starting point for writing your own code.

After you install the library, run the Arduino IDE, and open the following menu item: File / Examples / SFE_T5403 / SFE_T5403_example.

(If you don\'t see this menu item, you may not have installed the library correctly, or didn\'t restart the Arduino IDE. Take another look at the [library installation page](https://learn.sparkfun.com/tutorials/t5403-barometric-pressure-sensor-hookup/installing-the-arduino-library) to see if you missed any steps.)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/5/Screen_Shot_2014-03-06_at_5.59.17_PM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/5/Screen_Shot_2014-03-06_at_5.59.17_PM.jpg)

When the example opens, upload it to your Arduino (remember to select the correct board type and serial port), and open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) to 9600 baud. You should see some diagnostic information (if it can\'t find the device, double check your hardware connections) followed by measurement readings. For more about interpreting these readings, see the next page, Measuring Weather and Altitude.

### Writing Your Own Sketches

The comments and code in the example sketch should get you started when writing your own sketches. In many cases you should be able to copy and paste the example code into your own sketch.

## Measuring Weather and Altitude

The T5403 was designed to accurately measure atmospheric pressure. Atmospheric pressure varies with both weather and altitude; you can measure both of these using this sensor. Here\'s how:

### What is Atmospheric Pressure?

The definition of pressure is a force \"pressing\" on an area. A common unit of pressure is pounds per square inch (psi). One pound, pressing on one square inch, equals one psi. The [SI unit](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units/si-units) is newtons per square meter, which are called [pascals (Pa)](http://en.wikipedia.org/wiki/Pascals).

There are lots of situations in which pressure can be measured (gravity, pull, etc.), but right now we\'re interested in **atmospheric pressure**, which is the force that the air around you is exerting on everything. The weight of the gases in the atmosphere creates atmospheric pressure. One doesn\'t normally notice that air weighs anything, but if you took a one inch wide column of air from sea level to the top of the atmosphere, it would weigh about 14.7 pounds. (A 1 cm wide column of air would weigh about 1 kg.) This weight, pressing down on the footprint of that column, creates the atmospheric pressure that we can measure with sensors like the T5403.

Because that inch-wide column of air weighs about 14.7 pounds, and is pressing on one square inch, it follows that the average sea level pressure is about 14.7 pounds per square inch (psi), or 101325 pascals. This will drop about 4% for each 1000 feet (or 300 meters) you ascend. The higher you get, the less pressure you\'ll see, because the column to the top of the atmosphere is that much shorter and therefore weighs less. This is useful to know, because by measuring the pressure and doing some math, you can determine your altitude.

**Fun fact:** The air pressure at 12,500 feet (3810 meters) is only half of that at sea level. In other words, half of the mass of the atmosphere is below 12,500 feet, and the air at 12,500 feet is half as dense as that at sea level. No wonder you have a harder time breathing up there.

The T5403 outputs absolute pressure in [hectopascal (hPa)](http://en.wikipedia.org/wiki/Pascals). This is equivalent to 100 pascals (Pa). One pascal is a very small amount of pressure, approximately the amount that a sheet of paper will exert resting on a table. You will more often see measurements in hectopascals (1 hPa = 100 Pa) or kilopascals (1 kPa = 1000 Pa). The Arduino library we\'ve provided outputs values in hPa, which also happens to equal one [millibar (mbar)](http://en.wikipedia.org/wiki/Bar_%28unit%29).

Here are some conversions to other [pressure units](http://en.wikipedia.org/wiki/Pressure_units#Units):

1 hPa = 100 Pa = 1 mbar = 0.001 bar

1 hPa = 0.75006168 Torr

1 hPa = 0.01450377 psi (pounds per square inch)

1 hPa = 0.02953337 inHg (inches of mercury)

1 hpa = 0.00098692 atm (standard atmospheres)

### Temperature Effects

Because temperature affects the density of a gas, and density affects the mass of a gas, and mass affects the pressure (whew), atmospheric pressure will change dramatically with temperature. Pilots know this as \"density altitude\", which makes it easier to take off on a cold day than a hot one because the air is more dense and has a greater aerodynamic effect.

To compensate for temperature, the T5403 includes a rather good temperature sensor as well as a pressure sensor. To perform a pressure reading, you first take a temperature reading, then combine that with a raw pressure reading to come up with a final temperature-compensated pressure measurement. (Don\'t worry, the Arduino library makes all of this very easy.)

### Measuring Absolute Pressure

As we just mentioned, if your application requires measuring absolute pressure, all you have to do is get a temperature reading, then perform a pressure reading (see the [example sketch](https://github.com/sparkfun/SparkFun_T5403_Barometric_Sensor_Arduino_Library/blob/V_1.0/examples/SFE_T5403_example.ino) for details). The final pressure reading will be in hPa = mbar. If you wish, you can convert this to a different unit using the above conversion factors.

Note that the absolute pressure of the atmosphere will vary with both your altitude and the current weather patterns, both of which are useful things to measure.

### Weather Observations

The atmospheric pressure at any given location on earth (or anywhere with an atmosphere) isn\'t constant. The complex interaction between the earth\'s spin, axis tilt, and many other factors result in moving areas of higher and lower pressure, which in turn cause the variations in weather we see every day. By watching for changes in pressure, you can predict short-term changes in the weather. For example, dropping pressure usually means wet weather or a storm is approaching (a low-pressure system is moving in). Rising pressure usually means that clear weather is approaching (a high-pressure system is moving through).

But remember that atmospheric pressure also varies with altitude. The absolute pressure in Denver (altitude 5280\') will always be lower than the absolute pressure in San Francisco (altitude 52\'). If weather stations just reported their absolute pressure, it would be difficult to directly compare pressure measurements from one location to another (and large-scale weather predictions depend on measurements from as many stations as possible).

To solve this problem, weather stations always remove the effects of altitude from their reported pressure readings by mathematically adding the equivalent fixed pressure to make it appear as if the reading was taken at sea level. When you do this, a higher reading in San Francisco than Denver will always be because of weather patterns, and not because of altitude.

To do this, there is a function in the sketch called `seaLevel(P,A)`. This takes absolute pressure (P) in hPa, and the station\'s current altitude (A) in meters, and removes the effects of the altitude from the pressure. You can use the output of this function to directly compare your weather readings to other stations around the world.

For more information, here is a good Wikipedia article on [mean sea level pressure](http://en.wikipedia.org/wiki/Atmospheric_pressure#Mean_sea_level_pressure).

### Determining Altitude

Since pressure varies with altitude, you can use a pressure sensor to measure altitude (with a few caveats).

The average pressure of the atmosphere at sea level is 1013.25 hPa (or mbar). This drops off to zero as you climb towards the vacuum of space. Because the curve of this drop-off is well understood, you can compute the altitude difference between two pressure measurements (p and p~0~) by using this equation:

[![alt text](https://cdn.sparkfun.com/assets/3/3/2/0/4/527d393b757b7f68548b456f.jpg)](https://cdn.sparkfun.com/assets/3/3/2/0/4/527d393b757b7f68548b456f.jpg)

There are two ways you can take advantage of this.

1.  If you use sea level pressure (1013.25 hPa) as the baseline pressure (p~0~), the output of the equation will be your current altitude above sea level.

2.  Or, if you take a single pressure reading at your current location, and use that as your baseline (p~0~), all subsequent pressure readings will result in *relative* altitude changes from the baseline. Climb the stairs and you should see the altitude go from zero to 3 or 4 meters. Go down to the basement, and you\'ll see -3 or -4 meters. There\'s an example function in the example sketch called `altitude(P,P0)` that calculates the relative altitude change. If you give it the sea level pressure (1013.25 hPa) for p~0~, and your local pressure for p, it will give you your altitude above sea level. If you use a local pressure measurement for p~0~, subsequent p pressure readings will give you your change in altitude from the baseline.

Now for the caveats:

**Accuracy:** How accurate is this? The theoretical noise level at the T5403s highest resolution is 0.25m (about 10 inches), though in practice we see noise on the order of 1m (40 inches). You can improve the accuracy by taking a large number of readings and averaging them, although this will slow down your sample rate and response time.

**Weather:** You should also remember that pressure changes due to weather will affect your altitude readings. The best accuracy will be obtained if you take a \"fresh\" p~0~ when you need it and don\'t rely on it to be accurate for extended periods due to changes in the weather.

**Maximum altitude:** The T5403 can\'t measure all the way down to vacuum (or up to space). It\'s advertised lower limit is about 300 hPa (or mbar), which corresponds to an altitude of about 3000m or 30,000 feet. People have flown these to higher altitudes and gotten useful results, but this isn\'t guaranteed or likely to be accurate. (You might consider using [GPS](https://learn.sparkfun.com/tutorials/gps-basics) for high-altitude measurements).

**Minimum altitude:** Similarly, this sensor isn\'t suited for large pressures either. The advertised upper limit is 1100 hPa=mbar (or 16 psi), which is about 500 feet below sea level (that\'s in air - the T5403 isn\'t submersible in water). This sensor isn\'t a good choice for submersible or compressed-gas measurements.

## Tips and Tricks

### Things to Watch Out For

**Give it the right voltage:** The T5403 will operate on voltages from 1.7v to 3.6v. We recommend operating it at 3.3V. **Never connect the \"+\" header to voltages higher than 3.6V!**. Note that it is safe to connect the SCA and SDL pins to an I^2^C port on a 5V Arduino, as the pullup resistors on the T5403 board will keep the voltage below 3.6V.

**Give it air:** Remember that the T5403 needs access to ambient air to measure its pressure, so don\'t put it in a sealed case. Providing a small vent hole should be adequate.

**But not too much air:** On the other hand, exposure to fast-moving air or wind can cause momentary pressure variations that will affect your readings. Shield the device from strong air currents.

**Keep it cool:** Because an accurate temperature reading is needed to measure the pressure, try not to expose the device to rapid temperature changes, and keep it away from nearby hot parts and other heat sources.

**Keep it dry:** The T5403 is sensitive to moisture. Don\'t submerge it or allow it to contact liquid water.

### Changing the Solder Jumper

Solder jumpers are closely-spaced pads on a printed circuit board that are covered by blobs of solder to create an electrical connection. The T5403 breakout board has one such jumper; you can remove the solder from these pads to break the connection and alter the function of the board.

**To remove the solder from a solder jumper**, cover it with [solder wick](https://www.sparkfun.com/products/9327), and carefully heat it with a soldering iron. When the solder melts, it will be absorbed by the wick. Remove the wick before the solder cools so it doesn\'t stick to the pads. If you didn\'t get all of the solder on the first pass, give it another try with a clean section of solder wick. When you\'re done you should be able to see a broken connection between the pads. While doing this be careful not to overheat the board (let it cool off if you\'re having problems), or the copper pads may lift from the board.

[![T5403 Breakout Board](https://cdn.sparkfun.com/assets/parts/8/6/0/0/12039-02.jpg)](https://cdn.sparkfun.com/assets/parts/8/6/0/0/12039-02.jpg)

#### Disabling the I^2^C pullup resistors (SJ1)

The T5403 communicates with a host microcontroller via a communications standard called [\"I^2^C\"](https://learn.sparkfun.com/tutorials/i2c) (for Inter Integrated Circut). I^2^C uses two wires, usually labeled SCL (Serial Clock) and SDA (Serial Data). To function properly, I^2^C requires a pullup resistor on each of those lines. The T5403 board includes these resistors. They\'re enabled by default, but you can disable them by clearing solder jumper.

I^2^C allows you to have multiple devices connected to the same two lines (collectively called a bus). The pullup resistors allow the bus to function, but you should only have **one** set of pullup resistors per bus.

**If you have just one I^2^C device (such as the T5403 breakout board) connected to your microcontroller, the board is already set up properly. You don\'t need to change anything.**

However, if you wish to connect more than one device to the bus, you should ensure that there is only one set of pullup resistors enabled on the bus. You do this by disabling every set of pullup resistors except one. (It doesn\'t matter where the enabled resistors live; they can be anywhere on the bus.)

**To disable the I^2^C pullup resistors**, remove **all** of the solder from the jumper. This jumper has three pads; be sure to separate all of the pads from each other. Remember that you\'ll need to ensure that another set of pullup resistors are enabled somewhere on the I^2^C bus.

**Note** that you should not operate an I^2^C bus without pullup resistors, as the internal weak pull-up resistors in the Arduino will pull the bus to 5V, which may damage the T5403.

#### Using the EOC pin

The End of Conversion (EOC) pin is used to signal when the T5403 is finished taking a measurement. There is a waiting period to read a measurement from the device. This time varies with the measurement type and accuracy desired. The example code uses preset delays as stated in the data sheet.