# Source: https://learn.sparkfun.com/tutorials/light-up-your-3d-printers-bed

## Introduction

Are you 3D printing in a room at night with barely any light? That\'s the problem that I came across when inspecting prints at SparkFun during odd hours. The light source behind me created a shadow over the print bed making it hard to see what was going on. In this tutorial, we will be using a LED strip to light up the print bed on a LulzBot 3D printer!

[![Non Addressable LEDs on Illuminating a 3D Printer\'s Bed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/Adding_LED_Strips_to_Light_Up_Your_3D_Printer_Bed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/Adding_LED_Strips_to_Light_Up_Your_3D_Printer_Bed.jpg)

### Required Materials

**Note:** This tutorial uses non-addressable LED strips but you could also customize your lighting by using an addressable LED strip of your choice. This will require additional components to get started.

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a screw driver, wire strippers, and diagonal cutters.

#### You Will Also Need

In addition to the materials listed above, you will need:

- Electrical Tape
- Hot Glue Gun and Glue Sticks

## Hardware Hookup

**⚡ Note:** While the LED strip is labeled 12V, a 9V power supply was used so that the LEDs were not overwhelmingly bright. At 9V, it also did not dissipate as much heat.

The wiring is simple between the female barrel jack adapter and the non-addressable LED strip. Simply insert the black wire connecting the \"**12V**\"\" pin to the \"**+**\"\" of the barrel jack adapter\'s screw terminal. Then insert the rest of the wires to the \"**\--**\" screw terminal.

[![Fritzing Diagram for Adapter and LED Strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/Non_Addressable_LED_Strip_Simple_bb_Fritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/Non_Addressable_LED_Strip_Simple_bb_Fritzing.png)

*Click the image for a closer look.*

**Note:** When testing the non-addressable LED strip, the pin labeled \"G\" was actually blue and the \"B\" was actually green. Depending on the manufacturer, the label may vary. Try testing the LED strip out with a power supply to determine see if the letter represents the color.

#### Hookup Table

Below is a hookup table that shows the connection between the female barrel jack adapter and non-addressable RGB LED strip.

  Nonaddressable RGB LED Strip Pinout   Female DC Barrel Jack Adapter
  ------------------------------------- -------------------------------
  \+                                    12V
  \-                                    G
  \-                                    R
  \-                                    B

### Connecting and Modifying the LED Strip

**Note:** This tutorial was written with the [Taz 5 3D printer](https://www.sparkfun.com/products/retired/13300). However, you can use this as a guide to attach any type of LED strip to your 3D printer! You will just need to adjust the length as necessary depending on the size of your 3D printer frame and the density of LEDs on your strip.

We will be attaching the LEDs to the top of the frame. Make sure that the LEDs and wires are not in the way of any moving parts. Determine the length that you need by holding the LED strip up against the 3D printer\'s frame. The length depends on the size of your printer\'s frame. For the Lulzbot TAZ 3D printers, about 16x segments of the LED strip was used. For the Lulzbot Mini, about 12x segments seemed to be sufficient. Each segment consists of 3x LEDs between the exposed copper pads.

[![LED Strip Segment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/LED_Strip_Segment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/LED_Strip_Segment.jpg)

*Click the image for a closer look.*

Cut 4x segments off one end of the 1M non-addressable LED using the diagonal cutter. Relative to the 3D printer that I was using, I decided to remove the 4x segments from the right side of the LED strip.

[![Cut Between Segments](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/12023_1cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/12023_1cut.jpg)

Carefully [strip extra wire insulation](https://learn.sparkfun.com/tutorials/working-with-wire) to expose more wire for the screw terminal. You may need to tin the tips of the wires by adding more [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). Then, insert the wires for **R**, **G**, and **B**, into barrel jack adapter\'s screw terminal labeled as \"**\--**\". Then tighten the screw with a Phillips head screw driver. Repeat for the black wire labeled as **12V** on the \"**+**\" side.

[![Tighten Screw Terminal](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/InsertLEDWiresScrewTerminal_Tighten.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/InsertLEDWiresScrewTerminal_Tighten.jpg)

Pull gently to verify that the wires are secure in the socket.

[![Pull Wires to Check If Secure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/PullWirestoTest.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/PullWirestoTest.jpg)

Insulate the exposed end of the LED strip with hot glue.

[![Insulate with Hot Glue](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/InsulateExposedCopperPad_LEDStrip_HotGlue.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/InsulateExposedCopperPad_LEDStrip_HotGlue.jpg)

Connect a barrel jack power switch between barrel jack adapter and power supply.

[![Connected Hardware](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/AddSwitch_LEDSTrip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/AddSwitch_LEDSTrip.jpg)

### Testing

Now would be a good time to check if the hardware was wired properly. Connect the power supply to a wall outlet. If the LEDs do not light up, flip the switch to the other side to see if the LED strip lights up.

[![Powering the LED Strip to Test](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/Test_LED_Strip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/Test_LED_Strip.jpg)

### Secure the LEDs

Attach the LED strip flush against the top of the 3D printer\'s frame and ensure that the wires are not in the way of the printable area. Since we want to illuminate the print bed, aim the LEDs toward the printer. While we could use the 3M adhesive that is on the back of the LED strip\'s clear jacket, I wanted to ensure that the adhesive did not fail during a print. Instead, the wires were secured by using electrical tape and wrapping the strip against the frame. Depending on the width of the tape, you may want to cut it down to prevent the LEDs from being blocked. You could use zip ties as well.

[![Mount the LED Strip with Tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/Mount_LED_Strip_3D_Printer_Frame.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/Mount_LED_Strip_3D_Printer_Frame.jpg)

Tape was added as necessary on the enclosure; left, top, and right side of the frame as shown in the image below. Feel free to mount the power switch to another location so that you do not accidentally turn the power off to your 3D printer.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighted Areas with Electrical Tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/SecuringLEDStrip_3D_Printer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/SecuringLEDStrip_3D_Printer.jpg)   [![LED STrip Mounted to 3D Printer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/LED_Strip_3D_Printer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/LED_Strip_3D_Printer.jpg)
  *Hightlighted Areas with Electrical Tape*                                                                                                                                                                                             *LED Strip Mounted to 3D Printer*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Enjoy 3D Printing in the Light!

Insert the power supply into a wall outlet and flip the switch to power the lights when you need to check on your print!

[![3D Printer Lit Up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/0/LED_Strip_3D_Printer_Lit_Up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/0/LED_Strip_3D_Printer_Lit_Up.jpg)

## Making It Better

Like all projects, you can always make it better and build upon the design. Here are few ideas to make it even more impressive by adding effects or interactive!

- Add microcontroller and transistors to control each color with the press of a button to add an effect.

  ::::::::::::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)
  :::

  ::: main
  ### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

  [ DEV-13975 ]
  The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...
  :::

  :::: 
  ::: prices
  [ [\$22.50] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Multicolor Buttons - 4-pack](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/8/14460-01.jpg)](https://www.sparkfun.com/multicolor-buttons-4-pack.html)
  :::

  ::: main
  ### [Multicolor Buttons - 4-pack](https://www.sparkfun.com/multicolor-buttons-4-pack.html) 

  [ PRT-14460 ]
  This is a simple 4-pack of momentary, multicolor buttons, great for all sorts of projects! Unlike previous iterations of mult...
  :::

  :::: 
  ::: prices
  [ [\$1.95] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Resistor 10k Ohm 1/6th Watt PTH](https://cdn.sparkfun.com/r/140-140/assets/parts/8/3/1/08374-02-L.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-6th-watt-pth.html)
  :::

  ::: main
  ### [Resistor 10k Ohm 1/6th Watt PTH](https://www.sparkfun.com/resistor-10k-ohm-1-6th-watt-pth.html) 

  [ COM-08374 ]
  1/6th Watt, +/- 5% tolerance PTH resistor.
  :::

  :::: 
  ::: prices
  [ [\$0.10] ]
  :::
  ::::
  :::::::

  ::::: 
  ::: actions-wrap
  [![N-Channel MOSFET 60V 30A](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/5/10213-01.jpg)](https://www.sparkfun.com/n-channel-mosfet-60v-30a.html)
  :::

  ::: main
  ### [N-Channel MOSFET 60V 30A](https://www.sparkfun.com/n-channel-mosfet-60v-30a.html) 

  [ COM-10213 ]
  This part is no longer available. The recommended replacement is \[here\](https://www.sparkfun.com/products/24144). If you\'v...
  :::

  **Retired**
  :::::
  :::::::::::::::::::::

  ::: clearfix
  :::
- Add a motion or heat sensor to light up and change color indicating the print is finished.

  ::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![SparkFun Grid-EYE Infrared Array Breakout - AMG8833 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/7/5/14607-SparkFun_GridEYE_Infrared_Array_-_AMG8833__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-grid-eye-infrared-array-breakout-amg8833-qwiic.html)
  :::

  ::: main
  ### [SparkFun Grid-EYE Infrared Array Breakout - AMG8833 (Qwiic)](https://www.sparkfun.com/sparkfun-grid-eye-infrared-array-breakout-amg8833-qwiic.html) 

  [ SEN-14607 ]
  The SparkFun Grid-EYE Infrared Array Breakout board is an 8x8 thermopile array, giving you a square of 64 pixels capable of i...
  :::

  :::: 
  ::: prices
  [ [\$47.50] ]
  :::
  ::::
  :::::::

  ::::: 
  ::: actions-wrap
  [![SparkFun OpenPIR](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/0/6/13968-01.jpg)](https://www.sparkfun.com/sparkfun-openpir.html)
  :::

  ::: main
  ### [SparkFun OpenPIR](https://www.sparkfun.com/sparkfun-openpir.html) 

  [ SEN-13968 ]
  The SparkFun OpenPIR is a highly customizable Passive Infrared (PIR) sensor based around the NCS36000 PIR controller. Passive...
  :::

  **Retired**
  :::::
  :::::::::::

  ::: clearfix
  :::
- Instead of RGB, use cool white for a more natural white. Mixing red, green, and blue may produce a \"white light\" but it is not a pure white.

  ::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![LED - 3W Aluminum PCB (5 Pack, Cool White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/4/13105-00.jpg)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html)
  :::

  ::: main
  ### [LED - 3W Aluminum PCB (5 Pack, Cool White)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html) 

  [ COM-13105 ]
  So much power and light from such a small package. This 5 pack of \"Cool\" white 3 Watt aluminum backed PCBs is sure to shed a ...
  :::

  :::: 
  ::: prices
  [ [\$12.45] ]
  :::
  ::::
  :::::::

  ::::: 
  ::: actions-wrap
  [![White Tri-Color LED Strip - Addressable, Sealed (1m)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/4/8/13898-02.jpg)](https://www.sparkfun.com/products/13898)
  :::

  ::: main
  ### [White Tri-Color LED Strip - Addressable, Sealed (1m)](https://www.sparkfun.com/products/13898) 

  [ COM-13898 ]
  These are sealed, addressable 1-meter-long 5V white tri-color LED strips that come packed with 60 SK6812 5050 LEDs. Each of t...
  :::

  **Retired**
  :::::
  :::::::::::

  ::: clearfix
  :::