# Source: https://learn.adafruit.com/force-sensitive-resistor-fsr.md

# Force Sensitive Resistor (FSR)

## Overview

FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. &nbsp;This is a photo of an FSR, specifically the Interlink 402 model. The 1/2" diameter round part is the sensitive bit.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/426/medium800/force___flex_FSR402_MED.jpg?1396762932)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/427/medium800/force___flex_402FSR_large.jpg?1396762936)

The FSR is made of 2 layers separated by a spacer. The more one presses, the more of those Active Element dots touch the semiconductor and that makes the resistance go down.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/428/medium800/force___flex_FSRimage.jpg?1396762943)

FSRs are basically a resistor that changes its resistive value (in ohms Ω) depending on how much it is pressed. These sensors are fairly low cost, and easy to use but they're rarely accurate. They also vary some from sensor to sensor perhaps 10%. So basically when you use FSRs you should only expect to get _ranges_ of response. While FSRs can detect weight, they're a bad choice for detecting exactly how many pounds of weight are on them.

However, for most touch-sensitive applications like "has this been squeezed or pushed and about how much" they're a good deal for the money!

## Some Basic Stats

## These stats are specifically for the Interlink 402, but nearly all FSRs will be similar. Checking the datasheet will always illuminate any differences

- **Size:** 1/2" (12.5mm) diameter active area by 0.02" thick (Interlink does have some that are as large as 1.5"x1.5")
- **Price** [$7.00 from the Adafruit shop](http://www.adafruit.com/products/166)
- **Resistance range:** Infinite/open circuit (no pressure), 100KΩ (light pressure) to 200Ω (max. pressure)
- **Force range** : 0 to 20 lb. (0 to 100 Newtons) applied evenly over the 0.125 sq in surface area
- **Power supply:** Any! Uses less than 1mA of current (depends on any pullup/down resistors used and supply voltage)
- **[Datasheet](http://learn.adafruit.com/system/assets/assets/000/010/126/original/fsrguide.pdf)** (note there are some mathematical inconsistancies in here)

  
  
  
## How to measure force/pressure with an FSR
As we've said, the FSR's resistance changes as more pressure is applied. When there is no pressure, the sensor looks like an infinite resistor (open circuit), as the pressure increases, the resistance goes down. This graph indicates approximately the resistance of the sensor at different force measurements. (Note that force is not measured in grams and what they really mean is Newtons \* 100!)  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/429/medium800/force___flex_resistanceforce.jpg?1396762946)

It is important to notice that the graph isn't really _linear_ (its a log/log graph) and that at especially low force measurements it quickly goes from infinite to 100KΩ.

- [Next Page](https://learn.adafruit.com/force-sensitive-resistor-fsr/testing-an-fsr.md)

## Featured Products

### Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force

[Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force](https://www.adafruit.com/product/166)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF01A-N-221-A01&nbsp;with 1/2 diameter sensing region.

We used to stock the Interlink model 402 FSR - the Alpha version is almost half the price...

In Stock
[Buy Now](https://www.adafruit.com/product/166)
[Related Guides to the Product](https://learn.adafruit.com/products/166/guides)
### Square Force-Sensitive Resistor (FSR)

[Square Force-Sensitive Resistor (FSR)](https://www.adafruit.com/product/1075)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF02A-N-221-A01 FSR with a 38mm square sensing region. Note that this sensor can't detect _where_ on the square you pressed (for that, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1075)
[Related Guides to the Product](https://learn.adafruit.com/products/1075/guides)
### Extra-long force-sensitive resistor (FSR)

[Extra-long force-sensitive resistor (FSR)](https://www.adafruit.com/product/1071)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is a Interlink model 408 FSR with a massive 1/4-inch x 24-inch sensing region. You can press anywhere along the strip and the pressure will be recognized. Note...

In Stock
[Buy Now](https://www.adafruit.com/product/1071)
[Related Guides to the Product](https://learn.adafruit.com/products/1071/guides)
### Terminal Block - 2-pin 3.5mm - pack of 5!

[Terminal Block - 2-pin 3.5mm - pack of 5!](https://www.adafruit.com/product/724)
Nothing makes a project harder to maintain than a lot of loose wiring. That's why we like to use terminal blocks whenever making PCB-to-Wire connections. These particular 3.5mm terminal blocks are our favorite: big enough for a range of wire gauges, easy to adjust with a screwdriver, and...

In Stock
[Buy Now](https://www.adafruit.com/product/724)
[Related Guides to the Product](https://learn.adafruit.com/products/724/guides)

## Related Guides

- [Adafruit VEML6070 UV Sensor Breakout](https://learn.adafruit.com/adafruit-veml6070-uv-light-sensor-breakout.md)
- [Adafruit NAU7802 24-Bit ADC - STEMMA QT / Qwiic](https://learn.adafruit.com/adafruit-nau7802-24-bit-adc-stemma-qt-qwiic.md)
- [Arcade Stick Conversion](https://learn.adafruit.com/arcade-stick-conversion.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Wireless ESP32-S2 Touch Screen Controller for Pure Data](https://learn.adafruit.com/wireless-esp32-s2-controller-for-pure-data.md)
- [NAU7802 Pet Food Scale](https://learn.adafruit.com/nau7802-pet-food-scale.md)
- [Clue Coffee Scale](https://learn.adafruit.com/clue-coffee-scale.md)
- [ReBoots Animated LED Boot Laces](https://learn.adafruit.com/re-boots-animated-dancing-boot-laces.md)
- [SensoGlove Teardown](https://learn.adafruit.com/sensoglove-teardown.md)
- [ICEdot Teardown](https://learn.adafruit.com/icedot-teardown.md)
- [Tilt Sensor](https://learn.adafruit.com/tilt-sensor.md)
- [Wireless LED Juggling Balls with ESP-NOW](https://learn.adafruit.com/wireless-juggling-balls-esp-now.md)
- [CuteCircuit Twirkle Shirt Teardown](https://learn.adafruit.com/cutecircuit-twirkle-shirt-teardown.md)
- [Power Glove Wireless MIDI Controller](https://learn.adafruit.com/power-glove-bluetooth-midi-controller.md)
- [Flora MIDI Drum Glove](https://learn.adafruit.com/midi-drum-glove.md)
