# Source: https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Getting Started with Necto Studio

# Getting Started with Necto Studio

[≡ Pages](#)

Contributors: [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2253&name=Getting+Started+with+Necto+Studio "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2253 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+Necto+Studio&url=http%3A%2F%2Fsfe.io%2Ft2253&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2253&t=Getting+Started+with+Necto+Studio "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2253&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F2%2F5%2F3%2Flogo.PNG&description=Getting+Started+with+Necto+Studio "Pin It")

## Introduction

### Necto Studio

[Necto Studio](https://www.mikroe.com/necto) is a productive cross-platform integrated developing environment provided by MikroElektronika and is available on Windows, Linux, and macOS. It includes C compilers, mikroSDK 2.0, package manager, and USB or WiFi Debugger capabilities with flexible licensing options. The development environment features intelligent code completion, auto-close brackets, and drag and drop visual elements.

Users can find their favorite Click Board library and working example through the **Package Manager**. Users will also be notified about new versions of installed packages, and easily update in one click.

*Source: [MikroElektronika blog post](https://docs.mikroe.com/mikrosdk/user-manual/general/overview/)*

MikroElektronika even provides first-time users with the longest time trial on the market - Get fully unlocked, feature-rich NECTO for **three months**, and explore it to the most delicate details before purchase!

*For more information about NECTO Studio, please visit the [product page](https://www.mikroe.com/necto).*

#### mikroSDK

mikroSDK 2.0 makes application code portable and reusable on many different platforms and architectures, with virtually no code changes. It is a collection of open-source software libraries with unified API and software development tools. Everything you need to start developing, and prototyping cross-platform embedded applications, including Click board™ applications and GUIs for embedded devices.

mikroSDK 2.0 is open-source, and it's natively supported in NECTO Studio. The video below, is a brief overview of how to use the [mikroSDK](https://www.mikroe.com/mikrosdk):

*Source: [MikroElektronika Youtube channel](https://www.youtube.com/channel/UCO1mWkLyFqBKqgC7orIVHlQ)*

Additional Resources:

- [Blog: mikroSDK - Learn what it is and how to use it](https://www.mikroe.com/blog/the-mikrosdk-the-solution-for-embedded-development)
- [Reference Manual](https://docs.mikroe.com/mikrosdk/ref-manual/index.html)
- [User Manual](https://docs.mikroe.com/mikrosdk/user-manual/)
  - [Porting Guide](http://docs.mikroe.com/mikrosdk/user-manual/porting-guides/porting-to-3rd-party/)
- [GitHub Repository](https://github.com/MikroElektronika/mikrosdk_v2)

### Required Materials

To get started, users will need a few of items listed below. *(You may already have a some of these items; read through the guide and modify your cart accordingly.)*

To program a [STM32 processor board](https://www.sparkfun.com/products/17713) *(recommended)* through [Necto Studio](https://www.mikroe.com/necto), users will need a JTAG programmer. Below are programmers that are compatible with the Necto Studio software.

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

#### Optional Hardware

Users may also need some [soldering equipment](https://www.sparkfun.com/categories/49) and a [JTAG header](https://www.sparkfun.com/categories/379) to connect the programmer to the board.

**Note:** Users should verify that the pinout for the programmer and adapter match up to the corresponding pins to avoid damaging their MCU.

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

### Suggested Reading

Like our [Qwiic connect system](https://www.sparkfun.com/qwiic), [mikroBUS™ socket](https://www.mikroe.com/mikrobus) is a standardized interface for the MIKROE [Click boards™](https://www.sparkfun.com/categories/tags/click). Click on the banner below for more information.

[![mikroBUS Logo](https://cdn.sparkfun.com/assets/learn_tutorials/2/0/0/3/mikroBUS_logo.png "Click to learn more about the mikroBUS ecosystem!")](https://www.mikroe.com/mikrobus)

\

For users who aren\'t familiar with the following concepts, we also recommend reading the following tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/arm-programming)

### ARM Programming 

How to program SAMD21 or SAMD51 boards (or other ARM processors).

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

[](https://learn.sparkfun.com/tutorials/designing-with-micromod)

### Designing with MicroMod 

This tutorial will walk you through the specs of the MicroMod processor and carrier board as well as the basics of incorporating the MicroMod form factor into your own PCB designs!

[](https://learn.sparkfun.com/tutorials/micromod-mikrobus-carrier-board-hookup-guide)

### MicroMod mikroBUS™ Carrier Board Hookup Guide 

This carrier board takes advantage of the MicroMod, Qwiic, and the mikroBUS™ ecosystems and allows users to take advantage of the growing number of 7 MicroMod processor boards, 83 Qwiic (add-on) boards, and +1100 drop-in Click boards™, which equates to +51M different board combinations. Click to learn more.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft2253&name=Getting+Started+with+Necto+Studio "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft2253 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+Necto+Studio&url=http%3A%2F%2Fsfe.io%2Ft2253&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft2253&t=Getting+Started+with+Necto+Studio "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft2253&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F2%2F5%2F3%2Flogo.PNG&description=Getting+Started+with+Necto+Studio "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/all) [Next Page →\
[Software Installation]](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/software-installation)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/introduction) [Software Installation](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/software-installation) [Home Page Layout](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/home-page-layout) [User Account and Compiler License](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/user-account-and-compiler-license) [Setup - Hardware Configuration](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/setup---hardware-configuration) [Package Manager - Click Libraries](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/package-manager---click-libraries) [Projects - Start and Build](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/projects---start-and-build) [Programmer and Debugger Configuration](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/programmer-and-debugger-configuration) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/discuss) [Single Page](https://learn.sparkfun.com/tutorials/getting-started-with-necto-studio/all) [Print]

- **Tags**
- - [Development](https://learn.sparkfun.com/tutorials/tags/development)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)
  - [Start a Project](https://learn.sparkfun.com/tutorials/tags/start-a-project)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]