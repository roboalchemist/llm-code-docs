# Source: https://learn.sparkfun.com/tutorials/rfid-basics

## Introduction

A few months ago I checked out a stack of books at our local library by placing the books on a kiosk. All 5 books magically appeared on the computer screen. Around the same time my father ran in the [Bolder Boulder](http://www.bolderboulder.com/), a foot race of over 50,000 people. An electronic system kept track of his time and thousands of others by only having the runners wear paper race bibs. Pets that are found wandering can be identified and returned to their owners with a basic scan of the neck. How is all of this possible?

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/RFID_Tag-104.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/RFID_Tag-104.png)

*Source: [icons8](https://icons8.com/web-app/2354/rfid-tag)*

The answer is [RFID](https://www.sparkfun.com/rfid) or **R**adio **F**requency **ID**entification. This tutorial will cover the basics of how RFID works, and will help guide you towards getting started with RFID.

### Suggested Reading

If you aren\'t familiar with the following concepts, check out these tutorials before continuing. They will help with the basic understanding of RFID.

- [The Basics of Binary](https://sparkle.internal.sparkfun.com/sparkle/learn_tutorials/30#tab-attributes)
- [What is a Battery?](https://sparkle.internal.sparkfun.com/sparkle/learn_tutorials/508#tab-attributes)
- [Electric Power](https://sparkle.internal.sparkfun.com/sparkle/learn_tutorials/72#tab-attributes)

## Basics

### Basic Functionality

It may be tempting to believe that RFID functions thanks to the reader module containing a very small hamster with x-ray eyes, but in actuality, the system is a bit simpler than that.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfidoesnt.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfidoesnt.jpg)

*How RFID doesn\'t work*

RFID uses radio waves produced by a **reader** to detect the presence of (then read the data stored on) an RFID **tag**. Tags are embedded in small items like cards, [buttons](https://www.sparkfun.com/products/9417), or [tiny capsules](https://www.sparkfun.com/products/9416).

[![RFID System](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfid_works.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/2/8/rfid_works.png)

*Image courtesy of [EPC RFID](http://www.epc-rfid.info/rfid)*

These readers also use radio waves in some systems to write new information to the tags.

## Types of RFID Systems

There are two types of RFID systems: passive or active. The tag power system defines which type of system it is.

### Passive

In a passive RFID system, the tags do not use a battery; instead, they receive their energy to run from the reader. The reader emits an energy field of a few feet, providing the energy for any tag in the vicinity. The tag gathers the electromagnetic energy from the card reader, powers up, and responds with 'hello world' and its identification information.

Passive tags have the benefit of being able to be read at a fast rate (10 or more times a second). They are extremely thin (allowing them to be placed between layers of paper) and are extremely cheap (less than \$0.05 in 10,000+pcs volumes).

[![Pile of passive RFID tags](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/RFID_tags.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/RFID_tags.jpg)

*In general, the smaller the tag the much shorter the read range*

### Active

Active RFID systems include tags that have their own internal power supply for increased range. Active tags possess a battery and usually have larger SMD components. After a preset amount of time the tag emits an RF \'*chirp*\'. A reader in the vicinity can listen and hear for this chirp. Because an active tag is they can be read over much larger distances than passive tags (tens of feet).

Downsides to active tags include greater bulk (because of the battery), limited life span (tag is dead when the battery is exhausted), increased cost per tag, and varying report rates.

[![m130 Active RFID Tag](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/rf_code_m130assettaginside.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/3/rf_code_m130assettaginside.png)

*m130 Active RFID asset tag from [RF Code](http://www.rfcode.com/)*

## RFID Frequencies

As well as active and passive systems, RFID systems can also be broken out into different frequencies.

Some frequencies and systems are designed to only read one tag at a time, while others can read multiple. Cost of readers can also vary wildly based the frequency rating of the modules. In prior years a reader capable of reading multiple tags was in the thousands of dollars, sometimes tens of thousands. These systems were unattainable for most hobbyists and prototypers. However, this is finally beginning to change, and multi-read capable readers are becoming much more affordable.

Check out the following chart for a basic break down of the frequencies, and their associated properties.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A Few Common RFID Reader Types                                                                                                                                                                                                                                                                                    |
+=============================================+========================================================================================================================================================+========================+=======================+===================================+=======================+
| Frequency                                   | AKA                                                                                                                                                    | Range                  | Read/Write            | Read Multiple Tags Simultaneously | Average Tag Cost      |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+-----------------------------------+-----------------------+
| Low Frequency (120-150 kHz)                 | [\"Chips/microchips\" (in veterinary applications)](http://en.wikipedia.org/wiki/Microchip_implant_(animal)), prox cards, HID cards (both trade names) | Up to 20 cm/ \< 1 foot | Read Only             | No                                | \$0.50                |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+-----------------------------------+-----------------------+
| High Frequency (13.56 MHz)                  | MiFare, NFC                                                                                                                                            | Up to 1 meter          | Read/write            | No                                | \$1                   |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+-----------------------------------+-----------------------+
| Ultra High Frequency (433 MHz, 860-920 MHz) | Long-range RFID, powered RFID                                                                                                                          | Up to 100 meters       | Read/write            | Yes                               | \$0.05                |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+-----------------------------------+-----------------------+
| Information from [Wikipedia: Radio-frequency identification](http://en.wikipedia.org/wiki/Radio-frequency_identification)                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Tag Memory

RFID tags store a lot of data in their memory - that\'s what makes them so useful. While there can be many different types of identifying information stored in tags (which can vary from industry to industry), the majority of that is beyond the scope of this tutorial. You can find more detailed information on tag storage requirements from the [Tag Data Standard](http://www.gs1.org/epc/tag-data-standard), and the [Tag Data Translation Standard](http://www.gs1.org/epc/tag-data-translation-standard).

Some RFID tags (like the ubiquitous \"HID ProxCard II\" brand ID card and some brands of pet tag) use a **proprietary format**. School IDs and other cards from commercial access control systems may not work with all RFID readers.

### Gen2 UHF RFID Memory Standard

The [v2.0.1 standard](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/3/Gen2_Protocol_Standard.pdf) written by EPCglobal covers all RFID requirements for Gen2 RFID tags. Generally speaking, the memory of a tag is split into three: the TID, EPC, and User Memory.

#### Tag Identifier Memory

The TID or Tag Identifier is 20 bytes or 160 bits. These means there are 1,460,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 different possible tag IDs (1.46 \* 10^48^). More than there are atoms in the human body! Not quite the number of [atoms in the universe](https://en.wikipedia.org/wiki/Observable_universe#Matter_content). Every RFID tag has a unique TID. The TID is not editable.

#### Electronic Product Code Memory

While TIDs are good for absolute identification the Gen2 RFID standard was really created to replace the barcode in many retail environments. When you go to buy your groceries the register doesn\'t care if you have item TID 0xE242F3, it cares if you have a gallon of milk or a jar of peanut butter. That\'s where the Electronic Product Code (EPC) comes in: it\'s generally 12 bytes, user editable, and meant to be written to as a UPC type replacement. Slap an RFID tag on the gallon of milk, program the tag\'s EPC to be `0 7874203641 0` and the register will identify it as a half-gallon of Lactose Free 1% Low Fat Milk made by Great Value ([random source](http://www.health.state.mn.us/wic/vendor/fpchng/upc/download/milkpdf.cfm)). The tag doesn\'t care what you write to those 12 bytes so writing ASCII `RufusTheDog` is perfectly acceptable but keep it below 12 bytes.

#### User Memory

The size of User Memory can vary from 0 bytes to 64 bytes. The cheaper the tag the fewer bytes of user memory it will likely have. What do you do with 64 bytes? To continue with the gallon-of-milk analogy, user memory was originally intended to record things like expiration dates. The EPC is the global identifier (\'this is milk\'), and the User Memory was specific to that gallon (\'sell by August 15th\'). Again, the tag doesn\'t care so consider recording user setting data (this user enjoys a 10 degree decline in the pilot seat) or use the memory as the world\'s smallest [dead drop](https://en.wikipedia.org/wiki/Dead_drop).

#### Passwords

There are additional writable memory locations called the Access password and Kill password. The Access password can be used to prevent people from re-configuring tags (\"it may look like a sirloin steak but the register says it\'s a pack of gum\...\"). The Kill password is used to permanently and irrevocably disable a tag.

## Troubleshooting

Depending on the enclosure and environment you are operating an RFID system in, you may run into functionality issues with the readers not accurately reading or writing data from a tag. Here are a few pointers to keep in mind that may help improve your system\'s functionality.

- **Avoid RF Interference** - Any other RF-emmiting devices in the area of your system may negatively affect the performance of an RFID system, especially if they operate in the same band. Having multiple RFID readers near each other can cause system interference
- **Use a clean power supply** - Like most electronic systems, noisy and/or dirty power supplies can cause strange behavior in an RFID system. Clean, regulated power sources are recommended.
- **Check for line of site** - Open-air readings without other objects obstructing the line-of-site between the reader and the tag can improve outputs.
- **Use an external antenna** - This can improve read range for all systems. Onboard antennas are limited in power and range.
- **Stop Holding Tags (UHF systems)** - Humans are basically bags of water. If you hold the tag in your hand you\'ll degrade the range for reading significantly. Instead, tape the tag to a non-metal, non-watery device.
- **Change tag types** - Typically, the smaller the tag, the shorter the read range. If you are using a glass capsule, try a button. If you\'re using a button, try a card.

## Purchasing an RFID System

RFID kits, readers, and tags can all help define or expand your projects. If you\'re looking for one to get started with, these are some of the options available.

[![RFID Tag - ABS Token MIFARE Classic® 1K (13.56 MHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/3/9/2/10127-01.jpg)](https://www.sparkfun.com/rfid-tag-abs-token-mifare-classicr-1k-13-56-mhz.html)

### [RFID Tag - ABS Token MIFARE Classic® 1K (13.56 MHz)](https://www.sparkfun.com/rfid-tag-abs-token-mifare-classicr-1k-13-56-mhz.html) 

[ SEN-10127 ]

This is a basic RFID tag that functions within the MIFARE Classic® 1K guidelines. You can use these for all sorts of identif...

[ [\$3.75] ]

[![RFID Tag - Transparent MIFARE Classic® 1K (13.56 MHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/3/9/4/10128-01.jpg)](https://www.sparkfun.com/rfid-tag-transparent-mifare-classicr-1k-13-56-mhz.html)

### [RFID Tag - Transparent MIFARE Classic® 1K (13.56 MHz)](https://www.sparkfun.com/rfid-tag-transparent-mifare-classicr-1k-13-56-mhz.html) 

[ SEN-10128 ]

This is a basic RFID tag that functions within the MIFARE Classic® 1K guidelines. You can use these for all sorts of identif...

[ [\$3.75] ]

[![RFID Reader ID-12LA (125 kHz)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/8/7/11827-01.jpg)](https://www.sparkfun.com/rfid-reader-id-12la-125-khz.html)

### [RFID Reader ID-12LA (125 kHz)](https://www.sparkfun.com/rfid-reader-id-12la-125-khz.html) 

[ SEN-11827 ]

RFID (radio-frequency identification) is the wireless non-contact use of radio-frequency electromagnetic fields, for the purp...

[ [\$32.50] ]

[![SparkFun RFID Reader Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/2/7/13030-01.jpg)](https://www.sparkfun.com/sparkfun-rfid-reader-breakout.html)

### [SparkFun RFID Reader Breakout](https://www.sparkfun.com/sparkfun-rfid-reader-breakout.html) 

[ SEN-13030 ]

This is a simple breakout board for our RFID readers. The SparkFun RFID Reader Breakout converts the 2mm pins to bread board ...

[ [\$3.50] ]

[![UHF RFID Antenna (RP-TNC)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/2/8/14131-02a.jpg)](https://www.sparkfun.com/uhf-rfid-antenna-rp-tnc.html)

### [UHF RFID Antenna (RP-TNC)](https://www.sparkfun.com/uhf-rfid-antenna-rp-tnc.html) 

[ WRL-14131 ]

This is your solution when you absolutely, positively need to get the most out of an antenna for your next RFID project. This...

[ [\$48.50] ]

[![SparkFun RFID Qwiic Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/4/0/15209-SparkFun_RFID_Qwiic_Kit-01a.jpg)](https://www.sparkfun.com/sparkfun-rfid-qwiic-kit.html)

### [SparkFun RFID Qwiic Kit](https://www.sparkfun.com/sparkfun-rfid-qwiic-kit.html) 

[ KIT-15209 ]

The SparkFun RFID Qwiic Kit is a simple, yet all-in-one I2C based RFID starting point for the ID-3LA, ID-12LA, and ID-20LA re...

[ [\$49.95] ]

[![SparkFun Simultaneous RFID Reader - M7E Hecto](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/0/6/2/WRL-24738-Simultaneous-RFID-Reader-Feature.jpg)](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m7e-hecto.html)

### [SparkFun Simultaneous RFID Reader - M7E Hecto](https://www.sparkfun.com/sparkfun-simultaneous-rfid-reader-m7e-hecto.html) 

[ WRL-24738 ]

The SparkFun M7E Hecto Simultaneous RFID Reader simplifies reading UHF RFID tags (EPCglobal Gen 2) with its powerful M7E-HECT...

[ [\$309.95] ]

[![ThingMagic M7e UHF RAIN RFID Module](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/0/6/3/24936-RFID-Module-M7E-Hecto-Feature.jpg)](https://www.sparkfun.com/thingmagic-m7e-uhf-rain-rfid-module.html)

### [ThingMagic M7e UHF RAIN RFID Module](https://www.sparkfun.com/thingmagic-m7e-uhf-rain-rfid-module.html) 

[ WRL-24936 ]

The M7E-Hecto is a UHF RFID RAIN module allowing for the simultaneous reading of up to 300 tags per second.

[ [\$199.95] ]