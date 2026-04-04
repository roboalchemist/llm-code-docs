# Source: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c.md

# Adafruit's Raspberry Pi Lesson 4. GPIO Setup

## Configuring I2C

I2C is a very commonly used standard designed to allow one chip to talk to another. So, since the Raspberry Pi can talk I2C we can connect it to a variety of I2C capable chips and modules.

The I2C bus allows multiple devices to be connected to your Raspberry Pi, each with a unique address, that can often be set by changing jumper settings on the module. It is very useful to be able to see which devices are connected to your Pi as a way of making sure everything is working.

```auto
sudo apt-get install -y python3-smbus
sudo apt-get install -y i2c-tools
```

# Installing Kernel Support (with Raspi-Config)

Run **sudo raspi-config** and follow the prompts to install i2c support for the ARM core and linux kernel

Go to **Interfacing Options**

![](https://cdn-learn.adafruit.com/assets/assets/000/045/258/medium800/learn_raspberry_pi_interfacing.png?1502764684)

On older versions, look under **Advanced**

![](https://cdn-learn.adafruit.com/assets/assets/000/022/831/medium800/learn_raspberry_pi_advancedopt.png?1423001339)

then **I2C**

![](https://cdn-learn.adafruit.com/assets/assets/000/022/832/medium800/learn_raspberry_pi_i2c.png?1423001363)

Enable!

![](https://cdn-learn.adafruit.com/assets/assets/000/022/834/medium800/learn_raspberry_pi_wouldyoukindly.png?1423001393)

![](https://cdn-learn.adafruit.com/assets/assets/000/022/833/medium800/learn_raspberry_pi_i2ckernel.png?1423001374)

```
sudo reboot
```

# Testing I2C

Now when you log in you can type the following command to see all the connected devices

```
sudo i2cdetect -y 1
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/055/medium800/learn_raspberry_pi_i2c-detect.png?1396790698)

This shows that two I2C addresses are in use – 0x40 and 0x70.  
  
These values will be different for you depending on what is currently attached to the I2C pins of your Raspberry Pi

Note that if you are using one of the very first Raspberry Pis (a 256MB Raspberry Pi Model B) then you will need to change the command to:

```
sudo i2cdetect -y 0
```

The Raspberry Pi designers swapped over I2C ports between board releases. Just remember: 512M Pi's use i2c port 1, 256M ones use i2c port 0!

When you are finished in raspi-config reboot for the i2c modules to automatically load into the kernel.

- [Previous Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/adafruit-pi-code.md)
- [Next Page](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi.md)

## Featured Products

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
### Raspberry Pi 3 Model B Starter Pack - Includes a Raspberry Pi 3

[Raspberry Pi 3 Model B Starter Pack - Includes a Raspberry Pi 3](https://www.adafruit.com/product/3058)
Gotta say - this new Pi 3 is fly. &nbsp;All the cool kids are going to have it - but all the coolest kids are also going to have a big pack of super cool accessories.

We've hand chosen these accessories as the perfect accompaniment to your new Raspberry Pi 3 - Model B. &nbsp;It's...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/3058)
[Related Guides to the Product](https://learn.adafruit.com/products/3058/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)

[Budget Pack for Raspberry Pi 1 Model B (Doesn't include RasPi)](https://www.adafruit.com/product/965)
An optimized collection of parts and pieces to experiment with Raspberry Pi at home, school or work. Great for students and those that want to get their feet wet, no soldering required! **THIS PACK DOES NOT INCLUDE A RASPBERRY PI 1 MODEL B and is NOT compatible with Model B+ or Raspberry Pi...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/965)
[Related Guides to the Product](https://learn.adafruit.com/products/965/guides)
### GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin

[GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin](https://www.adafruit.com/product/862)
That new Raspberry Pi® Model A or B computer you just got has a row of 2x13 pin headers soldered on - those are the GPIO (general purpose input/output) pins and for those of us who like to hack electronics they are where the real fun is. By programming the Pi, you can twiddle those pins...

In Stock
[Buy Now](https://www.adafruit.com/product/862)
[Related Guides to the Product](https://learn.adafruit.com/products/862/guides)
### Programming the Raspberry Pi: Getting Started with Python

[Programming the Raspberry Pi: Getting Started with Python](https://www.adafruit.com/product/1089)
 **Program your own Raspberry Pi projects!**

An updated guide to programming your own Raspberry Pi projects. Learn to create inventive programs and fun games on your powerful Raspberry Pi--with no programming experience required. **This practical book has been revised...**

In Stock
[Buy Now](https://www.adafruit.com/product/1089)
[Related Guides to the Product](https://learn.adafruit.com/products/1089/guides)

## Related Guides

- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Drive a 16x2 LCD with the Raspberry Pi](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 13. Power Control](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-13-power-control.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Setting up a Raspberry Pi with NOOBS](https://learn.adafruit.com/setting-up-a-raspberry-pi-with-noobs.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
