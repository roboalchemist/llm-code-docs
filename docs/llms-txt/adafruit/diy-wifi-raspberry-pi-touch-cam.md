# Source: https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam.md

# DIY WiFi Raspberry Pi Touchscreen Camera

## Overview

http://www.youtube.com/watch?v=MRrELkIHgbU

This project explores the Adafruit PiTFT touchscreen and the Raspberry Pi camera board to create a simple point-and-shoot digital camera. One can optionally use WiFi and Dropbox (a cloud file storage and synchronization service) to automatically transfer photos to another computer for editing.

![](https://cdn-learn.adafruit.com/assets/assets/000/013/602/medium800/raspberry_pi_pi-cam.jpg?1389311971)

![](https://cdn-learn.adafruit.com/assets/assets/000/014/264/medium800/raspberry_pi_hero.jpg?1392317999)

This isn’t likely to replace your digital camera (or even phone-cam) anytime soon…it’s a learning exercise and not a polished consumer item…but as the code is open source, you or others might _customize it_ into something special that your regular camera can’t do.

## Things You’ll Need:

- **Raspberry Pi computer** , _any_ model will work. This project is not&nbsp;especially demanding, so it’s a great use for an older board if you have one around.
- **PiTFT display w/resistive touch.** Various sizes and models are available — for current Raspberry Pi boards (Pi 3, Pi 2, B+ and A+) you’ll want one of the _PiTFT Plus_ variants. For older Pi boards (original Model B or A), a “non-Plus” PiTFT is needed. See featured product links to the right. It _must_ be a PiTFT (connecting to the GPIO header, **not composite&nbsp;or HDMI** ) with **320x240** resolution (no higher, i.e. 3.5" PiTFT won’t work), _must_ have **resistive touch** , _not_ capacitive.
- **Raspberry Pi Camera Board.** &nbsp;Current “v2” cameras or original v1, any will do. For general work you’ll want the **[regular version](https://www.adafruit.com/products/3099)**. For special projects like security or nighttime nature photography, you can experiment with the **[infrared version](http://www.adafruit.com/products/1567 "https://www.adafruit.com/products/3100").**
- **[MicroSD memory card](https://www.adafruit.com/products/1294),** 4GB or larger.
- **HDMI monitor** and **USB keyboard** are needed temporarily during setup. Once everything is configured and working, these are no longer required.

The following parts are **optional:**

- A **[WiFi adapter](http://www.adafruit.com/products/814 "Link: http://www.adafruit.com/products/814")** allows the camera to upload photos to Dropbox (requires account, free). _The Raspberry Pi **3** has WiFi **built in** , so this part isn’t needed with that board._
- A **[USB battery pack](http://www.adafruit.com/products/1565 "Link: http://www.adafruit.com/products/1565")** makes the whole camera portable. If using WiFi, you’ll want a robust battery pack that can provide 1 Amp (some are limited to 500 mA max).

**Some additional parts, tools and skills are also required:** &nbsp;optional buttons or headers on&nbsp;PiTFT displays sometimes require soldering; some means of holding all the pieces together — could be as simple as a few rubber bands, to a drilled-out plastic electronics enclosure, to an elaborate custom 3D-printed case. This all depends on your available resources. Read through to see what’s involved in the project and come up with ideas along the way.

 **Other Raspberry Pi – Point & Shoot Cameras!**  
James Wolf made a Raspberry Pi - Point & Shoot Camera all inside the original Pi case (except battery). He made a little board attached to a cut down ribbon cable, just for the pull up resistors and the button - instructions, pictures and a link to the simple Python file are&nbsp;[located on his site](http://contractorwolf.wordpress.com/raspberry-pi-point-shoot-camera/).

http://www.youtube.com/watch?v=Jfca32qkgY8

- [Next Page](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/pi-setup.md)

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
