# Source: https://learn.adafruit.com/mini-thermal-receipt-printer/making-connections.md

# Mini Thermal Receipt Printers

## Making Connections

These printers might see use with **microcontrollers** or with Linux-based computers such as **Raspberry Pi**. The **Tiny** printer has the distinct option of connecting to a Raspberry Pi’s **USB** port, covered later on this page. But to start, let’s talk about&nbsp;_ **TTL serial** _—the non-USB connection present across _all_ of these printers.

## TTL Serial

Most microcontrollers can provide a 3.3V or 5V _TTL serial connection_. It’s not&nbsp;same as the 10V RS232 serial from a computer’s 9-pin serial port — don’t connect the printer directly to a standard PC port or you may damage it. A&nbsp;_USB-to-serial cable_&nbsp;(such as those made by FTDI, or similar) is an option on Linux PCs, but most will be using it with a microcontroller.

It **makes no difference** if the controller is a **5 Volt** or **3.3 Volt** device. The printer logic is 3.3V, but “5V tolerant,” meaning **no extra level-shifting circuitry is needed** in either direction. Some older documentation may still show a _voltage divider_ (two resistors and some extra wires), but that’s since been found unnecessary. The printer and 5V _or_ 3.3V devices can connect directly.

To start, we’ll connect to the data cable of the printer. Easiest is to simply press breadboard jumper wires into the data plug, then use those to extend the connection to the host: an Arduino or other microcontroller, Raspberry Pi, or USB-to-serial cable.

If the controller is on a **breadboard** or the **socket headers** along the edges of an Arduino Uno-like board, or with most **USB-to-serial** cables: **male/male** jumper wires are suitable.

If the controller is a **Raspberry Pi** : use **female/male** jumper wires to the Pi’s GPIO header.

The **wire color for each pin** is **_not_ the same** across all these printers. Please read the descriptions carefully.&nbsp;It’s _nice_ (but not _mandatory_) to match jumper wire colors to the printer’s data cable, to help keep track of things.

![](https://cdn-learn.adafruit.com/assets/assets/000/117/148/medium800/components_jumper-to-socket.jpg?1671212407)

## For Product #597: “Mini”

The **Mini** printer data cable has three wires:

- Black =&nbsp; **GROUND** reference
- Yellow = data **IN** to the printer (RX)
- Green = data **OUT** of the printer (TX)

This is in addition to the separate power cable, described on the prior page.

## For Product #2751: “Tiny”

The **Tiny** printer data cable has **five** wires:

- Red =&nbsp; **GROUND** (yes, red, and yes this totally is the opposite of common electronics conventions)
- Green = data **IN** to the printer (RX)
- Blue = data **OUT** of the printer (TX)
- Yellow (DTR) and black can be left **unconnected**

This is in addition to the separate power cable, described on the prior page.

## For Product #2752: “Nano”

The&nbsp; **Nano** printer cable has **five** wires and _no_&nbsp;separate power cable.

- Black = power _and_ signal&nbsp; **GROUND**
- Blue = data **IN** to the printer (RX)
- Green = data **OUT** of the printer (TX)
- Red = 5–9V DC power
- Yellow = DTR, can be left unconnected for now

Power and data share a single connector here. Ground must go to _both_ the power supply _and_ the microcontroller, meaning you’ll need a split here, perhaps using a breadboard’s power rail.

## For Product #2753: “Guts”

The **Printer Guts** &nbsp;cable has **five** wires and no separate power cable.

Some printers have a color-coded cable, while others have&nbsp;just have a plain white cable. Unplug this temporarily from the printer and you should find the pin functions **labeled on the PCB** :

![](https://cdn-learn.adafruit.com/assets/assets/000/029/179/medium800/components_2753-04.jpg?1450470643)

The pin order here is **not the same** as the Tiny or Nano printers. And if you have both Guts and Nano printers, be _super careful_ about the wiring, because the plugs are interchangeable but the sequence of wires and colors (if any) _do not_ have the same functions!

- **VH** = 5–9V DC power
- **GND** = power _and_ signal&nbsp; **GROUND**
- **RX** on the PCB&nbsp;= data **IN** to the printer
- **TX** on the PCB&nbsp;= data **OUT** of the printer
- **DTR** on the PCB = can leave unconnected for now

As with the Nano printer, power and data share a single connector. Ground must go to _both_ the power supply _and_ the microcontroller, meaning you’ll need a split here, perhaps using a breadboard’s power rail.

## To Arduino
For a board like the **Arduino Uno** , the other end of the jumper wires can insert into the **board edge sockets**. For smaller devices on a&nbsp; **breadboard** , insert into the corresponding **contact strip**.

**Ground** from the printer always connects to **GND** on the microcontroller board. For the data wires ( **TX** and **RX** ), which pins to connect to can vary by hardware and software, explained further on subsequent pages. Some situations may require specific pins, but you can usually use any two pins.&nbsp;Here’s the printer’s TX line connected to digital pin 5, and RX to digital pin 6:

![](https://cdn-learn.adafruit.com/assets/assets/000/117/149/medium800/components_jumpers-to-arduino.jpg?1671212539)

Warning: 

## To Raspberry Pi
Before connecting any **TTL serial** printers to **Raspberry Pi** , it’s _vitally important_ to perform a little **system configuration** first.

The Raspberry Pi board has a TTL serial connection on the GPIO breakout header. By default, it’s configured for a _serial console_ — connected to a terminal, this provides another way to log into the system (along with Ethernet, WiFi or keyboard+monitor).&nbsp;We need to **turn off** the serial console behavior, or a connected printer will just spit out endless gibberish! This only applies to a **TTL serial** connection; **Tiny** printers using **USB** , or others when using a&nbsp; **USB-to-serial** adapter, don’t need this step.

If using a **desktop** OS (mouse and GUI), it’s just a few clicks.&nbsp;From the “Pi” menu at the top left, select **Preferences→Raspberry Pi Configuration…**

Select the **Interfaces** tab.

Turn **Serial Port _ON_** _,_ and **Serial Console _OFF_** _,_ as shown in the image.

Click the “ **OK** ” button, then “ **Yes** ” when asked whether to reboot

![components_pi_a___b___2__3_pi-config.png](https://cdn-learn.adafruit.com/assets/assets/000/117/154/medium640/components_pi_a___b___2__3_pi-config.png?1671214340)

![components_pi_a___b___2__3_pi-config-serial.png](https://cdn-learn.adafruit.com/assets/assets/000/117/155/medium640/components_pi_a___b___2__3_pi-config-serial.png?1671214353)

If a “ **lite** ” OS (text login), this is done from the command line:

```terminal
sudo raspi-config
```

You’ll find the Serial Port settings under “ **Interface Options**.” Select “ **No** ” for the login shell, and “ **Yes** ” if asked about the serial port hardware (this option might not show up on older Pi models, where it’s always on). Tab over to “ **Finish** ” and reboot when asked.

_Now_ the printer can be connected without making a mess.

The diagram at left shows the Pi’s GPIO header. For orientation reference, the 5V pin at the top right is nearest the corner of the board.

TX and TXD mean the same thing: _transmit_ or _transmit data._ Likewise with RX and RXD. The terms might get used interchangeably.

![components_raspberry_pi_gpio-diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/117/151/medium640/components_raspberry_pi_gpio-diagram.png?1671212601)

 **TX** and **RX** from the printer go to specific GPIO pins with _opposite_ functions. TX to RX and RX to TX, known as a _crossover_ configuration:

![](https://cdn-learn.adafruit.com/assets/assets/000/117/150/medium800/components_printer-to-pi.png?1671212562)

Really you can use _any_&nbsp;GND shown in the pinout diagram above. The third pin is easy to locate, but that spot’s sometimes occupied by other hardware like small cooling fans.

If you happen to be using the **Mini** printer with the 3-pin data cable, and if the Pi and printer are kept close together, you might not even need jumper wires. Skip the first two 5V pins on the GPIO header, and the data cable can press right on to the next 3 pins in sequence: GND, TX and RX.

![components_pi_a___b___2__3_pi-printer-to-header.jpg](https://cdn-learn.adafruit.com/assets/assets/000/117/152/medium640/components_pi_a___b___2__3_pi-printer-to-header.jpg?1671212621)

## To USB-to-Serial Cable (FTDI, etc.)
The principle here is similar to Raspberry Pi above: create a _crossover_&nbsp;by connecting the printer’s TX to the adapter cable’s RX pin, RX to TX, and ground to ground.

The diagram here is representative, not literal. Some adapter cables might have this pinout, but others will not. FTDI cables, for example, usually have a 6-pin header with its own color code; only 3 pins are needed here. You’ll find pin functions and colors in the specific cable’s documentation.

![](https://cdn-learn.adafruit.com/assets/assets/000/117/153/medium800/components_printer-to-ftdi.png?1671212643)

Any of these cables will require _device driver_ software. Popular ones (FTDI, Prolific, etc.) might already be present on Linux systems. Check documentation.

Also, _how_ the device manifests when connected to a computer’s USB port will vary among manufacturers and drivers. In Linux it might show as `/dev/tty.USBserial` (followed by a number), but other conventions are sometimes used.&nbsp;Skim through the `/dev` directory and/or try the `lsusb` command to help identify the device.

## “Tiny” Printer: USB to Linux (Raspberry Pi, etc.)

The **Tiny** printer has the lovely option of connecting via USB cable, no jumper wires needed. On Raspberry Pi, there’s _no need_ to change anything with raspi-config…but there _are_ some things to know about the system.

On current Tiny printers, and on earlier ones _when suitably configured,_ the printer appears to the system as **/dev/usb/lp0** &nbsp;and operates through the _USB printing subsystem._ Sometimes there will be a different number at the end, if more printers are attached.

On earlier Tiny printers, the factory configuration instead has it appear as **/dev/ttyUSB0** , which mimics a Prolific _USB-to-serial bridge.&nbsp;_Sometimes there will be a different number at the end, if other USB-to-serial devices are attached.

Any software or commands that want to issue data to the printer should speak to the appropriate device name (try `ls /dev` from the command line to see what’s present, or try `lsusb`). Project code will often have the system device name in a global variable somewhere. Aside from that difference, they should both function the same; open the device, issue data, printer prints it.

If you have an older Tiny printer (defaulting to _USB-to-serial bridge_) and specifically _require_ USB printing subsystem compatibility instead, there’s a way to switch it over:

1. Similar to the self-test, **hold** the **paper feed button** while applying power…but now&nbsp;_ **keep holding it.** _
2. After the QR code, the current USB mode is printed: this will either be **COM** (USB-to-serial mode, the default) or **Printable Port** (USB printing subsystem).
3. **Release** the paper feed button.
4. To **keep** the current setting, **tap** the paper feed button once more.
5. To **change** to to the opposite USB setting (COM or Printable Port), **hold** the feed button for at least **2 seconds**. The printer will confirm the change.

![](https://cdn-learn.adafruit.com/assets/assets/000/117/145/medium800/components_printer_mode_change.jpg?1671161191)

This is present only&nbsp;in older Tiny printers. Current units work strictly in USB printing subsystem mode—it’s considered more modern—and continuing to hold the paper feed button will just eject a lot of paper…so don’t.

- [Previous Page](https://learn.adafruit.com/mini-thermal-receipt-printer/first-test.md)
- [Next Page](https://learn.adafruit.com/mini-thermal-receipt-printer/microcontroller.md)

## Primary Products

### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Tiny Thermal Receipt Printer - TTL Serial / USB

[Tiny Thermal Receipt Printer - TTL Serial / USB](https://www.adafruit.com/product/2751)
Add a _really small_ printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2751)
[Related Guides to the Product](https://learn.adafruit.com/products/2751/guides)
### Nano Thermal Receipt Printer - TTL Serial

[Nano Thermal Receipt Printer - TTL Serial](https://www.adafruit.com/product/2752)
Add a _really really small_ printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2752)
[Related Guides to the Product](https://learn.adafruit.com/products/2752/guides)
### Thermal Receipt Printer Guts

[Thermal Receipt Printer Guts](https://www.adafruit.com/product/2753)
Add printing capability to any microcontroller project with **just the innards of a thermal printer.** Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into a...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2753)
[Related Guides to the Product](https://learn.adafruit.com/products/2753/guides)

## Featured Products

### Mini Thermal Receipt Printer Starter Pack

[Mini Thermal Receipt Printer Starter Pack](https://www.adafruit.com/product/600)
Hit the ground running (and printing!) with this starter pack that includes a thermal printer and all the extras and save a few dollars while you're at it.  
  
Includes:

- [A mini thermal receipt printer](http://www.adafruit.com/products/597) - with cables and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/600)
[Related Guides to the Product](https://learn.adafruit.com/products/600/guides)
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
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Thermal Paper Roll - 33' long, 2.25"

[Thermal Paper Roll - 33' long, 2.25"](https://www.adafruit.com/product/2754)
A little roll of thermal paper! This fits very nicely into our&nbsp;[Tiny Thermal Receipt Printer](https://www.adafruit.com/products/2751). It's ~2.25" wide (about 57mm) and 33 feet long or about 10 meters.

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2754)
[Related Guides to the Product](https://learn.adafruit.com/products/2754/guides)
### Thermal Paper Roll - 16' long, 2.25"

[Thermal Paper Roll - 16' long, 2.25"](https://www.adafruit.com/product/2755)
A little roll of thermal paper! This fits very nicely into our [Nano Thermal Receipt Printer](https://www.adafruit.com/products/2752). It's ~2.25" wide (about 57mm) and 16 feet long or about 5 meters.

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/2755)
[Related Guides to the Product](https://learn.adafruit.com/products/2755/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Breadboarding wire bundle

[Breadboarding wire bundle](https://www.adafruit.com/product/153)
75 flexible stranded core wires with stiff ends molded on in red, orange, yellow, green, blue, brown, black and white. These are a major improvement over the "box of bent wires" that are sometimes sold with breadboards, and faster than stripping your own solid core wires. Makes...

In Stock
[Buy Now](https://www.adafruit.com/product/153)
[Related Guides to the Product](https://learn.adafruit.com/products/153/guides)

## Related Guides

- [How to Find Hidden COM Ports](https://learn.adafruit.com/how-to-find-hidden-com-ports.md)
- [Wireless Game Show Poppers for the Classroom!](https://learn.adafruit.com/wireless-game-show-poppers.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [RGB LED Matrix Basics](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix.md)
- [Analog Feedback Servos](https://learn.adafruit.com/analog-feedback-servos.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [Silicone Robo-Tentacle](https://learn.adafruit.com/silicone-robo-tentacle.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [Metal Inlay Capacitive Touch Buttons](https://learn.adafruit.com/metal-inlay-capacitive-touch-buttons.md)
- [Adafruit IO Basics: NeoPixel Controller](https://learn.adafruit.com/adafruit-io-basics-neopixel-controller.md)
- [Adafruit PN532 RFID/NFC Breakout and Shield](https://learn.adafruit.com/adafruit-pn532-rfid-nfc.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Adafruit INA219 Current Sensor Breakout](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout.md)
- [All About Arduino Libraries](https://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use.md)
