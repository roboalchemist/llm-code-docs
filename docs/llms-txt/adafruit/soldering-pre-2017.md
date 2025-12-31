# Source: https://learn.adafruit.com/pi-thermal-printer/soldering-pre-2017.md

# Internet of Things Printer for Raspberry Pi

## Soldering

Danger: 

Some soldering steps take place close to pieces of the case. Be very careful where you set your soldering iron so as not to damage the plastic parts! Also watch out for flux spatter.  
  
During the soldering and assembly process, certain parts will become “tethered” together by wires…always pick up and move these parts together, don’t let pieces hang by the wires…this could damage parts or solder joints.

# Prepare Wires
In the plastic baggie accompanying the thermal printer should be two cables, a bit over a foot long. The **power cable** has **two** conductors: red and black. The **data cable** has **three** conductors: green, yellow and black.

![raspberry_pi_wires1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/510/medium640/raspberry_pi_wires1.jpg?1487633939)

 **Cut** the **red/black power cable** &nbsp;in **half**. This cable has a different plug&nbsp;at each end. We want to **keep the wider of the two plugs** &nbsp;for the printer; the other can be discarded or tossed in your spare bits drawer.

**The data cable (green/yellow/black) is&nbsp;NOT cut**, only the power cable!

![raspberry_pi_Power-Wire.jpg](https://cdn-learn.adafruit.com/assets/assets/000/040/977/medium640/raspberry_pi_Power-Wire.jpg?1492832637)

Use wire cutters to clip the side “wings” off the&nbsp;plug at one end of the data cable.

**Do not** cut any of these wires! Just trim the plastic.

![raspberry_pi_clip1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/040/991/medium640/raspberry_pi_clip1.jpg?1492891625)

![raspberry_pi_clip2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/040/992/medium640/raspberry_pi_clip2.jpg?1492891640)

Next, grab the female/female jumper wires and cut off the connector at **one end** of each of the following colors:

- 2 Black
- 1 Red
- 1 Yellow
- 1 Green

![raspberry_pi_DSC_3453.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/535/medium640/raspberry_pi_DSC_3453.jpg?1487637199)

### 

You might have the older (pre-2017) version of this kit. Skip to the next page for wiring directions.

After cutting, you should have:

- A **three-conductor** (green/yellow/black) data cable with plugs&nbsp;at **both ends** , about 14&nbsp;inches&nbsp;long.
- A **two-conductor** (red/black) power cable with a **wide** &nbsp;plug&nbsp;at **one end** , about 7" long.
- **Five jumper wires** about 6" long, each with a **female** connector at **one end**.

![raspberry_pi_DSC_3454.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/533/medium640/raspberry_pi_DSC_3454.jpg?1487637153)

# Prepare Button

Don’t be confused by the colors here. This sequence is three of the&nbsp; **jumper&nbsp;wires** , <u>not</u> the serial data cable!

Looking at the back of the button, with the pins arranged in a “smile,” the functions from left to right are:

- **LED +**
- **NC** (Normally Closed)
- **NO** (Normally Open)
- **COMMON**
- **LED –**

![raspberry_pi_button1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/515/medium640/raspberry_pi_button1.jpg?1487634589)

Using finger pressure or small pliers (gently!), smoosh the last two pins ( **COMMON** and **LED –** ) close together. We need to loop a single wire through both of them…

![raspberry_pi_button2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/516/medium640/raspberry_pi_button2.jpg?1487634606)

Strip about 3/8" of insulation from the end of three of the jumper&nbsp;wires: **BLACK** , **YELLOW** and **GREEN**. Twist the ends a bit to keep the strands from fraying.  
  
**<u>Do not</u>** do this with the serial data cable! Use the one-sided **jumper&nbsp;wires**.

![raspberry_pi_button3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/517/medium640/raspberry_pi_button3.jpg?1487634623)

Loop the **BLACK** wire through the **LED –** and **COMMON** pins, bend it back on itself and solder.  
  
This is a tight squeeze for the wire, like threading a needle. It may help to turn the wire a bit while passing it through, to keep the strands from fraying. It may take a few tries…you can remove the wire, re-twist it, and try again.

![raspberry_pi_button4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/518/medium640/raspberry_pi_button4.jpg?1487634668)

Repeat with the **GREEN** wire on the **LED +** pin and the **YELLOW** wire on the **NO** (Normally Open) pin.  
  
The **NC** (Normally Closed) pin is **NOT CONNECTED.**

![raspberry_pi_button5.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/519/medium640/raspberry_pi_button5.jpg?1487634684)

Fish the three wires through the button hole on the top case piece, press the button into place and secure with the included nut.  
  
There is no front or back side for the top piece…you can insert the button either way.

![raspberry_pi_button6.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/520/medium640/raspberry_pi_button6.jpg?1487634701)

# Prepare DC Jack
There are three “legs” on the DC jack, but we’ll just be using two of them.  
  
The large center leg corresponds to the power supply tip, which will be +5V.  
  
The “outer” of the two small legs is the power supply ring (ground).  
  
The “inner” small leg is not connected.

![raspberry_pi_dc1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/521/medium640/raspberry_pi_dc1.jpg?1487634774)

Strip about 1/4" insulation from the red and black wires on the power cable and the one-sided jumper&nbsp;wires.

Twist the wires a bit to prevent the strands from fraying.

Twist the two red wires together, feed through the large center leg (+) and solder in place.

![raspberry_pi_dc3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/523/medium640/raspberry_pi_dc3.jpg?1487634839)

Repeat with the two black wires through the “outer” small leg (–).  
  
Remember, the “inner” small leg is <u>not connected</u>.

![raspberry_pi_dc4.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/524/medium640/raspberry_pi_dc4.jpg?1487634853)

Fish the connector and wires through the DC hole on the <u>back</u> piece of the case (this the part with the etched Adafruit logo) and press the jack into place.

Secure the DC jack from the other side with the included nut. You’ll need to fish the wires through this to get it into place.

&nbsp;

Once the jack is in place, solder the 4700uF capacitor to the + and - terminals. This will help keep the voltage stable when the thermal printer is operating.

&nbsp;

&nbsp;

![raspberry_pi_DSC_3450.jpg](https://cdn-learn.adafruit.com/assets/assets/000/039/525/medium640/raspberry_pi_DSC_3450.jpg?1487634945)

![](https://cdn-learn.adafruit.com/assets/assets/000/039/538/medium800/raspberry_pi_DSC_3452.jpg?1487637251)

Danger: 

That’s it for soldering! You can unplug your iron now.

- [Previous Page](https://learn.adafruit.com/pi-thermal-printer/raspberry-pi-software-setup.md)
- [Next Page](https://learn.adafruit.com/pi-thermal-printer/soldering.md)

## Primary Products

### Adafruit IoT Pi Printer Project Pack

[Adafruit IoT Pi Printer Project Pack](https://www.adafruit.com/product/1289)
Build an "Internet of Things" connected mini printer that will do your bidding! This is a fun weekend project that comes with a beautiful laser cut case. Once assembled, the little printer connects wirelessly to get Internet data for printing onto 2 1/4" wide receipt paper....

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1289)
[Related Guides to the Product](https://learn.adafruit.com/products/1289/guides)

## Featured Products

### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### Raspberry Pi - Skill badge, iron-on patch

[Raspberry Pi - Skill badge, iron-on patch](https://www.adafruit.com/product/906)
You are learning to use the small Linux based board, the Raspberry Pi! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many...

In Stock
[Buy Now](https://www.adafruit.com/product/906)
[Related Guides to the Product](https://learn.adafruit.com/products/906/guides)
### Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi

[Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi](https://www.adafruit.com/product/1105)
Now that you've finally got your hands on a [Raspberry Pi®](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi T-Cobbler from Adafruit, which can break out all those tasty...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1105)
[Related Guides to the Product](https://learn.adafruit.com/products/1105/guides)
### Mini Thermal Receipt Printer Starter Pack

[Mini Thermal Receipt Printer Starter Pack](https://www.adafruit.com/product/600)
Hit the ground running (and printing!) with this starter pack that includes a thermal printer and all the extras and save a few dollars while you're at it.  
  
Includes:

- [A mini thermal receipt printer](http://www.adafruit.com/products/597) - with cables and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/600)
[Related Guides to the Product](https://learn.adafruit.com/products/600/guides)
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Rugged Metal Pushbutton with White LED Ring

[Rugged Metal Pushbutton with White LED Ring](https://www.adafruit.com/product/558)
These chrome-plated metal buttons are rugged&nbsp;and look real good while doing it! Simply drill a 16mm hole into any material up to 1/2" thick and you can fit these in place, there's even a rubber gasket to keep water out of the enclosure. On the front of the button is a flat metal...

In Stock
[Buy Now](https://www.adafruit.com/product/558)
[Related Guides to the Product](https://learn.adafruit.com/products/558/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)

## Related Guides

- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Adafruit Raspberry Pi Educational Linux Distro](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [PyPortal IoT Plant Monitor with Google Cloud IoT Core and CircuitPython](https://learn.adafruit.com/pyportal-iot-plant-monitor-with-google-cloud-iot-core-and-circuitpython.md)
- [Adafruit QT Py ESP32-C3 WiFi Dev Board](https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board.md)
- [AstroPrint 3D Printing](https://learn.adafruit.com/astroprint-3d-printing.md)
- [No-Code Rain Sensing Smart Desktop Umbrella Stand](https://learn.adafruit.com/no-code-rain-sensing-smart-desktop-umbrella-stand.md)
- [MacroPad Remote Procedure Calls over USB to Control Home Assistant](https://learn.adafruit.com/macropad-remote-procedure-calls-over-usb-to-control-home-assistant.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
- [Mini Raspberry Pi Handheld Notebook](https://learn.adafruit.com/mini-raspberry-pi-handheld-notebook-palmtop.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [Huzzah Weather Display](https://learn.adafruit.com/huzzah-weather-display.md)
