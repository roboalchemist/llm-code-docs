# Source: https://learn.sparkfun.com/tutorials/shapeoko-assembly-guide

## Introduction

[SparkFun\'s Deluxe Shapeoko kit](https://www.sparkfun.com/products/13718) is a Carbide3D Shapoko 3 in fancy SparkFun red with our open source 3 axis mill driver, the [Stepoko](https://www.sparkfun.com/products/13155).

[![Shapeoko Parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/overview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/overview.png)

*The full kit. In this picture, the [Shapeoko parts](https://www.sparkfun.com/products/13713) have been assembled as per the Shapeoko guide, and the [SparkFun kit parts](https://www.sparkfun.com/products/13757) are shown beside it.*

### Guide Content

This guide directs you to the Shapeoko assembly instructions, then goes through the final steps to add the electronics to the mill.

### Required Materials

- [Shapeoko Assembly Instructions](https://drive.google.com/open?id=1qfTWocIAL8LGNLzAT395v2Oa9todR0w5) - Download and read before unboxing. It works well to print two pages per sheet in order to have a copy on hand, and to save trees.
- [Shapeoko Deluxe Kit Contents PDF](https://github.com/sparkfun/SparkFun_Stepoko/raw/master/Documentation/PartsList.pdf) - This list reflects exactly what comes in the deluxe kit and can be used to verify the shipment before starting assembly.
- A meter or so of [spare wire](https://www.sparkfun.com/products/11375).
- A [soldering iron](https://www.sparkfun.com/products/9507) and some [solder](https://www.sparkfun.com/products/9325).
- A [multimeter](https://www.sparkfun.com/products/12966).
- A 2.5mm hex wrench for belt clips.
- Pliers or small adjustable wrench.

### Suggested Reading

[Stepoko Guide](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide) - This guide talks about how the Stepoko control electronics works. Important information is also linked below.

## Assembly

1.  Follow the [Shapeoko assembly instructions](https://drive.google.com/open?id=1qfTWocIAL8LGNLzAT395v2Oa9todR0w5) until you get to the part where controller is added. There are a few differences, for instance the motors in this kit have equal length wires, but nothing too significant. Use the [parts list](https://github.com/sparkfun/SparkFun_Stepoko/raw/master/Documentation/PartsList.pdf) from downloaded from the \"Required Materials\" section above rather than the list from the assembly guide.

    ::: 
    **[] Set Aside Some Time** It may take about four hours to complete the initial assembly. Once you\'ve got it, continue on.
    :::

2.  Install the Shapeoko into the enclosure. There are 10 4-40 screws for this purpose, but you\'ll only need 8. Use a number 1 phillips screwdriver.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-37.jpg)

    *To get the Stepoko into the enclosure, put the \'port end\' in first.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-38.jpg)

    *Installing the 4-40 screws*

3.  Get ready to install the controller. Test fit it first, but don\'t install just yet, set it down such that the pad can be added, and then it can be rotated into position. Make sure the aluminum heatsink and extruded mill rail are clean and free of debris.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-39.jpg)

    *Test fitting the enclosure \-- the motor wires will go through the top*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-02-ARROW.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-02-ARROW.jpg)

    *Here the enclosure is ready to rotate up onto the mill into the correct orientation. This picture is shown with the wires installed. Don\'t worry if yours are not installed yet, that will be covered later.*

4.  Peel one side\'s protective sheet away and discard. Both sides will be removed, but just peel one for now.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-03.jpg)

    *Peeling the protective sheet. Once removed, the rigidity of the material changes completely*

5.  Holding by the corners, lower the pad onto the exposed heat sink, and gently press into place. Generally, it just needs to be centered and overlapping the edge of the heat sink. It\'s been sized so that the following two points can insure it\'s in the correct position:

    - The long edge is flush with the enclosure\'s edge, towards the motor wires.
    - The short edge is flush with the keyholed mounting hole.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-04.jpg)

    *Lowering the pad*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/7/Shapeoko_Thermal_Pad_Intstallation-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/7/Shapeoko_Thermal_Pad_Intstallation-05.jpg)

    *Checking for proper alignment. Here, my thumb checks flushness on one edge while I point out the proper alignment near the mounting hole.*

6.  Peel the second protective layer away.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-06.jpg)

    *Removing the protective sheeting*

7.  Install the Stepoko controller. The pad will add thickness and cause the enclosure to sit off the mill, so don\'t tighten the mounting bolts down too hard. Use threadlocker to keep the screw from backing out due to vibrations. Alternately, a flat washer that\'s slightly thinner than the pad can be used here.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-07.jpg)

    *Applying threadlocker \-- Here, a bit too much is used. It only needs to be filling in the treads. Excess may run.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Thermal_Pad_Intstallation-08.jpg)

    The finished installation. Notice that the enclosure is nice and even and not deformed along the mill.

8.  Install the enclosure to the rail with the terminal connections at the top. Use the extra M6x12mm bolts provided with the Shapeoko.

9.  Connect the X and Z axes to the Stepoko. For more information, check the Stepoko guide\'s [Hardware: Connecting the Motors](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide#hardware-connecting-the-motors) section.

    - [Tin the wire ends](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering#advanced-techniques-and-troubleshooting) with some solder.
    - [Identify which pairs of wire are connected](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#continuity) inside the motors with your meter.
    - Match the coils to the winding symbols on the Stepoko. Either polarity or A-B position will work, but may make the motors spin the other way. This can be changed in software.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-40.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-40.jpg)

    *The X and Z axis are connected.*

10. Connect the Y axis. But wait! **It has two motors that are wired in parallel**.

    If two stepper motors are connected in parallel, they may not spin in the same direction because the internal polarities may not be the same. The solution to this problem is to transpose the colors of one pair of coil wires. This polarity/spin direction problem is compounded by the fact that the motors are mirrored on the mill and actually need to spin different directions.

    Watch the video below go get a basic idea, then work through these steps.

    - Connect short leads to the Y axis terminals.
    - Identify the coils.
    - Group one coil from each motor together by color, except with reversed polarities.
    - Twist the ends to test.
    - Try and move the mill in the Y axis. If it moves smoothly, solder the wires and apply heatshrink/electrical tape, or use wire nuts.
    - If the axis moved roughly, unlike the X and Z axes, filp *one* of the pairs of coils so that it has the same colors combined, but leave the other reversed. This is because the motor\'s coils are not always wired the same internally.

    ::::: 
    :::: 
    ::: 
    :::
    ::::

    *Take a quick look at this video to see, and hear, how the Y axis when wired incorrectly, and correctly.*
    :::::

11. Set the motor drive currents. Make sure the trimpots are in the center for 1A service until you are more experienced. Or, read up on how the current setting works in the Stepoko Guide\'s [Hardware: Setting the current](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-setting-the-current) section.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/potscentered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/potscentered.jpg)

    *The trimpots are centered for 1 A drive in this photograph.*

12. Mount the switch to a free hole on the gantry end plate and solder on leads.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-30.jpg)

    *Here the switch has been mounted and the switch wires are being measured. They go into the two terminals labled E-Stop.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-31.jpg)

    *Soldering on the leads.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-32.jpg)

    *All of the wires are added for this mill setup.*

13. Screw in the lid to the enclosure using a number 1 or 2 phillips.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-33.jpg)

14. Collect your wires and bind with twist ties or zip ties.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-34.jpg)

    *The Y axis wires have been twist tied together here. The X and Z axes are gently pulled out to see how long they are.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-35.jpg)

    *With the X axis moved ofer to one end, I can see that my bound wires have enough slack so that they won\'t be pulled on when the carriage moves.*

    ::: 
    **Caution:** If milling conductive materials, be sure to seal up the openings where the wires pass through. Conductive dust that enters the enclosure can short out the circuits.
    :::

15. Connect the power supply, power cord, and USB cord between your computer and the Stepoko

16. Open up the Universal Gcode Sender, open the Stepoko\'s serial port, and select the machine control tab. Set the switch to \'ON\' and try to move the machine by computer control. If the axis move in the wrong directions to your liking (but of course, up should be positive Z), switch the direction bit field accordingly. Use the Stepoko guide\'s [Software: Machine Control](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/software-machine-control-universal-g-code-sender) section for more information about grbl, or check out grbl\'s Github [wiki](https://github.com/winder/Universal-G-Code-Sender/wiki) for more information on changing settings.

17. Measure know movements and calibrate each axis. See the Stepoko guide\'s [Firmware: Configuring grbl and Calibrating](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide#firmware-configuring-grbl-and-calibrating) section for more info.

## Finishing Touches

The [cable carriers](https://www.sparkfun.com/products/13207) have been included in your kit to help with wire management, but it\'s up to you to decide what cables to carry and where you you would like them to be. They can go either way on an axis and don\'t need to be full length to get the job done.

This section shows the installation of a cable carrier between the mill head and the cross-rail. The process is the same for any axis.

1.  Start by finding the location and length of the cable carrier. Hold the fixed end of the carrier in where you think it should go, and move the mill head through the full range to make sure the cable carrier has unrestrained motion along the axis of movement. Alternately, mimic the motion of the mill to approximately check the motion. The cable carrier should be shortened if there\'s not enough play in the wires or if the loop hangs too far off the mill.

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       [![](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update-09.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update-08.jpg)
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    *Mimic the motion of the axis to get a good idea where to mount the fixed end and how long the carrier needs to be.*

2.  Pull the wires through the carrier. A hooked wire or tape on a straight wire helps. When running multiple groups of similar colors through, mark each set differently with sharpie or tape.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-02.jpg)

    *Use a helper wire to thread the cable carriers. Here, four of the eight wires have a tape wrap to indicate that they belong to the same motor*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-03.jpg)

    *The wires are probably not long enough to pull through with a bend, so carefully work the ends free.*

3.  After you\'ve located where the fixed end will be, cut a small piece of double-sided tape, and firmly squish the carrier down. For these Shapeoko mills, make sure nothing crosses the center line in the extrusion.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-05.jpg)

    *Here, the tape is being dispensed directly onto the location and cut right in place. Notice that it does not cross the center line.*

4.  Check that the wires will reach the terminals, that the axis has a full range of motion, and that the roller bolt misses the cable carrier. Then connect the motor wires for the final time.

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-06.jpg)

    *A view of the installed cable carrier. Also shown, the strip of cable carrier on the enclosure is a convenient place to stuff fixed wires \-- just pull them in with your wire hook. This is made from extra bits of the other carriers from when they were shortened.*

    [![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update_Images-07.jpg)

    *The roller clears the cable carrier with no problems! If this is not the case, simply peel up the cable carrier, and try again.*