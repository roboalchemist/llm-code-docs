# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/3-3v-conversion.md

# Arduino Tips, Tricks, and Techniques

## 3.3V Conversion

## Introduction

Arduino UNO's and many other Arduino boards run on 5 volts, which for a long time was the 'standard' voltage for hobbyist electronics and microcontrollers. But now the coolest new sensors, displays and chips are 3.3V and are not 5V compatible. For example, XBee radios, and SD cards and acellerometers all run on 3.3V logic and power. If you tried to connect to them with 5V you could damage the internals of the accessory.  
  
We use chips like the [CD4050 to do level conversion](http://www.adafruit.com/partfinder/ic?s%5B%5D=cd4050#logic) but if you are using a lot of 3.3V devices, maybe you're just better off upgrading the entire Arduino to run from 3.3V!  
  
To do that, we will replace the regulator so that the DC barrel jack goes to a 3.3v type regulator, not a 5V. And then reconfigure the 5V usb power line so it goes through the regulator as well.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/531/medium800/learn_arduino_pre.jpg?1396798085)

## Replace the Regulator
The default regulator is a 5.0V type, but we want 3.3V out, so we'll need to replace it. We'll use a 1117-3.3V (there are a few manufacturers of 1117 regulators, just like the 7805 is made by many factories) regulator in a TO-252-3 package. It looks like this:  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/532/medium800/learn_arduino_33vreg.jpg?1396798090)

You can get these from any electronics component shop, [for example here is the digikey link](http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=NCP1117DT33GOS-ND).  
  
To start, we'll need to remove the old regulator. The easiest way to do that is to first clip the two legs.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/533/medium800/learn_arduino_vregclip.jpg?1396798096)

Then you'll need to heat the tab up to get it liquid so you can lift off the old part. Although it may seem counter intuitive, its best to **add** some solder to the tab, melt it on with your iron, this will improve the heat conduction since the tab is so large.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/534/medium800/learn_arduino_vregremoving.jpg?1396798103)

Clean up the tabs and remove any clipped parts still stuck on.![](https://cdn-learn.adafruit.com/assets/assets/000/003/535/medium800/learn_arduino_vregremoved.jpg?1396798109)

Now line up the new 3.3V regulator, and solder the tab first, use plenty of solder and be patient, the tab acts like a heat sink.![](https://cdn-learn.adafruit.com/assets/assets/000/003/536/medium800/learn_arduino_vregtab.jpg?1396798119)

Then do the two legs.![](https://cdn-learn.adafruit.com/assets/assets/000/003/537/medium800/learn_arduino_vregleg.jpg?1396798130)

## Replacing the Fuse
The next part is a little tricky, the USB jack gives us exactly 5V already, and normally that is tied to the output of the voltage regulator (essentially, its got a little circuitry that connects it when the DC jack is not powered).  
  
The easiest way to make the USB 5V also go through the regulator is to remove the fuse and solder a diode from the USB output to the regulator input.  
  
[You can use any power diode, a 1N4001 is perfect](http://www.adafruit.com/partfinder/diodes#power_blocking "Link: http://www.adafruit.com/partfinder/diodes#power\_blocking") and only a few pennies.  
  
The trade off is now there is no 500 mA fuse for the USB jack. The good news is that computers will have their own fuses on the USB connector (inside the computer) so its not likely you will destroy your PC. But be aware that you're losing a little safety.  
  
Heat the fuse with your soldering iron, again adding solder may help thermal conductivity. Since the fuse is very conductive you can probably just heat one side for a while and both ends will melt.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/538/medium800/learn_arduino_fuseremove.jpg?1396798138)

Clip the diode short and bend the leads over. Solder the side without a stripe (anode) to the old fuse pad, nearest the board edge. Solder the striped end (cathode) to the right hand leg of the regulator.  
  
The Arduino will still automatically select whichever power plug is giving you more power.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/539/medium800/learn_arduino_diode.jpg?1396798147)

That's it! You are now 3.3V powered. This is a little lower than the power/frequency specification for the AVR chips since they ought to have about 3.6V to run 16Mhz but its&nbsp;_probably_&nbsp;not going to be an issue since AVRs can be overclocked a little.- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/upgrade.md)
- [Next Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-hacks.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Arduino bootloader-programmed chip (Atmega328P)

[Arduino bootloader-programmed chip (Atmega328P)](https://www.adafruit.com/product/123)
This is a preprogrammed Atmega328P chip, useful if you want to make your own Arduino-compatible or repair a damaged chip on an exisiting Arduino UNO, Duemilanove, Diecimila, or NG!  
  
This chip is programmed with 'ADAboot', my version of the bootloader that is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/123)
[Related Guides to the Product](https://learn.adafruit.com/products/123/guides)

## Related Guides

- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
