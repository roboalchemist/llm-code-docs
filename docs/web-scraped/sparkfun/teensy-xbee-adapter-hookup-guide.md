# Source: https://learn.sparkfun.com/tutorials/teensy-xbee-adapter-hookup-guide

## Introduction

**Note:** While the adapter was designed for the Teensy 3.1, it is compatible with the Teensy 3.2 as well. The Teensy 3.2 is populated with a more powerful 3.3V voltage regulator with the ability to power additional power-hungry 3.3V devices! Additionally, the adapter interfaces best with the Teensy 3.1, but the Teensy LC can be utilized as well. For more information, check out the specs on PJRC:\
\

[PJRC Teensy 3.2 / 3.1 Specs](https://www.pjrc.com/teensy/teensy31.html#specs)

**Heads up!** Originally, this tutorial was written to configure an XBee Series 1 to communicate in transparency mode. However, this can apply to the XBee Series 3 module as long as you configure the firmware to the legacy 802.15.4 protocol. For more information, check out the [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) tutorial.

The Teensy is a great way to get more computing power than an Arduino, and in less space. When a decently ranged, no-frills wireless serial link is required, the XBee series is a great solution. The [Teensy XBee Adapter](https://www.sparkfun.com/products/13311) joins the two with ease and brings wireless to your Teensy projects. This tutorial will demonstrate the basics of using the adapter board.

[![Teensy 3.1 XBee Adapter](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/8/7/13311-01.jpg)](https://www.sparkfun.com/teensy-3-1-xbee-adapter.html)

### [Teensy 3.1 XBee Adapter](https://www.sparkfun.com/teensy-3-1-xbee-adapter.html) 

[ BOB-13311 ]

The Teensy is an amazing development platform that allows you to get more computing power than an Arduino Uno, and in less sp...

**Retired**

This tutorial demonstrates:

- How to initialize Teensy 3.1 HW serial
- How to initialize Teensy 3.1 SW serial using softwareSerialAlt library
- The basics of packetizing data.
- How to make a simple controller that effects something far away

### Required Materials

At a minimum, you\'ll need an XBee explorer, two XBees, a Teensy and the adapter board. Here\'s a list of things you\'ll need if you want *two* Teensy XBee radio stations that are both off-the-grid, plus some useful extras.

#### Required Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49). Depending on your setup, you will also need hookup wire, wire strippers, and a hobby knife.

- Soldering iron and flux core solder
- Hookup wire
- Wire strippers
- X-acto or knife for cutting traces (optional)

#### Software Requirements

- [Arduino IDE](http://www.arduino.cc/en/Main/Software)
- [Teensyduino add-on for the Arduino IDE](https://www.pjrc.com/teensy/td_download.html)
- [AltSoftSerial library](https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html)
- [X-CTU](http://www.digi.com/products/wireless-wired-embedded-solutions/zigbee-rf-modules/xctu)

### Suggested Reading

Before getting started, there are a few concepts that you should be familiar with. If you haven\'t used a Teensy or XBee before, read these tutorials before continuing:

- [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy) - How to install Teensyduino, comparison of the Teensy 3.1 and LC, and soldering options.
- [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) - Guide to configuring the XBees using the XBee tool XCTU
- [XBee Buying Guide](https://www.sparkfun.com/pages/xbee_guide) - Shows various XBee models including current consumption use an Arduino to control the APDS-9960
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics) - Lots of information about serial. If you\'ve only ever used the Arduino Serial monitor (or no terminal at all), this is a good resource. It shows how to get serial terminals working on Mac, Linux, and Windows.

## Hardware Overview

Apart from mechanically connecting the The Teensy and XBee, the adapter has a some features to help you get the most from the hardware. Here\'s what each section does.

[![Teensy Xbee Adapter Numbered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/4/HardwareParts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/HardwareParts.jpg)

*Key Parts of the Adapter*

1.  **Teensy 3.2/3.1 (and LC) Footprint** - Connect the Teensy here. Make sure to add headers next to the shorter row of pins next to the Teensy\'s reset button to power the XBee by default.
2.  **UART1/S-UART Switch** - Select which serial pins are connected to the XBee (pins 0/1 for the hardware UART, pins 20/21 for the software UART).
3.  **XBee Socket** - Plug the XBee in here matching silkscreen shape.
4.  **VIN/EXT Jumper Pad** - Short to source Teensy power from the EXT_IN pins.
5.  **XBee Status LEDs** - Shows data movement, signal strength, and digital IO pin 5 (XBee signals).
6.  **Spare Ground Connections** - My gift to you! More ground pins for reference.
7.  **TNSY/EXT Jumper Pads** - Selects the source of power for the XBee. The default is connected to the Teensy\'s on-board voltage regulator. When providing external power from the EXT_PWR (3.3V) pins, move the solder jumper to the EXT_IN side.
8.  **Power LED** - Shows if XBee is getting power.
9.  **EXT_PWR (3.3V)** - Supply regulated 3.3v here only when necessary.
10. **XBee Reset Switch** - Resets the XBee.

[![Bottom View](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/4/Teensy_XBEE_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Teensy_XBEE_Tutorial-04.jpg)

*Bottom View*

[![Xbee and Teensy Installed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/4/Teensy_XBEE_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Teensy_XBEE_Tutorial-02.jpg)

*With XBee and Teensy Installed*

Don\'t forget to check out the [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy) tutorial for information on attaching the Teensy to an adapter.

## Hardware Assembly

There are a few theoretical steps to get a project working with the Teensy and XBee that will be discussed.

Here are the basic steps:

- Determine how to power the system
- Connect the hardware
- Configure the XBees
- Establish serial over XBee (this tests all systems - highly recommended)
- Build and test the actual project

### Determine How the System is Going to be Powered

#### Powering Low Power XBees [Default Solder Jumper]

⚡**Note:** The Teensy 3.2 is populated with a more powerful 3.3V voltage regulator with the ability to power additional power-hungry 3.3V devices! For more information, check out the specs on PJRC:\
\

[PJRC Teensy 3.2 / 3.1 Specs](https://www.pjrc.com/teensy/teensy31.html#specs)

The XBee requires around 3.3V to operate, depending on the model. The Teensy 3.1 and 3.0 have an on-board regulator that outputs 3.3V, which is perfect, but only for lower power radios that consume less than 100mA.

[![Diagram for Default Jumper to Power XBee](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/4/PowerOption1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/PowerOption1.png)

*Powering from the Teensy\'s Internal Regulator*

This is the default configuration. The internal regulator can supply about 100mA of current for 3.3V use, including what is consumed by the Teensy and things on the 3.3V rail. XBees up to 2mW (non-\"pro\" models) consume up to 40mA, so, if you have a basic XBee, this is probably the route for you. Supply 3.7V to 5.5V (or USB power).

[] **Heads up!** Remember, you need to add headers next to the shorter row of pins next to the Teensy\'s reset button to power the XBee by default.\
\

[![](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Teensy_XBee_Adapter_Default_Jumper_XBeer_Power.jpg "Default Jumper")](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Teensy_XBee_Adapter_Default_Jumper_XBeer_Power.jpg)

#### Powering High Power XBees [EXT Solder Jumper]

If you have a higher powered XBee, or more than 100mA of load on your 3.3V rail, you\'ll need to disconnect the XBee from the Teensy 3.1 and 3.0\'s internal regulator and supply 3.3v from somewhere else. A [Breadboard Power Supply Stick](https://www.sparkfun.com/products/13157) is a possible power source for this application.

[![External Power for XBee](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/4/PowerOption2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/PowerOption2.png)

*Powering the XBee from an External 3.3v Regulator*

In this case,

- switch the **PWR**\'s solder jumper from the **TNSY** side to the **EXT** side
- short the jumper pad between **VIN** and **EXT_PWR**
- cut the trace between the Teensy\'s USB PWR jumper

  Example                                                                                                                                                                                                                                               Notes
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13311-04_EXT_Jumper.jpg "move solder jumper to EXT side")](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13311-04_EXT_Jumper.jpg)                                                  switch the **PWR**\'s solder jumper from the **TNSY** side to the **EXT** side
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13311-04_EXT_PWR_Jumper_3.jpg "short the jumper pad between VIN and EXT_PWR")](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13311-04_EXT_PWR_Jumper_3.jpg)                        short the jumper pad between **VIN** and **EXT_PWR**
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13736-04_Teensy_3.1_Cut_VUSB_Here.jpg "cut the trace between the Teensy's USB PWR jumper")](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/13736-04_Teensy_3.1_Cut_VUSB_Here.jpg)   cut the trace between the Teensy\'s USB PWR jumper indicated by the red line in the image

Now both the Teensy and XBee are powered from the ext power pins, so you\'ll need to provide power and plug in the USB if you want to reprogramming the device.

### Connect the Teensy to the XBee.

The XBee fits straight into the adapter. Make sure the XBee outline matches the silkscreen on the adapter.

The Teensy and adapter come as PCB without headers. Check out the Sparkfun [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy) for example of how pins and sockets can be attached.

### Connect Periphery Equipment

Use the outer holes to connect all manor of switches and sensors that you wish to read from the Teensy. This tutorial makes a controller, so buttons and LEDs are connected as shown in this diagram.

[![Buttons and LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Fritzing_export.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Fritzing_export.png)

### Configure the XBees

The XBees are shipped with a default configuration (see XBee documentation). Even if they work out of the box, you\'ll be using the default IDs and will be suseptable to unseen XBees interfering with your system (because some other designer had the similar thought, \"I\'m the only one here, why not use the default IDs.\") Also, you can change other more advanced features once you\'re familiar with the concepts.

**The parameters used for these demos**

- ID/PAN ID = A5F1 - This can be any 16 bit hex value used to identify your network. Make sure it is the same for both radios and unique in your area. A5F1 was randomly chosen for this guide. You can choose any ID for your network.
- Data rate = 9600
- Parity = N
- All others at factory default

**Configuring XBees with USB based explorers**

- Socket an XBee into the explorer matching the silkscreen orientation
- Plug the explorer into the USB port
- Open X-CTU
- Select your explorer\'s serial port
- Querry the XBee to make sure the drivers are working
- Read the configuration from the XBee
- Modify the parameters
- Write the new configuration to the XBee

Repeat this process so that both XBees have the new configuration.

### Power the System!

Apply to the system. Powering through the Teensy, use 3.7 to 5.5v. Alternately, supply **regulated** 3.3v to the EXT_PWER pins. Does the power LED on the adapter illumniated? It shows if power is getting to the XBee. Try running the blink sketch to determine if the Teensy is really powered and ready to recieve firmware.

## Software

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Working with Your Serial UART Ports

Working with wireless devices is more difficult than just a single Arduino because more than one serial port is in use. Where Arduino allows you to simply load the serial monitor to talk to your code, be extra careful remembering which ports what device and which terminal are using.

The first serial link in use is between the XBee and computer through the serial explorer. Get this port open and communicating to the XBee, then leave it alone. It ushers bytes you type into it into the air, and prints whatever comes into it\'s antenna to your screen. When the system is fully functional, this terminal will tell you what buttons are being pressed.

The second serial link is the Arduino serial monitor, which connects to the Teensy over the USB cable. Eventually the Teensy will be disconnected from the computer but it can be useful to get debugging information from your program while working with it. Be careful not to confuse it with the other serial ports. When you upload a sketch, the serial monitor automatically closes. If you\'re using a 3rd party terminal here make sure it is closed before upload in order to free up the USB port for programming.

The trickiest serial link in this project is the one that goes from the Teensy to the XBee because we have little information about it. Without expensive scopes, use the Din and Dout LEDs to monitor if there is activity from the Teensy to the XBee. One illuminates when the Teensy sends data to the XBee, and the other for showing when data is coming from the XBee to the Teensy.

**Heads up!** Previously, the code used in this tutorial used a `Serial1.print()` with a `BYTE` to pass serial data. You may receive the following error when compiling code:\
\

``` c
teensy_3_1_xbee_UART1_example:31: error: 'BYTE' was not declared in this scope
     Serial1.print(Serial.read(), BYTE);

                                  ^

teensy_3_1_xbee_UART1_example:37: error: 'BYTE' was not declared in this scope
     Serial.print(Serial1.read(), BYTE);

                                  ^

'BYTE' was not declared in this scope
```

After a [certain version of Arduino](https://forum.arduino.cc/index.php?topic=85382.msg639273#msg639273), the functionality was removed and `BYTE` is no longer a keyword. Instead of:\
\

    Serial1.print(Serial.read(), BYTE);  

Make sure to replace the `print` methods with `write`. Then remove any instance of \"`, BYTE`\". The code in this tutorial has been updated to reflect this note.\
\

    Serial1.write(Serial.read());  

### Test Your Serial and XBee Configuration

Two sketches are provided to ease bringing the XBees on line. They pass data between the XBee and the serial monitor using the HW UART or the SW UART \'AltSoftSerial\' library. You can get them from the [GitHub repository for the Teensy 3.1 XBee Adapter](https://github.com/sparkfun/Teensy_3_1_XBee_Adapter) or by copy-pasting the code.

[Download GitHub Repo SparkFun Teensy 3.1 XBee Adapter (ZIP)](https://github.com/sparkfun/Teensy_3_1_XBee_Adapter/archive/master.zip)

#### Hardware UART Example [teensy_3_1_xbee_UART1_example.ino]

The following uses the Teensy\'s hardware serial UART to create a serial passthrough in the *teensy_3_1_xbee_UART1_example.ino* sketch in order to test the hardware UART and XBee configurations. Make sure to set the adapter\'s serial switch to **UART1**. Then load and run the example.

    language:c
    //Serial test using the hardware uart on pins 0/1 (UART1).
    //Connect an XBee and Teensy 3.1 to the adapter board
    //Connect an XBee to a serial terminal of your choice (USB dongle for example)
    //
    //Characters sent out the XBee terminal go:
    // Onto the airwaves -> into UART1 RX -> out the serial monitor
    //
    //Characters sent out the serial monitor go:
    // Out the UART1 TX pin -> onto the airwaves -> out the SBee serial terminal
    //
    //Be sure to select UART1 on the adapter board's switch for HW serial

    void setup()
    

    void loop()
    

      // Take data received from the HW UART and pass it to the serial monitor
      if(Serial1.available())
      

      //Wait to reduce serial load
      delay(5);
    }

Open the serial monitor. Text entered in the serial monitor will be passed to the XBee, and come out the X-CTU (or other, I use Tera Term) serial monitor. Typing in that terminal will send the text back to the Arduino serial monitor.

#### Software Serial UART Example [teensy_3_1_xbee_SUART_example.ino]

The following uses the Teensy\'s software serial UART to create a serial passthrough in the *teensy_3_1_xbee_SUART_example.ino* sketch in order to test the hardware UART and XBee configurations. This sketch works much like the UART1 example but with the AltSoftSerial library, leaving the hardware UART free to connect to other resources. Make sure to set the adapter\'s switch to **S-UART** and run the sketch.

    language:c
    #include <AltSoftSerial.h>
    //Serial test using the software uart on pins 20/21.
    //Connect an XBee and Teensy 3.1 to the adapter board
    //Connect an XBee to a serial terminal of your choice (USB dongle for example)
    //
    //Characters sent out the XBee terminal go:
    // Onto the airwaves -> into S-UART RX -> out the serial monitor
    //
    //Characters sent out the serial monitor go:
    // Out the S-UART TX pin -> onto the airwaves -> out the SBee serial terminal
    //
    //Be sure to select S-UART on the adapter board's switch for HW serial

    AltSoftSerial altSerial;

    void setup() 

    // the loop routine runs over and over again forever:
    void loop() 

      // Take data received from the HW UART and pass it to the serial monitor
      if(altSerial.available())
      

      //Wait to reduce serial load
      delay(5);
    }

Text should be passed between the two serial terminals.

### Running the Demo Sketch

One sketch is provided to demonstrate passing data between a computer with [SparkFun XBee Explorer USB](https://www.sparkfun.com/products/11812) and a remote Teensy with XBee. You can get it from the [GitHub repository for the Teensy 3.1 XBee Adapter](https://github.com/sparkfun/Teensy_3_1_XBee_Adapter) or by copy-pasting the code.

#### Hardware Hookup

If you have not already, make sure to connect LEDs and buttons to the remote Teensy with XBee.

- Attach buttons to pins 14-17 of the Teensy, and to ground. The pins are pulled up inside the Teensy and will float high until a button is depressed.
- Attach LEDs from pins 4-12 of the Teensy, through a current limiting resistor, to ground. It\'s not so important to have all 8, 2 or 3 is enough to demonstrate the effect.

[![Buttons and LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Fritzing_export.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/4/Fritzing_export.png)

#### Remote Control of I/O [teensy_3_1_xbee_buttons_and_leds_example.ino]

This sketch demonstrates bi-directional communication and shows off operation that is more than just data echo.

    language:c
    #include <AltSoftSerial.h>
    //To use this example you will need to have the following connections:
    //  4 buttons connected to pins 14 through 17, normally open, short to ground.
    //  8 LEDs connected to pins 4 through 11, each with their own current limiting resistor.
    //  The sketch is intended to have leds with a common ground, though using a common power
    //  will work invertedly.
    //
    //You will also need:
    //  A Teensy 3.1 to XBee adapter board with XBee
    //  A 2nd XBee connected to serial terminal (USB dongle with Tera Term for example)
    //  The S-UART / UART1 switch set to S-UART for a software UART using the altSoftSerial library
    //  
    //Load the sketch and press the buttons.  In the serial terminal the '0's change to '1's.
    //Press 1-8 on the keyboard in the terminal window.  The LEDs will illuminate.  Press enter or
    //any other key to clear the LEDs.

    // Define pin locations
    int upleftButton = 14;
    int uprightButton = 15;
    int downleftButton = 16;
    int downrightButton = 17;
    int led1Pin = 4;
    int led2Pin = 5;
    int led3Pin = 6;
    int led4Pin = 7;
    int led5Pin = 8;
    int led6Pin = 9;
    int led7Pin = 10;
    int led8Pin = 11;

    AltSoftSerial altSerial;

    void setup() 

    // the loop routine runs over and over again forever:
    void loop() 

      }

      delay(100);        // delay in between reads for stability
    }

Each time the loop() runs, the sketch the Teensy:

- Converts button presses to an ASCII representation
- Prints the button states to the Arduino serial monitor
- Transmits the button states as a series of ASCII characters
- Checks for received data from the XBee. If a number 1-8 is received, the associated LED on pins 14-21 is illuminated. If any other character is received, all 8 LEDs are are switched off.

## Conclusion

The Teensy is really a great small-footprint powerhouse. Paired with the XBee you can get a great long distance serial connection, and with the 72MHz of processing speed (48MHz for the Teensy-LC) you can do a lot with the information. The Teensy is also capable of being a \"class driver\" device, you can get that data into a computer with ease, turning it into a keyboard, mouse, serial, or midi device.