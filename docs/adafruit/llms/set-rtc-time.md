# Source: https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-rtc-time.md

# Adding a Real Time Clock to Raspberry Pi

## Set RTC Time

Now that we have the module wired up and verified that you can see the module with i2cdetect, we can set up the module.

Warning: 

# Raspberry Pi OS's with systemd

This should be the case for any current release. For much older releases without systemd, skip to the next section.

_[Thanks to ad8g for the hints!](https://ad8g.net/2015/10/29/adding-a-real-time-clock-on-raspbian-jessie/)_

You can add support for the RTC by adding a device tree overlay. Run

**sudo nano /boot/config.txt**

to edit the pi configuration and add whichever matches your RTC chip:

`dtoverlay=i2c-rtc,ds1307`

or

`dtoverlay=i2c-rtc,pcf8523`

or

`dtoverlay=i2c-rtc,ds3231`

to the end of the file

![](https://cdn-learn.adafruit.com/assets/assets/000/035/976/medium800/raspberry_pi_dtoverlay.png?1474665354)

Save it and run `sudo reboot` to start again. Log in and run `sudo i2cdetect -y 1` to see the UU show up where 0x68 should be

![](https://cdn-learn.adafruit.com/assets/assets/000/035/977/medium800/raspberry_pi_UU.png?1474665431)

Disable the "fake hwclock" which interferes with the 'real' hwclock

```terminal
sudo apt-get -y remove fake-hwclock
sudo update-rc.d -f fake-hwclock remove
sudo systemctl disable fake-hwclock
```

![](https://cdn-learn.adafruit.com/assets/assets/000/036/611/medium800/raspberry_pi_removehwclock.png?1476488388)

Now with the fake-hw clock off, you can start the original 'hardware clock' script.

Run **sudo nano /lib/udev/hwclock-set** and comment out these three lines **:**

**#if [-e /run/systemd/system] ; then  
# exit 0  
#fi**

![](https://cdn-learn.adafruit.com/assets/assets/000/036/616/medium800/raspberry_pi_hwclock-set.png?1476496229)

Also comment out the two lines

` /sbin/hwclock --rtc=$dev --systz --badyear`

and

`/sbin/hwclock --rtc=$dev --systz`

![](https://cdn-learn.adafruit.com/assets/assets/000/075/786/medium800/pi_a___b___2__3_image.png?1558249620)

## Sync time from Pi to RTC

When you first plug in the RTC module, it's going to have the wrong time because it has to be set once. You can always read the time directly from the RTC with `sudo hwclock -r`

(ignore use of deprecated -D parameter in the screenshot)

![](https://cdn-learn.adafruit.com/assets/assets/000/036/612/medium800/raspberry_pi_invalidclok.png?1476489364)

You can see, the date at first is invalid! You can set the correct time easily. First run `date` to verify the time is correct. Plug in Ethernet or WiFi to let the Pi sync the right time from the Internet. Once that's done, run `sudo hwclock -w` to **w** rite the time, and another `sudo hwclock -r` to **r** ead the time

![](https://cdn-learn.adafruit.com/assets/assets/000/036/613/medium800/raspberry_pi_setrtc.png?1476489499)

Once the time is set, make sure the coin cell battery is inserted so that the time is saved. You only have to set the time _once_

That's it! Next time you boot the time will automatically be synced from the RTC module

To only ready time from the RTC and not the internet, you can disable the timesync service with:

```terminal
sudo systemctl disable systemd-timesyncd.service
```

### 

If you are getting an error message like this when trying to read/write to the RTC, make sure you have a good coin cell battery installed.

# Raspbian Wheezy or other pre-systemd Linux

First, load up the RTC module by running

`sudo modprobe i2c-bcm2708 sudo modprobe i2c-dev sudo modprobe rtc-ds1307`

Then, as root (type in **sudo bash** ) run

`echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device`

If you happen to have an old Rev 1 Pi, type in

`echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device`

You can then type in **exit** to drop out of the root shell.  
  
Then check the time with **sudo hwclock -r** which will read the time from the DS1307 module. If this is the first time the module has been used, it will report back Jan 1 2000, and you'll need to set the time

![](https://cdn-learn.adafruit.com/assets/assets/000/001/938/medium800/raspberry_pi_jan01.gif?1447864325)

First you'll need to get the right time set on the Pi, the easiest way is to connect it up to Ethernet or Wifi - it will automatically set the time from the network. Once the time is correct (check with the **date** command), run **sudo hwclock -w** to write the system time to the RTC  
  
You can then verify it with **sudo hwclock -r**

![](https://cdn-learn.adafruit.com/assets/assets/000/001/940/medium800/raspberry_pi_hwclockset.gif?1447864326)

Next, you'll want to add the RTC kernel module to the /etc/modules list, so its loaded when the machine boots. Run **sudo nano /etc/modules** and add **rtc-ds1307** at the end of the file (the image below says rtc-1307 but its a typo)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/939/medium800/raspberry_pi_addmodule.gif?1447864325)

Older pre-Jessie raspbian is a little different. First up, you'll want to create the DS1307 device creation at boot, edit /etc/rc.local by running

`sudo nano /etc/rc.local`

and add:

> `echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device` _(for v1 raspberry pi)_  
> `echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device` _(for v2 raspberry pi)_  
> `sudo hwclock -s` _(both versions)_

before `exit 0` (we forgot the hwclock -s part in the screenshot below)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/941/medium800/raspberry_pi_etcrclocal.gif?1447864330)

That's it! Next time you boot the time will automatically be synced from the RTC module

- [Previous Page](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-up-and-test-i2c.md)

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
