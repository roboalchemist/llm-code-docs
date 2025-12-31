# Source: https://learn.adafruit.com/mini-thermal-receipt-printer/hacking.md

# Mini Thermal Receipt Printers

## Hacking!

![](https://cdn-learn.adafruit.com/assets/assets/000/025/205/medium800/components_bigprints.jpg?1430762656)

Look at those huge, razor-sharp image prints! You want some?

The following…

- Is an **undocumented** &nbsp;printer feature and is **NOT guaranteed** to work.
- May require&nbsp; **modifying** your printer — a **warranty-voiding** operation! Continue at your own risk.

You should _only_ attempt this if **_all_** of the following apply:

- Have first confirmed that the **printer works as expected** &nbsp;when operated through **conventional procedures**.
- Have a **genuine performance bottleneck** that cannot be adequately resolved by&nbsp; **adjusting the printer** timing and thermal settings first.
- Are comfortable **opening things** and **soldering**.

Danger: 

These printers have a limited serial receive buffer. Push bits to the printer faster than it can physically heat dots and feed paper, and you experience an “overflow” — bitmap images become garbled, text and formatting commands may be skipped.

The thermal printer library tries to throttle data to the printer at just the right rate. Too fast and an overflow occurs. Too slow and it wastes your time; the printer isn’t operating at peak throughput. This is an imperfect process…though we use very conservative timing estimates, the actual speed through the printer is impossible to predict…sometimes overflows _still_ occur.

_Hardware handshaking_ is a means by which a printer or other device can report to the microcontroller that it’s ready to receive more data, virtually eliminating buffer overflows while operating at peak throughput…the paper feed stops only when it physically absolutely must. Optimal performance.

It appears that some varieties of these thermal printers support hardware handshaking (e.g. firmware v2.64, 2.68). This is barely mentioned&nbsp;in the datasheet, and in fact **there isn’t even a physical connection&nbsp;for this on the outside of the printer.** A little surgery is in order…

Primary: 

# Parts and Tools Needed

- Small Phillips head screwdriver
- Pliers
- Soldering iron and related paraphernalia
- A bit&nbsp;of wire…but ideally a female jumper wire

# Procedure
Unplug all cables, turn the printer over and remove the two small Phillips screws.

![components_backscrews.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/207/medium640/components_backscrews.jpg?1430763081)

Take the back plate off, then remove the two (or sometimes four) Phillips screws holding the circuit board in place.

&nbsp;

These screws are a little smaller than the back-holding ones…don’t get them mixed up!

![components_pcbscrews.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/209/medium640/components_pcbscrews.jpg?1430763780)

Carefully, so as not to unseat or unplug the connectors, turn the circuit board over and look for the unpopulated via&nbsp;labeled “DTR.”

&nbsp;

There are some other interesting solder points in here, if you’re so inclined. “HV” is the raw 5–9 Volts from the power supply. On the right is a 3.3V pin, though I don’t know the available current. Conceivably one could bring these out to reduce overall cabling in a project…or even install a tiny microcontroller right inside!

![components_dtrpin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/210/medium640/components_dtrpin.jpg?1430763797)

Cut an end off a female jumper wire and strip & tin the end.

&nbsp;

This will be hanging out of the printer…so a _female_ jumper prevents accidental contact with things if you’re not using the connection. If you only have regular wire, that’s fine, just be careful not to leave a bare&nbsp;end dangling.

![components_cutwire.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/212/medium640/components_cutwire.jpg?1430764324)

Solder the wire to the DTR pad. Top, bottom, doesn’t matter…it’s right up against the serial connection plug, so use whatever path works best for you, there’s ample room for routing the wire around either way.

![components_solderwire.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/214/medium640/components_solderwire.jpg?1430764727)

Language pedants may note that this isn’t technically a DTR pin, but rather CTS.&nbsp;It’s long-standing thing among printer manufacturers…apparently the misnomer was made decades&nbsp;ago but has stuck for consistency.

On the back plate, there’s a small metal “finger” between the serial and power sockets. Using pliers, this can be bent back to provide an exit route&nbsp;for the DTR wire.

![components_finger1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/215/medium640/components_finger1.jpg?1430765440)

![components_finger2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/216/medium640/components_finger2.jpg?1430765478)

Screw the controller board back in place (check that neither of the cables has come unseated), routing the DTR wire around between the two sockets, then screw the back on.

&nbsp;

Finished with the hardware!

![components_close.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/217/medium640/components_close.jpg?1430765650)

You can then reconnect the power and serial sockets, and wire those up as before.

Use a jumper wire to connect DTR to any available Arduino pin. In our examples, we’ll use digital pin 4.

The printer electronics operate&nbsp;at 3.3V (but are “5V safe”), so no level shifting is needed with&nbsp;3.3V boards (Arduino Due, etc.)…this can safely be connected directly.

# Code Changes

Just one line…the Adafruit\_Thermal constructor…needs changing. It can accept an optional parameter, a pin number to use for DTR:

```
Adafruit_Thermal printer(&amp;mySerial, 4);
```

This works just as well with a hardware serial port (e.g. Arduino Mega or Due):

```
Adafruit_Thermal printer(&amp;Serial1, 4);
```

No other changes are necessary. Try this with one of the example sketches…you’ll find the printer is suddenly _lots_ faster! That’s because the software&nbsp;throttle is no longer used…the printer continually reports its actual “ready” state to the microcontroller.

# Printing Huge Images
![](https://cdn-learn.adafruit.com/assets/assets/000/025/225/medium800/components_chrysler.jpg?1430768599)

The printBitmap() function can output images from an open stream or stored in PROGMEM (flash memory)…as explained on the “Printing Bitmaps” page.

Although the Arduino Mega has a whopping 256K flash space, a limitation of the AVR microcontroller is that a single array can’t exceed 32K…that’s about a 384x680 pixel bitmap image. If you try to embed a larger image in your code, the compiler will report an error.

One workaround might be to break really long images into multiple smaller images, and print these out consecutively without a feed() in between.

Another is to use a non-AVR Arduino-compatible board, such as the 32-bit Arduino Due. This has no problem with massive arrays. The&nbsp;Chrysler Building image above is 384x1132 pixels!

# &nbsp;Other Things to Know

This type of printer fares best with light line art and sometimes dithered&nbsp;photographic images as long as the overall dot density is fairly low, like under&nbsp;50%. Large solid-filled areas exhibit strange streaky artifacts…this isn’t a bug of the library or printer firmware, but just a side-effect of how receipt printers operate, that they can only heat so many dots at a time and have to pull shenanigans to&nbsp;go beyond that, else they jam.

Here are a couple examples from fancy commercial receipt printers.

&nbsp;

Notice in the first one that the “solid black” area isn’t _really_ solid black…examining it closely, you can see it’s densely dithered, but not 100% filled.

&nbsp;

The second _does_ have solid fills, but limits the total area. On any given row, only so many pixels are set.

![components_receipt-subway.jpg](https://cdn-learn.adafruit.com/assets/assets/000/025/324/medium640/components_receipt-subway.jpg?1431152828)

![components_receipt-lucky.gif](https://cdn-learn.adafruit.com/assets/assets/000/025/325/medium640thumb/components_receipt-lucky.jpg?1448318087)

If you try to print a “dense” image and the paper jams (image gets squashed vertically), pass a lower density value to printer.begin(). Default value is 120. So for example:

```
printer.begin(80);
```

DTR support is not a panacaea. **Glitches occasionally do&nbsp;still happen** …sometimes overflows, sometimes “framing errors” with serial data. But overall it seems fairly reliable and _buttery smooth!_

- [Previous Page](https://learn.adafruit.com/mini-thermal-receipt-printer/troubleshooting.md)

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
