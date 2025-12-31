# Source: https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/init-script.md

# Drive a 16x2 LCD with the Raspberry Pi

## Display Time & IP on Every Boot

It's all fine and dandy to have a script which we can manually run, but wouldn't it be nice to have the time and ip address pop up on the display when the Raspberry Pi boots up? This is done using an init script which runs our Python code every time your Raspberry Pi boots up.&nbsp;

## Download the service file
The following command will allow you to download the lcd.service file directly to your Pi.

```auto
wget https://raw.githubusercontent.com/adafruit/Adafruit_Learning_System_Guides/master/Drive_a_16x2_LCD_with_the_Raspberry_Pi/lcd.service
```

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Drive_a_16x2_LCD_with_the_Raspberry_Pi/lcd.service

## Place the lcd.service file
The lcd.service file needs to be copied into the correct location and the systemctl command can be used to start | stop | enable the service. It is a good idea to test this before enabling as there might be a minor path difference on your system.&nbsp;

```auto
sudo cp lcd.service /etc/systemd/system
```

## Test the lcd.service
```auto
sudo systemctl daemon-reload
sudo systemctl start lcd.service
ps auxww | grep -i 16x2
```

![](https://cdn-learn.adafruit.com/assets/assets/000/069/574/medium800/learn_raspberry_pi_ps-rpi-screenshot.png?1547774442)

The following commands read the updates to the service file, start the lcd.service and confirm that the process is running. If the script shows up in the 'ps' command output you have done everything correctly and can now enable the service and reboot. The service should activate upon bootup automatically.

## Enable lcd.service
```auto
sudo systemctl enable lcd.service
```

Now on each boot the LCD will automatically show the date/time/ip address on startup. This means you will know when the Pi is reachable and what the ip address is without having to plug a monitor in.

- [Previous Page](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/python-code.md)
- [Next Page](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/time-zone.md)

## Featured Products

### Standard LCD 16x2 + extras

[Standard LCD 16x2 + extras](https://www.adafruit.com/product/181)
Standard HD44780 LCDs are useful for creating standalone projects.

- 16 characters wide, 2 rows
- White text on blue background
- Connection port is 0.1" pitch, single row for easy breadboarding and wiring
- Pins are documented on the back of the LCD to assist...

In Stock
[Buy Now](https://www.adafruit.com/product/181)
[Related Guides to the Product](https://learn.adafruit.com/products/181/guides)
### Raspberry Pi 3 - Model B - ARMv8 with 1G RAM

[Raspberry Pi 3 - Model B - ARMv8 with 1G RAM](https://www.adafruit.com/product/3055)
Did you really think the Raspberry Pi would stop getting better? At this point, we sound like a broken record, extolling on the new Pi’s myriad improvements like we’re surprised that the folks at the Raspberry Pi Foundation are continuously making their flagship board better.&nbsp;...

In Stock
[Buy Now](https://www.adafruit.com/product/3055)
[Related Guides to the Product](https://learn.adafruit.com/products/3055/guides)
### Adafruit Assembled Pi T-Cobbler Breakout for Raspberry Pi

[Adafruit Assembled Pi T-Cobbler Breakout for Raspberry Pi](https://www.adafruit.com/product/1754)
Now that you've finally got your hands on a [Raspberry Pi®](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an **assembled** add on prototyping Pi T-Cobbler from Adafruit, which can...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1754)
[Related Guides to the Product](https://learn.adafruit.com/products/1754/guides)
### Assembled Pi Cobbler Plus - Breakout Cable

[Assembled Pi Cobbler Plus - Breakout Cable](https://www.adafruit.com/product/2029)
The Raspberry Pi B+ / Pi 2 / Pi 3 / Pi 4&nbsp;has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit card sized bomb of DIY joy. And while you can use most of our great Model B accessories by hooking up our [downgrade...](https://www.adafruit.com/product/1986)

In Stock
[Buy Now](https://www.adafruit.com/product/2029)
[Related Guides to the Product](https://learn.adafruit.com/products/2029/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)

## Related Guides

- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Circadian Pi Desk Light](https://learn.adafruit.com/circadian-pi-desk-light.md)
- [Speech Synthesis on the Raspberry Pi](https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [Raspberry Pi Analog to Digital Converters](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Getting Started With Windows IoT Core on Raspberry Pi](https://learn.adafruit.com/getting-started-with-windows-iot-on-raspberry-pi.md)
- [Trinket Ultrasonic Rangefinder](https://learn.adafruit.com/trinket-ultrasonic-rangefinder.md)
