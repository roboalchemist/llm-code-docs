# Source: https://learn.sparkfun.com/tutorials/working-with-wire

## Introduction

When someone mentions the word wire, they are more than likely referring to a flexible, cylindrical piece of metal that can vary in size from just a few millimeters in diameter to several centimeters. Wire can refer to either a mechanical or electrical application. An example of a mechanical wire could be a [Guy-wire](http://en.wikipedia.org/wiki/Guy-wire), but this this guide will focus on electrical wiring.

[![stripped stranded wire](//cdn.sparkfun.com/r/600-600/assets/4/7/4/6/6/51155039ce395f2754000001.JPG)](//cdn.sparkfun.com/assets/4/7/4/6/6/51155039ce395f2754000001.JPG)

*Inside a stranded wire*

Electrical wire is a backbone of our society. There is wire in houses to turn on lights, heat the stove, and even talk on the phone. Wire is used to allow [current](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/current) to flow from one place to another. Most wires have insulation surrounding the metallic core. An electrical insulator is a material whose internal electric charges do not flow freely and, therefore, does not conduct an electric current. A perfect insulator does not exist. However, some materials such as glass, paper, and Teflon, which have high resistivity, are very good electrical insulators. Insulation exists because touching a bare wire could allow current to flow through a person\'s body (bad) or into another wire unintentionally.

### Recommended Reading

Here are some topics you might want to explore before reading about wire:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units)

### Metric Prefixes and SI Units 

This tutorial will explain how to use and convert between the standard metric prefixes.

## Stranded vs Solid Core Wire

Wire can come in one of two forms: solid or stranded core.

### Solid Core

Solid wire is composed of a single piece of metal wire, also known as a strand. One very common type of solid wire is known as [wire wrap](http://en.wikipedia.org/wiki/Wire_wrap).

[![Stripped Solid Wire](//cdn.sparkfun.com/assets/f/7/7/9/1/51155039ce395f6140000006.jpg)](//cdn.sparkfun.com/assets/f/7/7/9/1/51155039ce395f6140000006.jpg)

*Various colors of solid core wire*

### Stranded Core

Stranded wire is composed of many pieces of solid wire all bundled into one group. It is much more flexible than solid wire of equal size.

[![Stranded Wire](//cdn.sparkfun.com/r/600-600/assets/2/6/4/7/8/51155039ce395fe53f000006.jpg)](//cdn.sparkfun.com/assets/2/6/4/7/8/51155039ce395fe53f000006.jpg)

*Various colors and sizes of stranded wire*

### Applications of Solid and Stranded Core Wire

Since stranded wire is more flexible than solid core wire of equal size, it can be used when the wire needs to move around frequently, in a robot arm for example. Conversely, solid wire is used when little or no movement is needed, such as prototyping [circuits](http://learn.sparkfun.com/tutorials/what-is-a-circuit) on a [breadboard or protoboard](https://www.sparkfun.com/categories/301). Using solid core wire makes it easy to push the wire into a breadboard and plated through holes of a printed circuit board.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Solid Core Wire Used on a Breadboard for Prototyping](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/0/babysitter-microview.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/0/babysitter-microview.jpg)   [![Solid Core Wire Being Soldered in Through Hole](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/2/4x4_RGB_Button_Pad_Hookup_Guide-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/2/4x4_RGB_Button_Pad_Hookup_Guide-21.jpg)
  *Solid Core Wire Used in a Breadboard with the [Battery Babysitter](https://learn.sparkfun.com/tutorials/battery-babysitter-hookup-guide)*                                                                                            *Solid Core Wire Soldered into a Plated Through Hole with the [Button Pad Breakout Board](https://learn.sparkfun.com/tutorials/button-pad-hookup-guide)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Trying to use stranded wire on a breadboard or plated through hole can be very difficult depending on the thickness as the strands want to separate as they are pressed in.

[![stranded wire partially separated in breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Stranded_Core_Wire_in_BreadBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Stranded_Core_Wire_in_BreadBoard.jpg)

**Tip:** Trying to connect stranded wires to screw terminals, breadboards, or through holes? Try twisting the wire and tinning the tips. Below is an example with a stepper motor in the [Stepoko Hookup Guide](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide). The wire ends looking pretty ratty from the factory.\
\
[![Exposed Stranded Wires](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-01_showing_wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-01_showing_wires.jpg)\
\
The image on the left shows the wire strands being twisted by giving them about 180 degrees of twist along the length of the strip. The image on the right shows the wires being tinned with soldered. Apply excess solder to allow the flux to work, and pull the extra solder off with the iron yielding a solid cylinder of wire.\
\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-02_twisting_wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-02_twisting_wires.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-04_tinning2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-04_tinning2.jpg)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Keep in mind, that a soldered joint (of a tinned tip) can fracture under mechanical stress and thermal cycling may cause joint failure.

## Wire Thickness

The term 'gauge' is used to define the diameter of the wire. The gauge of a wire is used to determine the amount of [current](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/current) a wire can safely handle. Wire gauge can refer to both electrical and mechanical. This tutorial will only cover electrical. There are two main systems for measuring gauge, [American Wire Gauge (AWG)](http://en.wikipedia.org/wiki/American_wire_gauge) and [Standard Wire Gauge (SWG)](http://en.wikipedia.org/wiki/Standard_Wire_Gauge). The differences between the two are not critical to this guide.

[![Wire Gauges](//cdn.sparkfun.com/assets/9/a/f/6/e/51155039ce395f0805000006.jpg)](//cdn.sparkfun.com/assets/9/a/f/6/e/51155039ce395f0805000006.jpg)

*An approximate scale of several different gauges of wire*

The amount of current that a wire can carry depends on a few different factors, for example the composition of the wire, wire length, and condition of the wire. In general, thicker wire can carry more current.

[![Amps to Gauge](//cdn.sparkfun.com/assets/f/d/2/3/3/51155039ce395f5e3d000002.jpg)](//cdn.sparkfun.com/assets/f/d/2/3/3/51155039ce395f5e3d000002.jpg)

*An approximate wire thickness to current capability chart*

Here at SparkFun, we typically use **22 AWG** wire for prototyping and breadboarding. When using a breadboard or PCB, solid core is perfect because it fits nicely into the holes. For other prototyping/building involving soldering, the stranded core is #1, just be sure not to let too much current run through a single wire. It will get hot and could melt!

SparkFun carries a variety of both solid and stranded 22 AWG wire.

[![Jumper Wire Kit - 140pcs](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/00124-Jumper_Wire_Kit_-_140pcs-01.jpg)](https://www.sparkfun.com/jumper-wire-kit-140pcs.html)

### [Jumper Wire Kit - 140pcs](https://www.sparkfun.com/jumper-wire-kit-140pcs.html) 

[ PRT-00124 ]

This is a time saving kit of 140 jumper wires - cut, stripped, and pre-bent for your prototyping pleasure.

[ [\$8.95] ]

[![Large Jumper Wire Kit - 700pcs](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/6/9/14671-Jumper_Wire_Kit_-_700pcs-01.jpg)](https://www.sparkfun.com/large-jumper-wire-kit-700pcs.html)

### [Large Jumper Wire Kit - 700pcs](https://www.sparkfun.com/large-jumper-wire-kit-700pcs.html) 

[ PRT-14671 ]

This is a time saving large kit of 700 jumper wires - cut, stripped, and pre-bent for your prototyping pleasure.

[ [\$37.95] ]

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[Click to Browse More Wire Options!](https://www.sparkfun.com/categories/141)

However, there is still an option to use **30 AWG** wire wrap if you need to go smaller.

[ ![Wire Wrap Wire - Blue (Solid, 30AWG, 100ft)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/9/8/14913-Hook-up_Wire_Blue__Solid__30AWG__100ft_.jpg) ]

### Wire Wrap Wire - Blue (Solid, 30AWG, 100ft) 

[ PRT-14913 ]

This is a 100ft spool of blue wire wrap wire. These wires are 30AWG with solid cores.

**Retired**

[ ![Wire Wrap Wire - White (Solid, 30AWG, 100ft) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/9/9/14914-Hook-up_Wire_White__Solid__30AWG__100ft_.jpg) ]

### Wire Wrap Wire - White (Solid, 30AWG, 100ft)  

[ PRT-14914 ]

This is a 100ft spool of white wire wrap wire. These wires are 30AWG with solid cores.

**Retired**

**Tip:** Wire wrap was first used to [build prototype circuits](http://en.wikipedia.org/wiki/Wire_wrap). In this day and age, it is much less common. However, it is still useful for connecting to small pins on a surface mount component or PCB, projects with small spaces, or repairing boards (i.e. \"[\"Green\" Wire Repairs](https://www.sparkfun.com/tutorials/99)).\
\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  [![Wire Wrap Making a Connection on a PCB\'s Small SMD Pins](https://cdn.sparkfun.com/r/500-400/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-03.jpg)](https://learn.sparkfun.com/tutorials/tech-prank-hardware-mouse-jiggler)   [![30 AWG Wire Wrap Used in Small Spaces](https://cdn.sparkfun.com/r/500-400/assets/learn_tutorials/3/7/8/InsertingMic.jpg)](https://learn.sparkfun.com/tutorials/heartbeat-straight-jacket#hacking-a-stethoscope)   [![PCB Trace Accidentally Damaged](https://www.sparkfun.com/images/tutorials/SMD_HowTo/RedWireFix-4.jpg)](https://www.sparkfun.com/tutorials/99)
  Wire Wrap connecting to a PCB\'s small SMD pins that are broken out on the [Hardware Mouse Jiggler](https://learn.sparkfun.com/tutorials/tech-prank-hardware-mouse-jiggler).                                                         Wire Wrap used in projects with small spaces of the [Heartbeat Straight Jacket](https://learn.sparkfun.com/tutorials/heartbeat-straight-jacket).                                                                     [\"Green\" Wire Repairs](https://www.sparkfun.com/tutorials/99) with a bad PCB design or damaged pad.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------

**Working with thick wire?** Wire wrap is also useful when splicing thick wire. For more information, check out the tutorial on [Building an Autonomouse Vehicle](https://learn.sparkfun.com/tutorials/building-an-autonomous-vehicle-the-batmobile/wire).\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/5/8/9/Soldering_Wire.jpg)](https://learn.sparkfun.com/tutorials/building-an-autonomous-vehicle-the-batmobile/wire)

## How to Strip a Wire

Safe, durable electrical connections begin with clean, accurate wire stripping. Removing the outer layer of plastic without nicking the wires underneath is critical. If a wire does get nicked, the connection may break or an electrical short may occur.

[![Nice Wires](//cdn.sparkfun.com/r/400-400/assets/f/7/7/9/1/51155039ce395f6140000006.jpg)](//cdn.sparkfun.com/assets/f/7/7/9/1/51155039ce395f6140000006.jpg)

*No nicks or gouges. These wires have been properly stripped*

### The Tools

#### Manual Wire Stripper

A simple manual [wire stripper](https://www.sparkfun.com/products/12630) is a pair of opposing blades much like scissors. There are several notches of varying size. This allows the user to match the notch size to the wire size, which is very important for not damaging the wires. Depending on the manufacturer, there may be additional features that include a locking mechanism, have an ergonomic handle, and the ability to cut screws.

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Wire Strippers - 20-30 AWG](https://cdn.sparkfun.com/r/600-600/assets/parts/2/3/9/4/7/24771-Wire-Strippers-Feature.jpg)](https://www.sparkfun.com/wire-strippers-20-30-awg.html)

### [Wire Strippers - 20-30 AWG](https://www.sparkfun.com/wire-strippers-20-30-awg.html) 

[ TOL-24771 ]

This wire stripper and cutter works with six standard wire sizes from 20 to 30 AWG.

[ [\$20.95] ]

[] **Warning:** Many wire strippers found at the hardware store do not strip small gauge wire (22 to 30). When getting into prototyping, be sure to get a tool that is capable of stripping 22 AWG and smaller. Being able to strip very small 30 AWG wire (also known as wire wrap wire) is a plus.

Although a knife would also strip the wires, it may also damage the wire by nicking the metal or cutting into it. Using a knife to strip wire is also really dangerous! The knife can easily slip and cause wicked injuries.

#### Self-Adjusting Wire Stripper

There are also self-adjusting wire strippers that automatically strip wire by placing a wire in the middle of the teeth and squeezing the handle. These take almost any wire and perfectly strip the wires every time. Depending on the manufacturer, there may be additional features included to cut or crimp insulated/non-insulated wires.

[![Self-Adjusting Wire Strippers](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/4/8/14872-Self-Adjusting_Wire_Strippers-04.jpg)](https://www.sparkfun.com/products/14872)

### [Self-Adjusting Wire Strippers](https://www.sparkfun.com/products/14872) 

[ TOL-14872 ]

The Self-Adjusting Wire Stripper can take a wire, placed in the head of the tool, compress the handles, and you will have a p...

**Retired**

**Tip:** The self-adjusting wire stripper are also useful for removing sheaths from cables or stripping multiple insulated wires simultaneously.

**Note:** We have found that the self adjusting wire stripper tool is very useful when modifying EL wire. Simply place the EL wire in the middle of the teeth and adjust the knob to reduce the grip on the wire. Make sure the corona wires are not directly under the teeth when stripping the wire.\
\

\>[![Stripping EL Wire with Self-Adjusting Wire Stripper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/9/Self-Adjusting-Wire-Stripper-EL-Electroluminescent_-Inner-Sheath-Removed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/9/Self-Adjusting-Wire-Stripper-EL-Electroluminescent_-Inner-Sheath-Removed.jpg)

#### Wire Wrap Tool

If you are using a wire wrap tool to wrap a wire around a pin, there may already a built-in stripper blade in the middle to strip the thin wire. Simply place the wire between the blades and pull.\

[ ![Wire Wrap Tool](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/2/0/0/14915-WireWrap_Tool_.jpg) ]

### Wire Wrap Tool 

[ TOL-14915 ]

This Wire Wrap Too wraps, unwraps, and even strips the appropriate wire diameter with a unique built-in stripper blade.

**Retired**

### Stripping the Wire with Manual Wire Strippers

By simply squeezing the handles of a manual wire stripper about 1/4\" from the end of the wire or the desired length, using the correct notch on the tool, and then twisting it slightly, the insulation will be cut free.

[![Wire in Stripper](//cdn.sparkfun.com/r/600-600/assets/0/5/0/0/f/5138de3cce395fbb1b000002.JPG)](//cdn.sparkfun.com/assets/0/5/0/0/f/5138de3cce395fbb1b000002.JPG)

Then by pulling the wire strippers towards the end of the wire, the insulation should slide right off of the wire.

[![Wire After Strip](//cdn.sparkfun.com/r/600-600/assets/3/9/5/5/f/5138de3cce395f9329000001.JPG)](//cdn.sparkfun.com/assets/3/9/5/5/f/5138de3cce395f9329000001.JPG)

### Stripping Cable Wires with Self-Adjusting Wire Strippers

The special self-adjusting wire strippers makes it easy to remove sheaths and stripping multiple insulated wires. For this example, we are going to wire strip a power cable. Place the end of the cable between the tool\'s wire cutter to cut. When ready, squeeze the handles tp cut the cable end.

[![Cut Cable Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Cutter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Cutter.jpg)

Turn the plastic guide away from the head and slide it out to adjust the wire length to cut. Reposition the plastic guide when you are satisfied with the wire length. For cables, you may want to strip more than the recommended guide.

[![Adjust cable Length to Cut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Adjust-Strip-Length.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Adjust-Strip-Length.jpg)

Insert the cable between the jaws. If necessary, increase/decrease the tension of the jaw using the tension knob as necessary depending on the cable and wire size.

[![Insert Cable Between Self-Adjusting Wire Stripper\'s Jaws](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Removing-Sheath.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Removing-Sheath.jpg)

While holding the cable in place, squeeze the handles to strip the sheath from the cable.

[![Part of Cable Sheet being Stripped](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Sheath-Stripped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Sheath-Stripped.jpg)

After sliding the sheeth from the cable, place the internal wires between the teeth. Adjust the tension of the jaw using the tension knob as necessary depending on the cable and wire size.

[![Stripping multiple wires in a cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Multiple-Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Multiple-Wires.jpg)

**Note:** Make sure to place the internal wires between the left jaw\'s teeth to strip the cable\'s wires.

When finished, your cable wires should be perfectly stripped!

[![Cable Wires Perfectly Stripped](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Perfectly-Stripped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Self-Adjusting-Wire-Stripper-Perfectly-Stripped.jpg)

### Tips, Tricks, and Hints

It is important to match the size of wire to the correct notch in the stripper. If the notch is too large, the wire will not get stripped. If the notch is too small, there is a risk of damaging the wire. Using an undersized notch means the strippers will close too far, digging into the wire underneath. With stranded wire, the tool will cut off the outer ring of wires, decreasing the total diameter of wire and reduce the strength of the wire. A nick in solid core wire will severely reduce the strength and flexibility of the wire. The likelihood of the wire breaking upon being bent increases significantly.

[![Damaged Wire](//cdn.sparkfun.com/r/600-600/assets/7/f/6/7/9/5138de3cce395f3c1d000001.JPG)](//cdn.sparkfun.com/assets/7/f/6/7/9/5138de3cce395f3c1d000001.JPG)

*This wire was not stripped properly, there are gouges and missing strands*

If a wire does accidentally get a nick in it, the best plan of action is to cut the damaged part of the wire off and try again.

## How to Splice Wires

Prepare the wire by stripping the wires ends using a wire stripper. If you are working with stranded wire, try twisting the ends to group the strands together and tinning the tips before soldering.

[![Striped Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Strip_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Strip_Wire.jpg)

Cut a piece of heat shrink to cover the exposed wires. Slide the heat shrink through one of the wires. Make sure to slide the heat shrink away from area where you are splicing.

[![Adding Heat Shirnk](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Adding_Heat_Shrink_Insulation.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Adding_Heat_Shrink_Insulation.jpg)

Face the wire terminals toward each other and touch the exposed ends together.

[![Touch Exposed Wires Together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Align_Wire_Ends.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Align_Wire_Ends.jpg)

Hold the wires together by using tape to hold the wires in place against a soldering mat.

[![Hold Wires Down Against Soldering Mat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Hold_Wires_Down.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Hold_Wires_Down.jpg)

**Tips:** Besides taping the wire down against a soldering mat, try using a [third hand](https://www.sparkfun.com/categories/377) or [3D printing clamps](https://www.sparkfun.com/news/2661) to hold the wires in place.\
\

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![3rd Hand Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/1/Soldering.jpg)](https://learn.sparkfun.com/tutorials/pokmon-go-patches-with-el-panels#adding-extension-cables)   [![3rd Hand Wires](https://cdn.sparkfun.com/r/600-600/assets/home_page_posts/2/6/6/1/3D_Printed_Helping_Hand_Blog-01.jpg)](https://www.instagram.com/p/BVk6kPWlJJG/)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add solder to the wires. Try not to leave the soldering iron on the wires too long. The insulation can melt away exposing more wire.

[![Add Solder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wires.jpg)

Ensure that the underside of the wire is also soldered.

[![Check the Underside of the Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wire_Ends_Thoroughly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wire_Ends_Thoroughly.jpg)

Flip the wire over and spread solder over the wires. If necessary, add flux and solder to cover wires.

[![Spread Solder on both sides of wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wire_Ends.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Solder_Wire_Ends.jpg)

If you are using heat shrink, slide it over the terminal to insulate the connection. Apply heat to the heat shrink from a soldering iron or a hot air rework station.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Heat Shrink and Soldering Iron](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Heat_Shrink_Soldering_Iron_Wand.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-Heat_Shrink_Soldering_Iron_Wand.jpg)   [![ Heat Shrink Tube and Hot Air](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-_Heat_Shrink_Hot_Air_Rework_Station.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Splicing_Wire-_Heat_Shrink_Hot_Air_Rework_Station.jpg)
  *Heat from a Soldering Iron*                                                                                                                                                                                                                                  *Heat from Hot Air Rework Station*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When complete, the heat shrink should fit over the exposed wire.

[![Completed Heat Shrink](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Completed_Spliced_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Completed_Spliced_Wire.jpg)

**Tips:** Looking for more ideas and methods of slicing wire? Try twisting the wires together. You can have the twisted wires [facing each other (a.k.a. twisted helix)](https://www.instagram.com/p/BAxjn_xDa09/) or [in the same direction](https://learn.sparkfun.com/tutorials/iot-weight-logging-scale#hardware-hookup).\
\

[![twisting wires in same direction](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/1/IoT_Scale_Tutorial-06.jpg)](https://learn.sparkfun.com/tutorials/iot-weight-logging-scale#hardware-hookup)

\
You can also try hooking and twisting the wires together in a [Western Union splice (a.k.a. Lineman\'s Splice)](https://makezine.com/2012/02/28/how-to-splice-wire-to-nasa-standards/). This method is ideal for solid core wire but it can be used on stranded wires.\
\

[![hooking and twisting wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Splicing_Wire-Hooked_Twisted_Wires.jpg)](https://makezine.com/2012/02/28/how-to-splice-wire-to-nasa-standards/)

\
For advanced users, you could also tap into the wire for a [Western T-splice](https://en.wikipedia.org/wiki/T-splice) instead of cutting straight through wire. This is useful when adding a component(s) (i.e. a pull-up resistor) if you have a limited amount of space to work with to save time and reduce costs. Simply strip the middle of your wire, remove the insulation using a hobby knife/soldering iron, wrap a separate wire/terminal to the exposed wire, and solder. When finished, add some heat shrink or hot glue for insulation. The image below shows a resistor and wire being added to the middle of two wires.\
\

[![Wire Tapped for a Western T-Splice with Resistor and Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/11-jumper_setup.jpg)](https://learn.sparkfun.com/tutorials/photon-remote-water-level-sensor#build-the-pump-controller)\
\
*Western T-Splice Method Used to Connect 3 Jumper Wires and 10kΩ Resistor*

**Tip:** Having trouble splicing wires together or connecting wires to a pin? Try using a PCB as a support when soldering similar to the one built in the custom EL wire extension cable.\
\

[](https://learn.sparkfun.com/tutorials/how-to-make-a-custom-el-wire-extension-cable)

### How to Make a Custom EL Wire Extension Cable 

October 24, 2018

In this tutorial, we will make a custom EL Wire extension cable as an alternative to splicing wire.

## How to Crimp an Electrical Connector

An electrical connector is a device for joining electrical circuits together using a mechanical assembly. The connection may be temporary or serve as a permanent electrical joint between two wires. There are [hundreds of types of electrical connectors](https://learn.sparkfun.com/tutorials/connector-basics). Connectors may join two lengths of wire together or connect a wire to an electrical terminal.

Below area few connector types. On the far, upper left, we have an **insulated splice connector** to connect two wire ends together. To the right, the **forked connector (a.k.a. spade, or split ring)** is useful for connecting wire to [screw terminals by sliding the fork into a screw terminal\'s socket](https://cdn.sparkfun.com/assets/learn_tutorials/7/7/9/Insert_Hot_Wire_Spade_Connector_Between_Metal_Square_Nuts_1.jpg). Screws can be partially screwed in before installing the terminal. The **ring terminals** in the middle are also useful for connecting wire to screw terminals. While the ring terminal provides a more reliable connection, you would need to completely remove the screw before installing the terminal. On the far, upper right we have a **male spade connector (a.k.a. blade)**. These can slide into the **female spade connector (a.k.a. double crimp)** that is shown on the bottom right. Depending on the design and application, these connectors can come in different flavors like flanged fork or locking ring terminal.

[![Connector Types](//cdn.sparkfun.com/r/600-600/assets/9/1/8/9/9/5138de3bce395f591d000000.JPG)](//cdn.sparkfun.com/assets/9/1/8/9/9/5138de3bce395f591d000000.JPG)

*Insulated Splice, Forked, Ring, Male Spade and Female Spade Connectors*

These connectors can also come in different sizes and ratings. The image shown below shows a [1/4\"](https://www.sparkfun.com/products/14407) and [2.8mm](https://www.sparkfun.com/products/14424) female spade connector.

[![Different Sizes for Female Spade Connector](https://cdn.sparkfun.com/r/300-300/assets/parts/1/2/1/1/0/Comparison-01.jpg)](https://cdn.sparkfun.com//assets/parts/1/2/1/1/0/Comparison-01.jpg)

You will want to match the size of the connectors for a secure connection. The image below shows 1/4\" female spade connectors connecting to a microswitch\'s male spade terminals.

[![Male and Female Spade Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/5/Exp2_Step3Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Exp2_Step3Hookup.jpg)

### What is a Crimp?

The word [crimping](https://en.wikipedia.org/wiki/Crimp_(electrical)) in this context means to join two pieces of metal together by deforming one or both of them to hold the other. The deformity is called the crimp.

[![crimped](//cdn.sparkfun.com/r/600-600/assets/3/c/7/2/5/5138de3cce395f141b000000.jpg)](//cdn.sparkfun.com/assets/3/c/7/2/5/5138de3cce395f141b000000.jpg)

*The metal has been deformed to pinch the wire and hold it in place*

### The Tool

In order to crimp connectors onto a wire, a special tool is require for the crimp pin. There are several different styles of crimpers available depending on the crimp pin.

#### Ratchet Crimp Tool

The best crimper has a built-in ratchet. As the handles are squeezed together, it will ratchet and prevent the jaws from opening back up. When enough pressure has been applied, the ratchet will disengage and release the crimped part. This ensures enough pressure has been applied. This style of crimper also has a wide jaw to cover more surface area on the connector.

[![Ratchet Syle Crimp Tool for Quick Disconnect Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Quick_Disconnect_Crimping_Tool_Ratchet.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Quick_Disconnect_Crimping_Tool_Ratchet.jpg)

*Ratchet Crimp Tool for Quick Disconnectors*

Depending on the size of the connector, the type of the \"die\" (i.e. the crimp tool\'s head) will be sized differently. The crimp tool below uses a different die to crimp smaller crimp pins that slide into a pin connector housing.

[![Ratchet Syle Crimp Tool for Crimp Pins](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/19193-03-crimp_pin_pliers.jpg)](https://www.sparkfun.com/products/13193)

*[Ratchet Crimp Tool](https://www.sparkfun.com/products/13193) for Crimp Pins*

The images below show different gauges of wire crimped to forked connector and crimp pin for a polarized connector.

  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com//assets/parts/1/1/9/5/8/14093-02.jpg)](https://www.sparkfun.com/products/14093)   [![](https://cdn.sparkfun.com//assets/parts/6/6/6/08100-Action.jpg)](https://www.sparkfun.com/products/8100)
  *Fork Connectors Crimped for a Wall Adapter*                                                                    *Crimp Pin Crimped Before Being Inserted to a Plastic Housing*
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------

#### Manual Crimp Tool

Manual crimping tools can achieve nearly the same results, although it requires the user be much more vigilant. This style of crimper is generally less sturdy. Attention must be given while crimping to ensure the jaws are lined up properly on the connector. Misalignment will cause a less than desirable crimp connection. Over time, wear and tear from normal usage can also cause the jaws to become separated and not close fully. Generally, squeezing it as hard as possible will be sufficient. The fancy wire stripper shown below can be used with quick disconnects. The tool can also be used to cut wire and strip wires/cables.

[![Manual Crimper on the Self-Adjusting Wire Stripper](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/14872-Self-Adjusting_Wire_Stripper_Crimper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/14872-Self-Adjusting_Wire_Stripper_Crimper.jpg)

*Manual Crimper on the [Self-Adjusting Wire Stripper](https://www.sparkfun.com/products/14872) for Insulated and Non-Insulated Spade Connectors*

While the self-adjusting wire stripper is a bit harder to work with than a ratchet, it has the ability to strip, cut, and crimp a quick disconnect.

![Wire Stripping and Crimping a Spade Connector](https://cdn.sparkfun.com//assets/parts/1/3/1/4/8/Self-Adjusting_Wire_Strippers.gif)

**Warning!** Pliers are not crimpers! Neither are hammers, vises, needle nose pliers or flat rocks. A good crimper when used correctly will make a cold weld between the wire and the barrel of the connector. If you were to cut a well executed crimp in half you would see a solid form of wire and connector. Using the wrong tool will not achieve a good crimp!\
\

[![Crimping pins the wrong way with needle nose pliers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimping_Pins_the_Wrong_Way_Pliers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimping_Pins_the_Wrong_Way_Pliers.jpg)

\
Why is this level of perfection required? A poor crimp leaves air pockets between the wire and connector. Air pockets allow moisture to collect, moisture causes corrosion, corrosion causes resistance, resistance causes heat, and may ultimately lead to breakage.

### Crimping a Quick Disconnect Connector

There are several arguments for and against using solid core wire with crimp connections. Many believe crimping to solid core wire creates a weak point in the wire, which can lead to breakage. There is also a greater chance for a crimp connection to come loose with solid core wire because the wire will not conform to the terminal as well. If you *must* use solid core wire, it is a good idea to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the wire in place after you crimp it.

First, the correct size wire must be chosen for the terminal size, or vice versa. We\'ll assume that you are using stranded wire so that th wire conforms to the crimped connection. Next, strip the wire. The amount of exposed wire should be equal to the length of the metal barrel on the connector, usually around ¼" or so. If the stripped wire fits up into the metal portion of the barrel with little or no free space, the connector is the right size.

[![Good Length](//cdn.sparkfun.com/r/600-600/assets/9/4/b/0/f/51390134ce395f091b000001.jpg)](//cdn.sparkfun.com/assets/9/4/b/0/f/51390134ce395f091b000001.jpg)

*A good length of wire to barrel ratio*

The wire should then be inserted until the insulation on the wire touches the end of the barrel.

[![Good Crimp Example](//cdn.sparkfun.com/r/600-600/assets/2/0/1/0/5/5138de3cce395f5a18000001.jpg)](//cdn.sparkfun.com/assets/2/0/1/0/5/5138de3cce395f5a18000001.jpg)

*Good: The wire is sticking past the barrel just a little*

The wire and terminal are then inserted into the crimper. The color of the terminal's insulation needs to be matched with the same color on the crimping tool. So if the terminal's insulation is red, use the spot marked by the red dot on the crimpers. Alternatively, if the crimper does not have color markings, use the gauge markings on the side.

The terminal should be sitting horizontal with the barrel side up. The tool is then held perpendicular to the terminal and placed over the barrel, nearest to the ring (or other connection type). To finish the crimp, the tool is squeezed with a considerable force. In general, it is almost impossible to 'over crimp' a connection.

[![crimped](//cdn.sparkfun.com/r/600-600/assets/3/c/7/2/5/5138de3cce395f141b000000.jpg)](//cdn.sparkfun.com/assets/3/c/7/2/5/5138de3cce395f141b000000.jpg)

**Heads up!** Check out the post from Hacakday for more information on crimping, a cross section of a crimped wire, and a video!\
\

[Hackaday \| Good in a Pinch: The Physics of Crimped Connections](https://hackaday.com/2017/02/09/good-in-a-pinch-the-physics-of-crimped-connections/)

\
For a detailed examples of good and bad crimped pin, check out the following from JST!\
\

[![Detiailed Chart of Correct/Incorrect Crimped Pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/4/1/JST_CrimpChart__English_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/JST_CrimpChart__English_.pdf)\
\
*Click on image for closer view.*

After the crimp is completed, the wire and connector should still hold together after trying to pull them apart with great force. If the connection can be pulled apart, the crimp was not done correctly. It is better to have the crimp fail now, versus after it has been installed in its application. Below is a military spec chart for crimped connections.

[![Mil Spec Chart](//cdn.sparkfun.com/r/600-600/assets/0/3/6/6/6/5138de3cce395fbe1a000000.png)](//cdn.sparkfun.com/assets/0/3/6/6/6/5138de3cce395fbe1a000000.png)

**Tip:** If the wire does not fit in the barrel, or is excessively loose, the wrong size and type of either wire or connector was chosen. If necessary, you could add a solder joint between the wire and connector. However, wires that are crimped properly will create a gas tight, cold joint and should not need solder.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Soldering_Wire_to_Quick_Disconnect.jpg "solder wire to crimp connector")](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Soldering_Wire_to_Quick_Disconnect.jpg)

\
Keep in mind, that adding solder will add stress to the joint due to mechanical vibrations and thermal cycling causing joint failure. Soldering can also increase resistance at the joint. For low power applications, users should not notice a significant difference.

**Tip:** Depending on the application, two wires can be crimped with together in a single crimp connector. You\'ll need to ensure that the combined wire diameter is able to fit in the crimp connection and the crimp connector is able to handle the amperage of the project.\
\
The image below demonstrates two wires crimped with female spade headers for the middle connections. In this case, the crimped wires were used to connect multiple devices to ground.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimping_Multiple_Wires_Crimp_Terminal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimping_Multiple_Wires_Crimp_Terminal.jpg)

### [][Crimping a Crimp Pin](#crimp-pin)

Remember, there are hundreds of types of electrical connectors out in the world. Depending on the design, the connector can be designed in a way to fit into a plastic housing. Instead of a barrel crimping down on a wire, the connector may include two crimp tabs (i.e. wings) to crimp over wire and its insulation. The additional crimp tabs for insulation provide strain relief. The crimp pin may also have a locking tab and terminal stop when the pin is inserted in a plastic housing.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Crimp Pin Cut from Reel for a Polarized Connector](https://cdn.sparkfun.com//assets/parts/6/6/6/08100-03a.jpg)](https://www.sparkfun.com/products/8100)   [![Plastic Housing for Polarized Connector](https://cdn.sparkfun.com//assets/parts/6/6/1/08095-Polarized_Connectors_-_Housing__2-Pin_-01.jpg)](https://www.sparkfun.com/products/8095)
  *Crimp Pin Cut from Reel for Polarized Connector*                                                                                                            *Plastic Housing for Polarized Connector*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

One example can be found in the pre-terminated, premium jumper wires. They are used for connecting to PCBs designed with 0.1\" PTH pads. Below is an image of a few crimped pins before being inserted in their plastic housing. On the left is a crimp pin to fit inside a polarized housing. On the center is a female pin used to mate with the male pin on the right.

[![Different Crimp Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Different-Crimped_-Pin-Heads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Different-Crimped_-Pin-Heads.jpg)

The process is a bit more tedious since you are working with smaller pins. Depending on your level of experience, this can be time consuming. However, users can create custom wire lengths and cables for a project.

First, cut and strip a piece of wire. Make sure to match the wire gauge with the crimp pin\'s specifications. In this case, we will use 22 AWG stranded hook-up wire to connect to the [JST RCY connector](https://www.sparkfun.com/products/10501) as recommended by the crimp pin\'s datasheet. After removing the crimp pin from it\'s metal strip, align the wire strands to the conducting tab and the insulator to the insulator tab to check if the wire meets the crimp pin\'s specifications.

[![Properly Cut and Stripped Stranded Wire for a Crimp Pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimp-Pin-Stranded-Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimp-Pin-Stranded-Wire.jpg)

If the wire and stripped sufficiently, insert the crimp pin into one of the crimp tool\'s jaw. You may need to bend the insulator\'s tabs inward to fit. We\'ll use the bigger jaw.

[![Crimp Pin Inserted in Crimp Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Insert-Crimp-Pin-Die.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Insert-Crimp-Pin-Die.jpg)

Make sure to take note grooves of the crimp tool when inserting the crimp pin into the die. If you observe closely, there are two semicylindrical grooves cut on one side of the jaw while the other has one groove. The side that has two grooves will be used to crimp the tabs. Additionally, half of the die is recessed for the insulator tab.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Side View of the Ratcheted Crimp Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Ratcheted-Crimper-Closed-Tool-Die.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Ratcheted-Crimper-Closed-Tool-Die.jpg)   [![Close-Up of the Crimp Tool With Two Grooves and Die Recessed for Insulator Tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Ratcheted-Crimper-Tool-Die-Close-Up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Ratcheted-Crimper-Tool-Die-Close-Up.jpg)
  *Side View of the Ratcheted Crimp Tool*                                                                                                                                                                                                      *Close-Up of Crimp Tool with Two Grooves and Die Recessed for Insulator Tab*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Warning!** If you insert a crimp pin incorrectly, the ratcheted crimp tool will not sufficiently crimp the tabs. As a result, the wire may not fully conduct with the pin and the pin will be damaged. The crimp tool can also get stuck in one position. If the crimp tool is stuck, you will need to flip the safety release pin just above the handle.\
\

[![Crimping a Pin the Wrong Way](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimping-Pins-the-Wrong-Way.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimping-Pins-the-Wrong-Way.jpg)

Slowly close the ratcheted crimp tool to hold the crimp pin in place and insert the stripped wire. You may need to adjust the crimp pin so that its insulator tab is flush with the die.

[![Wire Inserted in Crimp Pin and Crimp Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimp-Tool-Partially-Closed-Crimp-Pin-Stripped-Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimp-Tool-Partially-Closed-Crimp-Pin-Stripped-Wire.jpg)

When ready, slowly squeeze the handles more to continue crimping the tabs. If something is not right and you are using a ratcheted crimp tool, flip the safety release pin just above the handle. Continue squeezing the handle until the ratchet releases automatically to finish the crimp.

[![Crimp Pin and Wire Crimped Together in Crimp Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimping-Pin-Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimping-Pin-Wire.jpg)

Carefully, remove the crimped pin out of the crimp tool. Observe the crimped tabs. You should see something similar to crimped pins below. If necessary, you may need to re-insert the pin back into the jaws to sufficiently crimp the the tabs. The crimp pin on the far left was partially crimped and needed to be placed in the smaller jaw for a proper crimp.

[![Different Crimp Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Different-Crimped_-Pin-Heads.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Different-Crimped_-Pin-Heads.jpg)

When ready, insert the crimped pin into its respective housing. In this case, the crimped female pin was inserted into its respective JST RCY connector housing. Make sure to match the locking tab with hole in the plastic housing.

[![Crimp Pin Inserted into Respective Housing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimped-Pin-Inserted-Into-Plastic-Housing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimped-Pin-Inserted-Into-Plastic-Housing.jpg)

When finished, the wire should snap into its respective housing. Below are a few crimped pins in their respective housing. On the far left, we have crimped pins used for the polarized 1x2 \"Molex\" connector. The two on the right with black housing is an example of crimped pins used with the [standard 0.1\" headers](https://learn.sparkfun.com/tutorials/connector-basics#pin-header-connectors). Finally, the crimped pins in the red housing are used for the JST RCY connector.

[![Assortment of Different Crimp Pins in their Respective Housing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Crimped-Pins-Different-Plastic-Housing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Crimped-Pins-Different-Plastic-Housing.jpg)

### Common Mishaps

Below are a list of common mistakes when crimping quick disconnects and crimp pins. We\'ll use a quick disconnect for demonstration.

Wrong size connector for the wire or wrong size wire for the connector.

[![bad crimp 1](//cdn.sparkfun.com/r/400-400/assets/0/6/1/e/1/5138de3cce395fdf1a000000.jpg)](//cdn.sparkfun.com/assets/0/6/1/e/1/5138de3cce395fdf1a000000.jpg)

*Bad crimp. Connector was too small for the gauge of wire chosen.*

Be cautious not to strip too much insulation off.

[![bad crimp 2](//cdn.sparkfun.com/r/400-400/assets/9/4/c/1/7/5138de3bce395f161a000001.jpg)](//cdn.sparkfun.com/assets/9/4/c/1/7/5138de3bce395f161a000001.jpg)

*Too much insulation has been stripped off, too much bare wire exposed*

It is also worth mentioning that, while not necessarily harmful, The wire should not be protruding too far past the barrel. If this happens, trimming the wire is recommended.

[![bad crimp 3](//cdn.sparkfun.com/r/400-400/assets/2/6/b/d/7/5138de3cce395f401a000001.jpg)](//cdn.sparkfun.com/assets/2/6/b/d/7/5138de3cce395f401a000001.jpg)

*The excess bare wire should be trimmed off*

## How to Use a Wire Wrap Tool

[] **Caution!** Remember, wire wrap uses a small gauge. While this is perfect for projects that do not have a lot of room to work with, it is not able to handle a lot of power due to the thickness of the wire.

Strip the 30 AWG wire by inserting it between the wire wrap tool\'s blades. Pull the wire to remove the insulation.

[![Strip 30AGW Wire with Wire Wrap Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Wire_Wrap_Tool_Strip_30AWG.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Wire_Wrap_Tool_Strip_30AWG.jpg)

Make sure to strip away enough wire to wrap around a terminal for a sufficient connection. About a 1\" should be enough.

[![Remove about 1 Inch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Wire_Wrap_Tool_1_Inch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Wire_Wrap_Tool_1_Inch.jpg)

Insert the exposed wire into the hole along the side. Make sure to insert the wire on the side with the notch and place the wire in the cut along the side of the cylinder.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Insert Wires into Hole Along Side of Cylinder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Insert_Wire_Into_Wire_Wrap_Tool.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Insert_Wire_Into_Wire_Wrap_Tool.jpg)   [![Place Exposed Wire in Groove Along Cylinder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Lay_Wire_Along_Groove_Wire_Wrap_Tool.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Lay_Wire_Along_Groove_Wire_Wrap_Tool.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Insert the wire into header pin (a.k.a. post). In this case, [male header pins](https://www.sparkfun.com/products/12693) were used on a mini-breadboard.

[![Insert Header Pin in Center of Wire Wrap Tool ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Insert_Wire_Wrap_Tool_Header_Post.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Insert_Wire_Wrap_Tool_Header_Post.jpg)

**Note:** Stackable female header pins can twist with the wire wrap tool and wire. It is recommended that you wrap wire around [male header pins](https://www.sparkfun.com/products/116).

Rotate the tool clockwise to begin wrapping the wire around the square header pin. Hold the wire and header pins down with your other hand. Continue rotating the tool so that all of the stripped wire wraps around the pin.

[![Rotate Tool Counter Clockwise](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Twist_Wire_Wrap_Tool.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Twist_Wire_Wrap_Tool.jpg)

Remove the tool from the pin. When completed, the wire\'s insulation should start at the bottom of the pin. For a more permanent and secure connection, [add some solder between the wire and pin](https://www.instagram.com/p/60Hx9DDa0r/).

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Remove Wire Wrap Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Remove_Wire_Wrap_Tool.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Remove_Wire_Wrap_Tool.jpg)   [![Header Wrapped With Wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/30_AWG_Wrapped_Around_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/30_AWG_Wrapped_Around_Header.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you require more connections on the same pin, wrap more wires around the top of the first connection and repeat the steps outlined above. The amount you can stack depends on the length of the header pin. Try using the wire wrap tool to wrap wires around headers on a microcontroller, LED, or resistor for prototyping.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Wrapping More Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Stacking_Wire_Wraps.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Stacking_Wire_Wraps.jpg)   [![SparkFun Pro Micro with Wire Wrap, LED, and Resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Wire_Wrap_Arduino_LED_Terminals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Wire_Wrap_Arduino_LED_Terminals.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Removing Wrapped Wires

If you need to disconnect the wire from the pin, simply use the other end of the tool and rotate it in a counterclockwise direction.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Removing Wire Wrap with Other End](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Removing_Installed_Wire_Wrap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Removing_Installed_Wire_Wrap.jpg)   [![Rotate in Counterclockwise direction](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Twist_Wire_Wrap_Tool_Remove.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Twist_Wire_Wrap_Tool_Remove.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the wire wrap is loosened, pull the wire away from the pin.

[![Removed Wire wrap from Header](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/Wire_Wrap_Removed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/Wire_Wrap_Removed.jpg)

**Note:** For more information about wire wrapping, types of wrapping, and tips, check out the article from [Nuts and Volts: Wire Wrap is Alive and Well!](http://www.nutsvolts.com/magazine/article/wire_wrap_is_alive_and_well)

## Wire Management

### Twisting Wires into a Braid

It is a good idea to braid long wires that are used in a project. There are a few benefits of twisting the wires together:

- keeps the project organized
- prevents wires from being pulled from moving parts
- strengthens the connection

**Note:** The following was inspired by [McCall's tutorial](http://diyaudioprojects.com/Power/Low-Inductance-DIY-Speaker-Cables/) when completing projects.

Below is an example of braiding four hook-up wires together for a non-addressable LED. To braid your wires, twist a pair of wires in a counterclockwise pattern between your index finger and thumb using both hands. In this case, the green and red wires were twisted first.

[![Wire Management Braiding Counterclockwise 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg)

Twist the other pair of wires in a counterclockwise pattern.

[![Wire Management Braiding Counterclockwise 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg)

Twist the pairs of wires in a clockwise pattern.

[![Wire Management Braiding Clockwise](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg)

Once finished, the wires in your project will be manageable and easier to handle. Below are a few examples with braided wires used in projects.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Circuit secured to bottom of cardboard box with electrical tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/3D_Printed_Diamond_Prop_Circuit_in_Enclosure.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/3D_Printed_Diamond_Prop_Circuit_in_Enclosure.jpg)   [![Inside of Bluetooth Box with Twisted Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/1/Wireless_Bluetooth_Speaker_Project-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/1/Wireless_Bluetooth_Speaker_Project-11.jpg)
  *Some Twisted Wires Used in the [Interactive 3D Printed LED Diamond Prop Tutorial](https://learn.sparkfun.com/tutorials/interactive-3d-printed-led-diamond-prop)*                                                                                                                                *Twisted Wires Used in the [Wireless Audio Bluetooth Adapter w/ BC127 Tutorial](https://learn.sparkfun.com/tutorials/wireless-audio-bluetooth-adapter-w-bc127)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Tip:** Try using a [power drill to twist long wires together.](%20https://www.instagram.com/p/7GJ2kuja8D/)

### Sleeves and Cable Carriers

Sleeves and [cable carriers](https://www.sparkfun.com/products/13207) are also useful in further protecting the connection from moveable parts. The image below shows loose wires on the Shapeoko.

[![Unprotected Wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/5/6/Shapeoko_Tutorial-35.jpg)

Below are images of wires within a sleeve and cable carrier for protection.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Cable Sleeve](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-15_heatsinkchassis.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Stepoko_Tutorial-15_heatsinkchassis.jpg)   [![Cable Carrier](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/0/6/Shapeoko_Update-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/6/Shapeoko_Update-09.jpg)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Labeling Complex Wiring

Sometimes it is useful to label wires using sticky notes, tape, or markers to help keep track of connections using the same color of wire, complex wiring, and to troubleshoot projects.

[![Wires Inserted into Poke-Home Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/5/Exp3_Joystick6_duplicate.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/5/Exp3_Joystick6_duplicate.jpg)

*Labeled wires from the [micro:arcade kit](https://learn.sparkfun.com/tutorials/microarcade-kit-experiment-guide/experiment-3-fun-with-the-joystick)*

**Tips:** Check out the links below for more ideas.\
\

- *Printable Shrink Tube* - Try using [printable heat shrink](https://www.instagram.com/p/BZ16ObuBiWL/?utm_source=ig_web_copy_link) to label wires.
- *Markers* - Another option is [labeling wire ends with a marker](https://www.instagram.com/p/78JSoLDazZ/?taken-by=sparkfun).