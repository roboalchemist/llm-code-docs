# Source: https://learn.sparkfun.com/tutorials/nest-protect-teardown

## \"Safety Shouldn't Be Annoying\"

\...So goes the tagline for the Nest Protect smoke and CO detector. This clever little device replaces your existing smoke detector with the promise of keeping you safer and better informed. To achieve this, the Nest Protect connects to your home WiFi connection as well as any other Nest devices you own, such as smoke detectors or thermostats. Not only is it massively connected, but it\'s much more aware of the surrounding environment than your old smoke detector: ambient light, motion, humidity and temperature are all monitored and used to assess danger.

[![Nest Protect](https://cdn.sparkfun.com/r/600-600/assets/f/1/5/8/9/52cd7919ce395fc93e8b456b.jpg)](https://cdn.sparkfun.com/assets/f/1/5/8/9/52cd7919ce395fc93e8b456b.jpg)

This might all sound like too much automation for a simple smoke detector (in some cases it may well be), but, whether or not you want one in your house, you have to admit that the Nest Protect is an impressive piece of hardware and we couldn\'t wait to tear into it to find out what makes it tick!

## Breaking In

Flip the device over you\'ll notice there are a few interesting things that stand out. First, I\'ve never owned a smoke alarm with a USB port. Also, there don\'t seem to be any hidden screws, probably because you actually have to remove this back cover in order to change the batteries. So step one was to pop out those screws, and get the cover off.

[![Teardown pic 1](https://cdn.sparkfun.com/r/500-500/assets/e/1/1/a/1/52cdc94cce395fbe4c8b4569.jpg)](https://cdn.sparkfun.com/assets/e/1/1/a/1/52cdc94cce395fbe4c8b4569.jpg)

Popping the cover and removing the batteries reveals some kind of 4-position connector as well as the detection chamber for the optical smoke sensor. You can also see a finger switch that, according to the back cover, will erase all settings. More importantly, though, there are more screws! At this point I have to express my delight that Nest has chosen not to use some silly tamper resistant fasteners or hidden all the screws under warranty stickers.

[![Teardown pic 2](https://cdn.sparkfun.com/r/500-500/assets/0/4/7/a/3/52cdca98ce395fcc4f8b4567.jpg)](https://cdn.sparkfun.com/assets/0/4/7/a/3/52cdca98ce395fcc4f8b4567.jpg)

That said, pulling those screws didn\'t actually help until I pried the main board out of the enclosure. This is where all of the action is, so we\'ll be coming back to it after we\'ve stripped everything else out of the case. With the main board out of the way, the battery holder still wasn\'t going to budge without first removing the speaker. The speaker is connected to the enclosure with a single screw and connected to the main board by a fragile little 2-position connector.

[![Teardown Pic 3](https://cdn.sparkfun.com/r/500-500/assets/5/2/8/8/9/52f43f3fce395fcc238b4568.jpg)](https://cdn.sparkfun.com/assets/5/2/8/8/9/52f43f3fce395fcc238b4568.jpg)

With the speaker removed, the battery holder popped right out leaving just the Nest button at the front of the enclosure. It took some prying, but the plastic cover on the front of the button did eventually come off revealing that, not only is it an attractive design feature, but it\'s also a [Fresnel lens](http://en.wikipedia.org/wiki/Fresnel_lens)! It may be opaque to visible light but it\'s perfect for the underlying PIR sensor.

[![Teardown pic 4](https://cdn.sparkfun.com/r/500-500/assets/8/f/d/0/b/52cdca98ce395f974a8b456b.jpg)](https://cdn.sparkfun.com/assets/8/f/d/0/b/52cdca98ce395f974a8b456b.jpg)

The flex-board that holds the PIR sensor as well as the RGB LEDs and button switch for the \"Nest\" button is glued to the plastic housing, but some gentle prying will free it.

[![Teardown pic 5](https://cdn.sparkfun.com/r/500-500/assets/8/2/4/4/e/52cdca98ce395f0b448b4568.jpg)](https://cdn.sparkfun.com/assets/8/2/4/4/e/52cdca98ce395f0b448b4568.jpg)

Alright, now that we\'ve separated the parts let\'s see what we\'re dealing with:

[![All Parts Spread Out](https://cdn.sparkfun.com/r/600-600/assets/8/8/d/8/d/52cd791bce395f673f8b4567.jpg)](https://cdn.sparkfun.com/assets/8/8/d/8/d/52cd791bce395f673f8b4567.jpg)

Behold! The Nest Protect in all its naked glory! Now that we\'re in, let\'s take a closer look at the construction\...

## Clever Enclosure Tricks

Before looking at the electronic bits let\'s take a moment to admire the very clever engineering that went into this enclosure. I\'ve broken it up into a few features that I admire and that contribute to both the form and functionality of the device.

### Ventilation

Packing everything into a fairly standard size for a smoke detector is hard enough when all it does is beep. This full blown computer has to fit in the same space as your old smoke detector and still allow for smoke to get in behind the dense brick of electronic gizmos inside. This was achieved through a combination of PCB and enclosure layout. First of all, in order to save space, the Nest Protect uses a custom made photoelectric smoke detector that\'s built through a hole in the PCB. This allows the electrical part of the sensor to sit on the \"sensor side\" of the board while the detection chamber sits on the ceiling side. By building through the board, they save some vertical space as well, which keeps the device slim.

The other thing you\'ll notice is that the ceiling side of the device is vented along the perimeter and a series of baffles, molded into the back panel, direct air into the detection chamber without allowing the mounting tabs to disrupt the flow. A smoke detector only works, after all, if the smoke can get in.

### Invisible Sensors

Despite being loaded with sensors the Nest Protect has somehow avoided looking like some sort of advanced spy drone. In fact, to look at the face of the Protect, you\'d be forgiven for wondering how it\'s supposed to work at all. It sort of looks like an intercom speaker with a page button in the middle, but behind that friendly perforated exterior is a small army of components that need to see through to the outside world.

The way that the PCB fits into the front panel of the Protect is really slick. Just behind the grill there\'s a plastic baffle that directs input to all of the sensors. Sandwiched between the grill and this baffle there\'s a fine mesh that keeps dust out of the circuits but allows CO to get into the detector as well as sound to get out from the speaker.

The plastic sensor baffle couples to a pair of ultrasonic transducers presumably to avoid weird echos from inside the enclosure interfering with their operation. There\'s also a light pipe that focuses the ambient light from outside the unit directly onto the on-board light sensor. This baffle also supports what I call the \"Button Spider\", a portion of the plastic that floats on thin plastic legs and allows you to push the central button while taking some of the mechanical stress off of the switch itself. Actually, that gets its own paragraph\...

### Button Spider

While this is technically the same piece of plastic as the baffle, it displays some of its own cleverness. By joining the LED ring to the actual plastic button piece this part contributes significantly to the Protect\'s [HAL9000-esque](http://en.wikipedia.org/wiki/HAL_9000) appearance. The \'Nest\' button snaps into place on the front face of the spider, which houses the LED ring electronics behind it. A system of fins are molded in to keep the button from deforming as you push it (although a little bit of give seems to have been left intentionally as it makes the button feel friendlier). These fins also lock the flexPCB in place so that it can\'t rotate and free itself from the tacky glue that secures it to the spider. Finally, the inside face of the spider has a feature that keeps the switch in place on the backside of the button. Oh yeah, the spider has one more feature, it maintains the proper spacing between the PIR sensor and a part so cool that I gave it a German compound word: Die Objektivtaste.

### \"Die Objektivtaste\"

Or \"Lensbutton\" in English (also a made-up word), is the button cover that\'s visible from the front of the unit. This rubberized plastic disc makes the pushbutton switch attractive, displays the brand name of the device, and is the visual focal point of the design. Ironically, besides being a visual focal point, it\'s also a lens. I know, you\'re thinking, \"That\'s no lens! I can\'t see through it!,\" and you\'re right, you probably can\'t. However, the PIR sensor behind it has no such trouble. Removing the lens-button from the device and flipping it over reveals a Fresnel lens configuration molded into the plastic. It\'s pretty kaleidoscopic, really, to look at your own reflection in it. You\'ll recognize that configuration and the milky white color from other PIR/lens modules, like [this one](https://www.sparkfun.com/products/8630)!

### Cool Speaker

I really want to find a source for these speaker modules. It\'s just a plastic speaker in a little plastic box, and it\'s great! It sounds much bigger than it is (a function of the plastic enclosure), but that also has a lot to do with the fact that the sound and speech effects are probably tailored to the frequency response of this admittedly somewhat plastic-sounding speaker. Let this be a lesson: 50% of any speaker is the box you put it in!

### Custom Photoelectric Detector

As I mentioned before, the photoelectric smoke detector in the Protect appears to be something they designed for this unit and not an off-the-shelf device. It\'s comprised of two plastic pieces: one of which houses an emitter/detector pair and the other, which acts as the optical chamber. These devices work by projecting a beam of light into a chamber and past a detector. When there\'s no smoke, the light sails right by, but when there\'s smoke present, it scatters some portion of light into the detector. This is a part that needs to meet rigorous standards as a safety device, and the temptation would be to buy a monolithic device that they know operates to code and just pop it into their design. Designing their own to save space? Good move.

## Sensor Scavenger Hunt

Now we return to the main board to hunt down all of the sensors that one might expect in a device like this. Somehow, the Nest Protect needs to know the following:

- Is there smoke in the room? (obviously)
- Is there CO in the room? (obviously)
- Is there someone standing below me? (\"Pathlight\" feature)
- Is there someone waving at me? (\"Heads Up\" feature)
- Is the light on? (\"Nightly Promise\" feature)

The Amazon listing for this product actually has a summary of the sensor package, which claims that the Protect boasts the following sensors:

- Photoelectric smoke sensor
- Carbon monoxide sensor
- Heat sensor
- Three activity sensors (A little vague, but okay)
- Ambient sensor (You know, to sense the ambiance)

So all-in-all, we should find enough embedded devices to account for the functionality above. That and at least one controller to wrangle all that data. Oh yeah, and at least one radio to get to The Internets.

Proper shielding is important to the good folks at Nest\... apparently. This board has so many little shields on it that they might as well have just wrapped it in foil. Using a small, flat-head screw driver, I popped all of the shielding off like unwrapping a tiny, FCC compliant Christmas presents. And much like Christmas morning, it was a positive overall experience peppered with moments of confusion and delight. Behold:

[![Mainboard](https://cdn.sparkfun.com/r/500-500/assets/a/c/2/0/e/52f43f45ce395f8e448b4567.jpg)](https://cdn.sparkfun.com/assets/a/c/2/0/e/52f43f45ce395f8e448b4567.jpg)

### Controllers and Radio ICs

Let\'s start with the biggest package on the board and work our way around counter-clockwise:

[![Kinetis K60](https://cdn.sparkfun.com/r/300-300/assets/6/c/2/e/c/52f44b04ce395f5c7a8b4567.jpg)](https://cdn.sparkfun.com/assets/6/c/2/e/c/52f44b04ce395f5c7a8b4567.jpg)

*You\'re up first, big guy.*

If I had to guess, based purely on the number of pins, this is the brains of the operation. Google tells me that what we\'re looking at here is a [Freescale Kinetis K60](https://cdn.sparkfun.com/assets/c/c/8/e/d/52a8c005757b7f4b738b456c.pdf), a 32-bit ARM Cortex based MCU that boasts a bunch of peripherals including USB and Ethernet. The part number indicates a flash size of 512K but they seem to have augmented that with a chunk of discrete memory on the side.

[![EM357](https://cdn.sparkfun.com/r/300-300/assets/3/d/4/3/1/52f44b06ce395f440c8b4567.jpg)](https://cdn.sparkfun.com/assets/3/d/4/3/1/52f44b06ce395f440c8b4567.jpg)

*I see a crystal and an antenna. This is a radio.*

The two miniature rf connectors in this corner of the board hint at the presence of two separate radios, a dynamic duo of which the EM357 is half. The [EM357](https://cdn.sparkfun.com/assets/5/7/7/1/b/52a8c007757b7f75218b4569.pdf) is a ZigBee radio SoC featuring a 32-bit ARM Cortex processor, 2.4GHz transceiver, and a bunch of GPIO. Hold on, though, I thought this thing was supposed to connect to my WiFi so what is this ZigBee radio for? If you remember our [Nest thermostat teardown](https://www.sparkfun.com/tutorials/334), you may remember Nate discovering a ZigBee radio in that product as well, so we expected to see this. ZigBee not only allows the Nest products to talk to eachother, but it leaves the door open for them to communicate with future home automation products. Aside from being a popular public-band standard, ZigBee also has no trouble co-existing with WiFi. That reminds me\...

[![Type ZX](https://cdn.sparkfun.com/r/300-300/assets/b/5/f/3/3/52f44b04ce395f347d8b4567.jpg)](https://cdn.sparkfun.com/assets/b/5/f/3/3/52f44b04ce395f347d8b4567.jpg)

*Moar Radio*

Ah yes, the WiFi radio! What we\'re looking at here is the [muRata Type ZX WiFi Module](http://www.murata-ws.com/products/spec_sheet.php?type=Type%20ZX%202.4GHz%20Wi-Fi%20802.11b/g/n&record=30), a b/g/n WiFi module with built-in Broadcom chipset, crystal, RF filter, and passives. Not bad considering its only 7mm on its longest side. Doesn\'t look like a datasheet is available unless you\'re a MuRata Direct customer, so that\'s about all we know on this one.

[![K16](https://cdn.sparkfun.com/r/300-300/assets/8/e/7/d/6/52f44b03ce395f09778b4568.jpg)](https://cdn.sparkfun.com/assets/8/e/7/d/6/52f44b03ce395f09778b4568.jpg)

*You aren\'t trying to hide from me are you?*

For those of you counting, this is the third ARM Cortex core we\'ve crossed paths with during this teardown. This time it\'s buried in another Freescale MCU, specifically the [Freescale K16](https://cdn.sparkfun.com/assets/9/7/d/1/6/52a8c006757b7f692f8b4568.pdf). I wouldn\'t venture to guess what this MCU\'s job is. It is located close to the piezo alarm and critical sensors, so perhaps it handles the critical safety functions separate from the \"convenience\" functions.

### Sensors

But wait, aren\'t there supposed to be a bunch of sensors on this thing? Where are they all hiding? Time to flip this thing over and check out the other side. Starting from the CO detector tube and moving clockwise this time:

[![Figaro CO](https://cdn.sparkfun.com/r/300-300/assets/9/3/f/5/a/52f44b04ce395f3a2b8b4568.jpg)](https://cdn.sparkfun.com/assets/9/3/f/5/a/52f44b04ce395f3a2b8b4568.jpg)

*This thing could save your life?*

Here\'s a boring looking component that could warn you of an invisible threat\... no, not ninjas, carbon monoxide poisoning! Removing the shielding reveals that this component is a [Figaro TGS-5342 CO Sensor](https://cdn.sparkfun.com/assets/8/4/3/e/f/52a8c005757b7f292e8b456c.pdf), an electrochemical detector from the Japanese company Figaro Engineering Inc. I won\'t confirm by cutting it open, but this thing might be full of sulfuric acid! Cool, huh? It turns out that electrochemical CO detectors are actually fuel cells that use CO as the fuel. The CO is oxidized to CO2 at one end, oxygen is consumed at the other, and a current is produced. The amount of current produced is proportional to the concentration of CO in the cell making it not only capable of signaling the presence of monoxide but also of quantifying it.

[![Piezo](https://cdn.sparkfun.com/r/300-300/assets/e/4/6/f/f/52f44b03ce395fb0778b4568.jpg)](https://cdn.sparkfun.com/assets/e/4/6/f/f/52f44b03ce395fb0778b4568.jpg)

*Loud things come in small packages*

This is your standard, run-of-the-mill piezoelectric siren. These things are loud, like, ear-damaging loud. They\'re also a commodity part, and there\'s nothing really special about this one. I had to search the patent number on the device just to find some basic specs on it, but you can buy these anywhere.

[![Light Sensor](https://cdn.sparkfun.com/r/300-300/assets/3/a/1/b/5/52f44b01ce395fa23d8b4567.jpg)](https://cdn.sparkfun.com/assets/3/a/1/b/5/52f44b01ce395fa23d8b4567.jpg)

*I know what it is but I don\'t think there\'s a part number on it\...*

Like trying to identify a robber from the blurry bank security footage, trying to track down the manufacturer of this light sensor was a long and arduous process with no luck. I can\'t give you any specs on this part except to say that it\'s tiny, appears to have 6 pins, and may or may not be a color light detector.

[![Ultrasonic Transducer](https://cdn.sparkfun.com/r/300-300/assets/2/b/f/5/9/52f44b00ce395fcc798b4569.jpg)](https://cdn.sparkfun.com/assets/2/b/f/5/9/52f44b00ce395fcc798b4569.jpg)

*These guys look [familiar](https://www.sparkfun.com/products/8502)*

Ah yes, the telltale shape of an ultrasonic transducer. I suppose these guys are used to determine whether or not you\'re waving at the unit because the PIR sensor probably doesn\'t work particularly well for that. It is odd that it has both, though. I wasn\'t able to identify who makes these, so I\'m not certain what the beam width is supposed to be. Safe to say, it has something to do with either the \"Pathlight\" or \"Heads Up\" features. It\'s a handy device to have on board if they ever want to upgrade the firmware and add interactivity.

[![SHT20](https://cdn.sparkfun.com/r/300-300/assets/f/0/7/5/7/52f44afece395f82758b4567.jpg)](https://cdn.sparkfun.com/assets/f/0/7/5/7/52f44afece395f82758b4567.jpg)

*These guys also look [familiar](https://www.sparkfun.com/products/8227)*

Well if it isn\'t our old friend the SHT20. We carry a breakout board for another device in this same family. We love these, and they\'re everywhere. Small, cheap, and reliable. I\'m not sure whether the temp and humidity data help determine the presence of a threat, calibrate other sensors, or if it\'s simply good data to have when you\'re making a peripheral device for a thermostat. Having temp and humidity in several rooms throughout your house accessible by the same computer that controls your HVAC? That could allow for some cool features.

[![Photoelectric Smoke Detector](https://cdn.sparkfun.com/r/300-300/assets/0/3/5/c/c/52f44b04ce395f847a8b456a.jpg)](https://cdn.sparkfun.com/assets/0/3/5/c/c/52f44b04ce395f847a8b456a.jpg)

*Oooooh. Ahhhhh.*

This is the photoelectric smoke detector that I was talking about earlier. Because it\'s a custom part there\'s no datasheet available, and it would be very hard to identify the emitter/detector pair that they\'ve used. I only mention it here as part of the sensor package, but I\'m afraid it is among the few components on this board that lead very private lives.

[![PIR](https://cdn.sparkfun.com/r/300-300/assets/f/6/0/6/0/52f44affce395f3c0a8b4569.jpg)](https://cdn.sparkfun.com/assets/f/6/0/6/0/52f44affce395f3c0a8b4569.jpg)

*I\'m afraid I can\'t do that.*

Like staring into the eye of a cold and uncaring machine, except this cold and uncaring machine could save your family from a house fire. The PIR sesnsor doesn\'t have any identifying markings but wins the award for most cleverly mounted device. Well done, PIR, well done indeed.

## Datasheet Roundup 

[![All Parts Laid Out](https://cdn.sparkfun.com/r/600-600/assets/8/8/d/8/d/52cd791bce395f673f8b4567.jpg)](https://cdn.sparkfun.com/assets/8/8/d/8/d/52cd791bce395f673f8b4567.jpg)

Here\'s a list of the datasheets and product pages that I was able to pull together in case you want more information on any of the parts that go into the Protect. Not every device had identifying markings, and, even then, some of them weren\'t well documented. These should cover most of the more exotic parts, though:

- [Freescale Kinetis K60](https://cdn.sparkfun.com/assets/c/c/8/e/d/52a8c005757b7f4b738b456c.pdf)
- [Freescale K16](https://cdn.sparkfun.com/assets/9/7/d/1/6/52a8c006757b7f692f8b4568.pdf)
- [EM357 ZigBee SoC](https://cdn.sparkfun.com/assets/5/7/7/1/b/52a8c007757b7f75218b4569.pdf)
- [Figaro TGS-5342 CO Sensor](https://cdn.sparkfun.com/assets/8/4/3/e/f/52a8c005757b7f292e8b456c.pdf)
- [muRata Type ZX WiFi Module](http://www.murata-ws.com/products/spec_sheet.php?type=Type%20ZX%202.4GHz%20Wi-Fi%20802.11b/g/n&record=30)
- [Passive IR Sensor](http://epled-2008.en.made-in-china.com/product/DbZEXIchQCVw/China-Passive-Infared-PIR-Sensor.html)

I hope you enjoyed this teardown. This is just another great example of how amazingly inexpensive computers have become. This smoke detector undoubtedly has thousands of times the amount of processing power as the computers that landed us on the moon\... And considering my habit of leaving the soldering iron on at home, that\'s probably a good thing.