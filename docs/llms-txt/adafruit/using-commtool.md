# Source: https://learn.adafruit.com/ttl-serial-camera/using-commtool.md

# TTL Serial Camera

## Using CommTool

To use the Comm Tool, a windows utility, we need to set up a serial link to the camera. There's two ways we suggest doing this. One is to use something like an FTDI friend or other USB/TTL serial converter. If you have an Arduino you can 'hijack' the serial chip (FTDI chip or similar) by uploading a blank sketch to the Arduino:

```
// empty sketch
 
void setup()  
{
}
 
void loop()
{
}
```

Danger: 

If you're using a Leonardo, Micro, Yun, or other ATmega32U4-based controller, use this Leo\_passthru sketch instead of the "blank" sketch.

```
//Leo_passthru
// Allows Leonardo to pass serial data between 
// fingerprint reader and Windows.
//
// Red connects to +5V
// Black connects to Ground
// Green goes to Digital 0
// White goes to Digital 1

void setup() {
  Serial1.begin(57600);
  Serial.begin(57600);
}

void loop() 
{  
  while (Serial.available())
    Serial1.write(Serial.read());
  while (Serial1.available())
    Serial.write(Serial1.read());
}
```

Now, wire it up as follows:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/206/medium800/camera_commhijack.jpeg?1396761182)

Danger: 

Note the 10K resistor divider, the camera's serial data pins are 3.3v logic and its a good idea to divide the 5V down so that its 2.5V. Normally the ouput from the digital 0 pin is 5V high, the way we connected the resistors is so the camera input (white wire) never goes above 3.3V  
  
Now download and install the VC0706 CommTool software (see below in the Download section)  
  
Start up the software and select the COM port that the Arduino is on.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/207/medium800/camera_commport.gif?1447974961)

Then **Open** the port and click **Get Version**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/208/medium800/camera_commversion.gif?1447974972)

Note it says VC0703 - we don't know precisely why the DSP is programmed with a different number - its one of those mysteries! Still, you should get a response  
  
&nbsp;The next button you should press is near the bottom **FBUF CTRL**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/209/medium800/camera_fbuf.gif?1447974982)

This is quite a panel, but we can use this to get images directly from the camera which is good for debugging.

- Point the camera at something you want to take a photo of
- Click&nbsp; **Stop FBuf** &nbsp;to freeze the frame buffer
- Click&nbsp; **Sel File** &nbsp;to select the file to save the&nbsp;JPG&nbsp;as

![](https://cdn-learn.adafruit.com/assets/assets/000/000/210/medium800/camera_savefile.gif?1447974991)

Next press&nbsp; **Read** &nbsp;(next to&nbsp; **Sel Fil**** e**) to read the jpeg image off the camera![](https://cdn-learn.adafruit.com/assets/assets/000/000/211/medium800/camera_commimageread.gif?1447975003)

Thats it! You can now easily test reading camera images. To take another photo. Press **Resume** up at the top to have the video start up again. Then click **Stop CFbuf** when you want to snap another photo. Finally you can select the **Compression Ratio** which will improve or degrade the image quality but also change the image transfer time. There's no way to change the image size from this program (easily) but we can do it using the Arduino sketch so just try it out here to start.  
  
You might notice there's a dropdown for changing the baud rate. By default the baudrate is 38400 baud.

## **Despite the software letting you change the baud rate this is a very flaky setting and even if it works, when you power up the camera again it will reset. Some experimenters have accidentally disabled their cameras by trying to change the baud rate. We do not suggest you mess with the baud rate settings. If you do, you may permanently disable your camera and we will not replace it!**

## 
![](https://cdn-learn.adafruit.com/assets/assets/000/000/212/medium800/camera_commconfig.gif?1447975015)

The only other thing we suggest checking out is the **Image Property** button, which will let you adjust settings for the camera, we bumped up our saturation a bit to get better images. Dragging the sliders will make the video output change immediately so this is a handy place to get a TV connected up so you can check out how it works

![](https://cdn-learn.adafruit.com/assets/assets/000/000/213/medium800/camera_commimage.gif?1447975025)

There are many options for this software, here's what we think of the other buttons. Personally, we don't suggest going in to any of them unless you really need to.

- **Config - see above**
- **Get Version - see above**
- **R/W**** &nbsp;Data**&nbsp;- this is for writing raw data to the DSP chip processor. Don't do this unless you're sure you know what you're doing since it will mess with the camera's ability. Even we don't know what it would be good for
- **Color Ctrl -** &nbsp;this is for selecting Color or Black&White or Auto select (probably based on lighting conditions). You probably want to keep it at Auto
- **Mirror Ctrl** &nbsp;- we think this is so you can flip the display (if its bouncing off a mirror)
- **Power Ctrl&nbsp;** - this is for testing the power down mode, and it seems like you might be able to have it auto-power down when there's no motion.
- **Timer Ctrl** &nbsp;- there is an RTC built into the DSP which you can set, however there's no battery backup so if power is lost the RTC will be reset so we don't think its terribly useful
- **AE**** &nbsp;Ctrl**&nbsp;- this is for controlling the auto-contrast/brightness. By default its set to auto-select for indoor or outdoor use. Probably best to leave it as is
- **Motion Ctrl** &nbsp;- this is for the motion detection system. You can tweak the settings and also test it. We have an Arduino sketch for interacting with the motion detection system. By default it works pretty good but you can super tweak it out if you want to.
- **OSD Config -&nbsp;** The protocol sheet and this seem to imply you can do on-screen-display but after much time spent on it, we determined its not activated somewhere in the DSP. We've never seen a VC0706 camera that could do it. :(
- **Image property - see above**
- **Gamma -&nbsp;** this is for more precise gamma control of the CMOS sensor. It seems to be preset to be OK but you can mess with this if you'd like
- **SPI Flash** &nbsp;- for reading/writing to the SPI storage? Not sure if its a good idea to mess with this
- **Other Ctrl&nbsp;** - for playing with the DAC? No idea what this is for.
- **Up/Down Load** &nbsp;- this is for reading and writing to the flash probably to upload new DSP code. We dont suggest messing with this
- **System Reset -&nbsp;** does a reset of the module. Press this if its not responding
- **FBuff Ctrl - see above**
- **Zoom Ctrl -&nbsp;** The module has built in 'Pan Tilt Zoom' ability BUT its for video only and wont affect photos snapped. You can play with the PTZ here, its pretty basic but could be useful for someone

- [Previous Page](https://learn.adafruit.com/ttl-serial-camera/testing-the-camera.md)
- [Next Page](https://learn.adafruit.com/ttl-serial-camera/arduino-usage.md)

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
