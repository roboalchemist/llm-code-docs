# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-hacks.md

# Arduino Tips, Tricks, and Techniques

## Arduino Hacks

## Bumpers
Having the conductive traces touch your table is not so great, you can protect your Arduino by adding bumpers to the bottom.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/540/medium800/learn_arduino_decimillabumper_MED.jpg?1396798154)

You can buy these from McMaster Carr part no. [95495K66](http://www.mcmaster.com/nav/enter.asp?partnum=95495K66&pagenum=3612) (in large quantities) or [Adafruit](http://www.adafruit.com/products/550)

## Free up some RAM
If you're working on a project that needs **a lot** of memory, you can free up 100 more bytes (10% of the RAM on an ATmega168!) by lessening the serial receive buffer. By default its 128 bytes, which is quite a bit!  
  
Open up **hardware/cores/arduino** (or **cores/arduino** ) directory, and edit the file named **wiring\_serial.c** or **HardwareSerial.cpp**  
  
Near the top is a **#define RX\_BUFFER\_SIZE 128** , which means 128 bytes are used for the buffer. You can change this to 32 (or even 16!). If you have almost no serial input, make it as low as you'd like as long as its \> 0.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/541/medium800/learn_arduino_rxbuffermod.jpg?1396798163)

You can also save another 2 bytes by changing **rx\_buffer\_head** and **rx\_buffer\_tail** from **int** to **uint8\_t**

- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/3-3v-conversion.md)
- [Next Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduinoisp.md)

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
