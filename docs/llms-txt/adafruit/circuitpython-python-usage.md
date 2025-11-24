# Source: https://learn.adafruit.com/ttl-serial-camera/circuitpython-python-usage.md

# TTL Serial Camera

## CircuitPython & Python Usage

In addition to taking pictures with the camera in Arduino, you can also use Python and CircuitPython to snap photos and save them to a SD card, computer or Raspberry Pi!&nbsp; The [Adafruit CircuitPython VC0706](https://github.com/adafruit/Adafruit_CircuitPython_VC0706) library is your key to accessing the TTL camera and grabbing images over a serial connection.

You can use this camera with any CircuitPython microcontroller board or with a computer that has GPIO and Python [thanks to Adafruit\_Blinka, our CircuitPython-for-Python compatibility library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

# CircuitPython Microcontroller Wiring
First you'll need to connect the TTL camera and a micro SD card holder to your CircuitPython board.&nbsp; The easiest and recommended option is to use a Feather M0 Adalogger board loaded with CircuitPython. This gives you a micro SD card holder that's pre-wired and ready to go, just connect the camera to the board.&nbsp; Here's an example of connecting the camera to a Feather M0 Adalogger:

Just like connecting the camera to an Arduino you need to connect these wires:

- **Camera 5V** to **board USB or 5V power** (note this means you must have the board plugged into a USB / 5V power supply to properly power the camera).
- **Camera GND** to **board GND**.
- **Camera RX** to **board TX**.
- **Camera TX** to **board RX**.

In addition, please make sure a micro SD card formatted with the FAT32 filesystem (highly recommended to [use the official SD card formatter here](https://www.sdcard.org/downloads/formatter_4/) and not your operating system's formatter!) is inserted in the SD card holder.

![m0_adalogger_ttl_camera_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/047/939/medium640/m0_adalogger_ttl_camera_bb.png?1572540204)

# Python Computer Wiring

Since there's _dozens_ of Linux computers/boards you can use, we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

Here you have two options: An external USB-to-serial converter, or the built-in UART on the Pi's TX/RX pins. Here's an example of wiring up the [USB-to-serial converter](https://www.adafruit.com/product/954):

- **Camera Vin** &nbsp; to **USB**  **5V** or **3V** (red wire on USB console cable)
- **Camera Ground** to **USB Ground** (black wire)
- **Camera RX (white wire)** to **USB TX** (green wire)
- **Camera TX (green wire)** to **USB RX** (white wire)

![camera_VC0706_USBSerial_UART_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/083/347/medium640/camera_VC0706_USBSerial_UART_bb.png?1572561946)

Here's an example using the Pi's built-in UART:

- **Camera 5V (black wire)**&nbsp; to **PI**  **3V or 5V**  
- **Camera GND (black wire)** to **Pi Ground&nbsp;**
- **Camera RX (white wire)** to **Pi TX**
- **Camera TX (green wire)** to **Pi RX**

![camera_VC0706_Raspi_UART_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/083/348/medium640/camera_VC0706_Raspi_UART_bb.png?1572562067)

If you want to use the built-in UART, you'll need to disable the serial console and enable the serial port hardware in **raspi-config**. See [the UART/Serial section of the CircuitPython on Raspberry Pi guide](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/uart-serial) for detailed instructions on how to do this.

Warning: 

# CircuitPython Installation of VC0706

As mentioned, you'll also need to install the [Adafruit CircuitPython VC0706](https://github.com/adafruit/Adafruit_CircuitPython_VC0706) library on your CircuitPython board. In addition, the [Adafruit CircuitPython SD](https://github.com/adafruit/Adafruit_CircuitPython_SD) library is used to read and write data to the SD card.&nbsp;&nbsp;

First make sure you are running the&nbsp;[latest version of Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)&nbsp;for your board.

Next you'll need to install the necessary libraries&nbsp;to use the hardware--carefully follow the steps to find and install these libraries from&nbsp;[Adafruit's CircuitPython library bundle](https://circuitpython.org/libraries).&nbsp; The Welcome to CircuitPython guide has [a great page on how to install the library bundle](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

[If your board supports&nbsp; **sdcardio**](https://docs.circuitpython.org/en/latest/shared-bindings/support_matrix.html), then this is the preferred method to do things.&nbsp; **sdcardio&nbsp;** is a built-in module on boards that support it, so you don't have to copy it over.

After downloading the bundle, copy the necessary libraries from the bundle:

- **adafruit\_vc0706.mpy**
- **adafruit\_sdcard.mpy** (if your board doesn't support sdcardio)
- **adafruit\_bus\_device**

Before continuing, make sure your board's **lib** folder has the **adafruit\_vc0706.mpy, adafruit\_sd.mpy,** and **adafruit\_bus\_device** files and folders&nbsp;copied over.

Next[&nbsp;connect to the board's serial REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl) so you are at the CircuitPython&nbsp; **\>\>\>** &nbsp;prompt.

# Python Installation of VC0706 Library

You'll need to install the **Adafruit\_Blinka** library that provides the CircuitPython support in Python. This may also require enabling UART on your platform and verifying you are running Python 3. [Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)!

Once that's done, from your command line run the following command:

- `sudo pip3 install adafruit-circuitpython-vc0706`

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

# Microcontroller CircuitPython Usage (not for Linux/SBC)

To demonstrate the usage of the camera, let's look at an example that will capture an image and save it to the micro SD card as a jpeg file.&nbsp; Load up the example below and save it as **code.py** on your **CIRCUITPY** drive, then open the serial REPL to see the output:

https://github.com/adafruit/Adafruit_CircuitPython_VC0706/blob/main/examples/vc0706_snapshot_simpletest.py

You should see output like the following as the program prints&nbsp;information about the camera and saves an image to the micro SD card:

![](https://cdn-learn.adafruit.com/assets/assets/000/047/940/medium800/camera_Screen_Shot_2017-11-03_at_12.33.26_PM.png?1509737665)

Be aware saving the image to the card takes some time, as the data is transferred over both a serial connection from the camera and the SPI connection to the micro SD card.&nbsp; A full image capture at 640x480 pixels takes about 30 seconds, but might take longer depending on your board and micro SD card speed.

Once the image capture finishes, you'll see a message printed:

![](https://cdn-learn.adafruit.com/assets/assets/000/047/941/medium800/camera_Screen_Shot_2017-11-03_at_12.39.17_PM.png?1509737973)

Exit the REPL and power down the board, then remove the SD card and connect it to your computer.&nbsp; You should see an **image.jpg** file saved on it, and inside will be a picture captured from the camera:

![](https://cdn-learn.adafruit.com/assets/assets/000/047/942/medium800/camera_image.jpg?1509738006)

Woo hoo, that's all there is to the basics of capturing an image with the serial TTL camera and CircuitPython!&nbsp; Let's look at the code in a tiny bit more detail to understand the usage.

First the example needs to setup the SD card and mount it on the filesystem.&nbsp; This is all boilerplate code from the [CircuitPython SD card guide](../../../../micropython-hardware-sd-cards/)&nbsp;(highly recommended to read it too!):

```auto
# Configuration:
SD_CS_PIN = board.D10  # CS for SD card (SD_CS is for Feather Adalogger)
IMAGE_FILE = "/sd/image.jpg"  # Full path to file name to save captured image.
# Will overwrite!

# Setup SPI bus (hardware SPI).
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Setup SD card and mount it in the filesystem.
# Uncomment if your board doesn't support sdcardio
# sd_cs = digitalio.DigitalInOut(SD_CS_PIN)
# sdcard = adafruit_sdcard.SDCard(spi, sd_cs)
sdcard = sdcardio.SDCard(
    spi, SD_CS_PIN
)  # Comment out if your board doesn't support sdcardio

vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
```

Now the VC0706 module is setup and an instance of the VC0706 class is created.&nbsp; Notice we need to create a UART device on whatever pins have hardware support and then this is passed to the camera creator.

```
# Create a serial connection for the VC0706 connection, speed is auto-detected.
uart = busio.UART(board.TX, board.RX, timeout=250)
# Setup VC0706 camera
vc0706 = adafruit_vc0706.VC0706(uart)
```

Once the VC0706 instance is created you can read some interesting properties, like the version string:

```
# Print the version string from the camera.
print('VC0706 version:')
print(vc0706.version)
```

Or even set and get the size of the image (640x480, 320x240, 160x120):

```
# Set the image size.
vc0706.image_size = adafruit_vc0706.IMAGE_SIZE_640x480 # Or set IMAGE_SIZE_320x240 or
                                                       # IMAGE_SIZE_160x120
# Note you can also read the property and compare against those values to
# see the current size:
size = vc0706.image_size
if size == adafruit_vc0706.IMAGE_SIZE_640x480:
    print('Using 640x480 size image.')
elif size == adafruit_vc0706.IMAGE_SIZE_320x240:
    print('Using 320x240 size image.')
elif size == adafruit_vc0706.IMAGE_SIZE_160x120:
print('Using 160x120 size image.')
```

Now the real fun, you can capture an image!&nbsp; This works by first telling the camera to 'freeze' the current image frame in memory with the `take_picture` function.&nbsp; Then you need to make a loop that calls the `read_picture_into` function repeatedly to grab buffers of image data from the camera.&nbsp; Once you have image data it's up to you to do something with it, like write it to a SD card file (although you don't have to do that, you could send it to a web service or do other fun thing!).

The code in this example will capture an image and then save it to a file on the SD card:

```
# Take a picture.
print('Taking a picture in 3 seconds...')
time.sleep(3)
print('SNAP!')
if not vc0706.take_picture():
    raise RuntimeError('Failed to take picture!')

# Print size of picture in bytes.
frame_length = vc0706.frame_length
print('Picture size (bytes): {}'.format(frame_length))

# Open a file for writing (overwriting it if necessary).
# This will write 50 bytes at a time using a small buffer.
# You MUST keep the buffer size under 100!
print('Writing image: {}'.format(IMAGE_FILE), end='')
with open(IMAGE_FILE, 'wb') as outfile:
    wcount = 0
    while frame_length &gt; 0:
        # Compute how much data is left to read as the lesser of remaining bytes
        # or the copy buffer size (32 bytes at a time).  Buffer size MUST be
        # a multiple of 4 and under 100.  Stick with 32!
        to_read = min(frame_length, 32)
        copy_buffer = bytearray(to_read)
        # Read picture data into the copy buffer.
        if vc0706.read_picture_into(copy_buffer) == 0:
            raise RuntimeError('Failed to read picture frame data!')
        # Write the data to SD card file and decrement remaining bytes.
        outfile.write(copy_buffer)
        frame_length -= 32
        # Print a dot every 2k bytes to show progress.
        wcount += 1
        if wcount &gt;= 64:
            print('.', end='')
            wcount = 0

```

One thing to be aware of is that the size of the buffer passed to `read_picture_into` must be a multiple of 4. This is an requirement of the camera hardware itself.&nbsp; In addition, it must be below 100 to fit within an internal buffer.&nbsp; Stick with using a value of 32 like the example here shows!

That's all there is to capturing and saving an image to an SD card using CircuitPython!

# Saving Images to CircuitPython Internal Filesystem

Instead of using the SD card to store images it's also possible with CircuitPython or Python to save images to the internal filesystem where your code and other data files live.&nbsp; This is possible with a few caveats, in particular once you enable writing to the internal storage **you can't set or change your code** over the USB drive connection to your computer.&nbsp; This means you probably want to get your program working first on SD storage or ignoring the file save, and then switch to using internal storage when you know your code is working and ready to write files.

Also be aware internal storage is quite limited on some boards.&nbsp; The non-express boards only have ~64kb or space and a single 640x480 JPEG image from the camera can occupy 50 kilobytes of more of space alone!&nbsp; You likely only want to save images to the internal storage for Express boards that have 2 megabytes of space, however even on those boards take care to not store too many images as they will quickly add up

## Activate Internal storage on Microcontrollers

**This step is not used on Linux / Single Board Computers**

To get started first [follow the steps on the CircuitPython Storage page of the CircuitPython Essentials guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage) to enable writing to internal storage.&nbsp; In particular edit the **boot.py** on your **CIRCUITPY** drive (creating it if it doesn't exist) and add these lines:

```
import digitalio
import board
import storage
 
switch = digitalio.DigitalInOut(board.D5)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
 
# If the D5 is connected to ground with a wire
# you can edit files over the USB drive again.
storage.remount("/", not switch.value)
```

Remember once you remount("/") **you cannot edit code over the USB drive anymore!** &nbsp; That means you can't edit **boot.py** which is a bit of a conundrum. So we configure the **boot.py** to selectively mount the internal filesystem as writable based on a switch or even just alligator clip connected to ground.&nbsp; Like the [CPU temperature guide shows](../../../../cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem#selectively-setting-readonly-to-false-on-boot). In this example we're using **D5** but select any available pin.

This code will look at the **D5** digital input when the board starts up and if it's connected to ground (use an alligator clip or wire, for example, to connect from **D5** to board ground) it will disable internal filesystem writes and allow you to edit code over the USB drive as normal.&nbsp; Remove the alligator clip, reset the board, and the **boot.py** will switch to mounting the internal filesystem as writable so you can log images to it again (but not write any code!).&nbsp;

Remember when you enable USB drive writes (by connecting **D5** to ground at startup) you **cannot write files** to the internal filesystem and any code in your **code.py** that attempts to do so (like the example below) will fail.&nbsp; Keep this in mind as you edit code, once you modify code you need to remove the alligator clip, reset the board to re-enable internal filesystem writes, and then watch the output of your program.

Danger: 

## Example Code for saving to internal file system (CircuitPython or Linux / SBC)

Now we can use a slightly modified version of the example that will save to the internal filesystem instead of a SD card. The code is exactly the same as for SD cards except instead of mounting the SD card and opening a file there, we open a file on the internal storage.&nbsp; The exact same VC0706 functions and control loop are used because Python's read and write functions don't care if they're writing to a SD card or internal storage--it's all the same to Python!

https://github.com/adafruit/Adafruit_CircuitPython_VC0706/blob/main/examples/vc0706_snapshot_filesystem.py

## Saving Images to Computer or Raspberry Pi / Linux

Saving images to a Raspberry Pi or other Linux computer is very similar to the CircuitPython internal filesystem. You simply need to comment out a line and uncomment two more depending on what set up you're using.

Info: 

Regardless of which set up you're using, you'll need to comment out the following line:

`uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=0.25)`

## USB to Serial Converter

If using a USB to serial converter, uncomment the following lines:

`# import serial`

` # uart = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=0.25)`

## Raspberry Pi / Linux

If using a Raspberry Pi, uncomment the following lines (if you're using a different single board computer, you may need to update the serial port!):

`# import serial`

`# uart = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=0.25)`

The rest of the code works the same way. Smile!

- [Previous Page](https://learn.adafruit.com/ttl-serial-camera/arduino-usage.md)
- [Next Page](https://learn.adafruit.com/ttl-serial-camera/f-a-q.md)

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
