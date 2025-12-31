# Source: https://learn.sparkfun.com/tutorials/makey-makey-classic-hookup-guide

## Introduction

Welcome to the world of [Makey Makey](https://www.sparkfun.com/products/14478)! A world where everyday objects are much more than they appear. Bananas are more than just a curvy fruit \-\-- they\'re keys to a virtual piano. Play-Doh isn\'t just a child\'s toy \-\-- it\'s the controlling force behind Pacman\'s up/down/left/right. And your simple pencil drawings are a portal to Portal.

[![Makey Makey Classic by JoyLabz](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/5/2/8/14478-02.jpg)](https://www.sparkfun.com/makey-makey-classic-by-joylabz.html)

### [Makey Makey Classic by JoyLabz](https://www.sparkfun.com/makey-makey-classic-by-joylabz.html) 

[ KIT-14478 ]

The MaKey MaKey Classic by JoyLabz is an invention kit that tricks your computer into thinking that almost anything is a keyb...

[ [\$53.50] ]

Be prepared to look at everyday objects in a whole new light. Be stoked! The world is your construction kit.

### Materials Required

- [Makey Makey](https://www.sparkfun.com/products/14478) \-\-- The star of the show! The kit should already **include**:
  - Mini-USB Cable
  - Alligator Clip Cables
  - Tinned Tipped Wires
- A **computer** (Windows, Mac OS X, or Linux) with an Available USB Slot
  - Software to Read Key Presses (e.g., [Canabalt](http://www.adamatomic.com/canabalt/), [Virtual Piano](http://www.virtualpiano.net/), [Tetris](http://www.freetetris.org/game.php), etc.)
- Button Material (e.g., fruit, Play-Doh, tin foil, copper tape, pencil, a friend)
- A Primed Imagination

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

## What is the Makey Makey?

The Makey Makey is a [collaborative project](https://makeymakey.com/about/#collaborators) between Jay Silver and Eric Rosenbaum of the MIT Media Lab and SparkFun Electronics. It\'s an invention kit that encourages people to find creative ways to interact with their computers by using everyday objects as a replacement for keyboards and mice. With the Makey Makey, you could replace your space key with a banana, use Play-Doh to move and click your mouse, or high-five your best friend to advance PowerPoint slides.

## Hardware Overview

### Top Side

The Makey Makey is a two-sided circuit board. On the more simple top side, the Makey Makey has six inputs: the up/down/left/right arrow keys, as well as the space bar and mouse left click:

[![Makey Makey Top Key Pads Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-06_MakeyMakeyTopHighlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-06_MakeyMakeyTopHighlighted.png)

Each of those inputs as well as the very important "Earth bar" are available in the form of what I like to call "alligator-bait" connectors. You\'ll use the included alligator clip cables to clip right into the hole pairs. This will all be made much more clear in the next section. For now, let\'s keep summarizing your Makey Makey.

If any key is activated with the \"Earth Bar,\" an associated LED will light up next to the pad.

[![Makey Makey LEDs Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-06_MakeyMakeyTopLEDHighlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-06_MakeyMakeyTopLEDHighlighted.png)

### Back Side

When you flip the board over to the back side, you will notice a mini-B USB connector and POWER LED. The connector is where you will connect the USB cable to a computer. The LED will light up when the board is powered.

[![Makey Makey USB Connector and Power LED](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_1.png)

You\'ve also got access to 12 more keys via the black female headers:

- W, A, S, D, F, and G on the keyboard side
- up/down/left/right mouse movement and left/right clicks on the mouse side

The bottom header has six additional ground (aka Earth) outputs.

[![Makey Makey Keyboard, Mouse, and Ground via Female Header](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_2.png)

The top header is an expansion/output header. They KEY OUT and MS OUT are connected to the LEDs on the back to indicate whether you\'re pressing a keyboard or mouse key, respectively. This can be used to connect low-power LEDs and small motors. The RESET will reset the board when connected to ground. There are also pins for power through the 5V and GND. The last two pins (PGD and PGC) are used by the factory to program.

[![Makey Makey Expansion Header and Status LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/14478-04MakeyMakeyBottomHighlighted_3.png)

The pins broken out through the black female headers are all available in the form of "jumper-wire" connectors to connect [male jumper wires](https://www.sparkfun.com/products/12795), [header pins](https://www.sparkfun.com/products/116), [stripped wires](https://learn.sparkfun.com/tutorials/working-with-wire#how-to-strip-a-wire), or tinned tipped wires.

## Hardware Hookup

The simplest Makey Makey key you can make is one that only uses your **fingers**. Below are instructions to make yourself into a key!

### Connect a USB Cable

First, grab the mini-USB cable included with the Makey Makey and insert the cable into the connector. Connect the other end to a USB port of your computer.

[![Connect the Mini-B USB Cable to the Makey Makey Classic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_USB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_USB.jpg)

### Ignore Pop-up Windows

When you first insert the Makey Makey into your computer, a window may pop up. You can cancel or close out the window.

### Connect Earth

Touch the **Earth** bar to ground yourself.

[![Ground Pad on the Makey Makey](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_ConnectGND.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_ConnectGND.jpg)

### Connect Yourself

Simultaneously touch the **SPACE** pad. The LED above the **SPACE** key should light up, and a space command should be sent to your computer.

[![Pressing a Key on the Makey Makey with Fingers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_SpacePad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_SpacePad.jpg)

Now try leaving one finger on the Earth bar while quickly tapping the space button. Getting a feel for it? It should work just like your standard space key!

### Testing With a Text Editor

Open up some sort of text editor (Notepad, Word, TextEdit, etc.) on your computer to confirm if the Makey Makey is sending a space to your computer. Remember, just as with your boring ol\' keyboard, your computer will interpret keypresses differently depending on what program is active. You can also use your mouse to click between the words in the textbox shown below.

Makey Makey Classic Test Area

[**Warning!** Any text written in this textbox will be erased when you refresh this webpage!]

### Online Apps for Makey Makey

Looking for some fun games to test out the Makey Makey? Click on the link below to try out the online apps provided by JoyLabz!

[Online Apps for Makey Makey](https://labz.makeymakey.com/d/)

\

## Making Your First Key

### Makey Makey Key-Making Materials

To make your \"standard\" key with the Makey Makey you need the following:

- A connection to a Makey Makey **input**. This can be done using alligator clips on the the hole pairs, or jumper wires on the black connector sockets.
- Connection to a Makey Makey **ground** (Earth). Again, you\'ll connect to earth using either alligator clips or jumper wires.
- Some sort of **key material**. This is the fun/creative part! There\'s a world of Makey Makey keys out there. Anything that\'s even slightly conductive is just waiting to become a computer input. The classics include your fingers, bananas and pencil scratchings.
- Something to **activate the key** by connecting between the key material and the ground input. Your fingers work pretty well for this. Anything even slightly conductive will do, though.

### Making a Key

Activating a key means creating a closed circuit. For the circuit to work, electrons have to be able to flow from the Makey Makey input key to Makey Makey\'s ground. Usually your fingers will be the missing link between those two:

[![Makey Makey key sketch](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/JoyLabz-makey-makey-how-it-works.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/JoyLabz-makey-makey-how-it-works.jpg)

*Image courtesy of [JoyLabz](https://makeymakey.com/)*

Let\'s try making a bona fide Makey Makey key. First, you\'ll need to find some sort of key object. Dig around your house, check your fruit basket or coin purse, or grab a pencil and make a drawing to try it out.

Pick out your favorite-colored alligator clip cable, open one of the jaws, and snap it down onto your key. Clip the other end of the clip into one of the Makey Makey top-side inputs. **SPACE** is great for testing purposes, so we will start with that key pad:

[![First alligator clip connected to banana](https://cdn.sparkfun.com/r/600-600/assets/0/5/2/5/5/52e94fe5ce395fa5058b456b.jpg)](https://cdn.sparkfun.com/assets/0/5/2/5/5/52e94fe5ce395fa5058b456b.jpg)

Now, grab a second cable for the ground connection. Black is the classic \"ground color\", but set your own trend and pick whatever you want. Clip one end of one cable into the Earth bar and let the other end dangle for now.

[![Ground clip attached to banana](https://cdn.sparkfun.com/r/600-600/assets/f/9/1/d/e/52e95247ce395f58708b456c.jpg)](https://cdn.sparkfun.com/assets/f/9/1/d/e/52e95247ce395f58708b456c.jpg)

Open up some sort of **text editor** (Notepad, Word, TextEdit, etc.) on your computer. Or you can click between the words in the test box provided below.

Makey Makey Classic Test Area

[**Warning!** Any text written in this textbox will be erased when you refresh this webpage!]

Finally! Grab the dangling end of the ground cable with one hand. Make sure you\'re touching the metal part of the clip. Then use your other hand to touch the banana, or whatever your key might be. BAM! Space!

[![Pressing the banana key](https://cdn.sparkfun.com/r/600-600/assets/6/7/d/4/2/52e952c1ce395f2b358b4567.jpg)](https://cdn.sparkfun.com/assets/6/7/d/4/2/52e952c1ce395f2b358b4567.jpg)

### Experimenting With Key Materials

Don\'t have a banana? Try experimenting with different materials. Some materials conduct better than others. Certain materials can also be conductive over a period of time. Try it out!

Below is an example of a hand-drawn key from a standard pencil. A dotted circle was drawn on two sides of a piece of paper and extended to the center. Lines of alternating lengths were drawn (short and long) from each extension with a gap between the lines so that one finger could be used as the key.

[![hand-drawn Buttons with the Makey Makey](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_PencilButtonDraw.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_PencilButtonDraw.jpg)

The first drawing with the thin lines labeled \"Button 1\" was a poor conductor on paper. However, the second drawing with the bold, thick lines labeled \"Button 2\" was able to conduct. In this case, the pencil was only able to conduct when there was enough of the material. After a few uses, the lines faded and required another layer of graphite.

[![Pressing Down on the Buttons with the Makey Makey](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_PencilButtonPress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_PencilButtonPress.jpg)

### Using the Back

Remember the black connectors on the other side of the board? There are additional keys that you can connect! You can follow a similar set of steps, replacing alligator cables with **jumper wires**. The wires included with the Makey Makey is one type of jumper wire. Jumper wires can be a bit tougher to connect to keys. An easy solution is to connect an alligator cable to the free end of the jumper.

Let\'s try it out. Insert one end of the tinned tipped wire fully into a socket. Connect the other end to a conductive material. You may need to use an alligator cable to extend and connect to the material. Repeat for the ground connection.

The example below is similar to the hand-drawn button. Strips of copper tape were used for \"Button 3\" instead of a pencil. Since the material is more conductive and thicker than the hand-drawn lines, only two stripes were used. Regular tape was used to secure the tinned ends of the wire against the paper and table. After a few uses, the copper fared better than the graphite pencil.

[![Copper Tape Button Pad with the Makey Makey](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakey_CopperButton.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakey_CopperButton.jpg)

### Adding More Keys!

To add more keys, simply connect another alligator clip to another Makey Makey input (e.g., arrow keys or mouse click) and connect the other end to a key material. No further ground connections are necessary as long as there is one available. Be creative and connect as many keys as you can to the Makey Makey!

[![Jim and Various Keys for the Makey Makey](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/Makey_Makey_Action_Shot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/Makey_Makey_Action_Shot.jpg)

*Jim and a Makey Makey connected to various types of keys!*

### What Makes a Key? Conductivity.

A material is a conductor if it allows electricity (even just a tiny bit of it) to flow. This is the magic behind the Makey Makey: most of the world *is* conductive! Anything metal will almost certainly conduct electricity. The \"standard\" conductors are copper, silver, gold, etc. But with the Makey Makey our conductor scope grows. Most organic materials \-\-- things like human skin, liquids, foods and frog legs \-\-- are at least a little conductive. And that\'s really all the Makey Makey needs.

If an object isn\'t conductive, it\'s an **insulator**. Common insulators include plastic, glass, ceramic and wood. You can usually tell just by looking at something whether it\'s an insulator or conductor. You\'ll have to watch out for objects like this, as they just won\'t work with the Makey Makey. To get around that, though, you can line them with a conductive material (like [copper tape](https://www.sparkfun.com/products/10561), or just regular old [wire](https://www.sparkfun.com/products/8022)) or paint. This creates the illusion that they\'re conducting electricity.

[![Makey Makey Controller with Copper Tape](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/11519-01_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/11519-01_1.jpg)

*Makey Makey held against an enclosure and connected to a controller with copper tape and alligator cables.*

**Resistance** is a measure of exactly how conductive a device is. Resistance can be measured with just about any standard [multimeter](https://www.sparkfun.com/products/9141). Any object with a resistance of about 4.5MΩ (that\'s a really high resistance) or less should work as a Makey Makey input. If you\'re not sure if something will work with the Makey Makey, whip out a multimeter (buy one if you have to; they\'re an essential tool for electronics hobbyists) and test that resistance! Or, better yet, just connect it to your Makey Makey and experiment.

## Remapping Keys

The Makey Makey v1.2 Classic has an option if you ever need to change the default keys. To remap the key, you will need to go online and head over to JoyLabz using any internet browser. Click on the button below to open a new window.

[Remap Your Makey Makey Key!](https://makeymakey.com/remap/)

\

Following the instructions provided by JoyLabz is pretty straightforward, but we also outlined the instructions below. By clicking on the link, it should have opened up a new tab or window. You will have two options. Click on the Makey Makey Classic.

[![Makey Makey Remapping Keys: Selecting the Makey Makey Classic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_1.png)

**Heads up!** When reprogramming the Makey Makey keys, you will need to have the browser window active. If you happen to click outside of the window, it will become dark. All you need to do is use your mouse and click back on the reprogramming window.\
\

[![](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_Browser.png "Active Remap Browser Window for Reprogramming the Makey Makey")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_Browser.png)\

\
The page will also time out if you take too long of a break. When this happens, you will need to start at the beginning.\
\

[![](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_timeout.png "Timeout in Browser Window for Reprogramming the Makey Makey")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_timeout.png)

Once selected, the prompt will ask you to check and ensure that you have the correct Makey Makey version. On the back side with the black female headers, you will notice that the board has a version number printed as **v.1.2** If you do not have that version, you will not be able to remap the keys with these instructions. If it is v.1.2, proceed by connecting the Mini-USB cable to the Makey Makey and clicking on the **START** button. For now, do not connect the other end to your computer\'s USB port.

[![Makey Makey Remapping Keys: Check Your Version](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_2.png)

Grab two alligator clips and connect the up (↑) and down (↓) arrows together. Then connect the left (←) and right (→) arrows. Once connected, connect the other end of the USB cable to your computer\'s USB port. You will notice the green LEDs begin to fade in and out, indicating that the Makey Makey is in programming mode.

[![Makey Makey Remapping Keys: Adding Alligator Clips to Cursors ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_3.png)

The browser will eventually respond with a note indicating that the Makey Makey is detected. If you do not see the message, you may need to unplug the USB cable from your computer and start again. Also, make sure that the browser to remap keys is active. Otherwise, follow the prompt by removing the alligator clips if the Makey Makey is in programming mode.

[![Makey Makey Remapping Keys: Removing Alligator Clips ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_4.png)

With one hand, ground yourself by touching the exposed GND pads. With the other hand, touch the left or right keys to navigate to the key that you are interested in remapping.

[![Makey Makey Remapping Keys: Remap Key ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_5.png)

**Note:** You will only be able to use the Makey Makey to navigate. You will not be able to use your keyboard or mouse.

The key that will be remapped will be highlighted yellow. Let\'s remap the left mouse \"CLICK\" on the Makey Makey. Navigate to the left mouse \"CLICK\" button. Once selected, keep one hand on GND and touch the \"CLICK\" pad to remap the key.

[![Makey Makey Remapping Keys: Navigate to Key ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_6.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_6.png)

The key that is being remapped will be highlighted green. The replacement key will be highlighted yellow. At this point, you can select the replacement key located at the bottom of the browser. Navigate through the keys using the Makey Makey\'s arrow pads. Let\'s select the \"enter\" key by moving to its icon and touching the \"CLICK\" pad.

[![Makey Makey Remapping Keys: Select Replacement Key](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_7.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_7.png)

The browser will have a nice animation and replace the old key with a new key. At this point, you can continue to remap the other keys. For now, we will just remap one key.

[![Makey Makey Remapping Keys: Replaced Key](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_8.png)

Navigate to the **SAVE** button by pressing on the down pad. Here, you will be able to **SAVE** the remapped key, **CANCEL** any changes that you have made, or **RESTORE** the Makey Makey default keys. Let\'s save the remapped key by pressing on the \"CLICK\" pad.

[![Makey Makey Remapping Keys: Save](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_save.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_save.png)

A prompt will pop up asking you to confirm the save. Use the left arrow pad to highlight \"YES\". Click on the \"CLICK\" pad to confirm.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_SaveConfirm.png "Makey Makey Remapping Keys: Confirm Save")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_SaveConfirm.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_SaveConfirmYes.png "Makey Makey Remapping Keys: Confirm Save")](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_SaveConfirmYes.png)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The settings will save and you will be greeted with a \"SUCCESS!\"

[![Makey Makey Remapping Keys: Success](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_Success.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/7/MakeyMakeyRemap_Success.png)

## Troubleshooting 

Not working as expected? Check out the Troubleshooting section for the Makey Makey v.1.2 Classic:

[JoyLabz Troubleshooting for the Makey Makey Classic](https://makeymakey.com/how-to/classic/#troubleshooting)

You may even want to check out their Frequently Asked Questions:

[JoyLabz FAQ for the Makey Makey](https://makeymakey.com/faq/#h.ggzwkib83bkb)