# Source: https://learn.sparkfun.com/tutorials/redboard-turbo-hookup-guide

## Introduction

If you\'re ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the RedBoard Turbo is an awesome alternative. The RedBoard Turbo uses the ATSAMD21G18, which is an ARM Cortex M0+, 32-bit microcontroller that can run at up to 48MHz. The [RedBoard Turbo](https://www.sparkfun.com/products/14812) is similar to the [SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672), with a few improvements. The RedBoard Turbo steps up the flash memory from the 256kB of internal memory to 4MB of external memory. Along with the UF2 Bootloader, the RedBoard Turbo is even easier to program than before!

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

The RedBoard Turbo equips the ATSAMD21G18 with a USB interface for programming and power, a Qwiic connector, an RTC crystal, WS2812-based addressable RGB LED, 600mA 3.3V regulator, LiPo charger, and a variety of other components.

### Required Materials

In addition to the RedBoard Turbo, you\'ll also need a [Micro-B Cable](https://www.sparkfun.com/products/10215) (as if you don\'t already have dozens in your USB cable drawer!). That\'s all you\'ll need to get started. You can also take advantage of its LiPo charger with a [single-cell Lithium Polymer battery](https://www.sparkfun.com/search/results?term=lithium%20polymer). You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

### Suggested Reading

Before continuing on with this tutorial, you may want to familiarize yourself with some of these topics if they're unfamiliar to you:

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide)

### SAMD21 Mini/Dev Breakout Hookup Guide 

An introduction to the Atmel ATSAMD21G18 microprocessor and our Mini and Pro R3 breakout boards. Level up your Arduino-skills with the powerful ARM Cortex M0+ processor.

## SAMD21 RedBoard Turbo Overview

**Note:** For those interested in the nitty, gritty details of the SAMD21, check out the section from the Dev Breakout\'s [SAMD21 overview](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/samd21-overview) or the [datasheet](https://cdn.sparkfun.com/assets/4/c/9/e/f/SAMD21-Family-DataSheet-DS40001882D.pdf).

Before we get into programming the SAMD21, let\'s first cover some of the features built into the [RedBoard Turbo](https://www.sparkfun.com/products/14812). The RedBoard Turbo is similar to our [SAMD21 Dev Breakout](https://www.sparkfun.com/products/13672), except turbocharged. In this section we\'ll cover powering the board, outlining the I/O pins, and what the various LEDs on the board are for.

### I/O Pins

If you\'ve used any Arduino before, this pinout shouldn\'t surprise you \-- the layout meets the Arduino 1.0 footprint standard, including a separate SPI header and additional I^2^C header. For a quick reference, consult our [graphical datasheet](https://github.com/sparkfun/RedBoard_Turbo/blob/master/Documentation/GraphicalDatasheet-SAMD21TurboDev_1.pdf), which exhaustively shows the capability of each I/O pin and some of the other features on the board.

[![Arduino pinout reference](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/Graphical_Datasheet_Simple.PNG)](https://github.com/sparkfun/RedBoard_Turbo/blob/master/Documentation/GraphicalDatasheet-SAMD21TurboDev_1.pdf)

*Preview of some of the RedBoard Turbo\'s Pin Functionality taken from the [Graphical Datasheet](https://github.com/sparkfun/RedBoard_Turbo/blob/master/Documentation/GraphicalDatasheet-SAMD21TurboDev_1.pdf)*

All **PWM-capable** pins are indicated with a tilde (\~) adjacent to the pin-label. Speaking of \"analog output\", true analog output is available on the A0 pin.

⚡ **5V Output Pin:** The pin for 5V output power is tied directly to the the USB jack. Therefore, if you need 5V power for a shield or to power a device, you will only to be able to draw 5V power from this pin if you are powering the board from the USB jack.

⚡ **3.3V Logic Levels!** When you start interfacing the SAMD21\'s I/O pins with external sensors and other components, keep in mind that each I/O will produce, at most, 3.3V for a high-level output.

When configured as an input, the maximum input voltage for each I/O is 3.6V (VDD+0.3V). If you\'re interfacing the SAMD21 with 5V devices, you may need some [level shifters](https://www.sparkfun.com/products/12009) in between.

### Supplying Power

Power can be supplied to the RedBoard Turbo through either USB, a single-cell (3.7-4.2V) lithium-polymer battery, or an external 5V source via barrel jack. Each of the power supply inputs are available on the top edge of the board (the VIN pin on the power header can also be used). Unlike the [RedBoard](https://www.sparkfun.com/products/15123), the Turbo\'s 5V pin is connected to the USB\'s 5V supply and is not a regulated 5V output.

[![Highlight of Power Supply Options](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/power_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/power_highlight.jpg)

⚡ **Warning** The barrel jack connection on the RedBoard Turbo has a lower input voltage than most Arduino development boards. Make sure that you are using a power supply **below 6V**!

#### USB Power

The USB jack comes in the form of a **micro-B** connector. It should work with one of the many USB phone-charging cables you have lying around, or one of our [Micro-B cables](https://www.sparkfun.com/products/10215). You can plug the other end into a computer USB port, or use a [USB Wall Adapter](https://www.sparkfun.com/products/15312). The USB supply input includes a 500mA PTC resettable fuse \-- if something on or connected to the breakout fails, it should help protect your supply from damage.

[![Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/4/TOL-15311-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html) 

[ TOL-15311 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA USB Micro-B wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

#### Single-Cell Lithium-Polymer (LiPo) Battery Charger

The SAMD21 touts many low-power features, so using it in battery-powered projects should be a common occurence. We\'ve integrated our standard 2-pin JST connector, and a single-cell USB battery charger into the board. Any of our single-cell [lithium polymer batteries](https://www.sparkfun.com/categories/54) can be used to power the board.

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

To charge the battery, simply **connect USB or a 5V wall adapter** while the battery is also connected.

[![Charging a LiPo battery](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-04.jpg)

The \"Charge\" LED should illuminate while the battery is charging, and it should eventually turn off once fully juiced up.

#### Configuring Battery Charge Current

The MCP73831\'s charge current is configured by a resistor value between 66kΩ and 2kΩ, to charge the battery at a rate between 15mA and 500mA, respectively. By default, the board is configured to charge the battery at around **250mA**.

Most batteries shouldn\'t be charged at a rate over 1C (for example, a 110mAh battery\'s 1C charge current would be 110mA). If you need to adjust the charge current, we\'ve added pads for a through-hole resistor. This resistor can be added [in parallel](https://learn.sparkfun.com/tutorials/resistors#series-and-parallel-resistors) with the 3.9kΩ resistor already on board, or the CHG SET resistor can be removed with a soldering iron.

[![](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/CHG_SET.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/CHG_SET.jpg)

If you need a smaller charge current, the charge set resistor *must* be removed, before adding your own. Increasing the charge current can be achieved by adding a resistor in parallel. Here are a few resistor value/charge current examples:

  Charge Current (I~Charge~)   Total Resistance (R~Prog~)   Parallel Resistor
  ---------------------------- ---------------------------- ----------------------------------
  40mA                         25kΩ                         No, must remove CHG SET resistor
  100mA                        10kΩ                         No, must remove CHG SET resistor
  400mA                        2.5kΩ                        6.9kΩ
  500mA                        2kΩ                          4.1kΩ

The charge current is calculated as:\

I~Charge~ = 1000/R~Prog~

\
R~Prog~ is the total programming resistor resistance, which may include the 3.9kΩ resistor in parallel.

#### Current Capabilities

Depending on the task it\'s given, the SAMD21\'s core will usually consume between 3-17mA. There should be plenty of juice left from the 600mA 3.3V regulator to power other sensors or components off the Turbo\'s 3.3V supply rail.

Each I/O pin can sink up to 10mA and source up to 7mA, with one caveat: **each cluster of I/O is limited to sourcing 14mA or sinking 19.5mA**. The GPIO clusters are:

  ----------------------------------------------------------------------------------------------------------
  Cluster           GPIO                                       Cluster Supply (Pin)   Cluster Ground (Pin)
  ----------------- ------------------------------------------ ---------------------- ----------------------
  1                 SWCLK, SWDIO                               VDDIN (44)             GND (42)

  2                 30, 31\                                    VDDIN (44)\            GND (42)\
                    (USB_HOST_EN, TX_LED)                      VDDIO (36)             GND (35)

  3                 D2, D5, D6, D7, D10, D11, D12, D13, D38\   VDDIO (36)\            GND (35)\
                    SCL, SDA, MISO, SCK, MOSI\                 VDDIO (17)             GND (18)
                    (USB_D-, USB_D+)                                                  

  4                 D0, D1, D3, D4                             VDDIO (17)             GND (18)

  5                 A1, A2, A3, A4\                            VDDANA (6)             GNDANA (5)
                    D8, D9                                                            

  6                 A0, A5, AREF\                              VDDANA (6)             GNDANA (5)
                    (RX_LED, RTC1, RTC2)                                              
  ----------------------------------------------------------------------------------------------------------

So, for example, if you\'re sourcing current to four LEDs tied to pins 0, 1, 3, and 4 (cluster 4), the sum of that current must be less than 14mA (\~3.5mA per LED).

### LEDs

Speaking of LEDs, the RedBoard Turbo has a lot of them: a power indicator, pin 13 \"status\" LED, USB transmit and receive LED indicators, a battery charge status indicator, and addressable WS2812 LED.

[![Dev Board LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/LED_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/LED_Highlight.jpg)

#### Status LED

The blue LED driven by the Arduino\'s pin 13 is actually sourced through an N-channel MOSFET, so less of our precious cluster-current is eaten up. The LED still turns on when you write the pin HIGH and off when pin 13 is LOW.

#### Serial UART LEDs

The RX and TX LEDs indicate activity on the USB serial port. They are also addressable within an Arduino sketch, using the macros `PIN_LED_RXL` and `PIN_LED_TXL`. These LEDs are **active-low**, so writing the pin HIGH will turn the LED off.

#### Charge LED

The charge LED is controlled by the board\'s integrated [MCP73831](https://cdn.sparkfun.com/datasheets/Components/General%20IC/33244_SPCN.pdf) battery charger. If a battery is connected and 5V supplied (via USB or the external jack), it will illuminate when a battery is being charged and should turn off once fully-charged.

#### Addressable WS2812 LED

The RGB LED uses the WS2812, which is connected to pin 44 which can be used for any purpose.

[![RGB LED Highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/LED_Highlight_1_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/LED_Highlight_1_.jpg)

## UF2 Bootloader and Drivers

**Heads up!** Please be aware that the RedBoard Turbo is **NOT currently supported on Windows 8** due to a lack of support drivers for those specific OS\'s.

The RedBoard Turbo is now easier than ever to program, thanks the UF2 bootloader. With this bootloader, the RedBoard Turbo shows up on your computer as a USB storage device **without having to install drivers** for Windows 10, Mac, and Linux!

From the Arduino IDE, you\'ll still need to select the correct port on your machine, but you can just as easily use another programming language such as CircuitPython or MakeCode, which will be available in the near future.

### [][Windows 7](#windows-7)

If you are using a Windows 7 OS, you will need to install the SAMD drivers using the [SAMD Windows 7 Installer](https://github.com/sparkfun/samd_windows7_installer/releases). Head over to the GitHub repo to install the executable.

[SAMD Windows 7 Installer](https://github.com/sparkfun/samd_windows7_installer/releases)

Scroll down the page to the assets in the **Latest release** and click on the **\'.exe** to download. The version number may be different depending on the release. The image below shows *sparkfun_drivers_1.0.5.3.exe* .

[![Windows 7 Driver Download](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/7/Windows_7_SAMD_Drivers_Download_Versions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/7/Windows_7_SAMD_Drivers_Download_Versions.jpg)

*Click on the image for a closer view.*

After downloading, click on the executable and follow the prompts to install. The steps to install are the same even though the following images show drivers for **v1.0.5.1**.

[![SparkFun Driver Executable](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_SparkFun_SAMD_Driver_Executable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_SparkFun_SAMD_Driver_Executable.jpg)

You will receive a warning from Windows. Click **yes** to continue.

[![Windows 7 Warning](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Warning.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Warning.jpg)

Another window will pop up. Read through the license and click \"**I Agree**\".

[![License Agreement](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Agreement.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Agreement.jpg)

When ready, hit the **Install** button.

[![Install SAMD Drivers](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Agreement_Install.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Agreement_Install.jpg)

Another window will pop up. Click on \"**Install this driver software anyway**\" to continue.

[![Windows Warning](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_SAMD_Drivers_Install_Anyway.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_SAMD_Drivers_Install_Anyway.jpg)

Your Windows 7 will begin installing the driver. This should take a few seconds. When the drivers have installed, hit the \"**Close**\" button to exit out of the installer.

[![Successful Install](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Successful_Install.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/Windows_7_Driver_Successful_Install.jpg)

### What is UF2?

UF2 stands for USB Flashing Format, which was developed by Microsoft for PXT (now known as MakeCode) for flashing microcontrollers over the Mass Storage Class (MSC), just like a removable flash drive. The file format is unique, so unfortunately, you cannot simply drag and drop a compiled binary or hex file onto the Turbo. Instead, the format of the file has extra information to tell the processor where the data goes, in addition to the data itself.

For Arduino users, the UF2 bootloader is **BOSSA compatible**, which the Arduino IDE expects on ATSAMD boards. For more information about UF2, you can read more from the [MakeCode blog](https://makecode.com/blog/one-chip-to-flash-them-all), as well as the [UF2 file format specification](https://github.com/Microsoft/uf2).

## Setting Up Arduino

While the SAMD21 alone is powerful enough, what truly makes it special is its growing support in the Arduino IDE. With just a couple click\'s, copies, and pastes, you can add ARM Cortex-M0+-support to your Arduino IDE. This page will list every step required for getting RedBoard Turbo support into your Arduino IDE.

**Update Arduino!** This setup requires *at least* Arduino version 1.6.4 or later. We\'ve tested it on 1.6.5 and the latest version -- 1.8.8.

If you\'re running an older version of Arduino, consider visiting [arduino.cc](https://www.arduino.cc/en/Main/Software) to get the latest, greatest release.

### Install Arduino SAMD Board Add-Ons

First, you\'ll need to install a variety of tools, including [low-level ARM Cortex libraries](http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php) full of generic code, [arm-gcc](https://launchpad.net/gcc-arm-embedded) to compile your code, and [bossa](http://www.shumatech.com/web/products/bossa) to upload over the bootloader. These tools come packaged along with Arduino\'s SAMD board definitions for the Arduino Zero.

To install the Arduino SAMD board definitions, navigate to your board manager (**Tools** \> **Board** \> **Boards Manager\...**), then find an entry for **Arduino SAMD Boards (32-bits ARM Cortex-M0+)**. Select it, and install the latest version (recently updated to *v1.6.19*).

[![Installing the Arduino SAMD boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/4/arduino-arduino-board-install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/arduino-arduino-board-install.png)

Downloading and installing the tools may take a couple minutes \-- arm-gcc in particular will take the longest, it\'s about 250MB unpacked.

Once installed, Arduino-blue \"Installed\" text should appear next to the SAMD boards list entry.

### Install SparkFun Board Add-On

Now that your ARM tools are installed, one last bit of setup is required to add support for the SparkFun SAMD boards. First, open your Arduino preferences (**File** \> **Preferences**). Then find the **Additional Board Manager URLs** text box, and paste the below link in:

    https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json

[![Arduino IDE Preferences Additional Moard Manager URLs](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/arduino-board-add.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/arduino-board-add.png)

Then hit \"OK\", and travel back to the **Board Manager** menu. You should (but probably won\'t) be able to find a new entry for **SparkFun SAMD Boards**. If you don\'t see it, close the board manager and open it again. ¯\\\_(ツ)\_/¯.

[![Installing the SparkFun SAMD Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/4/sparkfun-arduino-board-install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/sparkfun-arduino-board-install.png)

This installation should be much faster; you\'ve already done the heavy lifting in the previous section.

### Select the Board and Serial Port

Once the board is installed, you should see a new entry in your **Tools** \> **Board** list. **Select your SparkFun RedBoard Turbo.**

[![RedBoard Turbo board menu entry](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/Board_Selection.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/Board_Selection.png)

Finally, select your Turbo\'s port. Navigate back up to the **Tool** \> **Port** menu. The port menu may magically know which of your ports (if you have more than one) is the RedBoard Turbo board. On a Windows machine, the serial port should come in the form of \"**COM#**\". On a Mac or Linux machine, the port will look like \"**/dev/cu.usbmodem####**\".

[![Selecting the RedBoard Turbo port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/Port_Selection.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/Port_Selection.png)

Once you find it, select it!

## Example: Blink

As with any development board, if you can blink an LED, you\'re well on your way to controlling the rest of the world. Since the RedBoard Turbo has 3 user-controllable LEDs, let\'s blink them all!

[![RedBoard Turbo with all LEDs on](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-02.jpg)

The RX and TX LEDs are on pins 25 and 26, respectively, a couple pre-defined macros (`PIN_LED_RXL` and `PIN_LED_TXL`) can be used to access those pins, just in case you forget the numbers.

Here\'s a quick example sketch to blink the LEDs and make sure your environment is properly set up. Copy and paste from below, and upload!

    language:c
    const int BLUE_LED = 13; // Blue "stat" LED on pin 13
    const int RX_LED = PIN_LED_RXL; // RX LED on pin 25, we use the predefined PIN_LED_RXL to make sure
    const int TX_LED = PIN_LED_TXL; // TX LED on pin 26, we use the predefined PIN_LED_TXL to make sure

    bool ledState = LOW;

    void setup() 
    

    void loop() 
    

After hitting the \"Upload\" button, wait a handful of seconds while the code compiles and sends. While the code uploads, you should see the blue LED flicker. Once you\'ve verified that the IDE is all set up, you can start exploring the world of the ATSAMD21!

## Example: Serial Ports

One of the SAMD21\'s most exciting features is SERCOM \-- its multiple, configurable serial ports. The Arduino IDE equips the SAMD21 with two hardware serial ports, by default, plus a third \"USB serial port\" for communicating between the serial monitor.

Each of these serial ports has a unique `Serial` object which you\'ll refer to in code:

  Serial Object   Serial Port                   RX Pin   TX Pin
  --------------- ----------------------------- -------- --------
  `SerialUSB`     USB Serial (Serial Monitor)            
  `Serial1`       Hardware Serial Port 1        0        1

There are a couple critical things to notice here. First of all, if you\'re trying to use the Serial Monitor to debug, you\'ll need to use `SerialUSB.begin(<baud>)` and `SerialUSB.print()`. (Thankfully find/replace exists for adjusting example code.)

Here\'s a quick example demonstrating the differences between [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) and `Serial1`. It is designed to route data from `Serial1` to the Serial Monitor, and vice-versa.

    language:c
    void setup()
    

    void loop()
    
        // Print a message stating what we're sending:
        SerialUSB.println("Sending " + toSend + " to Serial1");

        // Send the assembled string out over the hardware
        // Serial1 port (TX pin 1).
        Serial1.print(toSend);
      }

      if (Serial1.available()) // If data is sent from device
      
        // Print a message stating what we've received:
        SerialUSB.println("Received " + toSend + " from Serial1");
      }
    }

Then try typing something into the serial monitor. Even with nothing connected to the hardware serial port, you should see what you typed echoed back at you.

[![Example serial monitor](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-monitor-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-monitor-example.png)

You can further test this sketch out by connecting an [3.3V FTDI Basic](https://www.sparkfun.com/products/9873) or any other serial device to the SAMD21\'s pins 0 (RX) and 1 (TX). By opening up a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows), any data sent from the FTDI should end up in your Arduino Serial Monitor, and data sent to your Arduino Serial Monitor will route over to the FTDI. Here\'s a table that shows what pins to connect together.

  RedBoard Turbo Pins   3.3V FTDI (or any USB-to-Serial Converter) Pins
  --------------------- -------------------------------------------------
  1/TX                  RXI
  0/RX                  TXO
  GND                   GND

## Example: Analog Input and Output

While it still has PWM-based \"analog outputs\", the SAMD21 also features true analog output in the form of a digital-to-analog converter (DAC). This module can produce an analog voltage between 0 and 3.3V. It can be used to produce audio with more natural sound, or as a kind of \"digital potentiometer\" to control analog devices.

The DAC is only available on the **Arduino pin A0**, and is controlled using `analogWrite(A0, <value>)`. The DAC can be set up to 10-bit resolution (make sure to call [analogWriteResolution(10)](https://www.arduino.cc/en/Reference/AnalogWriteResolution) in your setup), which means values between 0 and 1023 will set the voltage to somewhere between 0 and 3.3V.

In addition to the DAC, the SAMD21\'s ADC channels also stand apart from the ATmega328: they\'re equipped with up to **12-bit resolution**. That means the analog input values can range from 0-4095, representing a voltage between 0 and 3.3V. To use the ADC\'s in 12-bit mode, make sure you call [analogReadResolution(12)](https://www.arduino.cc/en/Reference/AnalogReadResolution) in your setup.

### Serial Plotting the DAC

The **Serial Plotter** in this example requires Arduino 1.6.6 or later. Visit [arduino.cc](https://www.arduino.cc/en/Main/Software) to get the latest, greatest version.

Here\'s an example that demonstrates both the 10-bit DAC and the 12-bit ADC. To set the experiment up, **connect A0 to A1** \-- we\'ll drive A0 with an analog voltage, then read it with A1. It\'s the simplest circuit we\'ve ever put in a tutorial:

[![A0 jumped to A1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-01.jpg)

*Jumping a temporary connection between A0 (our DAC) and A1.*

Then copy and paste the code below into your Arduino IDE, and upload!

    language:c
    // Connect A0 to A1, then open the Serial Plotter.

    #define DAC_PIN A0 // Make code a bit more legible

    float x = 0; // Value to take the sin of
    float increment = 0.02;  // Value to increment x by each time
    int frequency = 440; // Frequency of sine wave

    void setup() 
    

    void loop() 
    

This sketch produces a sine wave output on A0, with values ranging from 0 to 3.3V. Then it uses A1 to read that output into its 12-bit ADC, and convert it into a voltage between 0 and 3.3V.

You can, of course, open the serial monitor to view the voltage values stream by. But if the the sine wave is hard to visualize through text, check out Arduino\'s new **Serial Plotter**, by going to **Tools** \> **Serial Plotter**.

[![Opening the Serial Plotter](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-plotter-open.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-plotter-open.png)

And take in the majesty of that sine wave.

[![Sine wave plotted in Plotter](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-plotter.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/4/serial-plotter.png)

## Example: Addressable RGB LED

**Heads up!** Since the addressable WS2812 LED is attached to pin 44, we will be using the NeoPixel library. The FastLED will not be able to work at that high of an I/O number for the SAMD21

In this last example, we\'ll take a look at how to use the RGB LED on the RedBoard Turbo. The RGB LED comes in the form of a WS2812, which could be great as a status LED or for debugging if you don\'t want or need to use serial terminal. In the example below, we\'ll test the functionality of the LED by using the rainbow fade code below. To use this code, you will need to install the [NeoPixel library](https://github.com/adafruit/Adafruit_NeoPixel). You can obtain these libraries through the Arduino Library Manager. Search for NeoPixel and you should be able to install the latest version. If you prefer downloading the libraries manually you can grab them from the [GitHub repository](https://github.com/adafruit/Adafruit_NeoPixel):

[Download NeoPixel Library (ZIP)](https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip)

Once the library has been installed, copy and paste the following code into your Arduino IDE.

    language:c
    #include <Adafruit_NeoPixel.h>
    #define LEDPIN RGB_LED // connect the Data from the strip to this pin on the Arduino
    #define NUMBER_PIEXELS 1 // the number of pixels in your LED strip
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

    int wait = 10; // how long we wait on each color (milliseconds)

    void setup() 

    void loop() 
        strip.show();
        delay(wait);
      }
    }

    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos)  else if(WheelPos < 170)  else 
    }

Once uploaded, you should see the LED changing colors. Notice in the code, the RGB LED\'s pin is defined using **RGB_LED**. You could also call it using `LED4` or it\'s pin number, `44`.

[![Controlling RGB LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/RedBoard_Turbo_Hookup_Guide-03.jpg)

## Troubleshooting

For troubleshooting tips, checkout the [SAMD21 Troubleshooting guide here](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/troubleshooting) for common issues that you might run into when using the SAMD21 with Arduino. The only exception is that the RedBoard Turbo does no require drivers so tips for re-installing drivers will not apply.

[SAMD21 Mini/Dev Breakout Hookup Guide: Troubleshooting](https://learn.sparkfun.com/tutorials/samd21-minidev-breakout-hookup-guide/troubleshooting)

## Reinstalling Circuit Python 

If you decided to do your developing in Arduino, you\'ll find that upon loading up your first sketch via Serial Upload, that the RedBoard Turbo no longer pops up like a removable USB device as it did previously. That\'s to be expected, so don\'t panic. In this section we\'ll walk through a few simple steps to getting Circuit Python re-uploaded onto your computer.

### Reset board to Bootloader

We want the board to reset to the UF2 bootloader which as mentioned above, enables the board to act like a flash drive. To do that we\'ll take the steps mentioned underneath the troubleshooting section: we\'ll *double* tap the reset button. Shortly after you do that, the board will pop up as a USB drive named *TURBOBOOT*.

### Drag and Drop Circuit Python Firmware

From here, it\'s a simple drag and drop to success. Download the Circuit Python Firmware below (also found in the Github Repo under the Firmware folder). Drag the contents named `turbo-boot_cp.uf2` onto your *TURBOBOOT* USB drive and the folder should disappear momentarily only to reappear as a *CIRCUITPY* USB drive instead.

[Circuit Python Firmware (ZIP)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/1/turbo-boot_cp.zip)