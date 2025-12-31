# Source: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/download-and-install.md

# Adalight Project Pack

## Download & Install

We’ll install the software next, because it’s easier to test and troubleshoot the electronics on your desk than behind the telly!  
  
Three packages need to be downloaded:

## Download Arduino IDE
First, download the Arduino IDE (integrated development environment)&nbsp;[from the Arduino web site](http://arduino.cc/en/Main/Software). Select the version of the software for your computer type: Windows, Mac or Linux. Read the&nbsp;[Getting Started page](http://arduino.cc/en/Guide/HomePage)&nbsp;for an explanation of how to install the software on your computer. It’s a little different for each of the three operating systems. ## Download Processing IDE
Next, download the Processing IDE&nbsp;[from the Processing web site](http://processing.org/download/). The first section of the&nbsp;[Getting Started page](http://processing.org/learning/gettingstarted/)&nbsp;explains how to install the software.  
Danger: 

Warning: 

## Download Adalight ZIP
Finally, [visit the Adalight page on Github](https://github.com/adafruit/Adalight) and download the ZIP file. The download button is near the upper left of the page:  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/489/medium800/led_pixels_zip-button.jpg?1396773301)

After uncompressing the ZIP file, you’ll need to move some files into place.  
  
If you’ve run the Arduino and/or Processing IDEs before, there will be corresponding “Arduino” and “Processing” folders inside your personal “Documents” folder (or “My Documents” in Windows).&nbsp;In that case, move the&nbsp;<u>contents</u> of the Arduino and Processing folders from the Adalight ZIP file into the corresponding document folders.  
  
If the Arduino and Processing folders don’t yet exist on your system, you can just copy these from the Adalight ZIP file to your Documents folder.  
  
The other files and folders in the ZIP file can be ignored. These are for advanced users and aren’t essential to its use.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/518/medium800/led_pixels_file-locations.png?1396773632)

 **DO NOT** &nbsp;use the “LEDstream\_LPD8806” sketch/folder unless you are specifically using LPD8806 LED strips in a custom build. Use&nbsp;just the plain “ **LEDstream** ” folder when building the Adalight Project Pack, or for a DIY setup using similar&nbsp;WS2801 LEDs.

Danger: 

## Program the Arduino
The Arduino IDE must be installed before this step.  
  
Connect the Arduino board to your computer with a USB A-to-B cable. When connected&nbsp;for the first time, Windows users will prompted to install a driver.&nbsp;This is explained in the Arduino [Getting Started guide for Windows](http://arduino.cc/en/Guide/Windows). No driver is required for Mac or Linux.  
  
Launch the Arduino IDE. After a moment, you should see a simple blue and white window with some buttons.  
  
From the **File** menu, select **Sketchbook** , which should “roll over” to show **LEDstream**. Select this.  
  
From the **Tools** menu, select **Board** , then **Arduino Uno** (or whatever Arduino board type you’re using).  
  
From the **Tools** menu again, select **Serial Port** , and then the port corresponding to your Arduino board.  
  
Click the **Upload** button near the top-left of the window:![](https://cdn-learn.adafruit.com/assets/assets/000/001/526/medium800/led_pixels_upload.png?1396773720)

After the code is uploaded, if the LEDs are correctly wired up and the power supply is plugged in, the LEDs should all flash red, green, then blue for about a second each, then off. This is a startup diagnostic that tells you the LEDs and Arduino are working correctly, and are now awaiting data from the computer…  
  
Because the Arduino stores the program in non-volatile memory, you should only need to do this upload process once, not every time you want to use Adalight.

Danger: 

- [Previous Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/wiring-1.md)
- [Next Page](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/running-the-software.md)

## Featured Products

### Adalight - DIY Ambient Monitor Lighting Project Pack

[Adalight - DIY Ambient Monitor Lighting Project Pack](https://www.adafruit.com/product/461)
Build your own ambient-light addition for a monitor or media PC television with the Adalight project pack! This project pack is for our ["Adalight" project tutorial](http://learn.adafruit.com/adalight-diy-ambient-tv-lighting). By running the Processing code on your...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/461)
[Related Guides to the Product](https://learn.adafruit.com/products/461/guides)
### 12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Thin Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/322)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/322)
[Related Guides to the Product](https://learn.adafruit.com/products/322/guides)
### 12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)

[12mm  Diffused Flat Digital RGB LED Pixels (Strand of 25)](https://www.adafruit.com/product/738)
RGB Pixels are digitally-controllable lights you can set to any color, or animate. Each RGB LED and controller chip is molded into a 'dot' of silicone. The dots are weatherproof and rugged. There are four flanges molded in so that you can 'push' them into a 12mm drill hole in...

In Stock
[Buy Now](https://www.adafruit.com/product/738)
[Related Guides to the Product](https://learn.adafruit.com/products/738/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [Arduino Tips, Tricks, and Techniques](https://learn.adafruit.com/arduino-tips-tricks-and-techniques.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [Wireless Power Switch with Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/wireless-power-switch-with-arduino-and-the-cc3000-wifi-chip.md)
- [Arduino Lesson 12. LCD Displays - Part 2](https://learn.adafruit.com/adafruit-arduino-lesson-12-lcd-displays-part-2.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [Adafruit Ultimate GPS Logger Shield](https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Wireless Gardening with Arduino + CC3000 WiFi Modules](https://learn.adafruit.com/wireless-gardening-arduino-cc3000-wifi-modules.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [A REST API for Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/a-rest-api-for-arduino-and-the-cc3000-wifi-chip.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [How to program a Zumo Robot with Simulink](https://learn.adafruit.com/zumo-robot-control-with-simulink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
