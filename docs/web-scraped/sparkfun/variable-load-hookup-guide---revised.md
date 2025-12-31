# Source: https://learn.sparkfun.com/tutorials/variable-load-hookup-guide---revised

## Introduction

**Note:** This guide is for the latest version of the Variable Load\'s firmware. If you have an **older version (purchased prior to 24 May 2018)**, or if your board doesn\'t behave in the way suggested by this tutorial, please refer to [the older tutorial](https://learn.sparkfun.com/tutorials/variable-load-hookup-guide).

SparkFun\'s [Variable Load board](https://www.sparkfun.com/products/14449) is designed to allow users to draw a specific amount of current from a voltage source. It can be used to test stability of the power supply under various loads, battery lifetime, safety cutoffs, and other design elements of power supplies under test.

The Variable Load can test supplies of up to 30V at currents ranging from a few mA to 4A. For safety, the total load power is limited to 15W, and even at 15W the heatsink gets very hot. The Variable Load is designed to be extensible, with headers for a [basic character-based LCD](https://www.sparkfun.com/products/709) so it can be used without a connection to a PC.

[![SparkFun Variable Load Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/7/9/14449-SparkFun_Variable_Load_Kit-05.jpg)](https://www.sparkfun.com/sparkfun-variable-load-kit.html)

### [SparkFun Variable Load Kit](https://www.sparkfun.com/sparkfun-variable-load-kit.html) 

[ KIT-14449 ]

The SparkFun Variable Load is a quick to assemble kit that has been designed to allow users to draw a specific amount of curr...

**Retired**

### Required Materials

Everything you need to follow this hookup guide is included in the kit, except for the heat sink thermal compound linked below. If you want to add an LCD, any of our 5V character LCDs will work, as linked below. You\'ll also need some male header pins. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Basic 16x2 Character LCD - White on Black 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/1/00709-action.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-white-on-black-5v.html)

### [Basic 16x2 Character LCD - White on Black 5V](https://www.sparkfun.com/basic-16x2-character-lcd-white-on-black-5v.html) 

[ LCD-00709 ]

This is a basic 16 character by 2 line display with a snazzy black background with white characters. Utilizes the extremely c...

[ [\$24.95] ]

[![Basic 16x2 Character LCD - Black on Green 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/7/00255-action.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-5v.html)

### [Basic 16x2 Character LCD - Black on Green 5V](https://www.sparkfun.com/basic-16x2-character-lcd-black-on-green-5v.html) 

[ LCD-00255 ]

This is a basic 16 character by 2 line display. Black text on Green background. Utilizes the extremely common HD44780 paralle...

[ [\$22.50] ]

[![Heatsink Compound](https://cdn.sparkfun.com/r/140-140/assets/parts/3/4/2/2/09599-Heatsink_Compound-01.jpg)](https://www.sparkfun.com/heatsink-compound.html)

### [Heatsink Compound](https://www.sparkfun.com/heatsink-compound.html) 

[ PRT-09599 ]

This is a 5g syringe of white heatsink compound (aka thermal grease, thermal paste, thermal goo). Use this whenever you\'re co...

[ [\$2.75] ]

[![Basic 16x2 Character LCD - RGB Backlight 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/1/10862-Action_new.jpg)](https://www.sparkfun.com/basic-16x2-character-lcd-rgb-backlight-5v.html)

### [Basic 16x2 Character LCD - RGB Backlight 5V](https://www.sparkfun.com/basic-16x2-character-lcd-rgb-backlight-5v.html) 

[ LCD-10862 ]

This is similar to other 16x2 character LCDs that you\'ve seen before but with one vibrant difference: The backlight is actual...

[ [\$18.95] ]

[![Basic 16x2 Character LCD - Yellow on Blue 5V](https://cdn.sparkfun.com/r/140-140/assets/parts/5/5/6/00790-action.jpg)](https://www.sparkfun.com/products/790)

### [Basic 16x2 Character LCD - Yellow on Blue 5V](https://www.sparkfun.com/products/790) 

[ LCD-00790 ]

This is a basic 16 character by 2 line display with a Blue background and a Yellow backlight. Utilizes the extremely common H...

**Retired**

### Required Tools

For assembly of this kit, you will need [standard soldering tools](https://www.sparkfun.com/categories/49). Any soldering iron of reasonable quality and solder should work fine. To mount the transistor to the heat sink, a Phillips head screwdriver is required.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

## Assembly

We recommend following this guide for easy assembly of the kit.

### Install the Heat Sink

This may seem a little backwards, but there\'s a reason for this. We want to make sure that the hole in the heat sink is at the right height for the hole in the transistor to mate with it, and the heat sink is of fixed height, so we want to install it first.

[![Heat sink nubs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-01.jpg)

Note that [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) these nubs down takes patience and a willingness to get things pretty hot. If you don\'t heat the nubs up enough, the solder won\'t flow over them nicely and you\'ll get a gloppy, goopy cold solder joint. Heating the nubs takes time, of course, because they\'re attached to a heat sink! Persist and don\'t become discouraged if the solder won\'t flow onto the nubs at first. Give it lots of time. If you have one, a large, hoof-type soldering iron tip is the best bet for heating up the nubs for a good joint.

[![Soldering nubs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-02.jpg)

Note too that there are no exposed copper pads on the PCB. This is okay, as the solder will flow over the nubs and down through the holes, forming a tight fit.

[![Nubs soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-03.jpg)

### Install the Terminal Block

This is a good time to install the terminal block. Notice which side of the board it is installed on, and the orientation of the terminal block with the silkscreen.

[![Terminal block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-04.jpg)

Soldering it down should be a fairly straightforward endeavor.

### Install the Transistor On the Heat Sink

Apply a small amount of thermal grease to the back of the transistor. This will improve heat transfer to the heat sink.

[![Thermal grease](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-05.jpg)

Then, insert the 3/8\" 4-40 machine screw through the hole in the transistor. Insert the legs of the transistor into the holes on the PCB and slide the pins down until the screw fits through the hole on the heat sink.

Thread the 4-40 nut onto the screw where it protrudes through the heat sink.

[![Nut threaded onto screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-06.jpg)

Tighten down the nut until it is snug. A screwdriver will help with this process. Do not overtighten the screw. It only needs to be a little tighter than finger tight. Then, flip the board and solder the transistor pins to the board.

[![Screw placed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-07.jpg)

Attach the standoffs to the corners of the board.

[![Standoff assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-15.jpg)

Finally, connect a micro-B cable to the Variable Load and your computer to get started.

### Optional: Install the LCD Assembly

If you\'re going to use the Variable Load with the optional LCD, now is the time to attach it.

Start by installing the header on the LCD. Observe the image below for proper orientation.

[![Header in LCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-17.jpg)

I like to tack down one pin first. Then melt the solder on that pin with one hand and use the other to make sure the header is at a right angle to the board. After soldering down all the pins, you can insert the header into the Variable Load board and repeat the process. Solder down the headers like the image below.

[![LCD mated to variable load board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-18.jpg)

The LCD is now in place and should just work when powered up. Connect a micro-B USB cable to the Variable Load and your computer to get started.

[![LCD Showing Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-19.jpg)

## Operation

The Variable Load board is designed to work with one of two output modes. Either using a:

- Console on a PC for Feedback
- Basic 16x2 Character LCD

In either case, the capacitive touch buttons on the front of the Variable Load PCB can be used to change the settings.

### General Operation

The primary method for controlling the Variable Load is the set of capacitive touch buttons on the front of the board. There are four buttons: up arrow, down arrow, \"Enter\" and \"Back\". The up and down arrow keys will adjust the current set point up or down in steps determined by the present set point. The higher the set point, the larger the step size. The \"Enter\" key turns the load on or off without affecting the set point, and the \"Back\" button resets the set point to zero.

[![Capacitive Touch Buttons](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/14449-SparkFun_Variable_Load_Kit-03Buttons.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/14449-SparkFun_Variable_Load_Kit-03Buttons.jpg)

There is an LED visible from the front of the board which will tell you whether the load is enabled or disabled at any given time.

[![Load Status LED](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/14449-SparkFun_Variable_Load_Kit-03LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/14449-SparkFun_Variable_Load_Kit-03LED.jpg)

The voltage limit for the board is **40V**. Exceeding this level may cause damage to the circuits on board. The current limit is **4A**, and the board will not in any case let you set a current draw above 4A. There is also a wattage limit of **15W**, which is calculated in live time. Normally, the current draw remains the same as the voltage is increased, but if the voltage is increased beyond a point where the product of the voltage and current exceeds 15W, the output will be disabled until the voltage drops to a safe point again.

### Using a Console for Output

**Note: The Arduino serial console will not work for this.** The Variable Load board uses VT100 terminal commands to draw its output and the Arduino console does **NOT** support VT100 emulation.

Start by checking out our [serial terminal basics](https://learn.sparkfun.com/tutorials/terminal-basics) tutorial. This will get you up and running with a serial terminal. Open a serial terminal program (i.e. PuTTY) to connect.

You\'ll need to identify the port name of the Variable Load board when it is connected. There are a few methods of determining which port the Variable Load Board is connected to.

One method to determine which port the Variable Load board is on, I recommend using the Arduino IDE. Under the \"Tools\" menu, there is a sub-menu for \"Port\". Since we had connected the USB cable to a computer\'s COM port already, make note of the items on the listed port names. Then unplug the micro-B USB cable from your computer. Give it a few seconds, then re-open that sub-menu to see what item has disappeared. By process of elimination, we can determine the port name that the Variable Load has enumerated to. Reconnect the cable to verify. The port name should reappear as the same name in the sub-menu. Remember, the Arduino IDE\'s Serial Monitor will not work with the Variable Load board.

#### Windows

If you don\'t have the Arduino IDE installed and don\'t want to install it, you can find the same information using built in tools. Under Windows, open up your device manager (if you don\'t know how to do this, do a search online for OS specific information on how to do it since it\'s slightly different under various versions of Windows). Take note of the devices on the list, then unplug the Variable Load and see which port on the list disappears. The port which disappeared from the list is the one you want.

[![Windows device manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/dev_manager_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/dev_manager_1.png)

#### Mac

Using a Mac OS, you\'ll need to open a terminal window. To figure out which port the Variable Load has connected to, type this command:

    language:bash
    ls /dev/cu.usbserial-*

This will return a list of USB-Serial converter ports on the system. Take note of the devices on the list, then unplug the Variable Load and see which port on the list disappears. The port which disappeared from the list is the one you want. You can then connect to the port in question by typing this command:

    language:bash
    screen /dev/cu.usbserial-XXXXXXXX 115200

where the XXXXXXXXX is replaced by information gleaned from the first command.

#### Linux

Under Linux, the process is similar to Mac OS, only use this command to identify the serial port:

    language:bash
    ls /dev/ttyUSB*

You may use `screen` command to connect to the Variable Load:

    language:bash
    screen /dev/ttyUSBX 115200

Again, the \"X\" should be replaced with information gleaned from the `ls` command above. If you receive an error about `screen` not being installed, you can install `screen` by typing this command:

    language:bash
    sudo apt-get install screen

Then re-enter the above command to connect via `screen`.

### The Console

This is what the console will look like when you\'ve connected to the Variable Load. It reports five values:

- **I Source** \-- the actual current being drawn from the source
- **I Limit** \-- the current limit set for the load
- **V Source** \-- the current load voltage at the Variable Load board
- **V Min** \-- the current minimum voltage before the load cuts out
- **mA Hours** \-- the number of milliamp hours drawn from the source since it was last reset

[![The console as viewed with the variable load connected](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/console_view.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/console_view.png)

**Not Case Sensitive:** The Variable Load board will accept lower case and capital letters from your keyboard. So if you were setting the current to 0.5 A for your load, you could type [i.5] and the [Enter] key. Or you could also type [I.5] followed by the [Enter] key..

#### Setting I~Limit~ and V~Min~

The console may be used to set two values: **I limit** and **V min**. To set **I limit**, type \"[I]\" followed by a decimal value and then hit the [Enter] key on your keyboard. To set the **V min** voltage, type \"[V]\" and then a decimal value and hit the [Enter] key.

#### Turning Load and Setting mAh

The console can also be used to enable or disable the supply. Simply type \"[E1]\" followed by the [Enter] key to turn the supply on. Typing \"[E0]\" or \"[E]\" followed by the [Enter] key will turn the supply off. It can also be used to reset the amount of energy drawn from the supply (the mAh number)\--type \"[R]\" and hit [Enter].

#### Bootloader Mode

Finally, the console is used to put the device into bootloadable mode. Enter \"[B]\" and then hit the [Enter] key and the board will reset itself into bootloader mode. The bootloader host application within PSoC Creator can then be used to load new code onto the board.

### Using the LCD

The LCD output is very similar to the console, except slightly less verbose to fit the data on it. You can use the console and the LCD at the same time, but that sort of defeats the purpose of using the LCD. When using the LCD alone, you\'ll have to rely on the buttons on the board to control the set point.

[![LCD Showing Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/2/Variable_Load_Sensor_Hookup_Guide-19.jpg)

## Changing the Firmware

All of the firmware is available on the [GitHub page for the product](https://github.com/sparkfun/Variable_Load). You can customize the firmware as you need using the bootloader on the board, without having to use a programming cable, so long as your board has the most updated firmware. Boards shipped **prior to 24 May 2018** do **not** have a bootloader on them.

### PSoC Creator

**Note:** To build and edit the firmware, you\'ll need to download [Cypress\' PSoC Creator IDE](http://www.cypress.com/products/psoc-creator-integrated-design-environment-ide). When writing this tutorial, *PSoC Creator v4.2* was used. Using Creator is outside the scope of this tutorial. However, we do have [some content on using Creator](https://learn.sparkfun.com/tutorials/freesoc2-hookup-guide-v14#getting-started-with-psoc-creator) in our FreeSoC2 Hookup Guide, and Cypress has a [good quickstart guide available](http://www.cypress.com/file/44826/download).

Download and unzip the files from the GitHub repository for the Variable Load board.

[Download GitHub Repository for Variable_Load (ZIP)](https://github.com/sparkfun/Variable_Load/archive/master.zip)

Open the *Variable_Load.cyprj* project file in PSoC Creator. Under the build configuration, set it to **Release** mode.

[![Select Release Mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/0/PSoC_Creator_Build_Configuration_Release_Mode.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/PSoC_Creator_Build_Configuration_Release_Mode.jpg)

In the menu bar, select **Build \> Build All Projects** to generate the files for the project. The one that we are interested in is the application file for the bootloader (*Variable_Load.cyacd*) which will be used later.

[![Build All Projects](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/0/PSoC_Creator_BuildAllProjects.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/PSoC_Creator_BuildAllProjects.jpg)

### Entering Bootloader Mode

To place the board in bootloader mode, open a console connected to the board and type \"[B]\" and hit [Enter]. The console will lose its connection and the board will reenumerate with a different port number. You can now bootload the board.

### Using the Bootloader Host Application

To open the bootloader host application, open the \"**Tools**\" menu in PSoC Creator and select \"**Bootloader Host\...**\".

[![Where to find the bootloader host menu item in creator](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/bootloader_host_menu_option.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/bootloader_host_menu_option.png)

This window will appear. Select the new COM port number for your board in the list.

[![The bootloader host application window](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/bootloader_host.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/bootloader_host.png)

Baud rate, data bits, stop bits and parity can all be left as-is. So can \"**Active application**\", and the \"**Security key**\" box can be left unchecked. Click the \"**\...**\" button next to the file to bring up the file selection dialog.

The application file for the bootloader is of type \"**\*.cyacd**\" and it can be found in the firmware directory under \"**\.../CortexM3/ARM_GCC_541/Release**\", assuming you are using *PSoC Creator 4.2* with a *build configuration* set in **Release** mode.

[![The path to the bootloader app file](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/0/path_to_cyacd_file.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/path_to_cyacd_file.png)

The **\*.cyacd** file will automatically be generated whenever the project is built. Note that using the \"**Program**\" button in the main PSoC Creator menu bar does **not** work for bootloaded projects!

The last step in the bootloading process is to click the \"**Program**\" button in the button bar at the top of the Bootloader Host window. You should see messages indicating a successful programming scroll past in the text window at the bottom of the window.

[![Where to find the program button](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/program_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/0/program_button.png)