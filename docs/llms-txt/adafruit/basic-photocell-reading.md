# Source: https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading.md

# Basic Resistor Sensor Reading on Raspberry Pi

## Basic Photocell Reading

![](https://cdn-learn.adafruit.com/assets/assets/000/001/327/medium800/raspberry_pi_cds_LRG.jpg?1396771063)

We'll start with a basic photocell. This is a resistor that changes resistance based on how bright the light is. [You can read tons more about photocells in our tutorial](http://learn.adafruit.com/photocells/) but basically we'll be able to measure how bright or dark the room is using the photocell. Note that photocells are not precision measurement devices, and this technique is also not very precise so its only good for basic measurements. [For precision sensing, you'd want a digital lux sensor like this one](https://www.adafruit.com/products/439) - we don't have a tutorial on connecting that to the Pi but we do have example code for Arduino.

## Download the Code
The following code can be downloaded to your raspberry pi

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Basic_Resistor_Sensor_Reading_on_Raspberry_Pi/Basic_Resistor_Sensor_Reading_on_Raspberry_Pi.py

Let's put this file right in your home directory for simplicity. The wget command makes things easy.

```
$ wget https://raw.githubusercontent.com/adafruit/Adafruit_Learning_System_Guides/master/Basic_Resistor_Sensor_Reading_on_Raspberry_Pi/Basic_Resistor_Sensor_Reading_on_Raspberry_Pi.py
```

# Running the Code
With the Pi connected to the Cobbler, run the script and shade your hand over the sensor to test it out!

The following command will start the program and you should see the ADC output on your screen.

```
$ sudo python3 ./Basic_Resistor_Sensor_Reading_on_Raspberry_Pi.py
```

![](https://cdn-learn.adafruit.com/assets/assets/000/072/430/medium800/force___flex_Screen_Shot_2019-03-07_at_9.01.47_PM.png?1552017739)

Once you know it works you can change what pin you are using by changing the

**RCpin = board.D18&nbsp;**

**to**

**RCpin = board.D(**_yourpinnumberhere_**)**

any pin will work.

- [Previous Page](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/wiring.md)

## Featured Products

### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Photo cell (CdS photoresistor)

[Photo cell (CdS photoresistor)](https://www.adafruit.com/product/161)
CdS cells are little light sensors. As the squiggly face is exposed to more light, the resistance goes down. When it's light, the resistance is about ~1KΩ, when dark it goes up to ~10KΩ.

To use, connect one side of the photocell (either one, it's symmetric) to power...

In Stock
[Buy Now](https://www.adafruit.com/product/161)
[Related Guides to the Product](https://learn.adafruit.com/products/161/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Long Flex sensor

[Long Flex sensor](https://www.adafruit.com/product/182)
This sensor can detect flexing or bending in one direction. They were popularized by being used in the Nintendo PowerGlove as a gaming interface.  
  
These sensors are easy to use, they are basically resistors that change value based on how much they're&nbsp;flexed. If they're...

In Stock
[Buy Now](https://www.adafruit.com/product/182)
[Related Guides to the Product](https://learn.adafruit.com/products/182/guides)
### Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force

[Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force](https://www.adafruit.com/product/166)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF01A-N-221-A01&nbsp;with 1/2 diameter sensing region.

We used to stock the Interlink model 402 FSR - the Alpha version is almost half the price...

In Stock
[Buy Now](https://www.adafruit.com/product/166)
[Related Guides to the Product](https://learn.adafruit.com/products/166/guides)

## Related Guides

- [Adding Basic Audio Ouput to Raspberry Pi Zero](https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [CircuitPython Libraries on Linux and Google Coral](https://learn.adafruit.com/circuitpython-on-google-coral-linux-blinka.md)
- [Speech Synthesis on the Raspberry Pi](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Adafruit 16-Channel PWM/Servo HAT & Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi.md)
