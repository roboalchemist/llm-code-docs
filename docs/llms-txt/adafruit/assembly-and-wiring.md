# Source: https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/assembly-and-wiring.md

# Source: https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/assembly-and-wiring.md

# Adafruit 4-Channel ADC Breakouts

## Assembly and Wiring

# Assembly:
The board comes with all surface-mount parts pre-soldered. &nbsp;For breadboard use, the included header-strip should be soldered on:## Prepare the header strip
Cut the supplied header strip to length and insert it long-pins-down in your breadboard to hold it for soldering.![sensors_2012_11_10_IMG_0757-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/576/medium640/sensors_2012_11_10_IMG_0757-1024.jpg?1396784735)

## Position the breakout&nbsp;board
Place the breakout board on the header pins.![sensors_2012_11_10_IMG_0759-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/577/medium640/sensors_2012_11_10_IMG_0759-1024.jpg?1396784744)

## Solder!
Solder each pin for a good electrical connection.  
![sensors_2012_11_10_IMG_0761-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/578/medium640/sensors_2012_11_10_IMG_0761-1024.jpg?1396784751)

# Wiring:

## Power
First connect VDD and GND. &nbsp;These boards will work with either a 3.3v or a 5v supply. &nbsp;The diagram below shows connection to the Arduino 5v pin.  
Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/673/medium800/sensors_ADC_Power_bb-1024.jpg?1396785683)

## I2C Connections
I2C requires just 2 pins to communicate. &nbsp;These can be shared with other I2C devices. &nbsp;For R3 and later Arduinos (including MEGA and DUE models), connect SDA-\>SDA and SCL-\>SCL.![](https://cdn-learn.adafruit.com/assets/assets/000/002/674/medium800/sensors_ADC_i2c_bb-1024.jpg?1396785691)

## I2C "Classic"
For older Arduino boards without dedicated SDA and SCL pins, connect as shown below. &nbsp;(For older Arduino Megas, SDA and SCL are on pins 20 and 21)![](https://cdn-learn.adafruit.com/assets/assets/000/002/675/medium800/sensors_ADC_Classic_i2c_bb-1024.jpg?1396785699)

## I2C Addressing

The ADS11x5 chips have a base 7-bit I2C address of 0x48 (1001000) and a clever addressing scheme that allows four different addresses using just one address pin (named **ADR** for ADdRess). To program the address, connect the address pin as follows:

![](https://cdn-learn.adafruit.com/assets/assets/000/112/700/medium800/arduino_compatibles_addrPin.png?1656448546)

The following diagram shows one board addressed as 0x48:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/676/medium800/sensors_ADC_Address_0_bb-1024.jpg?1396785706)

## Multiple Boards
By assigning each board a different address, up to 4 boards can be connected as below:![](https://cdn-learn.adafruit.com/assets/assets/000/002/677/medium800/sensors_FourBoards_bb-1024.jpg?1396785716)

- [Previous Page](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/pinouts.md)
- [Next Page](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/signal-connections.md)

## Featured Products

### ADS1115 16-Bit ADC - 4 Channel with Programmable Gain Amplifier

[ADS1115 16-Bit ADC - 4 Channel with Programmable Gain Amplifier](https://www.adafruit.com/product/1085)
For microcontrollers without an analog-to-digital converter or when you want a higher-precision ADC, the ADS1115 provides 16-bit precision at 860 samples/second over I2C. The chip can be configured as 4 single-ended input channels, or two differential channels. As a nice bonus, it even...

In Stock
[Buy Now](https://www.adafruit.com/product/1085)
[Related Guides to the Product](https://learn.adafruit.com/products/1085/guides)
### ADS1015 12-Bit ADC - 4 Channel with Programmable Gain Amplifier

[ADS1015 12-Bit ADC - 4 Channel with Programmable Gain Amplifier](https://www.adafruit.com/product/1083)
For microcontrollers without an analog-to-digital converter or when you want a higher-precision ADC, the ADS1015 provides 12-bit precision at 3300 samples/second over I2C. The chip can be configured as 4 single-ended input channels&nbsp;or two differential channels. As a nice bonus, it even...

In Stock
[Buy Now](https://www.adafruit.com/product/1083)
[Related Guides to the Product](https://learn.adafruit.com/products/1083/guides)
### STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long

[STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long](https://www.adafruit.com/product/4399)
This 4-wire cable is&nbsp;50mm / 1.9" long and fitted with JST SH female 4-pin connectors on both ends. Compared with the chunkier JST PH these are 1mm pitch instead of 2mm, but still have a nice latching feel, while being easy to insert and remove.

<a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/4399)
[Related Guides to the Product](https://learn.adafruit.com/products/4399/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)

## Related Guides

- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Arduino Lesson 16. Stepper Motors](https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Light Meter](https://learn.adafruit.com/light-meter.md)
- [Making Adabot: Part 2](https://learn.adafruit.com/making-adabot-part-2.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Digital Circuits 7: MCUs... how do they work?](https://learn.adafruit.com/mcus-how-do-they-work.md)
- [Adafruit Motor Shield](https://learn.adafruit.com/adafruit-motor-shield.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
