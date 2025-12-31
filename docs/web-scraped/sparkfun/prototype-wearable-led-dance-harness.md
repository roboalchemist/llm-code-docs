# Source: https://learn.sparkfun.com/tutorials/prototype-wearable-led-dance-harness

## Introduction

Have you ever wanted to merge technology with your dance? In this tutorial, you will learn how to design and build a wearable LED harness for dance performances. The design is not just limited to dance. You can also use it as a guide for costumes.

[![Dress Rehearsal with LED Straps](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/Minions_LED_Costume.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/Minions_LED_Costume.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** Make sure to use an appropriate [gauge wire](https://learn.sparkfun.com/tutorials/working-with-wire#wire-thickness) when wiring the pieces of LED strip and adapter together. After stress testing with a 9V Alkaline battery and checking with a multimeter, the wires used in the wishlist were sufficient. Make sure to test the circuit if you decide to use a different battery chemistry or thinner wires.

- Electrical Tape
- [12 Gauge Clear Vinyl](http://www.joann.com/12-gauge-vinyl-54in-clear/1151489.html)
- ⅞\" Yellow Ribbon
- 1 ½\" Yellow Ribbon
- Adhesive Velcro
- Thread
- Twine or Any Toothy String
- Translucent Yellow Button Up Shirt
- Bow Tie (*Optional*)
- Folded Handkerchief (*Optional*)

### Tools

You will need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), and tools to work with wire.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Diagonal Cutters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Weller WE1010 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/6/1/14734-Weller_WE1010_Soldering_Station_-01.jpg)](https://www.sparkfun.com/products/14734)

### [Weller WE1010 Soldering Station](https://www.sparkfun.com/products/14734) 

[ TOL-14734 ]

The WE1010 from Weller is a powerful 70 watt soldering station that is perfect for passionate hobbyists, DIYers, and anyone w...

**Retired**

You will also need:

- Scissors
- Cutting Board
- Rotary Cutter
- Lighter
- Needle
- Sewing Machine
- Measuring Tape
- Yard Stick

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

## Design

Designing wearable electronics around a dancer is difficult depending on the movement. As a [bboy](https://en.wikipedia.org/wiki/Breakdancing), just about every part of the body is used on the floor.

[![Bboy Holding a Chair Freeze](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/BboyBobbyFreeze.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/BboyBobbyFreeze.jpg)

So when planning for a show using wearable electronics, it needs to be:

- Flexible
- Durable
- Secure
- Quick to Connect
- Safe
- Light Up Throughout the Performance

On top of that, I needed to make enough for each student in my troupe. I decided make a harness to hold the electronics based on a backpack\'s shoulder straps. A button up shirt was used to diffuse the light. A bowtie and pocket square were added for detail.

For the scope of the tutorial, I\'ll be focusing on the harness to hold the LEDs and the electronics.

### Electroluminescence (EL) vs Light Emitting Diode (LED)?

I debated with using either [EL wire](https://www.sparkfun.com/categories/226) or [LEDs](https://www.sparkfun.com/categories/175). Each have different uses depending on the performance and lighting of the environment.

With the first wearable design for dance, I found that EL was harder to see with ambient lighting even with EL tape and panel. I was also limited to one color at a time. However, it required less power and it did have a different affect. For the second design, the LEDs were easier to see with the ambient light and I was able to select more than one color. The LEDs did require a little bit more power.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/ELDanceShirt.jpg "Wearable EL Dance Shirt")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/ELDanceShirt.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/LEDDanceHarness.jpg "Wearable LED Dance Harness")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/LEDDanceHarness.jpg)
  *Mark I: EL Dance Shirt*                                                                                                                                                                    *Mark II: LED Dance Harness*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Understanding Your Circuit

The circuit for the wearable LED harness is simple. Let\'s take a look at the left side of the harness that holds the battery, adapters, and LEDs.

### Initial Circuit

Power is connected to the \"*+12V*\" pad of the non-addressable LED strip. To complete the circuit and power the LEDs, ground is connected to each color\'s pad labeled \"*G*,\" \"*R*\", or \"*B*.\" Green and blue were chosen to make cyan from the primary colors. For one side of the harness, LED segment A consisted of a long strip of 33x LEDs. LED segment B and C consisted of 3x LEDs each.

[![Fritzing Diagram Wearable LED Harness Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDHarnessCircuit_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDHarnessCircuit_1.png)

*Having a hard time seeing the circuit? Click the image for a closer look.*

**Note:** When testing the non-addressable LED strip, the pin labeled \"G\" was actually blue and the \"B\" was actually green. Depending on the manufacturer, the label may vary. Try testing the LED strip out with a power supply to determine see if the letter represents the color.

A **9V** battery and custom made adapters were used for each harness. Keep in mind that a 9V battery is not able to power all three colors simultaneously. However, using two colors was sufficient enough for the project and performance.

**Warning!** You may need a transistor and microcontroller to control the power delivered to the LEDs depending on the type of battery that you are using. Remember to check with a multimeter and test it out thoroughly.

### Complete Circuit

The connection was then wired in [parallel](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits#parallel-circuits) on the other side of the harness by connecting to the same rails on the solderable breadboard.

[![Fritzing Diagram Wearable LED Harness Fill Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDHarnessCircuit_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDHarnessCircuit_2.png)

*Having a hard time seeing the circuit? Click the image for a closer look.*

## Stitching It Together

**Heads up!** The length of this harness was based on the average size of my students ranging from about 8-12 years old. You may need to measure and adjust the length depending on how tall the user is from the shoulder down to the stomach. Once the length of the shoulder and waist is measured, double the length and test it out before making multiple units.

From the image shown below, prepare the fabric based on the user\'s height by cutting the ribbons and transparent vinyl. Carefully heat the ribbon ends with lighter to prevent the ends from unraveling. Listed below are the average lengths used for a kid.

- 2x Transparent Vinyl - 25\"
- 4x Transparent Vinyl - 3\"
- 2x 0.5\" Ribbon A (for the top) - 25\"
- 2x 1.0\" Ribbon B (for the back) - 9\"
- 4x 0.5\" Ribbon C (for the front ribbon ties) - 15\"
- 4x 0.5\" Ribbon D (for the bottom) - 5\"

[![Prepare the Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_1.jpg)

Pin down the bottom of the harness and sew the ends together in a square pattern with a needle and thread.

[![Sew Bottom of the Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_2.jpg)

Pin and sew the bottom of the harness with the longer piece of ribbon. Make sure to sew the end in a triangular or square pattern to secure the ribbon.

[![Sew Top of Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_3.jpg)

Make sure that the ribbon is flat and facing the same direction when sewing the top and bottom together. They should be free from any twists.

[![Left and Right Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_4.jpg)

Starting with the right side of the harness, pin and sew the ribbon ties for the sternum and waist. The ribbon tie for the chest was about 10 inches above the waist. The ribbon tie for the waist was added to the bottom of the long strip. Repeat for the left side. Choosing one side of the harness, attatch the back ribbons using the same 10 inch spacing as the ribbon ties.

[![Sew the Ribbon Ties and the Back](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_5.jpg)

At this time, sew the opposite side to the harness. Using pins and a sewing machine, sew clear vinyl to the inside of the ribbon to the top and bottom each side. The vinyl should wrap around the LEDs and end behind the LEDs.

[![Attach Both Sides to the Harness and Sew the Vinyl Together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_6.jpg)

The completed harness should look like the image below.

[![Completed Wearable LED Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomLEDHarness_7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomLEDHarness_7.jpg)

## Hardware Hookup

### Connecting LED Strip Segments

Cut the LED strip at the center of the exposed pads using a [diagonal cutter](https://www.sparkfun.com/products/8794). The dot and dashed line in the image below is where you will need to perform the cut. Make sure to remove part of the silicone tube in order to be able to access the LED Strip\'s pads.

[![Cut between the LED Strip\'s Pads](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/12023_1cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/12023_1cut.jpg)

Cut half of the 12\" premium jumper wires and strip the insulation. Then solder the wires to each of the LED strip\'s pads.

[![Solder Wires to LED Strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/SolderLEDStrip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/SolderLEDStrip.jpg)

The connection to the pads needed to be secure so I decided to braid the wires together to manage the connections. I was inspired by [McCall's tutorial](http://diyaudioprojects.com/Power/Low-Inductance-DIY-Speaker-Cables/) when completing projects. To braid your wires, twist a pair of wires in a counterclockwise pattern between your index finger and thumb using both hands. I decided to start with the green and red wires.

[![Wire Management Braiding Counterclockwise 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg)

Twist the other pair of wires in a counterclockwise pattern.

[![Wire Management Braiding Counterclockwise 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg)

Twist the pairs of wires in a clockwise pattern.

[![Wire Management Braiding Clockwise](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg)

Repeat for segment B and C. The segments will be using shorter wire.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg "Wire Management Braiding Counterclockwise 1")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_1.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg "Wire Management Braiding Counterclockwise 2")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingCounterclockwise_2.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg "Wire Management Braiding Clockwise")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementBraidingClockwise.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Clean Solder Joints

If you were using water soluble flux, clean the solder joints with de-ionized water and a toothbrush. Dry the LED strips thoroughly using compressed air. Luckily, SparkFun has a [PCB cleaning room](https://learn.sparkfun.com/tutorials/electronics-assembly/washing). As an alternative, you could use [water from the sink and towels](https://www.sparkfun.com/news/1161).

[![Clean Solder Joints](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CleanSolderJoints.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CleanSolderJoints.jpg)

### Test LED Strips

Once dry, test the LED strips to make the colors matched and the wires are connected to its respective pads. I decided to use a benchtop power supply set to output about 9V to verify the connection.

[![Testing LED Strips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/LEDStripTests.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/LEDStripTests.jpg)

### Secure w/ Hot Glue

Add hot glue to the terminals to secure the wires further.

[![Hot Glue Terminals](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireManagementHotGlueTerminals.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireManagementHotGlueTerminals.jpg)

**Tip:** To smooth out the glue on the wires and LED strip, try using a little hot air from a [heat gun](https://www.sparkfun.com/products/10326) or [hot air rework station](https://www.sparkfun.com/products/14557).

### Custom Power Adapter w/ Solderable Breadboard

Using a dremel and [Panavise](https://www.sparkfun.com/products/10410), carefully cut the solderable breadboard in half.

[![Cut Solderable Breadboard in Half](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/12702-03_Cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/12702-03_Cut.jpg)

**Note:** Cutting the board in half was not necessary but I was able to reuse the unpopulated area on the mini-solderable breadboard. Try using the [snappable protoboard](https://www.sparkfun.com/products/13268) as an alternative to reduce the amount of tools required in the project. Just make sure to to add wire and solder bridges to make the connections for each rail.

Solder the female barrel jack connector to the board so that the connector is flush with the edge.

[![Solder the Female Barrel Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomePowerAdapterBarrelJackSmall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomePowerAdapterBarrelJackSmall.png)

Cut the 1x4 pin jumper wire in half and strip each wire using 0.1\" spacing. Solder the wires as illustrated earlier in the Fritzing diagram.

[![Solder each 1x4 jumper wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomePowerAdapter1x4PinWireSmall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomePowerAdapter1x4PinWireSmall.png)

Solder the GND pins together for two of the colors with a solder bridge. Then connect it back to the barrel jack connector an extra wire to the sheath.

[![Connect GND](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomePowerAdapterGNDSmall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomePowerAdapterGNDSmall.png)

Solder the center pin to the \"+12V\" pin.

[![Connect Center Positive to +12V](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomePowerAdapter_VSmall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomePowerAdapter_VSmall.png)

Clean, dry, and test the board with a multimeter, power supply, and the LED strips. Feel free to label the connections with a marker or paint.

[![Complated Custom Power Adapter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomePowerAdapterSmall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomePowerAdapterSmall.png)

Finally, secure the wires and insulate the connection using hot glue just like the LED strip.

## Secure Wires

Secure all the jumper wires with electrical tape.

[![Electrical Tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/TapePinHousingWearableLEDHarness.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/TapePinHousingWearableLEDHarness.jpg)

Place the LED strip between the ribbon and vinyl. Make sure to have the LEDs facing out of the clear vinyl. Attach adhesive velcro as highlighted in the image below to hold LED strip down.

[![Velcro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/VelcroWearableLEDHarness.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/VelcroWearableLEDHarness.jpg)

Add extra M/F premium jumper wires to extend the LED strip on one side to the breadboard power adapter on the other side. To be consistent I chose to attach the battery and custom adapter on the dancer\'s left side.

[![Wire Extensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WireExtensionsWearableLEDHarness.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WireExtensionsWearableLEDHarness.jpg)

Tie the wires extended on the back and the custom power adapter with string.

[![Tie down](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/StringTiesWearableLEDHarness.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/StringTiesWearableLEDHarness.jpg)

The user can then slide the harness on like a backpack, tie the ribbons across the chest and waist, and plug in the battery to test.

[![Wearable LED Harness](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDHarness_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDHarness_2.jpg)

## Repeat

Once the first wearable LED dance harness was finished, I repeated the steps until there was enough for each dancer in the troupe. I built a total of 7x units for my students. This required a lot of time and patience.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/StrippedWires.jpg "Stripped Wires")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/StrippedWires.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/LEDStripsCut.jpg "Cut LED Strips")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/LEDStripsCut.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/BraidedWires.jpg "LED Strips Soldered and Wires Braided")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/BraidedWires.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CustomWearableLEDPowerAdapters.jpg "Custom Wearable LED Power Adapters")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CustomWearableLEDPowerAdapters.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/HotGlueJointsandTestLEDStrips.jpg "Hot Glued Solder Joints and Tested LED Strips")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/HotGlueJointsandTestLEDStrips.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Over the course of about 2-3 months and balancing my usual work schedule, I was able to finish the project!

[![Completed Wearable LED Harnesses Illuminating Shirts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/CompletedWearableLEDHarnessesIlluminatingShirts_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/CompletedWearableLEDHarnessesIlluminatingShirts_1.jpg)

## Stress Testing In the Field

### Benchtop Tests

Before the rehearsals and performances, I tested the harnesses out under the fabric using a benchtop power supply for about 60 minutes. I then tested it in a studio with the choreography using 9V batteries.

[![LED Dance Costume Harness Testing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/LEDDanceCostumeHarness.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/LEDDanceCostumeHarness.jpg)

### Dress Rehearsal

When the time came, my students were excited to test it out for the dress rehearsal. This was a good time to explain how to tie the harness, put on the shirt, and power the LEDs with the barrel jack underneath the button up.

[![Dress Rehearsal](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal.jpg)

The LED harnesses lasted throughout the dress rehearsal even though they were upside down, side ways, or moving across the floor. There did not appear to be any damage to the circuit. After about an hour, the 9V battery still had power for the show!

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal2.JPG "Rehearsal")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal2.JPG)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal3.JPG "Rehearsal")](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/WearableLEDDanceHarnessRehearsal3.JPG)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Show Time!

When it came time for the show, I had my handy multimeter, scissors, electrical tape, and backup 9V batteries just in case I needed to troubleshoot. However, everything seemed fine. Here\'s a picture of them backstage right before going on.

[![Backstage](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/6/4/DanceBboysDance_LEDHarnessBackstage_small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/6/4/DanceBboysDance_LEDHarnessBackstage_small.jpg)

In the end, the performance (which lasted \~1:30-2:00 minutes) ran smoothly without the LED harnesses \"breaking\" on my bboys. Whew, that was a lot of work!

## Making It Better

There\'s always room for improvement. After the project was completed, I realized that the harness could be built better. Below are a list of possible upgrades and improvements that could be implemented for future builds.

- **Vest** - It was exhausting making about 10x-15x units for each student. In the future, I may just consider buying a vest/harness and adding the parts to the material to save on time and energy.

- **Quick Release Buckle vs Ribbon Ties** - A few of the students had some issues tying the ribbon. Instead of using ribbon ties, a quick release buckle could make it easier

- **Snaps vs Velcro** - The velcro held the LEDs and the vinyl securely. As an alternative, a button tool and metal snap could be used.

- **Pocket for 9V Battery** - With the amount of time I had available, I decided to just tape the battery and cable to the harness and the ribbon tie. A pocket to hold the 9V battery would make it easier to switch out.

- **Labels** - Initially, I did not label the wire colors. After a few months, I forgot about the wire connections on the LED strips, jumper wires, and custom power adapter. I decided to try and revise the project by adding sensors to control the LED straps. It was not until I inspected the connection throughout the harness again that I remembered the simple circuit. Labeling the connection with a marker or paint would have saved some time.

- **Connectors** - The 1x4 female header pins were tedious to strip and solder each wire to the breadboard. Using individual jumper wires might have been easier to connect. However, troubleshooting wires might not be the quickest if a wire becomes loose during a performance. I also noticed that a male header pin broke off one of my student\'s harness after about 1 year due to wear and tear. In the future, I would probably consider using pigtail connector or polarized PTH connector with cable extensions. I would use switches or transistors rated to handle the current in order to switch between the LED colors.

  ::::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![LED Strip Pigtail Connector (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/1/14576-LED_Pigtail_connector_4_Pin_-01.jpg)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html)
  :::

  ::: main
  ### [LED Strip Pigtail Connector (4-pin)](https://www.sparkfun.com/led-strip-pigtail-connector-4-pin.html) 

  [ CAB-14576 ]
  These 4-pin JST-SM pigtail connectors mate perfectly with LED strips and other applications that require only two lines and a...
  :::

  :::: 
  ::: prices
  [ [\$1.95] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![JST Jumper 4 Wire Assembly](https://cdn.sparkfun.com/r/140-140/assets/parts/4/0/2/2/09916-02b.jpg)](https://www.sparkfun.com/jst-jumper-4-wire-assembly.html)
  :::

  ::: main
  ### [JST Jumper 4 Wire Assembly](https://www.sparkfun.com/jst-jumper-4-wire-assembly.html) 

  [ PRT-09916 ]
  This is a simple four wire cable. Great for jumping from board to board or just about anything else. There is a 4-pin JST con...
  :::

  :::: 
  ::: prices
  [ [\$1.95] ]
  :::
  ::::
  :::::::
  :::::::::::::

  ::: clearfix
  :::

- **Switch** - Plugging in the battery underneath the button up shirt was a little difficult even with the barrel jack. Adding a latching switch after the battery would improve on the design. Below are a few switches that could be used but an enclosure might be needed for the panel mounts switches.

  :::::::::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![Toggle Switch and Cover - Illuminated (Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/9/0/11310-01b.jpg)](https://www.sparkfun.com/toggle-switch-and-cover-illuminated-red.html)
  :::

  ::: main
  ### [Toggle Switch and Cover - Illuminated (Red)](https://www.sparkfun.com/toggle-switch-and-cover-illuminated-red.html) 

  [ COM-11310 ]
  This simple on-off switch is rated for 20A at 12V but who cares about all that, it looks way awesome. These toggle switches c...
  :::

  :::: 
  ::: prices
  [ [\$4.75] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Barrel Jack Power Switch - M-F (3\")](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/8/6/11705-01.jpg)](https://www.sparkfun.com/barrel-jack-power-switch-m-f-3.html)
  :::

  ::: main
  ### [Barrel Jack Power Switch - M-F (3\")](https://www.sparkfun.com/barrel-jack-power-switch-m-f-3.html) 

  [ COM-11705 ]
  We use barrel jacks a lot around here and sometimes we need to pop a switch into the mix. That usually means hacking up a per...
  :::

  :::: 
  ::: prices
  [ [\$3.50] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Metal Pushbutton with Wires - Latching (16mm, Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/4/5/1/11971-Metal_Pushbutton_-_Latching__16mm__Red_-01.jpg)](https://www.sparkfun.com/metal-pushbutton-latching-16mm-red.html)
  :::

  ::: main
  ### [Metal Pushbutton with Wires - Latching (16mm, Red)](https://www.sparkfun.com/metal-pushbutton-latching-16mm-red.html) 

  [ COM-11971 ]
  This is a perfect choice if you are in need of a heavy duty push button! These metal push buttons are a very tough, small, pa...
  :::

  :::: 
  ::: prices
  [ [\$9.95] ]
  :::
  ::::
  :::::::
  ::::::::::::::::::

  ::: clearfix
  :::

------------------------------------------------------------------------

For *Mark III*, I was able to explore the following option.

- **Sensor** \-- Adding a sensor can make the wearable LED dance harness more interactive. It was not until *Mark III* that I was able to add an acceleroemeter with the wearable LED dance harness. I used the full mini-solderable breadboard, microcontroller, and a MOSFET. For more information, check out the [motion controlled wearable LED dance harness](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness).

  :::::::: tile-wrap
  ::::::: 
  [](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness)

  :::: thumb-wrap
  ::: 
  :::
  ::::

  ### Motion Controlled Wearable LED Dance Harness 

  ::: metaline
  January 30, 2019
  :::

  ::: description
  Control LEDs based on your movement using an accelerometer! Make your LEDs breathe by fading in and out when laying on the floor, turn off the LEDs when moving to your side, or make the LEDs blink in a headstand!
  :::
  :::::::
  ::::::::

  ::: clearfix
  :::