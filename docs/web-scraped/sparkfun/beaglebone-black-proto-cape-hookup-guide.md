# Source: https://learn.sparkfun.com/tutorials/beaglebone-black-proto-cape-hookup-guide

## Board Overview

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/2/thumb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/thumb.jpg)

The BeagleBone Black Proto Cape is a great way to prototype or design custom capes for the [BeagleBone Black](https://www.sparkfun.com/products/12076). This cape gives you access to all gpio available on the BeagleBone Black. There are also two red LED\'s available for user applications. The included EEPROM lets the user prototype cape description files, which are used by the [BeagleBoard Foundation](http://beagleboard.org/) to register boards.

### Suggested Reading

Before you start, we recommend the following background knowledge:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)

## Assembly 

First let\'s solder some headers to the cape. There are two styles of headers you may choose from.

If you only plan on using one cape, straight headers will do just fine.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/12791-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/12791-01.jpg)

[Header 2x23 (PRT-12791)](https://www.sparkfun.com/products/12791)

If you plan to use multiple capes, it is necessary to use stackable headers.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/12790-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/12790-01.jpg)

[Stackable Header 2x23 (PRT-12790)](https://www.sparkfun.com/products/12790)

### Soldering Headers

It is important when soldering the headers that they are held in straight. Tack two opposite pins and check the alignment before finishing the rest of the pins. When you are complete allow the cape to cool before inserting.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/2/solderTack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/solderTack.png)

Removing capes can be quite difficult. Do not try to pull them off in one motion. Try to rock or slowly apply pressure to the corners. Separating in this fashion will prevent the pins from being bent.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/2/Separating_capes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/Separating_capes.jpg)

Let\'s take a look at how the prototyping area is laid out.

## Proto Area

There is plenty of space on which to prototype. There are two power buses provided along with ground connections on both sides of the board, all .1\" spaced through holes.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/PinLayout_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/PinLayout_1.png)

Two LED\'s have been provided for quick and easy debugging or general purpose use.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/LED_Schematic.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/LED_Schematic.png)

Simply apply a current to each LED to illuminate. They work with both 3.3v and 5v inputs.

Now, let\'s look at the EEPROM and its features.

## Using the EEPROM

The Cape EEPROM is great for storing pin configuration data. The cape EEPROM is read by the BeagleBone Black during boot. It can then automatically setup the pins for use. There are several steps to understand how the EEPROM is used. For now, we will show you the possible settings available. The cape comes with a blank EEPROM.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/2/EEPROMGuide.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/EEPROMGuide.png)

The default address for the EEPROM is 0x57. You can change it to addresses 0x54 - 0x57 with the selection of the two address jumpers. They are Labled A0 and A1. Changing the address of the Cape is important when you are using multiple capes.

# Address Table

## 

  A2   A1   A0   7-bit address
  ---- ---- ---- ---------------
  1    0    0    0x54
  1    0    1    0x55
  1    1    0    0x56
  1    1    1    0x57

Once you have created your next great thing you can register your settings with the BeagleBone foundation. This registration allows them to upload your settings to the latest operating system available. This removes the need for users to setup their board to use your cape.