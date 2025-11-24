# Source: https://learn.adafruit.com/photocells/using-a-photocell.md

# Photocells

## Using a Photocell

## Analog Voltage Reading Method
The easiest way to measure a resistive sensor is to connect one end to Power and the other to a&nbsp; **pull-down** &nbsp;resistor to ground. Then the point between the fixed pulldown resistor and the variable photocell resistor is connected to the analog input of a microcontroller such as an Arduino (shown)  
  
  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/458/medium800/light_cdsanasch.gif?1447975677)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/459/medium800/light_cdspulldowndiag.gif?1447975687)

For this example I'm showing it with a 5V supply but note that you can use this with a 3.3v supply just as easily. In this configuration the analog voltage reading ranges from 0V (ground) to about 5V (or about the same as the power supply voltage).

The way this works is that as the resistance of the photocell decreases, the total resistance of the photocell and the pulldown resistor decreases from over 600KΩ to 10KΩ. That means that the current flowing through both resistors&nbsp;_increases_&nbsp;which in turn causes the voltage across the fixed 10KΩ resistor to increase. It's quite a trick!

| Ambient light like… | Ambient light (lux) | Photocell resistance (Ω) | LDR + R (Ω) | Current thru LDR +R | Voltage across R |
| --- | --- | --- | --- | --- | --- |
| Dim hallway | 0.1 lux | 600KΩ | 610 KΩ | 0.008 mA | 0.1 V |
| Moonlit night | 1 lux | 70 KΩ | 80 KΩ | 0.07 mA | 0.6 V |
| Dark room | 10 lux | 10 KΩ | 20 KΩ | 0.25 mA | 2.5 V |
| Dark overcast day / Bright room | 100 lux | 1.5 KΩ | 11.5 KΩ | 0.43 mA | 4.3 V |
| Overcast day | 1000 lux | 300 Ω | 10.03 KΩ | 0.5 mA | 5V |

_This table indicates the approximate analog voltage based on the sensor light/resistance w/a 5V supply and 10K__Ω pulldown resistor._

If you're planning to have the sensor in a bright area and use a 10KΩ pulldown, it will quickly _saturate_. That means that it will hit the 'ceiling' of 5V and not be able to differentiate between kinda bright and really bright. In that case, you should replace the 10KΩ pulldown with a 1KΩ pulldown. In that case, it will not be able to detect dark level differences as well but it will be able to detect bright light differences better. This is a tradeoff that you will have to decide upon!

You can also use the "Axel Benz" formula by first measuring the minimum and maximum resistance value with the multimeter and then finding the resistor value with: Pull-Down-Resistor = squareroot(Rmin \* Rmax), this will give you slightly better range calculations

| Ambient light like… | Ambient light (lux) | Photocell resistance (?) | LDR + R (?) | Current thru LDR+R | Voltage across R |
| --- | --- | --- | --- | --- | --- |
| Moonlit night | 1 lux | 70 KΩ | 71 KΩ | 0.07 mA | 0.1 V |
| Dark room | 10 lux | 10 KΩ | 11 KΩ | 0.45 mA | 0.5 V |
| Dark overcast day / Bright room | 100 lux | 1.5 KΩ | 2.5 KΩ | 2 mA | 2.0 V |
| Overcast day | 1000 lux | 300 Ω | 1.3 KΩ | 3.8 mA | 3.8 V |
| Full daylight | 10,000 lux | 100 Ω | 1.1 KΩ | 4.5 mA | 4.5 V |

_This table indicates the approximate analog voltage based on the sensor light/resistance w/a 5V supply and 1K pulldown resistor._

Note that our method does not provide linear voltage with respect to brightness! Also, each sensor will be different. As the light level increases, the analog voltage goes up even though the resistance goes down:

**Vo = Vcc ( R / (R + Photocell) )**

That is, the voltage is proportional to the&nbsp; **inverse** &nbsp;of the photocell resistance which is, in turn, inversely proportional to light levels.

- [Previous Page](https://learn.adafruit.com/photocells/connecting-a-photocell.md)
- [Next Page](https://learn.adafruit.com/photocells/arduino-code.md)

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
