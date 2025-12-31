# Source: https://learn.adafruit.com/chumby-hacker-board/i2c-sensor.md

# Chumby Hacker Board

## i2c Sensor

## i2c Twiddler
First, you'll need to have a toolchain installed so make sure you go back and install it!  
  
Sean Cross wrote a great i2c twiddler-tool. This allows you to poke and peek at i2c chips right from the command line. Nice!  
  
Scroll down and copy his i2c C code. Open up your terminal to the CHB and type in **mkdir /mnt/storage/dev** (or whatever place you want to store your code), then **cd /mnt/storage/dev** and finally **cat \> i2c.c** into the terminal and hit return. Then paste in the code and finish by typing **Control-D**  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/385/medium800/microcomputers_i2ccopy.gif?1447864338)

Then compile the code with **gcc** by typing in&nbsp; **gcc -o i2c i2c.c** to create the **i2c** executable. Then run it and make sure you get the response below.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/386/medium800/microcomputers_i2ccompile.gif?1447864338)

## Reading the MMA7455L accelerometer

There's a Freescale +-2G to +-8G 3-access accelerometer on the CHB for you to play with, lets get some readings. First off, we need to know what the i2c address is.&nbsp;[Open up the datasheet](http://www.freescale.com/files/sensors/doc/data_sheet/MMA7455L.pdf) and look for the section called "i2c Secondary Address".

![](https://cdn-learn.adafruit.com/assets/assets/000/002/387/medium800/microcomputers_mma7455addr.gif?1447864338)

 **$1D** means hexadecimal 0x1D which is the same as decimal 29. Great! Lets read byte #0 from the accelerometer by typing in **./i2c r 29 0** ![](https://cdn-learn.adafruit.com/assets/assets/000/002/388/medium800/microcomputers_i2cfail.gif?1447864339)

?? We got an error that the register was not readable. This means the chip could not be found on the i2c bus. :( But then we rememer that i2c addresses are 7 bits long and are transmitted in the upper bits of an 8-bit byte. So we actually need to shift the address up by 1 bit. That's easy to do, though, just multiply by 2 to get i2c address **58**

![](https://cdn-learn.adafruit.com/assets/assets/000/002/389/medium800/microcomputers_i2cok.gif?1447864339)

Rock! Now we need to figure out what registers we can read, looking at the datasheet we see:![](https://cdn-learn.adafruit.com/assets/assets/000/002/390/medium800/microcomputers_mma7455reg.gif?1447864340)

There's a lot of stuff! Lets start with one we know is going to work, like **$0D** (hex 0x0D = dec 13)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/391/medium800/microcomputers_mmareg13.gif?1447864341)

It in fact returns the value 0x1D which we know is the i2c address.## Acceleromate!
OK so now we want to get that XYZ data, right? Looking at the register file it seems like the first 6 bytes are used for 10-bit readings, but we can get single 8 bit readings from registers number 6, 7 and 8.  
  
If you're careful you can read those registers while having a friend gently shake the board, you'll see different values returned.  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/392/medium800/microcomputers_mmai2ctest.gif?1447864342)

However, wouldn't it be great if you didn't need a friend to shake the board while you pressed Up-arrow & Return? Lets edit Sean's code. To begin we will put&nbsp; **#define**'s in for the address and registers.```
// The 'raw' 7 bit address shifted up 
#define MMA7455_I2CADDR (0x1D * 2)

// The registers to read!
#define MMA7455_XOUT8 6
#define MMA7455_YOUT8 7
#define MMA7455_ZOUT8 8
```

Then replace the **main()** function with our own which is shorter and only reads those registers to print out the values.

```
int main(int argc, char **argv) {
    int i2c_file;
    int8_t x, y, z;  // the readings are 8 bits and signed!

    // Open a connection to the I2C userspace control file.
    if ((i2c_file = open(I2C_FILE_NAME, O_RDWR)) &lt; 0) {
        perror("Unable to open i2c control file");
        exit(1);
    }

    // ignore arguments!

    while (1) {
      
      // read X and Y and Z from the register
      if( get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_XOUT8, &amp;x) ||
	  get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_YOUT8, &amp;y) ||
	  get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_ZOUT8, &amp;z) ) {

	printf("Unable to read register!\n");
	return -1;
      }

      printf("X = %d\tY = %d\tZ = %d\n", x, y, z); 
    }

    close(i2c_file);
    return 0;
}
```

Note the while() loop, and that we read all three registers and stick the results into 8-bit signed variables. Then we printf() 'em all and loop again.  
  
You can grab all of the code below.  
  
Stick the code in a new file called **mma7455.c** by copying and pasting as before. Then compile by running **gcc -o mma7455 mma7455.c** and run with **./mma7455**. Now shake it!  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/393/medium800/microcomputers_shaken.gif?1447864343)

There you go! Now you can talk to the accelerometer to get motion data, and this code is easily adaptable for any i2c chip you may want to use. Enjoy!## Basic i2c twiddler Code
```
/*
 This software uses a BSD license.

Copyright (c) 2010, Sean Cross / chumby industries
All rights reserved.
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.  
 * Neither the name of Sean Cross / chumby industries nor the names
   of its contributors may be used to endorse or promote products
   derived from this software without specific prior written
   permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
 WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
 
 */

#include &lt;stdio.h&gt;
#include &lt;linux/i2c.h&gt;
#include &lt;linux/i2c-dev.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/ioctl.h&gt;
#include &lt;string.h&gt;


#define I2C_FILE_NAME "/dev/i2c-0"
#define USAGE_MESSAGE \
    "Usage:\n" \
    "  %s r [addr] [register]   " \
        "to read value from [register]\n" \
    "  %s w [addr] [register] [value]   " \
        "to write a value [value] to register [register]\n" \
    ""

static int set_i2c_register(int file,
                            unsigned char addr,
                            unsigned char reg,
                            unsigned char value) {

    unsigned char outbuf[2];
    struct i2c_rdwr_ioctl_data packets;
    struct i2c_msg messages[1];

    messages[0].addr  = addr;
    messages[0].flags = 0;
    messages[0].len   = sizeof(outbuf);
    messages[0].buf   = outbuf;

    /* The first byte indicates which register we'll write */
    outbuf[0] = reg;

    /* 
     * The second byte indicates the value to write.  Note that for many
     * devices, we can write multiple, sequential registers at once by
     * simply making outbuf bigger.
     */
    outbuf[1] = value;

    /* Transfer the i2c packets to the kernel and verify it worked */
    packets.msgs  = messages;
    packets.nmsgs = 1;
    if(ioctl(file, I2C_RDWR, &amp;packets) &lt; 0) {
        perror("Unable to send data");
        return 1;
    }

    return 0;
}


static int get_i2c_register(int file,
                            unsigned char addr,
                            unsigned char reg,
                            unsigned char *val) {
    unsigned char inbuf, outbuf;
    struct i2c_rdwr_ioctl_data packets;
    struct i2c_msg messages[2];

    /*
     * In order to read a register, we first do a "dummy write" by writing
     * 0 bytes to the register we want to read from.  This is similar to
     * the packet in set_i2c_register, except it's 1 byte rather than 2.
     */
    outbuf = reg;
    messages[0].addr  = addr;
    messages[0].flags = 0;
    messages[0].len   = sizeof(outbuf);
    messages[0].buf   = &amp;outbuf;

    /* The data will get returned in this structure */
    messages[1].addr  = addr;
    messages[1].flags = I2C_M_RD/* | I2C_M_NOSTART*/;
    messages[1].len   = sizeof(inbuf);
    messages[1].buf   = &amp;inbuf;

    /* Send the request to the kernel and get the result back */
    packets.msgs      = messages;
    packets.nmsgs     = 2;
    if(ioctl(file, I2C_RDWR, &amp;packets) &lt; 0) {
        perror("Unable to send data");
        return 1;
    }
    *val = inbuf;

    return 0;
}


int main(int argc, char **argv) {
    int i2c_file;

    // Open a connection to the I2C userspace control file.
    if ((i2c_file = open(I2C_FILE_NAME, O_RDWR)) &lt; 0) {
        perror("Unable to open i2c control file");
        exit(1);
    }


    if(argc &gt; 3 &amp;&amp; !strcmp(argv[1], "r")) {
        int addr = strtol(argv[2], NULL, 0);
        int reg = strtol(argv[3], NULL, 0);
        unsigned char value;
        if(get_i2c_register(i2c_file, addr, reg, &amp;value)) {
            printf("Unable to get register!\n");
        }
        else {
            printf("Register %d: %d (%x)\n", reg, (int)value, (int)value);
        }
    }
    else if(argc &gt; 4 &amp;&amp; !strcmp(argv[1], "w")) {
        int addr = strtol(argv[2], NULL, 0);
        int reg = strtol(argv[3], NULL, 0);
        int value = strtol(argv[4], NULL, 0);
        if(set_i2c_register(i2c_file, addr, reg, value)) {
            printf("Unable to get register!\n");
        }
        else {
            printf("Set register %x: %d (%x)\n", reg, value, value);
        }
    }
    else {
        fprintf(stderr, USAGE_MESSAGE, argv[0], argv[0]);
    }


    close(i2c_file);


    return 0;
}
```

## MMA7455L reader
```
/*
 This software uses a BSD license.

Copyright (c) 2010, Sean Cross / chumby industries &amp;  Limor Fried / adafruit industries (we are both industrious people, eh?)

All rights reserved.
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:

 * Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.  
 * Neither the name of Sean Cross / chumby industries nor the names
   of its contributors may be used to endorse or promote products
   derived from this software without specific prior written
   permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
 WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
 */

#include &lt;stdio.h&gt;
#include &lt;linux/i2c.h&gt;
#include &lt;linux/i2c-dev.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/ioctl.h&gt;
#include &lt;string.h&gt;

// The 'raw' 7 bit address shifted up 
#define MMA7455_I2CADDR (0x1D * 2)

// The registers to read!
#define MMA7455_XOUT8 6
#define MMA7455_YOUT8 7
#define MMA7455_ZOUT8 8


#define I2C_FILE_NAME "/dev/i2c-0"

static int get_i2c_register(int file,
                            unsigned char addr,
                            unsigned char reg,
                            unsigned char *val) {
    unsigned char inbuf, outbuf;
    struct i2c_rdwr_ioctl_data packets;
    struct i2c_msg messages[2];

    /*
     * In order to read a register, we first do a "dummy write" by writing
     * 0 bytes to the register we want to read from.  This is similar to
     * the packet in set_i2c_register, except it's 1 byte rather than 2.
     */
    outbuf = reg;
    messages[0].addr  = addr;
    messages[0].flags = 0;
    messages[0].len   = sizeof(outbuf);
    messages[0].buf   = &amp;outbuf;

    /* The data will get returned in this structure */
    messages[1].addr  = addr;
    messages[1].flags = I2C_M_RD/* | I2C_M_NOSTART*/;
    messages[1].len   = sizeof(inbuf);
    messages[1].buf   = &amp;inbuf;

    /* Send the request to the kernel and get the result back */
    packets.msgs      = messages;
    packets.nmsgs     = 2;
    if(ioctl(file, I2C_RDWR, &amp;packets) &lt; 0) {
        perror("Unable to send data");
        return 1;
    }
    *val = inbuf;

    return 0;
}


int main(int argc, char **argv) {
    int i2c_file;
    int8_t x, y, z;  // the readings are 8 bits and signed!

    // Open a connection to the I2C userspace control file.
    if ((i2c_file = open(I2C_FILE_NAME, O_RDWR)) &lt; 0) {
        perror("Unable to open i2c control file");
        exit(1);
    }

    // ignore arguments!

    while (1) {
      
      // read X and Y and Z from the register
      if( get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_XOUT8, &amp;x) ||
	  get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_YOUT8, &amp;y) ||
	  get_i2c_register(i2c_file, MMA7455_I2CADDR, MMA7455_ZOUT8, &amp;z) ) {

	printf("Unable to read register!\n");
	return -1;
      }

      printf("X = %d\tY = %d\tZ = %d\n", x, y, z); 
    }

    close(i2c_file);
    return 0;
}
```

- [Previous Page](https://learn.adafruit.com/chumby-hacker-board/compiler.md)
- [Next Page](https://learn.adafruit.com/chumby-hacker-board/wifi.md)

## Featured Products

### USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply

[USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply](https://www.adafruit.com/product/961)
Add lots more USB capability to your Raspberry Pi or computer using this powered USB 2.0 hub. It adds a full **seven powered ports** , all at USB 2.0 speeds so you can use video cameras and other high speed devices (cheaper hubs are v1.1 and not as fast!)  
  
The extra sauce...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/961)
[Related Guides to the Product](https://learn.adafruit.com/products/961/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 2.1mm to 1.7mm DC jack adapter

[2.1mm to 1.7mm DC jack adapter](https://www.adafruit.com/product/411)
We're carrying this adapter primarily to allow Chumby Hacker Board users to adapt our nice [5V @ 2A power supply](http://www.adafruit.com/products/276) to their CHB. But you can use this adapter for anything else that has a 1.7mm DC jack, such as a PSP.

In Stock
[Buy Now](https://www.adafruit.com/product/411)
[Related Guides to the Product](https://learn.adafruit.com/products/411/guides)
### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### Ethernet Cable - 10 ft long

[Ethernet Cable - 10 ft long](https://www.adafruit.com/product/730)
We have so many Internet-connected goodies in the shop, we figured it's time to carry a cable so you can easily connect them up! This cable is 10 feet long, black and has all 8 wires installed. Perfect for use with the [BeagleBone](http://www.adafruit.com/products/513), <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/730)
[Related Guides to the Product](https://learn.adafruit.com/products/730/guides)
### USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi

[USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi](https://www.adafruit.com/product/954)
The cable is easiest way ever to connect to your microcontroller/Raspberry Pi/WiFi router serial console port. Inside the big USB plug is a USB\<-\>Serial conversion chip and at the end of the 36" cable are four wire - red power, black ground, white RX into USB port, and green TX out...

In Stock
[Buy Now](https://www.adafruit.com/product/954)
[Related Guides to the Product](https://learn.adafruit.com/products/954/guides)
### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [CircuitPython Libraries on MicroPython using the Raspberry Pi Pico](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico.md)
- [Hallowing Minotaur Maze](https://learn.adafruit.com/hallowing-minotaur-maze.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Adafruit 2.9" eInk Display Breakouts and FeatherWings](https://learn.adafruit.com/adafruit-2-9-eink-display-breakouts-and-featherwings.md)
- [Pi SSD Media Server](https://learn.adafruit.com/pi-ssd-media-server.md)
- [Creating Slideshows in CircuitPython](https://learn.adafruit.com/creating-slideshows-in-circuitpython.md)
- [Network Interface Failover using FONA](https://learn.adafruit.com/network-interface-failover-using-fona.md)
- [Matrix Keypad](https://learn.adafruit.com/matrix-keypad.md)
- [Native MP3 decoding on Arduino](https://learn.adafruit.com/native-mp3-decoding-on-arduino.md)
- [Raspberry Pi HQ Camera Case](https://learn.adafruit.com/raspberry-pi-hq-camera-case.md)
- [Articulated Pi Display V2 Mount](https://learn.adafruit.com/pi-wall-mount.md)
- [World's Smallest MAME Arcade Cabinet](https://learn.adafruit.com/worlds-smallest-mame-arcade-cabinet.md)
- [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python.md)
- [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython.md)
- [Adafruit QT Py and NeoPixel LEDs](https://learn.adafruit.com/qt-py-and-neopixel-leds.md)
