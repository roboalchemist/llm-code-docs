# Source: https://learn.adafruit.com/beaglebone/ethernet.md

# BeagleBone

## Ethernet

This mini tutorial will show you how to connect to the Bone via the serial connection to determine the IP address, test the network connection and&nbsp;DNS. You'll need to know the COM serial port address, see the&nbsp;[Drivers](http://www.ladyada.net///drivers.html)&nbsp;tutorial on how to determine the COM and install drivers.

For this tutorial you will need:

- **[Beagle Bone](http://www.adafruit.com/products/513)**
- **[Ethernet Cable](http://www.adafruit.com/products/730)**

Pick these parts up at the Adafruit shop!

## Terminal Software
  
To connect via the USB cable, you'll need a terminal program. Built into Windows is Hyperterm. You can google around to find another good terminal program.

Connect to the Bone's COM port at 115200 baud, 8 bit, No parity, 1 stop bit, no flow control.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/300/medium800/beaglebone_com17.gif?1447975312)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/303/medium800/beaglebone_hyperterm.gif?1447975331)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/304/medium800/beaglebone_prop.gif?1447975342)

Hit return a few times, to show the login screen.![](https://cdn-learn.adafruit.com/assets/assets/000/000/305/medium800/beaglebone_angstrom-login.gif?1447975352)

Log in with the user name&nbsp; **root&nbsp;** and no password.![](https://cdn-learn.adafruit.com/assets/assets/000/000/307/medium800/beaglebone_rootlogin.gif?1447975373)

That's it you're logged in!## dmesg
  
Now we can try out the Ethernet connection. Plug a standard straight-through cable from the Bone to your Ethernet router.

Our favorite tool is&nbsp; **dmesg** &nbsp;- this will tell you all the system messages, such as what hardware was found. Type&nbsp; **dmesg** &nbsp;and hit return at the&nbsp; **root@beaglebone: ~#** &nbsp;prompt.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/309/medium800/beaglebone_dmesg1.gif?1447975395)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/311/medium800/beaglebone_dmesg2.gif?1447975416)

As you can see the last part of boot up is to bring the ethernet connection&nbsp; **eth0** &nbsp;up.## Ethernet Test
  
You can verify the ethernet connection by typing in&nbsp; **ifconfig -a**  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/313/medium800/beaglebone_ifconfig--a.gif?1447975439)

You can see under&nbsp; **inet addr:** &nbsp;the internet address of the Bone - it uses&nbsp;DHCP&nbsp;to automatically get an IP address and this is what the router gave us back. If you don't see anything, try rebooting the system by typing in&nbsp; **reboot** &nbsp;and hitting return. Make sure your Ethernet cable is well connected to both the Bone and the router.

Now you can test the outgoing connection. Type in&nbsp; **ping 18.70.0.160** &nbsp;and hit return.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/314/medium800/beaglebone_ping.gif?1447975452)

If it works, you'll see the above. You can type Control-C to cancel.

Next you can test the&nbsp;DNS&nbsp;system, by pinging&nbsp;[www.google.com](http://www.google.com/)&nbsp;, which should also succeed.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/315/medium800/beaglebone_pingdns.gif?1447975466)

- [Previous Page](https://learn.adafruit.com/beaglebone/installing-drivers.md)
- [Next Page](https://learn.adafruit.com/beaglebone/wifi.md)

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
