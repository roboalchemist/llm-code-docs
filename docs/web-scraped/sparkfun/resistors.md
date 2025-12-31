# Source: https://learn.sparkfun.com/tutorials/resistors

## Take a Stance, The Resist Stance

Resistors - the most ubiquitous of electronic components. They are a critical piece in just about every circuit. And they play a major role in our favorite equation, [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/ohms-law).

[![resistors](https://cdn.sparkfun.com/r/500-500/assets/c/4/a/9/d/515c7a2bce395f653d000002.png)](https://cdn.sparkfun.com/assets/c/4/a/9/d/515c7a2bce395f653d000002.png)

In this, our pièce de *résistance*, we\'ll cover:

- What is a resistor?!
- Resistor units
- Resistor circuit symbol(s)
- Resistors in series and parallel
- Different variations of resistors
- Color coding decoding
- Surface mount resistor decoding
- Example resistor applications

### Consider reading\...

Some of the concepts in this tutorial build on previous electronics knowledge. Before jumping into this tutorial, consider reading (at least skimming) these first:

- [What is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [What is a Circuit](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [Series vs. Parallel Circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
- [How to Use A Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/) - Specifically check out the [measuring resistance](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/measuring-resistance) section.
- [Metric Prefixes](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units)

------------------------------------------------------------------------

## Looking to get hands-on with resistors?

We\'ve got you covered!

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/6/14491-03.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14491 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.50] ]

[![Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/7/14490-03.jpg)](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14490 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.25] ]

[![Power Resistor Kit - 10W (25 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/7/1/10353-01.jpg)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html)

### [Power Resistor Kit - 10W (25 pack)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html) 

[ KIT-13053 ]

Holy Wattage, Batman! This Power Resistor Kit comes with 5 each of 5 different 10 Watt resistor values including 1 Ohm, 2 Ohm...

[ [\$9.50] ]

[See all resistors](https://www.sparkfun.com/categories/324)

 

![Field Guide to Resistors](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/resistors.png)

 

## Resistor Basics

Resistors are electronic components which have a specific, never-changing [electrical resistance](../voltage-current-resistance-and-ohms-law/resistance). The resistor\'s resistance **limits the flow of electrons** through a circuit.

They are **passive** components, meaning they only consume power (and can\'t generate it). Resistors are usually added to circuits where they complement **active** components like op-amps, microcontrollers, and other [integrated circuits](https://learn.sparkfun.com/tutorials/integrated-circuits). Commonly resistors are used to limit current, [divide voltages](https://learn.sparkfun.com/tutorials/voltage-dividers), and [pull-up I/O lines](https://learn.sparkfun.com/tutorials/pull-up-resistors).

## Resistor units

The electrical resistance of a resistor is measured in **ohms**. The symbol for an ohm is the greek capital-omega: Ω. The (somewhat roundabout) definition of 1Ω is the resistance between two points where 1 volt (1V) of applied potential energy will push 1 ampere (1A) of current.

As [SI units](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units) go, larger or smaller values of ohms can be matched with a prefix like kilo-, mega-, or giga-, to make large values easier to read. It\'s very common to see resistors in the kilohm (kΩ) and megaohm (MΩ) range (much less common to see miliohm (mΩ) resistors). For example, a 4,700Ω resistor is equivalent to a 4.7kΩ resistor, and a 5,600,000Ω resistor can be written as 5,600kΩ or (more commonly as) 5.6MΩ.

## Schematic symbol

All resistors have **two terminals**, one connection on each end of the resistor. When modeled on a schematic, a resistor will show up as one of these two symbols:

[![Resistor schematic symbols](https://cdn.sparkfun.com/r/600-600/assets/f/c/c/c/b/515dbf24ce395f2359000000.png)](https://cdn.sparkfun.com/assets/f/c/c/c/b/515dbf24ce395f2359000000.png)

*Two common resistor schematic symbols. R1 is an American-style 1kΩ resistor, and R2 is an international-style 47kΩ resistor.*

The terminals of the resistor are each of the lines extending from the squiggle (or rectangle). Those are what connect to the rest of the circuit.

The resistor circuit symbols are usually enhanced with both a resistance value and a name. The value, displayed in ohms, is obviously critical for both evaluating and actually constructing the circuit. The name of the resistor is usually an *R* preceding a number. Each resistor in a circuit should have a unique name/number. For example, here\'s a few resistors in action on a 555 timer circuit:

[![Example schematic with resistors - a 555 timer](https://cdn.sparkfun.com/assets/7/f/4/f/7/515dc512ce395f4e58000001.PNG)](https://cdn.sparkfun.com/assets/7/f/4/f/7/515dc512ce395f4e58000001.PNG)

*In this circuit, resistors play a key role in setting the frequency of the 555 timer\'s output. Another resistor (R3) limits the current through an LED.*

------------------------------------------------------------------------

## Types of Resistors

Resistors come in a variety of shapes and sizes. They might be through-hole or surface-mount. They might be a standard, static resistor, a pack of resistors, or a special variable resistor.

## Termination and Mounting

Resistors will come in one of two termination-types: through-hole or surface-mount. These types of resistors are usually abbreviated as either PTH (plated through-hole) or SMD/SMT (surface-mount technology or device).

**Through-hole** resistors come with long, pliable leads which can be stuck into a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) or hand-soldered into a prototyping board or [printed circuit board (PCB)](https://learn.sparkfun.com/tutorials/pcb-basics). These resistors are usually more useful in breadboarding, prototyping, or in any case where you\'d rather not solder tiny, little 0.6mm-long SMD resistors. The long leads usually require trimming, and these resistors are bound to take up much more space than their surface-mount counterparts.

The most common through-hole resistors come in an axial package. The size of an axial resistor is relative to its power rating. A common ½W resistor measures about 9.2mm across, while a smaller ¼W resistor is about 6.3mm long.

[![1/4 and 1/2 watt resistors](https://cdn.sparkfun.com/assets/6/9/c/4/3/515dcac7ce395f7259000000.png)](https://cdn.sparkfun.com/assets/6/9/c/4/3/515dcac7ce395f7259000000.png)

*A half-watt (½W) resistor (above) sized up to a quarter-watt (¼W).*

**Surface-mount** resistors are usually tiny black rectangles, terminated on either side with even smaller, shiny, silver, conductive edges. These resistors are intended to sit on top of PCBs, where they\'re soldered onto mating landing pads. Because these resistors are so small, they\'re usually set into place by a [robot](https://learn.sparkfun.com/tutorials/electronics-assembly/pick-and-place), and sent through an oven where solder melts and holds them in place.

[![SMD resistor on a quarter](https://cdn.sparkfun.com/assets/d/b/5/b/a/515dcbe6ce395fec3b000000.jpg)](https://cdn.sparkfun.com/assets/4/e/e/7/f/515dcb62ce395f5959000000.jpg)

*A tiny 0603 330Ω resistor hovering over shiny George Washington\'s nose on top of a \[U.S. quarter\](http://en.wikipedia.org/wiki/Quarter\_(United_States_coin).*

SMD resistors come in standardized sizes; usually either 0805 (0.08\" long by 0.05\" wide), 0603, or 0402. They\'re great for mass circuit-board-production, or in designs where space is a precious commodity. They take a steady, precise hand to manually solder, though!

## Resistor Composition

Resistors can be constructed out of a variety of materials. Most common, modern resistors are made out of either a **carbon, metal, or metal-oxide film**. In these resistors, a thin film of conductive (though still resistive) material is wrapped in a helix around and covered by an insulating material. Most of the standard, no-frills, through-hole resistors will come in a carbon-film or metal-film composition.

[![Peeled away view of carbon-film resistors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/4/fixResistors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/fixResistors.jpg)

*Peek inside the guts of a few carbon-film resistors. Resistance values from top to bottom: 27Ω, 330Ω and a 3.3MΩ. Inside the resistor, a carbon film is wrapped around an insulator. More wraps means a higher resistance. Pretty neat!*

Other through-hole resistors might be wirewound or made of super-thin metallic foil. These resistors are usually more expensive, higher-end components specifically chosen for their unique characteristics like a higher power-rating, or maximum temperature range.

Surface-mount resistors are usually either **thick or thin-film** variety. Thick-film is usually cheaper but less precise than thin. In both resistor types, a small film of resistive metal alloy is sandwiched between a ceramic base and glass/epoxy coating, and then connected to the terminating conductive edges.[]

## Special Resistor Packages[]

There are a variety of other, special-purpose resistors out there. Resistors may come in pre-wired packs of five-or-so [resistor arrays](https://www.sparkfun.com/products/10855). Resistors in these arrays may share a common pin, or be set up as voltage dividers.

[![Resistor Network](https://cdn.sparkfun.com/r/600-600/assets/9/f/e/3/6/515ddfc0ce395f9a58000000.png)](https://cdn.sparkfun.com/assets/9/f/e/3/6/515ddfc0ce395f9a58000000.png)

*An array of five 330Ω resistors, all tied together at one end.*

## Variable Resistors (i.e. Potentiometers)

Resistors don\'t have to be static either. Variable resistors, known as **rheostats**, are resistors which can be adjusted between a specific range of values. Similar to the rheostat is the **potentiometer**. Pots connect two resistors internally, in series, and adjust a center tap between them creating an adjustable [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers). These variable resistors are often used for inputs, like volume knobs, which need to be adjustable.

[![A smattering of potentiometers](https://cdn.sparkfun.com/assets/6/6/4/4/2/515deb26ce395f3959000000.png)](https://cdn.sparkfun.com/assets/6/6/4/4/2/515deb26ce395f3959000000.png)

*A smattering of potentiometers. From top-left, clockwise: [a standard 10k trimpot](https://www.sparkfun.com/products/9288), [2-axis joystick](https://www.sparkfun.com/products/9032), [softpot](https://www.sparkfun.com/products/9074), a [breadboard friendly 10k trimpot](https://www.sparkfun.com/products/9806), [classic right-angle](https://www.sparkfun.com/products/9939), and a [slide pot](https://www.sparkfun.com/products/11620).*

------------------------------------------------------------------------

## Decoding Resistor Markings

Though they may not display their value outright, most resistors are marked to show what their resistance is. PTH resistors use a color-coding system (which really adds some flair to circuits), and SMD resistors have their own value-marking system.

## Decoding the Color Bands

Through-hole, axial resistors usually use the color-band system to display their value. Most of these resistors will have four bands of color circling the resistor, though you will also find five band and six band resistors.

[![Resistors showing their stripes](https://cdn.sparkfun.com/r/600-600/assets/c/4/a/9/d/515c7a2bce395f653d000002.png)](https://cdn.sparkfun.com/assets/c/4/a/9/d/515c7a2bce395f653d000002.png)

### Four Band Resistors

In the standard four band resistors, the first two bands indicate the **two most-significant digits** of the resistor\'s value. The third band is a weight value, which **multiplies** the two significant digits by a power of ten.

The final band indicates the **tolerance** of the resistor. The tolerance explains how much more or less the *actual* resistance of the resistor can be compared to what its nominal value is. No resistor is made to perfection, and different manufacturing processes will result in better or worse tolerances. For example, a 1kΩ resistor with 5% tolerance could actually be anywhere between 0.95kΩ and 1.05kΩ.

How do you tell which band is first and last? The last, tolerance band is often clearly separated from the value bands, and usually it\'ll either be silver or gold.

### Five and Six Band Resistors

Five band resistors have a third significant digit band between the first two bands and the **multiplier band**. Five band resistors also have a wider range of tolerances available.

Six band resistors are basically five band resistors with an additional band at the end that indicates the temperature coefficient. This indicates the expected change in resistor value as the temperature changes in degrees Celsius. Generally these temperature coefficient values are extremely small, in the ppm range.

### Decoding Resistor Color Bands

When decoding the resistor color bands, consult a resistor color code table like the one below. For the first two bands, find that color\'s corresponding digit value. The 4.7kΩ resistor shown here has color bands of yellow and violet to begin - which have digit values of 4 and 7 (47). The third band of the 4.7kΩ is red, which indicates that the 47 should be multiplied by 10^2^ (or 100). 47 times 100 is 4,700!

[![Close-up of a 4.7kOhm resistor](https://cdn.sparkfun.com/r/600-600/assets/7/1/1/a/b/5165e04ece395f663e000001.jpg)](https://cdn.sparkfun.com/assets/1/0/4/0/9/5165df6ace395f343f000003.jpg)

*4.7kΩ resistor with four color bands*

If you\'re trying to commit the color band code to memory, a mnemonic device might help. There are [a handful of](http://en.wikipedia.org/wiki/List_of_electronic_color_code_mnemonics) (sometimes unsavory) mnemonics out there to help remember the resistor color code. A good one, which spells out the difference between *b*lack and *b*rown is:

\"**B**ig **b**rown **r**abbits **o**ften **y**ield **g**reat **b**ig **v**ocal **g**roans **w**hen **g**ingerly **s**napped.\"

\

Or, if you remember \"ROY G. BIV\", subtract the *indigo* (poor indigo, no one remembers indigo), and add black and brown to the front and gray and white to the back of the classic rainbow color-order.

### Resistor Color Code Table

[![Image of 4, 5, and 6 band resistors and what each band stands for](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/Resistors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/4/Resistors.png)

*Having trouble seeing? Click the image for a better view!*

### Resistor Color Code Calculator

If you\'d rather skip the math (we won\'t judge!), and just use a handy calculator, give one of these a try!

#### Four Band Resistors

Band 1

Band 2

Band 3

Band 4

Value 1 (MSV)

Value 2

Weight

Tolerance

Black (0) Brown (1) Red (2) Orange (3) Yellow (4) Green (5) Blue (6) Violet (7) Gray (8) White (9)

Black (0) Brown (1) Red (2) Orange (3) Yellow (4) Green (5) Blue (6) Violet (7) Gray (8) White (9)

Black (1) Brown (10) Red (100) Orange (1k) Yellow (10k) Green (100k) Blue (1M) Violet (10M) Gray (100M) White (1G)

   

Gold (± 5%) Silver (± 10%)

### Resistance:  1 kΩ ±5%

#### Five and Six Band Resistors

**Note:** Calculate your six band resistor here, but be sure to append the temperature coefficient to the final value of the resistor.\
\
\

Band 1

Band 2

Band 3

Band 4

Band 5

Value 1 (MSV)

Value 2

Value 3

Weight

Tolerance

Black (0) Brown (1) Red (2) Orange (3) Yellow (4) Green (5) Blue (6) Violet (7) Gray (8) White (9)

Black (0) Brown (1) Red (2) Orange (3) Yellow (4) Green (5) Blue (6) Violet (7) Gray (8) White (9)

Black (0) Brown (1) Red (2) Orange (3) Yellow (4) Green (5) Blue (6) Violet (7) Gray (8) White (9)

Black (1) Brown (10) Red (100) Orange (1k) Yellow (10k) Green (100k) Blue (1M) Violet (10M) Gray (100M) White (1G)

   

Gold (± 5%) Silver (± 10%) Brown (± 1%) Red (± 2%) Green (± 0.5%) Blue (± 0.25%) Violet (± 0.1%) Gray (± 0.05%)

### Resistance:  1 kΩ ±5%

## Decoding Surface-Mount Markings

SMD resistors, like those in 0603 or 0805 packages, have their own way of displaying their value. There are a few common marking methods you\'ll see on these resistors. They\'ll usually have three to four characters \-- numbers or letters \-- printed on top of the case.

If the three characters you\'re seeing are *all numbers*, you\'re probably looking at an **E24** marked resistor. These markings actually share some similarity with the color-band system used on the PTH resistors. The first two numbers represent the first two most-significant digits of the value, the last number represents a magnitude.

[![Examples of E-24 marked SMD resistors](https://cdn.sparkfun.com/r/600-600/assets/b/b/1/6/6/5165e105ce395f443f000002.jpg)](https://cdn.sparkfun.com/assets/b/b/1/6/6/5165e105ce395f443f000002.jpg)

In the above example picture, resistors are marked *104*, *105*, *205*, *751*, and *754*. The resistor marked with *104* should be 100kΩ (10x10^4^), *105* would be 1MΩ (10x10^5^), and *205* is 2MΩ (20x10^5^). *751* is 750Ω (75x10^1^), and *754* is 750kΩ (75x10^4^).

Another common coding system is **E96**, and it\'s the most cryptic of the bunch. E96 resistors will be marked with three characters \-- two numbers at the beginning and a letter at the end. The two numbers tell you the first *three* digits of the value, by corresponding to one of the not-so-obvious values on this lookup table.

  -------------------------------------------------------------------------------------------------------------
  Code   Value   \   Code   Value   \   Code   Value   \   Code   Value   \   Code   Value   \   Code   Value
  ------ ------- --- ------ ------- --- ------ ------- --- ------ ------- --- ------ ------- --- ------ -------
  01     100     \   17     147     \   33     215     \   49     316     \   65     464     \   81     681

  02     102     \   18     150     \   34     221     \   50     324     \   66     475     \   82     698

  03     105     \   19     154     \   35     226     \   51     332     \   67     487     \   83     715

  04     107     \   20     158     \   36     232     \   52     340     \   68     499     \   84     732

  05     110     \   21     162     \   37     237     \   53     348     \   69     511     \   85     750

  06     113     \   22     165     \   38     243     \   54     357     \   70     523     \   86     768

  07     115     \   23     169     \   39     249     \   55     365     \   71     536     \   87     787

  08     118     \   24     174     \   40     255     \   56     374     \   72     549     \   88     806

  09     121     \   25     178     \   41     261     \   57     383     \   73     562     \   89     825

  10     124     \   26     182     \   42     267     \   58     392     \   74     576     \   90     845

  11     127     \   27     187     \   43     274     \   59     402     \   75     590     \   91     866

  12     130     \   28     191     \   44     280     \   60     412     \   76     604     \   92     887

  13     133     \   29     196     \   45     287     \   61     422     \   77     619     \   93     909

  14     137     \   30     200     \   46     294     \   62     432     \   78     634     \   94     931

  15     140     \   31     205     \   47     301     \   63     442     \   79     649     \   95     953

  16     143     \   32     210     \   48     309     \   64     453     \   80     665     \   96     976
  -------------------------------------------------------------------------------------------------------------

\

The letter at the end represents a multiplier, matching up to something on this table:

  Letter   Multiplier      Letter   Multiplier      Letter   Multiplier
  -------- ------------ -- -------- ------------ -- -------- ------------
  Z        0.001           A        1               D        1000
  Y or R   0.01            B or H   10              E        10000
  X or S   0.1             C        100             F        100000

\

[![Resistors marked with E-96 codes](https://cdn.sparkfun.com/r/600-600/assets/6/1/2/f/9/5165e105ce395f463f000001.jpg)](https://cdn.sparkfun.com/assets/6/1/2/f/9/5165e105ce395f463f000001.jpg)

So a *01C* resistor is our good friend, 10kΩ (100x100), *01B* is 1kΩ (100x10), and *01D* is 100kΩ. Those are easy, other codes may not be. *85A* from the picture above is 750Ω (750x1) and *30C* is actually 20kΩ.

------------------------------------------------------------------------

## Power Rating

The power rating of a resistor is one of the more hidden values. Nevertheless it can be important, and it\'s a topic that\'ll come up when selecting a resistor type.

[Power](https://learn.sparkfun.com/tutorials/electric-power) is the rate at which energy is transformed into something else. It\'s calculated by multiplying the voltage difference across two points by the current running between them, and is measured in units of a watt (W). Light bulbs, for example, power electricity into light. But a resistor can only turn electrical energy running through it into **heat**. Heat isn\'t usually a nice playmate with electronics; too much heat leads to smoke, sparks, and fire!

Every resistor has a specific maximum power rating. In order to keep the resistor from heating up too much, it\'s important to make sure the power across a resistor is kept under it\'s maximum rating. The power rating of a resistor is measured in watts, and it\'s usually somewhere between ⅛W (0.125W) and 1W. Resistors with power ratings of more than 1W are usually referred to as power resistors, and are used specifically for their power dissipating abilities.

## Finding a resistor\'s power rating

A resistor\'s power rating can usually be deduced by observing its package size. Standard through-hole resistors usually come with ¼W or ½W ratings. More special purpose, power resistors might actually list their power rating on the resistor.

[![Some examples of power resistors](https://cdn.sparkfun.com/r/600-600/assets/7/7/3/6/1/5165e344ce395ff93e000000.jpg)](https://cdn.sparkfun.com/assets/7/7/3/6/1/5165e344ce395ff93e000000.jpg)

*These power resistors can handle a lot more power before they blow. From top-right to bottom-left there are examples of 25W, 5W and 3W resistors, with values of 2Ω, 3Ω 0.1Ω and 22kΩ. Smaller power-resistors are often used to sense current.*

The power ratings of surface mount resistors can usually be judged by their size as well. Both 0402 and 0603-size resistors are usually rated for 1/16W, and 0805\'s can take 1/10W.

## Measuring power across a resistor

Power is usually calculated by multiplying voltage and current (P = IV). But, by applying Ohm\'s law, we can also use the resistance value in calculating power. If we know the current running through a resistor, we can calculate the power as:

[![P=I\^2\*R](https://cdn.sparkfun.com/assets/3/2/b/9/b/515f2ea5ce395f6f25000003.png)](https://cdn.sparkfun.com/assets/3/2/b/9/b/515f2ea5ce395f6f25000003.png)

Or, if we know the voltage across a resistor, the power can be calculated as:

[![P=V\^2/R](https://cdn.sparkfun.com/assets/1/0/6/8/6/515f2ea5ce395f8a24000000.png)](https://cdn.sparkfun.com/assets/1/0/6/8/6/515f2ea5ce395f8a24000000.png)

------------------------------------------------------------------------

## Series and Parallel Resistors

Resistors are paired together all the time in electronics, usually in either a [series or parallel](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits) circuit. When resistors are combined in series or parallel, they create a **total resistance**, which can be calculated using one of two equations. Knowing how resistor values combine comes in handy if you need to create a specific resistor value.

## Series resistors

When connected in series resistor values simply add up.

[![Schematic of resistors in series](https://cdn.sparkfun.com/r/600-600/assets/f/b/0/0/b/515f1161ce395f4c25000000.png)](https://cdn.sparkfun.com/assets/f/b/0/0/b/515f1161ce395f4c25000000.png)

[![Equation for adding resistors in series](https://cdn.sparkfun.com/assets/8/5/1/e/5/515f1161ce395f9824000000.png)](https://cdn.sparkfun.com/assets/8/5/1/e/5/515f1161ce395f9824000000.png)

*N resistors in series. The total resistance is the sum of all series resistors.*

So, for example, if you just *have to have* a 12.33kΩ resistor, seek out some of the more common resistor values of 12kΩ and 330Ω, and butt them up together in series.

## [] Parallel resistors

Finding the resistance of resistors in parallel isn\'t quite so easy. The total resistance of *N* resistors in parallel is the inverse of the sum of all inverse resistances. This equation might make more sense than that last sentence:

[![Schematic of resistors in parallel](https://cdn.sparkfun.com/r/300-300/assets/3/4/e/d/c/515f1161ce395ff424000000.png)](https://cdn.sparkfun.com/assets/3/4/e/d/c/515f1161ce395ff424000000.png)

[![Equation for adding resistors in parallel](https://cdn.sparkfun.com/assets/7/0/e/2/9/515f1161ce395ff630000000.png)](https://cdn.sparkfun.com/assets/7/0/e/2/9/515f1161ce395ff630000000.png)

*N resistors in parallel. To find the total resistance, invert each resistance value, add them up, and then invert that.*

(The inverse of resistance is actually called **conductance**, so put more succinctly: the *conductance* of parallel resistors is the sum of each of their conductances).

As a special case of this equation: if you have **just two** resistors in parallel, their total resistance can be calculated with this slightly-less-inverted equation:

[![Equation for calculating two resistors in parallel](https://cdn.sparkfun.com/assets/5/6/7/a/6/515f1161ce395f4d25000000.png)](https://cdn.sparkfun.com/assets/5/6/7/a/6/515f1161ce395f4d25000000.png)

As an even *more special* case of that equation, if you have two parallel resistors of **equal value** the total resistance is half of their value. For example, if two 10kΩ resistors are in parallel, their total resistance is 5kΩ.

A shorthand way of saying two resistors are in parallel is by using the parallel operator: **\|\|**. For example, if R~1~ is in parallel with R~2~, the conceptual equation could be written as R~1~\|\|R~2~. Much cleaner, and hides all those nasty fractions!

## Resistor networks

As a special introduction to calculating total resistances, electronics teachers just *love* to subject their students to finding that of crazy, convoluted resistor networks.

A tame resistor network question might be something like: \"what\'s the resistance from terminals *A* to *B* in this circuit?\"

[![An example of a resistor network](https://cdn.sparkfun.com/r/600-600/assets/4/9/8/d/f/515f2153ce395fc724000000.png)](https://cdn.sparkfun.com/assets/4/9/8/d/f/515f2153ce395fc724000000.png)

To solve such a problem, start at the back-end of the circuit and simplify towards the two terminals. In this case R~7~, R~8~ and R~9~ are all in series and can be added together. Those three resistors are in parallel with R~6~, so those four resistors could be turned into one with a resistance of R~6~\|\|(R~7~+R~8~+R~9~). Making our circuit:

[![Resistor network simplified](https://cdn.sparkfun.com/r/600-600/assets/2/7/d/8/e/515f242dce395f1d25000001.png)](https://cdn.sparkfun.com/assets/2/7/d/8/e/515f242dce395f1d25000001.png)

Now the four right-most resistors can be simplified even further. R~4~, R~5~ and our conglomeration of R~6~ - R~9~ are all in series and can be added. Then those series resistors are all in parallel with R~3~.

[![Resistor network further simplified](https://cdn.sparkfun.com/r/600-600/assets/c/e/1/c/f/515f252ece395f5924000000.png)](https://cdn.sparkfun.com/assets/c/e/1/c/f/515f252ece395f5924000000.png)

And that\'s just three series resistors between the *A* and *B* terminals. Add \'em on up! So the total resistance of that circuit is: R~1~+R~2~+R~3~\|\|(R~4~+R~5~+R~6~\|\|(R~7~+R~8~+R~9~)).

------------------------------------------------------------------------

## Example Applications

Resistors exist in just about every electronic circuit ever. Here are a few examples of circuits, which heavily depend on our resistor friends.

## [] [LED Current Limiting](#current-limiting)

Resistors are key in making sure [LEDs](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds) don\'t blow up when power is applied. By connecting a resistor **in series** with an LED, current flowing through the two components can be limited to a safe value.

[![Current limiting resistor schematic](https://cdn.sparkfun.com/r/400-400/assets/4/6/2/1/4/515f3293ce395f4a25000000.png)](https://cdn.sparkfun.com/assets/4/6/2/1/4/515f3293ce395f4a25000000.png)

When sizing out a current-limiting resistor, look for two characteristic values of the LED: the **typical forward voltage**, and the **maximum forward current**. The typical forward voltage is the voltage which is required to make an LED light up, and it varies (usually somewhere between 1.7V and 3.4V) depending upon the color of the LED. The maximum forward current is usually around 20mA for basic LEDs; continuous current through the LED should always be equal to or less than that current rating.

Once you\'ve gotten ahold of those two values, you can size up a current-limiting resistor with this equation:

[![Current limiting resistor = (Vs-Vf)/If](https://cdn.sparkfun.com/assets/8/3/4/4/e/515f354dce395fc424000000.png)](https://cdn.sparkfun.com/assets/8/3/4/4/e/515f354dce395fc424000000.png)

V~S~ is the source voltage \-- usually a battery or power supply voltage. V~F~ and I~F~ are the LED\'s forward voltage and the desired current that runs through it.

For example, assume you have a 9V battery to power an LED. If your LED is red, it might have a forward voltage around 1.8V. If you want to limit the current to 10mA, use a series resistor of about 720Ω.

[![Current limiting example equation R=(9-1.8)/.010](https://cdn.sparkfun.com/assets/3/2/b/a/2/515f369cce395f5425000000.png)](https://cdn.sparkfun.com/assets/3/2/b/a/2/515f369cce395f5425000000.png)

## Voltage Dividers

A [voltage divider](https://learn.sparkfun.com/tutorials/voltage-dividers) is a resistor circuit which turns a large voltage into a smaller one. Using just two resistors in series, an output voltage can be created that\'s a fraction of the input voltage.

Here\'s the voltage divider circuit:

[![Voltage divider circuit](https://cdn.sparkfun.com/assets/6/2/d/1/2/515c8377ce395fa71d000000.png)](https://cdn.sparkfun.com/assets/6/2/d/1/2/515c8377ce395fa71d000000.png)

Two resistors, R~1~ and R~2~, are connected in series and a voltage source (V~in~) is connected across them. The voltage from V~out~ to GND can be calculated as:

[![Voltage divider equation](https://cdn.sparkfun.com/assets/4/6/b/5/b/515c8377ce395f331d000000.png)](https://cdn.sparkfun.com/assets/4/6/b/5/b/515c8377ce395f331d000000.png)

For example, if R~1~ was 1.7kΩ and R~2~ was 3.3kΩ, a 5V input voltage could be turned into 3.3V at the V~out~ terminal.

Voltage dividers are very handy for reading resistive sensors, like [photocells](https://www.sparkfun.com/products/9088), [flex sensors](https://www.sparkfun.com/products/8606), and [force-sensitive resistors](https://www.sparkfun.com/products/9375). One half of the voltage divider is the sensor, and the part is a static resistor. The output voltage between the two components is connected to an [analog-to-digital converter](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) on a microcontroller (MCU) to read the sensor\'s value.

[![A photocell and resistor make a light sensor](https://cdn.sparkfun.com/assets/a/a/0/c/f/515c84d0ce395f7f1d000000.png)](https://cdn.sparkfun.com/assets/a/a/0/c/f/515c84d0ce395f7f1d000000.png)

*Here a resistor R~1~ and a photocell create a voltage divider to create a variable voltage output.*

## Pull-up Resistors

A [pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors) is used when you need to bias a microcontroller\'s input pin to a known state. One end of the resistor is connected to the MCU\'s pin, and the other end is connected to a high voltage (usually 5V or 3.3V).

Without a pull-up resistor, inputs on the MCU could be left *floating*. There\'s no guarantee that a floating pin is either high (5V) or low (0V).

Pull-up resistors are often used when interfacing with a button or [switch](https://learn.sparkfun.com/tutorials/switch-basics) input. The pull-up resistor can bias the input-pin when the switch is open. And it will protect the circuit from a [short](https://learn.sparkfun.com/tutorials/what-is-a-circuit/short-and-open-circuits) when the switch is closed.

[![A resistor pulling up a button input](https://cdn.sparkfun.com/assets/7/a/5/1/3/515c86cfce395fb61d000000.jpg)](https://cdn.sparkfun.com/assets/7/a/5/1/3/515c86cfce395fb61d000000.jpg)

In the circuit above, when the switch is open the MCU\'s input pin is connected through the resistor to 5V. When the switch closes, the input pin is connected directly to GND.

The value of a pull-up resistor doesn\'t usually need to be anything specific. But it should be high enough that not too much power is lost if 5V or so is applied across it. Usually values around 10kΩ work well.

------------------------------------------------------------------------

## Purchasing Resistors

Don\'t limit your flow of resistors. We\'ve got kits, packs, single pieces, and tools that you just can\'t *resist*.

### Our Recommendations:

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/6/14491-03.jpg)](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 10K Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-10k-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14491 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.50] ]

[![Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/1/7/14490-03.jpg)](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html)

### [Resistor 330 Ohm 1/4 Watt PTH - 20 pack (Thick Leads) ](https://www.sparkfun.com/resistor-330-ohm-1-4-watt-pth-20-pack-thick-leads.html) 

[ PRT-14490 ]

These are your run-of-the-mill 1/4 Watt, +/- 5% tolerance PTH resistors. Commonly used in breadboards and other prototyping a...

[ [\$1.25] ]

[![Power Resistor Kit - 10W (25 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/7/1/10353-01.jpg)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html)

### [Power Resistor Kit - 10W (25 pack)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html) 

[ KIT-13053 ]

Holy Wattage, Batman! This Power Resistor Kit comes with 5 each of 5 different 10 Watt resistor values including 1 Ohm, 2 Ohm...

[ [\$9.50] ]

[Click Here to View More Resistors in the Catalog](https://www.sparkfun.com/categories/324)

#### Tools:

[![Digital Multimeter - Basic](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/0/7/12966-01.jpg)](https://www.sparkfun.com/digital-multimeter-basic.html)

### [Digital Multimeter - Basic](https://www.sparkfun.com/digital-multimeter-basic.html) 

[ TOL-12966 ]

The digital multimeter (DMM) is an essential tool in every electronic enthusiasts arsenal. The SparkFun Digital Multimeter, h...

[ [\$21.50] ]

[![Resistor Lead Bending Tool](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/6/6/13114-01.jpg)](https://www.sparkfun.com/resistor-lead-bending-tool.html)

### [Resistor Lead Bending Tool](https://www.sparkfun.com/resistor-lead-bending-tool.html) 

[ TOL-13114 ]

This little piece of notched plastic is a Resistor Lead Bending Tool. Sometimes referred to as a \"forming\" tool, this little ...

[ [\$8.95] ]

[![SparkFun Resistor Chart Sticker](https://cdn.sparkfun.com/r/140-140/assets/parts/4/3/5/5/10108-01.jpg)](https://www.sparkfun.com/sparkfun-resistor-chart-sticker.html)

### [SparkFun Resistor Chart Sticker](https://www.sparkfun.com/sparkfun-resistor-chart-sticker.html) 

[ SWG-10108 ]

This handy resistor code sticker allows you to decipher the color coded bands on resistors and determine their value.

[ [\$1.95] ]

------------------------------------------------------------------------