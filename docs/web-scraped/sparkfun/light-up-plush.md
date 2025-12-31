# Source: https://learn.sparkfun.com/tutorials/light-up-plush

## Introduction

For this project, we\'ll try individually controlling the LEDs in an e-textile circuit. We'll explore two ways of controlling the flow of current to an LED using a button and switch while we craft a creative plush creature.

[] Design and build time: 2 - 3 hours

[![light-up plush](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/FinishedPlush.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/FinishedPlush.jpg)

This is Project 3 from the [LilyPad Sewable Electronics Kit](https://www.sparkfun.com/products/13927), take a look at the other projects in the kit:

- Project 1: [Glowing Pin](https://learn.sparkfun.com/tutorials/glowing-pin)
- Project 2: [Illuminated Mask](https://learn.sparkfun.com/tutorials/illuminated-mask)
- Project 4: [Night-Light Pennant](https://learn.sparkfun.com/tutorials/night-light-pennant-with-lilymini-protosnap)

### Suggested Reading

If this is your first sewable electronics project, we recommend you read our LilyPad Basics tutorial.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

December 17, 2016

Learn how to use conductive thread with LilyPad components.

## Materials and Tools

Let\'s go over all of the things you\'ll need to sew your project together.

[![LilyPad Sewable Electronics Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/9/8/13927-05.jpg)](https://www.sparkfun.com/lilypad-sewable-electronics-kit.html)

### [LilyPad Sewable Electronics Kit](https://www.sparkfun.com/lilypad-sewable-electronics-kit.html) 

[ KIT-13927 ]

The LilyPad Sewable Electronics Kit lets you explore the wonderful world of electronic sewing (e-sewing) and e-textiles throu...

[ [\$107.95] ]

### Items included in the [LilyPad Sewable Electronics Kit](https://www.sparkfun.com/products/13927):

- The following are found on the LilyPad E-Sewing Protosnap (only available in the kit).
  - [LilyPad Coin Cell Battery Holder](https://www.sparkfun.com/products/13883)
  - 3x [LilyPad LEDs](https://www.sparkfun.com/products/13902) (carefully snap out from the panel of five)
  - [LilyPad Button Board](https://www.sparkfun.com/products/8776)
  - [LilyPad Slide Switch](https://www.sparkfun.com/products/9350)
- [3V Coin Cell Battery](https://www.sparkfun.com/products/338)
- [Conductive Thread](https://www.sparkfun.com/products/10867)
- [Needle](https://www.sparkfun.com/products/10405)
- Plush Templates (1 piece) - see [Planning Your Project](https://learn.sparkfun.com/tutorials/light-up-plush#planning-) for printable downloads
- Felt (one 9\"x12\" sheet of craft felt will make one plush; use scraps of felt to add decorations)
- Fiberfill Stuffing
- Embroidery or Sewing Thread

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushMaterials.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushMaterials.jpg)

Don\'t have a LilyPad Sewable Electronics Kit? You can also follow along with this project using the [E-Sewing ProtoSnap Kit](https://www.sparkfun.com/products/14528):

[![LilyPad E-Sewing ProtoSnap Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/1/2/14528-02.jpg)](https://www.sparkfun.com/lilypad-e-sewing-protosnap-kit.html)

### [LilyPad E-Sewing ProtoSnap Kit](https://www.sparkfun.com/lilypad-e-sewing-protosnap-kit.html) 

[ KIT-14528 ]

The LilyPad E-Sewing ProtoSnap Kit is a great way to incorporate buttons and switches into an e-textile project without any p...

[ [\$13.50] ]

### You will also need:

- Pen, marker, or chalk
- Scissors
- Hot glue gun (with extra glue)
- Optional: Craft supplies for decorating (feathers, sequins, buttons, etc.)

## Planning Your Project 

For this project, we'll be using the Light-Up Plush template (download below or use the template included with your kit). If needed, download and print the provided template. Right-click the image below and choose "Save Link As" to download the template to your computer.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushTemplateThumbnail.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/LightUpPlush_Template.pdf)

*Right-click and choose "Save Link As" or click image to download PDF*

Trace and cut out the plush template shape on a piece of felt. To hide your stitches entirely, cut out an extra half-piece of felt (as shown) to place on top of your finished plush (see [Finishing Touches](https://learn.sparkfun.com/tutorials/light-up-plush#finishing-touches)).

[] The two halves of what will become your plush are connected at the "feet" to allow your entire circuit to be on one surface and to make stuffing the project easier. **Don't cut these two halves apart.**

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushCut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushCut.jpg)

### Working with ProtoSnap

If you are using individual LilyPad components instead of the E-Sewing ProtoSnap, you will not be able to follow along with the experiment in the next section exactly, but read along to learn more about buttons and switches.

We'll use the LilyPad pieces in the circuit to turn different LEDs on and off. Using the E-Sewing ProtoSnap, we'll examine how buttons and switches behave differently, then snap the pieces apart and build them into a plush creature with light-up features.

Before we arrange our circuit on the felt, with the battery installed, slide the battery holder switch to the ON position.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/ProtoSnapLabels.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/ProtoSnapLabels.jpg)

[] Don't snap apart your E-Sewing ProtoSnap board quite yet. You'll need it intact for a brief experiment first.

## Understanding Your Circuit

[Buttons and switches](https://learn.sparkfun.com/tutorials/switch-basics) are electronic components that control the flow of electricity through a circuit. The circuit is closed when current is allowed through by turning on a switch or pressing a button. When a piece of the circuit is disconnected by turning a switch or button off, it is an [open circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit#short-and-open-circuits).

### LilyPad Slide Switch

The LilyPad Slide Switch has a small switch labeled ON/OFF. When the toggle is moved to the ON position, the two sew tabs on the switch are connected, allowing current to flow through and close the circuit. When moved to OFF, parts inside the switch move away from each other and open the circuit (disconnecting it). It helps to visualize switches as drawbridges for electricity -- when the bridge is up (open), nothing can cross over. When it is down (closed), the pathway is reconnected, and electricity can flow along the original path.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/ProtoSnapSwitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/ProtoSnapSwitch.jpg)

### LilyPad Button

The LilyPad Button Board is also a type of switch. When you press the button in the middle of the board, it connects the two sew tabs and allows current to flow through. When you let go of the button, the connection is opened again, and the button springs back into place. This button is an example of a momentary switch -- it is only active when an action is applied.

This is slightly different from the slide switch, which is an example of a maintained switch, meaning its state remains the same until changed.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/ProtoSnapButton.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/ProtoSnapButton.jpg)

*Learn more about buttons and switches in our [Switch Basics](https://learn.sparkfun.com/tutorials/switch-basics) tutorial.*

## Arranging Your Circuit 

Carefully snap apart the connected components on the E-Sewing ProtoSnap panel. Discard the non-sewable pieces and scraps. You will end up with six LilyPad pieces: a battery holder with battery, three LEDs, a button, and a switch.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/ProtoSnapBreak.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/ProtoSnapBreak.jpg)

[] Always remove your battery when working on your circuit to avoid damaging your components.

Arrange the pieces on the felt according to the diagram below. Make sure to check the orientation of the LilyPad LEDs before you stitch them together. The positive tabs of the LED connect to the button or switch, and the negative tabs connect to the negative tab on the battery holder. When your circuit design is finalized, use a dab of glue on the back of each component to attach them to the felt.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushLayout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushLayout.jpg)

For this project, we'll be arranging the pieces slightly differently from on the E-Sewing ProtoSnap. To avoid any crossed conductive thread, we are connecting (+) with both the button and the switch instead of having two separate paths to the battery holder. When creating circuits with e-textiles, both the electrical properties of the circuit and aesthetic decisions are part of the design process.

This project has a lot of stitching. If you want to hide the stitches, use a layer of felt or decorations over the thread after you've finished your circuit (see [Finishing Touches](https://learn.sparkfun.com/tutorials/light-up-plush#finishing-touches) section), or use a hidden stitch (see our [E-Sewing Basics](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing#sewing-with-conductive-thread) tutorial).

## Stitching It Together

#### If you need help sewing with conductive thread [this tutorial](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing) covers the basics.

### STEP 1:

Cut a long piece of conductive thread, thread the needle, and tie a knot at the end. Begin sewing at the positive sew tab on the battery holder closest to the fold or "feet" on the felt cutout. Remember to use three to four loops around each tab as you sew.

Use a running stitch or hidden stitch (see [E-Sewing Basics](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing#sewing-with-conductive-thread) for these techniques) to connect the positive sew tab on the battery board to the closest sew tab on the switch. Sew three to four loops around the switch's sew tab to secure, then tie a knot and cut.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushSwitchStitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushSwitchStitch.jpg)

### STEP 2:

With a new piece of thread, connect the other side of the switch to the positive sew tabs of the top two LEDs and end with three to four loops on the closest tab of the button. Tie and cut.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushLEDSwitchStitch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushLEDSwitchStitch.jpg)

### STEP 3:

With a new piece of thread, begin at the other side of the button and stitch three to four loops around the sew tab. Continue stitching to the positive side of the last LED, ending with three to four loops.

Tie and cut.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushButtonLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushButtonLED.jpg)

### STEP 4:

Finally, we'll stitch all the negative connections. With a new piece of thread, stitch three to four loops on the negative (--) sew tab of the first LED and connect to the negative tabs on the other LEDs, ending at the negative tab of the battery holder as shown. Make sure to loop three to four times on each connection.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/PlushNegative.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/PlushNegative.jpg)

*After all the stitching is complete, turn the project over, and trim any loose thread tails before testing.*

## Installing Your Battery and Testing

Insert the coin cell battery into the battery holder with the positive (labeled +) side facing up. Test the button and switch to make sure the LEDs light up. If they do, remove the battery and continue to the Finishing Touches section.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/2/BatteryInsert.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/2/BatteryInsert.jpg)

*How to place a battery in a LilyPad Battery Holder.*

### Troubleshooting

With any electronics project there are times you will have to troubleshoot if your circuit isn\'t working. If your circuit isn\'t lighting up, try a new battery or check that your project is switched on. Check your sewing for any loose threads or ends that may be touching other parts of your circuit and causing a [short circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit#short-and-open-circuits). Learn more about troubleshooting your project in the [LilyPad Basics: E-Sewing](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing#troubleshooting) tutorial.

## Finishing Touches

[] Always remove your battery when working on your project to avoid damaging your components.

Conductive thread can be part of the visual design, or hidden. To hide stitches, add a layer of felt on top with cutouts to allow the LEDs to shine through and to access the button and switch.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/HidingStitches.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/HidingStitches.jpg)

Once you've finished testing, it's time to make the plush three-dimensional. Remove the battery, and fold the felt at the connected points (feet) at the bottom so the LilyPad components are on the outside. Using non-conductive sewing or embroidery thread (or a glue gun) seal all but 2 inches at the top of the plush; we will add fiberfill stuffing in this opening.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/StitchingPlush.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/StitchingPlush.jpg)

Push the fiberfill stuffing into the hole to fill the plush. Use your fingers or a pencil to fill up the arms and legs. The stuffing will give the plush its shape in addition to acting as an insulator for the conductive thread stitching on the inside. Stitch the opening closed with embroidery or sewing thread to finish the project.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/7/1/StuffingPlush.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/StuffingPlush.jpg)

You can now use craft supplies such as glitter, paint, or other decorative accents to enhance the plush or hide your LEDs and stitching. To protect the battery holder and battery, you can make a small flap of felt to cover the pieces and secure with velcro for easy access.

Here are a few examples of creative decorations on finished plush projects:

![ https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Examples_Main.jpg](%20https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Examples_Main.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Example_OrangeMonster.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Example_RedMonster.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Example_Robot.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Example_Steampunk.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/4/7/1/Examples_Green.jpg)

[[]](#carousel-6954f6d90dc04) [[]](#carousel-6954f6d90dc04)

1.  ::: 
    :::

2.  ::: 
    :::

3.  ::: 
    :::

4.  ::: 
    :::

5.  ::: 
    :::

6.  ::: 
    :::