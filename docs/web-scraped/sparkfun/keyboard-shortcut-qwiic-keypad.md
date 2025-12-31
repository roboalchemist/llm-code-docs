# Source: https://learn.sparkfun.com/tutorials/keyboard-shortcut-qwiic-keypad

## Introduction

You may not realize it, but you probably often use [keyboard shortcuts](https://en.wikipedia.org/wiki/Keyboard_shortcut) for common tasks that, otherwise, were previously extremely monotonous. A perfect example of these shortcuts are the [Cut, Copy, and Paste](https://en.wikipedia.org/wiki/Cut,_copy,_and_paste) commands, which are almost universally used in every computer application today. Originally, people used to cut (with special scissors) and paste these changes manually.

In this guide, we will cover how to utilize the [RedBoard Turbo](https://www.sparkfun.com/products/14812) to emulate an HID keyboard that responds to inputs from the [Qwiic Keypad](https://www.sparkfun.com/products/15290) to create your own custom shortcut keypad. This is perfect for gaming hotkeys, keyboard shortcuts that require more than two button combinations, or for command line/data/text entries.

[![Hotkey Keypad](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/3/Stickers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/Stickers.jpg)

This will be similar to the [Enginursday Blog Post: Pressing Our Buttons](https://www.sparkfun.com/news/2412), but without the complex soldering. Although not necessary, it would be good to review the blog post.

Please be aware that the example code below is written to run explicitly on **Windows OS**. For Mac OS, you will need to modify the code for the appropriate Mac OS keycodes.

### Required Materials

For this project, you will need the following products. You may already have a few of these items, so feel free to modify your cart based on your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun Qwiic Keypad - 12 Button](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/7/7/7/15290-SparkFun_Qwiic_Keypad_-_12_Button-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-keypad-12-button.html)

### [SparkFun Qwiic Keypad - 12 Button](https://www.sparkfun.com/sparkfun-qwiic-keypad-12-button.html) 

[ COM-15290 ]

The SparkFun Qwiic Keypad comes fully assembled and makes the development process for adding a 12 button keypad easy.

[ [\$13.50] ]

### Suggested Reading

If you haven\'t already gone through the hookup guides for each of these parts, we highly suggest starting off there to understand the basic functionality of each board:

[](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide)

### Qwiic Keypad Hookup Guide 

If you are tired of taking up GPIO pins, wiring a bunch of pull up resistors, and using firmware that scans the keys taking up valuable processing time\... check out the new Qwiic Keypad.

[](https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide)

### RedBoard Turbo Hookup Guide 

An introduction to the RedBoard Turbo. Level up your Arduino-skills with the powerful SAMD21 ARM Cortex M0+ processor!

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

This project utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

For a better understanding of how example codes work, please review the following references for the platform you are interested in:

- CircuitPython References

  - [Circuit Python I^2^C](https://learn.adafruit.com/circuitpython-essentials/circuitpython-i2c)
  - [Circuit Python HID Keyboard/Mouse](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

- Arduino References

  - [NicoHood HID-Project Wiki Page](https://github.com/NicoHood/HID/wiki)
  - [Arduino HID-Project Library GitHub Repository](https://github.com/NicoHood/HID)
  - [Arduino Wire Library Reference Page](https://www.arduino.cc/en/reference/wire)
  - [Arduino Wire Library (In-Depth) Reference](https://playground.arduino.cc/Main/WireLibraryDetailedReference)

## Project Overview

In this example project, we will be focusing on three different types of shortcuts that will probably be the most useful for readers.

### [Button Combinations]

These are shortcuts that require a combination of buttons. This is not just limited to easy ones like [Ctrl] + [x] that you may use often. Often in program applications, there will be a number of shortcut button combinations available for users. These shortcuts may even use combinations of +3 buttons or may not always seem intuitive.

Win10/Linux:

- [Ctrl] + [Alt] + [F1]: Used to switch between virtual desktops.

Force Quit Application

- Win 10: [Ctrl] + [Alt] + [Esc]
- Mac OSX: [⌘] + [Option] + [Esc]

Microsoft Excel:

- [Ctrl] + [Shift] + [U]: Expand or collapse the formula bar
- [Alt] + [F8]: Create, run, edit, or delete a macro
- [Alt] + [F11]: Open the Microsoft Visual Basic For Applications Editor
- [Alt] + [H] + [D] + [C]: Delete column
- [Alt] + [H] + [H]: Select a fill color
- [Alt] + [H] + [B]: Add a border

### [Functional Buttons]

These are consumer functions or multimedia buttons available on modern keyboards. Usually these buttons have special icons and may lie outside the normal keyboard layout. (*If inside the keyboard layout, they may require special buttons like [Fn].*)

Example Functions: Web Search [[]], Volume Up/Down [[]] [[]], Mute [[]], Calculator, or Increase/Decrease Screen Brightness.

![](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/PC_keyboard2.jpg)

![](https://cdn.sparkfun.com/r/635-280/assets/learn_tutorials/8/8/3/MAC_keyboard2.jpg)

[[]](#carousel-6954f6c4044c6) [[]](#carousel-6954f6c4044c6)

1.  ::: 
    :::

2.  ::: 
    :::

### [Text Strings]

Text strings, these may be things that you must commonly write everyday. Think of it as a quick type or saved clipboard. Essentially, these buttons will automatically generate keyboard entries for saved text strings.

For example, I am in charge of writing tutorials and hookup guides and often I need to create HTML features like the ones listed below. I have most of them memorized, but it still takes a few seconds to type everything out. We\'ll use the HTML table as an example for the one of the buttons code below.

#### HTML Ordered List:

+-----------------------------------+-------------------------------------+
| ##### Example:                    | ##### Code:                         |
+-----------------------------------+-------------------------------------+
| 1.  Thing A                       | ```  |
| 2.  Thing B                       | <ol>                                |
| 3.  Thing C                       |     <li>Thing A</li>                |
|                                   |     <li>Thing B</li>                |
|                                   |     <li>Thing C</li>                |
|                                   | </ol>                               |
|                                   | ```                                 |
+-----------------------------------+-------------------------------------+

#### HTML Table:

+---------------------------------------------------------------------------+---------------------------------------------------------------------+
| ##### Example:                                                            | ##### Code:                                                         |
+---------------------------------------------------------------------------+---------------------------------------------------------------------+
|   ----------------------- ----------------------- ----------------------- | ```                                  |
|   A\                      B                       C                       | <table border="1">                                                  |
|   B\                                                                      |     <tr style="padding:10px">                                       |
|   C                                                                       |         <td width="25%" style="padding:10px">                       |
|                                                                           |             A<br>                                                   |
|   1                       2                       3                       |             B<br>                                                   |
|                                                                           |             C                                                       |
|   \*                      \+                      =                       |         </td>                                                       |
|   ----------------------- ----------------------- ----------------------- |         <td width="25%" style="padding:10px" valign="center">B</td> |
|                                                                           |         <td width="25%" style="padding:10px" valign="top">C</td>    |
|                                                                           |     </tr>                                                           |
|                                                                           |     <tr>                                                            |
|                                                                           |         <td style="padding:1px">1</td>                              |
|                                                                           |         <td style="padding:10px">2</td>                             |
|                                                                           |         <td style="padding:5px">3</td>                              |
|                                                                           |     </tr>                                                           |
|                                                                           |     <tr>                                                            |
|                                                                           |         <td>*</td>                                                  |
|                                                                           |         <td>+</td>                                                  |
|                                                                           |         <td>=</td>                                                  |
|                                                                           |     </tr>                                                           |
|                                                                           | </table>                                                            |
|                                                                           | ```                                                                 |
+---------------------------------------------------------------------------+---------------------------------------------------------------------+

#### HTML Alerts or Wells:

##### Example:

**Heads up!** This is some kind of warning.

##### Code:

    <div class="alert alert-warning"><b>Heads up!</b> This is some kind of warning.</div>

## Hardware Assembly

**Note:** Don\'t forget to [install the SAMD21 driver](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/hardware-setup) for the RedBoard Turbo, if necessary.

With the Qwiic connector system, assembling the hardware is simple. All you need to do is connect your [Qwiic Keypad](https://www.sparkfun.com/products/15290) to a [RedBoard Turbo](https://www.sparkfun.com/products/14812) with a [Qwiic cable](https://www.sparkfun.com/products/14427).

[![Hardware assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/3/Turbo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/Turbo.jpg)

If you wish to create a custom enclosure, this can easily be done with a laser cutter and or 3D printer. For custom button faces, you can use printable stickers or some paper and glue.

[![Example stickers](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/8/8/3/Hotkeys.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/Hotkeys.png)\
*Stickers*

[![Stickers on Keypad](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/8/8/3/Stickers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/Stickers.jpg)\
*Stickers on keypad. (Click to enlarge)*

## Arduino Example

**Note:** This tutorial assumes you are familiar with Arduino products and you are using the latest stable version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Arduino Library

The easiest way to install the Arduino libraries are by searching **SparkFun Qwiic Keypad** and **HID-Project** inside the Arduino library manager. To manually install, head on over to their respective GitHub repositories:

- [SparkFun Qwiic Keypad Library GitHub Repository](https://github.com/sparkfun/SparkFun_Qwiic_Keypad_Arduino_Library)
- [HID-Project Library GitHub Repository](https://github.com/NicoHood/HID)

or feel free to download the libraries below:

[SparkFun Qwiic Keypad Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_Keypad_Arduino_Library/archive/master.zip) [HID-Project Library (ZIP)](https://github.com/NicoHood/HID/archive/master.zip)

### Using the Qwiic Keypad Library

The functionality of the Qwiic Keypad library is pretty straight forward. The example code, primarily draws from the [`Example1_ReadButton.ino` sketch](https://github.com/sparkfun/SparkFun_Qwiic_Keypad_Arduino_Library/blob/master/examples/Example1_ReadButton/Example1_ReadButton.ino). Below is a quick summary of the library functions that are used in the example code.

- `keypad1.begin()`- Used to connect to Qwiic Keypad.
- `keypad1.updateFIFO()`- Used to increment the FIFO.
- `char button = keypad1.getButton()`- Used to read button press from FIFO with value stored as a character in the variable *button*.

### Using the HID-Project Library

The [HID-Project library](https://github.com/NicoHood/HID), built by [NicoHood](https://github.com/NicoHood) work similarly to the [Arduino Keyboard library](http://arduino.cc/en/Reference/MouseKeyboard). It is also compatible with the [original key definitions](https://www.arduino.cc/en/Reference/KeyboardModifiers), just make sure you use the name, not the number. (*i.e* `Keyboard.write(0xB0)` *will not work, use* `Keyboard.write(KEY_RETURN)` *instead.*)

#### Button Combinations

To create shortcut using button combinations, find out the button combination for your shortcut. These should be listed in the user manual for your program or operating system; otherwise, the internet is a great resource. Make sure to test that the shortcut works before programming it.

To code your shortcut in Arduino, use the `Keyboard.press(`*`Define_Key`*`)` function, designating the individual key. To press multiple keys together, call this function again while designating each of the individual keys. Then use `Keyboard.releaseAll()` to release all the *keys pressed* at once. Please refer to the [*ImprovedKeylayouts.h*](https://github.com/NicoHood/HID/blob/master/src/KeyboardLayouts/ImprovedKeylayouts.h) header file from the HID-Project library for the naming convention (or keycode) of each keyboard key.

Example: [Ctrl] + [Alt] + [F1]

Code:

    language:c
    Keyboard.press(KEY_CTRL);
    Keyboard.press(KEY_F1);
    Keyboard.press(KEY_ALT);
    Keyboard.releaseAll();

#### Functional Buttons

To create a functional shortcut in Arduino, use the `Consumer.write(`*`Define_Key`*`)` function, designating the functional key to implement. Please refer to the [*ConsumerAPI.h*](https://github.com/NicoHood/HID/blob/master/src/HID-APIs/ConsumerAPI.h) header file from the HID-Project library for the naming convention (or keycode) of the available keys.

Example: [[]]

Code:

    language:c
    Consumer.write(MEDIA_VOLUME_DOWN);
    delay(50);
    Keyboard.releaseAll();

#### Text String

To type out a string of text in Arduino, use the `Keyboard.print("`*`Text`*`")` or `Keyboard.println("`*`Text`*`")` function.

Example Text:

``` 
<table>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
```

Code:

``` 
Keyboard.println("<table border=\"1\">");
Keyboard.println("    <tr style=\"padding:10px\">");
Keyboard.println("        <td style=\"padding:10px\" valign=\"center\"></td>");
Keyboard.println("        <td style=\"padding:10px\" valign=\"center\"></td>");
Keyboard.println("        <td style=\"padding:10px\" valign=\"center\"></td>");
Keyboard.println("    </tr>");
Keyboard.println("    <tr style=\"padding:10px\">");
Keyboard.println("        <td style=\"padding:10px\" valign=\"top\"></td>");
Keyboard.println("        <td style=\"padding:10px\"></td>");
Keyboard.println("        <td style=\"padding:10px\"></td>");
Keyboard.println("    </tr>");
Keyboard.println("    <tr style=\"padding:10px\">");
Keyboard.println("        <td></td>");
Keyboard.println("        <td></td>");
Keyboard.println("        <td></td>");
Keyboard.println("    </tr>");
Keyboard.println("</table>");
```

### Example Code

In the example code below I have implemented specific keyboard shortcuts for my personal needs. You will also notice, that in certain instances, I have combined a series of different shortcuts for greater functionality.

[Download Example Arduino Code](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/hotkeypad.ino)

    language:c
    /*
      Hot-Shortcut KeyPad
      By: Wes Furuya
      SparkFun Electronics
      Date: March 27th, 2019
      License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/14641
      https://www.sparkfun.com/products/14812

      This sketch allows the RedBoard Turbo to emulate a HID keyboard. The buttons on the Qwiic Keypad are set for
      specific keyboard entries. For more details, please refer to the project guide:
      https://learn.sparkfun.com/tutorials/keyboard-shortcut-qwiic-keypad

    */
    //#include "Keyboard.h"
    #include "HID-Project.h"
    #include <Wire.h>

    #include "SparkFun_Qwiic_Keypad_Arduino_Library.h" //Click here to get the library: http://librarymanager/All#SparkFun_keypad
    KEYPAD keypad1; //Create instance of this object

    void setup(void)
    
      SerialUSB.print("Initialized. Firmware Version: ");
      SerialUSB.println(keypad1.getVersion());
      SerialUSB.println("Press a button: * to do a space. # to go to next line.");

    //  Initializes keyboard functions
      Keyboard.begin();
      Consumer.begin();
    }

    void loop(void)
    
      else if (button != 0)
      
        else if (button == '2')
        
        else if (button == '3')
        
        else if (button == '4')
        
        else if (button == '5')
        
        else if (button == '6')
        
        else if (button == '7')
        
        else if (button == '8')
        
        else if (button == '9')
        
        else if (button == '*')
        
        else if (button == '0')
        
        else if (button == '#')
        
        else
            
      }

      //Do something else. Don't call your Keypad a ton otherwise you'll tie up the I2C bus
      delay(25); //25 is good, more is better
    }

## CircuitPython Example

In an effort to utilize the CircuitPython capability of the RedBoard Turbo, I also have included CircuitPython example code. When you plug the RedBoard Turbo into the computer, it should show up as an USB drive. If not, check out the [Troubleshooting](https://learn.sparkfun.com/tutorials/keyboard-shortcut-qwiic-keypad#troubleshooting) section below on how to re-install CircuitPython. To upload your code to your board, you must save the python file on the drive that appears when the board is plugged in.

**Note:** This tutorial assumes you are familiar with Arduino products and CircuitPython. If you need help, please consult the [CircuitPython documentation](https://circuitpython.readthedocs.io/en/latest/docs/index.html).

### Import CircuitPython Libraries

#### Installing the Libraries

There may be better instructions than these, but this is what I did to get the CircuitPython libraries onto the RedBoard Turbo. You can also download the library directly using the button below.

1.  Go to the [**Releases**](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20190326) tab for the GitHub Repository.
2.  Download the .zip file containing \"[*bundule-3.x-mpy*](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20190326/adafruit-circuitpython-bundle-3.x-mpy-20190326.zip)\" in the name or click the button below.
3.  Unzip the file.
4.  Copy the lib folder from file onto the board.

[Download CircuitPython LIbrary](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20190326/adafruit-circuitpython-bundle-3.x-mpy-20190326.zip)

**Note:** The instructions for importing the CircuitPython libraries were confusing for me; I originally ended up downloading the *master* .zip file, instead of the *release* .zip file.

#### Utilizing the Libraries

To utilize the libraries in your code, you need to **`import`** them. Below, are the lines used for importing the libraries in the example python code.

    language:python
    import time
    import board
    import busio

    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    from adafruit_hid.keycode import Keycode
    from adafruit_hid.consumer_control import ConsumerControl
    from adafruit_hid.consumer_control_code import ConsumerControlCode

### Implementing CircuitPython

#### Querying the Keypad

Using the description of the FIFO operation from the [Qwiic Keypad hookup guide](https://learn.sparkfun.com/tutorials/qwiic-keypad-hookup-guide#hardware-overview), the Qwiic Keypad utilizes two registers for querying button presses. The first is register **0x03**, that is read for the oldest entry in the FIFO (first-in, first-out) *stack*. The second is the FIFO increment command register, **0x06**, used to update register **0x03** with the next button value.

##### Setup for I^2^C

To setup your I^2^C connection, you need to import the following libraries. You also need to define the pins used for the I^2^C bus, which was built into the `board` library for the SAMD21 used on the Turbo. Finally, the I^2^C address for the Qwiic Keypad was store as a variable.

    language:python
    import time
    import board
    import busio

    i2c = busio.I2C(board.SCL, board.SDA)
    i2caddress = 75 #equals 0x4B in HEX

##### Read Register

The following code is used to read the value of the oldest button press out of the FIFO *stack* from register **0x03**.

    language:python
    i2c.writeto(i2caddress, bytes([0x03]), start=0, end=8, stop=True)
    time.sleep(.2)
    i2c.readfrom_into(i2caddress, result2, start=0, end=1)

##### Write/Set Register

The following code is used to write **0x01** to register **0x06** to increment the FIFO *stack*, updating the value stores in register **0x03**.

    language:python
    i2c.writeto(i2caddress, bytes([0x06,0x01]), start=0, end=16, stop=True)

#### Creating Shortcuts

##### Utilizing HID Library

The [CircuitPython HID library](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html) works similarly to the Arduino library used in the previous section. To reference keycodes and naming conventions I used a combination of the following documentation:

- [CircuitPython HID library](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html)
- [USB HID Keycode Usage Table](https://usb.org/sites/default/files/documents/hut1_12v2.pdf)
- [Keyboard Keycodes from Arduino HID-Project Library](https://github.com/NicoHood/HID/blob/master/src/KeyboardLayouts/ImprovedKeylayouts.h)
- [Consumer Keycodes from Arduino HID-Project Library](https://github.com/NicoHood/HID/blob/master/src/HID-APIs/ConsumerAPI.h)

#### Button Combinations

To create shortcut using button combinations, find out the button combination for your shortcut. These should be listed in the user manual for your program or operating system; otherwise, the internet is a great resource. Make sure to test that the shortcut works before programming it.

To code your shortcut in CircuitPython, use the `kbd.press(`*`Define_Key`*`)` function, designating the individual key. To press multiple keys together, call this function again while designating each of the individual keys. Then use `kbd.release_all()` to release all the *keys pressed* at once. Please refer to the documentation listed above for the naming convention (or keycode) of each keyboard key.

Example: [Ctrl] + [Alt] + [F1]

Code:

    language:python
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.ALT)
    kbd.press(Keycode.INSERT)
    kbd.release_all()

#### Functional Buttons

To create a functional shortcut in CircuitPython, use the `cc.send(`*`Define_Key`*`)` function, designating the functional key to implement. Please refer to the documentation listed above for the naming convention (or keycode) of the available keys.

Example: [[]]

Code:

    language:python
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)

#### Text String

To type out a string of text in CircuitPython, use the `layout.write('`*`Text`*`')` function.

Example Text:

``` 
<table>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
```

Code:

``` 
layout.write('<table border="1">\n')
layout.write('    <tr style="padding:10px">\n')
layout.write('        <td style="padding:10px" valign="center"></td>\n')
layout.write('        <td style="padding:10px" valign="center"></td>\n')
layout.write('        <td style="padding:10px" valign="center"></td>\n')
layout.write('    </tr>\n')
layout.write('    <tr style="padding:10px">\n')
layout.write('        <td style="padding:10px" valign="top"></td>\n')
layout.write('        <td style="padding:10px"></td>\n')
layout.write('        <td style="padding:10px"></td>\n')
layout.write('    </tr>\n')
layout.write('    <tr style="padding:10px">\n')
layout.write('        <td></td>\n')
layout.write('        <td></td>\n')
layout.write('        <td></td>\n')
layout.write('    </tr>\n')
layout.write('</table>\n')
```

### Example Code

In the example code below I have implemented specific keyboard shortcuts for my personal needs. You will also notice, that in certain instances, I have combined a series of different shortcuts for greater functionality.

[Download Example CircuitPython Code](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/3/code.py)

**Note:** Your code must be saved in a file named `code.py` on the drive that appears when the RedBoard Turbo is plugged into your computer.

    language:python
    """   Hot-Shortcut KeyPad
    By: Wes Furuya
    SparkFun Electronics
    Date: March 27th, 2019
    License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

    Feel like supporting our work? Buy a board from SparkFun!
    https://www.sparkfun.com/products/14641
    https://www.sparkfun.com/products/14812

    This sketch allows the RedBoard Turbo to emulate a HID keyboard. The buttons on the Qwiic Keypad are set for specific keyboard entries. For more details, please refer to the project guide:
    https://learn.sparkfun.com/tutorials/keyboard-shortcut-qwiic-keypad """

    import time

    import board
    import busio

    # https:#github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20190326
    # 1. Download "bundule-3.x":
    #    https:#github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20190326/adafruit-circuitpython-bundle-3.x-mpy-20190326.zip
    # 2. Unzip
    # 3. Copy lib folder on to board

    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    from adafruit_hid.keycode import Keycode
    from adafruit_hid.consumer_control import ConsumerControl
    from adafruit_hid.consumer_control_code import ConsumerControlCode

    cc = ConsumerControl()
    kbd = Keyboard()
    layout = KeyboardLayoutUS(kbd)

    i2c = busio.I2C(board.SCL, board.SDA)
    i2caddress = 75 #equals 0x4B in HEX
    CALCULATOR = 402 #equals 0x192 in HEX

    while not i2c.try_lock():
        pass

    while True:
        result2 = bytearray(1)
        i2c.writeto(i2caddress, bytes([0x03]), start=0, end=8, stop=True)
        i2c.readfrom_into(i2caddress, result2, start=0, end=1)

        if result2 != bytes([0x00]):
            if result2 == b'1':
                cc.send(ConsumerControlCode.MUTE)
                print(result2)

            elif result2 == b'2':
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
                print(result2)

            elif result2 == b'3':
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
                print(result2)

            elif result2 == b'4':
                cc.send(CALCULATOR) #cc.send(402)
                print(result2)

            elif result2 == b'5':
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.ALT)
                kbd.press(Keycode.INSERT)
                kbd.release_all()
                print(result2)

            elif result2 == b'6':
                kbd.send(227) #Windows Button
                time.sleep(.05)
                layout.write('ter')
                time.sleep(.1)
                kbd.send(Keycode.ENTER)
                print(result2)

            elif result2 == b'7':
                # Cuts selected entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.X)
                kbd.release_all()
                time.sleep(.05)

                layout.write('<!-- product_big(')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write(') -->\n')
                layout.write('<!-- products_by_id(')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('ID1, ID2) -->\n')
                layout.write('<div class="clearfix"></div>')

            elif result2 == b'8':
                #Types text
                layout.write('<table border="1">\n')
                layout.write('    <tr style="padding:10px">\n')
                layout.write('        <td style="padding:10px" valign="center"></td>\n')
                layout.write('        <td style="padding:10px" valign="center"></td>\n')
                layout.write('        <td style="padding:10px" valign="center"></td>\n')
                layout.write('    </tr>\n')
                layout.write('    <tr style="padding:10px">\n')
                layout.write('        <td style="padding:10px" valign="top"></td>\n')
                layout.write('        <td style="padding:10px"></td>\n')
                layout.write('        <td style="padding:10px"></td>\n')
                layout.write('    </tr>\n')
                layout.write('    <tr style="padding:10px">\n')
                layout.write('        <td></td>\n')
                layout.write('        <td></td>\n')
                layout.write('        <td></td>\n')
                layout.write('    </tr>\n')
                layout.write('</table>\n')

            elif result2 == b'9':
                #Cuts selected entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.X)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('<div class="alert alert-info"><b>Note:</b>')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('</div>')

            elif result2 == b'*':
                #Cuts selected entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.X)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('-> [![alt text](')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write(')](')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write(') <-')
                layout.write('<div class="center-block text-center"> *Caption* </div>')

            elif result2 == b'0':
                #Cuts selected entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.X)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('<center><a href="')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('"><img src="')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('" alt=""></a></center>')
                layout.write('<center><i>Caption</i></center>')

            elif result2 == b'#':
                #Cuts selected entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.X)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('<kbd>')
                time.sleep(.05)

                #Pastes entry
                kbd.press(Keycode.CONTROL)
                kbd.press(Keycode.V)
                kbd.release_all()
                time.sleep(.05)

                #Types text
                layout.write('</kbd>')

            else:
                print(result2)

        time.sleep(.05)
        i2c.writeto(i2caddress, bytes([0x06,0x01]), start=0, end=16, stop=True)

## Troubleshooting

### Drivers

After plugging in your board into the computer, make sure that the drivers for the SAMD21 are installed on your computer. For MAC OSX and Win 10, this should be done automatically once the board is plugged in. I believe this also applies for the more popular flavors of Linux as well.

If needed, you can download the Windows driver using the button below. You can find instructions for this process in the [SAMD21 MiniDev Hookup Guide](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/hardware-setup).

[Windows SAMD21 Driver](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/SparkFun-SAMD21-Driver-111115.zip)

Please be aware that the SparkFun SAMD21 driver is **NOT currently supported** on Windows OS prior to **Win 8**.

### Double-Tapping Into the Bootloader

The bootloader is what allows us to load code over a simple USB interface. If you have bricked your board, try to upload code from bootloader mode. To manually enter bootloader mode, **rapidly double-tapping the reset button** (after hitting the reset button once, you have about half a second to hit it again). The board will remain in bootloader mode until power cycles (happens automatically after uploading code) or the reset button is hit again (once).

On the Turbo, the there are a clues to if it is in bootloader mode:

- RGB LED (on Pin 44) will be **solid green**.
- The D13 LED indicator will be a solid blue (might fade in and out a little).
- Charge indicator LED will be flashing constantly.
- Board will show up under a different COM port.

### Dual Serial Ports

One global issue to be aware of is that each SAMD21 Board appears to your computer as **two USB devices**, and your computer will assign **two different port numbers** to your SAMD21 Board - one for the bootloader, the other for the sketch.

- Verify that you are selecting the available serial port for the board.
- If your computer isn\'t registering the board try double-tapping it into bootloader mode.

### Serial Port Not Appearing in Port Menu

If your SAMD21 board is plugged in \-- power LED illuminated \-- but it isn\'t appearing in your Arduino port list, first of all, make sure you have the [drivers installed](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/hardware-setup#driver-install) (Windows computers only). Then follow these steps to see if you can get the port back:

1.  Close *all* Arduino windows. (Don't forget to save!)
2.  Unplug SAMD21 Board from your computer.
3.  Wait a few seconds for the device to be detached.
4.  Plug SAMD21 Board back in.
5.  Open Arduino back up, check the Ports menu again.

### Upload Fails or Freezes

If a sketch upload is taking longer than usual, or fails entirely, try **resetting into the bootloader** and uploading directly there. If the SAMD21 is in bootloader mode, you may need to **re-select your port** \-- this time selecting the bootloader port.

- **Closing the serial monitor** before uploading may also make for more reliable uploading.

### Reinstalling CircuitPython

If you do your developing in Arduino, you\'ll find that after uploading your first sketch, the RedBoard Turbo no longer pops up like a removable USB device as it did previously. That\'s to be expected. In this section we\'ll walk through a few simple steps to getting CircuitPython re-uploaded onto your RedBoard Turbo.

1.  Reset board to Bootloader

    We want the board to reset to the UF2 bootloader, which enables the board to act like a flash drive. To do that we\'ll *double* tap the reset button. Shortly after you do that, the board will pop up as a USB drive named *TURBOBOOT*.

2.  Download and Drag CircuitPython Firmware

    Download the CircuitPython firmware below (also found in the [GitHub product repository](https://github.com/sparkfun/RedBoard_Turbo/tree/master/Firmware)). Drag the contents named `turbo-boot_cp.uf2` onto your *TURBOBOOT* USB drive and the USB drive should disappear momentarily only to reappear as a *CIRCUITPY* USB drive instead.

    ::: 
    [CircuitPython Firmware (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/turbo-boot_cp.zip)
    :::

3.  Re-install the CircuitPython Libraries (to get example code working)

    Download the CircuitPython library bundle below and then drag the **lib** folder over to the USB drive for the RedBoard Turbo. For more details see the instructions [above](https://learn.sparkfun.com/tutorials/keyboard-shortcut-qwiic-keypad#circuitpython-example).

    ::: 
    [Download CircuitPython LIbrary](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20190326/adafruit-circuitpython-bundle-3.x-mpy-20190326.zip)
    :::

## Project Notes

This is the end of the project documentation, excluding the resources linked below. Here are a few notes I had following the completion of the project tutorial.

### CircuitPython

Unfortunately, this was my first time using CircuitPython and there was a little confusion getting everything working. Specifically, I am not sure if I implemented the I^2^C functionality properly (as intended) for CircuitPython, but it worked for the purpose of this project. Feel free to comment below on any changes that should be made.

In my initial attempt to get the Qwiic Keypad running, I was able to read from all the registers. However, I wasn\'t able to implement a write to set individual register values in a similar fashion using the `writeto` function. It wasn\'t until I looked at how the code was operating with a logic analyzer, that I realized that these functions operated at a lower level. Despite being able to read a whole register block, the functions actually were meant for read and write bit operations as demonstrated above.

    language:python
    try:
        #initial attempt
        result1 = bytearray(8)
        i2c.readfrom_into(i2caddress, result1, start=0, end=7)
        print(result1)
        time.sleep(3)

    finally:
        i2c.unlock()

### Going Further with Macros

Do you have a repetitive task that you perform daily on your computer that you wish to automate? If you are more computer savy, you may already use or have created your own simple [macro](https://en.wikipedia.org/wiki/Macro_(computer_science)) for more complex tasks that can\'t be handled with a mere keyboard shortcut or hotkey. Although we won\'t cover macros in this guide, they are simple, yet powerful tools.

#### How simple\...

Even a grade schooler, could easily use Microsoft Excel to record a custom macro in VBA.

#### How powerful\...

Macros can perform essentially, almost any function you can with a mouse and keyboard. If you are particularly diabolical, this is an easy way to prank your friends\... you could easily create and hide a macro to cause mouse movements or play a particular audio file randomly. However, please be aware of the security risks involved in using macros (see note below).

**Danger:** When enabled, macros, although useful, may open up your computer to security risks. In the past macros, have been [known to be exploited as security flaws](https://en.wikipedia.org/wiki/Macro_and_security) to access computers for private information. Please make sure to research the risks thoroughly before using or enabling macros on any computer.