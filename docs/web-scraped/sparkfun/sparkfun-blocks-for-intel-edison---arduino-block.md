# Source: https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---arduino-block

## Introduction

The [Arduino Block for Edison](https://www.sparkfun.com/products/13036) provides the [Intel(R) Edison](https://www.sparkfun.com/products/13024) with a direct, serial link to an Arduino-compatible ATmega328 microprocessor.

[![Arduino Block iso](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/deafultarduino_block_iso.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/deafultarduino_block_iso.jpg)

Why would you need an Arduino connected to your Edison? Isn\'t it powerful enough to handle anything that may be thrown at it? That\'s the problem \-- it\'s almost too powerful. Because it\'s running an operating system, it\'s incapable of real-time processing \-- the bread-and-butter of smaller microcontrollers like the ATmega328. Components which require precise timing \-- like [WS2812 LEDs](https://www.sparkfun.com/products/11820) or [servo motors](https://www.sparkfun.com/categories/245) \-- may be incompatible with the Edison as it can\'t reliably generate clock signals.

The Arduino block allows the Edison to offload those lower-level hardware tasks. Additional to that, if you\'ve already written Arduino code for an external component, you don\'t have to port that code to the Edison \-- just run it on an Arduino block!

### Suggested Reading

If you are unfamiliar with Blocks, take a look at the [General Guide to Sparkfun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison).

Other tutorials that may help you on your Arduino Block adventure include:

- [Edison Getting Started Guide](https://learn.sparkfun.com/tutorials/edison-getting-started-guide)
- [Powering Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [Using the Arduino Pro Mini 3.3V](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

## Board Overview

[![Annotated diagram of Arduino Block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/annotated.png)

- **Expansion Header** \-- The 70-pin Expansion header breaks out the functionality of the Intel Edison. This header also passes signals and power throughout the stack. These function much like an [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields).
- **Arduino I/O Pins** \-- All of the Arduino\'s I/O pins are broken out to a pair of headers (plus a couple in between). This header footprint exactly matches that of the [Arduino Pro Mini](https://www.sparkfun.com/products/11114) \-- if you have any Mini shields they should mate exactly to this header.
- **Arduino Programming Header** \-- The standard 6-pin FTDI header is used to program the Arduino\'s serial bootloader. Plug a [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) in to program your Arduino.
- **D13 LED** \-- Every good Arduino needs an LED! This small, green LED is tied to the Arduino\'s pin 13. Great for blinking \"Hello, world\" or debugging.
- **Power LED** \-- The Arduino block has an on-board 3.3V regulator, and this LED is tied to the output of that regulator.
- **Arduino Reset Button** \-- This reset button is tied to the Arduino\'s reset line. It will only reset the Arduino; it has no effect on the Edison.

### Schematic Overview

The Arduino block pairs the ATmega328 to your Edison via one of two UARTs. The board defaults to connecting the Arduino to Edison via UART1. Jumpers (see more below) allow you to select UART2, if your application requires. Take care using UART2, though, it\'s default utility is for console access to the Edison.

The Arduino Block has an on-board 3.3V voltage regulator, which takes its input from the Edison\'s VSYS bus. Since the Arduino is running at 3.3V, its **clock speed is limited to 8MHz**.

If you want to take a closer look at the schematic, download the PDF [here](https://cdn.sparkfun.com/datasheets/Dev/Edison/arduino_block.pdf).

### Jumpers

On the back-side of the Arduino block, there are a handful of jumpers, which lend extra utility to the board.

[![Arduino Block Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/jumpers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/jumpers.png)

Three two-way jumpers \-- for RX, TX, and DTR \-- allow you to select between UART1 (default) and UART2. To switch these jumpers, grab a [hobby knife](https://www.sparkfun.com/products/9200), cut the default traces, and drop a solder blob between the middle pad and outer pad of your choice.

The jumper labeled **VIN/VSYS** allows you to remove the VSYS line from powering the Arduino block. This is handy if you need to isolate the Arduino block\'s power source from the Edison. In this case, you\'ll need to supply power (3.3-12V) externally via the \"VIN\" pin.

## Using the Arduino Block

To use the Arduino Block, attach it to either an Edison or add it to a stack of other SparkFun Block\'s.

[![Arduino Block in a stack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/stack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/stack.jpg)

*Arduino block stacked on top of a [GPIO Block](https://www.sparkfun.com/products/13038) and a [Base Block](https://www.sparkfun.com/products/13045).*

In order to supply power to your Edison, you\'ll need at least one additon Block in your stack. You can use a [Base Block](https://www.sparkfun.com/products/13045) or [Battery Block](https://www.sparkfun.com/products/13037), for example.

### Programming the Arduino

The Arduino on the Arduino Block can be programmed while it\'s either on or off the Edison. Depending on your application, though, it\'s recommended that you load code on the Arduino while it\'s disconnected from your Edison stack, before adding it to the rest of the system.

If you\'ve ever uploaded an Arduino sketch to an [Arduino Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11114), you\'re already familiar with uploading code to the Arduino block. Connect a [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) to the 6-pin FTDI header on the board.

[![Programming the Edison block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/programming.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/programming.jpg)

*Using a 3.3V FTDI Basic to program the Arduino on the Arduino Block.*

In Arduino (the non-Edison version of Arduino!), select \"Arduino Pro or Pro Mini 3.3V/8MHz\" from the Tools \> Board menu. If you\'re using the latest release of Arduino (1.6 or later), first select **Arduino Pro or Pro Mini** from the \"Board\" menu.

[![Board selection](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/board_selection_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/board_selection_01.png)

Then select **ATmega328 (3.3V, 8MHz)** from the \"Processor\" menu.

[![Processor selection](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/board_selection_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/board_selection_02.png)

Then upload away!

### Using the Arduino Pins

The Arduino\'s I/O pins are all broken out to a pair of headers. These headers match up exactly to the Arduino Pro Mini. If you have any shields or piggyback boards for a Pro Mini, it should work seamlessly with the Arduino Block.

You can solder [headers](https://www.sparkfun.com/products/115), [wires](https://www.sparkfun.com/products/11367), or any other connectors to these pins.

[![Arduino Block in action](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/6/in-action.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/6/in-action.jpg)

If you\'re soldering headers to the pins, take extra care deciding which side to solder to. Depending on the rest of your Edison stackup, those headers might get in the way of connectors on other boards (the USB connectors on the Base and Console Blocks, in particular).

### Connecting the Edison to the Arduino

The Arduino Block connects the Arduino to the Edison through a serial (UART) connection. Jumpers on the back of the board allow you select which of the Edison\'s two UARTs mate with the Arduino. Unless you can\'t avoid it, we recommend leaving the jumpers in the default configuration \-- the Edison\'s UART2 is usually devoted to console access.

To program the Edison to control and interact with the Arduino, you\'ll need to use the UART to establish a communication protocol between the devices. See the next section for an easy example of UART communication between Arduino and Edison.

## Controlling the Arduino Block with Firmata

Firmata is an [established protocol](https://github.com/firmata/protocol) popular within the Arduino realm for applications that require a separate machine (usually a computer) to control the Arduino. It\'s a serial-based protocol that uses defined messages to set digital pins, read analog pins, and do everything else you\'re used to with Arduino.

Firmata is so useful, the standard Arduino IDE even ships with the Firmata library. Here\'s an example of how an Edison can be used to control and interact with an Arduino running Firmata.

### Upload StandardFirmata to the Arduino

Before uploading any code to the Edison, let\'s load something into the Arduino. Once the Firmata code is running on your Arduino, you may never have to upload code to it again.

Using the standard Arduino IDE (i.e. *not* the IDE built for Edison), load up the \"StandardFirmata\" sketch by going to **File** \> **Examples** \> **Firmata** \> **StandardFirmata**.

    language:c
        /*
     * Firmata is a generic protocol for communicating with microcontrollers
     * from software on a host computer. It is intended to work with
     * any host computer software package.
     *
     * To download a host software package, please clink on the following link
     * to open the download page in your default browser.
     *
     * http://firmata.org/wiki/Download
     */

    /*
      Copyright (C) 2006-2008 Hans-Christoph Steiner.  All rights reserved.
      Copyright (C) 2010-2011 Paul Stoffregen.  All rights reserved.
      Copyright (C) 2009 Shigeru Kobayashi.  All rights reserved.
      Copyright (C) 2009-2011 Jeff Hoefs.  All rights reserved.

      This library is free software; you can redistribute it and/or
      modify it under the terms of the GNU Lesser General Public
      License as published by the Free Software Foundation; either
      version 2.1 of the License, or (at your option) any later version.

      See file LICENSE.txt for further informations on licensing terms.

      formatted using the GNU C formatting and indenting
    */

    /* 
     * TODO: use Program Control to load stored profiles from EEPROM
     */

    #include <Servo.h>
    #include <Wire.h>
    #include <Firmata.h>

    // move the following defines to Firmata.h?
    #define I2C_WRITE B00000000
    #define I2C_READ B00001000
    #define I2C_READ_CONTINUOUSLY B00010000
    #define I2C_STOP_READING B00011000
    #define I2C_READ_WRITE_MODE_MASK B00011000
    #define I2C_10BIT_ADDRESS_MODE_MASK B00100000

    #define MAX_QUERIES 8
    #define MINIMUM_SAMPLING_INTERVAL 10

    #define REGISTER_NOT_SPECIFIED -1

    /*==============================================================================
     * GLOBAL VARIABLES
     *============================================================================*/

    /* analog inputs */
    int analogInputsToReport = 0; // bitwise array to store pin reporting

    /* digital input ports */
    byte reportPINs[TOTAL_PORTS];       // 1 = report this port, 0 = silence
    byte previousPINs[TOTAL_PORTS];     // previous 8 bits sent

    /* pins configuration */
    byte pinConfig[TOTAL_PINS];         // configuration of every pin
    byte portConfigInputs[TOTAL_PORTS]; // each bit: 1 = pin in INPUT, 0 = anything else
    int pinState[TOTAL_PINS];           // any value that has been written

    /* timer variables */
    unsigned long currentMillis;        // store the current value from millis()
    unsigned long previousMillis;       // for comparison with currentMillis
    int samplingInterval = 19;          // how often to run the main loop (in ms)

    /* i2c data */
    struct i2c_device_info ;

    /* for i2c read continuous more */
    i2c_device_info query[MAX_QUERIES];

    byte i2cRxData[32];
    boolean isI2CEnabled = false;
    signed char queryIndex = -1;
    unsigned int i2cReadDelayTime = 0;  // default delay time between i2c read request and Wire.requestFrom()

    Servo servos[MAX_SERVOS];
    /*==============================================================================
     * FUNCTIONS
     *============================================================================*/

    void readAndReportData(byte address, int theRegister, byte numBytes)  else 

      Wire.requestFrom(address, numBytes);  // all bytes are returned in requestFrom

      // check to be sure correct number of bytes were returned by slave
      if(numBytes == Wire.available()) 
      }
      else  else 
      }

      // send slave address, register and received bytes
      Firmata.sendSysex(SYSEX_I2C_REPLY, numBytes + 2, i2cRxData);
    }

    void outputPort(byte portNumber, byte portValue, byte forceSend)
    
    }

    /* -----------------------------------------------------------------------------
     * check all the active digital inputs for change of state, then add any events
     * to the Serial output queue using Serial.print() */
    void checkDigitalInputs(void)
    

    // -----------------------------------------------------------------------------
    /* sets the pin mode to the correct state and sets the relevant bits in the
     * two bit-arrays that track Digital I/O and PWM status
     */
    void setPinModeCallback(byte pin, int mode)
    
      if (IS_PIN_SERVO(pin) && mode != SERVO && servos[PIN_TO_SERVO(pin)].attached()) 
      if (IS_PIN_ANALOG(pin)) 
      if (IS_PIN_DIGITAL(pin))  else 
      }
      pinState[pin] = 0;
      switch(mode) 
          pinConfig[pin] = ANALOG;
        }
        break;
      case INPUT:
        if (IS_PIN_DIGITAL(pin)) 
        break;
      case OUTPUT:
        if (IS_PIN_DIGITAL(pin)) 
        break;
      case PWM:
        if (IS_PIN_PWM(pin)) 
        break;
      case SERVO:
        if (IS_PIN_SERVO(pin)) 
        }
        break;
      case I2C:
        if (IS_PIN_I2C(pin)) 
        break;
      default:
        Firmata.sendString("Unknown pin mode"); // TODO: put error msgs in EEPROM
      }
      // TODO: save status to EEPROM here, if changed
    }

    void analogWriteCallback(byte pin, int value)
    
      }
    }

    void digitalWriteCallback(byte port, int value)
    
          }
          mask = mask << 1;
        }
        writePort(port, (byte)value, pinWriteMask);
      }
    }

    // -----------------------------------------------------------------------------
    /* sets bits in a bit array (int) to toggle the reporting of the analogIns
     */
    //void FirmataClass::setAnalogPinReporting(byte pin, byte state) 
    void reportAnalogCallback(byte analogPin, int value)
     else 
      }
      // TODO: save status to EEPROM here, if changed
    }

    void reportDigitalCallback(byte port, int value)
    
      // do not disable analog reporting on these 8 pins, to allow some
      // pins used for digital, others analog.  Instead, allow both types
      // of reporting to be enabled, but check if the pin is configured
      // as analog when sampling the analog inputs.  Likewise, while
      // scanning digital pins, portConfigInputs will mask off values from any
      // pins configured as analog
    }

    /*==============================================================================
     * SYSEX-BASED commands
     *============================================================================*/

    void sysexCallback(byte command, byte argc, byte *argv)
    
        else 

        switch(mode) 
          Wire.endTransmission();
          delayMicroseconds(70);
          break;
        case I2C_READ:
          if (argc == 6) 
          else 
          break;
        case I2C_READ_CONTINUOUSLY:
          if ((queryIndex + 1) >= MAX_QUERIES) 
          queryIndex++;
          query[queryIndex].addr = slaveAddress;
          query[queryIndex].reg = argv[2] + (argv[3] << 7);
          query[queryIndex].bytes = argv[4] + (argv[5] << 7);
          break;
        case I2C_STOP_READING:
          byte queryIndexToSkip;      
          // if read continuous mode is enabled for only 1 i2c device, disable
          // read continuous reporting for that device
          if (queryIndex <= 0)  else 
            }

            for (byte i = queryIndexToSkip; i<queryIndex + 1; i++) 
            }
            queryIndex--;
          }
          break;
        default:
          break;
        }
        break;
      case I2C_CONFIG:
        delayTime = (argv[0] + (argv[1] << 7));

        if(delayTime > 0) 

        if (!isI2CEnabled) 

        break;
      case SERVO_CONFIG:
        if(argc > 4) 
        }
        break;
      case SAMPLING_INTERVAL:
        if (argc > 1)       
        } else 
        break;
      case EXTENDED_ANALOG:
        if (argc > 1) 
        break;
      case CAPABILITY_QUERY:
        Serial.write(START_SYSEX);
        Serial.write(CAPABILITY_RESPONSE);
        for (byte pin=0; pin < TOTAL_PINS; pin++) 
          if (IS_PIN_ANALOG(pin)) 
          if (IS_PIN_PWM(pin)) 
          if (IS_PIN_SERVO(pin)) 
          if (IS_PIN_I2C(pin)) 
          Serial.write(127);
        }
        Serial.write(END_SYSEX);
        break;
      case PIN_STATE_QUERY:
        if (argc > 0) 
          Serial.write(END_SYSEX);
        }
        break;
      case ANALOG_MAPPING_QUERY:
        Serial.write(START_SYSEX);
        Serial.write(ANALOG_MAPPING_RESPONSE);
        for (byte pin=0; pin < TOTAL_PINS; pin++) 
        Serial.write(END_SYSEX);
        break;
      }
    }

    void enableI2CPins()
     
      }

      isI2CEnabled = true; 

      // is there enough time before the first I2C request to call this here?
      Wire.begin();
    }

    /* disable the i2c pins so they can be used for other functions */
    void disableI2CPins() 

    /*==============================================================================
     * SETUP()
     *============================================================================*/

    void systemResetCallback()
    
      for (byte i=0; i < TOTAL_PORTS; i++) 
      // pins with analog capability default to analog input
      // otherwise, pins default to digital output
      for (byte i=0; i < TOTAL_PINS; i++)  else 
      }
      // by default, do not report any analog inputs
      analogInputsToReport = 0;

      /* send digital inputs to set the initial state on the host computer,
       * since once in the loop(), this firmware will only send on change */
      /*
      TODO: this can never execute, since no pins default to digital input
            but it will be needed when/if we support EEPROM stored config
      for (byte i=0; i < TOTAL_PORTS; i++) 
      */
    }

    void setup() 
    

    /*==============================================================================
     * LOOP()
     *============================================================================*/
    void loop() 
    
          }
        }
        // report i2c data for all device with read continuous mode enabled
        if (queryIndex > -1) 
        }
      }
    }

With the Firmata firmware uploaded, you can disconnect the FTDI Basic, and connect the Arduino Block to your Edison stack.

### Edison Firmata for Arduino Client

The harder part of this equation is writing something that executes on the Edison which interacts with our Firmata-running Arduino. There are tons of great client examples in the [Firmata GitHub profile](https://github.com/firmata), but nothing quite built for the Edison.

Riffing on the [Firmata Processing example](https://github.com/firmata/processing/blob/master/src/Firmata.java), we wrote this sketch to enact an Edison Firmata client.

**Arduino version alert!** This Arduino sketch is intended to run on the Edison. You\'ll need to download the [Edison Arduino IDE](http://www.intel.com/support/edison/sb/CS-035180.htm), and use that to upload this code to your Edison. For more help programming the Edison in Arduino, check out our [Getting Started with Edison tutorial](https://learn.sparkfun.com/tutorials/edison-getting-started-guide#programming-the-edison-in-arduino).

Here\'s the sketch. Copy/paste from below, or grab the latest version from [this Gist](https://gist.github.com/jimblom/71a06b6493e5ef927f0c):

    language:c
    /****************************************************************
       Edison Firmata Client
       by: Jim Lindblom @ SparkFun Electronics
       created on: Februrary 12, 2015
       github: 

       This is an Firmata client sketch for the Edison. It can
       communicate with an Arduino running Firmata over a Serial
       connection.

       Support for the following functions is written:
         firmata_init() -- set up firmata and pin reporting
         firmata_pinMode([pin], [0, 1, 2, 3, 4, 5, 6])
         firmata_digitalWrite([pin], [LOW/HIGH])
         firmata_analogWrite([pin], [0-255])
         firmata_analogRead([0-7])
         firmata_digitalRead([pin])
         firmata_servoWrite([pin], [value])

       Development Environment Specifics:
       Arduino 1.5.3 (for Edison)
       Intel Edison rev C
       Arduino Block for Edison
         Arduino should be running StandardFirmata

       This sketch is based on Firmata's processing client:
       https://github.com/firmata/processing
       As such, it is released under the same, free license. You can 
       redistribute it and/or modify it under the terms of the GNU 
       Lesser General Public License as published by the Free 
       Software Foundation; either version 2.1 of the License, or 
       (at your option) any later version.

       Distributed as-is; no warranty is given. 
    ****************************************************************/
    // SerialEvent1 isn't defined in the Edison core (I think).
    // To get some form of interrupt-driven Serial input, we'll read
    // serial in on a timer.
    #include <TimerOne.h>

    #define MAX_DATA_BYTES 4096
    #define MAX_PINS 128

    // Pin Mode definitons:
    // Use any of these six values to set a pin to INPUT, OUTPUT,
    // ANALOG, PWM, SERVO, SHIFT, or I2C.
    enum const_pin_mode ;

    // Message Types
    // Used by the low-level Firmata functions to set up the 
    // Firmata messages.
    #define ANALOG_MESSAGE  0xE0
    #define DIGITAL_MESSAGE 0x90
    #define REPORT_ANALOG   0xC0
    #define REPORT_DIGITAL  0xD0
    #define START_SYSEX     0xF0
    #define SET_PIN_MODE    0xF4
    #define END_SYSEX       0xF7
    #define REPORT_VERSION  0xF9
    #define SYSTEM_RESET    0xFF

    // Extended Commands:
    // Used by the low-level Firmata functions to set up the 
    // Firmata messages.
    #define SERVO_CONFIG            0x70
    #define STRING_DATA             0x71
    #define SHIFT_DATA              0x75
    #define I2C_REQUEST             0x76
    #define I2C_REPLY               0x77
    #define I2C_CONFIG              0x78
    #define EXTENDED_ANALOG         0x6F
    #define PIN_STATE_QUERY         0x6D
    #define PIN_STATE_RESPONSE      0x6E
    #define CAPABILITY_QUERY        0x6B
    #define CAPABILITY_RESPONSE     0x6C
    #define ANALOG_MAPPING_QUERY    0x69
    #define ANALOG_MAPPING_RESPONSE 0x6A
    #define REPORT_FIRMWARE         0x79
    #define SAMPLING_INTERVAL       0x7A
    #define SYSEX_NON_REALTIME      0x7E
    #define SYSEX_REALTIME          0x7F

    // Flags and variables to keep track of message reading status:
    boolean parsingSysex = false;
    int waitForData = 0;
    int storedInputData[MAX_DATA_BYTES];
    int sysexBytesRead = 0;
    int executeMultiByteCommand = 0;
    int multiByteChannel = 0;
    // Variable arrays to keep track of pin values read in.
    int digitalInputData[] = ;
    int analogInputData[] = ;
    int analogChannel[MAX_PINS];
    boolean blinkFlag = false;

    void setup()
    

    void loop() 
    
      else
      

    }

    ///////////////////////////////////
    // Upper Level Firmata Functions //
    ///////////////////////////////////
    // Firmata functions that you should use in your sketch above.
    // If this was a class, these'd be public functions.

    // firmata_init() -- 
    // - Initialize our Firmata Serial port. 
    // - Set up a timer to read in Serial messages outside of loop().
    // - Configure our Firmata Arduino to report all digital outputs
    // - Configure our Firmata Arduino to report all analog outputs
    void firmata_init()
    
      // This function will check for analog channels and set them
      // to REPORTING
      firmata_queryAnalogMapping();
    }

    // firmata_digitalRead([pin]) --
    // - Returns the latest digital input value we've read on the
    //   requested pin.
    // - digitalInputData[] is updated in firmata_processInput()
    //   as serial messages come in.
    int firmata_digitalRead(int pin)
    

    // firmata_analogRead([pin])
    // - Returns the latest analog value we've read on the requested
    //   pin.
    // - analogInputData[] is updated in firmata_processInput()
    //   as serial messages come in.
    int firmata_analogRead(int pin)
    

    // firmata_pinMode([pin], [mode])
    // - Set an Arduino pin to input, output, analog in, PWM, servo,
    //   shift register, or i2c.
    // - [pin] - can be any Arduino pin 0-13, A0-A7
    // - [mode] - should be one of these defined values:
    //          - MODE_INPUT  - Digital input
    //          - MODE_OUTPUT - Digital output
    //          - MODE_ANALOG - Analog input
    //          - MODE_PWM    - Analog output
    //          - MODE_SERVO  - Servo output
    //          - MODE_SHIFT  - Shift register output
    void firmata_pinMode(int pin, int mode)
    

    // firmata_digitalWrite([pin], [value])
    // - Set an Arduino digital pin to HIGH or LOW
    // - [pin] - Any digital pin 0-18
    // - [value] - LOW or HIGH
    void firmata_digitalWrite(int pin, int value)
    

    // firmata_analogWrite([pin], [value])
    // - Set an Arduino pin - CONFIGURED AS PWM (!) - to an
    //   analog output value.
    // - [pin] - Any analog output capable pin (3, 5, 6, 9, 10, 11
    // - [value] - 0-255
    void firmata_analogWrite(int pin, int value)
    

    // firmata_servoWrite([pin], [value])
    // - Set an Arduino pin - CONFIGURED AS SERVO (!) - to output
    //   a servo signal.
    void firmata_servoWrite(int pin, int value)
    

    /////////////////////////////////
    // Low level Firmata functions //
    /////////////////////////////////
    // Firmata helper functions you probably won't need to call in
    // your sketch. If this was a class, these'd be private functions.

    // checkSerial()
    // Interrupt-recurring function. Checks for available serial data
    // and processes any serial messages that come in.
    void checkSerial()
    
      if (blinkFlag)
      
      else
      
    }

    // firmata_processInput([inputData])
    // Handles all Firmata messages - everything from version checks
    // to analog and digital readings.
    void firmata_processInput(unsigned char inputData)
    
        else
        
      }
      else if (waitForData > 0 && inputData < 128)
      
        }
      }
      else // Beginning of a message
      
        else
        
        switch (command)
        
      }
    }

    // firmata_processSysexMessage()
    // - Process a system message.
    // - Mostly just handles defining which pins are analog channels.
    void firmata_processSysexMessage()
    
        }
        break;
      }
    }

    // firmata_queryAnalogMapping()
    // - Send the ANALOG_MAPPING_QUERY request message.
    // - Called in init to keep track of which pins are analog ins
    void firmata_queryAnalogMapping()
    

    // firmata_setDigitalInputs()
    // - Set a value in the digitalInputData array to portData
    void firmata_setDigitalInputs(int portNumber, int portData)
    

    // firmata_setAnalogInput
    // - Set an analog pin value to [value].
    void firmata_setAnalogInput(int pin, int value)
    

    void firmata_setVersion(int majorVersion, int minorVersion)
    

After uploading that sketch to your Edison, your Arduino Block should begin blinking the D13 pin. You can also open up the Serial Monitor to see what values your Arduino Block is reading in on D4 and A0.

This serves as a simple Firmata client for the Edison, but it should be easily expandable. Try using any of these functions (defined in lower portions of the sketch) to add more features to your Edison Firmata Client:

- **`firmata_pinMode([pin], [mode])`** \-- As with any Arduino sketch, setting the pin\'s mode is critical. Firmata requires an extra bit of information. Use any Arduino pin for the `[pin]` variable. For the `[mode]` variable use either `MODE_INPUT`, `MODE_OUTPUT`, `MODE_ANALOG`, `MODE_PWM`, `MODE_SERVO`, or `MODE_SHIFT`.
- **`firmata_digitalRead([pin])`** \-- Read in the digital value of a pin. This function will return a value between 0 and 1. That pin should be set as `MODE_INPUT` before calling this function.
- **`firmata_analogRead([pin])`** \-- Read in the value of an anlog pin. This function will return a value between 0 and 1023. The pins should be set as `MODE_ANALOG` before being read.
- **`firmata_digitalWrite([pin], [value])`** \-- Write a digital pin either HIGH or LOW. The pin should be set as `MODE_OUTPUT` before calling the function.
- **`firmata_analogWrite([pin], [value])`** \-- Write an analog-output pin to a value between 0 and 255. The pin must be PWM-capable \-- that means either pin 3, 5, 6, 9, 10, or 11. And it should be configured as a `MODE_PWM` before hand.
- **`firmata_servoWrite([pin], [value])`** \--Set a pin to output a servo signal. The value here is an angle between 0 and whatever the high-end angle of your servo is. Remember to set the pin to `MODE_SERVO` before calling this function!

------------------------------------------------------------------------

Don\'t feel like you have to user Firmata when using the Arduino block with your Edison. It\'s a great place to start, though, if you\'re looking for a simple communication protocol over the serial interface.