# Source: https://learn.adafruit.com/beaglebone/wifi.md

# BeagleBone

## WiFi

Info: 

Now that you have your Bone up and running, and Ethernet works, wouldn't it be nice to get rid of that Ethernet cable? Yeah, let's go WiFi! This tutorial is specifically for the verified&nbsp;**[WiFi adapter for Beagle Bone](http://www.adafruit.com/products/814)&nbsp;**adapter in the Adafruit shop. It will not work with other WiFi adapters, as they all have different chipsets!![](https://cdn-learn.adafruit.com/assets/assets/000/000/120/medium800/beaglebone_wifiplug.jpg?1396760591)

For this tutorial you will need:

- **[Beagle Bone](http://www.adafruit.com/products/513)**
- **[WiFi adapter](http://www.adafruit.com/products/814)**
- **[5V 2000mA Power Adapter](http://www.adafruit.com/products/276)**

Pick these parts up at the Adafruit shop!

## Power and WiFi
  
The BeagleBone has the neat ability to power itself just through the mini USB port. However, this can cause some problems because the USB port cannot supply enough power for BOTH the Bone and a WiFi adapter.  
Info: 

## Driver Install
You'll need to have [Internet connectivity using Ethernet](http://learn.adafruit.com/beaglebone) , and also be logged into the terminal to install the WiFi   
adpater's driver, so make sure to complete those tutorials first!

While logged in with Internet working, run **opkg update**

Then run **mkdir /home/root/tmp** to make a new temp directory then run **opkg**  **-t /home/root/tmp upgrade**

  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/121/medium800/beaglebone_opkg-update.gif?1447974714)

then type in&nbsp; **opkg list 'linux-firmware-rt** \*' and hit return.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/122/medium800/beaglebone_list-pkg.gif?1447974725)

Finally type in&nbsp; **opkg install linux-firmware-rtl8192cu** &nbsp;and press return. Plug in the WiFi dongle, then type in&nbsp; **reboot** &nbsp;and return to reboot the machine.

Now that its rebooted, check&nbsp; **dmesg** &nbsp;- you should see the following

![](https://cdn-learn.adafruit.com/assets/assets/000/000/123/medium800/beaglebone_postreboot.gif?1447974735)

And if you type in&nbsp; **ifconfig wlan0** &nbsp;there should be a link, it wont be connected yet so there's a lot of 0's and no&nbsp; **inet addr** ![](https://cdn-learn.adafruit.com/assets/assets/000/000/124/medium800/beaglebone_ifconfigwlan0.gif?1447974745)

Now we can set up the connection manager to automatically manage the wifi. Edit&nbsp; **/var/lib/connman/settings&nbsp;** (I use vi but nano is also installed) and change WiFi from false to true, save it.![](https://cdn-learn.adafruit.com/assets/assets/000/000/125/medium800/beaglebone_viconnman.gif?1447974755)

Create a file **&nbsp;/var/lib/connman/wifi.config** &nbsp;with your settings as shown below, starting with the&nbsp;**[service\_home]**&nbsp;line and with a return after the **&nbsp;Passphrase&nbsp;** line, of course this should match your home network, not the adafruit one!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/126/medium800/beaglebone_wificonfig.gif?1447974766)

Restart connman to get it to accept the new settings:

**root@beaglebone:~# systemctl restart connman.service**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/127/medium800/beaglebone_resetartconnman.gif?1447974777)

After less than 30 seconds or so, you should be connected:

**root@beaglebone:~# ifconfig wlan0**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/128/medium800/beaglebone_wlan0up.gif?1447974788)

There should now be an&nbsp; **inet addr&nbsp;** You can then test pinging an IP address and a domain name.![](https://cdn-learn.adafruit.com/assets/assets/000/000/129/medium800/beaglebone_wlanping.gif?1447974799)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/130/medium800/beaglebone_wlandns.gif?1447974809)

Finally, if you want more detailed information about your link you can&nbsp; **opkg install wireless-tools** &nbsp;to get the&nbsp; **iwconfig** &nbsp;command, which will give you tons of details.![](https://cdn-learn.adafruit.com/assets/assets/000/000/131/medium800/beaglebone_installwirelesstools.gif?1447974820)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/132/medium800/beaglebone_iwconfig.gif?1447974829)

## Troubleshooting

If you get an error device descriptor read/64, error -71, reboot and stop the boot process with the space bar. Then add the following boot option with the follow at the U-Boot prompt  
  
setenv bootargs irqpoll RETURN  
  
boot RETURN
- [Previous Page](https://learn.adafruit.com/beaglebone/ethernet.md)
- [Next Page](https://learn.adafruit.com/beaglebone/downloads.md)

## Featured Products

### Adafruit Beagle Bone Black Starter Pack

[Adafruit Beagle Bone Black Starter Pack](https://www.adafruit.com/product/703)
If you've heard about the Beagle Bone Black and you want to hit the ground running, this starter pack is for you. We've picked out everything you need to start out, with essential parts and accessories to save on a bundle.  
  
Includes:

- <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/703)
[Related Guides to the Product](https://learn.adafruit.com/products/703/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### Ethernet Cable - 10 ft long

[Ethernet Cable - 10 ft long](https://www.adafruit.com/product/730)
We have so many Internet-connected goodies in the shop, we figured it's time to carry a cable so you can easily connect them up! This cable is 10 feet long, black and has all 8 wires installed. Perfect for use with the [BeagleBone](http://www.adafruit.com/products/513), <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/730)
[Related Guides to the Product](https://learn.adafruit.com/products/730/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)

## Related Guides

- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [SSD1306 OLED Displays with Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black.md)
- [RePaper eInk Development Board for ARM + GNU/Linux](https://learn.adafruit.com/repaper-eink-development-board-arm-linux-raspberry-pi-beagle-bone-black.md)
- [Connecting a Push Button to BeagleBone Black](https://learn.adafruit.com/connecting-a-push-button-to-beaglebone-black.md)
- [MAX31855 Thermocouple Sensor Python Library](https://learn.adafruit.com/max31855-thermocouple-python-library.md)
- [User-space SPI TFT Python Library - ILI9341](https://learn.adafruit.com/user-space-spi-tft-python-library-ili9341-2-8.md)
- [Adding a Real Time Clock to BeagleBone Black](https://learn.adafruit.com/adding-a-real-time-clock-to-beaglebone-black.md)
- [Blinking an LED with BeagleBone Black](https://learn.adafruit.com/blinking-an-led-with-beaglebone-black.md)
- [LedGames - a BeagleBone Black 64x64 LED Game](https://learn.adafruit.com/ledgames-beaglebone-black-64x64-led-game.md)
- [Setting up WiFi with BeagleBone Black](https://learn.adafruit.com/setting-up-wifi-with-beaglebone-black.md)
- [Introduction to the BeagleBone Black Device Tree](https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree.md)
- [Measuring Light with a BeagleBone Black](https://learn.adafruit.com/measuring-light-with-a-beaglebone-black.md)
- [Measuring Temperature with a BeagleBone Black](https://learn.adafruit.com/measuring-temperature-with-a-beaglebone-black.md)
- [Adafruit WebIDE](https://learn.adafruit.com/webide.md)
- [FONA Tethering to Raspberry Pi or BeagleBone Black](https://learn.adafruit.com/fona-tethering-to-raspberry-pi-or-beaglebone-black.md)
