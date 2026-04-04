# Source: https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/using-the-camera.md

# DIY WiFi Raspberry Pi Touchscreen Camera

## Using the Camera

You briefly saw the camera interface during testing. We can explain in more detail now how it works and what options are available.  
  
Upon startup, the camera program presents a live viewfinder and a couple of buttons. The majority of the screen itself functions as the shutter “button” — tap to take a still photo.  
  
At the bottom of the screen are two buttons. The left button (with the gear icon) will take you to various settings. The right button (with the “play” symbol) lets you review previously-taken photos (if no photos have been taken yet, the camera will let you know it’s “empty”).

![](https://cdn-learn.adafruit.com/assets/assets/000/013/596/medium800/raspberry_pi_screen-basics.jpg?1389301126)

The _Settings_ menu provides access to camera settings. This is <u>not</u> an exhaustive list of every feature possible with the Raspberry Pi camera, just a few essentials to get you started.  
  
The left/right arrow buttons at the top of the screen select among the settings options:

The _Storage_ screen selects between three different options, each with some pros and cons:

- **Photos Folder:** images will be saved inside a “Photos” folder in your Raspberry Pi home directory (the folder will be created if it doesn’t exist). They can be easily accessed from other programs on the Pi, but this partition isn’t easily accessed when inserting the SD card in other computers.  
- **Boot Partition:** images will be saved in the folder “/boot/DCIM/CANON999” on the boot partition. When the SD card is inserted in another computer, it mimics a card from a digital camera and may import photos automatically, depending on system settings. The downside is that space in the boot partition is <u>very</u> limited; you might only store a dozen or so photos there.  
- **Dropbox:** as previously discussed, images are saved in the Photos folder as well as uploaded to Dropbox (if WiFi is connected and Dropbox configured).  

![raspberry_pi_scr1.png](https://cdn-learn.adafruit.com/assets/assets/000/013/597/medium640/raspberry_pi_scr1.png?1389308292)

The _Size_ screen selects from three different image sizes:

- **Large (2592x1944, 4:3 ratio):** this is the largest size (5 megapixels) supported by the Raspberry Pi camera. The actual area captured stretches well beyond what’s shown in the live viewfinder though.  
- **Medium (1920x1080, 16:9 ratio):** HD resolution, widescreen, 2 megapixels.  
- **Small (1440x1080, 4:3 ratio):** 1.5 megapixels.

The latter two modes _should_ display the actual full photo boundaries in the live viewfinder mode, but don’t yet (something in the camera library documentation doesn’t correspond to reality). This is a work in progress and will be addressed once its understood.![raspberry_pi_scr2.png](https://cdn-learn.adafruit.com/assets/assets/000/013/598/medium640/raspberry_pi_scr2.png?1389308318)

The _Effect_ screen is where all the fun happens.  
  
There are 16 different artistic effects that can be applied to photos (plus “normal,” no effect). Make your photos look like an oil painting, or a pen sketch, or turn the colors weird! These all operate on the live preview as well.

![raspberry_pi_scr3.png](https://cdn-learn.adafruit.com/assets/assets/000/013/599/medium640/raspberry_pi_scr3.png?1389308339)

The _ISO_ setting adjusts the camera’s sensitivity to light.  
  
This is a tradeoff…more sensitive settings (higher numbers) work better in low light, but the resulting image may be grainy.  
  
ISO has no effect on the live viewfinder, only captured photos.

![raspberry_pi_scr4.png](https://cdn-learn.adafruit.com/assets/assets/000/013/600/medium640/raspberry_pi_scr4.png?1389308364)

The last screen is an option to quit the camera program, returning to the command line.  
  
Tap the red button to exit, the arrow buttons for other settings, or the Done button to cancel.

![raspberry_pi_scr5.png](https://cdn-learn.adafruit.com/assets/assets/000/013/601/medium640/raspberry_pi_scr5.png?1389308384)

The “Done” button returns to viewfinder mode.  
  
All the camera settings will be saved; next time you run the script, all prior settings will be as you left them.

- [Previous Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/dropbox-setup.md)
- [Next Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/next-steps-dot-dot-dot.md)

## Featured Products

### Raspberry Pi DIY Camera Pack

[Raspberry Pi DIY Camera Pack](https://www.adafruit.com/product/3275)
If the holidays promise anything, it’s almost certainly a deluge of photographs. Instead of taking out your smartphones, why not build your own camera?

With one of Adafruit’s best selling screens and an official Raspberry Pi camera, you’ll be ready to set up your very...

Out of Stock
[Buy Now](https://www.adafruit.com/product/3275)
[Related Guides to the Product](https://learn.adafruit.com/products/3275/guides)
### PiTFT Plus Assembled 320x240 2.8" TFT + Resistive Touchscreen

[PiTFT Plus Assembled 320x240 2.8" TFT + Resistive Touchscreen](https://www.adafruit.com/product/2298)
Is this not the cutest little display for the Raspberry Pi? It features a 2.8" display with 320x240 16-bit color pixels and a resistive&nbsp;touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2298)
[Related Guides to the Product](https://learn.adafruit.com/products/2298/guides)
### PiTFT Plus 320x240 3.2" TFT + Resistive Touchscreen

[PiTFT Plus 320x240 3.2" TFT + Resistive Touchscreen](https://www.adafruit.com/product/2616)
Is this not the cutest little display for the Raspberry Pi? It features a 3.2" display with 320x240 16-bit color pixels and a resistive&nbsp;touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2616)
[Related Guides to the Product](https://learn.adafruit.com/products/2616/guides)
### Adafruit PiTFT 2.4" HAT Mini Kit - 320x240 TFT Touchscreen

[Adafruit PiTFT 2.4" HAT Mini Kit - 320x240 TFT Touchscreen](https://www.adafruit.com/product/2455)
Is this not the cutest little display for the Raspberry Pi? It features a 2.4" display with 320x240 16-bit color pixels and a resistive touch overlay. The HAT uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or video...

Out of Stock
[Buy Now](https://www.adafruit.com/product/2455)
[Related Guides to the Product](https://learn.adafruit.com/products/2455/guides)
### Adafruit PiTFT - 320x240 2.8" TFT+Touchscreen for Raspberry Pi

[Adafruit PiTFT - 320x240 2.8" TFT+Touchscreen for Raspberry Pi](https://www.adafruit.com/product/1601)
Is this not the cutest little display for the Raspberry Pi? It features a 2.8" display with 320x240 16-bit color pixels and a resistive touch overlay. The plate uses the high speed SPI interface on the Pi and can use the mini display as a console, X window port, displaying images or video...

Out of Stock
[Buy Now](https://www.adafruit.com/product/1601)
[Related Guides to the Product](https://learn.adafruit.com/products/1601/guides)
### Raspberry Pi 3 - Model B - ARMv8 with 1G RAM

[Raspberry Pi 3 - Model B - ARMv8 with 1G RAM](https://www.adafruit.com/product/3055)
Did you really think the Raspberry Pi would stop getting better? At this point, we sound like a broken record, extolling on the new Pi’s myriad improvements like we’re surprised that the folks at the Raspberry Pi Foundation are continuously making their flagship board better.&nbsp;...

In Stock
[Buy Now](https://www.adafruit.com/product/3055)
[Related Guides to the Product](https://learn.adafruit.com/products/3055/guides)
### Raspberry Pi 2 - Model B v1.2 - ARM Cortex-A53 with 1G RAM

[Raspberry Pi 2 - Model B v1.2 - ARM Cortex-A53 with 1G RAM](https://www.adafruit.com/product/2358)
Didn't think the Raspberry Pi could get any better? You're in for a big surprise! The Raspberry Pi 2 Model B is out and it's amazing! With an upgraded ARM Cortex-A53&nbsp;quad-core processor, Dual Core VideoCore IV Multimedia coprocessor, and a full Gigabyte of RAM, this...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2358)
[Related Guides to the Product](https://learn.adafruit.com/products/2358/guides)
### Raspberry Pi Model A+ 512MB RAM

[Raspberry Pi Model A+ 512MB RAM](https://www.adafruit.com/product/2266)
 **Note:** As of August 10th, 2016 the Raspberry Pi A+ now includes 512 MB of RAM!

The Raspberry Pi Model A+ is the perfect board for the minimalist Pi fan. This low-cost Pi uses the same processor as the model B+, but does away with the Ethernet jack and three of the USB...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2266)
[Related Guides to the Product](https://learn.adafruit.com/products/2266/guides)

## Related Guides

- [Kali Linux on the Raspberry Pi with the PiTFT](https://learn.adafruit.com/kali-linux-on-the-raspberry-pi-with-the-pitft.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
- [Processing on the Raspberry Pi & PiTFT](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft.md)
- [PiGRRL 2](https://learn.adafruit.com/pigrrl-2.md)
- [RasPipe: A Raspberry Pi Pipeline Viewer, Part 2](https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer-part-2.md)
- [Monitor PiCam and temperature on a PiTFT via adafruit.io](https://learn.adafruit.com/monitor-picam-and-temperature-on-a-pitft-via-adafruit-dot-io.md)
- [AstroPrint 3D Printing](https://learn.adafruit.com/astroprint-3d-printing.md)
- [Touchscreen Pi Timelapse Controller](https://learn.adafruit.com/touchscreen-pi-timelapse-controller.md)
- [Using the Slamtec RPLIDAR on a Raspberry Pi](https://learn.adafruit.com/slamtec-rplidar-on-pi.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Pi Hole Ad Detection Display with PiTFT](https://learn.adafruit.com/pi-hole-ad-pitft-tft-detection-display.md)
- [SnapPiCam Raspberry Pi Camera](https://learn.adafruit.com/snappicam-raspberry-pi-camera.md)
- [JOY of Arcada — USB Game Pad for Adafruit PyGamer and PyBadge](https://learn.adafruit.com/joy-of-arcada-usb-game-pad-for-adafruit-pygamer-pybadge.md)
- [Go Fishing with Rotary Encoders](https://learn.adafruit.com/gone-fishing-game.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
