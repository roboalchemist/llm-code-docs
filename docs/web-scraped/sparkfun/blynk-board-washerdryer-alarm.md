# Source: https://learn.sparkfun.com/tutorials/blynk-board-washerdryer-alarm

## Introduction

We created the [SparkFun Blynk Board](https://www.sparkfun.com/products/13794) to solve problems. Big problems \-- like [keeping plants healthy](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-12-botanitweeting) \-- and problems trending closer to the \"first-world\" end of the spectrum \-- like a phone-alerting laundry monitor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/photo-project-2-1000.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/photo-project-2-1000.JPG)

This tutorial demonstrates how to pair the Blynk Board with an [MMA8452Q Accelerometer Breakout](https://www.sparkfun.com/products/12756) to create a shake-sensing laundry monitor. Once the laundry is done, the electronics will communicate with the [Blynk app](http://blynk.cc) \-- over Wi-Fi \-- to send your phone a **push notification**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-notification.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-notification.PNG)

Together, the Blynk Board and app will allow you to power through laundry day as quickly and efficiently as possible!

### Required Materials

The wishlist below includes all of the electronics and components you\'ll need to follow along with this tutorial:

In addition to those breakout boards and cables, this project also requires a bit of **soldering**. A simple [soldering iron](https://www.sparkfun.com/products/9507), some [solder](https://www.sparkfun.com/products/9163), [wire strippers](https://www.sparkfun.com/products/12630), and a [flush cutter](https://www.sparkfun.com/products/11952) should be all you really need.

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Flush Cutters - Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/2/2/11952-Hakko-Flush-Cutters-feature.jpg)](https://www.sparkfun.com/flush-cutters-hakko.html)

### [Flush Cutters - Hakko](https://www.sparkfun.com/flush-cutters-hakko.html) 

[ TOL-11952 ]

Tool for a flush cut.

[ [\$10.50] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

### Suggested Reading

To follow along with this tutorial, you\'ll need to program your Blynk Board with new firmware. Hopefully, by this point, you\'ve already exhausted the [Project Guide](https://learn.sparkfun.com/tutorials/blynk-board-project-guide) and set your computer up to [program the Blynk Board using Arduino](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide). If not, check out either \-- or both \-- of those tutorials first.

[Blynk Board Project Guide](https://learn.sparkfun.com/tutorials/blynk-board-project-guide) [Blynk Board Arduino Development Guide](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide)

This project builds on a handful of electronics concepts. If your unfamiliar with any of the subjects below, consider reading through that tutorial first.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/mma8452q-accelerometer-breakout-hookup-guide)

### MMA8452Q Accelerometer Breakout Hookup Guide 

How to get started using the MMA8452Q 3-axis accelerometer \-- a solid, digital, easy-to-use acceleration sensor.

## Hardware Hookup

The MMA8452Q is controlled and monitored via an [I^2^C interface](https://learn.sparkfun.com/tutorials/i2c) interface \-- a two-wire, serial interface popular among embedded electronics like this. On the Blynk Board, that interface is broken out to the 4-pin, white JST connector adjacent to the USB port.

[![I2C connector location](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/hardware-i2c-highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/hardware-i2c-highlighted.jpg)

Our [4-Pin JST wire assembly](https://www.sparkfun.com/products/9916) mates perfectly with that connector, but tying the other end to an accelerometer will require some soldering.

If you've never soldered before, don't run off just yet! This is relatively simple soldering, and is a great introduction to the skill. Check out our [How to Solder - Through Hole tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) to learn how to get started.

### Solder the JST Cable to the Accelerometer

Plugged into the Blynk Board, the colors of the 4-wire JST assembly match up closely with what you\'d expect. Black is ground, red is power (3.3V), yellow is SCL, and blue is SDA. That\'s exactly how you\'ll need to solder the accelerometer on the other end.

[![MMA8452Q accelerometer soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/hardware-mma8452q-soldered_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/hardware-mma8452q-soldered_1.jpg)

Once the JST cable is soldered into the accelerometer, simply plug the connector into the mating end of the Blynk Board.

[![Blynk Board and accelerometer together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/hardware-plugged.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/hardware-plugged.jpg)

### Optional: Add a Battery

This project can take advantage of the Blynk Board\'s integrated **LiPo battery charger**. If you don\'t have an empty wall outlet nearby, you can simply plug the battery in and set the assembly on top of your washer/dryer.

[![Battery plugged in to circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/hardware-plugged-battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/hardware-plugged-battery.jpg)

Any of our single-cell lithium-polymer batteries should work. If you\'re looking for suggestions, we find the [400mAh](https://www.sparkfun.com/products/10718) and [850mAh](https://www.sparkfun.com/products/341) LiPo\'s to be a nice compromise between capacity and size.

To charge the battery, simply connect a USB cable (connected on the other end to either a computer or [wall adapter](https://www.sparkfun.com/products/11456)) to the Blynk Board.

## Blynk Setup

To enable phone notifications -- and to configure the Blynk Board laundry monitor on-the-fly -- we\'re using the Blynk app. Blynk is available for both iOS and Android devices. Click one of the links below, if you don\'t have the app yet.

[![AS_link](https://cdn.sparkfun.com/assets/learn_tutorials/4/9/4/AS_link.png)](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8)

[![GP_link](https://cdn.sparkfun.com/assets/learn_tutorials/4/9/4/GP_link.png)](https://play.google.com/store/apps/details?id=cc.blynk)

On your phone, create a new Blynk project (or use a previously-created project if you prefer). Then drag in the following widgets:

#### Push Notifications

The most critical widget of the bunch! There\'s not a whole lot to configure here. The \"Send even if app is in background\" option is useful, but may end up draining more of your phone\'s battery.

[![Notification settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-notify.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-notify.PNG)

#### Button \| \"Enable Push\" \| V0

This button will allow you to easily enable or disable push notifications \-- just in case you don\'t always want the intrusive alerts.

[![Button settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-button.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-button.PNG)

Make sure the button is set to **switch** mode.

#### Slider \| \"Shake Threshold\" \| V1

The code adds up sensed acceleration in all three dimensions, then compares that sum against a previous measurement. This threshold value sets the minimum difference between those two measurements that will trigger a \"shake\".

[![Threshold slider settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-threshold-slider.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-threshold-slider.PNG)

Depending on how much your washer or dryer shakes, a value between 10 and 100 should work. You can monitor the gauge widget to fine-tune this value.

#### Slider \| \"Start Time (ms)\" \| V2

This slider configures the amount of time shaking must be sensed before the Blynk Board assumes the laundry is running. This helps filter out steps, a door closing, earth tremors, etc.

[![Start time slider settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/scree-start-slider.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/scree-start-slider.PNG)

You may need to tweak this value, but 500 (milliseconds) is usually a good default.

#### Slider \| \"Stop Time (s)\" \| V3

This slider sets the number of seconds from when shaking stops to when the notification is sent. Some washers or dryers will try to fake you out, by pausing their cycle for a few seconds before picking back up.

[![Stop time slider settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-stop-slider.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-stop-slider.PNG)

A value between 10 and 60 seconds should work \-- though you may have to extend it even more depending on your appliance. Just know that the higher this value is, the slower you\'ll be to your laundry when it\'s done.

#### LCD \| \"Laundry Status\" \| V4 (Advanced)

Bits of data like the state of your washer/dryer or how long it\'s been running/stopped are routed to the LCD.

[![LCD Slider settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-lcd.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-lcd.PNG)

A quick glance at this, while the project is running, may give you an idea of how much time is left on your wash.

#### Gauge \| \"Shakiness\" \| V5

The raw \"shakiness\" calculation is supplied to this virtual variable a few times per second.

[![Shakiness gauge settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-gauge-2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-gauge-2.PNG)

This widget is helpful in tweaking the threshold (V1) slider. Or for verifying that the machine is still shaking.

------------------------------------------------------------------------

Arrange the widgets however you\'d like, customize the colors, have fun with it! Here\'s an example set up:

[![Example project layout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-project-stopped-2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-project-stopped-2.PNG)

## Program the Blynk Board

If you haven't set your computer up to program the Blynk Board using Arduino yet, read through our [Blynk Board Arduino Development Guide](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide) first. Following that, you should have the Blynk Board hardware definitions and most of the libraries you'll need added to your Arduino IDE.

[Set your Arduino IDE up for Blynk Board development!](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide)

### Install the SparkFun MMA8452Q Arduino Library

The latest version of our MMA8452Q Arduino library can be downloaded from the [SparkFun_MMA8452Q_Arduino_Library GitHub repository](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library) (click the \"Download ZIP\" button there). Or you can skip the detour, by clicking the button below.

[Download the MMA8452Q Arduino Library](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library/archive/master.zip)

The library will be downloaded as a ZIP file. To install it in Arduino, navigate to **Sketch** \> **Include Library** \> **Add .ZIP Library\...**. Then select the MMA8452Q ZIP folder you just downloaded.

[![Add library from zip folder](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/add-zip-library.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/add-zip-library.png)

### Copy/Paste the Code

Our \"Blynk Board Laundry Monitor\" source code is also available [on GitHub](https://github.com/sparkfun/Blynk_Board_ESP8266/blob/master/Firmware/Examples/Laundry_Monitor/Laundry_Monitor.ino). Download it from there, or copy/paste from the box below:

    language:c
    #include <ESP8266WiFi.h>
    #include <BlynkSimpleEsp8266.h>
    #include <Wire.h> // Must include Wire library for I2C
    #include <SparkFun_MMA8452Q.h> // Includes the SFE_MMA8452Q library
    #include <Adafruit_NeoPixel.h>

    //////////
    // WiFi //
    ////////// // Enter your WiFi credentials here:
    const char WiFiSSID[] = "WiFiNetworkName";
    const char WiFiPSWD[] = "WiFiPassword";

    ///////////
    // Blynk //
    ///////////             // Your Blynk auth token here
    const char BlynkAuth[] = "0a1b2c3d4e5f";
    bool notifyFlag = false;
    #define VIRTUAL_ENABLE_PUSH     V0
    #define VIRTUAL_SHAKE_THRESHOLD V1
    #define VIRTUAL_START_TIME      V2
    #define VIRTUAL_STOP_TIME       V3
    #define VIRTUAL_LCD             V4
    #define VIRTUAL_SHAKE_VALUE     V5
    WidgetLCD lcd(VIRTUAL_LCD);
    bool pushEnabled = false;
    void printLaundryTime(void);

    /////////////////////
    // Shake Detection //
    /////////////////////
    unsigned int shakeThreshold = 50;
    unsigned int shakeStartTimeHysteresis = 1000;
    unsigned int shakeStopTimeHysteresis = 10;
    unsigned long shakeStateChangeTime = 0;
    unsigned long shakeStartTime = 0;
    bool loadTimer = true;

    enum  shakingState = NO_SHAKING;

    // Possible return values from the shake sensor
    enum sensorShakeReturn ;
    sensorShakeReturn checkShake(void);
    void shakeLoop(void);

    ////////////////////////////
    // MMA8452Q Accelerometer //
    ////////////////////////////
    MMA8452Q accel;
    int16_t lastX, lastY, lastZ;
    void initAccel(void);

    //////////////////////////
    // Hardware Definitions //
    //////////////////////////
    const int LED_PIN = 5;
    const int RGB_PIN = 4;
    Adafruit_NeoPixel rgb = Adafruit_NeoPixel(1, RGB_PIN, NEO_GRB + NEO_KHZ800);
    void setLED(uint8_t red, uint8_t green, uint8_t blue);

    void setup()
    

    void loop()
    

    bool firstConnect = true;
    BLYNK_CONNECTED()
    
    }

    BLYNK_WRITE(VIRTUAL_ENABLE_PUSH)
    
      else
      
    }

    BLYNK_WRITE(VIRTUAL_SHAKE_THRESHOLD)
    

    BLYNK_WRITE(VIRTUAL_START_TIME)
    

    BLYNK_WRITE(VIRTUAL_STOP_TIME)
    

    void printLaundryTime(void)
    

      if (shakingState == PRE_SHAKING)
        lcd.print(0, 0, "Laundry starting");
      else if (shakingState == SHAKING)
        lcd.print(0, 0, "Laundry running ");
      else if (shakingState == NO_SHAKING)
        lcd.print(0, 0, "Laundry stopping");
      else if (shakingState == NO_SHAKING_LONG)
        lcd.print(0, 0, "Laundry done!   ");
      lcd.print(0, 1, runTimeString);
    }

    void shakeLoop(void)
    
          printLaundryTime();
          break;
        case PRE_SHAKING: // If we're pre-hysteresis shaking
          if (millis() - shakeStateChangeTime >= shakeStartTimeHysteresis)
          
          break;
        case SHAKING: // If we're already shaking
          printLaundryTime(); // Update laundry timer
          break; // Do nothing
        case POST_SHAKING: // If we didn't stop shaking before hysteresis
          shakingState = SHAKING; // Go back to shaking
          break;
        }
      }
      else if (sensorState == SENSOR_NOT_SHAKING) // If the sensor is not shaking
      
          }
          break;
        case PRE_SHAKING: // If we're pre-hysteresis shaking
          shakingState = NO_SHAKING; // Go back to no shaking
          setLED(0, 32, 0);
          break;
        case SHAKING: // If we're already shaking
          shakingState = POST_SHAKING; // Go to hysteresis cooldown
          shakeStateChangeTime = millis();
          break; // Do nothing
        case POST_SHAKING: // If we're in the shake cooldown state
          if (millis() - shakeStateChangeTime >= shakeStartTimeHysteresis)
          
          break;      
        }
      }
    }

    sensorShakeReturn checkShake(void)
    
      else // If sensore didn't have new data
      
      // If shake value exceeded threshold
      if (shake >= shakeThreshold)
        return SENSOR_SHAKING; // Return "shaking"
      else 
        return SENSOR_NOT_SHAKING; // Or return "not shaking"
    }

    void initAccel(void)
    

    void setLED(uint8_t red, uint8_t green, uint8_t blue)
    

Before uploading, however, you\'ll need to adjust a few strings.

#### Configure Your WiFi Network

Near the top of the sketch, you\'ll find a couple string constants named `WiFiSSID` and `WiFiPSWD`. Change the `WiFiNetworkName` and `WiFiPassword` values to match your WiFi network name (SSID) and password.

    language:c
    const char WiFiSSID[] = "WiFiNetworkName";
    const char WiFiPSWD[] = "WiFiPassword";

#### Configure Your Blynk Token

Next, you\'ll need to configure the `BlynkAuth` string to match your **Blynk auth token**. You can find this in the settings section of your Blynk project \-- click the hexagon-shaped \"nut\" icon in the upper-right.

Use the **E-Mail** feature to send yourself a copy of the auth token, which you can copy and paste into the code:

    language:c
    const char BlynkAuth[] = "0a1b2c3d4e5f..."

### Upload the Code

Finally, upload the code \-- making sure your serial port is correctly selected and the board type is set to **SparkFun Blynk Board**.

[![Select the Blynk Board board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/arduino-board-select-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/arduino-board-select-2.png)

## Monitoring the Monitor

Once you\'ve uploaded the code, set up your Blynk project, and connected the hardware. You should be all set to monitor your laundry machines!

### RGB Status LED

You may want to test the apparatus out with some manual shaking first. Aside from the LCD and gauge widgets, the Blynk Board\'s RGB LED should also relay information about the laundry monitor\'s state.

  LED Color   State
  ----------- -------------------------------------------------------------------------------------------
  Blue        Board initializing, connecting to WiFi/Blynk.
  Green       Monitor primed - laundry inactive.
  Purple      Preliminary shakes detected. \"Start time\" hasn\'t been fully triggered yet.
  Red         Laundry machine active!
  Orange      Preliminary laundry stoppage. No shaking, but the full \"stop time\" hasn\'t elapsed yet.

Once the board connects to WiFi and Blynk, the LED should turn green. As you begin to shake the sensor it should turn purple. Continuing to shake beyond the \"start time\" settings should turn the LED red, and it will remain red as long as you continue shaking above the threshold.

Once the shaking stops, the LED should turn orange. And as long as the shaking stays below the threshold for the set \"stop time\" setting, the LED will eventually turn back to green.

When the LED turns **from orange to green**, the Blynk Board will send a notification \-- assuming the \"Enable Push\" button is ON.

Continue shaking the sensor until you get a feel for how all three the sliders affect the board\'s state.

### Place the Sensor!

Load up your laundry, add your detergent, and set the laundry monitor up on top of your appliance. Use this first load to gauge some of the time and threshold settings that need adjusting.

[![Monitor in place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/photo-6120-1000.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/photo-6120-1000.JPG)

While the machine is rocking, you should see the \"shakiness\" gauge widget doing some rocking of its own. Tune the **threshold slider** up or down so it only triggers when the machine is running. Messages on the LCD should tell you whether or not the Blynk Board thinks your laundry is running.

Watch for any \"fake stops\", and turn the \"Stop Time\" slider up accordingly. If you feel like everything\'s set where it needs to be, turn the \"Enable\" button on, and go take care of other household needs. When your machine stops shaking, your phone should let you know!

[![Laundry done notification](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/1/screen-notification.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/1/screen-notification.PNG)