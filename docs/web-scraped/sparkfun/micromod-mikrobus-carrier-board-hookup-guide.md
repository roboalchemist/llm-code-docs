# Source: https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroMod mikroBUS™ Carrier Board Hookup Guide

# MicroMod mikroBUS™ Carrier Board Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [ MAKIN-STUFF]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2003&name=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2003 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2003&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2003&t=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2003&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F0%2F3%2Fassembly-prog_click_UART.jpg&description=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Pin It")

## Introduction

**Advanced Product:** Novice users, may find the amount information contained in this tutorial somewhat daunting. This board is relatively complex and involves compatibility with three separate ecosystems and can be utilize two different development environments.

- For beginners, who have never programmed; we highly recommend that these users begin with a simpler microcontroller learning kit; such as the [SparkFun Inventor\'s Kit (SIK)](https://www.sparkfun.com/products/15631). The kit includes a simpler microcontroller development board like the [Arduino Uno](https://www.sparkfun.com/products/11224) or [SparkFun RedBoard](https://www.sparkfun.com/products/15123).
- For slightly more advanced users who aren\'t familiar with the [MicroMod ecosystem](https://www.sparkfun.com/micromod), but are at least familiar with programming; we recommend that these users begin with a basic MicroMod board combination. The [MicroMod Qwiic carrier board](https://www.sparkfun.com/products/17723) and [SAMD51 processor board](https://www.sparkfun.com/products/16791) are a great introductory board combination from the [MicroMod product line](https://www.sparkfun.com/categories/tags/micromod).

Introducing the our most versatile development board, the [MicroMod mikroBUS™ Carrier Board](https://www.sparkfun.com/products/18710)! This new board takes advantage of the [MicroMod](https://www.sparkfun.com/micromod), [Qwiic](https://www.sparkfun.com/qwiic), and the [mikroBUS™](https://www.sparkfun.com/categories/tags/mikrobus) ecosystems and allows users to take advantage of the growing number of 7 [MicroMod processor boards](https://www.sparkfun.com/categories/tags/processor-board), 83 [Qwiic *(add-on)* boards](https://www.sparkfun.com/categories/tags/qwiic), and [1079 available](https://www.mikroe.com/click-boards) [Click boards™](https://www.sparkfun.com/categories/tags/click) *(as of September 2021)*, which equates to +51M different board combinations.

[![SparkFun MicroMod mikroBUS Carrier Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/2/4/8/18710-SparkFun_MicroMod_mikroBUS_Carrier_Board-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-mikrobus-carrier-board.html)

### [SparkFun MicroMod mikroBUS Carrier Board](https://www.sparkfun.com/sparkfun-micromod-mikrobus-carrier-board.html) 

[ DEV-18710 ]

The MicroMod mikroBUS Carrier Board takes advantage of the MicroMod, Qwiic, and mikroBUS ecosystems making it easy to rapidly...

**Retired**

The [mikroBUS™ standard](https://www.mikroe.com/mikrobus) was developed by [MikroElektronika](https://www.mikroe.com/). Similar to our [Qwiic](https://www.sparkfun.com/qwiic) and [MicroMod](https://www.sparkfun.com/micromod) interfaces, [mikroBUS™](https://www.sparkfun.com/categories/tags/mikrobus) provides a standardized connection for add-on [Click boards™](https://www.sparkfun.com/categories/tags/click) to be hooked up to a microcontroller based development board.

[![1000clicks-logo.png](https://cdn.mikroe.com/img/1000-click-boards-presskit/1000clicks-logo.png)](https://www.mikroe.com/1000-click-boards)

[*Image source: <https://www.mikroe.com/1000-click-boards>*]

For more details, check out their [blog post on the 1000th Click board™ and the origins of the mikroBUS™ standard](https://www.mikroe.com/1000-click-boards) and [mikroBUS™ standard specifications](https://download.mikroe.com/documents/standards/mikrobus/mikrobus-standard-specification-v200.pdf).

### Required Materials

To get started, users will need a few of items listed below. *(You may already have a some of these items; read through the guide and modify your cart accordingly.)*

#### MicroMod Processor Board

Like other [MicroMod Carrier Boards](https://www.sparkfun.com/categories/tags/carrier-board), a [Processor Board](https://www.sparkfun.com/categories/tags/processor-board) is required for the product to operate. Users will need a Processor Board *(of their choice)* to attach to the [MicroMod M.2 connector](https://www.sparkfun.com/products/16549); *since, one is not included with this product*. Below, are few options; however, we recommend the [STM32 processor board](https://www.sparkfun.com/products/17713). Currently, it is the only processor board supported by [Necto Studio](https://www.mikroe.com/necto) and the Arduino IDE.

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/8/1/7/17713-SparkFun_MicroMod_STM32_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor-dev-17713.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor-dev-17713.html) 

[ DEV-17713 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

**Retired**

[![SparkFun MicroMod Teensy Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/2/16402-SparkFun_MicroMod_Teensy_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html)

### [SparkFun MicroMod Teensy Processor](https://www.sparkfun.com/sparkfun-micromod-teensy-processor.html) 

[ DEV-16402 ]

This board leverages the awesome computing power of the NXP iMXRT1062 chip (ARM Cortex-M7) and pairs it with the M.2 MicroMod...

[ [\$24.95] ]

[![SparkFun MicroMod nRF52840 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/9/2/1/16984-SparkFun_MicroMod_nRF52840_Processor-04.jpg)](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html)

### [SparkFun MicroMod nRF52840 Processor](https://www.sparkfun.com/sparkfun-micromod-nrf52840-processor.html) 

[ WRL-16984 ]

The SparkFun MicroMod nRF52840 Processor offers a powerful combination of ARM Cortex-M4 CPU and 2.4 GHz Bluetooth transceiver...

[ [\$29.50] ]

[![SparkFun MicroMod STM32 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/1/2/2/STM32F405-_01.jpg)](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html)

### [SparkFun MicroMod STM32 Processor](https://www.sparkfun.com/sparkfun-micromod-stm32-processor.html) 

[ DEV-21326 ]

The SparkFun MicroMod STM32 Processor Board is ready to rock your MicroMod world with its ARM® Cortex®-M4 32-bit RISC core!

[ [\$20.50] ]

[![SparkFun Arduino IoT Weather Station](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/7/9/5/22636-_KIT-_01.jpg)](https://www.sparkfun.com/sparkfun-arduino-iot-weather-station.html)

### [SparkFun Arduino IoT Weather Station](https://www.sparkfun.com/sparkfun-arduino-iot-weather-station.html) 

[ KIT-22636 ]

Whether you\'re an agriculturalist, a professional meteorologist, or a weather hobbyist, building a weather station can be a r...

[ [\$129.95] ]

#### Required Hardware

A Phillips screw driver is necessary to attach the Processor board to the Carrier Board.

[![MicroMod Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/6/1/1/19012-MicroMod_Screwdriver-01.jpg)](https://www.sparkfun.com/micromod-screwdriver.html)

### [MicroMod Screwdriver](https://www.sparkfun.com/micromod-screwdriver.html) 

[ TOL-19012 ]

This is a pocket size magnetic tip Philips head screwdriver designed to be used specifically with the MicroMod ecosystem.

[ [\$0.75] ]

[![SparkFun MicroMod mikroBUS Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/2/4/8/18710-SparkFun_MicroMod_mikroBUS_Carrier_Board-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-mikrobus-carrier-board.html)

### [SparkFun MicroMod mikroBUS Carrier Board](https://www.sparkfun.com/sparkfun-micromod-mikrobus-carrier-board.html) 

[ DEV-18710 ]

The MicroMod mikroBUS Carrier Board takes advantage of the MicroMod, Qwiic, and mikroBUS ecosystems making it easy to rapidly...

**Retired**

##### JTAG Programming

To program the [STM32 processor board](https://www.sparkfun.com/products/17713) *(recommended)* through [Necto Studio](https://www.mikroe.com/necto) *(preferred)*, users will need a JTAG programmer. Below are programmers that are compatible with the Necto Studio software.

**Apple Mac/Linux:** Users with a Mac or Linux OS, should purchase the CODEGRIP programmer. The mikroProg is only compatible with Windows PCs.

[![MIKROE mikroProg for STM32](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/7/0/7/19104-mikroBus_Hookup_Guides-01.jpg)](https://www.sparkfun.com/mikroe-mikroprog-for-stm32.html)

### [MIKROE mikroProg for STM32](https://www.sparkfun.com/mikroe-mikroprog-for-stm32.html) 

[ PGM-19104 ]

MIKROE mikroProg for STM32 is a fast USB 2.0 programmer and hardware debugger based on ST-LINK v2.

**Retired**

[![MIKROE CODEGRIP for STM32](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/7/0/8/19105-MIKROE_CODEGRIP_for_STM32-01.jpg)](https://www.sparkfun.com/mikroe-codegrip-for-stm32.html)

### [MIKROE CODEGRIP for STM32](https://www.sparkfun.com/mikroe-codegrip-for-stm32.html) 

[ PGM-19105 ]

MIKROE CODEGRIP for STM32 is a fast USB-C and WiFi programmer and hardware debugger that supports STM32 Cortex M0, M3, M4, an...

**Retired**

Users will also need some [soldering equipment](https://www.sparkfun.com/categories/49) and a [JTAG header](https://www.sparkfun.com/categories/379) to connect the programmer to the board. Additionally, with the *(recommended)* programmers, an adapter is needed to convert the .1\" *(100 mil)* header spacing of the programmer\'s cable to the .05\" *(50 mil)* header spacing of the JTAG pins on the MicroMod mikroBUS™ carrier board.

**Note:** Users should verify that the pinout for the programmer and adapter match up to the corresponding pins of the MicroMod mikroBUS™ carrier board to avoid damaging the MCU.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

[![Straight Header - Male (PTH, 0.05in., 2x5-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/0/0/15362-Male_2x5_1.27mm_headers-01.jpg)](https://www.sparkfun.com/header-2x5-pin-male-1-27mm.html)

### [Straight Header - Male (PTH, 0.05in., 2x5-Pin)](https://www.sparkfun.com/header-2x5-pin-male-1-27mm.html) 

[ PRT-15362 ]

This is a super small, 2x5 pin male PTH header. This header is in the common configuration for JTAG applications.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.05in., 2x5-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/0/1/15363-Header_-_2x5_Pin__Female__1.27mm__-01.jpg)](https://www.sparkfun.com/header-2x5-pin-female-1-27mm.html)

### [Straight Header - Female (PTH, 0.05in., 2x5-Pin)](https://www.sparkfun.com/header-2x5-pin-female-1-27mm.html) 

[ PRT-15363 ]

This is a super small, 2x5 pin female PTH header. This header is in the common configuration for JTAG applications.

[ [\$1.75] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

[![MIKROE 50-100mil Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/4/6/19220-MIKROE_50-100mil_Adapter.jpeg)](https://www.sparkfun.com/mikroe-50-100mil-adapter.html)

### [MIKROE 50-100mil Adapter](https://www.sparkfun.com/mikroe-50-100mil-adapter.html) 

[ PGM-19220 ]

This MIKROE 50-100mil Adapter allows you to connect a mikroProg for STM32 programmer and hardware debugger to a Cortex debug ...

**Retired**

##### USB Programming

To program a MicroMod processor through the Arduino IDE *(not the preferred method)*, a USB-C cable is needed to connect the Carrier Board to a computer.

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

##### Click Board™

We recommend purchasing a Click board™ to utilize the mikroBUS™ socket. Feel free to choose from any of the available [Click boards™](https://www.sparkfun.com/categories/tags/click) in our catalog. Below are a few options.

**Note:** If users intend to use the Arduino IDE, we recommend that novice users select a [Click board™](https://www.sparkfun.com/categories/tags/click) that is supported with an Arduino library. Otherwise, users will have difficulties programming their board to utilize the associated Click board™.

[![TIMI-MB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/8/3/19253-TIMI-Click-01.jpg)](https://www.sparkfun.com/timi-mb.html)

### [TIMI-MB](https://www.sparkfun.com/timi-mb.html) 

[ LCD-19253 ]

TIMI-MB (mikroBUS™) is a 0.96" TFT LCD display module that is driven directly by a PIXXI-28 graphics processor from 4D La...

[\$29.95] [ [\$25.95] ]

[![TIMI-MB Starter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/8/4/19254-TIMI-Click_Starter_Kit-01.jpg)](https://www.sparkfun.com/timi-mb-starter-kit.html)

### [TIMI-MB Starter Kit](https://www.sparkfun.com/timi-mb-starter-kit.html) 

[ DEV-19254 ]

TIMI-MB (mikroBUS™) is a 0.96" TFT LCD display module that is driven directly by a PIXXI-28 graphics processor from 4D La...

[\$39.95] [ [\$33.95] ]

[![TIMI to MikroBUS Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/8/7/19257-TIMI_to_Click_Adapter-01.jpg)](https://www.sparkfun.com/timi-to-mikrobus-adapter.html)

### [TIMI to MikroBUS Adapter](https://www.sparkfun.com/timi-to-mikrobus-adapter.html) 

[ DEV-19257 ]

This adapter supports the mikroBUS™ Click socket with a MatesBUS interface to connect products of any TIMI model directly t...

[ [\$9.95] ]

[![SparkFun MicroMod mikroBUS Starter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/6/7/0/19935-SparkFun_MicroMod_mikroBUS_Starter_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-mikrobus-starter-kit.html)

### [SparkFun MicroMod mikroBUS Starter Kit](https://www.sparkfun.com/sparkfun-micromod-mikrobus-starter-kit.html) 

[ KIT-19935 ]

The SparkFun MicroMod mikroBUS™ Starter Kit is designed to give you just what you need to start using the MicroMod and Clic...

[\$79.95] [ [\$59.95] ]

**Note:** If users intend to use [Click board™](https://www.sparkfun.com/categories/tags/click), with code that requires a serial data output, there are no serial pins broken out on the board besides the mikroBUS™ socket. Therefore, it is recommended that users also purchase the [MIKROE Terminal Click](https://www.sparkfun.com/products/18961), a **3.3V** serial-to-UART adapter, jumper wires, and corresponding USB cable to access the serial data pins from the mikroBUS™ socket. Below, are a few options from our catalog:

\

[![SparkFun Serial Basic Breakout - CH340C and USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/2/15096-SparkFun_Serial_Basic_Breakout_-_CH340C_and_USB-C-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html)

### [SparkFun Serial Basic Breakout - CH340C and USB-C](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html) 

[ DEV-15096 ]

This SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G and takes advantage of the ha...

[ [\$10.50] ]

[![SparkFun FTDI Basic Breakout - 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/9/5/8/09873-01a.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html)

### [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html) 

[ DEV-09873 ]

This is the newest revision of our \[FTDI Basic\](https://www.sparkfun.com/products/retired/8772). We now use a SMD 6-pin heade...

[ [\$18.50] ]

[![SparkFun Serial Basic Breakout - CH340G](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/8/8/14050-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html)

### [SparkFun Serial Basic Breakout - CH340G](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html) 

[ DEV-14050 ]

The SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G IC from WCH.

[ [\$9.25] ]

[![MIKROE Terminal Click](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/5/2/6/18961_-_Terminal_Click_2_.jpg)](https://www.sparkfun.com/mikroe-terminal-click.html)

### [MIKROE Terminal Click](https://www.sparkfun.com/mikroe-terminal-click.html) 

[ DEV-18961 ]

MIKROE Terminal Click is a mikroBUS™ socket expansion board.

**Retired**

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

[![USB Mini-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/2/9/13243-01.jpg)](https://www.sparkfun.com/usb-mini-b-cable-6.html)

### [USB Mini-B Cable - 6\"](https://www.sparkfun.com/usb-mini-b-cable-6.html) 

[ CAB-13243 ]

This is a USB 2.0 type B to Mini-B 5-pin black cable. You know, the mini-B connector that usually comes with USB Hubs, Camera...

[ [\$2.50] ]

#### Optional Hardware

To connect [Qwiic breakout boards](https://www.sparkfun.com/qwiic) for your MicroMod project, [Qwiic cables](https://www.sparkfun.com/categories/tags/qwiic-cables) are required.

**Note:** If users intend to use Necto Studio, we recommend that novice users select [Qwiic products](https://www.sparkfun.com/categories/tags/qwiic) that are supported with a MIKROE library. Otherwise, users will have difficulties programming their board to utilize the associated Qwiic board.

[![SparkFun GPS Breakout - NEO-M9N, U.FL (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/9/3/15712-SparkFun_GPS_Breakout_-_NEO-M9N__U.FL__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-neo-m9n-u-fl-qwiic.html)

### [SparkFun GPS Breakout - NEO-M9N, U.FL (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-neo-m9n-u-fl-qwiic.html) 

[ GPS-15712 ]

The SparkFun NEO-M9N GPS Breakout is a high quality GPS board with equally impressive configuration options.

[ [\$70.95] ]

[![SparkFun Qwiic Mini ToF Imager - VL53L5CX](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/6/1/2/19013-SparkFun_Qwiic_Mini_ToF_Imager_-_VL53L5CX-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-mini-tof-imager-vl53l5cx.html)

### [SparkFun Qwiic Mini ToF Imager - VL53L5CX](https://www.sparkfun.com/sparkfun-qwiic-mini-tof-imager-vl53l5cx.html) 

[ SEN-19013 ]

The SparkFun Qwiic Mini ToF Imager is built around VL53L5CX from ST Electronics; a state of the art, Time-of-Flight (ToF), mu...

[ [\$25.95] ]

[![SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/2/9/16466-SparkFun_Environmental_Sensor_Breakout_-_BME680__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html)

### [SparkFun Environmental Sensor Breakout - BME680 (Qwiic)](https://www.sparkfun.com/sparkfun-environmental-sensor-breakout-bme680-qwiic.html) 

[ SEN-16466 ]

This SparkFun Environmental Sensor is a breakout for the 4-in-1 BME680 gas sensor from Bosch.

[ [\$22.95] ]

[![SparkFun Micro OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/2/1/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14532)

### [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532) 

[ LCD-14532 ]

The SparkFun Qwiic Micro OLED Breakout is a Qwiic enabled version of our popular MicroView and micro OLED display!

**Retired**

[![Qwiic Cable - Grove Adapter (100mm)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/7/5/15109-Qwiic_Cable_-_Grove_Adapter__150mm_-01.jpg)](https://www.sparkfun.com/qwiic-cable-grove-adapter-100mm.html)

### [Qwiic Cable - Grove Adapter (100mm)](https://www.sparkfun.com/qwiic-cable-grove-adapter-100mm.html) 

[ PRT-15109 ]

The Qwiic to Grove Adapter Cable allows interoperability between the SparkFun Qwiic Connect System and the I2C based Grove bo...

[ [\$1.95] ]

[![Flexible Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/7/17260-Flexible_Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html)

### [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html) 

[ PRT-17260 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.50] ]

[![Flexible Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/0/7/8/17912-Flexible_Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-breadboard-jumper-4-pin.html)

### [Flexible Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/flexible-qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-17912 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![Flexible Qwiic Cable - Female Jumper (4-pin, Heat Shrink)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/1/9/4/22726-_CAB-_01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin-heat-shrink.html)

### [Flexible Qwiic Cable - Female Jumper (4-pin, Heat Shrink)](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin-heat-shrink.html) 

[ CAB-22726 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and female connectors o...

[ [\$1.95] ]

A [single-cell Lithium-ion battery](https://www.sparkfun.com/categories/tags/lithium-polymer) can be connected to the Qwiic Carrier Board for portability.

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

To modify the jumpers, users will need [soldering equipment](https://www.sparkfun.com/categories/49) and/or a [knife](https://www.sparkfun.com/categories/379).

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

### Suggested Reading

The [MicroMod ecosystem](https://www.sparkfun.com/micromod) is a unique way to allow users to customize their project to their needs. The [Qwiic connect system](https://www.sparkfun.com/qwiic) is a simple method for interfacing with I^2^C devices. The [mikroBUS™ socket](https://www.mikroe.com/mikrobus) is a standardized interface for the MIKROE [Click boards™](https://www.sparkfun.com/categories/tags/click). Click on the banners below for more information on each ecosystem.

[![MicroMod Logo](https://cdn.sparkfun.com/r/500-70/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)

\

[![Qwiic Logo](https://cdn.sparkfun.com/r/500-70/assets/custom_pages/2/7/2/qwiic-logo.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)

\

[![mikroBUS Logo](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/3/mikroBUS_logo.png "Click to learn more about the mikroBUS ecosystem!")](https://www.mikroe.com/mikrobus)

\

For users who aren\'t familiar with the following concepts, we also recommend reading the following tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[](https://learn.sparkfun.com/tutorials/designing-with-micromod)

### Designing with MicroMod 

This tutorial will walk you through the specs of the MicroMod processor and carrier board as well as the basics of incorporating the MicroMod form factor into your own PCB designs!

[](https://learn.sparkfun.com/tutorials/micromod-stm32-processor-hookup-guide)

### MicroMod STM32 Processor Hookup Guide 

Get started with the MicroMod Ecosystem and the STM32 Processor Board!

[](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio)

### Getting Started with Necto Studio 

Necto Studio is a user friendly development environment for users looking to get started with MikroElektronika\'s MIKROE products.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2003&name=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2003 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft2003&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2003&t=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2003&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F0%2F0%2F3%2Fassembly-prog_click_UART.jpg&description=MicroMod+mikroBUS%E2%84%A2+Carrier+Board+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/i) [Hardware Overview](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/hardware-overview) [Hadware Assembly](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/hadware-assembly) [Software Overview](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/software-overview) [Necto Studio Example](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/necto-studio-example) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/resources-and-going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Development](https://learn.sparkfun.com/tutorials/tags/development)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MicroMod](https://learn.sparkfun.com/tutorials/tags/micromod)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]