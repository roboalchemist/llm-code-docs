# Source: https://learn.sparkfun.com/tutorials/sparkfun-rfid-starter-kit-hookup-guide

## Introduction 

The [SparkFun RFID Starter Kit](https://www.sparkfun.com/products/13198) gives you the tools you need to start reading RFID tags with your computer or microcontroller!

[![SparkFun RFID Starter Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/3/3/4/13198-02.jpg)](https://www.sparkfun.com/sparkfun-rfid-starter-kit.html)

### [SparkFun RFID Starter Kit](https://www.sparkfun.com/sparkfun-rfid-starter-kit.html) 

[ KIT-13198 ]

This it the SparkFun RFID Starter Kit, an all-in-one kit that offer everything you need to get your next RFID project off the...

[ [\$53.50] ]

### Required Materials

The kit contains:

- 1x [RFID USB Reader](http://www.sparkfun.com/products/9963)
- 1x [ID-12LA RFID Module](https://www.sparkfun.com/products/11827)
- 2x [125KHz RFID cards](https://www.sparkfun.com/products/8310)

You will also need a [USB mini-B cable](https://www.sparkfun.com/products/11301) to connect the USB reader to a computer.

### Recommended Reading and Viewing

The ID-12LA module has a serial output. If you\'ve never worked with a serial device or a terminal program before, you might want to take a look at these tutorials first.

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics)
- [RFID Basics](https://learn.sparkfun.com/tutorials/rfid-basics)
- [Tim\'s RFID Comparison video](https://www.youtube.com/watch?v=FLjV5BT9slg) - Let Tim from Tech Support walk you through our entire line of Low Frequency RFID options, complete with range tests.
- [SparkFun Simple Sketches - RFID Starter Kit video](https://www.youtube.com/watch?v=aSqPt8UQOHM) - A simple video demo of the RFID Starter Kit in action.

## Hardware Overview: RFID USB Reader

The [RFID USB Reader](http://www.sparkfun.com/products/9963) has the following features:

[![RFID USB Hardware Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfid-base-annotated_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfid-base-annotated_2.jpg)

1.  **Buzzer and Buzzer Enabled Jumper** - A buzzer that sounds when a card is read. If you are using the RFID kit in a stealth application, you can disconnect the buzzer by removing the blob of solder on the **Buzz** jumper.

2.  **Card Read LED** - A \"card read\" status LED.

3.  **2mm RFID Sockets** - 2mm-spaced sockets that fit three of SparkFun\'s RFID modules (the [ID-3LA](https://www.sparkfun.com/products/11862), the [ID-12LA](https://www.sparkfun.com/products/11827), and the [ID-20LA](https://www.sparkfun.com/products/11828)).

4.  **USB mini-B Connector** - A USB mini-B connector to connect to a computer\'s USB port.

5.  **USB-to-Serial IC** - An FTDI232RL USB-to-serial IC that converts the module\'s TTL serial output to USB.

## Hardware Hookup

Place the ID-12 module onto the RFID USB Reader, and plug the base into your computer with a USB mini-B cable. Depending on your operating system, you may need to [install FTDI drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) after plugging in the base station.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/COM4_device_manager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/COM4_device_manager.png)

*Here\'s the RFID reader (on COM4) with the FTDI drivers installed.*

Open a terminal program of your choice. If you\'ve never used a terminal program before, [here\'s a guide to choosing and using them](https://learn.sparkfun.com/tutorials/terminal-basics).

First, use the Arduino IDE\'s built-in serial monitor:

- Open the Arduino IDE.
- Go to **Tools \> Port** and select the RFID reader\'s port.
- Go to **Tools \> Serial Monitor**. The default terminal settings (9600 baud, no line ending) are fine. The monitor should be blank.

Wave a card over the reader. You should hear a beep and see something like this.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/scanned_card.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/scanned_card.png)

Now, we\'ll do the same thing in RealTerm. (Mac users, you can try this section using [CoolTerm](https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux))

RealTerm may look like the cockpit of a 747 compared to the Arduino serial monitor, but it has several helpful features. [Keep the RealTerm tutorial open if you need it.](https://learn.sparkfun.com/tutorials/terminal-basics/real-term-windows)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_portsetting.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_portsetting.png)

*The RealTerm **Port** tab with the port set to `4` and the baud rate to `9600`*

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_hex.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_hex.png)

*The RealTerm **Display** tab*

With **Display As** set to `Hex[space]`, the card data appears as 16 hex bytes instead of 12 ASCII digits like it did in the Arduino Serial Monitor.

Wait, 16 bytes? Where did the extra four come from?

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/data_format.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/data_format.png)

Here\'s the \"Data format\" section from the ID-12 module datasheet. The 12 ASCII characters displayed in the Arduino serial monitor are just the filling in a 16-byte sandwich, with four more non-printing characters (STX or start-of-text, CR/carriage return, LF/linefeed, and ETX/end-of-text) as the bread.

Try switching the **Display As** setting to `ASCII` and scan again:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_ascii.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/realterm_ascii.png)

Now the \"bread\" is visible! That\'s cool, right?

## Example Project

As fun as it is to watch your cards pop up in the serial terminal, you\'d probably like to *do* something with all this power.

The example sketch below scans RFID cards and compares them against trusted cards, then moves a servo to unlock the secured\* item of your choice.

\* *Not suitable for critical applications, e.g. guarding the Hope Diamond.*

In addition to your RFID Reader Kit, you will want:

- A microcontroller like the [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or the [Arduino Uno](https://www.sparkfun.com/products/11021).
- [M/M Jumper Wires](https://www.sparkfun.com/products/12795)
- [Breadboard](https://www.sparkfun.com/products/12002)
- A [Servo](https://www.sparkfun.com/products/9065) - Larger sizes are suggested for larger locks.
- [Break-Away Male Headers](https://www.sparkfun.com/products/116) to solder to the board\'s through-holes. (If you need a soldering refresher, take a look at our [through-hole soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering))

[![RFID USB Reader Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/SparkFun_Arduino_RFID_USB_Kit__Servo_Lock_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/SparkFun_Arduino_RFID_USB_Kit__Servo_Lock_Fritzing_bb.png)

Connect the VCC, GND, and TX pins on the RFID USB Reader to the Arduino\'s 5V, GND, and D2 pins, and connect the servo to 5V, GND, and D9. Copy the code provided below and adjust values provided in the `knownTags[][]` array that was obtained in the simple hookup so that the Arduino recognizes your RFID tag. Upload the code, open your Serial Monitor by going to **Tools \> Serial Monitor**, and start scanning some cards!

    language:c
    /*****************************
         RFID-powered lockbox

    Written by: acavis, 3/31/2015
    Modified: Ho YUN "Bobby" Chan @ SparkFun Electronics Inc., 11/10/2017

    Inspired by & partially adapted from
    http://bildr.org/2011/02/rfid-arduino/

    Description: This sketch will move a servo when
    a trusted tag is read with the 
    ID-12/ID-20 RFID module

    ----------HARDWARE HOOKUP----------

    PINOUT FOR SERVO MOTOR
        Servo Motor ----- Arduino
        GND               GND
        Vcc               5V 
        SIG               D9

    PINOUT FOR SPARKFUN RFID USB READER
        Arduino ----- RFID module
        5V            VCC
        GND           GND
        D2            TX

    PINOUT FOR SPARKFUN RFID BREAKOUT BOARD
        Arduino ----- RFID module
        5V            VCC
        GND           GND
        GND           FORM
        D2            D0

    Optional: If using the breakout, you can also 
    put an LED & 330 ohm resistor between 
    the RFID module's READ pin and GND for 
    a "card successfully read" indication.

    Note: Make sure to GND the FORM pin to enable the ASCII output format. 

    --------------------------------------------------

    ******************************/

    #include <SoftwareSerial.h>
    #include <Servo.h>

    // Choose two pins for SoftwareSerial
    SoftwareSerial rSerial(2, 3); // RX, TX

    // Make a servo object
    Servo lockServo;

    // Pick a PWM pin to put the servo on
    const int servoPin = 9;

    // For SparkFun's tags, we will receive 16 bytes on every
    // tag read, but throw four away. The 13th space will always
    // be 0, since proper strings in Arduino end with 0

    // These constants hold the total tag length (tagLen) and
    // the length of the part we want to keep (idLen),
    // plus the total number of tags we want to check against (kTags)
    const int tagLen = 16;
    const int idLen = 13;
    const int kTags = 4;

    // Put your known tags here!
    char knownTags[kTags][idLen] = ;

    // Empty array to hold a freshly scanned tag
    char newTag[idLen];

    void setup() 

    void loop() 

      if (tag == true) 

          // If we see ASCII 3, ETX, the tag is over
          if (readByte == 3) 

        }
      }

      // don't do anything if the newTag array is full of zeroes
      if (strlen(newTag)== 0) 

      else 

        // If newTag matched any of the tags
        // we checked against, total will be 1
        if (total > 0) 

        else 
      }

      // Once newTag has been checked, fill it with zeroes
      // to get ready for the next tag read
      for (int c=0; c < idLen; c++) 
    }

    // This function steps through both newTag and one of the known
    // tags. If there is a mismatch anywhere in the tag, it will return 0,
    // but if every character in the tag is the same, it returns 1
    int checkTag(char nTag[], char oTag[]) 
        }
      return 1;
    }

**Note:** You may need to adjust the initial position of the servo in the setup depending on the servo motor that you are using. Certain servos (such as the [generic sub-micro size servo](https://www.sparkfun.com/products/9065)) may not be able to extend to its full range. Try changing the value in `lockServo.write(0)` to a higher value like `lockServo.write(10)`.

## Using the RFID Reader Breakout

For Arduino projects, you can also use the [SparkFun RFID Reader Breakout](https://www.sparkfun.com/products/13030) which gives the module a place to sit and breaks out its odd 2mm-pitch pins to a breadboard-friendly 0.1\" spacing.

To keep the module removable (and protect it from accidental damage during soldering), you can trim 2x [2mm XBee Sockets](https://www.sparkfun.com/products/8272) to size using a [diagonal cutter](https://www.sparkfun.com/products/8794) and solder them to the top of the breakout. You will need to sacrifice a header pin when cutting the 2mm XBee socket and pull/clip a pin from the 1x7 header before soldering to the RFID reader breakout as shown in figure 1. Make sure to test the header on the breakout board with the RFID module before soldering.

[![RFID Reader w/ Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/breakout_with_sockets.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/breakout_with_sockets.jpg)

- **Fig. 1** XBee sockets trimmed to size with one pin clipped short.
- **Fig. 2** Sockets soldered to the top of the breakout with [0.1\" male straight header pins](https://www.sparkfun.com/products/116) on the bottom.
- **Fig. 3** Module and breakout ready for use on a breadboard

The completed breakout can be used like the larger base station. Here\'s the same example as above with a green LED and 330 ohm resistor added to the READ pin. **TX** is labeled **D0** on the breakout.

[![RFID Breakout Fritzing Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/2/8/Arduino_RFID_Breakout_Servo_Lock_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/Arduino_RFID_Breakout_Servo_Lock_Fritzing_bb.png)

*Shown with the module removed so you can read the silk.*

**Note:** Make sure to connect the \"FORM\" pin to ground to enable the ASCII output format.