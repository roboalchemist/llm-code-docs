# Source: https://learn.adafruit.com/digital-led-belt/upload-the-test-sketch.md

# Digital LED Belt

## Upload the Test Sketch

Now its time to get BLINKY!  
  
We'll have to install a version of the Arduino IDE called Teensyduino and our LED strip library, so we can program the controller chip.  
  
**[If you're running Windows, you can just download this ready-to-go zip package. Uncompress it and inside will be an Arduino IDE](http://learn.adafruit.com/system/assets/assets/000/010/149/original/teensyduinov21b.zip "Link: http://learn.adafruit.com/system/assets/assets/000/010/149/original/teensyduinov21b.zip")**  
  
**[If you're running Mac OS X, you can just download this ready-to-go dmg package. Uncompress it and inside will be an Arduino IDE](http://learn.adafruit.com/system/assets/assets/000/010/150/original/teensyduino_v21.dmg "Link: http://learn.adafruit.com/system/assets/assets/000/010/150/original/teensyduino\_v21.dmg")**  
  
Download and install whichever matches your setup. Uncompress it onto your desktop or where ever you want to store the IDE folder. This will take a while so we'll wait here for you.  
  
OK welcome back! Now you will install the 'library' for the Digital LED strip.

Open up the Arduino library manager:

![](https://cdn-learn.adafruit.com/assets/assets/000/084/214/medium800/led_strips_library_manager_menu.png?1573774757)

Search for the&nbsp; **LPD8806** library and install it

![](https://cdn-learn.adafruit.com/assets/assets/000/084/215/medium800/led_strips_lpd8806.png?1573774780)

We also have a great tutorial on Arduino library installation at:  
[http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use](http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use "Link: http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use")

You should now see a new **example** folder called **LPD8806** and inside, an example called **LEDbeltKit**. Open up the LEDbeltKit example.  
  
Be sure to select **Atmega32u4 breakout** in the **Board** menu. Also select the Serial Port that is made when you plug in the Atmega32u4 board to USB.

![](https://cdn-learn.adafruit.com/assets/assets/000/003/334/medium800/led_strips_selectatmega32u4.gif?1448059470)

![](https://cdn-learn.adafruit.com/assets/assets/000/003/335/medium800/led_strips_leocom.gif?1448059465)

To upload the LEDbeltKit sketch, simply have the board plugged in, click the Upload button in the IDE and press the **RESET** button on the breakout board.

Danger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/003/336/medium800/led_strips_leoupload.gif?1448059460)

Once you've uploaded you should see the LED belt perform the blinky test! It will look a little similar to this:http://www.flickr.com/photos/adafruit/5387932657/

- [Previous Page](https://learn.adafruit.com/digital-led-belt/connect-the-led-strip.md)
- [Next Page](https://learn.adafruit.com/digital-led-belt/battery-protection-diode.md)

## Featured Products

### Digital programmable LED belt kit

[Digital programmable LED belt kit](https://www.adafruit.com/product/332)
By popular demand, we now have a project tutorial for how to make your own programmable, ultra-blinky LED belt. Perfect for parties, raves, parades, weddings, funerals, and bar mitzvahs. Wear it with pride, wear it with blinky! Follow our soldering tutorial to build your own heirloom LED belt,...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/332)
[Related Guides to the Product](https://learn.adafruit.com/products/332/guides)

## Related Guides

- [LED Sequin Bow Tie](https://learn.adafruit.com/led-sequin-bowtie.md)
- [Bluetooth-Controlled NeoPixel Goggles](https://learn.adafruit.com/bluetooth-neopixel-goggles.md)
- [Light Painting with Raspberry Pi](https://learn.adafruit.com/light-painting-with-raspberry-pi.md)
- [Glowing Viking Rune wayFinder](https://learn.adafruit.com/glowing-viking-rune-artifact.md)
- [3D Printing with Bamboo Wood Filament](https://learn.adafruit.com/3d-printing-with-bamboo-wood-filament.md)
- [Jellyfish Umbrella with easy WLED WiFi Control](https://learn.adafruit.com/jellyfish-umbrella-with-easy-wled-wifi-control.md)
- [Bandolier of Light](https://learn.adafruit.com/bandolier-of-light.md)
- [Electron Bow](https://learn.adafruit.com/electron-bow.md)
- [Steven Universe Cosplay Shirt & Gem](https://learn.adafruit.com/steven-universe-cosplay-shirt-gem.md)
- [CLUE Vertical Garden Weather Visualizer](https://learn.adafruit.com/clue-vertical-garden-weather-visualizer.md)
- [Cast a 3d Printed Necklace in Metal](https://learn.adafruit.com/cast-a-3d-printed-necklace-in-metal.md)
- [3D Printed Wearable Video Goggles](https://learn.adafruit.com/3d-printed-wearable-video-goggles.md)
- [Bunny Ears with MakeCode](https://learn.adafruit.com/bunny-ears-with-makecode.md)
- [Roll-up Video Light](https://learn.adafruit.com/roll-up-video-light.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
