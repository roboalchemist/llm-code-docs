# Source: https://learn.sparkfun.com/tutorials/photon-development-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Photon Development Guide

# Photon Development Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft400&name=Photon+Development+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft400 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Photon+Development+Guide&url=http%3A%2F%2Fsfe.io%2Ft400&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft400&t=Photon+Development+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft400&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F0%2F0%2Fdev-blink-ino.png&description=Photon+Development+Guide "Pin It")

## Introduction

Particle\'s [Photon Development Board](https://www.sparkfun.com/products/13345) is an awesomely powerful platform for projects that require WiFi and Internet-connectivity. Whether you\'re creating the next, great, IoT project, or just want an easy to use, over-the-air-programmable ARM Cortext M3 development board, the Photon is an excellent foundation.

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

As with any microcontroller platform, there is no shortage of routes you can take to develop firmware for the Photon. There is a web-based IDE, which make it easy to share and import import code and program your Photon remotely. There\'s a pre-configured local IDE, which shares many of the online IDE\'s advantages, but allows you to keep code stored on your hard drive. Or there are the more \"hardcore\" ARM development environments, which, while more complicated, can provide complete control over the contents of your Photon\'s program memory.

### Covered In This Tutorial

The purpose of this tutorial is provide a quick overview of the options you have when your developing firmware for the Photon. The online Build IDE is easy, but it\'s not for everyone \-- that shouldn\'t stop anyone from getting a chance to use this powerful, cost-effective WiFi development platform.

This tutorial is split into a few sections. Navigate using the menu on the right, or click below to skip straight to the section you\'re most interested in:

- [Particle Build](https://learn.sparkfun.com/tutorials/photon-development-guide#particle-build-online) \-- A beginner friendly, browser-based, online IDE hosted on [Particle.io](https://build.particle.io).
- [Particle Dev](https://learn.sparkfun.com/tutorials/photon-development-guide#particle-dev-half-online-half-offline) \-- An offline editor that allows you to locally store your source code, but still requires Internet connectivity for compiling and flashing code to your Photon.
- [ARM GCC and DFU Bootloading](https://learn.sparkfun.com/tutorials/photon-development-guide#arm-gcc-and-the-dfu-bootloader-offline) \-- The heart of the Photon is an STM32 ARM microcontroller, so if you already have an ARM IDE set up, the Photon\'s open-source firmware will make it easy to port to the Photon. Plus, because the Photon has a built-in USB bootloader, loading the code can take place entirely offline too!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft400&name=Photon+Development+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft400 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Photon+Development+Guide&url=http%3A%2F%2Fsfe.io%2Ft400&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft400&t=Photon+Development+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft400&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F0%2F0%2Fdev-blink-ino.png&description=Photon+Development+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/photon-development-guide/all) [Next Page →\
[Particle Build (Online)]](https://learn.sparkfun.com/tutorials/photon-development-guide/particle-build-online)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/photon-development-guide/introduction) [Particle Build (Online)](https://learn.sparkfun.com/tutorials/photon-development-guide/particle-build-online) [Particle Dev (Half-Online, Half Offline)](https://learn.sparkfun.com/tutorials/photon-development-guide/particle-dev-half-online-half-offline) [ARM GCC and the DFU Bootloader (Offline)](https://learn.sparkfun.com/tutorials/photon-development-guide/arm-gcc-and-the-dfu-bootloader-offline) [Resources and Going Further](https://learn.sparkfun.com/tutorials/photon-development-guide/resources--going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/photon-development-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/photon-development-guide/all) [Print]

- **Tags**
- - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Photon](https://learn.sparkfun.com/tutorials/tags/photon)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]