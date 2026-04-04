# Source: https://learn.adafruit.com/usb-next-keyboard-with-arduino-micro/research.md

# USB NeXT Keyboard with an Arduino Micro

## Research

The first thing to note is that the USB part (acting like a USB keyboard) is the easiest part of the project - there's already plenty of example code for how to do that with an Arduino Leonardo or Micro. The really tough part is figuring out how to read from the keyboard as it's not in any known or well documented protocol. The good news is whenever you're working with a really old technology, the computers back then were really slow and things weren't too complicated. Chances are whatever they did, it was meant to be simple and lightweight. Contrast this with a USB or Bluetooth or WiFi stack!  
  
Our first stop is over at the awesome [http://www.kbdbabel.org/conn/index.html](http://www.kbdbabel.org/conn/index.html "Link: http://www.kbdbabel.org/conn/index.html") ([http://archive.is/yqzKJ)](http://archive.is/yqzKJ)) where the nice author has documented the pinout of the keyboard. This is great because we won't accidentally smash the electronics with the wrong voltage. Also, it gives us a hint of how to talk to it. Power and ground at 5V are nice, easy to work with voltages. There's an RX and TX pin so at least we don't have to deal with a bi-directional or differential signal (whew).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/900/medium800/microcontrollers_kbd_connector_next.png?1396788473)

Ok so now we can power it up. I applied +5V to VCC and ground to GND. I did see 5V on the "from KDB" pin, but unfortunately no actual data when keys were pressed. This means that the keyboard isnt 'dumb' - it expects some sort of clock or reset signal on the "to KBD" pin. While one could try to figure it out cold, its a lot of effort.  
  
Ideally, we'd have a NeXT that we could plug the keyboard into and 'sniff' the traffic, that is the easiest way to do it. Unfortunately, we don't have one. We were in crisis!&nbsp; But then we kept searching and looking around (btw, searching for "next keyboard" is not a very efficient way to locate this brand of keyboard!) and we lucked out when we found a Japanese website of serious keyboard enthusiast [http://m0115.web.fc2.com/](http://m0115.web.fc2.com/ "Link: http://m0115.web.fc2.com/") It is using frames so we weren't too optimistic we'd find a GitHub repo, but after a lot of clicking we found the holy grail of NeXT timing information:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/901/medium800/microcontrollers_next.jpg?1396788484)

Yes! This is exactly what we need, not only does he include the timing diagram, but also the timeline for resetting and querying. 50 microsecond timing is well within the abilities of a 16 MHz microcontroller. Now we're ready to write code. (see the next section for the code listing)  
  
The only thing remaining was the scancode table. By this point I, was 5 hours into this project and getting a little tired, when I realized that any operating system written for NeXT would have this all written up for me. In fact, there was an NetBSD port to NeXT and all the keyboard mapping data was there for me! Link to: [NetBSD driver source](http://web.archive.org/web/20221212183955/http://cvsweb.netbsd.org/bsdweb.cgi/src/sys/arch/next68k/dev/nextkbd.c?rev=1.13&content-type=text/x-cvsweb-markup&only_with_tag=netbsd-6-base),&nbsp;[scancode table](http://web.archive.org/web/20221212184207/http://cvsweb.netbsd.org/bsdweb.cgi/src/sys/arch/next68k/dev/wskbdmap_next.c?rev=1.5&content-type=text/x-cvsweb-markup&only_with_tag=netbsd-6-base) via wayback machine.

- [Previous Page](https://learn.adafruit.com/usb-next-keyboard-with-arduino-micro/parts.md)
- [Next Page](https://learn.adafruit.com/usb-next-keyboard-with-arduino-micro/wiring-case.md)

## Featured Products

### Arduino Micro without Headers - 5V 16MHz ATmega32u4 - Assembled

[Arduino Micro without Headers - 5V 16MHz ATmega32u4 - Assembled](https://www.adafruit.com/product/1315)
Squee! It's the cutest, tiniest little Arduino yet! The Arduino Micro packs all of the power of the Arduino Leonardo in a 1.9" x 0.7" (48mm x 18mm) size. Although it may look like a stick of gum, its actually a USB-native 8-bit microcontroller, with 32K of flash, and 2.5K of RAM....

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1315)
[Related Guides to the Product](https://learn.adafruit.com/products/1315/guides)
### Arduino Micro with Headers - 5V 16MHz - (ATmega32u4 - assembled)

[Arduino Micro with Headers - 5V 16MHz - (ATmega32u4 - assembled)](https://www.adafruit.com/product/1086)
_Squee_! It's the cutest, tiniest little Arduino yet! The Arduino Micro packs all of the power of the Arduino Leonardo in a 1.9" x 0.7" (48mm x 18mm) size. Although it may look like a stick of gum, its actually a USB-native 8-bit microcontroller, with 32K of flash, and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1086)
[Related Guides to the Product](https://learn.adafruit.com/products/1086/guides)
### Altoids Gum sized tin

[Altoids Gum sized tin](https://www.adafruit.com/product/16)
Ever since Altoids discontinued the Gum version, its been hard to get tins. So we went and got a whole mess of them custom made! These tins are exactly the same shape and size as the old Altoids gum tins but they are blank and we got the bottom flattened instead of rounded (so it fits things...

In Stock
[Buy Now](https://www.adafruit.com/product/16)
[Related Guides to the Product](https://learn.adafruit.com/products/16/guides)
### USB cable - USB A to Micro-B

[USB cable - USB A to Micro-B](https://www.adafruit.com/product/592)
This here is your standard A to micro-B USB cable, for USB 1.1 or 2.0. Perfect for connecting a PC to your Metro, Feather, Raspberry Pi or other dev-board or microcontroller

Approximately 3 feet / 1 meter long

In Stock
[Buy Now](https://www.adafruit.com/product/592)
[Related Guides to the Product](https://learn.adafruit.com/products/592/guides)

## Related Guides

- [Adafruit PCA9546 4-Channel I2C Multiplexer](https://learn.adafruit.com/adafruit-pca9546-4-channel-i2c-multiplexer.md)
- [Blinking an LED with the Zephyr RTOS](https://learn.adafruit.com/blinking-led-with-zephyr-rtos.md)
- [Qualia S3 Fireplace](https://learn.adafruit.com/qualia-s3-fireplace.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Adafruit 4-Channel ADC Breakouts](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [ESPHole Ad Blocker](https://learn.adafruit.com/esphole-ad-blocker.md)
- [Adafruit QT Py and NeoPixel LEDs](https://learn.adafruit.com/qt-py-and-neopixel-leds.md)
- [The Pixif](https://learn.adafruit.com/the-pixif.md)
- [Quickstart IoT - Raspberry Pi Pico RP2040 with WiFi ](https://learn.adafruit.com/quickstart-rp2040-pico-with-wifi-and-circuitpython.md)
- [Atmega32u4 Breakout](https://learn.adafruit.com/atmega32u4-breakout.md)
- [Introducing Adafruit ItsyBitsy M4](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4.md)
- [Adafruit Metro M7 with microSD](https://learn.adafruit.com/adafruit-metro-m7-microsd.md)
- [Adafruit Infrared IR Remote Receiver](https://learn.adafruit.com/adafruit-infrared-ir-remote-receiver.md)
- [Adafruit Feather M4 CAN Express](https://learn.adafruit.com/adafruit-feather-m4-can-express.md)
