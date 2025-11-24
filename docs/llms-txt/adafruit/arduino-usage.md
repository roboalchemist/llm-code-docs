# Source: https://learn.adafruit.com/ttl-serial-camera/arduino-usage.md

# TTL Serial Camera

## Arduino Usage

Next up, we will wire the camera to our microcontroller (in this case an Arduino). This is pretty similar to the above except we will be using two digital pins and a software serial port to talk to the camera. To save images, you'll need some sort of external storage like our [microSD breakout board](https://www.adafruit.com/products/254).  
  
Connect up the camera like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/214/medium800/cameraduino.jpeg?1396761262)

Danger: 

We suggest testing the microSD card first. Check out our microSD breakout board tutorial and verify that you can read from the card by listing the files. Once you have verified the microSD card wiring, you can come back here and install the VC0706 camera library.  
  
[Visit the Github repository here.](https://github.com/adafruit/Adafruit-VC0706-Serial-Camera-Library) To download. click the DOWNLOADS button in the top right corner, rename the uncompressed folder Adafruit\_VC0706. Check that the Adafruit\_VC0706 folder contains Adafruit\_VC0706.cpp and Adafruit\_VC0706.h Place the Adafruit\_VC0706 library folder your _arduinosketchfolder_/libraries/ folder. You may need to create the libraries subfolder if its your first library. Restart the IDE.  
  
If you're using Arduino v23 or earlier, you'll also need to install the NewSoftSerial library. [Download it by clicking this link](http://arduiniana.org/NewSoftSerial/NewSoftSerial10c.zip) and install it as you did the Adafruit\_VC0706 library. Arduino 1.0 has this built in now (called SoftwareSerial)

## Taking a Snapshot
OK now you're finally ready to run the snapshot demo. Open up the Arduino IDE and select&nbsp; **File-\> Examples-\> Adafruit\_VC0706-\> Snapshot&nbsp;** sketch and upload it to the Arduino. Open up the serial monitor and you can see the sketch will take a 640x480 photo and save it to the microSD card. You can then pop the card into your computer to see the&nbsp;JPG&nbsp;file  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/215/medium800/camera_snapshot.gif?1447975036)

There are a few things you can change once you get it working. One is changing the pins the camera uses. You can use any two digital pins, change this line:

```
// This is the camera pin connection. Connect the camera TX
// to pin 2, camera RX to pin 3
NewSoftSerial cameraconnection = NewSoftSerial(2, 3);
```

You can also change the snapshot image dimension to 160x120, 320x240 or 640x480 by changing these lines:```
// Set the picture size - you can choose one of 640x480, 320x240 or 160x120 
  // Remember that bigger pictures take longer to transmit!
 
  cam.setImageSize(VC0706_640x480);        // biggest
  //cam.setImageSize(VC0706_320x240);        // medium
  //cam.setImageSize(VC0706_160x120);          // small
```

Simply uncomment the size you want, and comment out the others. Bigger pictures will take longer to snap, so you will want to think about how fast you need to grab data and save it to the disk## Detecting Motion
A neat thing that the camera has built in is motion detection. It will look for motion in the video stream and alert the microcontroller (by sending a serial data packet) when motion is detected. IN this way you can save a bit of cash and skip on having a PIR sensor (although a PIR sensor will be better at detecting warm mammalian things).  
  
Load up the **File-\> Examples-\> Adafruit\_VC0706-\> MotionDetect** sketch and upload it to the Arduino. It will take a photo immediately because it just turned on. Then wait a few minutes and wave you hand in front of the camera, it will take another photo.![](https://cdn-learn.adafruit.com/assets/assets/000/000/216/medium800/camera_motiondetect.gif?1447975046)

You can turn motion detection on or off by calling&nbsp;**setMotionDetect()**```
//  Motion detection system can alert you when the camera 'sees' motion!
  cam.setMotionDetect(true);           // turn it on
  //cam.setMotionDetect(false);        // turn it off   (default)
```

You'll need to 'poll' the camera to ask it when motion is detected, by calling&nbsp;**motionDetected()**- it will return true if motion was recently detected, and false otherwise.## Adjusting the Manual Focus
One last thing, the camera modules use a manual focus system - there's no auto focus. This can be good or bad. The camera comes with a far depth of focus which is good for most stuff. If you want to change the focus, we strongly recommend plugging it into a video monitor as shown above so you can see exactly how the camera focus looks. You can then lock the focus with the set screw![](https://cdn-learn.adafruit.com/assets/assets/000/000/217/medium800/camera_focus.jpeg?1396761289)

The version in the weatherproof housing is a little tougher to adjust but it can&nbsp; be done by unscrewing the housing (it takes a few steps but its all easy to do) and then adjusting the focus before reassembly

- [Previous Page](https://learn.adafruit.com/ttl-serial-camera/using-commtool.md)
- [Next Page](https://learn.adafruit.com/ttl-serial-camera/circuitpython-python-usage.md)

## Featured Products

### TTL Serial JPEG Camera with NTSC Video

[TTL Serial JPEG Camera with NTSC Video](https://www.adafruit.com/product/397)
This camera module can be a pretty neat project addition. It was designed to be used in security systems and does two main things - it outputs NTSC video and can take snapshots of that video (in color) and transmit them over the TTL serial link. You can snap pictures at 640x480, 320x240 or...

In Stock
[Buy Now](https://www.adafruit.com/product/397)
[Related Guides to the Product](https://learn.adafruit.com/products/397/guides)
### Miniature TTL Serial JPEG Camera with NTSC Video

[Miniature TTL Serial JPEG Camera with NTSC Video](https://www.adafruit.com/product/1386)
This tiny little camera module can be a pretty neat project addition, it is just like [our other JPEG cameras (same chipset/software)](http://www.adafruit.com/category/35_68), but much smaller and slimmer. It was designed to be used in security systems and does two main things - it...

In Stock
[Buy Now](https://www.adafruit.com/product/1386)
[Related Guides to the Product](https://learn.adafruit.com/products/1386/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Weatherproof TTL Serial JPEG Camera with NTSC Video and IR LEDs

[Weatherproof TTL Serial JPEG Camera with NTSC Video and IR LEDs](https://www.adafruit.com/product/613)
This weatherproof camera module is [a classy upgrade to the basic camera module we already stock in the shop](http://www.adafruit.com/products/397). The main differences is that this one comes in a nice metal case with a mounting hinge, a 1 meter long cable with the TTL & NTSC...

In Stock
[Buy Now](https://www.adafruit.com/product/613)
[Related Guides to the Product](https://learn.adafruit.com/products/613/guides)
### MicroSD card breakout board+

[MicroSD card breakout board+](https://www.adafruit.com/product/254)
Not just a simple breakout board, this microSD adapter goes the extra mile - designed for ease of use.

- Onboard 5v-\>3v regulator provides 150mA for power-hungry cards
- 3v level shifting means you can use this with ease on either 3v or 5v systems
- Uses a proper level...

In Stock
[Buy Now](https://www.adafruit.com/product/254)
[Related Guides to the Product](https://learn.adafruit.com/products/254/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### SD/MicroSD Memory Card (8 GB SDHC)

[SD/MicroSD Memory Card (8 GB SDHC)](https://www.adafruit.com/product/1294)
Add mega-storage in a jiffy using this 8 GB class 4 micro-SD card. It comes with a SD adapter so you can use it with any of our shields or adapters. Preformatted to FAT so it works out of the box with our projects. Tested and works great with our <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1294)
[Related Guides to the Product](https://learn.adafruit.com/products/1294/guides)

## Related Guides

- [Program an AVR or Arduino Using Raspberry Pi GPIO](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [Digital Circuits 7: MCUs... how do they work?](https://learn.adafruit.com/mcus-how-do-they-work.md)
- [Skill Badge Requirements: Microcontrollers](https://learn.adafruit.com/skill-badge-requirements-microcontrollers.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Adafruit OV5640 Camera Breakouts](https://learn.adafruit.com/adafruit-ov5640-camera-breakout.md)
- [Adalight Project Pack](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting.md)
- [Trellis 3D Printed Enclosure](https://learn.adafruit.com/trellis-3d-printed-enclosure.md)
- [Arduino Lesson 0. Getting Started](https://learn.adafruit.com/lesson-0-getting-started.md)
- [Cloud Thermometer](https://learn.adafruit.com/cloud-thermometer.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [0.96" mini Color OLED](https://learn.adafruit.com/096-mini-color-oled.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
