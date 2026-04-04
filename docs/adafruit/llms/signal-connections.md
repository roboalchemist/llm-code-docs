# Source: https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/signal-connections.md

# Adafruit 4-Channel ADC Breakouts

## Signal Connections

![](https://cdn-learn.adafruit.com/assets/assets/000/002/680/medium800/sensors_ADS1015.jpg?1396785737)

## Single Ended vs. Differential Inputs:
The ADS1x15 breakouts support up to 4 SIngle Ended or 2 Differential inputs.  
  
**Single Ended** inputs measure the voltage between the analog input channel (A0-A3) and analog ground (GND).  
  
**Differential** inputs measure the voltage between two analog input channels. &nbsp;(A0&A1 or A2&A3).  
## Which should I use?
Single ended inputs give you twice as many inputs. So why would you want to use differential inputs?   
  
Single ended inputs can, by definition, only measure positive voltages. Without the sign bit, you only get an effective 15 bit resolution.  
  
In addition to providing the full 16 bits of resolution and the ability to measure negative voltages, Differential measurements offer more immunity from electromagnetic noise. This is useful when using long signal wires or operating in an electrically noisy environment. This is also desirable when dealing with small signals requiring high gain, since the gain will amplify the noise as well as the signal.  
## Single Ended Connections:
Connect the signal wire to one of the analog input channels (A0 - A3). &nbsp;Connect the ground wire to GND. &nbsp;This diagram shows how to connect an ADXL335 to for measurement of the X, Y and Z axis on analog channels A0, A1 and A2. ![](https://cdn-learn.adafruit.com/assets/assets/000/002/678/medium800/sensors_ADC_SingleEnded_bb-1024.jpg?1396785723)

## Differential Connections:

Differential measurements use a pair of input pins, either A0&A1 or A2&A3. &nbsp;The following diagram shows connections for differential measurement of the battery voltage on a LiPo charger board.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/679/medium800/sensors_ADC_Differential_bb-1024.jpg?1396785730)

Danger: 

- [Previous Page](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/assembly-and-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython.md)

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
