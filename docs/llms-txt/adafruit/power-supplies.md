# Source: https://learn.adafruit.com/power-supplies.md

# Power Supplies

## Overview

## What is a power supply?
A power supply is a device that&nbsp; **supplies power to another device, at a specific voltage level, voltage type and current level**. For example, when we talk about a&nbsp; **9VDC @ 500mA** &nbsp;power supply can provide **as much as 500mA of current** &nbsp;and the voltage will be at least&nbsp; **9V DC** &nbsp;up to that maximum current level. While it sounds simple, power supplies have a lot of little hang-ups that can be very tricky for the uninitiated. For example, unregulated supplies say they can provide 9V but really may be outputting 15V! The very common 7805 regulator datasheet claims it can regulate up to 1000 mA of current, but when you put a 15V supply on one side, it overheats and shuts down! This tutorial will try to help explain all about power supplies.  
## Why a power supply?
When you start out with electronics, you'll hear a lot about&nbsp; **power supplies** &nbsp;- they're in every electronics project and they are the backbone of everything! A good power supply will make your project hum along nicely. A bad power supply will make life frustrating: stuff will work sometimes but not others, inconsistent results, motors not working, sensor data always off. Understanding power supplies (boring though they may be) is&nbsp; **key** &nbsp;to making your project work!

A lot of people don't pay much attention to power supplies until problems show up. We think you should always think about your power supply from day one - How are you going to power it? How long will the batteries last? Will it overheat? Can it get damaged by accidentally plugging in the wrong thing?

## Power supplies are all around you!
Unless you live in a shack in the woods, you probably have a dozen power supplies in your home or office.

Here is the power supply that is used in many apple products:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/084/medium800/components_m8943.jpg?1396768532)

Here is a classic 'wall wart' that comes with many consumer electronics:![](https://cdn-learn.adafruit.com/assets/assets/000/001/085/medium800/components_wart_t.jpg?1396768540)

This is a massive power supply that's in a PC, usually you dont see this unless you open up the PC and look inside for the big metal box:![](https://cdn-learn.adafruit.com/assets/assets/000/001/086/medium800/components_1ee9150d7ba821f662b2ad43cb51464e.media.500x375.jpg?1396768543)

All these power supplies have one thing in common - they take high voltage 120V or 220V AC power and&nbsp; **regulate** &nbsp;or&nbsp; **convert** &nbsp;it down to say 12V or 5V DC. This is important because the electronics inside of a computer, or cell phone, or video game console dont run at 120V and they don't run on AC power!

So, to generalize, here is what the power supplies for electronics do:

1. They convert AC (alternating current) power to DC (direct current)
2. They regulate the high voltage (120-220V) down to around 5V (the common voltages range from 3.3V to 15V)
3. They may have fuses or other overcurrent/overheat protection

**Hey, so if electronics can't run on AC, why doesn't wall power come in DC?**

You may be wondering - "I have 20 wall adapters, this seems silly! Why not just have DC power come out of the wall at 5V?" Essentially, because modern electronics are very recent. for many many decades wall power was used to power light bulbs, big motors (like fridges, vacuum cleaners, washing machines, air conditioners), and heaters. All of these use AC power more efficiently than DC power. Also, different electronics need different voltages. So far its worked out better to have a custom power supply for each device although it is a little irritating sometimes!

## AC/DC
![](https://cdn-learn.adafruit.com/assets/assets/000/001/087/medium800/components_aa0f9a37253f97e9d7c886c2ca78e77e.media.350x195.png?1396768570)

## So the power coming out of your wall is high voltage AC but microcontrollers and servos and sensors all want low voltage DC. How shall we make it work? Converting between AC power and DC power requires different techniques depending on what the input and output is. We'll refer to this table:  

| Power type in | Power type out | Technique | Pros | Cons | Commonly seen… |
| --- | --- | --- | --- | --- | --- |
| High Voltage AC (eg. 120V-220VAC) | Low voltage AC (eg. 12VAC) | Transformer | Really cheap, electrically isolated | Really big & heavy! | Small motors, in cheaper power supplies before the regulator |
| Low Voltage AC (eg. 20VAC) | High voltage AC (eg ~120VAC) | Transformer | Same as above, but the transformer is flipped around | Really big & heavy! | Some kinds of inverters, EL wire or flash bulb drivers |
| High Voltage AC (eg. 120V-220VAC) | High voltage DC (eg. 170VDC) | Half or full wave rectifier | Very inexpensive (just a diode or two) | Not isolated | We've seen these in tube amps |
| Low Voltage AC (eg. 20VAC) | Low voltage DC (eg 5VDC) | Half or full wave rectifier | Very inexpensive (just a diode or two) | Not isolated | Practically all consumer electronics that have transformer-based supplies |
| High Voltage AC (eg. 120V-220VAC) | Low voltage DC (eg 5VDC) | Transformer & rectifier&nbsp;  
Combination of High→Low AC & Low AC→Low DC | Fairly inexpensive | Kinda heavy, output is not precise, efficiency is so-so | Every chunky wall-wart contains this |
| High Voltage AC (eg. 120V-220VAC) | Low voltage DC (eg 5VDC) | Switching supply | Light-weight, output is often precise | Expensive! | Every slimmer wall-wart contains this |

Basically, to convert from AC to AC we tend to use a transformer. To convert from AC to DC we use a transformer + diodes (rectifier) or a switching supply. The former is inexpensive (but not very precise) and the later is expensive (but precise). Guess which one you're more likely to find in a cheaply-made device? :)

We left a few types out of this table because they're a little more esoteric or complex, such as the AC voltage doubler. These are still used but you're a little less likely to see them and they don't get used in power supplies you're likely to encounter.

- [Next Page](https://learn.adafruit.com/power-supplies/transformer-based-ac-dc-converters.md)

## Featured Products

### 12V 5A switching power supply

[12V 5A switching power supply](https://www.adafruit.com/product/352)
This is a beefy switching supply, for when you need a lot of power! It can supply 12V DC up to 5 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard 'figure-8'...

Out of Stock
[Buy Now](https://www.adafruit.com/product/352)
[Related Guides to the Product](https://learn.adafruit.com/products/352/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)
### 5V 1A (1000mA) USB port power supply - UL Listed

[5V 1A (1000mA) USB port power supply - UL Listed](https://www.adafruit.com/product/501)
Need a USB jack for charging or powering a project, but don't want to lug around a computer? This switching supply gives a clean regulated output at up to 1000mA! 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but...

In Stock
[Buy Now](https://www.adafruit.com/product/501)
[Related Guides to the Product](https://learn.adafruit.com/products/501/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 9 VDC 1000mA regulated switching power adapter - UL listed

[9 VDC 1000mA regulated switching power adapter - UL listed](https://www.adafruit.com/product/63)
This is a really nice power supply. It's a switching DC supply so it's small and light and efficient. It is thin so it fits in power strips without blocking other outlets. The output is regulated so you'll get a steady 9V up to 1000mA (1 Amp) of current draw. 5.5mm/2.1mm barrel...

Out of Stock
[Buy Now](https://www.adafruit.com/product/63)
[Related Guides to the Product](https://learn.adafruit.com/products/63/guides)

## Related Guides

- [Adafruit 16 Channel Servo Driver with Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi.md)
- [Adafruit PCA9548 8-Channel STEMMA QT / Qwiic I2C Multiplexer](https://learn.adafruit.com/adafruit-pca9548-8-channel-stemma-qt-qwiic-i2c-multiplexer.md)
- [Adafruit Motor Selection Guide](https://learn.adafruit.com/adafruit-motor-selection-guide.md)
- [Boomy Pi Airplay Boombox](https://learn.adafruit.com/boomy-pi-airplay.md)
- [Digital Circuits 3: Combinational Circuits](https://learn.adafruit.com/combinational-logic.md)
- [Digital Circuits 6: An EPROM Emulator](https://learn.adafruit.com/digital-circuits-6-eprom-emulator.md)
- [Adafruit TPS65131 Split Power Supply Boost Converter](https://learn.adafruit.com/adafruit-tps65131-split-power-supply-boost-converter.md)
- [Digital Circuits 4: Sequential Circuits](https://learn.adafruit.com/digital-circuits-4-sequential-circuits.md)
- [Piezo Ring Tones with Raspberry Pi](https://learn.adafruit.com/piezo-ring-tones-with-raspberry-pi.md)
- [All About Stepper Motors](https://learn.adafruit.com/all-about-stepper-motors.md)
- [Motion-Activated Solder Fume Extractor With Lamp](https://learn.adafruit.com/motion-activated-solder-fume-extractor-with-lamp.md)
- [Adafruit bq25185 USB / DC / Solar Charger with 5V Boost Board](https://learn.adafruit.com/adafruit-bq25185-usb-dc-solar-charger-with-5v-boost-board.md)
- [Secret Knock Activated Drawer Lock](https://learn.adafruit.com/secret-knock-activated-drawer-lock.md)
- [All About Batteries](https://learn.adafruit.com/all-about-batteries.md)
- [Adafruit SPI FRAM Breakouts](https://learn.adafruit.com/adafruit-spi-fram-breakout.md)
