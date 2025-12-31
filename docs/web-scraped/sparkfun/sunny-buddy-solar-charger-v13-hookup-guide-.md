# Source: https://learn.sparkfun.com/tutorials/sunny-buddy-solar-charger-v13-hookup-guide-

## Introduction

**Heads up!** If you have an older version of the Sunny Buddy ([V1.0](https://www.sparkfun.com/products/12084) and older), please refer to [this hookup guide](tutorials/170). For V1.3 and beyond, continue reading. Check the back of the board for the version number.

------------------------------------------------------------------------

The [Sunny Buddy](https://www.sparkfun.com/products/12885) is a small maximum power point tracking solar charger for single-cell LiPo batteries.

[![SparkFun Sunny Buddy - MPPT Solar Charger](https://cdn.sparkfun.com/r/600-600/assets/parts/9/7/7/2/12885-01.jpg)](https://www.sparkfun.com/sparkfun-sunny-buddy-mppt-solar-charger.html)

### [SparkFun Sunny Buddy - MPPT Solar Charger](https://www.sparkfun.com/sparkfun-sunny-buddy-mppt-solar-charger.html) 

[ PRT-12885 ]

This is the Sunny Buddy, a maximum power point tracking (MPPT) solar charger for single-cell LiPo batteries. This MPPT solar ...

[ [\$32.95] ]

This tutorial will help you understand what the Sunny Buddy is, why it\'s useful, and how to use it.

### Required Materials

The Sunny Buddy can\'t do anything without a supporting cast. Pair the Sunny Buddy with these buddies to make it work:

- **Solar Panel** \-- Most panels should work, just make sure they produce an output voltage between **6-20V**. Our [large](https://www.sparkfun.com/products/7840) and [huge](https://www.sparkfun.com/products/9241) panels will work. Our [small](https://www.sparkfun.com/products/7845) panels will work if you connect two of them in series (see the \"Hooking It Up\" page for details). The following panels with a center-positive barrel jack will be able to plug directly into the Sunny Buddy with ease.

  :::::::::::: tile-wrap
  ::::: 
  ::: actions-wrap
  [![Solar Panel - 3.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/4/9/13782-01.jpg)](https://www.sparkfun.com/products/13782)
  :::

  ::: main
  ### [Solar Panel - 3.5W](https://www.sparkfun.com/products/13782) 

  [ PRT-13782 ]
  Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...
  :::

  **Retired**
  :::::

  ::::: 
  ::: actions-wrap
  [![Solar Panel - 6W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/0/13783-01.jpg)](https://www.sparkfun.com/products/13783)
  :::

  ::: main
  ### [Solar Panel - 6W](https://www.sparkfun.com/products/13783) 

  [ PRT-13783 ]
  Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...
  :::

  **Retired**
  :::::

  ::::: 
  ::: actions-wrap
  [![Solar Panel - 9W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/1/13784-01.jpg)](https://www.sparkfun.com/products/13784)
  :::

  ::: main
  ### [Solar Panel - 9W](https://www.sparkfun.com/products/13784) 

  [ PRT-13784 ]
  Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...
  :::

  **Retired**
  :::::
  ::::::::::::

  ::: clearfix
  :::

**Heads up!** Under real world conditions, the Sunny Buddy may not be able to charge a LiPo battery sufficiently with the [small 2W](https://www.sparkfun.com/products/13781) solar panel. The Sunny Buddy\'s output charge current measured was about *7mA* since the small 2W solar panel was not able to reach the minimum input voltage requirements by itself. We recommend using a larger solar panel like the [3.5W](https://www.sparkfun.com/products/13782), [6W](https://www.sparkfun.com/products/13783), or [9W](https://www.sparkfun.com/products/13784) solar panels to achieve the Sunny Buddy\'s minimum voltage input requirements.

- **LiPo Battery** (single cell) \-- The Sunny Buddy is intended to charge a single Polymer Lithium Ion cell. LiPo\'s come in all shapes and sizes, we recommend you use one with a capacity greater than 450mAh (e.g. [850mAh](https://www.sparkfun.com/products/341), [1000mAh](https://www.sparkfun.com/products/339), or [2000mAh](https://www.sparkfun.com/products/8483)). Batteries like those, with a JST termination, will plug directly into the Sunny Buddy. The 450mAh size suggestion is due to the charge rate of the Sunny Buddy\--most LiPo cells don\'t like being charged faster than their equivalent capacity.

  ::::::::::::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)
  :::

  ::: main
  ### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

  [ PRT-13854 ]
  These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...
  :::

  :::: 
  ::: prices
  [ [\$13.61] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)
  :::

  ::: main
  ### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

  [ PRT-13855 ]
  These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...
  :::

  :::: 
  ::: prices
  [ [\$19.41] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)
  :::

  ::: main
  ### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

  [ PRT-13856 ]
  If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...
  :::

  :::: 
  ::: prices
  [ [\$48.44] ]
  :::
  ::::
  :::::::

  ::::: 
  ::: actions-wrap
  [![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)
  :::

  ::: main
  ### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

  [ PRT-13813 ]
  Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!
  :::

  **Retired**
  :::::
  :::::::::::::::::::::

  ::: clearfix
  :::

<!-- -->

- **A Load** \-- Your battery has to power *something*, right? Your load can be anything from an [LED](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds) to an [Arduino-powered robot](https://learn.sparkfun.com/tutorials/getting-started-with-the-redbot).

### Suggested Reading

Here are some other tutorials you may find useful before delving into this hookup guide:

- [Batteries](https://learn.sparkfun.com/tutorials/battery-technologies) \-- Check out the battery tutorial for some help understanding why the Sunny Buddy works only with LiPo batteries.

- [Electricity Basics](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) \-- It may be useful to review how current and voltage combine to transmit power to a load.

- [How to Power Your Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project) \-- Solar power and batteries are just one of many ways to power your project. Make sure to consider all possibilities!

- ::::::::::::::: tile-wrap
  :::::: 
  [](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

  :::: thumb-wrap
  ::: 
  :::
  ::::

  ### Voltage, Current, Resistance, and Ohm\'s Law 

  ::: description
  Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.
  :::
  ::::::

  :::::: 
  [](https://learn.sparkfun.com/tutorials/battery-technologies)

  :::: thumb-wrap
  ::: 
  :::
  ::::

  ### Battery Technologies 

  ::: description
  The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.
  :::
  ::::::

  :::::: 
  [](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

  :::: thumb-wrap
  ::: 
  :::
  ::::

  ### How to Power a Project 

  ::: description
  A tutorial to help figure out the power requirements of your project.
  :::
  ::::::
  :::::::::::::::

  ::: clearfix
  :::

## Why MPPT?

The Sunny Buddy is a maximum power point transfer (MPPT) solar charger. Why does that matter? What makes it worth having in a circuit? The answers lay ahead.

#### How Batteries Are Charged

Battery charging is a current dependent action, not a voltage dependent action. Battery chargers monitor the current flowing into the battery and limit it to some set value, chosen to prevent damage to the battery. An ideal battery charger will provide as much current to the battery as it is capable of drawing from its power supply, but no more than the battery can handle.

#### Power Supply Behavior

Consider the first part of that last sentence: \"as much current as it is capable of drawing from its power supply.\" I\'ve collected some data from five different power supplies: a [2000 mAh LiPo battery](https://www.sparkfun.com/products/8483), a bench supply, our [small solar cell](https://www.sparkfun.com/products/7845), our [large solar cell](https://www.sparkfun.com/products/7840), and the Sunny Buddy attached to the small cell in full Colorado sunlight (albeit in midwinter).

-\> [![Load testing results of various supplies](https://cdn.sparkfun.com/r/600-600/assets/4/0/0/c/9/52e84215ce395fcf468b4568.png)](https://cdn.sparkfun.com/assets/4/0/0/c/9/52e84215ce395fcf468b4568.png)

*That\'s some mighty fine data!*

The chart compares output voltage versus load current for the five sources listed above: in short, how much current each is capable of providing. For a sort of baseline comparison, note that the output of the bench supply, the battery, and the Sunny Buddy are pretty flat. You can clearly see the point at about 240mA where the Sunny Buddy could no longer safely draw more current from the solar cell. In a charging application, that\'s the point at which it would have settled in and charged the battery. Since I was actively increasing the load to stress the supplies, it folded back to a lower voltage to gracefully handle the excessive load without bursting into flames.

The solar cells, however, behave quite differently. They slowly droop until they reach a certain point, then decline increasingly rapidly until even a small increase in current draw causes the output voltage to plummet. There\'s a point on that curve, in the \"knee\" region, where the power transferred to the load is at its peak. This point, called the **maximum power point**, is crucial to squeezing the most efficiency out of a solar cell.

Finding that point is the key here. The solar cell curves will be compressed along the X-axis in lower light conditions, and, while the unloaded voltage may remain quite high even in low light, the amount of current which can be drawn from the cell decreases rapidly with the amount of light available.

The Sunny Buddy locks in on that point in the curve, pulling the maximum current the cell will provide, but no more, and turning it into charge current. The circled region of the graph shows this: the highest current the small solar cell can deliver is around 180mA, but the Sunny Buddy pushes out 240mA before entering current limit. That\'s an extra 33% more charge current available to your battery over a comparable 5V charger.

#### Efficiency

Efficiency in any power supply system can be said to be the ratio of power out to power in. This is another place where the Sunny Buddy is better than comparable linear solutions.

The Sunny Buddy is a switching supply; the output power is given by the equation `Pout = Pin * Efficiency`. The Sunny Buddy\'s efficiency has repeatedly measured to be about 80% in tests.

Let\'s consider a linear solution. To avoid getting too far into that steep region of the graph, we\'ll set our charge current at 160mA. To calculate the output efficiency, we divided the output power by the input power. Looking at the voltage on the solar cell curve, we see that for 160mA the output voltage is about 7V; thus, input power is `7V * 160mA = 1142mW`. Output power is `4.2V * 160mA = 672mW`. That\'s the approximate charge voltage times the charge current. Efficiency is power in over power out: `672/1142 = 59%`. Best case, that\'s the percentage of the electric power generated by the cell that you\'re using. It will actually be lower when the cell voltage is lower than 4.2V, which it will be over most of the charging range.

Here, again, Sunny Buddy wins: it\'s using (at least) 20% more of the available power from the solar cell.

#### Cloudy Days

But what happens to our linear charge circuit when the sun goes behind a cloud? As I mentioned earlier, as available solar energy decreases, the graph compresses along the X-axis. If that steep region drops below the set current of our charger, things go pear-shaped fast. The available voltage plummets, and the charger stops working.

We can combat that by either setting a lower charge current in the first place, which isn\'t ideal because it means on a good, sunny day, you\'re losing a lot of potential solar energy by not loading the solar cell heavily enough, or by servoing our charge current to the voltage, reducing or increasing it based on the cell voltage. While that may sound simple, in practice it\'s quite complex.

#### Enter the Sunny Buddy

The Sunny Buddy does just that: it monitors the cell voltage and stops drawing current when the voltage droop indicates the cell is being pushed a little too far. Furthermore, since the Sunny Buddy uses a switching topology rather than a linear topology, it has a better efficiency than any linear solution can provide.

## Hooking It Up

There are three parts to consider when embedding the Sunny Buddy into a project:

- Solar Panel Input
- Battery Output
- Load

[![Sunny Buddy Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/0/sunny-buddy-hookup_2_1000w.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/0/sunny-buddy-hookup_2_1000w.png)

### Solar Panel Input

The input side of the Sunny Buddy comes with a common barrel jack installed.

[![Input diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/3/input_map.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/3/input_map.jpg)

The following solar panels can be plugged directly in to the Sunny Buddy\'s female barrel jack with ease.

[![Solar Panel - 3.5W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/4/9/13782-01.jpg)](https://www.sparkfun.com/products/13782)

### [Solar Panel - 3.5W](https://www.sparkfun.com/products/13782) 

[ PRT-13782 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

[![Solar Panel - 6W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/0/13783-01.jpg)](https://www.sparkfun.com/products/13783)

### [Solar Panel - 6W](https://www.sparkfun.com/products/13783) 

[ PRT-13783 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

[![Solar Panel - 9W](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/5/1/13784-01.jpg)](https://www.sparkfun.com/products/13784)

### [Solar Panel - 9W](https://www.sparkfun.com/products/13784) 

[ PRT-13784 ]

Have a project that needs some good power? Do you like free power provided by our friend, Mr. Sun? Check out this high qualit...

**Retired**

**Heads up!** Under real world conditions, the Sunny Buddy may not be able to charge a LiPo battery sufficiently with the [small 2W](https://www.sparkfun.com/products/13781) solar panel. The Sunny Buddy\'s output charge current measured was about *7mA* since the small 2W solar panel was not able to reach the minimum input voltage requirements by itself. We recommend using a larger solar panel like the [3.5W](https://www.sparkfun.com/products/13782), [6W](https://www.sparkfun.com/products/13783), or [9W](https://www.sparkfun.com/products/13784) solar panels to achieve the Sunny Buddy\'s minimum voltage input requirements.

There are also additional footprints for attaching [3.5mm screw terminals](https://www.sparkfun.com/products/8084) or an additional [barrel jack](https://www.sparkfun.com/products/119) to the board.

[![DC Barrel Power Jack/Connector](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/8/00119-03-L.jpg)](https://www.sparkfun.com/dc-barrel-power-jack-connector.html)

### [DC Barrel Power Jack/Connector](https://www.sparkfun.com/dc-barrel-power-jack-connector.html) 

[ PRT-00119 ]

DC power jack/connector. This is a common barrel-type power jack for DC wall supplies. These are compatible with our DC wall ...

[ [\$1.75] ]

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

Please note that if you intend to use two solar panels, you **must** clear solder jumper **JP1** (it ships closed by default) and close solder jumper JP2 (it ships open by default). Failure to do this will result in the second supply being left unconnected. If *both* jumpers are left unconnected, no power will be sent to the board. If both jumpers are *shorted*, the second panel will be shorted out and contribute no power to the system but may be damaged by being short circuited.

The maximum recommended input to the board is **20V**; this is a stack of two of our panels. The minimum is **6V**, but most solar panels should be above this.

A useful trick for monitoring the input current of a single-panel system is to open JP1 and close JP2, then [connect an ammeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#measuring-current) between the **+** pads on the two 3.5mm footprints. This will allow you to monitor the current draw from the solar panel. **Note that JP1 must be resoldered and JP2 reopened before attempting to use the SunnyBuddy without the meter in place!**

### Setting the Input Current Limit

The revised Sunny Buddy has an input set point potentiometer. This allows the user to set an input voltage at which the Sunny Buddy will reduce its current draw to maintain peak power input from the solar panel.

You\'ll want the voltage at this node to be at 2.7V when the solar panel is at the \"knee\" voltage we discussed in the **Why MPPT?** section above. Some solar cell manufacturers may give you this information; the manufacturers of our panels, however, have not. You can either take the hard road and characterize your cell (ick) or take the easy road and make an educated guess that the MPPT point will be at about 90% of the voltage you see when you\'re in full sun.

To find that point, plug your solar panel into the Sunny Buddy, but don\'t put a battery or load on it. Measure the voltage from the \"SET\" pad to the \"GND\" pad next two it, and tweak the potentiometer until that voltage is about 3V. At that point, the Sunny Buddy will draw current until either 450mA is going to the load and the battery **or** the solar cell voltage is 90% of its full-sun open-circuit nominal voltage.

### Battery Output

The output of the Sunny Buddy is intended to charge a single Polymer Lithium Ion cell. A 2-pin JST connector is populated, and will mate up to most of the LiPo batteries SparkFun sells.The load should be connected in parallel with the battery; again, footprints for a 3.5mm terminal or a standard .1\" spaced header have been provided.

[![Output diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/3/output_tour.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/3/output_tour.jpg)

The charge current is set by resistor R1 in the schematic. By default it comes set to a maximum charge current of **450mA**. It\'s recommended that batteries not be charged at greater than their capacity rating; thus, the smallest battery that should be charged with the Sunny Buddy is 450mAh.

The revised Sunny Buddy adds an additional sense resistor footprint in parallel with the built-in resistor. The charge current is equal to .1/(R1\|\|RSen); putting a 1-ohm resistor on the Rsen pads will increase the charge current to \~550mA. R1 can be desoldered from the board if charge currents below 450mA are desired.

Note that it is possible to set the charge current to impossible levels. If the current level is too high, the inductor will saturate, which will limit the output current artificially.

Finally, note that there\'s a jumper on the board that can be cut to allow you to monitor the output current of the charger. You\'ll need to reconnect the jumper pads after you\'ve finished taking measurements.

### The Load

The load can be connected to either the 0.1\" or 3.5mm spaced pads on the right edge of the board.

[![LED Strip Pigtail Connector (2-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/1/9/14574-LED_Pigtail_connector_2_Pin_-01.jpg)](https://www.sparkfun.com/led-strip-pigtail-connector-2-pin.html)

### [LED Strip Pigtail Connector (2-pin)](https://www.sparkfun.com/led-strip-pigtail-connector-2-pin.html) 

[ CAB-14574 ]

These 2-pin JST-SM pigtail connectors mate perfectly with LED strips and other applications that require only two lines and a...

[ [\$1.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

It\'s important that the load not be too heavy; since it is in parallel with the battery, it will steal some of the charge current from the battery when it is operating.

To avoid this, [consider putting active circuitry to sleep](https://learn.sparkfun.com/tutorials/reducing-arduino-power-consumption) whenever possible, or using a microcontroller to turn parts of the load on or off as they are not needed. Methods for doing this are beyond the scope of this tutorial.