# Source: https://learn.adafruit.com/arduino-tips-tricks-and-techniques/bootloader.md

# Arduino Tips, Tricks, and Techniques

## Bootloader

Info: 

## Bootloader for the Atmega328
[Here is the package for a 'fixed up' ATmega328 bootloader](http://learn.adafruit.com/system/assets/assets/000/010/292/original/Adaboot328.zip). To program it you may need to change the Makefile's ISPTOOL, etc definitions. The commands are **make adaboot328; make TARGET=adaboot328 isp328** (I couldn't get the default 'isp' target to work so I made a new one).  
  
This version has a few fixes: first it integrates the 'no-wait' and 'no-hang' fixes below. It also fixes the annoying "missing signature bytes" bug that freaks out avrdude when programming without the IDE. I also repaired the EEPROM code so that now you can upload and download the EEPROM memory as well as flash. Finally, theres a 'upload feedback' using the LED, for arduino clones that don't have TX/RX leds.  
  
Please note that the fuses are different for this chip because of the extended memory!  
## "No-Wait" Bootloader
Here's a bootloader hack that will automatically start the sketch after it has been uploaded and will also only start the bootloader when the reset button is pressed (so when you plug in power it will go straight to the sketch).  
  
Copy the following lines:  
```
ch = MCUSR;
    MCUSR = 0;

    WDTCSR |= _BV(WDCE) | _BV(WDE);
    WDTCSR = 0;

    // Check if the WDT was used to reset, in which case we dont bootload and skip straight to the code. woot.
    if (! (ch &amp;  _BV(EXTRF))) // if its a not an external reset...
      app_start();  // skip bootloader
```

And paste them as shown:

```
/* main program starts here */
int main(void)
{
    uint8_t ch,ch2;
    uint16_t w;

    ch = MCUSR;
    MCUSR = 0;

    WDTCSR |= _BV(WDCE) | _BV(WDE);
    WDTCSR = 0;

    // Check if the WDT was used to reset, in which case we dont bootload and skip straight to the code. woot.
    if (! (ch &amp;  _BV(EXTRF))) // if its a not an external reset...
      app_start();  // skip bootloader

    /* set pin direction for bootloader pin and enable pullup */
    /* for ATmega128, two pins need to be initialized */
```

Now, in the same way, copy the following code:

```
// autoreset via watchdog (sneaky!)
	  WDTCSR = _BV(WDE);
	  while (1); // 16 ms
```

And paste it here:

```
/* Leave programming mode  */
	else if(ch=='Q') {
	  nothing_response();

	  // autoreset via watchdog (sneaky!)
	  WDTCSR = _BV(WDE);
	  while (1); // 16 ms
	}
	/* Erase device, don't care as we will erase one page at a time anyway.  */
	else if(ch=='R') {
	    nothing_response();
	}
```

You can also just grab the [source code](http://learn.adafruit.com/system/assets/assets/000/010/293/original/ATmegaBOOT_168.c) and [compiled hex file here](http://learn.adafruit.com/system/assets/assets/000/010/294/original/ATmegaBOOT_168_ng.hex.txt).  
  
It will work in NG or Diecimila Arduinos.

## No-Hang Bootloader
If you are using a Diecimila with auto-reset you may be frustrated when your communications program accidentally triggers the bootloader. Here is a quick hack to make the bootloader quit if it doesn't receive a '0' character first (which would indicate the Arduino software is trying to talk to it.  
  
Copy the following line:```
uint8_t firstchar = 0;
```

And paste:

```
/* main program starts here */
int main(void)
{
    uint8_t ch,ch2;
    uint16_t w;
    uint8_t firstchar = 0;
```

Copy:

```
firstchar = 1; // we got an appropriate bootloader instruction
```

Paste:

```
/* Hello is anyone home ? */ 
	if(ch=='0') {
	  firstchar = 1; // we got an appropriate bootloader instruction
	  nothing_response();
```

Then paste this below the above code:

```
} else if (firstchar == 0) {
	  // the first character we got is not '0', lets bail!
	  // autoreset via watchdog (sneaky!)
	  WDTCSR = _BV(WDE);
	  while (1); // 16 ms
	}
```

You can also just replace the last two lines with **app\_start()**

## Upload Sketches with AVRDUDE
The bootloader is an 'stk500'-compatible, which means you can use good ol' AVRDUDE to program the arduino.  
  
Just plug in the USB cable, then press the reset just before you start avrdude. [If you need an avrdude tutorial, check out this page](http://ladyada.net/learn/avr/index.html).  

- Use **-b 19200** to set the baud rate to 19200
- The device signature reads dont seem to work so you'll want to use **-F**
- The programmer type is **avrisp**
- The device type is **-p m168**
- The port is whatever the FTDI chip shows up as

![](https://cdn-learn.adafruit.com/assets/assets/000/003/514/medium800/learn_arduino_avrdudeload.jpg?1396797563)

- [Previous Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/arduino-libraries.md)
- [Next Page](https://learn.adafruit.com/arduino-tips-tricks-and-techniques/upgrade.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Arduino bootloader-programmed chip (Atmega328P)

[Arduino bootloader-programmed chip (Atmega328P)](https://www.adafruit.com/product/123)
This is a preprogrammed Atmega328P chip, useful if you want to make your own Arduino-compatible or repair a damaged chip on an exisiting Arduino UNO, Duemilanove, Diecimila, or NG!  
  
This chip is programmed with 'ADAboot', my version of the bootloader that is...

Out of Stock
[Buy Now](https://www.adafruit.com/product/123)
[Related Guides to the Product](https://learn.adafruit.com/products/123/guides)

## Related Guides

- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Adafruit Proto Shield for Arduino](https://learn.adafruit.com/adafruit-proto-shield-arduino.md)
- [Deciphering Strange Arduino Code](https://learn.adafruit.com/deciphering-strange-arduino-code.md)
- [Affordable HAL 9000 Replica](https://learn.adafruit.com/hal-9000-replica.md)
- [WiFi Candy Bowl Monitor](https://learn.adafruit.com/wifi-candy-bowl.md)
- [Arduino Lesson 1. Blink](https://learn.adafruit.com/adafruit-arduino-lesson-1-blink.md)
- [Using NeoPixels and Servos Together](https://learn.adafruit.com/neopixels-and-servos.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [1,500 NeoPixel LED Curtain with Raspberry Pi and Fadecandy](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
