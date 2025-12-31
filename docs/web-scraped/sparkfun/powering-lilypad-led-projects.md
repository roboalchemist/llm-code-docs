# Source: https://learn.sparkfun.com/tutorials/powering-lilypad-led-projects

## Introduction

One of the most commonly asked questions when getting started with e-textiles is \"How many LEDs can I put in my project?\" In this guide, we will cover conductive thread\'s resistance and how that affects powering LEDs, calculations to predict battery and power requirements, and some construction tips.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/5/LilyPadLEDPanel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/5/LilyPadLEDPanel.jpg)

### Suggested Reading

If any of the following topics sound unfamiliar to you, we recommend checking out the corresponding tutorial before continuing.

- [Voltage, Current, Resistance and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [Light-emitting Diodes (LEDs)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [Short Circuits](https://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits)
- [Battery Technologies](https://learn.sparkfun.com/tutorials/battery-technologies)

If this is your first time working with e-textiles, we recommend starting with this tutorial:

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

December 17, 2016

Learn how to use conductive thread with LilyPad components.

## Conductive Thread Resistance

One of the most important things to consider when building a wearable project is the resistance of conductive thread. Unlike copper wire, which has very little resistance, conductive thread\'s resistance will vary depending on the metal used to make the thread and the thickness of the thread. Most conductive threads list resistance in Ohms/Ft. The lower this number is, the better, because less resistance means more electricity can get through to the components used in your project.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/1/WirevsThread.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/1/WirevsThread.jpg)

The basic electrical property [Ohm's Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law#ohms-law) states that running an electrical current through a material high in resistance causes the voltage to drop. The higher the current, the greater the voltage drop. This means that even though a [LiPo battery](https://www.sparkfun.com/products/13112) powering your LilyPad may put out 3.7 volts, by the time it gets through the thread to your components, it may drop to 3.0 volts or less.

Many electrical components, such as LEDs, need a certain voltage to function properly. For example, in a project with LilyPad LEDs if the voltage drops below 3 volts, a blue LED will stop working, followed by the green and finally the red. To get full-color output from RGB LEDs like the [LilyPad RGB LED Board](https://www.sparkfun.com/products/8467), you should always try to run at 3 volts or above.

To figure out an LED\'s voltage needs, you can take a look at the **forward voltage** section of the LED\'s datasheet. Check out [this tutorial](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds?_ga=1.116596098.585794747.1436382744#get-the-details) for more detailed instructions on how to read an LED\'s datasheet.

### Forward voltages of LilyPad LEDs

LilyPad LED

Forward Voltage

Blue

3.2 Volts

Green

3.2 Volts

Pink

2.5 Volts

*Purple (retired)*

*2.8 Volts*

Red

2.0 Volts

White

3.3 Volts

Yellow

2.0 Volts

### Forward voltages of LilyPad RGB LEDs:

LilyPad LED

Red LED Forward Voltage

Green LED Forward Voltage

Blue LED Forward Voltage

LilyPad Tri-Color LED

2.0 Volts

3.5 Volts

3.5 Volts

LilyPad Pixel Board

2.2 Volts

3.4 Volts

3.4 Volts

To minimize voltage drop, we\'ll need to decrease the resistance of the power connections. There are a few ways to do this:

- **Keep the length of the power connections as short as possible**. Because the resistance increases with length, if you reduce the length, you'll reduce the resistance.

- **Reduce the resistance of the thread itself**. Thicker thread has a lower resistance than thinner thread, and using multiple strands at a time reduces the resistance even further.

**TIP:**\
Use a non conductive thread to stitch bundled thread (either placed together or braided) to your base fabric. Leave enough open spaces in the stitching so you are able to stitch conductive thread to the larger thread bundle when connecting components. This video from e-textile expert Lynne Bruning shows this technique at around the 4:10 mark:\
\

### Conductive Thread Alternatives:

For large projects that require thread to travel long distances, projects with a lot of power-hungry pieces such as a large amount of LilyPad Pixel Boards, or in spots where thread may break under stress, here are some alternatives that work well for wearables:

#### Conductive Ribbon

[![Conductive Ribbon - 3-Conductor (1 yard)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/4/7/7/10172-01.jpg)](https://www.sparkfun.com/products/10172)

### [Conductive Ribbon - 3-Conductor (1 yard)](https://www.sparkfun.com/products/10172) 

[ DEV-10172 ]

Here we have some conductive ribbon. Essentially, it\'s a fabric with 3 conductors woven into the ribbon. It measures roughly ...

**Retired**

Specialty nylon ribbon with flexible stranded wire woven into it is a great alternative to conductive thread with low resistance. You will need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) to the tinsel within the ribbon in order to use in a project.

**Tip:** For an example of how to solder the conductive ribbon conductor to plated through holes, check out some of these [archived images from fabrick.it](https://web.archive.org/web/20120715002818/http://www.fabrick.it/tutorials/soldering_the_ribbon).

#### Conductive Fabric Traces

[![Conductive Fabric - 12\"x13\" Ripstop](https://cdn.sparkfun.com/r/140-140/assets/parts/4/2/6/1/10056-03b.jpg)](https://www.sparkfun.com/products/10056)

### [Conductive Fabric - 12\"x13\" Ripstop](https://www.sparkfun.com/products/10056) 

[ DEV-10056 ]

This is a conductive knit fabric for use in e-textiles. It is similar in feel to a nylon ripstop material. It is highly condu...

**Retired**

[![Conductive Fabric - 12\"x13\" MedTex130](https://cdn.sparkfun.com/r/140-140/assets/parts/4/2/8/2/09769-01.jpg)](https://www.sparkfun.com/products/10070)

### [Conductive Fabric - 12\"x13\" MedTex130](https://www.sparkfun.com/products/10070) 

[ DEV-10070 ]

This is a conductive knit fabric for use in e-textiles. It is silver-plated nylon that is stretchy in both directions. It is ...

**Retired**

You can create your own low resistance traces using thin strips of conductive fabric. We recommend using iron-on adhesive to attach to fabric or ribbon, then using conductive thread to hand stitch components to the traces.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/5/Pixel_Ribbon.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/5/Pixel_Ribbon.png)

Don\'t forget to [insulate](https://learn.sparkfun.com/tutorials/insulation-techniques-for-e-textiles) the fabric traces as you would conductive thread.

#### Stranded Wire

[![Ribbon Cable - 6 wire (15ft)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/4/2/1/10646-02.jpg)](https://www.sparkfun.com/ribbon-cable-6-wire-15ft.html)

### [Ribbon Cable - 6 wire (15ft)](https://www.sparkfun.com/ribbon-cable-6-wire-15ft.html) 

[ CAB-10646 ]

Ribbon cable is really helpful in situations where you need to make a lot of connections without a big mess of wires. Nothing...

[ [\$4.50] ]

Another alternative is to switch from conductive thread to traditional wire. Wire has a much lower resistance than thread, allowing you to use more LEDs than a conductive thread circuit. You'll have to switch from sewing to soldering, but it's easy to solder wires to the same sew tabs to which you would normally connect thread.

Wire is prone to breaking if it is flexed repeatedly. For wearable projects that require maximum flexibility, use stranded wire (not solid), and look for special silicone-jacketed wire that is extremely flexible. For projects that will be washed, water may wick into exposed stranded wire, becoming trapped and potentially corroding it over time. Apply a small dab of silicone sealant to the cut ends of the wire to prevent this from happening.

[] When soldering, be careful not to melt or burn nearby fabric. Elevate or insulate the back of the LilyPad board from any backing fabric before applying heat.

If you have never soldered before or worked with wire, we recommend visiting the following tutorials.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

## How Long Will My Project Run on Battery Power?

To figure out how long your project will run on battery power, you need to know two things: how much **current** your project uses and the capacity of your battery.

You can measure exactly how much current your project uses by measuring it with a [multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#measuring-current), but we can also make a pretty accurate guess by looking at the LED datasheets and doing some math.

A typical **LilyPad LED** uses 20mA of current at full brightness. Multiply that by the number of LEDs you're using, add 10mA for the LilyPad that's running everything, and you'll have an estimate of your average current draw.

**Example:**\
A project with 10 LilyPad LEDs controlled by a LilyPad Arduino\
\

*20mA \* 10 + 10mA = 210mA*

A single **LilyPad Pixel Board** will use 40mA when it's set to white (all three internal LEDs fully on). For a worst-case estimate, you could multiply that by the number of pixels in your project.

However, you'll probably be displaying different colors on your LilyPad Pixel Boards and turning them off entirely at times. The resistance in the threads will also drop the voltage, meaning the LilyPixels will run slightly dimmer and use less current. Usually, it's safe to halve the above estimate, which gives us 20mA.

*For more detailed information on working with LilyPad Pixel Boards, take a look at our [LilyPad Pixel Board Hookup Guide](https://learn.sparkfun.com/tutorials/lilypad-pixel-board-hookup-guide).*

### Battery Capacity

Now, let's look at the battery. Battery capacity is given in **milliamp-hours** (mAh). This number tells you how many milli-amps (mA) a full battery can provide for one hour before it's empty. The [e-Textiles Battery](https://www.sparkfun.com/products/13112) that comes with most LilyPad Arduino kits has a 110mAh capacity. For many projects, especially ones with a large number of LEDs, you will probably want to use a higher capacity battery for a longer run time.

To find out how long a battery will last, use this formula:\
**Hours = Battery mAh / Project mA**\
\
Let\'s use the calculation above to see how long a 110mAh battery will power the project we used in the last example:\
\

*0.52 hrs = 110mAh / 210mA*

Thus, an e-Textile battery will only power the project for approximately half an hour. Here\'s an instance where a larger capacity battery would make sense, if the project needs to operate for a long time, such as during an event or showcase. The trade-off is that a higher capacity battery is also physically larger \-- make sure to plan accordingly for proper battery storage/attachment on your project to reduce strain on the wires and fabric.

***Here are some typical runtimes for various SparkFun batteries and numbers of LilyPad LEDs/LilyPixels:***

**Number of LEDs**

1

2

5

10

20

Battery Name

Battery mAh

Hours of Operation

[Polymer Lithium Ion Battery - 40mAh](https://www.sparkfun.com/products/11316)

40

1.3

0.8

0.4

0.2

0.1

[E-Textiles Battery - 110mAh (2C Discharge)](https://www.sparkfun.com/products/13112)

110

3.7

2.2

1.0

0.5

0.3

[Coin Cell Battery - 20mm (CR2032) \*](https://www.sparkfun.com/products/338)

250

8.3

5.0

2.3

1.2

.61

[Polymer Lithium Ion Battery - 400mAh](https://www.sparkfun.com/products/10718)

400

13.3

8.0

3.6

1.9

1.0

[Polymer Lithium Ion Battery - 850mAh](https://www.sparkfun.com/products/341)

850

28.3

17.0

7.7

4.0

2.1

[Polymer Lithium Ion Battery - 1000mAh](https://www.sparkfun.com/products/339)

1000

33.3

20.0

9.1

4.8

2.4

[Polymer Lithium Ion Battery - 2000mAh](https://www.sparkfun.com/products/8483)

2000

66.7

40.0

18.2

9.5

4.9

[Polymer Lithium Ion Battery - 6Ah](https://www.sparkfun.com/products/8484)

6000

200.0

120.0

54.5

28.6

14.6

`*` Note: the Coin Cell Battery is non-rechargeable.

[] The other [batteries](https://www.sparkfun.com/categories/54) in our catalog are not created especially for e-Textiles. Use caution to avoid shorting out conductive thread traces when using alternative batteries.