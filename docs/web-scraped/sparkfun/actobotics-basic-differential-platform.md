# Source: https://learn.sparkfun.com/tutorials/actobotics-basic-differential-platform

## Build Overview

### Introduction

The basic differential bot is a seed platform to help you get started making Actobotics-based robots. This tutorial will go over the basics for building this platform out of Actobotics mechanical parts, available at SparkFun. Control electronics will be covered in some detail but are not the primrary focus of this tutorial, The [wishlist](https://www.sparkfun.com/wish_lists/101884) contains the parts to build an almost-ready-to-drive vehicle. From here, you can add any sensors or mechanisms you like, or customize the layout for your own unique design.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Finished_Pic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Finished_Pic.jpg)

*The Completed Build*

### Required Materials

Here is a list of parts used to build this platform. Feel free to mix and match or completely remix this list for your own robot needs.

\

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Kit_spread_view.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Kit_spread_view.jpg)

*Parts included in this build*

### Required Tools

- [7/64" Hex Key](https://www.sparkfun.com/products/12609) - Use with #6-32 socket head cap screws
- 3/32" Hex Key - Use with set screws in hubs and shaft couplers
- [#1 Philips Screwdriver](https://www.sparkfun.com/products/9146) - Use with M3 pan-head screws
- 7/32" or 5.5mm Open-Ended wrench - Use with M3 nuts
- [Soldering Iron](https://www.sparkfun.com/products/9507) - Use to attach wires to DC motor leads
- [Modeling Knife](https://www.sparkfun.com/products/9200) - Helpful with removing plastic Tamiya parts from the sprue
- [Side Cutters](https://www.sparkfun.com/products/11952) - Helpful with removing plastic Tamiya parts from the sprue
- [Needle Nose Pliers](https://www.sparkfun.com/products/8793) - Helpful with removing plastic Tamiya parts from the sprue

### Additional Supplies

- [Solder](https://www.sparkfun.com/products/9161)
- Hookup Wire [red](https://www.sparkfun.com/products/8023) and [black](https://www.sparkfun.com/products/8022)

### Suggested Reading

This is intended to be an elementary build with no background knowlege required, however, the following links may help you get better acquainted with the concepts in this tutorial.

- [What is an Arduino](https://learn.sparkfun.com/tutorials/what-is-an-arduino?_ga=1.68264785.158945055.1394500308)
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Motors and selecting the right one](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one?_ga=1.169020513.158945055.1394500308)
- [Getting Started with the RedBot](https://learn.sparkfun.com/tutorials/getting-started-with-the-redbot?_ga=1.92998493.158945055.1394500308)
- [How To Solder - Through Hole](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering?_ga=1.92998493.158945055.1394500308)

## Hardware Assembly

### Ball Casters

The first assembly is the Tamiya Ball caster. Follow the included instructions for the 37mm layout.

### Drive Axle Assembly

The next assemblies are the left and right axle.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/DriveAxle.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/DriveAxle.PNG)

*Finished Drive Axle*

These are identical, so repeat this step for the second side. Attach the large rubber tire to the edge of the precision disc wheel. Then attach the ¼" set-screw hub to the wheel with the raised section of the hub inserted into the center hole of the wheel. Secure the wheel to the hub using four #6-32x ¼" screws. Next insert the D-shaft through the set screw hub, such that the flat side of the shaft is facing the set screw.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Setscrew_alignment.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Setscrew_alignment.png)

*Set Screw Alignment with Shaft*

Place the shaft so that about 3/16" is coming out the wheel side of the hub, then tighten the set screw in the hub.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Axle_alignment_profile.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Axle_alignment_profile.png)

*Approximate Pass-through Distance of the Shaft (Bearing and spacer omitted for clarity)*

Once the shaft is in place, slide one shaft spacer over the shaft on the hub side, followed by one flanged bearing. Orient the bearing so the flange is on the hub side, next to the spacer. Finally add the shaft coupler by inserting the shaft into the ¼" side (it won't go into the 6mm side). Again, align the set screw with the flat of the D-shaft and tighten. Repeat for the opposing side.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/DriveAxle-Exploded.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/DriveAxle-Exploded.png)

*Exploded View of Drive Axle*

### Motor Mounts

With the axles done, solder wires to the motor leads. Be sure to note the [polarity](https://learn.sparkfun.com/tutorials/polarity) with regard to your wire color.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Solder_Motors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Solder_Motors.jpg)

*Solder Directly to the Motor Leads*

Next, add the motor to the motor mount.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/MotorMount_assem_1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/MotorMount_assem_1.PNG)

*Motor Mount Assembly*

Holding the motor with the output shaft facing you, and oriented at 6:00, locate the holes at 3:00 and 9:00.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Motor_Face.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Motor_Face.png)

*Motor Alignment Holes*

These holes will align with the holes in the motor mount.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Screen_Shot_2014-12-22_at_1.30.50_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Screen_Shot_2014-12-22_at_1.30.50_PM.png)

*Motor Mount Alignment Holes*

Use the holes labelled '4' to align with the motor. Secure with the provided M3 screws. Repeat for the opposing side.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/MotorMount_assem_Exploded.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/MotorMount_assem_Exploded.png)

*Exploded View of the Motor Mount Assembly*

### Rail Assembly

With the sub-assemblies complete, we can proceed with building the left and right rails. The channels are the structural backbone of the vehicle so the sub assemblies will be added directly to them.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Strux_Rail-Exploded.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Strux_Rail-Exploded.png)

*Adding Sub Assemblies to the Channel*

Start by adding a completed caster to the channel in the location shown and secure with four M3x10mm screws and nuts included in the ball caster kit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Caster_mount_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Caster_mount_annotated.png)

*Caster Alignment and Location*

Next add the two #6-32 clamping screws provided with the tube clamps, but do not tighten. Add the clamps in the indicated locations at the ends of the channels. Orient the clamps so that the clamping screw heads are accessible from the ends of the channels. Secure each clamp with four #6-32 screws. Once secure, insert a ½" tube to the clamp near the caster and tighten the clamping screws to lock the rotation of the tube.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Tube_Clamp_Mount_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Tube_Clamp_Mount_annotated.png)

*Tube and Clamp Alignment and Location*

Finally, add the motor/mount assembly to the center of the channel. The motor should sit in the "up" position away from the casters. Secure the assembly with four #6-32 screws.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Motor_mount_rail_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Motor_mount_rail_annotated.png)

*Motor Mount*

Repeat for the opposing side.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Strux_Rail_1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Strux_Rail_1.PNG)

*Completed Rail*

### Final Mechanical Assembly

With the rails complete, add them together by inserting the free ends of the tubes into the open tube clamps. Tighten the remaining clamp screws to complete the frame. When finished, it should look like this.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Joined_rails.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Joined_rails.PNG)

*Joined Rails*

Finally, add the wheel/axle assemblies to the motor shafts. Again, align the set screw on the axle with the flat side of the motor output shaft. Also, be sure that the bearing has fully inserted into the ½" hole in the channel. Tighten the set screw to secure the axle. Repeat for the opposing side. Add a the channel mount clips to one of the rails across the open side of the channel.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Seed_Platform_assem_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Seed_Platform_assem_annotated.png)

*Final Chassis Assembly*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Seed_Platform_assem_1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Seed_Platform_assem_1.PNG)

*Completed Assembly*

The platform is now complete and ready for control electronics. If you are using an Aruduino Uno or Mega, the board can simply snap into the channel mounts. Tuck a battery behind the mounts and connect the motor lead wires to your motor driver shield.

This example uses the Redbot Mainboard to drive the vehicle via XBee radio control. The Redbot board is secured to the channel using two alternate channel mount clips designed for the RedBoard. The design file is available for download [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Channel_mount_RedBot.DXF) to laser cut a channel bracket for the RedBot Mainboard.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/4/0/Control_electronics_annotated.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/Control_electronics_annotated.PNG)

*RedBot Controller Board with Channel Mount Clips*

## Control System Connection and Setup

If using the Redbot Mainboard, Attach the board as indicated in the previous step. Place the board with the USB facing off the end of the vehicle and the battery jack facing the motor. Attach the lead wires from the motors to the ports on the redbot board. If you are following color convention (i.e. red is positive, black is negative), wire the left motor as indicated on the silkscreen and wire the right motor counter to the silkscreen.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/electronics.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/0/electronics.jpg)

**Leave the XBee off** the board until after the board has been programed. Set the MOTOR switch to STOP and set the POWER switch to ON.

The control sketch uses single-letter [ASCII commands](https://learn.sparkfun.com/tutorials/terminal-basics/basic-terminology-) to affect behavior of the vehicle. To program:

- Plug a Mini-B USB cable into the port on the board, and connect it to your computer.
- Let the FTDI populate on your computer, and open your Arduino environment. (If you need help installing FTDI drivers, visit our [tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)).
- Set the Port number to your Redbot, and set the board to Arduino Uno.
- Load the Receiver Code for Redbot sketch onto the board. If the sketch does not compile, please ensure that your Arduino Environment has the [RedBot Library](https://github.com/sparkfun/RedBot/tree/master/Arduino/libraries/RedBot) installed.
- Set the POWER switch to OFF, unplug the USB from the Redbot, set the MOTOR switch to RUN, set the XBee switch to HW SERIAL, plug in the XBee radio, and attach the 9V Battery.

The vehicle is now complete and ready to drive.