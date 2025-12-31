# Source: https://learn.sparkfun.com/tutorials/esp32-environment-sensor-shield-hookup-guide

## Introduction

The [ESP32 Environment Sensor Shield](https://www.sparkfun.com/products/14153) provides sensors and hookups for monitoring environmental conditions. This tutorial will show you how to connect your sensor suite to the Internet and post weather data online.

[![SparkFun ESP32 Thing Environment Sensor Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/0/6/0/14153-01.jpg)](https://www.sparkfun.com/products/14153)

### [SparkFun ESP32 Thing Environment Sensor Shield](https://www.sparkfun.com/products/14153) 

[ DEV-14153 ]

The SparkFun ESP32 Thing Environment Sensor Shield provides sensors and hookups for monitoring environmental conditions.

**Retired**

### Required Materials

You\'ll need the [ESP32 Thing board](https://www.sparkfun.com/products/13907) to interface with this shield. Other microcontroller boards will work, but since the shield is designed to stack on the ESP32 Thing, interfacing with them will be difficult.

You\'ll also need some means of connecting the two boards together. While it\'s possible to solder them together using [snappable male header pins](https://www.sparkfun.com/products/116), it makes good sense to use [female headers](https://www.sparkfun.com/products/115) on one of the boards board so the boards can be separated again later if needed.

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

The ESP32 Environment Sensor Shield comes with connections for our [weather station](https://www.sparkfun.com/products/8942). You may also wish to add a [soil moisture sensor](https://www.sparkfun.com/products/13322), which you\'ll need two [three-position 3.5mm screw terminals](https://www.sparkfun.com/products/8235) and enough [wire](https://www.sparkfun.com/products/11375) to connect the sensor to the board.

[![SparkFun Soil Moisture Sensor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/1/0/13322-01.jpg)](https://www.sparkfun.com/sparkfun-soil-moisture-sensor.html)

### [SparkFun Soil Moisture Sensor](https://www.sparkfun.com/sparkfun-soil-moisture-sensor.html) 

[ SEN-13322 ]

A simple breakout for measuring the moisture in soil and similar materials. The exposed pads function together acting as a va...

[ [\$6.55] ]

[![Screw Terminals 3.5mm Pitch (3-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/3/08235-Screw_Terminals_3.5mm_Pitch__3-Pin_-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-3-pin.html)

### [Screw Terminals 3.5mm Pitch (3-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-3-pin.html) 

[ PRT-08235 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

[![Weather Meters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/3/3/08942-01.jpg)](https://www.sparkfun.com/products/8942)

### [Weather Meters](https://www.sparkfun.com/products/8942) 

[ SEN-08942 ]

Whether you\'re an agriculturalist, a professional meteorologist or a weather hobbyist, building your own weather station can ...

**Retired**

### Tools

At a minimum, you\'ll need a [soldering iron](https://www.sparkfun.com/products/9507) and some [solder](https://www.sparkfun.com/products/9163). You may need a small screwdriver for attaching the wire to the screw terminals between the soil moisture sensor and the sensor shield. Our [pocket screwdriver](https://www.sparkfun.com/products/12891) and [screwdriver kit](https://www.sparkfun.com/products/10865) both have bits that will work wonderfully for that purpose. They\'re also just handy to keep around!

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Tool Kit - Screwdriver and Bit Set](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/7/10865-01.jpg)](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html)

### [Tool Kit - Screwdriver and Bit Set](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html) 

[ TOL-10865 ]

There\'s nothing worse than getting ready for a good hack and then realizing that you can\'t even get the box open because you ...

[ [\$16.50] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

### Suggested Reading

If you have not yet used the ESP32 Thing Development Board, check out this guide first.

[](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide)

### ESP32 Thing Hookup Guide 

October 27, 2016

An introduction to the ESP32 Thing\'s hardware features, and a primer on using the WiFi system-on-chip in Arduino.

If you intend to use wind and rain [Weather Meters](https://www.sparkfun.com/products/8942) with your ESP32 Environment Sensor Shield, check out our Weather Meter Assembly Guide.

[](https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide)

### Weather Meter Hookup Guide 

July 20, 2017

How to assemble your very own weather meter!

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

The ESP32 Environment Sensor Shield incorporates three sensors capable of measuring five different environmental variables. It also provides connections for several other sensors that can be connected if so desired.

### Onboard Sensors

All of the onboard sensors are connected to the ESP32 via I^2^C connection.

#### Pressure, Humidity, and Temperature

The first onboard sensor is a Bosch BME280. This sensor measures relative humidity, temperature, and barometric pressure. On the back side of the board is a solder jumper (labeled JP1) which can be closed to change the I^2^C address of the chip. By default the address is 0x77; closing the jumper forces the address to 0x76.

[![PHT Sensor region](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_PressureHumidityTemp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_PressureHumidityTemp.png)

#### Air Quality and Temperature

Next is the ams CCS811 air quality and temperature sensor. Note the routed out region around this sensor. That provides a buffer against thermal changes stimulated by the circuitry on the rest of the PCB. As with the BME280, it is possible to change the I^2^C address of this sensor. Closing jumper JP2 on the reverse side of the board causes the sensor to adopt address 0x5A, and by default it will be 0x5B.

[![Air quality region](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_AirQualityTemp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_AirQualityTemp.png)

#### Luminosity

The last onboard sensor is the Broadcom APDS-9301. It\'s capable of detecting and reading light levels from nighttime through broad daylight. Keep in mind that the sensor will saturate if exposed to direct sunlight. By defaul, the sensor will have an I^2^C address of 0x39. By adding a solder jumper toward 0 on the jumper pads labeled JP3 on the back of the board, the address can be changed to 0x29. By adding a solder jumper toward 1, the address can be set to 0x49.

[![light region](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Luminosity.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Luminosity.png)

### Jumpers on Back of the Board

There are five jumpers on the back of the board.

[![Jumpers on board backside](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-BottomJumpers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-BottomJumpers.png)

Here\'s what they do:

**JP1** - Close this jumper with a solder blob to change the I2C address of the BME280 sensor from 0x77 to 0x76.\
**JP2** - Close this jumper with a solder blob to change the I2C address of the CCS811 sensor from 0x5B to 0x5A.\
**JP3** - Close the 0 half of this jumper with a solder blob to set the address of the APDS-9301 sensor to 0x29. Close the 1 half of this jumper to set the address to 0x49. If you accidentally bridge the entire jumper, the address will be 0x29, but nothing bad will happen.\
**JP4** - Cut this trace to disable the onboard NTC thermistor used by the CCS811 for temperature compensation. **If you do this, you must add an external NTC thermistor for the CCS811 to work properly.**\
**JP5** - Cut the traces on this jumper to disable the pull-up resistors for the I2C bus.

### Optional, off-board Sensors

There are connections for five off-board sensors as well: wind speed and direction, rainfall amount, temperature, and soil moisture.

#### Wind Speed and Direction

Coupled with SparkFun\'s weather station, the wind speed and direction can be measured by counting pulses per second and by measuring the resistance of a discrete step potentiometer. The pins for these two functions are connected to ESP32 Thing pins 14 (speed) and 35 (direction).

[![Wind sensor connector](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Wind.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Wind.png)

One tick per second corresponds to 1.492mph (2.40 kph) of wind speed. Obviously, the orientation of the weather meter determines what the resistance is for a given position. Sixteen positions are available and the voltage corresponding to each can be found on page 2 of the [weather meter\'s datasheet](https://www.sparkfun.com/datasheets/Sensors/Weather/Weather%20Sensor%20Assembly..pdf). Our example code provides you with a solid example on using the direction sensor, as well.

#### Soil Moisture

SparkFun\'s soil moisture sensor can be connected to the shield and monitored via analog voltage conversion. The sensor connects to pin 26 of the ESP32 Thing.

[![Soil moisture sensor connection](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_SoilMoisture.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_SoilMoisture.png)

#### Rainfall

The weather station will also provide you with a rainfall gauge. Much like the wind speed gauge, the rainfall gauge generates ticks to tally the amount of rain that has fallen. Count ticks to determine how much rain has fallen recently. Each tick represents 0.011\" (0.28mm) of rainfall. This sensor is connected to pin 25 of the ESP32.

[![Rainfall connector](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Rain.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_Rain.png)

#### External Temperature

If you so desire, you can connect one of our TMP36 external temperature sensors to the board at this location. Connecting it through a short wire will allow you to measure temperature outisde of the enclosure that the rest of the system is in. It measures with a 10mV/deg C output voltage. It is connected to pin 13 of the ESP32.

[![External temp connector](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_ExtTemp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_ExtTemp.png)

#### Any I2C Sensor

We\'ve provided a header which will allow you to connect any other I2C sensor or device you may think useful to the board. In fact, the pinout of this header is such that many SparkFun I2C boards can be directly attached without any wire order change at all!

[![I2C Header](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_AnyI2C.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/14153-04_AnyI2C.png)

## Hardware Assembly

As previously mentioned, it\'s a good idea to use headers (both male and female) to connect the two boards. Here we\'ll show you a bomb-proof method to solder down the headers and making sure that they\'re true and square so it\'s easier to connect (and disconnect) the two boards.

### Trim the Headers

When you purchase [male](https://www.sparkfun.com/products/116) and [female headers](https://www.sparkfun.com/products/115), they\'ll be too long for the ESP32 Thing and Environment Sensor Shield. You\'ll need to trim them down to an appropriate length. This means 20 pins each.

For the male headers, this is relatively easy\--they\'re designed to be trimmed or snapped to length. They come in 40-position pieces, so you\'ll only need to order one and then snap it in half.

[![Snipping the male headers to length](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-01.jpg)

For the female headers, however, things are a little trickier. In order to trim to the appropriate length, you\'ll lose one pin since these come in 40-position pieces as well. That means you\'ll need to order **two** of these in order to get two 20-position pieces, and you\'ll have two 19-position pieces left over. Bummer, I know.

The best way to trim the female header pieces is to count out 20 pins, pull the 21st pin, then use a side cutter to cut the gap between the 20th and 22nd pin.

[![Pulling the pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-02.jpg)

You must be careful when cutting the header to center your snip. An off center cut may result in the mechanical portion of the header escaping or losing some of its retention force.

[![Snipping the female headers to length](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-03.jpg)

Optionally, you may take a file, piece of sandpaper, or some other sanding/grinding tool to sand down the end of the header so that it\'s smoother. You can do both pieces at the same time by holding them together and rubbing the ends on the finishing surface.

### Install the Male Headers

We\'re going to install the male headers on the ESP32 Thing board first. We\'re going to do so \"right side up\", with the headers extending down from the side of the board with no components on it. This is easier than doing it the other way as the connectors on the component side of the board create a difficult gap when attempting this method from that side.

First, insert your male headers long-side-down into a breadboard, as shown below. You can see that we\'re inserting the headers into the second column in from the edge\--columns labeled as B and I on the breadboard we\'re using here.

[![Putting headers in breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-04.jpg)

Now, with the headers installed, you can easily drop the ESP32 Thing board into place on top of them.

[![ESP32 in place on headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-05.jpg)

Go ahead and solder all the pins to the ESP32 Thing at this time.

[![Soldering Male Headers on ESP32](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-06.jpg)

If you\'re new to soldering, check out our [through-hole soldering tutorial.](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) We\'ll wait here.

If you\'re new to soldering, you may want to solder just the first and last position on each side, then pull the board free of the breadboard, to avoid heat damage to your breadboard. You may find it easier to remove the board from the breadboard by inserting a flat-edge screwdriver under the end of the ESP32 and **gently** levering the board away from the breadboard by turning the handle of the screwdriver.

[![Screwdriver levering up board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-07.jpg)

### Install the Female Headers

Now we need to install the female headers onto the ESP32 Environment Sensor Shield. We\'ll do this using the pins we just soldered to the ESP32 Thing.

Take your female headers and place them on the male headers on the ESP32 Thing, as shown here.

[![Female headers on the Thing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-08.jpg)

Because we used the breadboard to hold our pins perfectly perpendicular to the ESP32 Thing board, the pins of the female headers should line up perfectly with the holes on the ESP32 Environment Sensor Shield.

[![Shield with Thing and header pins in place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-10.jpg)

**Be certain you\'ve placed the shield in the proper orientation! The component side of the shield should be facing the non-component side of the ESP32 Thing! Double check that the pin labels on the shield match those on the ESP32 Thing! Failure to observe these facing rules will make everything horrible and nothing will work!**

Flip the board over before soldering the female header pins.

[![ESP32 Environment Shield in place on headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/ESP32_shield_hookup_guide-09.jpg)

You may now solder the female header pins to the ESP32 Environment Sensor Shield just like the male header pins for the ESP32 Thing.

## Software

Besides the [ESP32 Arduino Core](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide?_ga=2.108672706.1377919567.1499096011-84620802.1496420289#installing-the-esp32-arduino-core), the ESP32 Environment Sensor Shield also requires the [CCS811](https://github.com/sparkfun/SparkFun_CCS811_Arduino_Library), [BME280](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library) and [APDS-9301](https://github.com/sparkfun/SparkFun_APDS9301_Library) Arduino libraries. Be sure to grab the libraries from each respective GitHub repositories, or you can download the files directly from the buttons below:

[SparkFun CCS811 Arduino Library](https://github.com/sparkfun/SparkFun_CCS811_Arduino_Library/archive/master.zip)

[SparkFun BME280 Arduino Library](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/master.zip)

[SparkFun APDS-9301 Arduino Library](https://github.com/sparkfun/SparkFun_APDS9301_Library/archive/master.zip)

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

If you have not already, make sure to [setup your own weather station](https://www.wunderground.com/weatherstation/hardwareandsoftware.asp) with Wunderground. You will need to fill out a form and pick a username & password in order to receive a station ID. Sensor data from the ESP32 Thing and the ESP32 Environment Sensor Shield can then be pushed to Wunderground\'s server.

Here we present some example code for the ESP32 Environment Sensor Shield. This code reads all of the sensors, prints the resulting data to the serial port once per second, then posts some of the more germane data to Weather Underground once per minute.

    language:c
    #include <SparkFunCCS811.h>
    #include "SparkFunBME280.h"
    #include "Wire.h"
    #include <Sparkfun_APDS9301_Library.h>
    #include <WiFi.h>

    BME280 bme;
    CCS811 ccs(0x5B);
    APDS9301 apds;

    // Variables for wifi server setup 
    const char* ssid     = "your_ssid_here";
    const char* password = "password"; 
    String ID = "wunderground_station_id";
    String key = "wunderground_station_key";  
    WiFiClient client;
    const int httpPort = 80;
    const char* host = "weatherstation.wunderground.com";

    // Variables and constants used in calculating the windspeed.
    volatile unsigned long timeSinceLastTick = 0;
    volatile unsigned long lastTick = 0;

    // Variables and constants used in tracking rainfall
    #define S_IN_DAY   86400
    #define S_IN_HR     3600
    #define NO_RAIN_SAMPLES 2000
    volatile long rainTickList[NO_RAIN_SAMPLES];
    volatile int rainTickIndex = 0;
    volatile int rainTicks = 0;
    int rainLastDay = 0;
    int rainLastHour = 0;
    int rainLastHourStart = 0;
    int rainLastDayStart = 0;
    long secsClock = 0;

    String windDir = "";
    float windSpeed = 0.0;

    // Pin assignment definitions
    #define WIND_SPD_PIN 14
    #define RAIN_PIN     25
    #define WIND_DIR_PIN 35
    #define AIR_RST      4
    #define AIR_WAKE     15
    #define DONE_LED     5

    void setup() 
    
      Serial.println("");
      Serial.println("WiFi connected");
      Serial.println("IP address: ");
      Serial.println(WiFi.localIP());

      // Visible WiFi connected signal for when serial isn't connected
      digitalWrite(DONE_LED, HIGH);
    }

    void loop() 
    

      // This is a once-per-second timer that calculates and prints off various
      //  values from the sensors attached to the system.
      if (millis() - outLoopTimer >= 2000)
      

          // Repeat the process, this time over days.
          i = rainTickIndex-1;
          while ((rainTickList[i] >= secsClock - S_IN_DAY) && rainTickList[i] != 0)
          
          rainLastDayStart = i;
        }
      }

      // Update wunderground once every sixty seconds.
      if (millis() - wundergroundUpdateTimer >= 60000)
      
        else
        

        // Issue the GET command to Weather Underground to post the data we've 
        //  collected.
        client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                     "Host: " + host + "\r\n" +
                     "Connection: close\r\n\r\n");

        // Give Weather Underground five seconds to reply.
        unsigned long timeout = millis();
        while (client.available() == 0) 
        
        }

        // Read the response from Weather Underground and print it to the console.
        while(client.available()) 
        
      }
    }

    // Keep track of when the last tick came in on the wind sensor.
    void windTick(void)
    

    // Capture timestamp of when the rain sensor got tripped.
    void rainTick(void)
    

    // For the purposes of this calculation, 0deg is when the wind vane
    //  is pointed at the anemometer. The angle increases in a clockwise
    //  manner from there.
    void windDirCalc(int vin)
    

**Note:** When connecting to a WiFi network and the Wunderground server, make sure to modify the variables `ssid`, `password`, `ID`, and `key`.

#### Expected Output

Here is a picture of what you should expect upon starting up your ESP32 and letting it connect to WiFi:

[![Initial startup picture](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/output.png)

The first few lines are just diagnostics from the ESP32, and will be present at boot time regardless of the application being run. Immediately below the line \"Connecting to sparkfun-guest\" you see a series of dots. One dot appears every half second while the connection is pending, so you can see from this example that it took approximately 3 seconds for the WiFi to come online. After that, the various environmental parameters we\'re looking at are printed out, along with a timestamp in seconds since the platform was booted.

Once a minute, the stream of data from the sensors is interrupted by a connection to the weatherunderground.com servers. Here\'s what that output looks like:

[![Connecting to wunderground servers](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/output_connect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/9/output_connect.png)

There are two useful pieces of data here. The first, where it says \"Connection succeeded\", shows that a successful connection has been made to the Weather Underground server. If your internet connection is down, this will fail.

The second is the one lone line that says \"success\". This is the response from the server after your attempt to post data to it. If this fails, it means that you connected to the server, but the string you formatted to send to the server isn\'t formatted properly. This shouldn\'t be a problem unless you change the example code.