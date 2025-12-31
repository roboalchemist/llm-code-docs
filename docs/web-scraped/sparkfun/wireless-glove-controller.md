# Source: https://learn.sparkfun.com/tutorials/wireless-glove-controller

## Introduction

In this tutorial, we will build a wireless glove controller with Arduino to trigger an LED remotely using XBees!

[![Full Demo](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_RGB_LEDs_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_RGB_LEDs_Demo.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need wire, wire strippers, a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### You Will Also Need

- Glove
- Scissors
- Non-Conductive Thread
- Tape

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/ldk-experiment-5-make-your-own-switch)

### LDK Experiment 5: Make Your Own Switch 

Learn to create and integrate your own handmade switch into an e-textile circuit.

[](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide)

### XBee Shield Hookup Guide 

How to get started with an XBee Shield and Explorer. Create a remote-control Arduino!

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

## Understanding Your Circuit

### [][Wireless Glove Controller](#v1)

The simplest form of input is a button press, so we\'ll control LEDs remotely using buttons for this project as shown in the diagram below.

[![Circuit Diagram Transmitting XBee](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wearable_XBee_Wireless_Glove_Controller_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wearable_XBee_Wireless_Glove_Controller_Fritzing_bb.jpg)

#### Custom Button

Since the electronics are going on a glove, the usual momentary button won\'t be the most comfortable on the fingers. Instead, we\'ll make our own custom button using snappable pins, conductive thread, and wire. You\'ll need to make a contact between your thumb, middle, ring, and pinky to GND, pin 4, pin 11, and pin 12, respectively.

**Note:** Connecting all four snappable pins is entirely optional if you are looking to control something with more than one mode. Depending on your project, you may just need two snappable pins for a button press. The conductive thread shown in the grey/white \"wire\" is also optional. If you are moving around with the glove (i.e. dancing with your hands on the floor), I\'ve found that conductive thread was the best at preventing damage between the snappable pin that is attached to the fingers as opposed to [soldering wire](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) directly.

#### LEDs

For feedback to indicate that we have sent a character wirelessly, we\'ll solder an LED and 330Ω [current limiting resistor](https://learn.sparkfun.com/tutorials/resistors/example-applications#current-limiting) to the protoboard between pin 13 and ground. You could use the on-board LED on the RedBoard but it would be harder to see under the shield. Additionally, we\'ll attach a [diffused, common cathode RGB LED](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-1d-rgb-night-light#common_cathode_RGB_LED) to pins 5, 6, and 9. Make sure to add a second 330Ω current limiting resistor between the common cathode and GND, respectively.

**Note:** The RGB LED is also optional. However, I\'ve found that it is a useful indicator when [controlling a robot remotely](https://learn.sparkfun.com/tutorials/wireless-gesture-controlled-robot) or controlling EL Wire with a pattern using the [EL Sequencer](https://learn.sparkfun.com/tutorials/el-sequencerescudo-dos-hookup-guide#going-wireless). Additionally, each color in the RGB LED has a different specification. To balance the colors, you may want to use different resistors so that red is not saturating the other two colors when color mixing.

------------------------------------------------------------------------

### Receiving XBee Node

For the receiving XBee, we\'ll just mimic the LEDs used for feedback on the glove. The circuit is the same, that is without the custom buttons as shown in the diagram below. The board is flipped over to illustrate the receiving XBee node.

[![Circuit Diagram Receiving XBee](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Receiving_XBee_Wireless_RGB_Fritzing_bb_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Receiving_XBee_Wireless_RGB_Fritzing_bb_2.jpg)

------------------------------------------------------------------------

## Hardware Hookup

### Modify the XBee Shield

Using the circuit diagram from earlier, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the components to the XBee shield. Then [strip solid core hook-up wire](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire) and solder them between the pins. If you are following along, your board should look similar to the images below.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Modified XBee Wireless Shield](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_XBee3_Arduino_Shield.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_XBee3_Arduino_Shield.jpg)   [![Bottom View of XBee Wireless Shield](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_XBee_Shield_Modified.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_XBee_Shield_Modified.jpg)
  *Top View Components Soldered on XBee Shield*                                                                                                                                                                                                                        *Bottom View with Wires and Jumpers*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** For my application, I decided to use two stackable female headers and two rows of male headers. Depending on your preference and what you have, you could just use all four stacakable headers or male headers.

### Making a Connection Between Hard to Soft Materials

Grab four 12\" F/F jumper wires of different colors and cut them in half. At this point, we\'ll need solder a wire loop from the standed wire so that we can easily connect the conductive thread to each of the finger\'s snappable pins. The other option is to thread the stranded wire through one of the holes on the snappable pin and solder them together.

[![Hard to Soft Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/ETextiles_Wearables_Wire_Loop_Hard-To-Soft_Connection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/ETextiles_Wearables_Wire_Loop_Hard-To-Soft_Connection.jpg)

### Securing the Boards and Wires to the Glove

When you are finished, grab a needle, thread the non-conductive thread through the eye, and sew the RedBoard\'s mounting holes to the glove of your choice. I found that three of the holes was sufficient enough. Make sure to not sew the top and bottom of the glove together. Stack a [configured XBee](https://learn.sparkfun.com/tutorials/wireless-glove-controller#configuring-xbees), XBee shield, and RedBoard together. Then insert the female housing into the right angle headers of the shield.

[Braid the wires together](https://learn.sparkfun.com/tutorials/working-with-wire#wire-management) and secure it to the glove using some non-conductive thread. For each wire, you will need to separate the wires as it gets closer to the fingers. Make sure there is enough space between the board and connections so that the board is not pressing against the wires. Test it out to ensure that there is enough tolerance so that the wires do not get damaged when the hand is moving.

[![Sew RedBoard and Wires to the Glove Using Non-Conductive Thread](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Secure_Wires_Boards.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Secure_Wires_Boards.jpg)

### Sewing the Custom Buttons

To make a connection to the snappable pins using conductive thread, we\'ll need to use a small needle. The two small needles provided in the [needle set](https://www.sparkfun.com/products/10405) will be needed to sew the pin down. Find a spot for the snappable pin to make contact with the other finger. We\'ll start with the thumb. Grab the small needle, [thread the conductive thread](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing#sewing-with-conductive-thread) through the needle\'s eye, and sew the pin down. Sewing one of the four holes with conductive fabric should be sufficient enough if you loop it a few times. You could use non-conductive thread on the remaining holes. Again, avoid sewing the top and bottom fabric together.

[![Sew Female Snap Pin with Conductive Thread and Connect with the Wire\'s Loop](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Conductive_Thread_Snappable_Pin_Custom_Button.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Conductive_Thread_Snappable_Pin_Custom_Button.jpg)

After a few loops around the the snappable pin\'s hole, make a running stitch to the top of the hand and make a connection to the wire loop to the respective pin connection. Following the circuit diagram, the thumb should be connected to the GND wire. Tie and cut off any excess thread.

[![Connecting to a Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Conductive_Thread_Wire_Loop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Conductive_Thread_Wire_Loop.jpg)

Repeat for each snappable pin.

[![Snap (Metal Poppers) Pins Sewed on Glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Bottom_View.jpg)

**Note:** I decided to use an old bike glove that was worn down on the finger tips. Since I was using the glove to control a few suits while dancing on the floor, part of the fingertips were cut off for a better grip.

### Assembled Wireless Glove Controller

When finished, your glove should look like the images below! Feel free to click on the images for a closer look.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View of Assembled Wireless Glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Top_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Top_View.jpg)   [![Bottom View of Assembled Wireless Glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Bottom_View.jpg)
  *Top View*                                                                                                                                                                                                                                        *Bottom View*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you decide to use the glove remotely, add a 9V battery and secure it to the glove. In this case, electrical tape was used to hold the battery to the board. Feel free to sew together a [9V battery pouch](https://www.kobakant.at/DIY/?p=52) to the glove for a more secure method.

[![Glove with Battery Secured](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Secured.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Secured.jpg)

## Configuring XBees

To configure the XBees, we will be using the XBee Series 1 firmware. It is recommended to configure each XBee using the XBee Explorer USB.

[![XBee Inseted int XBee Explorer USB to Configure ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/8/XBee_3_Explorer_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/8/XBee_3_Explorer_USB.jpg)

If you have not already, check out the [Starting with XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu#starting-with-x-ctu) section under Exploring XBees and XCTU to configure your XBees. If you are using an XBee 3, make sure to configure the firmware with the Series 1 firmware to follow along with this tutorial.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

March 12, 2015

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

### Point-to-Point Configuration

For simplicity, we will be sending commands with the XBees in transparent mode set for a point-to-point configuration. Make sure to configure each XBee with a unique MY address if there are more than two XBees in your CH and PAN ID. You will then need to adjust the DL address for each respective XBee.

  --------------------------------------------------------------------------------------------------------
  Setting                    Acronym           Transmitting XBee Node 1\     Receiving XBee Node 2\
                                               (Wireless Glove Controller)   (i.e. LED/Robot/Dance Suit)
  -------------------------- ----------------- ----------------------------- -----------------------------
  Channel                    CH                C                             C

  PAN ID                     ID                3333                          3333

  Destination Address High   DH                0                             0

  Destination Address Low    DL                1                             0

  16-bit Source Address      MY                0                             1
  --------------------------------------------------------------------------------------------------------

## Example 1: Sending and Receiving

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)\
\
If you\'ve never connected an FTDI device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our [How to Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) tutorial for help with the installation.

### Example 1a: Sending a Character with the Glove

In this part of the example, we\'ll have the glove send a character when a button is pressed. While you could just [open a serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) to check if characters were received during testing, it would just not be as fun as blinking an LED wirelessly after a button press.

Copy the code, paste it into the Arduino IDE, select your board (**Arduino/Genuino Uno**), and COM port. Then upload the code to the glove.

    language:c
    // We'll use SoftwareSerial to communicate with the XBee:

    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    //Send
    const int button1Pin = 4; //push button
    const int status_LED = 13;  //LED on the push button

    char send_CHAR = 'A'; //default send character

    //initialize variables to read buttons
    int button1State;

    //variables to check for button1 state
    boolean prev_button1State = false;
    boolean current_button1State = false;

    /*******************Setup Loop***************************/
    void setup() 

      //Declare serial connections for debugging
      Serial.begin(9600);
      Serial.println("Arduino Serial Ready");

      XBee.begin(9600);
      Serial.println("Glove Controller's XBee Ready to Communicate");

    }//end setup()

    void loop() 
        else 
        prev_button1State = current_button1State;
      }

      //button has not been pressed, it will be high again
      else 
    }//end loop()

### Example 1b: Receiving XBee Node

In this part of the code, we\'ll have the receiving XBee blinking the LED connected to pin 13 as well. Copy the code below, paste it into the Arduino IDE, select your board (**Arduino/Genuino Uno**), and COM port. The Arduino should enumerate on a different COM port so make sure to adjust the COM port. Then upload the code to the receiving XBee\'s Arduino.

    language:c

    // We'll use SoftwareSerial to communicate with the XBee:

    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    //Declare character 'c_data'
    char c_data;

    //LED to check if the LED is initialized.
    const int status_LED = 13;

    /*******************Setup Loop***************************/
    void setup() 

      //Declare serial connections for debugging
      Serial.begin(9600);
      Serial.println("Arduino Serial Ready");

      XBee.begin(9600);
      Serial.println("XBee Ready to Receive");

    }//end setup()

    void loop() 

        else if (Serial.available()) 

        //Check to see if character sent is letter A
        if (c_data == 'A') 

        else 
      }
      delay(100);
      digitalWrite(status_LED, LOW); //turn OFF Status LED

    }//end loop()

### What You Should See

After uploading, touch the metal snap pins between your thumb and middle finger. This should send one character from the glove to the receiving XBee. As a result, the LED on the glove will stay on as long as the button is pressed. The receiving XBee\'s LED will blink whenever a character is received. As part of the design, we\'ll only send a character once when the button is pressed. To send another character, move your thumb away from the middle finger and then touch the metal snap pins together again.

[![Glove Wirelesly Controlling an LED](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_LED.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_LED.gif)

## Example 2: Controlling an RGB LED

### Example 2a: RGB Wireless Glove Controller

We\'ll build on the first example and have the glove a send character to control an RGB LED. We\'ll use the snappable pins on the ring and pinky to switch between the colors.

**Note:** Having the RGB LED is useful for feedback if you happen to have more than one character that you want to send. I found this useful to indicate what character was about to be sent before broadcasting it out and activating a certain sequence with each of my student\'s dance suits.

Copy the code, paste it into the Arduino IDE, select your board (**Arduino Uno**), and COM port. Make sure to switch the COM port back what the glove enumerated to before uploading. When ready, upload the code to the glove.

    language:c
    // We'll use SoftwareSerial to communicate with the XBee:

    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    //SEND Button
    const int button1Pin = 4; //push button
    const int status_LED = 13;  //LED on the push button

    char send_CHAR = 'A'; //default send character

    //initialize variables to read buttons
    int button1State;

    //variables to check for button1 state
    boolean prev_button1State = false;
    boolean current_button1State = false;

    //UP Button
    const int button2Pin = 11; //push button

    int button2State;
    boolean prev_button2State = false;
    boolean current_button2State = false;

    //DOWN Button
    const int button3Pin = 12;

    int button3State;
    boolean prev_button3State = false;
    boolean current_button3State = false;

    //LED Status Indicator
    int ledR = 5;//hardware PWM
    int ledG = 6;//hardware PWM
    int ledB = 9; //hardware PWM

    int pattern = 0; //pattern

    /*******************Setup Loop***************************/
    void setup() 

      // initialize the digital pins as an output for LEDs
      pinMode(ledR, OUTPUT);
      pinMode(ledG, OUTPUT);
      pinMode(ledB, OUTPUT);

      sequenceTest();//visually initialization

      //Declare serial connections for debugging
      Serial.begin(9600);
      Serial.println("Arduino Serial Ready");

      XBee.begin(9600);
      Serial.println("Glove Controller's XBee Ready to Communicate");

    }//end setup()

    void loop() 
        else 
        prev_button1State = current_button1State;
      }//-----------End Check for SENT Button----------

      //button has not been pressed, it will be high again
      else //-----------End Check for SENT Button----------

      //-----------Check If UP Button Has Been Pressed----------
      if (button2State == LOW) 

        }
        else 
        prev_button2State = current_button2State;
      }
      //UP button has not been pressed, it will be high
      else //-----------End Check for Up Button----------

      //-----------Check If DOWN Button Has Been Pressed----------
      if (button3State == LOW) 
        }
        else 
        prev_button3State = current_button3State;
      }
      //button has not been pressed, it will be high
      else //-----------End Check for DOWN Button----------

      delay(50);

      //save send character into variable depending on button press and change status LED
      switch (pattern) //end switch

    }//end loop()

    /*
      Check out the Venn Diagram on Basic Color Mixing:
      https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/2-basic-color-mixing

    */

    void redON() 

    void magentaON() 

    void blueON() 

    void cyanON() 

    void greenON() 

    void yellowON() 

    void allOFF() 

    void allON() 

    void sequenceTest() 

### Example 2b: RGB Receiving XBee Node

In this part of the example, we\'ll mimic the color being sent from the glove. Copy the code, paste it into the Arduino IDE, select your board (**Arduino Uno**), and COM port. Make sure to switch the COM port back to the receiving XBee\'s Arduino before uploading. When ready, upload the code to the receiving XBee\'s Arduino.

    language:c
    // We'll use SoftwareSerial to communicate with the XBee:

    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    //Declare character 'c_data'
    char c_data;

    //LED to check if the LED is initialized.
    const int status_LED = 13;

    //LED Status Indicator
    int ledR = 5;//hardware PWM
    int ledG = 6;//hardware PWM
    int ledB = 9; //hardware PWM

    /*******************Setup Loop***************************/
    void setup() 

      // initialize the digital pins as an output for LEDs
      pinMode(ledR, OUTPUT);
      pinMode(ledG, OUTPUT);
      pinMode(ledB, OUTPUT);

      sequenceTest();//visually initialization

      //Declare serial connections for debugging
      Serial.begin(9600);
      Serial.println("Arduino Serial Ready");

      XBee.begin(9600);
      Serial.println("XBee Ready to Receive");

    }//end setup()

    void loop() 

        else if (Serial.available()) 

        //Check to see if character sent is letter A
        if (c_data == 'A') 

        else if (c_data == 'B') 

        else if (c_data == 'C') 

        else if (c_data == 'D') 

        else if (c_data == 'E') 
        else if (c_data == 'F') 
        else if (c_data == 'G') 
        else if (c_data == 'H') 
        else 
      }

      delay(100);
      digitalWrite(status_LED, LOW); //turn OFF Status LED

    }//end loop()

    /*
      Check out the Venn Diagram on Basic Color Mixing:
      https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/2-basic-color-mixing

    */

    void redON() 

    void magentaON() 

    void blueON() 

    void cyanON() 

    void greenON() 

    void yellowON() 

    void allOFF() 

    void allON() 

    void sequenceTest() 

### What You Should See

By using the thumb to make contact with either the ring and pinky\'s snappable pin, the RGB LED will switch between colors. Pressing on the thumb and middle finger will send a character associated with the RGB LED. The receiving XBee should mimic the color of the RGB LED whenever a character is sent.

[![Glove Wirelessly Controlling an RGB LED](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_RGB_LEDs_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/9/Wireless_Glove_Controller_Button_RGB_LEDs_Demo.gif)