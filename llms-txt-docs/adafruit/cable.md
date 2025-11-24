# Source: https://learn.adafruit.com/electroknit/cable.md

# Electro-knit

## Cable

 **Make your own cable**

The kh930e is designed to work with a Tandy PDD1 floppy drive. We don't need it! Make your own cable to communicate between your computer and the machine. You will need:

- [FTDI cable](http://www.adafruit.com/index.php?main_page=product_info&cPath=18&products_id=70&zenid=08edecd591934eebcc4993c01b0259d6) - you should be able to use a '3.3v' or '5v' cable. 
- 2x4 connector part number [WM8036-ND on Digikey](http://search.digikey.com/scripts/DkSearch/dksus.dll?vendor=0&keywords=WM8036-ND) 

You will need to make some minor mods to get the cable talking to your knitting machine. Follow the tutorial to get your knitting cable going.

**Change 'polarity' of the FTDI cable**

 

FTDI cables have standard 'inverted' TTL (zero is 3-5V and one is 0v) but the KH930E requires the opposite. Luckily its very easy to fix this by reprogramming the software.

You will need a copy of [FTDI MProg](http://www.ftdichip.com/Resources/Utilities.htm "Link: http://www.ftdichip.com/Resources/Utilities.htm") (windows only) and your FTDI cable. Plug in the FTDI cable into your windows computer and [install the driver that matches your computer best](http://www.ftdichip.com/Drivers/VCP.htm "Link: http://www.ftdichip.com/Drivers/VCP.htm")

 For Windows users, [http://www.ftdichip.com/Drivers/CDM/CDM%202.08.28%20WHQL%20Certified.zip](http://www.ftdichip.com/Drivers/CDM/CDM%202.08.28%20WHQL%20Certified.zip "Link: http://www.ftdichip.com/Drivers/CDM/CDM%202.08.28%20WHQL%20Certified.zip") is the best choice  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/749/medium800/braincrafts_fetch.php.jpg?1396765527)

[Please read our detailed tutorial on installing the driver here](http://learn.adafruit.com/ftdi-friend) then come back when the driver is installed

Now download [FTDI MProg](http://www.ftdichip.com/Resources/Utilities.htm) (Search for MProg in the page, v3.5 was the latest version last we checked) and run the program

![](https://cdn-learn.adafruit.com/assets/assets/000/000/750/medium800/braincrafts_mprog.gif?1447976412)

Select **Scan…** from the menu

![](https://cdn-learn.adafruit.com/assets/assets/000/000/751/medium800/braincrafts_mprogscan.gif?1447976423)

The message window should say it found a cable.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/752/medium800/braincrafts_mprogscanned.gif?1447976431)

Now select **Read and Parse** to read in the cable programming.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/753/medium800/braincrafts_mprogread.gif?1447976438)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/754/medium800/braincrafts_mprogparsed.gif?1447976446)

Click the buttons that say to **Invert TX and RX**.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/755/medium800/braincrafts_mprogsignals.gif?1447976454)

Here is the wierd thing, you have to **Save as…** the settings so just save it anywhere.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/756/medium800/braincrafts_mprogsave.gif?1447976462)

Now you can click the **Program** button (lightening bolt).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/757/medium800/braincrafts_mprogprog.gif?1447976469)

The message window will say it programmed.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/758/medium800/braincrafts_mprogged.gif?1447976477)

You're done! Quit Mprog.  
  
**Rewire the connector**

Next we need to rewire the FTDI cable to match the pinout of the knitter. The cable comes with a 1x5 connector, but we need a 2x4 connector. You can also follow [Davi Post's excellent rendition of this cable-rewiring](http://daviworks.com/knitting/cable_tutorial.html "Link: http://daviworks.com/knitting/cable\_tutorial.html") section.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/759/medium800/braincrafts_propcablestart.jpg?1396765630)

Use tweezers to lift up the black connector tabs.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/760/medium800/braincrafts_propcableremovewire.jpeg?1396765637)

Then gently pull out the wire.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/761/medium800/braincrafts_propcablepullout.jpg?1396765644)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/762/medium800/braincrafts_propcableremoved.jpg?1396765652)

Repeat for all the wires.

You'll want to cut away a few inches of the black cable sheathing so you have plenty of 'space' to work with the wires. Cut **down** the sheathing without cutting the colored wires, use a fine scissors. Cut 1 or 2" away.

Now grab the 2x8 cable connector you bought from Digikey or whatever. You'll need to insert the wires so that they snap into the connector to match the following diagram. **Do not insert the red or green wires yet!!!** Insert just the orange and yellow wires. Look at the photos below to make sure you have the wires in the right order, they should just snap in. If they don't snap make sure the little lock-tab is facing 'out'

This diagram assumes you're looking at the connector from the end that goes into the machine. Again, check with the photos many times to be sure you get this right!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/763/medium800/braincrafts_connbott-adafruit-kmt.png?1396765671)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/764/medium800/braincrafts_conntop-adafruit-kmt.png?1396765687)

Pin 1 is black, pin 2 will be red, pin 3 will be green, pin 6 is orange, and pin 7 is yellow.

Next is the one tough part, you'll want to cut the green wire as close as you can to the black sheathing. Use the piece of green wire to branch off from the red wire by stripping a small opening in the red sheathing and soldering the green wire on. This produces one wire with two header inserts - red and green. See the following image:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/765/medium800/braincrafts_cablesplice_t.jpg?1396765695)

Wrap it up in electrical tape or heatshrink:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/766/medium800/braincrafts_cablewrapped_t.jpg?1396765695)

You're done!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/767/medium800/braincrafts_cabledone_t.jpg?1396765698)

 **TODO** : We're pretty sure its possible to make this part less difficult by using the RTS (green) wire without splicing it to the 5V (red) wire and using setRTS() in the python code but we already mangled the cable before trying this. If you try and succeed, please post up in the [forums](http://adafruit.com/forums/)!

- [Previous Page](https://learn.adafruit.com/electroknit/overview.md)
- [Next Page](https://learn.adafruit.com/electroknit/software.md)

## Featured Products

### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [Firework Ignitor](https://learn.adafruit.com/electric-ignitor.md)
- [Fruit Jam Chyron](https://learn.adafruit.com/fruit-jam-chyron.md)
- [Walkmellotron: Cassette Player Mods](https://learn.adafruit.com/walkmellotron.md)
- [Build your own BeBox and run BeOS using Virtualbox](https://learn.adafruit.com/build-a-bebox-with-beos-and-virtualbox.md)
- [BLE Sniffer with nRF52840](https://learn.adafruit.com/ble-sniffer-with-nrf52840.md)
- [Commodore 64 - The Most Popular Retro Computer of All Time](https://learn.adafruit.com/commodore-64-retro-guide.md)
- [Modifying Servos for Continuous Rotation](https://learn.adafruit.com/modifying-servos-for-continuous-rotation.md)
- [Convert your Model M Keyboard to Bluetooth with Bluefruit EZ-Key HID](https://learn.adafruit.com/convert-your-model-m-keyboard-to-bluetooth-with-bluefruit-ez-key-hid.md)
- [PlayStation Spinner Controller](https://learn.adafruit.com/playstation-spinner-controller.md)
- [Pico Four Keypad](https://learn.adafruit.com/pico-four-key-macropad.md)
- [BlueLive: Livestream Studio switcher controller](https://learn.adafruit.com/bluelive.md)
- [Compiling a cross-compiler on Windows](https://learn.adafruit.com/compiling-a-cross-compiler-on-windows.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [Android Smart Home Mirror](https://learn.adafruit.com/android-smart-home-mirror.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
