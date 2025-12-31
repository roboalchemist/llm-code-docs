# Source: https://learn.adafruit.com/2-8-tft-touch-shield/touchscreen-paint-example.md

# 2.8" TFT Touch Shield

## Touchscreen Paint Example

The LCD has a 2.8" 4-wire resistive touch screen glued onto it. You can use this for detecing finger-presses, stylus', etc. You'll need 4 pins to talk to the touch panel **but** we **reuse** some of the pins for the TFT LCD! This is because the resistance of the panel is high enough that it doesn't interfere with the digital input/output and we can query the panel in between TFT accesses, when the pins are not being used.

This tutorial requires the installation of the **Adafruit Touchscreen&nbsp;** library. This library is available for installation on the Arduino library manager.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/320/medium800/arduino_compatibles_library_manager_menu.png?1573837892)

Search for the&nbsp; **Adafruit Touchscreen&nbsp;** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/321/medium800/arduino_compatibles_touchscreen.png?1573837914)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

# Example

We connect the 4 pins as follows:

&nbsp;

- Y+ is connected to Analog 1
- Y- is connected to Digital 7
- X+ is connected to Digital 6
- X- is connected to Analog 2

Now start up the **tftpaint\_shield** example in the TFTLCD library. The right hand side will have 'color boxes' you can press to select which color you want to draw with. If you press the area to the **left** where the screen ends, it will erase the screen.

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/798/medium800/lcds___displays_tftshield.jpg?1396787159)

- [Previous Page](https://learn.adafruit.com/2-8-tft-touch-shield/adafruit-gfx-library.md)
- [Next Page](https://learn.adafruit.com/2-8-tft-touch-shield/bitmaps.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)

## Related Guides

- [LED Lightbox](https://learn.adafruit.com/led-lightbox.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Geofencing with the FONA 808 & Adafruit IO](https://learn.adafruit.com/geofencing-with-the-fona-808-and-adafruit-io.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [Mini Thermal Receipt Printers](https://learn.adafruit.com/mini-thermal-receipt-printer.md)
- [Bluefruit LE Connect for iOS and Android](https://learn.adafruit.com/bluefruit-le-connect.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Arduino Lesson 9. Sensing Light](https://learn.adafruit.com/adafruit-arduino-lesson-9-sensing-light.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Adafruit 16-channel PWM/Servo Shield](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield.md)
- [Naughty or Nice Machine](https://learn.adafruit.com/naughty-or-nice-machine.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
