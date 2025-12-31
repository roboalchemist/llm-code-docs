# Source: https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-up-and-test-i2c.md

# Adding a Real Time Clock to Raspberry Pi

## Set Up & Test I2C

# Set up I2C on your Pi

You'll also need to set up i2c on your Pi, to do so, run **sudo raspi-config** and under **Interface Options&nbsp;** select I2C and turn it on.

For more details, check out our tutorial on Raspberry Pi i2c setup and testing at [http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

You may need to reboot once you've done that with **sudo reboot**

# Verify Wiring (I2C scan)

Verify your wiring by running

```terminal
sudo apt-get install python3-smbus i2c-tools
```

to install the helper software and then `sudo i2cdetect -y 1 `at the command line, you should see ID #68 show up - that's the address of the DS1307, PCF8523 or DS3231!

If you have a much older Pi 1, you will have to run `sudo i2cdetect -y 0 `as the I2C bus address changed from 0 to 1

![](https://cdn-learn.adafruit.com/assets/assets/000/036/610/medium800/raspberry_pi_addr68.gif?1476488120)

Warning: 

- [Previous Page](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/wiring-the-rtc.md)
- [Next Page](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-rtc-time.md)

## Featured Products

### Adafruit PiRTC - PCF8523 Real Time Clock for Raspberry Pi

[Adafruit PiRTC - PCF8523 Real Time Clock for Raspberry Pi](https://www.adafruit.com/product/3386)
This is a great battery-backed real time clock (RTC) that allows your Raspberry Pi project to keep track of time if the power is lost. Perfect for data-logging, clock-building, time-stamping, timers and alarms, etc. Equipped with&nbsp; **PCF8523** &nbsp;RTC, it works great with the...

In Stock
[Buy Now](https://www.adafruit.com/product/3386)
[Related Guides to the Product](https://learn.adafruit.com/products/3386/guides)
### Adafruit PiRTC - Precise DS3231 Real Time Clock for Raspberry Pi

[Adafruit PiRTC - Precise DS3231 Real Time Clock for Raspberry Pi](https://www.adafruit.com/product/4282)
This is the best battery-backed real time clock (RTC) you can get that allows your Raspberry Pi project to keep track of time if the power is lost. Perfect for data-logging, clock-building, NTP servers, time-stamping, timers and alarms, etc. Equipped with **a genuine DS3231** RTC,...

In Stock
[Buy Now](https://www.adafruit.com/product/4282)
[Related Guides to the Product](https://learn.adafruit.com/products/4282/guides)
### Adafruit PCF8523 Real Time Clock Assembled Breakout Board

[Adafruit PCF8523 Real Time Clock Assembled Breakout Board](https://www.adafruit.com/product/3295)
This is a great battery-backed real time clock (RTC) that allows your microcontroller project to keep track of time even if it is reprogrammed, or if the power is lost. Perfect for datalogging, clock-building, time stamping, timers and alarms, etc. Equipped...

In Stock
[Buy Now](https://www.adafruit.com/product/3295)
[Related Guides to the Product](https://learn.adafruit.com/products/3295/guides)
### Adafruit DS1307 Real Time Clock Assembled Breakout Board

[Adafruit DS1307 Real Time Clock Assembled Breakout Board](https://www.adafruit.com/product/3296)
This is a great battery-backed real time clock (RTC) that allows your microcontroller project to keep track of time even if it is reprogrammed, or if the power is lost. Perfect for datalogging, clock-building, time stamping, timers and alarms, etc. The **DS1307** is the most...

In Stock
[Buy Now](https://www.adafruit.com/product/3296)
[Related Guides to the Product](https://learn.adafruit.com/products/3296/guides)
### ChronoDot - Ultra-precise Real Time Clock

[ChronoDot - Ultra-precise Real Time Clock](https://www.adafruit.com/product/255)
The **ChronoDot V3** is the latest version of macetech’s popular ChronoDot line of products. Designed during the Great Chip Shortage, it uses the newly-released MAX31328 temperature-compensated real-time clock chip. However, it remains pin- and code-compatible with the older...

In Stock
[Buy Now](https://www.adafruit.com/product/255)
[Related Guides to the Product](https://learn.adafruit.com/products/255/guides)
### Adafruit DS3231 Precision RTC Breakout

[Adafruit DS3231 Precision RTC Breakout](https://www.adafruit.com/product/3013)
The datasheet for the **DS3231** explains that this part is an "Extremely Accurate I²C-Integrated RTC/TCXO/Crystal". And, hey, it does exactly what it says on the tin! This **Real Time Clock (RTC)** is the most precise you can get in a small, low power...

In Stock
[Buy Now](https://www.adafruit.com/product/3013)
[Related Guides to the Product](https://learn.adafruit.com/products/3013/guides)
### CR1220 12mm Diameter - 3V Lithium Coin Cell Battery

[CR1220 12mm Diameter - 3V Lithium Coin Cell Battery](https://www.adafruit.com/product/380)
These are the highest quality & capacity batteries, the same as shipped with the iCufflinks,&nbsp;iNecklace, Datalogging and GPS Shields, GPS HAT, etc. One battery per order (you'll want one battery per cufflink or pendant.)  
  
Brand may vary but all battery brands are verified...

In Stock
[Buy Now](https://www.adafruit.com/product/380)
[Related Guides to the Product](https://learn.adafruit.com/products/380/guides)
### DS1307 Real Time Clock breakout board kit

[DS1307 Real Time Clock breakout board kit](https://www.adafruit.com/product/264)
**[We've upgraded this RTC breakout and made it even easier to use! Now available as a fully assembled board, it has the same components, chip, size, etc but you don't have to put it together. It's also less expensive! Check out...](https://www.adafruit.com/product/3296)**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/264)
[Related Guides to the Product](https://learn.adafruit.com/products/264/guides)

## Related Guides

- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [DS1307 Real Time Clock Breakout Board Kit](https://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit.md)
- [NeoPixel 60 Ring Wall Clock](https://learn.adafruit.com/neopixel-60-ring-clock.md)
- [NeoMatrix 8x8 Word Clock](https://learn.adafruit.com/neomatrix-8x8-word-clock.md)
- [Adafruit DS3231 Precision RTC Breakout](https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout.md)
- [MacroPad 2FA TOTP Authentication Friend](https://learn.adafruit.com/macropad-2fa-totp-authentication-friend.md)
- [Plotting Offline Data - JSONL to CSV files, filters and graphs](https://learn.adafruit.com/plotting-offline-data-jsonl-to-csv-files-filters-and-graphs.md)
- [Large Pi-based Thermometer and Clock](https://learn.adafruit.com/large-pi-based-thermometer-and-clock.md)
- [Blahaj Alarm and Lamp](https://learn.adafruit.com/blahaj-alarm.md)
- [Prop-Maker Feather Talking Adabot Clock](https://learn.adafruit.com/prop-maker-feather-talking-adabot-clock.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Monitor PiCam and temperature on a PiTFT via adafruit.io](https://learn.adafruit.com/monitor-picam-and-temperature-on-a-pitft-via-adafruit-dot-io.md)
- [DotStar Pi Painter](https://learn.adafruit.com/dotstar-pi-painter.md)
- [NextBus transit clock for Raspberry Pi](https://learn.adafruit.com/nextbus-transit-clock-for-raspberry-pi.md)
- [Wood Case for Raspberry Pi 3](https://learn.adafruit.com/wood-case-for-raspberry-pi-3.md)
