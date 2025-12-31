# Source: https://learn.adafruit.com/36mm-led-pixels.md

# 36mm LED Pixels

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/001/136/medium800/led_pixels_ID683_LRG.jpg?1396769137)

RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each pixel contains four RGB LEDs and a controller chip in a sturdy metal housing.&nbsp;The pixel is then 'flooded' with epoxy to make it waterproof. These are fairly large pixels but they have a lot of nice mounting options, such as two metal flanges on the side and a 0.15"/4mm diameter hole in the middle so you can screw them directly onto a surface. They're typically used to make outdoor signs. Compared to our other LED dots, these are much bigger and much brighter, good for larger scale installations.  
  
At&nbsp; **12 volts** , they draw a maximum of&nbsp; **120 milliamps** &nbsp;per pixel: 40 mA each for red, green and blue.  
  
The LED pixels are spaced along a strand of ribbon cable, with about&nbsp;**3 inches (75mm)**&nbsp;between pixels. If additional distance is needed you can cut the ribbon cable and solder 4 wires to extend the gap to the desired length.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/137/medium800/led_pixels_36mmbundle.jpg?1396769142)

Each pixel contains a small microchip. The WS2801 LED driver chip is custom designed for this purpose. We provide an Arduino library for communicating with the pixels (explained in subsequent pages), but if you want to write your own code for other microcontrollers, they’re very easy to communicate with using an SPI-like protocol. For each pixel, one “shifts out” 24 bits of color information — the first data out corresponds to the pixel closest to the microcontroller. To write colors to 10 LEDs, you would issue 240 bytes (10 \* 24). Following the data, a 500 microsecond pause will then “latch” the data and display the new LED colors.

- [Next Page](https://learn.adafruit.com/36mm-led-pixels/project-ideas.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 12V 5A switching power supply

[12V 5A switching power supply](https://www.adafruit.com/product/352)
This is a beefy switching supply, for when you need a lot of power! It can supply 12V DC up to 5 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard 'figure-8'...

Out of Stock
[Buy Now](https://www.adafruit.com/product/352)
[Related Guides to the Product](https://learn.adafruit.com/products/352/guides)
### 36mm  Square 12V Digital RGB LED Pixels (Strand of 20)

[36mm  Square 12V Digital RGB LED Pixels (Strand of 20)](https://www.adafruit.com/product/683)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each metal 'pixel square' contains 4 RGB LEDs and a controller chip soldered to a PCB. The pixel is then 'flooded' with epoxy to make it water resistant, however we cannot say 100% waterproof you...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/683)
[Related Guides to the Product](https://learn.adafruit.com/products/683/guides)

## Related Guides

- [Arduino Lesson 0. Getting Started](https://learn.adafruit.com/lesson-0-getting-started.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Sous-vide controller powered by Arduino - The SousViduino!](https://learn.adafruit.com/sous-vide-powered-by-arduino-the-sous-viduino.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [SMS Texting Pet Food Dish](https://learn.adafruit.com/sms-texting-pet-food-dish.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Low Power Coin Cell Voltage Logger](https://learn.adafruit.com/low-power-coin-cell-voltage-logger.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [20mm LED Pixels](https://learn.adafruit.com/20mm-led-pixels.md)
- [Arduino Lesson 11. LCD Displays - Part 1](https://learn.adafruit.com/adafruit-arduino-lesson-11-lcd-displays-1.md)
