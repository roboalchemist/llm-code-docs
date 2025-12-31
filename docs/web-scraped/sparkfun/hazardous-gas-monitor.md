# Source: https://learn.sparkfun.com/tutorials/hazardous-gas-monitor

## Introduction

Unfortunately Phant, our data-streaming service, is no longer in service. The system has reached capacity and, like a less-adventurous Cassini, has plunged conclusively into a fiery and permanent retirement. There are several other maker-friendly, data-streaming services and/or IoT platforms available as alternatives. The three we recommend are Blynk, ThingSpeak, and Cayenne. You can read our [blog post on the topic](https://www.sparkfun.com/news/2413) for an overview and helpful links for each platform. The code in this tutorial will need to be adjusted to work with the other data streams.\
\
As an example, try looking at the [Photon Remote Water Level Sensor Tutorial](https://learn.sparkfun.com/tutorials/photon-remote-water-level-sensor) which uses ThingSpeak.

Build a portable gas monitor to check for dangerous levels of hazardous gases in your home, community, or on the go and prevent your friends from lighting a cigarette during a gasoline fight.\*

\*\*Please note that this is solely a movie reference \-- gasoline fights should probably be avoided in real life.\*

[![Hazardous Gas Monitor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/FinalMonitor_Outside1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/FinalMonitor_Outside1.jpg)

This tutorial shows you how to build a web-connected \"canary\" monitor for three hazardous gases: [Liquid Propane Gas (\"LPG\")](https://www.sparkfun.com/products/9405), [Methane (aka natural gas)](https://www.sparkfun.com/products/9404), and [Carbon Monoxide (\"CO\")](https://www.sparkfun.com/products/9403). Using the [Particle Photon microcontroller](https://www.sparkfun.com/products/13774), the sensor readings are converted into parts-per-million (\"PPM\") and uploaded to the [data.sparkfun.com web service](http://data.sparkfun.com).

Check out the video below to see the Hazardous Gas Monitor in action:

### Helpful Background Info

1.  [How to set up the Particle Photon.](https://docs.particle.io/guide/getting-started/intro/core/)
2.  [Pushing data to the data.sparkfun.com web server.](https://learn.sparkfun.com/tutorials/pushing-data-to-datasparkfuncom/all)
3.  New to relays? [Check out this a handy reference.](http://www.learningaboutelectronics.com/Articles/How-to-connect-a-single-pole-double-throw-relay-in-a-circuit)
4.  [Here\'s a helpful overview on the N-Channel MOSFET.](http://bildr.org/2012/03/rfp30n06le-arduino/)
5.  For powering the Photon, [here\'s a thorough guide on the Photon Battery Shield.](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide?_ga=1.74236561.284649662.1439527581)
6.  Highly recommended to peruse the datasheets for the three gas sensors.
    1.  [LPG sensor datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Biometric/MQ-6%20Ver1.3%20-%20Manual.pdf)
    2.  [Methane sensor datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Biometric/MQ-4%20Ver1.3%20-%20Manual.pdf)
    3.  [CO sensor datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Biometric/MQ-7%20Ver1.3%20-%20Manual.pdf)

#### Choosing a Battery

The gas sensors used in this project require a fair amount of current, about 0.17 mA each at 5V. To make the system portable, we\'ll need a high capacity battery. One easy, and affordable, option is to use four (rechargeable) AA batteries in series. These batteries will last about 4 hours.

Another option is to use a lithium ion battery (\"LIB\"). LIBs have a higher capacity than AAs, but typically run at a lower voltage. If you go with this option, you may need to include a correction factor when you calculate the sensor value or boost the battery voltage with a transistor or other component.

Here\'s a table that shows the approximate lifetime of a few different battery options.

[![Table2_BatteryCap3Sensors](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/Table2_BatteryCap3Sensors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/Table2_BatteryCap3Sensors.jpg)

If all of this sounds confusing, [here\'s a more thorough tutorial.](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### Materials

To follow along with this tutorial, you\'ll need the following:

[![materials](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/SensorMaterials_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/SensorMaterials_1.jpg)

#### Microcontroller and Accessory Components

- [Particle Photon microcontroller](https://www.sparkfun.com/products/13774)
- [SparkFun Photon Battery Shield](https://www.sparkfun.com/products/13626)
- One 2000 mAh [Polymer Lithium Ion Battery](https://www.sparkfun.com/products/8483)
- [Surface Mount DC Barrel Jack](https://www.sparkfun.com/products/12748)
- [Barrel jack to USB power supply cable](https://www.sparkfun.com/products/8639)
- [One (1) Lamp Switch](https://www.sparkfun.com/products/11477)
- Optional: Male-to-Female JST connector cable

#### Gas Sensor Circuit

- [One (1) Project Case](https://www.sparkfun.com/products/11366)
- One (1) [4 AA battery case](https://www.sparkfun.com/products/552)
- Four (4) AA Rechargeable Batteries
- [One (1) Toggle Switch (SPST switch)](https://www.sparkfun.com/products/9276)
- [Piezo Buzzer](https://www.sparkfun.com/products/7950)
- [Three (3) Red LEDs](https://www.sparkfun.com/products/10632)
- Three (3) 10 kΩ resistors
- [One (1) PCB](https://www.sparkfun.com/products/12070)
- [22 Gauge stranded wire](https://www.sparkfun.com/products/11375)
- Optional: Electrical connectors (3-5)

##### LPG (MQ6) Gas Sensor

- [MQ6 LPG Gas Sensor](https://www.sparkfun.com/products/9405)
- [Gas Sensor Breakout Board](https://www.sparkfun.com/products/8891)
- One (1) 4.7 kΩ resistor
- One (1) [5V Voltage Regulator](https://www.sparkfun.com/products/107)

##### Methane (MQ4) Gas Sensor

- [MQ4 Methane Gas Sensor](https://www.sparkfun.com/products/9404)
- [Gas Sensor Breakout Board](https://www.sparkfun.com/products/8891)
- One (1) 4.7 kΩ resistor
- One (1) [5V Voltage Regulator](https://www.sparkfun.com/products/107)

##### Carbon Monoxide (MQ7) Gas Sensor

- [MQ7 CO Gas Sensor](https://www.sparkfun.com/products/9403)
- [Gas Sensor Breakout Board](https://www.sparkfun.com/products/8891)
- One (1) 4.7 kΩ resistor
- One (1) [5V Voltage Regulator](https://www.sparkfun.com/products/107)
- One (1) [5V SPDT Relay](https://www.sparkfun.com/products/100)
- One (1) [1N4148 Diode](https://www.sparkfun.com/products/8588)
- One (1) [N-Channel MOSFET](https://www.sparkfun.com/products/10213)
- One (1) [10 kΩ potentiometer](https://www.sparkfun.com/products/9806)
- One (1) 10 kΩ resistor

### Tools

- Soldering Iron
- Wire cutters/strippers
- Drill
- Screwdriver
- Epoxy (or hot glue)

## Build It

Below is the Fritzing diagram for the Hazardous Gas Monitor circuit. Since we are using the Photon Battery Shield breakout, make sure to connect the wires to the shield\'s pinouts instead of directly to the Particle Photon\'s header pins shown in the image. Additionally, the LiPo battery will be connected to the Photon battery Shield\'s JST connector **underneath** the Particle Photon.

[![Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/HazardousGasMonitor_Corrected.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/HazardousGasMonitor_Corrected.png)

*Click the image for a closer look.*

**Note:** The LiPo Battery in the Fritzing diagram is connected to the Particle Photon\'s VBAT pin for illustration. It should be connected to the Photon Battery Shield\'s JST connector. After making the connections on the Particle Photon\'s header pins and inserting the LiPo battery into the JST connector, you will stack the Particle Photon on the shield.

1.  Solder gas sensor breakout boards to gas sensors. Orientation doesn\'t matter, just be sure that the silkscreen (aka labels) are facing down so that you can read them (had to learn that one the hard way..). Solder wires to the gas sensor breakout board.

    [![breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/SensorBreadkoutCLoseUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/SensorBreadkoutCLoseUp.jpg)

2.  Solder three voltage regulators to the PCB board. For each regulator, connect positive battery output to the regulator input, and connect middle voltage regulator pin to ground.

    [![VREG](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/PCBVoltReg1and2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/PCBVoltReg1and2.jpg)

3.  Connect the LPG (MQ6) and Methane (MQ4) sensors.

    [![MQ6, MQ4](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/PCB_MQ6_MQ4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/PCB_MQ6_MQ4.jpg)

    For each sensor:

    1.  Connect H1 and A1 to the output of one of the voltage regulators (recommended to use an electrical connector).
    2.  Connect GND to ground.
    3.  Connect B1 to Photon analog pin (LPG goes to A0, Methane to A1)
    4.  Connect a 4.7 kΩ resistor from B1 to ground.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/PCBFull_MQ6_MQ4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/PCBFull_MQ6_MQ4.jpg)

4.  Connect the CO (MQ7) gas sensor.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/MQ7_Materials1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/MQ7_Materials1.jpg)

    *Aside: The MQ7 sensor requires cycling the heater voltage (H1) between 1.5V (for 90s) and 5V (for 60s). One way to do this is to use a relay triggered by the Photon (with the aid of a MOSFET and potentiometer) \-- when the relay is not powered, the voltage across H1 is 5V, and when the relay is powered the voltage across H1 is \~ 1.5V.*

    1.  Connect GND to ground.
    2.  Connect B1 to Photon analog pin (A2). Connect 4.7 kΩ resistor from B1 to ground.
    3.  Connect A1 to third voltage regulator output (5V source).
    4.  Connect Photon 3.3V pin to positive relay input.
    5.  Connect Photon Digital Pin D7 to left MOSFET pin, and a 10 kΩ resistor to ground.
    6.  Connect middle MOSFET pin to relay ground pin. Connect right MOSFET pin to ground.
    7.  Connect relay Normally Open (\"NO\") pin to A1, and the Normally Closed (\"NC\") pin to middle potentiometer pin.
    8.  Connect right potentiometer pin to ground, and left pin to A1.
    9.  Connect relay Common (\"COM\") pin to H1.
    10. Adjust potentiometer resistance until it changes the relay output to \~ 1.5V when the relay receives power.

5.  Connect an LED and 10 kΩ resistor to each of the Photon digital pins D0, D1, and D2. Connect buzzer to Photon digital pin D4.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/PCB_LEDs1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/PCB_LEDs1.jpg)

6.  Connect toggle switch between battery pack and PCB board power. *Recommended to include an electrical connector for the battery pack to make it easier to switch out batteries.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/SwitchWires1_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/SwitchWires1_1.jpg)

7.  Solder wires to Photon Battery Shield breakout.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/PhotonBatteryShield_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/PhotonBatteryShield_Wires.jpg)

8.  Connect lamp switch between LIB and Photon battery shield \-- recommended to use an extra JST cable for this to keep the LIB battery cable in tact (and make it easier to install the lamp switch).

9.  Build a case for the electronics!

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/Case_Marked1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/Case_Marked1.jpg)

    1.  Drill hole for toggle switch on case lid.

    2.  Drill 3 holes in the case lid for the LED lights to shine through, and 3 holes for the gas sensors to have air contact. Adhere components on the inside of the lid.

        [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/Case_LEDTest4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/Case_LEDTest4.jpg)

    3.  Drill hole in the side of the case for barrel jack USB cord to connect to the Photon Battery Shield.

        [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/Case_BarrelJackCable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/Case_BarrelJackCable.jpg)

    4.  Drill two small holes on the side of the case for the lamp switch cable. Adhere lamp switch to side of case.

    5.  Label the LEDs with its corresponding gas sensor on the outside of the case.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/FinalSystem_SensorCloseUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/FinalSystem_SensorCloseUp.jpg)

10. Check electrical connections and, if everything is good to go, coat electrical connections in epoxy or hot glue.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/FinalSystem2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/FinalSystem2.jpg)

## Calculate Gas Sensor PPM

Each of the gas sensors outputs an analog value from 0 to 4095. To convert this value into voltage, use the following equation:

    Sensor Voltage = AnalogReading * 3.3V / 4095

Once you have the sensor voltage, you can convert that into a parts per million (\"PPM\") reading using the sensitivity calibration curve on page 5 of the gas sensor datasheets. To do this, recreate the sensitivity curve by picking data points from the graph or using a graphical analysis software like [Engauge Digitizer](http://digitizer.sourceforge.net/).

Plot PPM on the y-axis and V_RL on the x-axis, where V_RL is the sensor voltage. There is a lot of room for error with this method, but it will give us enough accuracy to identify dangerous levels of hazardous gases. Estimated error bars are around 20 PPM for the LPG and Methane sensors, and about 5 PPM for the CO sensor.

[![MQ7_SensitivityPlot_CurvePoints](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/MQ7_SensitivityPlot_CurvePoints.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/MQ7_SensitivityPlot_CurvePoints.jpg)

Next, find an approximate equation for the PPM vs. V_RL curve. I used an exponential fit (e.g. y = e\^x) and got the following equations:

    LPG sensor: PPM = 26.572*e^(1.2894*V_RL)

    Methane sensor: PPM = 10.938*e(1.7742*V_RL)

    CO sensor: PPM = 3.027*e^(1.0698*V_RL)

## Program It

First, set up a data stream on the [data.sparkfun.com service](http://data.sparkfun.com). Next, write a program to read in the analog value of each gas sensor, convert it to PPM, and check it against known safe thresholds. Based on OSHA safety standards, the thresholds for the three gases are as follows:

- LPG: 1,000 PPM
- Methane: 1,000 PPM
- CO: 50 PPM

If you want to get up and running quickly, or are new to programming, feel free to grab the code from below, or you can get the most up to date files from the GitHub repository. Use it as-is or modify to suit your particular needs.

[Hazardous Gas Monitor GitHub Repository](https://github.com/jenfoxbot/HazardousGasMonitor)

    language:c
    // This #include statement was automatically added by the Particle IDE.
    //This library is used to push data to the data.sparkfun.com server.
    #include "SparkFunPhant/SparkFunPhant.h"
    #include "math.h" 

    //This code was written by Jennifer Fox <jenfoxbot@gmail.com>
    /*
     * ----------------------------------------------------------------------------
     * "THE Coffee-WARE LICENSE" (Revision 42):
     * <jenfoxbot@gmail.com>  wrote this file.  As long as you retain this notice you
     * can do whatever you want with this stuff. If we meet some day, and you think
     * this stuff is worth it, you can buy me a coffee in return.
     * ----------------------------------------------------------------------------
     */

    //Variables to push data to data.sparkfun.com host -- Change publicKey[] and privateKey[]
    const char server[] = "data.sparkfun.com"; // Phant destination server
    const char publicKey[] = "INSERT_PUBLIC_KEY_HERE"; // Phant public key
    const char privateKey[] = "INSERT_PRIVATE_KEY_HERE"; // Phant private key

    Phant phant(server, publicKey, privateKey); // Create a Phant object

    const unsigned long postingRate = 20000; //Post rate to data.sparkfun.com (time in milliseconds)
    unsigned long lastPost = millis(); //Keeps track of posting rate

    //Define analog pins on Photon to use for sensors
    const int LPG = A0;
    const int NG = A1;
    const int CO = A2;

    //Define digital pins on Photon to use for LEDs,  buzzer, and MQ7 (CO sensor) heater
    const int LPGled = D0;
    const int NGled = D1;
    const int COled = D2;
    const int buzzer = D3;
    const int CORelayPin = D6;
    const int COVoltPin = D7;

    //Set up raw signal and PPM variables for each gas sensor
    int LPGRaw;
    int NGRaw;
    int CORaw;

    int LPGppm;
    int NGppm;
    int COppm;

    //Set safety threshold levels for each  hazardous gas
    const int  LPGthresh = 1000;
    const int NGthresh = 1000;
    const int COthresh = 50;

    //Set variables for CO sensor (MQ7) voltage cycle
    unsigned long startMillis;        
    unsigned long switchTimeMillis;
    const int CO_5V_Interval = 60000; //60s for 5V interval
    const int CO_1_5V_Interval = 90000; //90s for 1.5V interval
    bool heaterInHighPhase;

    void setup() 

    void loop() 
        }
        else 
        }

        //Read in analog value from each gas sensor -- use function defined below to measure CO sensor at end of voltage cycle
        LPGRaw = analogRead(LPG); 
        NGRaw = analogRead(NG);
        CORaw = measureCOSensor();

        //Caclulate the PPM of each gas sensor using the funtions defined below            
        LPGppm = LPG_ppm(LPGRaw); 
        NGppm = NG_ppm(NGRaw); 
        COppm = CO_ppm(CORaw);

        //Serial monitor print for debugging and checking data 
        Serial.println(NGRaw);
        Serial.println(NGppm);
        delay(1000);

        //Check gas sensor measurements against safety thresholds
        checkThreshold(LPGppm, NGppm, COppm);

        //Wait to post until ~ 20s has lapsed
        if (lastPost + postingRate < millis()) 

    }

    //Functions to calculate PPM from Photon analog reading
    //Each equation is determined by visually picking points, plotting PPM v. V_RL, then fitting a trendline to the curve (exponential)
    //Calculate LPG PPM
    int LPG_ppm(double rawValue)

    //Calculate NG PPM
    int NG_ppm(double rawValue)

    //Calculate CO PPM
    int CO_ppm(double rawValue)

    //Function to check PPM reading with maximum safe PPM threshold
    //Include a margin of error (currently 10%)
    void checkThreshold(int lpgppm, int ngppm, int coppm) 
        else

        if (ngppm >= NGthresh*0.9) 
        else

        if (coppm >= COthresh*0.9) 
          else

        if(led1 | led2 | led3)

        else

    }

    //Functions to switch heater voltage on MQ7 (CO) sensor
    void turnHeaterHigh()

    void turnHeaterLow()

    //Function to read CO sensor voltage (just before switching to 1.5V)
    int measureCOSensor()

    //Function to post data to data.sparkfun.com host
    //Many thanks to Jim Lindblom <jim@sparkfun.com> for the sample code and Phant library.
    int postToPhant(int lpg, int ng, int co)
            // Search the response string for "200 OK", if that's found the post
            // succeeded.
            if (strstr(response, "200 OK"))
            
            else if (strstr(response, "400 Bad Request"))
            
            else
            
        }
        else
        
        client.stop();  // Close the connection to server.
        return retVal;  // Return error (or success) code.
    }

### Change the following in the code:

1.  Copy and paste your data stream public key to the array called `publicKey[]`.

    `const char publicKey[] = "INSERT_PUBLIC_KEY_HERE";`

2.Copy and paste your data stream private key to the array called `privateKey[]`.

    `const char privateKey[] = "INSERT_PRIVATE_KEY_HERE";`

To monitor the Photon output, use the Particle driver downloaded as described in the [\"Connecting Your Device\" Photon tutorial](https://docs.particle.io/guide/getting-started/connect/photon/). Once this is installed, in the command prompt, type `particle serial monitor`. This is super helpful for debugging and checking that the Photon is posting data to the web.

## Be a Citizen Scientist

[![FinalMonitor_Outside](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/1/FinalMonitor_Outside4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/1/FinalMonitor_Outside4.jpg)

Now we get to test and employ our gas monitor! Turn the batteries for the gas sensors on using the toggle switch, wait about 3 - 5 minutes, then turn the Photon on with the lamp switch (the gas sensor heater coils take some time to heat up). Check that the Photon is connected to WiFi (on-board LED will slowly pulse light blue) and is uploading data to the server. Also check that the gas sensor readings increase when in proximity to hazardous gases \-- one easy, and safe, way is to hold a lighter and/or a match close to the sensors.

Once up and running, use the sensor to monitor for dangerous gas leaks around your home, school, workplace, neighborhood, etc. You can install the sensor in one location permanently, or use it to check gas levels in different locations (e.g. SoCal..).

### Educator Extension!

This project is a perfect excuse for a hands-on chemistry lesson! Use the monitor to learn the fundamentals of various gases \-- what kinds of gases are in our environment, how are different gases produced, and what makes some of them hazardous or dangerous.

Study the local environment and use a lil\' math to record and plot LPG, Methane, and CO in specific locations over time to see how the levels change. Use the data to help determine what causes changes in the gas levels and where/when gas concentrations are the highest.