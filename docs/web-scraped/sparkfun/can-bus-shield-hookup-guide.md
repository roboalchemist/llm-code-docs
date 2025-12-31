# Source: https://learn.sparkfun.com/tutorials/can-bus-shield-hookup-guide

## Introduction

The [CAN-Bus Shield](https://www.sparkfun.com/products/13262) provides your Arduino or Redboard with CAN-Bus capabilities and allows you to hack your vehicle!

[![CAN-Bus Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/BoardFullySoldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/BoardFullySoldered.jpg)

*CAN-Bus Shield connected to a RedBoard.*

This shield allows you to poll the ECU for information including coolant temperature, throttle position, vehicle speed, and engine rpms. You can also store this data or output it to a screen to make an in-dash project.

### Materials Required

You will need the CAN-Bus Shield in order to follow along with this hookup guide.

[![CAN-BUS Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/6/6/13262-01.jpg)](https://www.sparkfun.com/can-bus-shield.html)

### [CAN-BUS Shield](https://www.sparkfun.com/can-bus-shield.html) 

[ DEV-13262 ]

The CAN-BUS Shield provides your Arduino or Redboard with CAN-BUS capabilities and allows you to hack your vehicle. This shie...

[ [\$35.95] ]

We also recommend you have access to the following materials.

### Suggested Reading

If you aren\'t familiar with the following concepts, you may want to review these tutorials before attempting to work with the CAN-Bus Shield.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/gps-shield-hookup-guide)

### GPS Shield Hookup Guide 

This tutorial shows how to get started with the SparkFun GPS Shield and read and parse NMEA data with a common GPS receiver.

[](https://learn.sparkfun.com/tutorials/microsd-shield-and-sd-breakout-hookup-guide)

### MicroSD Shield and SD Breakout Hookup Guide 

Adding external storage in the form of an SD or microSD card can be a great addition to any project. Learn how in this hookup guide for the microSD shield and SD breakout boards.

[](https://learn.sparkfun.com/tutorials/getting-started-with-obd-ii)

### Getting Started with OBD-II 

A general guide to the OBD-II protocols used for communication in automotive and industrial applications.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

## Hardware Overview

There are several features to be aware of on the CAN-Bus Shield.

[![Shield-Labeled](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/Shield_Labeled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/Shield_Labeled.png)

*CAN-Bus Shield with features labeled.*

### 1. DB9 Connector

The primary hardware feature on this shield is the DB9 connector. This allows you to interface to OBD-II ports with a [DB9 to OBD-II cable](https://www.sparkfun.com/products/10087).

### 2. GPS Connector

The GPS connector on-board is a [6-pin, JST SH compatible](https://www.sparkfun.com/products/9123) connector. The board is designed to interface with either the [EM-506 GPS Receiver](https://www.sparkfun.com/products/12751), or the [GP-735 GPS Receiver](https://www.sparkfun.com/products/13670). The `GND` jumper allows the user to modify the GPS connector for units that do not have a `GND` connection on pin 5 of the connector.

### 3. LCD Connector

The LCD footprint on the shield is compatible with a [male 3-pin JST connector](https://www.sparkfun.com/products/9915) and can interface with any of our serial LCD screens. The connection is designed for 5V LCDs, so don\'t accidentally plug in a 3.3V option! The pin order is 5V, GND, and RX/D6 when looking at the shield straight on.

### 4. JoyStick

The joystick included on the shield provides a basic user interface for controlling screen displays or selecting CAN scan settings. The connector gives 5 basic user options:

- Up
- Down
- Left
- Right
- Click selection

### 5. microSD Slot

This slot provides the user with the option of storing collected data onto a microSD card. Data collected can include user input on the joystick, CAN-Bus information collected, LCD outputs, or general I/O data.

### 6. Jumpers

There are six jumpers present on the CAN-Bus Shield.

- **6a. SJ1 and SJ2** - These two jumpers allow the user to select between UART and Software Serial for the GPS unit to communicate with the Arduino.

- **6b. SJ3** - This allows the user to separate pin 5 on the GPS connector from the `GND` line. This jumper comes closed by default.

- **6c. SJ4, SJ5, and SJ6** - These three jumpers allow the user to select the DB9 pin configuration between OBD-II and CAN. The jumpers are defaulted to the OBD-II configuration that matches SparkFun\'s [OBD-II to DB9 cable](https://www.sparkfun.com/products/10087).

**Note:** Though the pin configuration is labeled as OBD-II, this is still a \*CAN-specific\* device. The jumpers are simply for configuring the shield to work with other OBD-II/CAN-Bus \*\*cables\*\* if necessary.

For reference, here are the configuration options showing which pins are selected on the DB9 connector for each setting.

**Jumper Configurations for DB9 Pins**

Bus Lines

CAN Pins

OBD-II Pins

Solder Jumper

CAN-H

Pin 7

Pin 3

SJ4

CAN-L

Pin 2

Pin 5

SJ6

GND

Pin 3

Pin 2

SJ5

### 7. CAN Pins

4 CAN lines are broken out to allow you direct access to the raw CAN data coming off of the DB9 connector. These pins are:

- 5V
- GND
- CAN H (CAN HIGH)
- CAN L (CAN LOW)

Again, this data is raw coming off of the CAN-Bus. It has not been filtered through the MCP2515 or the MCP2551 ICs.

### Communication Methods

Because of all of the different hardware features on the shield, there are a couple different communication methods used.

- **SPI** - The MCP2515 IC and the microSD slot both communicate with the Arduino via the SPI lines. The CAN `Chip Select` line is located on `D10`. The SD `Chip Select` line is connected to `D9`.

- **Analog In** - The joystick is connected to pins A1-A5 on the Arduino. Each direction of the joystick has its own analog input.

- **Software Serial/UART** - The LCD and GPS both communicate over serial lines with the Arduino. The LCD\'s `RX` line connects to `D6`. The GPS either connects via Software Serial to `D4` and `D5`, or to the UART port on `D0` and `D1`.

## Hardware Hookup

### Solder Connectors

To get your CAN-Bus shield hooked up, solder on the [Arduino Stackable Headers](https://www.sparkfun.com/products/11417).

[![Headers Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/HeadersInserted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/HeadersInserted.jpg)

*You can use the RedBoard to hold the headers in place while soldering them to the shield.*

Once those are soldered, consider how you want to connect your LCD screen. You can use either male or female headers with 0.1\" spacing, or the JST connector. Solder your interface choice onto the shield at this time as well.

[![LCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/LCDConnectionSoldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/LCDConnectionSoldered.jpg)

*Make sure you solder the connector onto the top of the shield, so you can access it while the shield is inserted in the RedBoard.*

### Connect the Brain!

In our case, the brain will be the RedBoard. Insert your shield into the RedBoard. Take your time and go slowly to prevent bending the header pins.

### Connect the Extras

We recommend plugging in the GPS unit, LCD screen, and microSD card now. If you don\'t plan to use any of these features, you can skip this step.

If you\'re planning on putting your CAN-Bus/RedBoard combination into an enclosure, you may want to consider using an [extension cable](https://www.sparkfun.com/products/9123) for the GPS unit. Enclosures can block the satellites from view and lead to spotty GPS functionality, so placing the GPS unit outside of any enclosures should alleviate those issues.

**Note:** If you are not using the EM-506, verify the pinout of your GPS unit and make sure the GND jumper is in the proper configuration for your unit.

We also recommend connecting your LCD screen at this time. Your method of connecting the LCD screen will depend on what connector you soldered onto the shield previously. Looking the shield straight on, the connections are 5V, GND, and TX, if you are not using the JST connector.

Make sure you use a formatted microSD card. Once all the extras are connected, your circuit should look like the following:

[![GPS Inserted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/GPSInserted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/GPSInserted.jpg)

### Connect to your CAN-enabled device

This can be a simulator or a vehicle. Plug the DB9 connector into the shield, and plug the DLC connector into the device to which you plan on talking. If your shield+Arduino turns on now, that\'s ok. The vehicle/simulator can power the board over the cable.

### Final Circuit

Once everything is inserted, your circuit should look similar to the following:

[![Connected to Simulator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/ConnectedToSimulator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/ConnectedToSimulator.jpg)

In this case, we show the circuit connected to a CAN simulator. However, you could instead have your circuit connected to a DLC in a CAN-enabled vehicle.

[![Connected to Car](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/ConnectedToDash.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/ConnectedToDash.jpg)

*Here we see the circuit connected to [Pete Dokter\'s](https://www.sparkfun.com/news/tags/according-to-pete) VW.*

## Arduino Library Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

There\'s a really great library available for working with the CAN-Bus shield. You will need to download this and install it in your Arduino IDE. You can either search for it in the Arduino Library Manager or download the most recent version from the [GitHub repository](https://github.com/sparkfun/SparkFun_CAN-Bus_Arduino_Library) by downloading the library from the button below.

[Download CAN-Bus Shield Library (ZIP)](https://github.com/sparkfun/SparkFun_CAN-Bus_Arduino_Library/archive/master.zip)

## Example Code

**Heads up!** The following examples are a demonstration of the CAN-Bus shield\'s capabilities to get started. Depending on your particular vehicle\'s **parameter identification (PID)**, the code may need to be adjusted accordingly (i.e. check the [Canbus.h file](https://github.com/sparkfun/SparkFun_CAN-Bus_Arduino_Library/blob/ffcd67b7f4d5112f747f7c74a8677ef82a4ee202/src/Canbus.h#L22)). Additionally, make sure that CAN-bus shield is compatible with the **[communication protocol](https://learn.sparkfun.com/tutorials/getting-started-with-obd-ii#obd-ii-protocols)** of your particular car\'s model.

There are several different example sketches included in the library, each with different functionality.

1.  **SparkFun_CAN_Demo** - This sketch allows you test the CAN functionality of the board by itself.

2.  **SparkFun_ECU_Demo** - This sketch runs all hardware on the shield together, and logs CAN data and GPS data to the SD card, while outputting data over the serial LCD. You will need to instally the [TinyGPS library](https://github.com/mikalhart/TinyGPS) and the [SD library](https://github.com/arduino/Arduino/tree/master/libraries/SD) for this to work.

3.  **SparkFun_GPS_Demo**- This sketch runs through using the GPS module. You will need to instally the [TinyGPS library](https://github.com/mikalhart/TinyGPS) for this to work.

4.  **SparkFun_Joystick_Demo** - This quick sketch allows you to test the functionality of the on board joystick.

5.  **SparkFun_SD_Demo** - This sketch allows you to verify and test functionality of the microSD socket on board. You will need to install the [SD library](https://github.com/arduino/Arduino/tree/master/libraries/SD) for this to work.

6.  **SparkFun_SerialLCD_Demo** - A quick sketch to make sure your serial LCD screen is functioning properly.

7.  **CAN_Read_Demo** - A very stripped down sketch to read any and all data coming out of the CAN bus.

8.  **CAN_Write_Demo** - A basic demo for writing to the CAN bus.

**Note:** Examples 7 and 8 are courtesy of Stephen McCoy- a SparkFun customer. You can find Stephen\'s original tutorial on Instructables:\
\

[Instructables.com: Car To Arduino Communication - CAN Bus Sniffing and Broadcasting with Arduino](http://www.instructables.com/id/CAN-Bus-Sniffing-and-Broadcasting-with-Arduino/)

\

For our example, we are going to run through the *ECU_Demo* sketch, but feel free to use or modify the other sketches. If you decided to not plug in the microSD card, GPS unit and LCD screen, you should instead run the *CAN_Demo*.

#### ECU_Demo

This sketch shows off the basic functionality of each part of the shield. Once you\'ve installed the library, open up Arduino and upload this code to your RedBoard.

Check through the comments in the code for details of what each section does, but the general flow of the sketch is as follows:

1.  The Arduino initializes the pins, variables, and baud rates for the GPS, LCD, uSD card, and CAN-Bus.
2.  In the setup loop, each device is started, and verified that everything is connected as it should. Both the CAN-Bus and uSD card will print either success or failure messages to the LCD screen.
3.  The shield will wait for the user to click the joystick to begin collecting data off of the GPS module and the CAN-Bus.
4.  Once the user has clicked to begin logging, the CAN-Bus will poll for the engine RPM, and will write the latitude, longitude, and GPS speed. A message that the unit is logging will appear on the LCD screen, and the actual engine RPM will be printed to the Serial monitor. The data collected is written to the uSD card.
5.  Each loop, the code checks if the user has clicked the joystick. If so, the unit stops logging.

``` 

    /****************************************************************************
    ECU CAN-Bus Reader and Logger
    
    Toni Klopfenstein @ SparkFun Electronics
    September 2015
    https://github.com/sparkfun/CAN-Bus_Shield
    
    This example sketch works with the CAN-Bus shield from SparkFun Electronics.
    
    It enables reading of the MCP2515 CAN controller and MCP2551 CAN-Bus driver.
    This sketch also enables logging of GPS data, and output to a serial-enabled LCD screen.
    All data is logged to the uSD card. 
    
    Resources:
    Additional libraries to install for functionality of sketch.
    -SD library by William Greiman. https://github.com/greiman/SdFat 
     
    Development environment specifics:
    Developed for Arduino 1.65
    
    Based off of original example ecu_reader_logger by:
    Sukkin Pang
    SK Pang Electronics www.skpang.co.uk
    
    This code is beerware; if you see me (or any other SparkFun employee) at the local, 
    and you've found our code helpful, please buy us a round!
    
    For the official license, please check out the license file included with the library.
    
    Distributed as-is; no warranty is given.
    *************************************************************************/
    
    //Include necessary libraries for compilation
    #include 
    #include 
    #include 
    #include 
    #include 
    
    //Initialize uSD pins
    const int chipSelect = 9;
    
    
    //Initialize lcd pins
    SoftwareSerial lcd(3, 6);
    
    //Initialize GPS pins
    SoftwareSerial uart_gps(4,5);
    
    // Define Joystick connection pins 
    #define UP     A1
    #define DOWN   A3
    #define LEFT   A2
    #define RIGHT  A5
    #define CLICK  A4
    
    //Define LED pins
    #define LED2 8
    #define LED3 7
    
    //Define baud rates. GPS should be slower than serial to ensure valid sentences coming through
    #define GPSRATE 4800
    #define LCD_Rate 115200
    
    //Create instance of TinyGPS
    TinyGPS gps;
    
    //Declare prototype for TinyGPS library functions
    void getgps(TinyGPS &gps);
    
    //Declare GPS variables
    float latitude;
    float longitude;
    int year;
    byte month;
    byte day;
    byte hour;
    byte minute;
    byte second;
    byte hundredths;
    float gps_speed;
    
    
    //Declare SD File
    File dataFile;
    
    //Declare CAN variables for communication
    char *EngineRPM;
    char buffer[64];  //Data will be temporarily stored to this buffer before being written to the file
    
    //Define LCD Positions
    #define COMMAND 0xFE
    #define CLEAR   0x01
    #define LINE1  0x80
    #define LINE2  0xC0
    
    
    //********************************Setup Loop*********************************//
    void setup()  
      else
       
    
       //Check if uSD card initialized
      if (!SD.begin(chipSelect)) 
      else 
    
      //Print menu to LCD screen
      clear_lcd();
      lcd.print("Click to begin");
      lcd.write(COMMAND);
      lcd.write(LINE2);
      lcd.print("Logging Data");
     
      while(digitalRead(CLICK)==HIGH)
      
    
      delay(1000); 
    
    }
    
    //********************************Main Loop*********************************//
    void loop()
            
            clear_lcd();
            lcd.print("Logging.Click");
            lcd.write(COMMAND);
            lcd.write(LINE2);
            lcd.print("to stop logging");
            
            if(uart_gps.available())     // While there is data on the RX pin...
               
            
            dataFile.print("Engine RPM: "); 
            dataFile.println(EngineRPM);
            
            dataFile.println();
            dataFile.flush();
            dataFile.close();   //Close data logging file
          }
          clear_lcd();
          lcd.print("Logging stopped.");
          while(1); //Stop logging if joystick is clicked
          
        }
        
        //********************************LCD Functions*********************************//
        void clear_lcd(void)
         
        
        //********************************GPS Functions*********************************//
        void getgps(TinyGPS &gps)
        
```

If you\'ve uncommented the lines for serial debugging, you should see something like this:

[![Engine RPM](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/SerialMonitorOutput.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/SerialMonitorOutput.JPG)

*Engine RPM readings from CAN-Bus shield hooked up to a simulator.*

Once you have collected some readings, you can pull your uSD card out and take a look at the data recorded. There should be a file on your uSD card called \"DATA.TXT\", and it should include information like the following:

[![Recorded Data](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/uSDRecordedData.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/uSDRecordedData.JPG)

*Note: If you\'re only recording blank readings for your GPS, as shown above, make sure you have your GPS unit in an area with a good satellite view.*

Once you\'ve verified data is being stored to the uSD card, you\'re good to go! You\'ve successfully interfaced with your vehicle\'s CAN-Bus and can now start digging into diagnostic codes and building projects around your engine\'s data.