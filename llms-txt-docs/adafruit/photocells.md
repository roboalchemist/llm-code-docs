# Source: https://learn.adafruit.com/photocells.md

# Photocells

## Overview

Photocells are sensors that allow you to detect light. They are small, inexpensive, low-power, easy to use and don't wear out. For that reason they often appear in toys, gadgets and appliances. They are often referred to as CdS cells (they are made of Cadmium-Sulfide), light-dependent resistors (LDR), and photoresistors.

![](https://cdn-learn.adafruit.com/assets/assets/000/035/439/medium800/light_photocell.jpg?1473012308)

Photocells are basically a resistor that changes its resistive value (in ohms Ω) depending on how much light is shining onto the squiggly face. They are very low cost, easy to get in many sizes and specifications, but are very innacurate. Each photocell sensor will act a little differently than the other, even if they are from the same batch. The variations can be really large, 50% or higher! For this reason, they shouldn't be used to try to determine precise light levels in lux or millicandela. Instead, you can expect to only be able to determine basic light changes.

![](https://cdn-learn.adafruit.com/assets/assets/000/035/438/medium800/light_Photoresistors_-_three_sizes_-_mm_scale.jpg?1473012227)

For most light-sentsitive applications like "is it light or dark out", "is there something in front of the sensor (that would block light)", "is there something interrupting a laser beam" (break-beam sensors), or "which of multiple sensors has the most light hitting it", photocells can be a good choice!![](https://cdn-learn.adafruit.com/assets/assets/000/035/644/medium800/light_photocell-diagram.png?1473477670)

## Some Basic Stats
These stats are for the photocell in the Adafruit shop which is very much like the [PDV-P8001](http://learn.adafruit.com/system/assets/assets/000/010/127/original/PDV-P8001.pdf "Link: http://learn.adafruit.com/system/assets/assets/000/010/127/original/PDV-P8001.pdf") . Nearly all photocells will have slightly different specifications, although they all pretty much work the same. If there's a datasheet, you'll want to refer to it
- **Size:** Round, 5mm (0.2") diameter. (Other photocells can get up to 12mm/0.4" diameter!)
- **Price:** [$1.00 at the Adafruit shop](http://www.adafruit.com/index.php?main_page=product_info&cPath=35&products_id=161 "Link: http://www.adafruit.com/index.php?main\_page=product\_info&cPath=35&products\_id=161")
- **Resistance range:** 200KΩ (dark) to 10KΩ (10 lux brightness)
- **Sensitivity range:** CdS cells respond to light between 400nm (violet) and 600nm (orange) wavelengths, peaking at about 520nm (green).
- **Power supply:** pretty much anything up to 100V, uses less than 1mA of current on average (depends on power supply voltage)
- **[Datasheet](http://learn.adafruit.com/system/assets/assets/000/010/127/original/PDV-P8001.pdf)** and another **[Datasheet](http://learn.adafruit.com/system/assets/assets/000/010/128/original/DTS_A9950_A7060_B9060.pdf)**
- Two **[application notes on using](http://learn.adafruit.com/system/assets/assets/000/010/129/original/APP_PhotocellIntroduction.pdf)** and **[selecting photocells](http://learn.adafruit.com/system/assets/assets/000/010/130/original/gde_photocellselecting.pdf)** where nearly all of these graphs are taken from

## Problems you may encounter with multiple sensors

If, when adding more sensors, you find that the readings are inconsistent, this indicates that the sensors are interfering with each other when switching the analog reading circuit from one pin to the other. You can fix this by doing two delayed readings and tossing out the first one.

[See this post for more information](http://www.adafruit.com/blog/2010/01/29/how-to-multiplex-analog-readings-what-can-go-wrong-with-high-impedance-sensors-and-how-to-fix-it/ "Link: http://www.adafruit.com/blog/2010/01/29/how-to-multiplex-analog-readings-what-can-go-wrong-with-high-impedance-sensors-and-how-to-fix-it/")

- [Next Page](https://learn.adafruit.com/photocells/measuring-light.md)

## Featured Products

### Photo cell (CdS photoresistor)

[Photo cell (CdS photoresistor)](https://www.adafruit.com/product/161)
CdS cells are little light sensors. As the squiggly face is exposed to more light, the resistance goes down. When it's light, the resistance is about ~1KΩ, when dark it goes up to ~10KΩ.

To use, connect one side of the photocell (either one, it's symmetric) to power...

In Stock
[Buy Now](https://www.adafruit.com/product/161)
[Related Guides to the Product](https://learn.adafruit.com/products/161/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Digital Multimeter

[Digital Multimeter](https://www.adafruit.com/product/71)
This is a basic multimeter, I've played with it a bunch and I think its a great addition to a toolbox. It's low cost and simple to use with a big clear display and all the measurements you need:

- AC/DC Voltage measurement
- Current measurement, from 1uA up to...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/71)
[Related Guides to the Product](https://learn.adafruit.com/products/71/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Mini Thermal Receipt Printers](https://learn.adafruit.com/mini-thermal-receipt-printer.md)
- [Create an Internet of Things Dashboard with Adafruit IO](https://learn.adafruit.com/create-an-internet-of-things-dashboard-with-adafruit-dot-io.md)
- [Multi-tasking the Arduino - Part 2](https://learn.adafruit.com/multi-tasking-the-arduino-part-2.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [1.8" TFT Display Breakout and Shield](https://learn.adafruit.com/1-8-tft-display.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Adafruit VS1053 MP3/AAC/Ogg/MIDI/WAV Codec Breakout Tutorial](https://learn.adafruit.com/adafruit-vs1053-mp3-aac-ogg-midi-wav-play-and-record-codec-tutorial.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [Collin's Lab: MIDI](https://learn.adafruit.com/collins-lab-midi.md)
- [2.8" TFT Touchscreen](https://learn.adafruit.com/2-8-tft-touchscreen.md)
- [Current Limiting Stepper Driver with DRV8871](https://learn.adafruit.com/current-limiting-stepper-driver-with-drv8871.md)
