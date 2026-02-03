# Source: https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/wire-leds.md

# Raspberry Pi E-mail Notifier Using LEDs

## Wire the Cobbler to the LEDs

Modern Raspberry Pi's use a 40-pin header. The first generation of Pi's used a 26-pin header. This tutorial works with all of these versions using the same code and GPIO pins. We have provided wiring examples of both types using the same GPIO pins (#18 and #23).

When connecting the GPIO cable, make sure that you note the red or white wire on the ribbon, that's pin #1 of the cable. That end goes at the side closest to the SD Card and is labeled&nbsp; **P1** on the Pi. The other side connects to the cobbler and can only be inserted one way due to the notch in the cable.  
  
Place the cobbler onto the bread board straddling the center line. Connect the&nbsp; **GND** pin (ground) to the blue power rail on the side of the breadboard. You'll need two resistors (any values&nbsp;from 330 ohm up to 1000 ohm are fine).

Connect the first resistor to the cobbler row marked&nbsp; **#18** , and the other end to a row that isn't used by the cobbler.

Connect the second resistor to the cobbler row marked # **23** and the other end to another empty row.

# Raspberry Pi Cobbler Plus - 40-pin for Pi v2, v3, Zero
![](https://cdn-learn.adafruit.com/assets/assets/000/024/094/medium800/raspberry_pi_email_blinkies_bb.png?1427489683)

# Raspberry Pi Cobber - 26-pin - for Pi v1 only
![](https://cdn-learn.adafruit.com/assets/assets/000/024/147/medium800/raspberry_pi_little_cobbler_bb.png?1427733019)

# Step-by-Step Hookup on a 26-pin Pi Cobbler
![](https://cdn-learn.adafruit.com/assets/assets/000/000/716/medium800/raspberry_pi_resistors.jpg?1396765277)

Now grab a red LED and a green LED. Look for the long pins on the LEDs; those are the positive (+) legs.

Connect the long (+) leg of the red LED to the resistor connected to&nbsp; **#23** &nbsp;(GPIO #23), and the long leg of the green LED to&nbsp;the resistor connected to&nbsp; **#18**.

The short legs plug into the blue striped rail on the side of the breadboard.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/720/medium800/raspberry_pi_leds.jpg?1396765317)

The above images are for an original Pi Cobbler. For newer, 40-pin models like the A+/B+/Pi 2, you'll probably want to do something more like this, using wires to connect the resistors to the LEDs (click for a larger image):

That's it! You've just wired two LEDs with current-limiting resistors to the GPIO pins of the Pi.

- [Previous Page](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview.md)
- [Next Page](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/necessary-packages.md)

## Featured Products

### Raspberry Pi Starter Pack

[Raspberry Pi Starter Pack](https://www.adafruit.com/product/3049)
You're going to work hard with your Raspberry Pi 2 Model B or Raspberry Pi 1 Model B+. &nbsp;You're going to have to solder, code, and Linux your Maker heart out. &nbsp;That's why we've tried to make it as easy as possible to start...

In Stock
[Buy Now](https://www.adafruit.com/product/3049)
[Related Guides to the Product](https://learn.adafruit.com/products/3049/guides)
### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### 5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable

[5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable](https://www.adafruit.com/product/1995)
Our all-in-one 5V 2.5 Amp + MicroUSB cable power adapter is the perfect choice for powering single-board computers like Raspberry Pi, BeagleBone, or anything else that's power-hungry!

This adapter was specifically designed to provide 5.25V, not 5V, but we still call it a 5V USB...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1995)
[Related Guides to the Product](https://learn.adafruit.com/products/1995/guides)
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
### Diffused Red 10mm LED (25 pack)

[Diffused Red 10mm LED (25 pack)](https://www.adafruit.com/product/845)
Need some big indicators? We are big fans of these huge diffused red LEDs. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25 diffused red LEDs
- 10mm...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/845)
[Related Guides to the Product](https://learn.adafruit.com/products/845/guides)
### Diffused Green 10mm LED (25 pack)

[Diffused Green 10mm LED (25 pack)](https://www.adafruit.com/product/844)
Need some big indicators? We are big fans of these huge 10mm diffused green LEDs. They are fairly bright so they can be seen in daytime, and from any angle. They go easily into a breadboard and will add that extra zing to your project.

- Pack of 25 diffused green LEDs
- 10mm...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/844)
[Related Guides to the Product](https://learn.adafruit.com/products/844/guides)

## Related Guides

- [Speech Synthesis on the Raspberry Pi](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Drive a 16x2 LCD with the Raspberry Pi](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md)
- [Adding Basic Audio Ouput to Raspberry Pi Zero](https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [IoT Temperature Logger with Analog Devices ADT7410, Raspberry Pi, and Adafruit IO](https://learn.adafruit.com/iot-temperature-logger-with-python-and-adafruit-io.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Large Pi-based Thermometer and Clock](https://learn.adafruit.com/large-pi-based-thermometer-and-clock.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
