# Source: https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved

## Introduction

In this tutorial, we will guide you through how to make your very own jukebox. This project is intended to be used for toddlers, but can also serve as a great learning tool for any future audio or [RFID](https://www.sparkfun.com/rfid) projects. It is [Qwiic-based](https://www.sparkfun.com/qwiic), and so does not require soldering. For an overview of the project, please check out the following video:

**Attention:** If you plan to build the optional [Crafty Binary Cards](https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved#crafty-binary-cards-optional) feature, then you will need additional materials and tools. You will also want to review some additional literature. For more information, see the [Crafty Binary Cards (Optional)](https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved#crafty-binary-cards-optional) section below.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** If you plan to build this up without any soldering, you will want to use some of our [alligator to pig-tail connectors](https://www.sparkfun.com/products/13191). These will connect from the terminals on the buttons to the IO female headers on the RedBoard Qwiic. Some of the pictures in this tutorial have the button connections made with wires soldered directly to the button terminals. This is because mine were used in a previous project. Alligator to header-pin connectors will work just the same.

### Tools

Wiring up the electronics actually requires no tools at all, but depending on what you decide to do for your enclosure, you may need some general crafting tools. These could include scissors, hobby knife, Velcro tape, Scotch tape, and hot glue.

Although in this tutorial we will be showing a custom enclosure (with bent acrylic and a faceplate), the jukebox could very easily be housed in a cardboard box.

### Suggested Reading

You are more than welcome to jump right into this project and learn from the code provided here, but if you\'d like to do some reading and/or prototyping ahead of time, it couldn\'t hurt to check out the products involved and their individual hookup guides. Also, if this is your first time working with Arduino, we highly recommend checking out the [Installing Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide/all) to get you up and running.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/rfid-basics)

### RFID Basics 

Dive into the basics of Radio Frequency Identification (RFID) technology.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

[](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-rfid-idxxla-hookup-guide)

### SparkFun Qwiic RFID-IDXXLA Hookup Guide 

The Qwiic RFID ID-XXLA is an I2C solution that pairs with the ID-LA modules: ID-3LA, the ID-12LA, or the ID-20LA, and utilizes 125kHz RFID chips. Let\'s take a look at the hardware used for this tutorial.

[](https://learn.sparkfun.com/tutorials/qwiic-mp3-trigger-hookup-guide)

### Qwiic MP3 Trigger Hookup Guide 

Playing MP3s has never been easier.

## Hardware Overview

Since, this system only uses [Qwiic boards](https://www.sparkfun.com/Qwiic), it\'s really quite simple to plug everything together. The pictures below, show how everything should be plugged in. The [RedBoard Qwiic](https://www.sparkfun.com/products/15123), [MP3 trigger](https://www.sparkfun.com/products/15165), and [RFID reader](https://www.sparkfun.com/products/15209) all have Qwiic connectors (the small black connectors with four pins) for a solderless project. The buttons will require a bit more of precision (plugging into the correct pins on the RedBoard Qwiic), but we will go into that with more detail in the next section.

[![Back of project](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-07.jpg)\
*Back of project enclosure. (Click to enlarge.)*

[![Hardware connections](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-10.jpg)\
*Hardward connections. (Click to enlarge.)*

\
The Qwiic connectors and cables are polarized, so you don\'t have to worry about plugging in a cable backwards. The Qwiic boards can also be plugged in any order, they just need to daisy-chained together. This is handy as you may want a different order of connections depending on how your enclosure and faceplate are setup.

**Note:** You will notice that most [Qwiic boards](https://www.sparkfun.com/categories/399) have two connectors, which allows for daisy chaining; however, the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) board just has one. This is because the RedBoard Qwiic is the \"main brain\" of the project, so it is the *head* of the chain.

### Buttons

The buttons need to be wired up to specific pins on the Arduino. These [arcade buttons](https://www.sparkfun.com/products/9336) are actually made up of two parts. There is the large mechanical button that you press and then there is the electrical switch, which can be removed.

[![button assembly](https://cdn.sparkfun.com/r/400-200/assets/learn_tutorials/6/4/5/09336-2MicroSwitch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/09336-2MicroSwitch.png)\
*Button assembly. (Click to enlarge)*

[![part seperation](https://cdn.sparkfun.com/r/400-200/assets/learn_tutorials/6/4/5/Exp2_Step7bHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Exp2_Step7bHookup.jpg)\
*Removing switch from assembly. (Click to enlarge)*

\
Above you can see the electrical switch removed from the larger housing. We need to connect the buttons to each Arduino pin as listed in the tables below. (***COM** stands for **common** and **NO** stands for **normally open**.*)

**Button one (PLAY):**

  Button terminals   Arduino pins
  ------------------ --------------
  NO                 A0
  COM                GND

**Button two (STOP/PAUSE):**

  Button terminals   Arduino pins
  ------------------ --------------
  NO                 A2
  COM                GND

[![Close up of electrical switch](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-12.jpg)\
*Close up of electrical switch. (Click to enlarge)*

[![Wiring to RedBoard](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-11.jpg)\
*Wiring to RedBoard. (Click to enlarge)*

\
Here, I\'ve got some buttons pre-soldered. They were from a previous project. If you\'re comfortable soldering, then go ahead and solder it up! If you\'d like to create this project without any soldering (and potentially involve the toddler a bit more), it can be done with our [alligator to \"pig-tail\" cables](https://www.sparkfun.com/products/13191).

[![pigtail connections](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-13.jpg)

*Wiring with the alternative, solderless, option. (Click to enlarge)*

You could also pull off this project with a single button, and change the functionality to just PLAY/PAUSE. The current code provided here uses the STOP button for two purposes. A single press of the STOP button will do just that, stop the track. But a double-press of the STOP button will PAUSE the track. Normally, the pause and play functions are tied to the same button, but this was a design choice my toddler made.

### Power options

You have two options: Barrel jack or microB USB.

[![power options](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/15123-SparkFun_RedBoard_Qwiic-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/15123-SparkFun_RedBoard_Qwiic-04.jpg)

In the wish list above, we have included a [USB wall adapter](https://www.sparkfun.com/products/11456) and a [USB cable](https://www.sparkfun.com/products/10215). This is nice because this cable can be used for programming and then also power. If you have a cell phone charger (with **USB micro-B** type connector), this would work fine too for simply powering after programming.

Speaking of power, the hamburger speaker get\'s about 3 hours of play time on each charge. If you\'d like to avoid having to re-charge, you can leave this permanently plugged into a **USB Mini-B** type connector and additional [USB wall adapter](https://www.sparkfun.com/products/11456).

## The Enclosure

A lot of my projects end up in some size of a cardboard red box, but for this one, I actually had an enclosure from a previous project sitting in my basement.

[![the enclosure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-01.jpg)

The jukebox project enclosure.

### Shaping the Acrylic

As I was walking this project into the office, the first thing people asked me was, \"Did you bend that acrylic?\" Yep. It\'s actually not as difficult as it may seem. It requires a heating element strip that can be a little pricey. I believe the one we had at SparkFun was something similar to [this](https://www.tapplastics.com/product/supplies_tools/plastic_tools_supplies/free_standing_heaters/291).

The process is relatively simple, it involves planning your bend points. Then, you lay the acrylic piece on top of the heating element strip for a few minutes and it starts to get soft. If you hear crackling and see bubbles, then you\'ve heated it too long.

**Note:** A pro tip I learned from our mech shop guru, if you hold the angle you want and then use compressed air directly on the bend, you can cool it down very quickly and get a good angle. Otherwise you will need a jig of sorts to hold it for 10 or more minutes while it cools down.\
\
I\'d be curious if anyone reading has attempted to make their own heating element similar to this (or has any ideas on how to do it DIY). Please [comment](https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved/discuss) below. From all of the interest I have seen with this enclosure, I\'m sure a cheaper DIY option would be very popular.

### The Wooden Frame

For my enclosure, I opted to have wood sides. It makes for a nice finished look (without any screws or bolts showing). I used a hand router to make some channels where the edge of the bend acrylic would \"press\" into the side of my wood sides. Some great [info on hand routing here](https://www.instructables.com/lesson/Hand-Router/).

If you had a CNC machinelike the [Shapeoko XXL](https://www.instructables.com/lesson/Hand-Router/), you could design the route and get a much cleaner cut. To do it by hand, I layed my bent acrylic on it\'s side (on top of the wood), traced it, then slowly guided the router along the trace.

[![shot of imperfections](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-08.jpg)\
*Imperfections on the inner cut. (Click to enlarge.)*

[![epoxy bead](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-09.jpg)\
*Frame glued with epoxy. (Click to enlarge.)*

\
In the picture on the left, you can see how my route isn\'t perfectly straight, but ultimately the small imperfections will not be noticed. After a quick stain on the wood and a couple sprays of poly, the final step is to fill the route with a bead of epoxy and slide the acrylic into place (pictured on right).

### The Faceplate

I opted to have a removable faceplate, so that I could have better access to the electronics during development and eventually re-purpose this enclosure for various projects. I\'m so glad I did, because it worked perfectly for this jukebox project.

[![backside of faceplate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-15.jpg)

*The backside of the faceplate. (Click to enlarge)*

## Arduino Library 

**Note:** This guide assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The easiest way to install the required Arduino library is by clicking on the link at the top of the code. This will launch library manager. Then click \"install\".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/mp3librarylink.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/mp3librarylink.png)

You can also open library manager and search for **SparkFun MP3 Trigger**. And lastly, to manually install, head on over to the [MP3 GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_MP3_Trigger_Arduino_Library) or feel free to download the library below:

[SparkFun Qwiic MP3 Trigger Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_MP3_Trigger_Arduino_Library/archive/master.zip)

There is no library required for the RFID reader. However, if you would like, you can download the [firmware and example files](https://github.com/sparkfun/SparkFun_Qwiic_RFID_ID-XXLA/tree/master/Firmware/Arduino_Examples) from the [Qwiic RFID GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_RFID_ID-XXLA/tree/master/Firmware/Arduino_Examples).

## Arduino Code

All of the Arduino code necessary for this project lives in a GitHub repository here:

[GitHub Repo with Arduino Code](https://github.com/lewispg228/qwiic_jukebox)

Once you have your hardware all plugged in, follow these steps to get your jukebox up and running:

1.  Download the code from the [GitHub project repository](https://github.com/lewispg228/qwiic_jukebox).
2.  [Install the Arduino Library for Qwiic MP3](https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved#arduino-library).
3.  Upload the project sketches to your RedBoard Qwiic. There should be 3 tabs open in the Arduino IDE; one for each of project sketches.

    ::: 
    [![file tabs in arduino ide](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Tabs.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Tabs.PNG)
    :::

    ::: 
    *Project file tabs in Arduino IDE.*
    :::
4.  [Open a terminal](https://learn.sparkfun.com/tutorials/terminal-basics) at **115200 bps** and listen to debug messages.
5.  Determine each of your RFID tags\' IDs, by holding each tag up to the reader and watching the serial monitor.
6.  Update the `tagList[]` in the `rfidControl.ino` sketch.

    ::: 
    [![sketch with updated tag ids](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/8/8/7/taglistupdate.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/taglistupdate.png)
    :::

    ::: 
    *`rfidControl.ino` sketch updated with the RFID tag IDs. (Click to enlarge)*
    :::
7.  Upload your modified code.
8.  [Prepare your μSD card](https://learn.sparkfun.com/tutorials/build-a-qwiic-jukebox-that-is-toddler-approved#preparing-the-usd-card) with the MP3 files.

The bones of this code come from these two examples: [Qwiic MP3 Trigger: Example 1](https://github.com/sparkfun/SparkFun_Qwiic_MP3_Trigger_Arduino_Library/blob/master/examples/Example1-PlaySong/Example1-PlaySong.ino) and the [Qwiic RFID: Example 1](https://github.com/sparkfun/SparkFun_Qwiic_RFID_ID-XXLA/blob/master/Firmware/Arduino_Examples/Example1_ReadTag/Example1_ReadTag.ino).

The main `loop()`, in the project sketch, basically does three things:

1.  Checks for new tags (either from the RFID or the IR crafty card reader). Updates active track if necessary.
2.  Checks **PLAY** button. Commands Qwiic MP3 board to play if pressed.
3.  Checks **STOP** button. Commands Qwiic MP3 board as necessary. Note, this also waits to see a second \"tap\" indicating the user wants **PAUSE**.

**Note:** The provided code in the repository does need to be modified in order to work. It will also need to know your RFID tags\' IDs. If you listen on a terminal, it will tell you when a new tag is present and print out the unique ID.

## Preparing the uSD card

In order for your jukebox to play any songs or audio books, you will need to load up the micro SD card with some MP3 files. The most important thing to do here is name them correctly; the files must be named `F000.mp3`, `F001.mp3`, `F002.mp3`, and so forth. For more info, see our [Qwiic MP3 Trigger Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-mp3-trigger-hookup-guide).

[![files on SD card](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/files.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/files.png)

*An example of files listed on an SD card.*

**Note:** Make sure that these are the only files on the μSD card in order for the MP3 trigger to find them.

The `tagList[]`, mentioned in the previous section, is where the RFID tags\' IDs are linked to the MP3 files you want to play. This array of strings is located in the `rfidControl.ino` file, within the GitHub project repository. When using the Arduino IDE, it should be available as a tab (see image above).

[![list of tag and file association](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/tagtomp3file.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/tagtomp3file.png)

*A list of RFID tag and MP3 file associations from the `tagList[]` string array in the `rfidControl.ino` file.*

The first spot in this list is actually spot [0]. It is used to identify when there are no RFID tags present, and so we need to leave that in there. The second spot is actually spot [1] and the tag ID `850764172190` will cause the file `F001.mp3` to be queued when that tag is present at the RFID reader.

## Crafty Binary Cards (Optional)

In this section, we will show you how to build a \"crafty card reader\". But first, we would like to stress the fact that this is *optional*. The original project was designed with all qwiic boards and will work as is. If you\'d like to add in a crafty card reader, then read on.

Note, the code provided in the github repo will work with either type of card reader (Qwiic RFID or crafty binary). In fact, you can have both types of readers plugged in and the code will still work.

[![CardBoard Enclosure with IR Reader](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-02.jpg)

The crafty card reader uses four [IR readers](https://www.sparkfun.com/products/9454) facing upwards to look at the cards pattern of black and white squares.

[![Exposed sensors with spacer layer removed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-03.jpg)\
*Exposed sensors. (Click to enlarge.)*

[![Backside showing soldering](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-04.jpg)\
*Backside with exposed soldering. (Click to enlarge.)*

\

As shown above, it does require a fair amount of soldering. I opted to wire it up on one of our [solderable bread board prototyping PCBs](https://www.sparkfun.com/products/12070). These sensors do a good job at sensing black or white surfaces. They are often used in \"line following\" applications (like in some of our [redbot tutorials](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-redbot/experiment-6-line-following-with-ir-sensors)).

[![Button side of crafty cards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-21.jpg)\
*Bottom side of crafty cards. (Click to enlarge.)*

[![six more examples card stickers](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/8/7/Enginursday_-_Jukebox-22.jpg)\
*Six card \"stickers\". (Click to enlarge.)*

\

On the left are a couple finished crafty cards. On the right are some more example \"stickers\" that could be used to make more cards. A black box will be read as a \"cleared\" or \"zero\" bit, and a white box will be read as a \"set\" or \"one\" bit.

Turns out these readers change dramatically with distance. They work great as line followers on a robot because they are usually at a very consistent distance from the floor surface. Well, with my card reader idea, my cards were not holding position so perfectly inside the reader box. Luckily, I was able to add a little more cardboard and make sort of a \"wedge\" inside the reader. This held the input cards at a more consistent distance from the IR readers. They were basically touching the readers, but that turned out okay!

### Additional Tools and Materials:

\
\

[![SparkFun Solder-able Breadboard](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/7/7/12070-01.jpg)](https://www.sparkfun.com/sparkfun-solder-able-breadboard.html)

### [SparkFun Solder-able Breadboard](https://www.sparkfun.com/sparkfun-solder-able-breadboard.html) 

[ PRT-12070 ]

This is the SparkFun Solderable Breadboard. A bare PCB that is the exact size as our regular breadboard with the same connect...

[ [\$6.95] ]

[![Hook-up Wire - Black (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/2/08022-01.jpg)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html)

### [Hook-up Wire - Black (22 AWG)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html) 

[ PRT-08022 ]

Standard 22 AWG solid Black hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$3.25] ]

[![SparkFun Line Sensor Breakout - QRE1113 (Digital)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/1/5/0/09454-01b.jpg)](https://www.sparkfun.com/sparkfun-line-sensor-breakout-qre1113-digital.html)

### [SparkFun Line Sensor Breakout - QRE1113 (Digital)](https://www.sparkfun.com/sparkfun-line-sensor-breakout-qre1113-digital.html) 

[ ROB-09454 ]

This version of the QRE1113 breakout board features a digital output, using a capacitor discharge circuit to measure the amou...

[ [\$4.50] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Additional Reading:

You will also want to review the following tutorials as well.\
\

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

### Wiring

In order to wire up your crafty IR card reader, you will need to review the circuit for the IR sensor. The [product page](https://www.sparkfun.com/products/9454) and [bildr tutorial](https://web.archive.org/web/20160304200751/http://bildr.org/2011/06/qre1113-arduino/) are both good resources.

The four IR sensors in this project are wired up so that each output is connected to Arduino pins: 4,5,6,7. You also need to power each IR sensor with 5V and GND. For my hookup, I chose to use Arduino pins D2 and D3 for power. Set D2 to an OUTPUT HIGH (5V power) and D3 to an OUTPUT LOW (GND). You could choose to use the 5V pin and GND pin on the Redboard Qwiic, but I chose to use D2/D3 for power so that I could plug all of my lines from the IR sensors into a single row of six pins.