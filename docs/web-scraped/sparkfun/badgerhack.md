# Source: https://learn.sparkfun.com/tutorials/badgerhack

## Introduction

[![The Badger](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/badgerboard-02_tag.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/badgerboard-02_tag.png)

What you hold in your hands is a powerful piece of technology. OK, it\'s no [tricorder](http://en.wikipedia.org/wiki/Tricorder), but it can do some pretty cool stuff. You can program the BadgerStick (the thin board) to control a myriad of electronics, like buttons, lights, and LCDs. The LED board can be used to display patterns or show text.

In the first section of this guide, we will show you how to solder headers on to your BadgerStick and LED board to make a complete badge.

[![Completed badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-33.jpg)

On top of a sweet badge, you also get a development platform that you can use in lots of other projects. Once you have put your badge together, worn it with pride, and shown if off to everyone, you can remix it and make your own project!

The rest of the guide will focus on hacking your badge: how you can create your own graphics or add other electronics to make it do cool stuff.

[![Playing games on my BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-42.jpg)

### Suggested Reading

If you are new to soldering or electronics, we highly recommend you check out the following:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [What is Electricity](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

When you are ready to start hacking your badge, we definitely recommend reading:

- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

## Make Your Badge

Now that you have the Badger kit, let\'s make a badge! When we ask you to solder a pin, you will want to keep a few tips in mind (click for larger image):

[![SparkFun Soldering Tips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/tips.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Soldering_Tips_lg.png)

If you need a refresher on how to solder, we recommend the [How to Solder guide](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering).

### 1. Solder the 8-pin male header to the LED board

Insert the 8-pin male header into the LED board with the pin ends facing out. Note that the pins are coming out of the top of the board (the side with the LEDs).

[![Put the male header into the LED board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-02.jpg)

Flip the board over and solder all the pins.

[![Solder the male header to the LED board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-03.jpg)

### 2. Solder the 8-pin female header to pins 2-9 on the BadgerStick

Insert the 8-pin female header into the holes labeled **2, 3, 4, 5, 6, 7, 8, 9** on the BadgerStick. Make sure that the pins are coming out of the top of the board (the side with all the electronics).

[![Put the female header into the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-04.jpg)

Flip the board over, and ensure that only the holes in the white box labeled \"LED Array\" are used. Solder all 8 pins.

[![Solder the female header to the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-05.jpg)

### 3. Solder the 3-pin female header to the game port on the BadgerStick

Insert the 3-pin female header into the holes labeled **TX**, **GND**, **RX** on the bottom of the board. The header should be coming out of the top of the board.

[![Put the 3-pin female header into the game port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-06.jpg)

Flip the board over, and solder all 3 pins.

[![Solder the 3-pin header to the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-07.jpg)

### 4. Solder the the red battery wire to the + battery pin (VBAT)

Poke the red battery wire through the backside of the BadgerStick on the pin labeled VBAT (\"+\" on the backside).

[![Red wire through the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-08.jpg)

Solder the red wire to the hole.

[![Solder the red wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-09.jpg)

### 5. Solder the black battery wire to the - battery pin (GND)

Poke the black battery wire through the backside of the BadgerStick on the pin labeled GND (\"-\" on the backside).

[![Black wire through the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-10.jpg)

Solder the black wire to the hole.

[![Solder the black wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-11.jpg)

Flip the BadgerStick over, and verify that the red wire is going to the hole labeled \'+\' on the underside and that the black wire is going to the hole labeled \'-\'.

[![Battery wires going into the BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-13.jpg)

### 6. Add batteries

Using a Phillips screwdriver, remove the screw from the battery pack.

[![Use a screwdriver to open the battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-14.jpg)

Open the battery pack cover, and take note of the battery markings in the pack.

[![Markings in battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-16_annotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-16_annotated.jpg)

Put the batteries in the pack as noted by the markings. The bumped end of the battery is + and the flat end is -.

[![Batteries in battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-17.jpg)

Put the battery pack cover back on, and secure it with the screw.

[![Closed battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-18.jpg)

### 7. Connect the LED board to the BadgerStick

Connect the LED board and BadgerStick, by sliding the headers together. Ensure the LEDs and electronics on the BadgerStick are facing the same direction.

[![Connected LED board to BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-19.jpg)

Flip the boards over, and double-check your solder connections:

- 8-pin male header soldered to the pins in the white box on the LED board
- 8-pin female header soldered to the pins in the white box on the BadgerStick labeled \"LED Array\"
- 3-pin female header soldered to the pins in the white box on the BadgerStick labeled \"Game Port\"
- Red battery wire soldered to + Battery pin
- Black battery wire soldered to the - Battery pin

[![Back of completed badge electronics](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-20.jpg)

Before you stick your electronics to the badge, turn on the battery pack to make sure everything is working. Troubleshooting your board will be a lot easier if it\'s not adhered to the badge.

### 8. Affix the components to the badge

Add one piece of double-sided foam tape to the LED board and another piece to the BadgerStick.

[![Add tape to LED board and BadgerStick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-21.jpg)

Add another two pieces of foam tape on top of the existing foam tape.

[![Add another layer of tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-22.jpg)

Stick the LED board and BadgerStick to the front of the plastic badge.

[![Put electronics on badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-23.jpg)

Put one more piece of foam tape on the battery pack on the side with the screw.

[![Tape on the battery pack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-24.jpg)

Stick the battery pack to the back of the plastic badge. To prevent the wires from hanging out, wrap them around the side of the badge as in the picture.

[![Battery pack on badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-25.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-25.jpg)

### 9. Turn it on

Turn your badge over, and find the little switch on the battery pack. Flip it to \"ON.\"

[![Fire it up!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-26.jpg)

Flip your badge back over. Wait about 3 seconds, and you should see the LED matrix activate!

[![Light it up!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-33.jpg)

### 10. Badger it up!

You are now the proud owner of a SparkFun Badger badge! Attach a lanyard\...

[![Attach a lanyard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-27.jpg)

\...and wear it with pride.

[![Wearing the Badger](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/9/Badgerhack_Hookup_Guide-39.jpg)

## Hack Your Badge

What do you do with your badge after the event? Well, you can hack it!

**IMPORTANT:** If you received your BadgerHack kit on or before **September 1, 2015**, you likely have an old bootloader that needs to be updated in order to follow the steps below. You can either: **A)** Follow [this tutorial](https://www.hackster.io/tzikis/programming-an-old-badgderstick) to program your old BadgerStick or **B)** Follow the directions [here](https://www.hackster.io/tzikis/programming-a-badgerstick) to connect another Arduino (Arduino as ISP) to the BadgerStick (Arduino to be programmed) and burn the new bootloader

### Install the BadgerStick Drivers into the Arduino IDE

Install the Arduino IDE, and download the BadgerStick Repository.

Unzip the files, and copy the \"badgerstick\" directory into `$Arduino Installation Directory/hardware`. Restart Arduino, and you should see \"BadgerStick\" as an available board under \"Tools -\> Board\".

### Example 1: Hello World

You will need to install the LED Array 8x7 Arduino Library into your IDE in order to use the following examples.

[Download SparkFun LED Array 8x7 Arduino Library](https://github.com/sparkfun/SparkFun_LED_Array_8x7_Arduino_Library/archive/master.zip)

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Plug your BadgerStick into an available USB port. Make sure \"BadgerStick\" and the associated COM port are selected in the Arduino IDE. Upload the following `ScrollText.ino` sketch to your BadgerStick.

    language:c
        /****************************************************************
    ScrollText.ino
    LED Array 8x7 Charlieplex
    Shawn Hymel @ SparkFun Electronics
    February 3, 2015
    https://github.com/sparkfun/LED_Array_8x7_Charlieplex

    Scrolls text across the LED array for 10 seconds.

    Hardware Connections:

    IMPORTANT:  The Charlieplex LED board is designed for 2.0 - 5.2V!
                Higher voltages can damage the LEDs.

     Arduino Pin | Charlieplex Board
     ------------|------------------
          2      |         A
          3      |         B
          4      |         C
          5      |         D
          6      |         E
          7      |         F
          8      |         G
          9      |         H

    Resources:
    Include Chaplex.h, SparkFun_LED_8x7.h
    The Chaplex library can be found at: 
    http://playground.arduino.cc/Code/Chaplex

    Development environment specifics:
    Written in Arduino 1.6.7
    Tested with SparkFun RedBoard and BadgerStick (Interactive Badge)

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).

    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.

    Distributed as-is; no warranty is given.
    ****************************************************************/

    #include <SparkFun_LED_8x7.h>
    #include <Chaplex.h>

    // Global variables
    static byte led_pins[] = ; // Pins for LEDs

    void setup() 

    void loop() 

Your badge should scroll \"Hello: Let\'s Scroll!.\"

[![Hello World on BadgerHack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/6/Badgerhack_Hookup_Guide-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/6/Badgerhack_Hookup_Guide-35.jpg)

Now the fun begins! Edit the string \"Let\'s Scroll!\" on line 65 to say your name (don\'t forget the quotes!). Run it on the BadgerStick and watch your name scroll across the LEDs.

### Example 2: Shapes

Once you have had enough scrolling text, try making some shapes. Upload the \`DrawShapes.ino\' sketch to the BadgerStick.

    language:c
        /****************************************************************
    DrawShapes.ino
    LED Array 8x7 Charlieplex
    Shawn Hymel @ SparkFun Electronics
    February 9, 2015
    https://github.com/sparkfun/LED_Array_8x7_Charlieplex

    Draws lines, rectangles, and circles on the LEDs.

    Hardware Connections:

    IMPORTANT:  The Charlieplex LED board is designed for 2.0 - 5.2V!
                Higher voltages can damage the LEDs.

     Arduino Pin | Charlieplex Board
     ------------|------------------
          2      |         A
          3      |         B
          4      |         C
          5      |         D
          6      |         E
          7      |         F
          8      |         G
          9      |         H

    Resources:
    Include Chaplex.h, SparkFun_LED_8x7.h
    The Chaplex library can be found at: 
    http://playground.arduino.cc/Code/Chaplex

    Development environment specifics:
    Written in Arduino 1.6.7
    Tested with SparkFun RedBoard and BadgerStick (Interactive Badge)

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).

    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.

    Distributed as-is; no warranty is given.
    ****************************************************************/

    #include <SparkFun_LED_8x7.h>
    #include <Chaplex.h>

    // Global variables
    byte led_pins[] = ; // Pins for LEDs
    byte i;

    void setup() 

    void loop() 

You should see a basic square, line, and filled circle appear on the LED array. What other fun shapes and pictures can you make?