# Source: https://learn.sparkfun.com/tutorials/glowing-pin

## Introduction 

In this project, we'll create a wearable pin using conductive thread to connect a LilyPad LED to a battery holder. Follow along by drawing your own design on a piece of fabric, or download and print one of SparkFun's designs.

[] Design and build time: 30 minutes --- 1 hour

[![glowing pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LilyPadPinFinished.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LilyPadPinFinished.jpg)

This is Project 1 from the [LilyPad Sewable Electronics Kit](https://www.sparkfun.com/products/13927), take a look at the other projects in the kit:

- Project 2: [Illuminated Mask](https://learn.sparkfun.com/tutorials/illuminated-mask)
- Project 3: [Light-Up Plush](https://learn.sparkfun.com/tutorials/light-up-plush)
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

- [LilyPad Coin Cell Battery Holder](https://www.sparkfun.com/products/13883)
- [3V Coin Cell Battery](https://www.sparkfun.com/products/338)
- [1 LilyPad LED](https://www.sparkfun.com/products/13903) (carefully snap out from the panel of five)
- [Conductive Thread](https://www.sparkfun.com/products/10867)
- [Needle](https://www.sparkfun.com/products/10405)
- Pin Template (1 piece) - see [Planning Your Project](https://learn.sparkfun.com/tutorials/glowing-pin#planning-your-project) for printable downloads
- White Felt (you will need at least 3 square inches)
- Pin Back

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/PinMaterials.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinMaterials.jpg)

Don\'t have a LilyPad Sewable Electronics Kit? You can follow along with this project using this [wish list](https://www.sparkfun.com/wish_lists/83222) of individual LilyPad pieces. You will need to source your own felt and pin back (available at local craft stores) to complete the project.\
\

### You Will Also Need:

- Pen, marker, or chalk
- Fabric to draw a design on or [printable fabric](http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=printable+fabric) (optional)
- Scissors
- Hot glue gun (with extra glue)
- Printer if you are downloading and printing one of SparkFun's pin designs

## Planning Your Project

For this project, we'll be using the Glowing Pin template (download below or use the template included with your kit). If needed, download and print the provided template. We\'ve also provided some color and black and white designs to use with printable fabric for the top layer of the pin. Right-click the images below and choose "Save Link As" to download the template to your computer.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinTemplateThumbnail.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/GlowingPinTemplate.pdf)

*Right-click and choose "Save Link As" or click image to download PDF*

**Printable Fabric Designs:**

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinThumbnailBlack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/GlowingPin_PrintableFabricBW.pdf) [![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinThumbnailColor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/GlowingPin_PrintableFabricColor.pdf)

*Right-click and choose "Save Link As" or click image to download PDF*

*After downloading a design, follow the directions on the package of your printable fabric to print them out. Feel free to create a larger pin by scaling the downloadable designs, if you'd like more room to work with or for a real statement piece.*

Trace the pin template on white felt and cut out. We'll be building our circuit on the felt piece, then adding a decorative layer of fabric with designs on top of it. Trace and cut a slightly larger circle or SparkFun design out of thin fabric (or design your own out of felt) for the top layer of the pin.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/PinCut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinCut.jpg)

## Understanding Your Circuit

This project is an example of a basic [circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit) -- an electrical loop that travels from a power source along a path (called a trace) to a component (or components) that uses the electricity to function, and then back to the power source. For our project, we'll use an [LED (Light-Emitting Diode)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds). When this loop is completed by stitching the pieces together with conductive thread traces, electricity from the power source is able to flow from the positive (+) side of the battery through to the LED (lighting it up) and back to the negative (--) side of the battery. This electric flow is called current. As you build projects with LilyPad pieces, you will learn different ways to design conductive thread circuits and experiment with additional pieces that help control or use the flow of electricity.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/UnderstandingCircuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/UnderstandingCircuit.jpg)

In this circuit, the LED is installed facing the fabric to shine through the other side. Other LilyPad projects may use LEDs facing outward from the fabric.

Take a look at the LED and battery holder. Notice that the silver sew tabs are labeled either positive or negative. Many electronic components have [polarity](https://learn.sparkfun.com/tutorials/polarity), meaning electric current can only flow through them in one direction.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LEDPolarity.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LEDPolarity.jpg)

If hooked up incorrectly, they will not light up. The batteries in this kit are also polarized; they have a positive and negative side. Always check the labels on LilyPad pieces to make sure they are correctly oriented before sewing together a circuit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LEDInstallation.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LEDInstallation.jpg)

## Arranging Your Circuit

[] Don\'t put your battery in yet.

Position the battery holder with the ON/OFF switch to the left side and the bottom two sew tabs close to the bottom edge of the felt. Use a small dot of hot glue in the center of the holder to attach it to the felt, as shown. Gluing the battery holder on this way leaves room for placing the LilyPad LED on the felt.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LilyPadPinBatteryPlacement.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LilyPadPinBatteryPlacement.jpg)

Remember: Glue is great for keeping your components in place, but it can interfere with your circuit. Try to keep glue clear of sew tabs.

While planning the LED's placement, note that it will need to be slightly above the center or toward the top half of the fabric so it doesn't touch or overlap the battery holder. If you are using one of SparkFun's pre-made designs, hold the design over the felt, and use a fabric marker or chalk to mark where the LED should be placed to shine through. Gather one LED (snap off of an LED panel if needed).

For this project only, we'll place the LED with the lens facing the felt, allowing it to shine through to the other side. The back of the LED has a cursive L, which should be facing you. For the rest of the projects in the LilyPad Sewable Electronics Kit, we'll install the LED with the lens up (away from the felt).

Before attaching the LED, rotate it so the (+) and (--) symbols on the LED board align with the (+) and (--) symbols on the battery holder's sew tabs. Use a small dab of hot glue on the center of the front of the board to secure to the felt. Be careful not to cover the holes with glue -- we'll need those to sew through later.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LilyPadPinLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LilyPadPinLED.jpg)

## Stitching It Together

#### If you need help sewing with conductive thread, [this tutorial](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing) covers the basics.

### STEP 1:

Cut a long piece of conductive thread, thread the needle, and tie a knot at the end. Now, it's time to connect the LED to the battery holder with the conductive thread. One line of stitching will connect the positive (+) side of the battery holder to the positive end of the LED. A second line of stitching will connect the negative (--) sides of the boards and complete the circuit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/LilyPadPinStitchPos.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/LilyPadPinStitchPos.jpg)

### STEP 2:

Finish your first line of stitching by tying a [finishing knot](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing/sewing-with-conductive-thread#finishing) on the sew tab and trimming your excess thread.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/PinPosFinish.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinPosFinish.jpg)

*Don't forget! You'll need to tie a new knot at the end of your thread before you begin the next section of stitching.*

### STEP 3:

Repeat the process with a new piece of thread to connect the negative side of the battery holder to the negative end of the LED. Be careful not to let the stitches touch the path used for the positive connections, as that would cause a short circuit. Trim any thread tails before testing. Now, the circuit is complete!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/PinNegativeStitching.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/PinNegativeStitching.jpg)

## Installing Your Battery and Testing

Insert the coin cell battery with the positive side facing up, labeled as (+), into the opening on the battery holder across from the ON/OFF switch. Turn on the switch to allow current to flow through the circuit. Turn off the switch when not in use to prolong battery life.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/2/BatteryInsert.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/2/BatteryInsert.jpg)

*How to place a battery in a LilyPad Battery Holder..*

### Troubleshooting

With any electronics project, there are times you will have to troubleshoot if your circuit isn\'t working. If your circuit isn\'t lighting up, try a new battery or check that your project is switched on. Check your sewing for any loose threads or ends that may be touching other parts of your circuit and causing a [short circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit#short-and-open-circuits). Learn more about troubleshooting your project in the [LilyPad Basics: E-Sewing](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing#troubleshooting) tutorial.

## Finishing Touches

[] Always remove your battery when working on your project to avoid damaging your components.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/GlowingPinStitching.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/GlowingPinStitching.jpg)

With the battery removed, use a hot glue gun or thread to attach your fabric design over your felt circle so the LED shines through. Draw a design on the fabric, if you'd like (or see design templates in the [Planning Your Project](https://learn.sparkfun.com/tutorials/glowing-pin#planning-your-project) step). Turn the project over, and attach an adhesive pin back to finish up your wearable art!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/0/StitchingPin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/StitchingPin.jpg)

Here are a few examples of creative glowing pins:

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPinMain.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPin1.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPin2-1.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPin2_1.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPin3.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/0/ExamplesPin4.jpg)

[[]](#carousel-6954f65f73cda) [[]](#carousel-6954f65f73cda)

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