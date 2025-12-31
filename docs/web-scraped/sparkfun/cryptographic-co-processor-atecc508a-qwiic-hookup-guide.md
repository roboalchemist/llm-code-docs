# Source: https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Cryptographic Co-Processor ATECC508A (Qwiic) Hookup Guide

# Cryptographic Co-Processor ATECC508A (Qwiic) Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1003&name=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1003 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1003&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1003&t=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1003&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F0%2F0%2F3%2Fcrypto_coprocessor_logo-03-2.png&description=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Pin It")

## Introduction

🔒 **Note:** Please follow through the hookup guide in its entirety before using this board. The chip cannot be re-configured after it is **[PERMANENTLY]** locked.

The [SparkFun Cryptographic Co-processor Breakout ATECC508A (Qwiic)](https://www.sparkfun.com/products/15573) takes all the great features of the Microchip ATECC508A Cryptographic Authentication Device and adds two [Qwiic](https://www.sparkfun.com/qwiic) ports for plug and play functionality. In this tutorial we will cover the fundamentals of cryptographic authentication and how to use the ATECC508A to add a very high level of security to your projects.

[![SparkFun Cryptographic Co-Processor Breakout - ATECC508A (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/1/6/9/15573-SparkFun_Cryptographic_Co-Processor_Breakout_-_ATECC508A__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-cryptographic-co-processor-breakout-atecc508a-qwiic.html)

### [SparkFun Cryptographic Co-Processor Breakout - ATECC508A (Qwiic)](https://www.sparkfun.com/sparkfun-cryptographic-co-processor-breakout-atecc508a-qwiic.html) 

[ DEV-15573 ]

The SparkFun ATECC508A Crypto Co-processor Breakout allows you to add strong authentication security to your IoT node, edge d...

[ [\$7.85] ]

The ATECC508A is capable of many cryptographic processes. This tutorial focuses on [Elliptic-curve cryptographic digital signatures](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (ECC) - using [asymetric private/public keys](https://en.wikipedia.org/wiki/Public-key_cryptography). If those last few words are new to you, please read on! We will spend some time explaining in a bit.

🔒 **Note:**This chip is **[NOT] capable of encrypting and decrypting data**. It can however, perform quite a few cryptographic *authentication* processes such as secure private key creation, secure key storage and digital signature creation and verification.

At a very high level, the purpose of using this chip is to (1) verify that the message received actually came from the true sender and (2) verify that the data received was not tampered with. This technology is used in hyper-critical devices such as rocket launches, medical devices, two factor authentication keys (2FA), ink cartridges, garage door openers and car key FOBs.

Probably it\'s most important feature: this device can securely store a private ECC key. In fact, this private key will never be accessible - not even to you, the owner. It is created internally on the chip during configuration, and it can *never* be read from the chip (even if your de-capped the chip). Although you will never *know* it, you can still command the co-processor to *use* the secret private key to create a unique signature on some data. With this functionality, it can be used to securely authenticate a message in any kind of communication system. For example, between systems such as a node in an IoT system. Follow along, and you\'ll be creating 64 byte signatures (yes, *bytes*) and verifying them securely in no time!

*Checkout these videos for more details on this tutorial.*

### Required Materials

To follow along with this tutorial, you will need the following materials that are included in the kit. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** To follow this tutorial, an [Artemis microcontroller board](https://www.sparkfun.com/categories/424) has to be used with this product due to the buffer size required for the I^2^C bus.

For more **[advanced users]**, other microcontrollers can be used, but the buffer size of Wire library and/or the syntax for the serial print statements will need to be modified. (*\*This is outside the scope of this tutorial.*)

[![SparkFun Cryptographic Development Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/6/4/2/18303-SparkFun_Cryptographic_Development_Kit-01.jpg)](https://www.sparkfun.com/sparkfun-cryptographic-development-kit.html)

### [SparkFun Cryptographic Development Kit](https://www.sparkfun.com/sparkfun-cryptographic-development-kit.html) 

[ KIT-18303 ]

With the SparkFun Cryptographic Development kit you will get everything you need to learn the fundamentals of cryptographic a...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend you read over these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/artemis-development-with-arduino)

### Artemis Development with Arduino 

Get our powerful Artemis based boards (Artemis Nano, BlackBoard Artemis, and BlackBoard Artemis ATP) blinking in less than 5 minutes using the SparkFun Artemis Arduino Core!

[](https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis)

### Hookup Guide for the SparkFun RedBoard Artemis 

Get started with the RedBoard Artemis - all the functionality of the SparkFun Artemis module wrapped in the familiar Uno R3 footprint

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1003&name=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1003 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1003&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1003&t=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1003&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F0%2F0%2F3%2Fcrypto_coprocessor_logo-03-2.png&description=Cryptographic+Co-Processor+ATECC508A+%28Qwiic%29+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/all) [Next Page →\
[Cryptographic Authentication]](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/cryptographic-authentication)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/introduction) [Cryptographic Authentication](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/cryptographic-authentication) [Hardware Overview](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/hardware-overview) [Hardware Hookup](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/hardware-hookup) [Software Setup](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/software-setup) [Arduino Library](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/arduino-library) [Example 1: Configuration](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-1-configuration) [Example 2: Sign](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-2-sign) [Example 3: Verify](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-3-verify) [Example 4: From Alice to Bob](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-4-from-alice-to-bob) [Example 5: Random](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-5-random) [Example 6: Challenge](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-6-challenge) [Troubleshooting](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/resources-and-going-further)

[Comments [11]](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Artemis](https://learn.sparkfun.com/tutorials/tags/artemis)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Security](https://learn.sparkfun.com/tutorials/tags/security)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]