# Source: https://learn.sparkfun.com/tutorials/battery-technologies

## Battery Options

There are a multitude of different battery technologies available. There are some really great resources available for the nitty gritty details behind [battery chemistries](http://batteryuniversity.com/learn/article/whats_the_best_battery). Wikipedia is especially good and [all encompassing](http://en.wikipedia.org/wiki/List_of_battery_types). This tutorial focuses on the most often used batteries for embedded systems and DIY electronics.

[![Pile of different battery types](//cdn.sparkfun.com/r/600-600/assets/a/6/5/e/f/5114447cce395f697e000009.jpg)](//cdn.sparkfun.com/assets/a/6/5/e/f/5114447cce395f697e000009.jpg)

### Suggested Reading

There are some concepts and bits of knowledge you may want to know before reading this tutorial:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

[](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Alternating Current (AC) vs. Direct Current (DC) 

Learn the differences between AC and DC, the history, different ways to generate AC and DC, and examples of applications.

## Looking to explore different batteries?

We\'ve got you covered!

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 18650 Cell (2600mAh)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/5/12895-01_1.jpg)](https://www.sparkfun.com/lithium-ion-battery-18650-cell-2600mah.html)

### [Lithium Ion Battery - 18650 Cell (2600mAh)](https://www.sparkfun.com/lithium-ion-battery-18650-cell-2600mah.html) 

[ PRT-12895 ]

No, these aren\'t some sort of weird, AA battery, this is actually a 18650 Lithium Ion Cell. These round high capacity cells h...

[ [\$9.83] ]

[![Coin Cell Battery - 20mm (CR2032)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/338-Coin-Cell-Battery-20mm-Feature.jpg)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html)

### [Coin Cell Battery - 20mm (CR2032)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html) 

[ PRT-00338 ]

CR2032 Lithium metal 3V 250mAh button cell battery. Great for powering low power processors or blink an LED for weeks at a ti...

[ [\$2.25] ]

[![9V Alkaline Battery](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/6/2/10218-01.jpg)](https://www.sparkfun.com/9v-alkaline-battery.html)

### [9V Alkaline Battery](https://www.sparkfun.com/9v-alkaline-battery.html) 

[ PRT-10218 ]

These are your standard 9 Volt alkaline batteries from Rayovac. Don\'t even think about trying to recharge these. Use them wit...

[ [\$2.40] ]

[See all batteries](https://www.sparkfun.com/categories/54)

------------------------------------------------------------------------

## Terminology

Here are some terms often used when talking about batteries.

**Capacity** - Batteries have different ratings for the amount of power a given battery can store. When a battery is fully charged, the capacity is the amount of power it contains. Batteries of the same type will often be rated by the amount of current they can output over time. For example, there are [1000mAh](https://www.sparkfun.com/products/339) (milli-Amp Hour) and [2000mAh](https://www.sparkfun.com/products/8483) batteries.

**Nominal Cell Voltage** - The average voltage a cell outputs when charged. The nominal voltage of a battery depends on the chemical reaction behind it. A lead-acid car battery will output 12V. A lithium coin cell battery will output 3V.

The key word here is \"nominal\", the actual measured voltage on a battery will decrease as it discharges. A fully charged LiPo battery will produce about 4.23V, while when discharged its voltage may be closer to 2.7V.

**Shape** - Batteries come in many sizes and shapes. The term 'AA' references a specific shape and style of a cell. There are a [large variety](http://en.wikipedia.org/wiki/List_of_battery_sizes).

**Primary vs. Secondary** - Primary batteries are synonymous with **disposable**. Once fully-drained, primary cells can\'t be recharged (reliably/safely). Secondary batteries are better known as **rechargeable**. These require another power source to fully charge back up, but they can fully charge/discharge many times over their life. In general primary batteries have a lower discharge rate, so they\'ll last longer, but they can be less economical than rechargeable batteries.

  Battery Shape                  Chemistry                 Nominal Voltage   Rechargeable?
  ------------------------------ ------------------------- ----------------- ---------------
  AA, AAA, C, and D              Alkaline or Zinc-carbon   1.5V              No
  9V                             Alkaline or Zinc-carbon   9V                No
  Coin Cell                      Lithium                   3V                No
  Silver Flat Pack               Lithium Polymer (LiPo)    3.7V              Yes
  AA, AAA, C, D (Rechargeable)   NiMH or NiCd              1.2V              Yes
  Car Battery                    Six-cell lead acid        12.6V             Yes

  : **Common batteries, their chemistry, and their nominal voltage**

**Energy Density** - Combining capacity with shape and size of a battery, the energy density of a battery can be calculated. Different technologies allow different densities. For example, lithium batteries typically pack more juice into a given volume than alkaline or coin cell batteries.

**Internal Discharge Rate** - Have you ever tried to start a car that has been sitting for 6 months? Batteries discharge when sitting on the shelf or when unused. The rate at which the battery discharges itself over time is called internal discharge rate.

**Safety** - Because batteries store power, they are basically very tiny explosives. To prevent harm, batteries are designed to be as safe as possible. Most batteries technologies are designed to discharge safely in the event of misuse. If you hook up an alkaline battery incorrectly, it may get hot to the touch but should not catch fire. Most Lithium Polymer batteries have safety circuits built-in to prevent damage to battery and prevent it from unsafe usage.

For a full list of terms and technical overview Wikipedia is an \[excellent resource\](http://en.wikipedia.org/wiki/Battery\_(electricity)).

## Lithium Polymer

Lithium Polymer (often abbreviated LiPo) batteries are very useful for embedded electronics. They offer the highest density readily available on the market. Because cell phones predominantly use this battery type, they are easy to find for reasonable prices. They **do** require special charging, so be sure to use the right charger for the job. SparkFun carries a variety of 3.7V Lithium Polymer batteries - many of which are listed below. The capacity of the battery you choose will depend on the intended run time of your project, size constraints, and other factors.

[![Lithium Ion Battery - 110mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/0/13853-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-110mah.html)

### [Lithium Ion Battery - 110mAh](https://www.sparkfun.com/lithium-ion-battery-110mah.html) 

[ PRT-13853 ]

This is a very small, extremely light weight battery based on Lithium Ion chemistry. This is the highest energy density curre...

[ [\$7.53] ]

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 1500mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/8/8/0/PRT-26059-Lithium-Ion-Battery-Feature.jpg)](https://www.sparkfun.com/lithium-ion-battery-1500mah-iec62133-certified.html)

### [Lithium Ion Battery - 1500mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1500mah-iec62133-certified.html) 

[ PRT-26059 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. With output at a nominal 3.7V at 1500 mAh and is IEC62...

[ [\$15.95] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Polymer Lithium Ion Battery - 40mAh (JST-PH)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/9/13857-01.jpg)](https://www.sparkfun.com/polymer-lithium-ion-battery-40mah.html)

### [Polymer Lithium Ion Battery - 40mAh (JST-PH)](https://www.sparkfun.com/polymer-lithium-ion-battery-40mah.html) 

[ PRT-13852 ]

This is an extremely tiny and light weight battery based on the new Polymer Lithium Ion chemistry.

[ [\$7.14] ]

### Nominal Voltage

An individual LiPo cell has a **nominal voltage of 3.7V**. When fully charged you will see nearly 4.3V on the cell but it will quickly drop to 3.7V under normal use. When depleted, the cell will be around 3V. This means your project will need to handle various voltages if you are running directly from a cell. If you need 5V you will need to combine two LiPos in series to create a 7.4V pack and regulate down to 5V.

[![LiPo discharge curve](//cdn.sparkfun.com/r/600-600/assets/6/7/4/7/9/5112a224ce395fb479000003.png)](//cdn.sparkfun.com/assets/6/7/4/7/9/5112a224ce395fb479000003.png)

*Image from [ProTalk.net](http://prototalk.net/forums/showthread.php?t=22)*

### Connectors

[![JST connector on a LiPo](//cdn.sparkfun.com/r/400-400/assets/8/c/0/5/5/5112a390ce395fb079000000.jpg)](//cdn.sparkfun.com/assets/8/c/0/5/5/5112a390ce395fb079000000.jpg)

In the small electronics world, most LiPo batteries come terminated with various 2-pin connectors. At SparkFun, we use the **JST connector**. This prevents the battery from being plugged in wrong. The connector is a friction fit so it's common to use pliers to [gently remove the battery](//cdn.sparkfun.com/assets/f/e/2/a/b/5114447cce395f7a7a000005.jpg).

### Charging and Discharging

[![LiPo connected to charger](//cdn.sparkfun.com/r/600-600/assets/5/7/c/d/a/5114447cce395fa87d00000d.jpg)](//cdn.sparkfun.com/assets/5/7/c/d/a/5114447cce395fa87d00000d.jpg)

There are many low-cost chargers created to charge LiPo batteries. They commonly use USB to charge the battery. **Do not** attempt to charge a LiPos without a charger. A LiPo battery can be harmed by overcharging, so use a specifically designed LiPo charger like the ones here:

[![SparkFun LiPo Charger/Booster - 5V/1A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/3/2/14411-01.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html)

### [SparkFun LiPo Charger/Booster - 5V/1A](https://www.sparkfun.com/sparkfun-lipo-charger-booster-5v-1a.html) 

[ PRT-14411 ]

The SparkFun 5V/1A LiPo Charger/Booster is a no-nonsense circuit for generating one amp from a Lithium Polymer battery at 5V....

[ [\$18.50] ]

[![SparkFun LiPo Charger Basic - Micro-B](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/6/1/10217-02a.jpg)](https://www.sparkfun.com/sparkfun-lipo-charger-basic-micro-usb.html)

### [SparkFun LiPo Charger Basic - Micro-B](https://www.sparkfun.com/sparkfun-lipo-charger-basic-micro-usb.html) 

[ PRT-10217 ]

If you need to charge LiPo batteries, this simple charger will do just that, and do it fast! The SparkFun LiPo Charger Basic ...

[ [\$10.50] ]

[![SparkFun Adjustable LiPo Charger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/9/1/14380b-01.jpg)](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html)

### [SparkFun Adjustable LiPo Charger](https://www.sparkfun.com/sparkfun-adjustable-lipo-charger.html) 

[ PRT-14380 ]

The SparkFun Adjustable LiPo Charger is a single-cell lithium polymer (LiPo) and lithium ion battery charger. Because it's ...

[ [\$13.95] ]

[![SparkFun USB LiPoly Charger - Single Cell](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/5/6/12711-01.jpg)](https://www.sparkfun.com/sparkfun-usb-lipoly-charger-single-cell.html)

### [SparkFun USB LiPoly Charger - Single Cell](https://www.sparkfun.com/sparkfun-usb-lipoly-charger-single-cell.html) 

[ PRT-12711 ]

If you need to charge LiPo batteries, this simple charger will do just that, and do it fast! The SparkFun USB LiPo Charger is...

[ [\$18.50] ]

Before charging a Lithium Ion battery, make sure you are aware of your battery\'s capacity and the charge current supplied by the charger. More information can be found in the following tutorial: [Setting the Charge Current](https://learn.sparkfun.com/tutorials/lipo-usb-charger-hookup-guide#setting-the-charge-current).

[![Setting Charge Rates for LiPo Battery](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/7/Adjustable_Lipo_Charger_Hookup_Guide-02.jpg)](https://learn.sparkfun.com/tutorials/adjustable-lipo-charger-hookup-guide#hardware-assembly)

*Image from the [Adjustable LiPo Charger Hookup Guide](https://learn.sparkfun.com/tutorials/adjustable-lipo-charger-hookup-guide#hardware-assembly)*

LiPo batteries can also be harmed by being discharged too far. To protect against this, almost all LiPo batteries have a small safety circuit built into the top of the cell that will shut off the battery if the voltage drops below a certain threshold (usually **3V**). The protection circuit board is usually under the yellow Kapton tape where the wires are connected.

[![LiPo Battery Protection Circuit](https://cdn.sparkfun.com//assets/parts/1/1/4/0/1/13813-05.jpg)](https://cdn.sparkfun.com//assets/parts/1/1/4/0/1/13813-05.jpg)

*LiPo Battery Protection Circuit under the Yellow Kapton Tape*

LiPo batteries have a **very low internal discharge rate**. This makes them a good candidate for projects that have low power requirements and need to run for many days or months.

**Respect the energy density:** These batteries pack a punch and can source multiple amps continuously. The short-circuit protection will shut off the battery when a short is detected but when using these batteries with projects use common sense.

**Note:** Certain datasheets provided by the manufacturer have units as C~5~A for the rated capacity. This is a standard that is used when measuring LiPo batteries. For example, a 850mAh LiPo battery with a rated capacity of 0.2C~5~A indicates that the capacity (C) was obtained by multiplying the capacity 850mA with 0.2 over a period of 5 hours. This current value was used with a load until the LiPo battery reached a minimum voltage during that period of time.

We recommend LiPo for nearly every portable application. They are fairly robust and when used safely provide a great power source.

### Other Types of Lithium Ion Batteries

#### Round, High Capacity Lithium Ion Batteries

[![Round High Capacity LiPo Battery](https://cdn.sparkfun.com/r/300-300/assets/parts/9/7/8/5/12895-02_1.jpg)](https://cdn.sparkfun.com/assets/parts/9/7/8/5/12895-02_1.jpg)

These batteries have been mainly used in flashlight type applications but are easy to use and install and have a lot of juice.

- **Nominal Voltage** - These batteries also carry a nominal voltage of **3.7V** but unlike the flat LiPo batteries, these round cell batteries do **NOT** have a protection circuit built in. Special care must be taken when charging and discharging these batteries so that they do not become damaged. More information on protection circuits can be found [here](https://www.digikey.com/en/maker/blogs/lithium-ion-cell-protection).

- **Connectors** - These batteries can be easily integrated into projects with specific battery holders:

  ::::::::::::::::::: tile-wrap
  ::::::: 
  ::: actions-wrap
  [![Battery Holder - 1x18650 (wire leads)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/8/0/0/12899-01.jpg)](https://www.sparkfun.com/battery-holder-1x18650-wire-leads.html)
  :::

  ::: main
  ### [Battery Holder - 1x18650 (wire leads)](https://www.sparkfun.com/battery-holder-1x18650-wire-leads.html) 

  [ PRT-12899 ]
  This is an incredibly simple one cell 18650 Battery Holder. When someone thinks of 18650 Cells they tend to think of flashlig...
  :::

  :::: 
  ::: prices
  [ [\$1.25] ]
  :::
  ::::
  :::::::

  ::::::: 
  ::: actions-wrap
  [![Battery Holder - 18650 (PTH)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/6/5/13113-03.jpg)](https://www.sparkfun.com/battery-holder-18650-pth.html)
  :::

  ::: main
  ### [Battery Holder - 18650 (PTH)](https://www.sparkfun.com/battery-holder-18650-pth.html) 

  [ PRT-13113 ]
  This is a PCB mount clip to hold a 18650 Lithium Ion Cell battery. Each battery holder is sold in single units, you\'ll need t...
  :::

  :::: 
  ::: prices
  [ [\$0.95] ]
  :::
  ::::
  :::::::

  ::::: 
  ::: actions-wrap
  [ ![Battery Holder - 1x18650 (board mount)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/5/6/14963_-_534-1044.jpg) ]
  :::

  ::: main
  ### Battery Holder - 1x18650 (board mount) 

  [ PRT-14963 ]
  Keystone Electronics 18650 Battery Holders are ideal for 3.7V, high energy, lower weight mobile electronics, industrial, and ...
  :::

  **Retired**
  :::::

  ::::: 
  ::: actions-wrap
  [ ![Battery Holder - 2x18650 (board mount)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/5/7/14964_-_534-1047.jpg) ]
  :::

  ::: main
  ### Battery Holder - 2x18650 (board mount) 

  [ PRT-14964 ]
  Keystone Electronics 18650 Battery Holders are ideal for 3.7V, high energy, lower weight mobile electronics, industrial, and ...
  :::

  **Retired**
  :::::
  :::::::::::::::::::

  ::: clearfix
  :::

- **Charging and Discharging** - Since there is no protection circuit on these batteries, the user must account for the possibility of over or under charging such that the battery isn\'t damaged. We recommend a universal charger like this one:

  :::::::: 
  ::::::: 
  ::: actions-wrap
  [![Tenergy T4s Intelligent Universal Charger - 4-Bay](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/1/14457-02.jpg)](https://www.sparkfun.com/tenergy-t4s-intelligent-universal-charger-4-bay.html)
  :::

  ::: main
  ### [Tenergy T4s Intelligent Universal Charger - 4-Bay](https://www.sparkfun.com/tenergy-t4s-intelligent-universal-charger-4-bay.html) 

  [ TOL-14457 ]
  The 4-Bay T4s Intelligent Universal Charger from Tenergy is an automatic smart charger compatible with almost all types of re...
  :::

  :::: 
  ::: prices
  [ [\$58.95] ]
  :::
  ::::
  :::::::
  ::::::::

#### High Discharge Lithium Ion Batteries

[![High Discharge Lithium Ion Battery](https://cdn.sparkfun.com/r/300-300/assets/parts/8/2/5/2/11856-01.jpg)](https://cdn.sparkfun.com/assets/parts/8/2/5/2/11856-01.jpg)

High discharge lithium ion batteries are a great way to power any R/C, robotic, or portable project that needs a small battery with a lot of punch.

- **Nominal Voltage** - These have a nominal voltage of **7.4V** and like the round cell batteries, do ***NOT*** have a built in protection circuit. Special care must be taken when charging and discharging these batteries so that they do not become damaged. More information on protection circuits can be found [here](https://www.digikey.com/en/maker/blogs/lithium-ion-cell-protection).

- **Connectors** - The charge connector is a 3 pin JST-XH charge plug. Discharge is via Dean's Connector discharge leads.

- **Charging and Discharging** -Since there is no protection circuit on these batteries, the user must account for the possibility of over or under charging such that the battery isn\'t damaged. Because these are typically dual cell battery packs, a special charger is needed. This battery is not compatible with single cell chargers. We recommend a specialized charger such as this one:

  ::::::::: tile-wrap
  ::::: 
  ::: actions-wrap
  [![Tenergy 5-in-1 Intelligent Battery Cell Meter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/7/5/15348-Tenergy_5_in_1_Intelligent_Battery_Cell_Meter-01.jpg)](https://www.sparkfun.com/products/15348)
  :::

  ::: main
  ### [Tenergy 5-in-1 Intelligent Battery Cell Meter](https://www.sparkfun.com/products/15348) 

  [ TOL-15348 ]
  The Tenergy 5-in-1 Intelligent Cell Meter takes you one step closer to becoming an all-seeing and all-powerful battery wizard...
  :::

  **Retired**
  :::::

  ::::: 
  ::: actions-wrap
  [![SkyRC IMAX B6 V2 Professional Balance Charger / Discharger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/0/2/16793-SkyRC_IMAX_B6_V2_Balance_Charger_-_Discharger-01.jpg)](https://www.sparkfun.com/skyrc-imax-b6-v2-professional-balance-charger-discharger.html)
  :::

  ::: main
  ### [SkyRC IMAX B6 V2 Professional Balance Charger / Discharger](https://www.sparkfun.com/skyrc-imax-b6-v2-professional-balance-charger-discharger.html) 

  [ PRT-16793 ]
  The SkyRC B6 V2 is a DC input high-performance, micro-processor controlled charge/discharge/DC/DC converter with battery mana...
  :::

  **Retired**
  :::::
  :::::::::

  ::: clearfix
  :::

## Nickel Metal Hydride

Nickel Metal Hydride (often abbreviated NiMH) batteries are a proven rechargeable technology. These batteries are often lower cost than other chemistries but suffer from lower densities than LiPo. NiMH batteries require less stringent charging curves, which lower the cost of the chargers. NiMH are often found in lower cost electronic devices such as toothbrushes and cordless shavers where output voltage is less of a concern (you'll notice your toothbrush running more slowly but continues to work).

[![2500 mAh NiMH Battery - AA](https://cdn.sparkfun.com/r/600-600/assets/parts/2/6/1/00335-AA-Battery-Feature-2.jpg)](https://www.sparkfun.com/2500-mah-nimh-battery-aa.html)

### [2500 mAh NiMH Battery - AA](https://www.sparkfun.com/2500-mah-nimh-battery-aa.html) 

[ PRT-00335 ]

2500mAh 1.2V Nickel Metal Hydride rechargeable \'AA\' batteries. \[NiMH technology\](http://en.wikipedia.org/wiki/Nickel_metal_hy...

**Retired**

Each cell outputs **nominally 1.2V**. This is very similar to alkaline batteries of the same size that output 1.5V. Combining four AA NiMH will get you a 4.8V pack which should run most 5V systems but will drop in voltage as the pack discharges.

### Charging and Discharging

NiMH batteries on their own have no discharge protection circuits. A discharge protection circuit prevents the battery from discharging below a certain voltage level to prevent damage to the battery. More information on NiMH batteries and over-discharge can be found [here](https://en.wikipedia.org/wiki/Nickel%E2%80%93metal_hydride_battery).

Because of their similarity to regular consumer batteries, charging NiMH batteries is often done with [chargers](https://www.sparkfun.com/products/10052) that plug into the wall. We recommend NiMH for applications where a device has already been designed to use AA type batteries.

[![Wall mount NiMH Charger](//cdn.sparkfun.com/assets/3/7/5/1/e/5112ba49ce395f322a000001.jpg)](//cdn.sparkfun.com/assets/3/7/5/1/e/5112ba49ce395f322a000001.jpg)

## Coin Cell

[Coin cell](https://www.sparkfun.com/products/338) batteries are great for very small, low power projects. These batteries are cheap! Buy them in bulk if you need a lot. They are great for testing [LEDs](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds). You\'ll find these type of batteries hidden inside [remote controls](https://www.sparkfun.com/products/10280), [electronic tealight candles](https://www.google.com/search?q=tea+candles) and lots of smaller disposable devices.

[![Coin Cell Battery - 20mm (CR2032)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/6/4/338-Coin-Cell-Battery-20mm-Feature.jpg)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html)

### [Coin Cell Battery - 20mm (CR2032)](https://www.sparkfun.com/coin-cell-battery-20mm-cr2032.html) 

[ PRT-00338 ]

CR2032 Lithium metal 3V 250mAh button cell battery. Great for powering low power processors or blink an LED for weeks at a ti...

[ [\$2.25] ]

These batteries **are not** rechargeable. There are a few, more complex [chargeable versions](https://www.sparkfun.com/products/10319), but the vast majority of coin cells are meant to be thrown away once used.

The chemistries and technologies behind coin cells vary. Some are alkaline, others are lithium. Alkaline coin cell batteries have a nominal voltage of 1.5V. Lithium coin cell batteries, on the other hand, have a nominal voltage of 3V.

Coin cell batteries come in a few different sizes, each with a specially coded name to indicate the size and chemistry. Alkaline coin cells all start with an \"L\", while lithium coin cells are all prefixed with a \"C\". The popular [CR2032](https://www.sparkfun.com/products/338), for example, is a lithium battery (3V nominal voltage) measuring 20mm in diameter and 3.2mm tall. An [LR1154 (aka LR44)](https://www.sparkfun.com/products/11305) is an alkaline battery (1.5V) measuring 11mm across and 5.4mm tall.

Coin cells are great for powering an ATtiny or other small [microcontroller and LED](https://tindie.com/shops/miceuz/chirp-plant-watering-alarm/) projects.

## Alkaline

We've all grown up with this type of disposable battery. These batteries have been around for many decades, so you'll find them everywhere! There's also a multitude of [battery holders](https://www.sparkfun.com/search/results?term=battery+holder&what=products) and accessories for AA and 9V batteries.

These batteries are cheap, safe to use, and available everywhere, but sadly, they **are not** rechargeable. The alkaline chemistry makes these batteries particularly idiot proof (safe).

AAs and AAAs are the most common alkaline batteries and output **1.2V nominally** (but are around 1.5V when first used). Because AAs output 1.2V, you will need to combine them in packs of 3 or 4 to run your 3.3V or 5V system. 9V batteries are obviously 9V nominally.

[![Panasonic Alkaline Battery - AA](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/2/5/15201-Panasonic_Alkaline_Battery_-_AA-02.jpg)](https://www.sparkfun.com/panasonic-alkaline-battery-aa.html)

### [Panasonic Alkaline Battery - AA](https://www.sparkfun.com/panasonic-alkaline-battery-aa.html) 

[ PRT-15201 ]

These are your standard 1.5V AA alkaline batteries from Panasonic.

[ [\$0.60] ]

A 9V battery with a [connector cable](https://www.sparkfun.com/products/9518) is a great, quick way to make a project portable, but don't expect the battery to last very long! While it outputs 9 volts, the capacity of a 9V battery is pretty low.

[![9V Alkaline Battery](https://cdn.sparkfun.com/r/600-600/assets/parts/4/5/6/2/10218-01.jpg)](https://www.sparkfun.com/9v-alkaline-battery.html)

### [9V Alkaline Battery](https://www.sparkfun.com/9v-alkaline-battery.html) 

[ PRT-10218 ]

These are your standard 9 Volt alkaline batteries from Rayovac. Don\'t even think about trying to recharge these. Use them wit...

[ [\$2.40] ]

We regularly use this type of batteries with beginners. They are often comfortable with this type of battery and can easily find them. If they attach the battery backwards it may heat up, but little damage is done. Once a student is past the basics we generally transition users to LiPos because they last longer and can be recharged.