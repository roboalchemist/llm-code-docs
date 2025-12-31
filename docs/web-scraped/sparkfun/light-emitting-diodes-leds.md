# Source: https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds

## Introduction

**LEDs are all around us:** In our phones, our cars and even our homes. Any time something electronic lights up, there\'s a good chance that an LED is behind it. They come in a huge variety of sizes, shapes, and colors, but no matter what they look like they have one thing in common: they\'re the bacon of electronics. They\'re widely purported to make any project better and they\'re often added to unlikely things (to everyone\'s delight).

[![LED = Bacon?](https://cdn.sparkfun.com/assets/b/7/6/0/4/51f1ba6bce395f3c20000003.jpg)](https://cdn.sparkfun.com/assets/b/7/6/0/4/51f1ba6bce395f3c20000003.jpg)

Unlike bacon, however, they\'re no good once you\'ve cooked them. This guide will help you avoid any accidental LED barbecues! First things first, though. What exactly *is* this LED thing everyone\'s talking about?

LEDs (that\'s \"ell-ee-dees\") are a particular type of [diode](https://learn.sparkfun.com/tutorials/diodes/introduction) that convert electrical energy into light. In fact, LED stands for \"Light Emitting Diode.\" (It does what it says on the tin!) And this is reflected in the similarity between the diode and LED schematic symbols:

[![Diode Schematic Symbol](https://cdn.sparkfun.com/assets/c/5/7/2/7/51f1c87ace395fea20000004.png)](https://cdn.sparkfun.com/assets/c/5/7/2/7/51f1c87ace395fea20000004.png)

In short, LEDs are like tiny lightbulbs. However, LEDs require a lot less power to light up by comparison. They\'re also more energy efficient, so they don\'t tend to get hot like conventional lightbulbs do (unless you\'re really pumping power into them). This makes them ideal for mobile devices and other low-power applications. Don\'t count them out of the high-power game, though. High-intensity LEDs have found their way into accent lighting, spotlights and even automotive headlights!

Are you getting the craving yet? The craving to put LEDs on everything? Good, stick with us and we\'ll show you how!

### Suggested Reading

Here are some other topics that will be discussed in this tutorial. If you are unfamiliar with any of them, please have a look at the respective tutorial before you go any further.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

[](https://learn.sparkfun.com/tutorials/diodes)

### Diodes 

A diode primer! Diode properties, types of diodes, and diode applications.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

[](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units)

### Metric Prefixes and SI Units 

This tutorial will explain how to use and convert between the standard metric prefixes.

### Suggested Viewing

## How to Use Them

So you\'ve come to the sensible conclusion that you need to put LEDs on everything. We thought you\'d come around.

[![Different LEDs GIF](https://cdn.sparkfun.com/assets/a/0/8/8/5/51f1d073ce395f7120000002.gif)](https://cdn.sparkfun.com/assets/a/0/8/8/5/51f1d073ce395f7120000002.gif)

Let\'s go over the rule book:

### 1) Polarity Matters

In electronics, [polarity](https://learn.sparkfun.com/tutorials/polarity) indicates whether a circuit component is symmetric or not. LEDs, being diodes, will only allow current to flow in one direction. And when there\'s no current-flow, there\'s no light. Luckily, this also means that you can\'t break an LED by plugging it in backwards. Rather, it just won\'t work.

[![alt text](https://cdn.sparkfun.com/r/300-300/assets/1/6/5/a/4/51f1d3a2ce395fd720000008.jpg)](https://cdn.sparkfun.com/assets/1/6/5/a/4/51f1d3a2ce395fd720000008.jpg)

The positive side of the LED is called the **\"anode\"** and is marked by having a longer \"lead,\" or leg. The other, negative side of the LED is called the **\"cathode.\"** Current flows from the anode to the cathode and never the opposite direction. A reversed LED can keep an entire circuit from operating properly by blocking current flow. So don\'t freak out if adding an LED breaks your circuit. Try flipping it around.

### 2) Moar Current Equals Moar Light

The brightness of an LED is directly dependent on how much current it draws. That means two things. The first being that super bright LEDs drain batteries more quickly, because the extra brightness comes from the extra power being used. The second is that you can control the brightness of an LED by controlling the amount of current through it. But, setting the mood isn\'t the only reason to cut back your current.

### 3) There is Such a Thing as Too Much Power

If you connect an LED directly to a current source it will try to dissipate as much power as it\'s allowed to draw, and, like the tragic heroes of olde, it will destroy itself. That\'s why it\'s important to limit the amount of current flowing across the LED.

For this, we employ resistors. Resistors limit the flow of electrons in the circuit and protect the LED from trying to draw too much current. Don\'t worry, it only takes a little basic math to determine the best resistor value to use. You can find out all about it in the example applications of our [resistor tutorial](https://learn.sparkfun.com/tutorials/resistors/example-applications)!

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

April 1, 2013

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

Don\'t let all of this math scare you, it\'s actually pretty hard to mess things up too badly. In the next section, we\'ll go over how to make an LED circuit without getting your calculator.

## LEDs Without Math

Before we talk about how to read a datasheet, let\'s hook up some LEDs. After all, this is an LED tutorial, not a *reading* tutorial.

It\'s also not a math tutorial, so we\'ll give you a few rules of thumb for getting LEDs up and running. As you\'ve probably put together from the info in the last section, you\'ll need a battery, a resistor, and an LED. We\'re using a battery as our power source, because they\'re easy to find and they can\'t supply a dangerous amount of current.

The basic template for an LED circuit is pretty simple, just connect your battery, resistor and LED in series. Like this:\

[![LED Circuit with Current Limiting Resistor](https://cdn.sparkfun.com/assets/6/e/8/3/c/51f93d85757b7f2049270817.png)](https://cdn.sparkfun.com/assets/6/e/8/3/c/51f93d85757b7f2049270817.png)

\

### 330 Ohm Resistor

A good resistor value for most LEDs is **330 Ohms** ([ orange ] - [ orange ] - [ brown ]). You can use the information from the last section to help you determine the exact value you need, but this is LEDs *without* math\... So, start by popping a 330 Ohm resistor into the above circuit and see what happens.

[![330 Ohm Resistor](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14490-02_330OhmResistor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14490-02_330OhmResistor.jpg)

### Trial and Error

The interesting thing about resistors is that they\'ll dissipate extra power as heat, so if you have a resistor that\'s getting warm, you probably need to go with a smaller resistance. If your resistor is too small, however, you run the risk of burning out the LED! Given that you have a handful of LEDs and resistors to play with, here\'s a flow chart to help you design your LED circuit by trial and error:\

[![Flow Chart Choosing a resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/g6109.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/g6109.png)

\

### Throwies with a Coin Cell Battery

Another way to light up an LED is to just connect it to a coin cell battery! Since the coin cell can\'t source enough current to damage the LED, you can connect them directly together! Just push a [CR2032 coin cell](https://www.sparkfun.com/products/338) between the leads of the LED. The long leg of the LED should be touching the side of the battery marked with a \"+\". Now you can wrap some tape around the whole thing, add a magnet, and stick it to stuff! Yay for [throwies](http://www.instructables.com/id/LED-Throwies/)!

[![LED + Coin Cell Battery = Throwie](https://cdn.sparkfun.com/r/300-300/assets/2/2/9/3/8/51f94eed757b7f573d96660d.png)](https://cdn.sparkfun.com/assets/2/2/9/3/8/51f94eed757b7f573d96660d.png)

\

Of course, if you\'re not getting great results with the trial and error approach, you can always get out your calculator and math it up. Don\'t worry, it\'s not hard to calculate the best resistor value for your circuit. But before you can figure out the optimal resistor value, you\'ll need to find the optimal current for your LED. For that we\'ll need to report to the datasheet\...

## Get the Details

Don\'t go plugging any strange LEDs into your circuits, that\'s just not healthy. Get to know them first. And how better than to read the datasheet.

As an example we\'ll peruse the [datasheet](http://www.sparkfun.com/datasheets/Components/LED/COM-09590-YSL-R531R3D-D2.pdf) for our [Basic Red 5mm LED](https://www.sparkfun.com/products/9590).

### LED Current

Starting at the top and making our way down, the first thing we encounter is this charming table:

[![alt text](https://cdn.sparkfun.com/assets/8/a/5/0/2/51f20420ce395fe058000000.JPG)](https://cdn.sparkfun.com/assets/8/a/5/0/2/51f20420ce395fe058000000.JPG)

Ah, yes, but what does it all mean?

The first row in the table indicates how much current your LED will be able to handle continuously. In this case, you can give it 20mA or less, and it will shine its brightest at 20mA. The second row tells us what the maximum peak current should be for short bursts. This LED can handle short bumps to 30mA, but you don\'t want to sustain that current for too long. This datasheet is even helpful enough to suggest a stable current range (in the third row from the top) of 16-18mA. That\'s a good target number to help you make the resistor calculations we talked about.

The following few rows are of less importance for the purposes of this tutorial. The reverse voltage is a diode property that you shouldn\'t have to worry about in most cases. The power dissipation is the amount of power in milliWatts that the LED can use before taking damage. This should work itself out as long as you keep the LED within its suggested voltage and current ratings.

### LED Voltage

Let\'s see what other kinds of tables they\'ve put in here\... Ah!

[![alt text](https://cdn.sparkfun.com/assets/4/4/9/0/9/51f6d886ce395f8c67000006.jpg)](https://cdn.sparkfun.com/assets/4/4/9/0/9/51f6d886ce395f8c67000006.jpg)

This is a useful little table! The first row tells us what the **forward voltage** drop across the LED will be. Forward voltage is a term that will come up a lot when working with LEDs. This number will help you decide how much voltage your circuit will need to supply to the LED. If you have more than one LED connected to a single power source, these numbers are really important because the forward voltage of all of the LEDs added together can\'t exceed the supply voltage. We\'ll talk about this more in-depth later in the [delving deeper](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds/delving-deeper) section of this tutorial.

### LED Wavelength

The second row on this table tells us the wavelength of the light. Wavelength is basically a very precise way of explaining what color the light is. There may be some variation in this number so the table gives us a minimum and a maximum. In this case it\'s 620 to 625nm, which is just at the lower red end of the spectrum (620 to 750nm). Again, we\'ll go over wavelength in more detail in the [delving deeper](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds/delving-deeper) section.

### LED Brightness

The last row (labeled \"Luminous Intensity\") is a measure of how bright the LED can get. The unit mcd, or **millicandela**, is a standard unit for measuring the intensity of a light source. This LED has an maximum intensity of 200 mcd, which means it\'s just bright enough to get your attention but not quite flashlight bright. At 200 mcd, this LED would make a good indicator.

### Viewing Angle

[![alt text](https://cdn.sparkfun.com/assets/0/f/0/4/a/51f2041fce395f9356000000.JPG)](https://cdn.sparkfun.com/assets/0/f/0/4/a/51f2041fce395f9356000000.JPG)

Next, we\'ve got this fan-shaped graph that represents the viewing angle of the LED. Different styles of LEDs will incorporate lenses and reflectors to either concentrate most of the light in one place or spread it as widely as possible. Some LEDs are like floodlights that pump out photons in every direction; Others are so directional that you can\'t tell they\'re on unless you\'re looking straight at them. To read the graph, imagine the LED is standing upright underneath it. The \"spokes\" on the graph represent the viewing angle. The circular lines represent the intensity by percent of maximum intensity. This LED has a pretty tight viewing angle. You can see that looking straight down at the LED is when it\'s at its brightest, because at 0 degrees the blue lines intersect with the outermost circle. To get the 50% viewing angle, the angle at which the light is half as intense, follow the 50% circle around the graph until it intersects the blue line, then follow the nearest spoke out to read the angle. For this LED, the 50% viewing angle is about 20 degrees.

### Dimensions

[![alt text](https://cdn.sparkfun.com/assets/3/2/5/b/9/51f2041fce395f9856000000.JPG)](https://cdn.sparkfun.com/assets/3/2/5/b/9/51f2041fce395f9856000000.JPG)

Finally, the mechanical drawing. This picture contains all of the measurements you\'ll need to actually mount the LED in an enclosure! Notice that, like most LEDs, this one has a small flange at the bottom. That comes in handy when you want to mount it in a panel. Simply drill a hole the perfect size for the body of the LED, and the flange will keep it from falling through!

Now that you know how to decipher the datasheet, let\'s see what kind of fancy LEDs you might encounter in the wild\...

## Types of LEDs

Congratulations, you know the basics! Maybe you\'ve even gotten your hands on a few LEDs and started lighting stuff up, that\'s awesome! How would you like to step up your blinky game? Let\'s talk about makin\' it fancy outside of your standard LED.

[![Super Bright LED Zoomed In](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/SuperBrightLED_ZoomedIn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/SuperBrightLED_ZoomedIn.jpg)

*Close Up of Super Bright 5mm LED Close Up*

### Types of LEDs

Here\'s the cast of other characters.

### RGB LEDs

[RGB (Red-Green-Blue) LEDs](https://www.sparkfun.com/search/results?term=rgb+led) are actually three LEDs in one! But that doesn\'t mean it can only make three colors. Because red, green, and blue are the additive primary colors, you can control the intensity of each to create every color of the rainbow. Most RGB LEDs have four pins: one for each color, and a common pin. On some, the common pin [is the anode](https://www.sparkfun.com/products/10820), and on others, [it\'s the cathode](https://www.sparkfun.com/products/105).

[![RGB Common Clear Cathode](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/00105-03-LCommonClearCathode.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/00105-03-LCommonClearCathode.jpg)

*RGB Common Clear Cathode LED*

### LEDs w/ Integrated Circuits

#### Cycling

Some LEDs are smarter than others. Take the [cycling LED](https://www.sparkfun.com/search/results?term=rgb+cycling), for example. Inside these LEDs, there\'s actually an [integrated circuit](https://learn.sparkfun.com/tutorials/integrated-circuits) that allows the LED to blink without any outside controller. Here\'s a closeup of the IC (the big, black square chip on the tip of the anvil) controlling the colors.

[![5mm Slow Cycling LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/SlowCyclingLED_ZoomedIn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/SlowCyclingLED_ZoomedIn.jpg)

*5mm Slow Cycling LED Close Up*

Simply power it up and watch it go! These are great for projects where you want a little bit more action but don\'t have room for control circuitry. There are even RGB flashing LEDs that cycle through thousands of colors!

#### Addressable LEDs

Other types of LEDs can be controlled individually. There are different chipsets ([WS2812](https://www.sparkfun.com/search/results?term=ws2812), [APA102](https://www.sparkfun.com/search/results?term=apa102), [UCS1903](https://www.sparkfun.com/products/14555), to name a few) used to control an individual LED that is chained together. Below is a closeup of a WS2812. The bigger square IC on the right controls the colors individually.

[![WS2812 Clear Addressable LED Zoomed In](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/AddressableLEDWS2812_ZoomedIn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/AddressableLEDWS2812_ZoomedIn.jpg)

*Addressable WS2812 PTH Close Up*

#### [][Built-In Resistor](#LED-built-in-resistor)

What is this magic? An LED with a built-in resistor? That\'s right. There are also LEDs that include a small, current limiting resistor. If you look closely at the image below, there is a small, black square IC on the post to limit the current on these types of LEDs.

[![LED with Built in Resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/1/SuperBrightLEDwithBuiltInResistor_ZoomedIn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/SuperBrightLEDwithBuiltInResistor_ZoomedIn.jpg)

*LED with Built-In Resistor Close Up*

So plug the LED with built-in resistor to your power source and light it up! We have tested these types of LEDs at 3.3V, 5V, and 9V.

[![LED powered with built in resistor](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14563-LED_-_Green_with_Resistor_5mm__25_pack_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14563-LED_-_Green_with_Resistor_5mm__25_pack_.jpg)

*Super Bright Green LED with Built in Resistor Powered*

**Note:** The datasheet for the LEDs with built-in resistor indicates that the recommended forward voltage is around 5V. Testing one out at 5V, it pulls about 18mA. Stress testing with a 9V battery, it pulls about 30mA. This is probably at the higher end of the input voltage. Using a higher voltage can reduce the life of the LED. At about 16V, the LED blew out under our stress tests.

### Surface Mount (SMD) Packages

[SMD LEDs](https://www.sparkfun.com/products/10866) aren\'t so much a specific kind of LED but a package type. As electronics get smaller and smaller, manufacturers have figured out how to cram more components in a smaller space. SMD (Surface Mount Device) parts are tiny versions of their standard counterparts. Here\'s a closeup of a WS2812B addressable LED packaged into a small 5050 package.

[![WS2812B Closeup](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/WS2812B_SMD_Closeup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/WS2812B_SMD_Closeup.jpg)

*Addressable WS2812B Close Up*

SMD LEDs come in several sizes, from fairly large to smaller than a grain of rice! Because they\'re so small, and have pads instead of legs, they\'re not as easy to work with, but if you\'re tight on space, they might be just what the doctor ordered.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/13667-02_SMD-WS2812B_5050.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/13667-02_SMD-WS2812B_5050.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14608-SMD_LED_-_RGB_APA102-2020.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14608-SMD_LED_-_RGB_APA102-2020.jpg)
  *WS2812B-5050 Package*                                                                                                                                                        *APA102-2020 Package*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SMD LEDs also make it easier and quicker for pick and place machines to **populate a lot** of LEDs onto PCBs and strips. You would probably not to manually solder all of those components by hand.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/13304-03_FlexibleLEDMatrix_8x32_WS2812B.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/13304-03_FlexibleLEDMatrix_8x32_WS2812B.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14016-action_Addressable_LED_Strip_APA102.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/14016-action_Addressable_LED_Strip_APA102.jpg)
  *Close Up of 8x32 Addressable (WS2812-5050) LED Matrix*                                                                                                                                                   *5M Addressable (APA102-5050) LED Strip Powered*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### High Power

[High-Power LEDs](https://www.sparkfun.com/products/8718) from manufacturers like Luxeon and CREE, are crazy bright. These are brighter than the super brights! Generally, an LED is considered High-Power if it can dissipate 1 Watt or more of power. These are the fancy LEDs that you find in really nice flashlights. Arrays of them can even be built for spotlights and automobile headlights. Because there\'s so much power being pumped through the LED, these often require heatsinks. A [heatsink](https://www.sparkfun.com/tutorials/314) is basically a chunk of heat conducting metal with lots of surface area whose job is to transfer as much waste heat into the surrounding air as possible. There can be some heat dissipation built into the design of some breakout board such as the one shown below.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08718-04b_HighPowerLED_Red.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08718-04b_HighPowerLED_Red.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08718-03b_HighPowerLED_Aluminum_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08718-03b_HighPowerLED_Aluminum_Back.jpg)
  *High Power RGB LED*                                                                                                                                                            *Aluminum Back for some Heat Dissipation*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

High-Power LEDs can generate so much waste heat that they\'ll damage themselves without proper cooling. Don\'t let the term \"waste heat\" fool you, though, these devices are still incredibly efficient compared to conventional bulbs. To control, you could use a [constant current LED driver](https://www.sparkfun.com/products/13716).

### Special LEDs

There are even LEDs that emit light outside of the normal visible spectrum. You probably use [infrared LEDs](https://www.sparkfun.com/products/9469) every day, for instance. They\'re used in things like TV remotes to send small pieces of information in the form of invisible light! These may look like standard LEDs so it will be hard to distinguish from normal LEDs.

[![Infrared LED 850nm](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/09469-1_Infrared_LED_850nm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/09469-1_Infrared_LED_850nm.jpg)

*IR LED*

On the opposite end of the spectrum you can also get [ultraviolet LEDs](https://www.sparkfun.com/products/8662). Ultraviolet LEDs will make certain materials fluoresce, just like a blacklight! They\'re also used for disinfecting surfaces, because many bacteria are sensitive to UV radiation. They may also be used counterfeit detection (bills, credit cards, documents, etc), sun burns, the list goes on. Please wear eye protection when using these LEDs.

[![UV LED](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08662-02-L_Ultraviolet_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/08662-02-L_Ultraviolet_LED.jpg)

*UV LED Inspecting a US Bill*

### More LEDs

With fancy LEDs like these at your disposal, there\'s no excuse for leaving anything un-illuminated. However, if your thirst for LED knowledge hasn\'t been slaked, then read on, and we\'ll get into the nitty-gritty on LEDs, color, and luminous intensity!

## Delving Deeper

So you\'ve graduated from LEDs 101 and you want more? Oh, don\'t worry, we\'ve got more. Let\'s start with the science behind what makes LEDs tick\... err\... blink. We\'ve already mentioned that LEDs are a special kind of diode, but let\'s delve a little deeper into exactly what that means:

What we call an LED is really the LED and the packaging together, but the LED itself is actually tiny! It\'s a chip of semiconductor material that\'s doped with impurities which creates a [boundary](https://en.wikipedia.org/wiki/P-n_junction) for charge carriers. When current flows into the semi-conductor, it jumps from one side of this boundary to the other, releasing energy in the process. In most diodes that energy leaves as heat, but in LEDs that energy is dissipated as light!

The wavelength of light, and therefore the color, depends on the type of semiconductor material used to make the diode. That\'s because the energy band structure of semiconductors differs between materials, so photons are emitted with differing frequencies. Here\'s a table of common LED semiconductors by frequency:

[![LED Color Chart](https://cdn.sparkfun.com/r/600-600/assets/5/b/5/b/a/51f95fcd757b7f6f3dcb351f.jpg)](https://cdn.sparkfun.com/assets/5/b/5/b/a/51f95fcd757b7f6f3dcb351f.jpg)

*Truncated table of semiconductor materials by color. The full table is available on the [Wikipedia entry for \"LED\"](https://en.wikipedia.org/wiki/LED)*

While the wavelength of the light depends on the band gap of the semiconductor, the intensity depends on the amount of power being pushed through the diode. We talked about luminous intensity a little bit in a previous section, but there\'s more to it than just putting a number on how bright something looks.

The unit for measuring luminous intensity is called the candela, although when you\'re talking about the intensity of a single LED you\'re usually in the millicandela range. The interesting thing about this unit is that it isn\'t really a measure of the amount of light energy, but an actual measure of \"brightness\". This is achieved by taking the power emitted in a particular direction and weighting that number by the luminosity function of the light. The human eye is more sensitive to some wavelengths of light than others, and the luminosity function is a standardized model that accounts for that sensitivity.

The luminous intesity of LEDs can range from the tens to the tens-of-thousands of millicandela. The power light on your TV is probably about 100 mcd, whereas a good flashlight might be 20,000 mcd. Looking straight into anything brighter than a few thousand millicandela can be painful; don\'t try it.[]

### Forward Voltage Drop

Oh, I also promised that we\'d talk about the concept of Forward Voltage Drop. Remember when we were looking at the datasheet and I mentioned that the Forward Voltage of all of your LEDs added together can\'t exceed your system voltage? This is because every component in your circuit has to *share* the voltage, and the amount of voltage that every part uses together will always equal the amount that\'s available. This is called [Kirchhoff\'s Voltage Law](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws). So if you have a 5V power supply and each of your LEDs have a forward voltage drop of 2.4V then you can\'t power more than two at a time.

Kirchhoff\'s Laws also come in handy when you want to approximate the voltage across a given part based on the Forward Voltage of other parts. For instance, in the example I just gave there\'s a 5V supply and 2 LEDs with a 2.4V Forward Voltage Drop each. Of course we would want to include a current limiting resistor, right? How would you find out the voltage across that resistor? It\'s easy:

> 5 (System Voltage) = 2.4 (LED 1) + 2.4 (LED 2) + Resistor
>
> 5 = 4.8 + Resistor
>
> Resistor = 5 - 4.8
>
> Resistor = 0.2

So there is .2V across the resistor! This is a simplified example and it isn\'t always this easy, but hopefully this gives you an idea of why Forward Voltage Drop is important. Using the voltage number you derive from Kirchhoff\'s Laws you can also do things like determine the current across a component using Ohm\'s Law. In short, **you want your system voltage equal to the expected forward voltage of your combined circuit components.**

### Calculating Current Limiting Resistors

If you need to calculate the exact current limiting resistor value in series with an LED, check out one of the [example applications in the resistors tutorial](https://learn.sparkfun.com/tutorials/resistors#current-limiting) for more information.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Equation to Calculate Current Limiting Resistor](https://cdn.sparkfun.com/r/600-600/assets/8/3/4/4/e/515f354dce395fc424000000.png)](https://learn.sparkfun.com/tutorials/resistors#current-limiting)
  [Equation Used to Calculate a Current Limiting Resistor](https://learn.sparkfun.com/tutorials/resistors#current-limiting)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------