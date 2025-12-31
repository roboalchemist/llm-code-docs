# Source: https://learn.adafruit.com/beaglebone/installing-drivers.md

# BeagleBone

## Installing Drivers

This section will detail how to install drivers for the USB/Serial connection (and the other USB devices) from the Bone onto your Windows computer. We'll try to have more documentation on using the Bone with a Mac & Linux at some point but since so many people use Windows and its tougher to install the drives on Win than other&nbsp;OS's we'll start here!

For this tutorial you will need:

- **[Beagle Bone](http://www.adafruit.com/products/513)**

Pick these parts up at the Adafruit shop!

## Download & Install

First, we'll install the Windows driver package.[&nbsp;Download this link to BONE\_DRV.exe](http://beagleboard.org/static/beaglebone/latest/Drivers/Windows/BONE_DRV.exe)&nbsp;and double click it.  
  
When prompted/warned about the software, click&nbsp; **Continue Anyways** &nbsp;- you'll need to do it 3 times - once for each driver.
![](https://cdn-learn.adafruit.com/assets/assets/000/000/279/medium800/beaglebone_bone1.png?1396761749)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/281/medium800/beaglebone_bone2.png?1396761782)

## Connect!
Start by opening up your Bone packaging, and finding the MiniB USB cable  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/282/medium800/beagleboneexrtas.jpeg?1396761787)

Plug the miniB side into the Bone, and the A side into your Windows computer. You'll see a popup saying the computer found a USB serial converter.![](https://cdn-learn.adafruit.com/assets/assets/000/000/284/medium800/beaglebone_found-xds100v2.png?1396761809)

And then an install popup. Click&nbsp; **Install the software automatically** &nbsp;and&nbsp; **Next.** ![](https://cdn-learn.adafruit.com/assets/assets/000/000/286/medium800/beaglebone_install-xds100v.png?1396761836)

Click&nbsp; **Continue Anyway** &nbsp;when it warns you.![](https://cdn-learn.adafruit.com/assets/assets/000/000/287/medium800/beaglebone_xds-continue.png?1396761852)

You should finish successfully.![](https://cdn-learn.adafruit.com/assets/assets/000/000/289/medium800/beaglebone_xds100v1.png?1396761877)

Next you'll go through the same process for the Disk Drive and Beaglebone devices.![](https://cdn-learn.adafruit.com/assets/assets/000/000/290/medium800/beaglebone_found-disk-drive.png?1396761895)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/292/medium800/beaglebone_found-new-hardware-bone.png?1396761921)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/293/medium800/beaglebone_usbserialport-popup.png?1396761935)

Follow the same instructions, installing&nbsp; **Automatically** &nbsp;and clicking&nbsp; **Continue Anyways.**

Finally, you will have the new USB serial port. Go to the Device Manager on your computer to find the name of the COM port. In my case its&nbsp; **COM17.**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/295/medium800/beaglebone_device-manager.png?1396761967)

That's it, you've installed the drivers! Next up we'll connect via serial and log in.- [Previous Page](https://learn.adafruit.com/beaglebone/overview.md)
- [Next Page](https://learn.adafruit.com/beaglebone/ethernet.md)

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
