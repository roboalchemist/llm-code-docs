# Source: https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/cosm-account-and-feed.md

# Send Raspberry Pi Data to COSM

## COSM Account and Feed

Info: 

COSM (used to be Pachube) helps connect little devices like the raspberry pi to the internet. You will need to do the following to use COSM.

- Setup a Account
- Create a Feed
- Save the API\_KEY
- Save the FEED ID

  
# Setup a Account
You will need to create a COSM account. Click on the blue "Get Started" circle to create a new account. It's your typical e-mail/password followed by password verification. You will need to check your e-mail and click the verification link. ![](https://cdn-learn.adafruit.com/assets/assets/000/019/695/medium800/raspberry_pi_cosm-signup.jpg?1410968098)

# Add a Feed
Click the blue plus to add a feed.&nbsp;  
![](https://cdn-learn.adafruit.com/assets/assets/000/019/696/medium800/raspberry_pi_cosm-add-feed.jpg?1410968150)

Select Arduino

![](https://cdn-learn.adafruit.com/assets/assets/000/019/697/medium800/raspberry_pi_cosm-something-else.jpg?1410968188)

Give your new&nbsp;feed a title and tags.  
  
Title: "Raspberry Pi Temperature" _(or whatever you like)_  
Tags: raspberry pi, temperature, adc _(or make up your own)_  
&nbsp;  
Select the "Create" button.

![](https://cdn-learn.adafruit.com/assets/assets/000/019/698/medium800/raspberry_pi_cosm-configure-arduino.jpg?1410968231)

You need to extract the API\_KEY and FEEDID from the code sample that COSM provides. These will go into the python script that we setup on the next page. The API\_KEY lets&nbsp;COSM knows who is connecting and to which feed they want to send data.  
  
In this example the API\_KEY is:&nbsp;5RNOO3ShYJxYiq2V2sgSRtz3112SAKxFQjNDQmNXc0RScz0g  
The FEEDID is: 68872  
  
Do not use those numbers, use your own!

![](https://cdn-learn.adafruit.com/assets/assets/000/019/699/medium800/raspberry_pi_cosm-api-key-feedid.jpg?1410968272)

- [Previous Page](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/necessary-packages.md)
- [Next Page](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm/python-script.md)

## Featured Products

### MCP3008 - 8-Channel 10-Bit ADC With SPI Interface

[MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://www.adafruit.com/product/856)
Need to add analog inputs? This chip will add 8 channels of 10-bit analog input to your microcontroller or microcomputer project. It's super easy to use and uses SPI so only 4 pins are required. We chose this chip as a great accompaniment to the Raspberry Pi computer because it's fun...

In Stock
[Buy Now](https://www.adafruit.com/product/856)
[Related Guides to the Product](https://learn.adafruit.com/products/856/guides)
### TMP36 - Analog Temperature sensor

[TMP36 - Analog Temperature sensor](https://www.adafruit.com/product/165)
Wide range, low power temperature sensor outputs an analog voltage that is proportional to the ambient temperature. To use, connect pin 1 (left) to power (between 2.7 and 5.5V), pin 3 (right) to ground, and pin 2 to analog in on your microcontroller. The voltage out is 0V at -50°C and...

In Stock
[Buy Now](https://www.adafruit.com/product/165)
[Related Guides to the Product](https://learn.adafruit.com/products/165/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin

[GPIO Ribbon Cable for Raspberry Pi Model A and B - 26 pin](https://www.adafruit.com/product/862)
That new Raspberry Pi® Model A or B computer you just got has a row of 2x13 pin headers soldered on - those are the GPIO (general purpose input/output) pins and for those of us who like to hack electronics they are where the real fun is. By programming the Pi, you can twiddle those pins...

In Stock
[Buy Now](https://www.adafruit.com/product/862)
[Related Guides to the Product](https://learn.adafruit.com/products/862/guides)
### Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B

[Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B](https://www.adafruit.com/product/859)
 **Discontinued** - you can grab&nbsp;[Adafruit Pi Box Plus - Enclosure for RasPi Model B+/Pi 2/ Pi 3](https://www.adafruit.com/product/1985) instead!&nbsp;

**We're still selling this classic Adafruit case for those who specifically want it but <a...></a...>**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/859)
[Related Guides to the Product](https://learn.adafruit.com/products/859/guides)

## Related Guides

- [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://learn.adafruit.com/mcp3008-spi-adc.md)
- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [PyPortal IoT Plant Monitor with AWS IoT and CircuitPython](https://learn.adafruit.com/pyportal-iot-plant-monitor-with-aws-iot-and-circuitpython.md)
- [Adafruit PMSA003I Air Quality Breakout](https://learn.adafruit.com/pmsa003i.md)
- [10" Raspberry Pi Desktop](https://learn.adafruit.com/10-raspberry-pi-desktop.md)
- [Adafruit BMP388 and BMP390 - Precision Barometric Pressure and Altimeter](https://learn.adafruit.com/adafruit-bmp388-bmp390-bmp3xx.md)
- [Little Desktop Connection Machine](https://learn.adafruit.com/little-connection-machine.md)
- [USB Audio Cards with a Raspberry Pi ](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi.md)
- [Sparkle Motion Dance Shoes](https://learn.adafruit.com/sparkle-motion-dance-shoes.md)
- [CircuitPython on Raspberry Pi (Bare Metal / No OS)](https://learn.adafruit.com/circuitpython-on-raspberry-pi-bare-metal-no-os.md)
- [Jack-o-Theremin](https://learn.adafruit.com/jack-o-theremin.md)
- [Raspberry Pi Hosting Node-Red](https://learn.adafruit.com/raspberry-pi-hosting-node-red.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [MPR121 Capacitive Touch Sensor on Raspberry Pi & BeagleBone Black](https://learn.adafruit.com/mpr121-capacitive-touch-sensor-on-raspberry-pi-and-beaglebone-black.md)
- [Using OSC to Communicate with a Raspberry Pi](https://learn.adafruit.com/raspberry-pi-open-sound-control.md)
- [How to Scan and Detect I2C Addresses](https://learn.adafruit.com/scanning-i2c-addresses.md)
