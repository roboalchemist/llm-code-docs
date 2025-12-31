# Source: https://learn.adafruit.com/photocells/measuring-light.md

# Photocells

## Measuring Light

As we've said, a photocell's resistance changes as the face is exposed to more light. When its dark, the sensor looks like an large resistor up to 10MΩ, as the light level increases, the resistance goes down. This graph indicates approximately the resistance of the sensor at different light levels. Remember each photocell will be a little different so use this as a guide only!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/452/medium800/light_graph.gif?1447975659)

Note that the graph is not linear, its a log-log graph!

Photocells, particularly the common CdS cells that you're likely to find, are not sensitive to all light. In particular they tend to be sensitive to light between 700nm (red) and 500nm (green) light.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/453/medium800/light_cdsspectrum.gif?1447975668)

Basically, blue light wont be nearly as effective at triggering the sensor as green/yellow light!## What the Heck is Lux?
Most datasheets use&nbsp;[lux](http://en.wikipedia.org/wiki/Lux)&nbsp;to indicate the resistance at certain light levels. But what is&nbsp;[lux](http://en.wikipedia.org/wiki/Lux)&nbsp;? Its not a method we tend to use to describe brightness so its tough to gauge. Here is a table&nbsp;[adapted from a Wikipedia article on the topic!](http://en.wikipedia.org/wiki/Lux)| Illuminance | Example |
| --- | --- |
| **0.002 lux** | Moonless clear night sky |
| **0.2 lux** | Design minimum for emergency lighting (AS2293). |
| **0.27 - 1 lux** | Full moon on a clear night |
| **3.4 lux** | Dark limit of civil twilight under a clear sky |
| **50 lux** | Family living room |
| **80 lux** | Hallway/toilet |
| **100 lux** | Very dark overcast day |
| **300 - 500 lux** | Sunrise or sunset on a clear day. Well-lit office area. |
| **1,000 lux** | Overcast day; typical TV studio lighting |
| **10,000 - 25,000 lux** | Full daylight (not direct sun) |
| **32,000 - 130,000 lux** | Direct sunlight |

- [Previous Page](https://learn.adafruit.com/photocells/overview.md)
- [Next Page](https://learn.adafruit.com/photocells/testing-a-photocell.md)

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
