# Source: https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering

## Introduction

Soldering is one of the most fundamental skills needed to dabble in the world of electronics. The two go together like peas and carrots. And, although it is possible to learn about and build electronics without needing to pick up a soldering iron, you\'ll soon discover that a whole new world is opened with this one simple skill. We here at SparkFun believe that soldering should be a skill in everyone\'s arsenal. In a world of increasing technological surroundings, we believe it is important that people everywhere be able to not only understand the technologies they use everyday but also be able to build, alter, and fix them as well. Soldering is one of many skills that will empower you to do just that.

[![soldering action shot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/Soldering_Action-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/Soldering_Action-01.jpg)

In this tutorial we will go over the basics of **through-hole soldering** \-- also known as plated through-hole soldering (PTH), discuss the tools needed, go over techniques for proper soldering, and show you where you can go from there. We will also discuss rework as it pertains to through-hole soldering and give you some tips and tricks that will make fixing any piece of electronics a breeze. This guide will be for beginners and experts alike. Whether you\'ve never touched an iron before or are looking for a little refresher, this tutorial has a little something for everyone.

### Suggested Reading

As stated earlier, you can learn about and build electronics without touching a soldering iron. If you would like to learn more about electronics theory before learning to solder, we recommend starting with some of these tutorials:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

If you would like to know more about building circuits without needing to pick up a soldering iron, check out our solderless breadboard tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

Lastly, we will be building upon some previous tutorials, so it is suggested that you read about and understand these subjects before moving forward in this tutorial:

[](https://learn.sparkfun.com/tutorials/pcb-basics)

### PCB Basics 

What exactly IS a PCB? This tutorial will breakdown what makes up a PCB and some of the common terms used in the PCB world.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/polarity)

### Polarity 

An introduction to polarity in electronic components. Discover what polarity is, which parts have it, and how to identify it.

------------------------------------------------------------------------

If you\'re all caught up on the above reading, let\'s dive right in!

------------------------------------------------------------------------

## What is Solder?

Before learning how to solder, it\'s always wise to learn a little bit about solder, its history, and the terminology that will be used while discussing it.

**[Solder](https://www.sparkfun.com/categories/49)**, as a word, can be used in two different ways. Solder, *the noun*, refers to the alloy (a substance composed of two or more metals) that typically comes as a long, thin wire in spools or tubes. Solder, *the verb*, means to join together two pieces of metal in what is called a **solder joint**. So, we solder with solder!

[![Solder](https://cdn.sparkfun.com/r/600-600/assets/4/a/e/6/2/51d9ac14ce395fd62a000000.jpg)](https://cdn.sparkfun.com/assets/4/a/e/6/2/51d9ac14ce395fd62a000000.jpg)

*Solder wire sold as a [spool](https://www.sparkfun.com/products/10243) (left) and in a [tube](https://www.sparkfun.com/products/9163) (right). These come in both leaded and lead-free varieties.*

### Leaded vs. Lead-free Solder \-- A Brief History

One of the most important things to be aware of when it comes to solder is that, traditionally, solder was composed of mostly lead (Pb), tin (Sn), and a few other trace metals. This solder is known as **leaded solder**. As it has come to be known, [lead is harmful to humans](http://chemistry.about.com/od/howthingsworkfaqs/f/leadpoisoning.htm) and can lead to lead poisoning when exposed to large amounts. Unfortunately, lead is also a very useful metal, and it was chosen as the go-to metal for soldering because of its low melting point and ability to create great solder joints.

With the adverse effects of leaded soldering known, some key individuals and countries decided it was best to not use leaded solder anymore. In 2006, the European Union adopted the [Restriction of Hazardous Substances Directive](http://en.wikipedia.org/wiki/Restriction_of_Hazardous_Substances_Directive) (**RoHS**). This directive, stated simply, restricts the use of leaded solder (amongst other materials) in electronics and electrical equipment. With that, the use of **lead-free solder** became the norm in electronics manufacturing.

Lead-free solder is very similar to its leaded counterpart, except, as the name states, it contains no lead. Instead it is made up of mostly tin and other trace metals, such as silver and copper. This solder is usually marked with the RoHS symbol to let potential buyers know it conforms to the standard.

### Choosing the Right Solder for the Job

When it comes to manufacturing electronics, it\'s best to use lead-free solder to ensure the safety of your products. However, when it comes to you and your electronics, the choice of solder is yours to make. Many people still prefer the use of leaded solder on account of its superb ability to act as a joining agent. Still, others prefer safety over functionality and opt for the lead-free. SparkFun [sells both varieties](https://www.sparkfun.com/search/results?term=solder+lead+&what=products) to allow individuals to make that choice for themselves.

Lead-free solder is not without its downfalls. As mentioned, lead was chosen because it performs the best in a situation such as soldering. When you take away the lead, you also take away some of the properties of solder that make it ideal for what it was intended \-- joining two pieces of metal. One such property is the melting point. Tin has a higher melting point than lead resulting in more heat needed to achieve flow. And, although tin gets the job done, it sometimes needs a little help. Many lead-free solder variants have what\'s called a **flux core.** For now, just know that flux is a chemical agent that aids in the flowing of lead-free solder. While it is possible to use lead-free solder without flux, it makes it much easier to achieve the same effects as with leaded solder. Also, because of the added cost in making lead-free solder, it can sometimes be more expensive than leaded solder.

Aside from choosing leaded or lead-free solder, there are a number of other factors to consider when picking out solder. First, there are tons of other solder compositions out there aside from lead and tin. Check out the [Wikipedia solder page](http://en.wikipedia.org/wiki/Solder) for an extensive list of the different types. Second, solder comes in a variety of gauges, or widths. When working with small components, it\'s often better to use a very thin piece of solder \-- the larger then number, the smaller the gauge. For large components, thicker wire is recommended. Last, solder comes in other forms besides wire. When getting into surface-mount soldering, you\'ll see that solder paste is the form of choice. However, since this is a through-hole soldering tutorial, solder paste will not be discussed in detail.

### Purchasing Solder

SparkFun offers many sizes of spools of solder in both leaded and lead-free varieties. Whether you just need enough for one project or are stocking up for the coming winter, SparkFun has what you need. You can visit the [Soldering category](https://www.sparkfun.com/categories/49) of the SparkFun catalog for more solder options as well.

#### Lead Free

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Solder - 1/4lb Spool (0.032\") Special Blend](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/9/3/10243-Solder_-_1_4lb_Spool__0.032___Special_Blend-01.jpg)](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html)

### [Solder - 1/4lb Spool (0.032\") Special Blend](https://www.sparkfun.com/solder-1-4lb-spool-0-032-special-blend.html) 

[ TOL-10243 ]

We don\'t want to hype this solder TOO much, but this could possibly be the best solder in the world. There, we\'ve said it. Th...

[ [\$28.50] ]

[![Solder - 1/4lb Spool (0.020\") Special Blend](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/9/2/10242-Solder_-_1_4lb_Spool__0.020in.__Special_Blend.jpg)](https://www.sparkfun.com/solder-1-4lb-spool-0-020-special-blend.html)

### [Solder - 1/4lb Spool (0.020\") Special Blend](https://www.sparkfun.com/solder-1-4lb-spool-0-020-special-blend.html) 

[ TOL-10242 ]

We don\'t want to hype this solder TOO much, but this could possibly be the best solder in the world. There, we\'ve said it. Th...

[ [\$33.95] ]

#### Leaded

[![Solder Leaded - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/5/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-leaded-100-gram-spool.html)

### [Solder Leaded - 100-gram Spool](https://www.sparkfun.com/solder-leaded-100-gram-spool.html) 

[ TOL-09161 ]

This is your basic spool of leaded solder with a 63/37 water soluble resin core. 0.031\" gauge and 100 grams. This is a good s...

[ [\$9.95] ]

[![Solder Leaded - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/6/09162-02-L.jpg)](https://www.sparkfun.com/solder-leaded-15-gram-tube.html)

### [Solder Leaded - 15-gram Tube](https://www.sparkfun.com/solder-leaded-15-gram-tube.html) 

[ TOL-09162 ]

This is your basic tube of leaded solder with a 63/37 water soluble resin core. 0.031\" gauge and 15 grams (around 5ft). Easy ...

[ [\$2.95] ]

Now that you know how to choose the best solder for the job, let\'s move on to tools and more terminology.

------------------------------------------------------------------------

## Soldering Irons

There are many tools that aid in soldering, but none are more important than the [soldering iron](https://www.sparkfun.com/categories/49). If nothing else, you need at least an iron and some solder to accomplish the task at hand. Soldering irons come in a variety of from factors and range from simple to complex, but they all function roughly the same. Here, we\'ll discuss the parts of an iron and the different types of irons.

[![Soldering Iron Stations](https://cdn.sparkfun.com/r/600-600/assets/e/3/9/9/4/51d9fbe1ce395f7a2a000000.jpg)](https://cdn.sparkfun.com/assets/e/3/9/9/4/51d9fbe1ce395f7a2a000000.jpg)

### Soldering Iron Anatomy

Here are the basic parts that make up a soldering iron.

- **[Soldering Tips](https://www.sparkfun.com/search/results?term=solder+tip)** - No iron is complete without an iron tip. The tip is the part of the iron that heats up and allows solder to flow around the two components being joined. Although solder will stick to the tip when applied, a common misconception is that the tip transfers the solder. The tip actually transfers heat, raising the temperature of the metal components to the melting point of the solder, and the solder melts accordingly. Most irons give you the option to change your tip, should you need to replace an old tip or if you need to switch to a different style of tip. Tips come in a variety of sizes and shapes to accommodate any component.

[![Soldering Iron Tips](https://cdn.sparkfun.com/r/600-600/assets/f/8/1/4/9/51d9fdd4ce395f4432000000.jpg)](https://cdn.sparkfun.com/assets/f/8/1/4/9/51d9fdd4ce395f4432000000.jpg)

*Several types of tips. From left to right, the bevel tip (aka hoof tip), two conical tips with varying widths, and the chisel tip.*

Changing the tip is a simple process that consists of either unscrewing the wand or simply pushing in and pulling out the tip

[![changing the tip](https://cdn.sparkfun.com/assets/e/d/9/0/f/51da1220ce395f8b2a000001.jpg)](https://cdn.sparkfun.com/assets/e/d/9/0/f/51da1220ce395f8b2a000001.jpg)

[] **Tip:** The efficiency of the heat transferred from the tip to the joint is dependent on the the size of the soldering iron tip that you are using. Usually, you want to have a soldering tip that is about the same width as the soldering pad you are soldering to. For more information, check out [this article by Hakko](http://www.hakko.com/english/tip_selection/selection_1.html).

- **Wand** - The wand is the part of the iron that holds the tip. This is also the part that is handled by the user. Wands are usually made of a variety of insulating materials (such as rubber) to prevent the heat of the tip from transferring to the outside of the wand, but they also house wires and metal contacts that transfer heat from the base or outlet to the tip. This dual role of heating and preventing burns makes a high quality wand much appreciated.

[![wands](https://cdn.sparkfun.com/r/600-600/assets/c/a/7/e/f/51d9ff71ce395fe229000000.jpg)](https://cdn.sparkfun.com/assets/c/a/7/e/f/51d9ff71ce395fe229000000.jpg)

*Two varieties of wands. Notice how the tips screw into the wand allowing for interchangeability. Some wands have tips that simply push in and pull out without any attaching mechanism.*

Some irons consist of just a wand that plugs into a wall outlet. These irons are as simple as they come, and they do not have any controls to vary the temperature. In these irons, the heating element is built directly into the wand.

[![wand iron](https://cdn.sparkfun.com/assets/4/8/8/3/0/51da077ece395fb529000002.jpg)](https://cdn.sparkfun.com/assets/4/8/8/3/0/51da077ece395fb529000002.jpg)

*A [simple soldering iron](https://www.sparkfun.com/products/9507) that consists of just the wand. Some of these irons do not offer interchangeable tips.*

- **Base** - The base of the soldering iron is the control box that allows the adjusting of temperatures. The wand attaches to the base and receives its heat from the electronics inside. There are analog bases, which have a dial that controls the temperature, and there are digital bases, which have buttons to set the temperature and a display that tells you the current temperature. Some bases even have extra features such as heat profiles that allow you to quickly change the amount of heat provided to the tip for soldering a variety of components.

[![bases](https://cdn.sparkfun.com/r/600-600/assets/a/6/7/3/0/51da017fce395ffd29000000.jpg)](https://cdn.sparkfun.com/assets/a/6/7/3/0/51da017fce395ffd29000000.jpg)

*Two variations of a soldering iron base. On the left, a digital base, complete with control buttons and a digital display. On the right, an analog base that uses a dial to control the temperature.*

The base typically is comprised of a large transformer and several other control electronics that safely allow you to vary the heat of your tip.

[![inside iron](https://cdn.sparkfun.com/assets/c/f/7/6/6/51da0d69ce395fa029000001.jpg)](https://cdn.sparkfun.com/assets/c/f/7/6/6/51da0d69ce395fa029000001.jpg)

*The insides of a soldering iron base*

- **Stand (Cradle)** - The iron stand (often referred to as a cradle) is what houses the iron when it is not in use. The stand may seem trivial, but leaving an unattended iron laying around on your desk or workbench is a potential hazard: it could burn you, or, worse, it could burn your desk and start a fire. Again, they can be as simple as a [metal stand](https://www.sparkfun.com/products/9477), or they can be complex, offering an auto-shutoff feature that reduces the temperature of the tip when the wand is placed in the cradle. This helps prevent the wearing of your tip over time.

[![Soldering Iron stands](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/standsGOOD.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/standsGOOD.jpg)

*Different types of iron cradles. Notice some allow for a regular sponge while others hold a brass sponge.*

- **[Brass Sponge](https://www.sparkfun.com/products/8964)** - As you solder, your tip will tend to **oxidize**, which means it will turn black and not want to accept solder. Especially with lead-free solder, there are impurities in the solder that tend to build up on the tip of your iron, which causes this oxidization. This is where the sponge comes in. Every so often you should give your tip a good cleaning by wiping off this build-up. Traditionally, an actual wet sponge was used to accomplish this. However, using a wet sponge can drastically reduce the lifespan of your tip. By wiping your tip on a cool, wet sponge, the tip tends to expand and contract from the change in temperature. This expansion and contraction will wear out your tip and can sometime cause a hole to develop in the side of the tip. Once a tip has a hole, it is no good for soldering. Thus, brass sponges have become the standard for tip cleaning. Brass sponges pull the excess solder from your tip while allowing the tip to maintain its current heat level. If you do not have a brass sponge, a regular sponge is better than nothing.

[![brass sponge](https://cdn.sparkfun.com/assets/5/2/c/d/d/51da0016ce395f9d29000000.jpg)](https://cdn.sparkfun.com/assets/5/2/c/d/d/51da0016ce395f9d29000000.jpg)

*A [brass sponge](https://www.sparkfun.com/products/8964). If your iron stand doesn\'t have a spot for a brass sponge, you can get [one](https://www.sparkfun.com/products/8965) with its own base.*

------------------------------------------------------------------------

## Purchasing a Soldering Iron

Whether you\'re just beginning or a seasoned pro we\'ve got a soldering iron for you!

### Our Recommendations:

[![PINECIL Soldering Iron Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/5/KIT-24063-PINECIL-Soldering-Iron-Kit-Feature.jpg)](https://www.sparkfun.com/pinecil-soldering-iron-kit.html)

### [PINECIL Soldering Iron Kit](https://www.sparkfun.com/pinecil-soldering-iron-kit.html) 

[ KIT-24063 ]

The PINECIL Soldering Iron Kit provides a compact powerhouse and everything you need to ignite your DIY dream.

[ [\$119.95] ]

[![Hakko FX-888DX Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/6/4/6/TOL-25926-Hakko-FX-888DX-Soldering-Station-feature.jpg)](https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html)

### [Hakko FX-888DX Soldering Station](https://www.sparkfun.com/hakko-fx-888dx-soldering-station.html) 

[ TOL-25926 ]

The HAKKO FX-888DX Digital Soldering Station improves the user interface from the FX-888D using a more intuitive method for a...

[ [\$129.95] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![iFixit FixHub - Power Series Portable Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/3/0/0/TOL-27147-Ifixit-Portable-Soldering-Station-Feature2.jpg)](https://www.sparkfun.com/ifixit-fixhub-power-series-portable-soldering-station.html)

### [iFixit FixHub - Power Series Portable Soldering Station](https://www.sparkfun.com/ifixit-fixhub-power-series-portable-soldering-station.html) 

[ TOL-27147 ]

The FixHub Portable Soldering Station gives you the power of a benchtop setup, anywhere you need it---without compromising pe...

[ [\$249.95] ]

Looking for more options for soldering iron? Click on the button below for additional options in the catalog!

[Click to Here for More Soldering Iron & Stations](https://www.sparkfun.com/categories/49)

------------------------------------------------------------------------

## Soldering Accessories

Now that you know the ins and outs of a soldering iron, it\'s time to discuss the other tools that will aid you on your soldering adventure.

### Solder Wick

- **[Solder Wick](https://www.sparkfun.com/products/8775)** - The eraser to soldering\'s pencil. When dealing with issues such as jumpers or the removal of parts (desoldering), solder wick comes in very handy. Solder wick \-- aka desoldering braid \-- is comprised of thin copper wire braided together. Solder is soaked (wicked) up by the copper allowing you to [\"erase\" extra globs of solder](https://learn.sparkfun.com/tutorials/simon-says-assembly-guide#solder_wick).

[![Solder Wick #2 25ft. - TechSpray](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/9/4/08775-01-L.jpg)](https://www.sparkfun.com/solder-wick-2-25ft-techspray.html)

### [Solder Wick #2 25ft. - TechSpray](https://www.sparkfun.com/solder-wick-2-25ft-techspray.html) 

[ TOL-08775 ]

Solder wick, coffee, and paper towels keep SparkFun running. You can steal someone\'s diagonal cutters for a minute, but you\'d...

**Retired**

14782

### Tip Tinner

- **[Tip Tinner](https://www.sparkfun.com/products/13246)** - A chemical paste used to clean the tip of your soldering iron. It is composed of a mild acid that helps remove baked on residue (like when you accidentally melt your tip on a component) and helps prevent oxidation (the nasty black stuff) that accumulates on your soldering tip when not in use.

[![Solder Tip Tinner and Cleaner](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/3/9/13246-01.jpg)](https://www.sparkfun.com/solder-tip-tinner-and-cleaner.html)

### [Solder Tip Tinner and Cleaner](https://www.sparkfun.com/solder-tip-tinner-and-cleaner.html) 

[ TOL-13246 ]

Tip tinner is a good thing to have in your arsenal of soldering supplies. Composed of a mild acid, it helps remove baked on r...

[ [\$11.50] ]

### Solder Vacuum (Solder Sucker)

- **[Solder Vacuum](https://www.sparkfun.com/products/13203) (Solder Sucker)** - A great tool for removing solder left behind in through-holes when desoldering components. We\'ll go over how to use this tool a little later in the tutorial.

[![Solder Vacuum](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/3/4/4/13203-Solder_Vacuum-Black-01.jpg)](https://www.sparkfun.com/solder-vacuum.html)

### [Solder Vacuum](https://www.sparkfun.com/solder-vacuum.html) 

[ TOL-13203 ]

The Solder Vacuum, a great (and sometimes under appreciated) little tool for solder rework. It allows you to pull the molten ...

[ [\$6.95] ]

### Flux

- **[Water Soluble Flux](https://www.sparkfun.com/products/retired/8967)** - Flux is a chemical agent that aids in the flowing of lead-free solder. Flux pens allow you to dab stubborn components with liquid flux to create better looking solder joints. It is recommended to [clean and remove](https://learn.sparkfun.com/tutorials/electronics-assembly#washing) any remaining water soluble flux residue on the board.

[![Water Soluble Flux Pen](https://cdn.sparkfun.com/r/400-400/assets/3/f/e/a/1/523a9588757b7f1d4f8b4568.jpg)](https://cdn.sparkfun.com/assets/3/f/e/a/1/523a9588757b7f1d4f8b4568.jpg)

- **[No Clean Flux](https://www.sparkfun.com/products/14579)** - Flux is another chemical agent that aids in the flowing of lead-free solder. Flux pens allow you to dab stubborn components with liquid flux to create better looking solder joints. Cleaning and flux removal is not required. For those interested in removing the flux residue, isopropyl alcohol (IPA) is required. Flux can also be applied through a syringe or precision tip application bottle.

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

[![Chip Quik No-Clean Tack Flux in 5cc Syringe (with Tips)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/5/5/7/TOL-25101-Chip-Quik-No-Clean-Tack-Flux-Feature.jpg)](https://www.sparkfun.com/chip-quik-no-clean-tack-flux-in-5cc-syringe-with-tips.html)

### [Chip Quik No-Clean Tack Flux in 5cc Syringe (with Tips)](https://www.sparkfun.com/chip-quik-no-clean-tack-flux-in-5cc-syringe-with-tips.html) 

[ TOL-25101 ]

This 5cc no-clean flux syringe from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$11.50] ]

### Silicone Soldering Mat

- **[Insulated Silicone Soldering Mat](https://www.sparkfun.com/products/14672)** - Protect your desktop and keep it clean with a silicone soldering mat.

[![Insulated Silicone Soldering Mat](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/7/0/14672-Insulated_Silicone_Soldering_Mat-01.jpg)](https://www.sparkfun.com/insulated-silicone-soldering-mat.html)

### [Insulated Silicone Soldering Mat](https://www.sparkfun.com/insulated-silicone-soldering-mat.html) 

[ TOL-14672 ]

With this Insulated Silicone Soldering Mat you will be provided with the means to protect your desktop, soldering station, or...

[ [\$15.95] ]

### Solder Dispenser

- **[Solder-Mate Solder Dispenser](https://www.sparkfun.com/products/14232)** - To prevent your spool from rolling away and dispense your solder.

[![Solder-Mate Solder Dispenser](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/1/7/7/14232-04.jpg)](https://www.sparkfun.com/solder-mate-solder-dispenser.html)

### [Solder-Mate Solder Dispenser](https://www.sparkfun.com/solder-mate-solder-dispenser.html) 

[ TOL-14232 ]

The Solder-Mate™ Solder Dispenser provides you with an easy way to, well\...dispense solder! This handy tool provides a cont...

[ [\$15.50] ]

### Other Suggested Tools

The following tools aren\'t necessary, but they sure do make soldering easier at times.

### Third Hand (Third Arm)

- **[Third Hand](https://www.sparkfun.com/search/results?term=third) (Third Arm)** - Third hands are great for holding PCBs, wires, and components in place while you solder. The articulation depends on how the third arm is manufactured. Some third arms will have a wider range of motion to hold the PCB up than other third arms.

[![Third Hand](https://cdn.sparkfun.com/r/600-600/assets/parts/2/8/5/8/09317-01.jpg)](https://www.sparkfun.com/third-hand.html)

### [Third Hand](https://www.sparkfun.com/third-hand.html) 

[ TOL-09317 ]

This is a solderer\'s best helper, the third hand. Comes with a heavy base, two alligator clips, a soldering iron holder, and ...

[ [\$15.95] ]

[![SparkFun Third Hand Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/8/0/3/1/11784-05.jpg)](https://www.sparkfun.com/sparkfun-third-hand-kit.html)

### [SparkFun Third Hand Kit](https://www.sparkfun.com/sparkfun-third-hand-kit.html) 

[ TOL-11784 ]

Are you frustrated with the lack of dexterity from most third hands? The SparkFun Third Hand gives you the ability to hold a ...

[ [\$38.50] ]

[![Magnetic Third-Hand Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/7/9/19944-Magnetic_Third-Hand_Kit-01.jpg)](https://www.sparkfun.com/magnetic-third-hand-kit.html)

### [Magnetic Third-Hand Kit](https://www.sparkfun.com/magnetic-third-hand-kit.html) 

[ TOL-19944 ]

If you need an extra pair of hands (or three!) to help with the delicate, detailed work, you will appreciate this magnetic th...

[ [\$81.50] ]

### Panavise Jr.

- **[Panavise Jr. - Vacuum Base](https://www.sparkfun.com/products/10410)** - Another great tool for holding PCBs, wires, and components in place while you solder and reworking your board.

[![Panavise Jr. - Vacuum Base](https://cdn.sparkfun.com/r/600-600/assets/parts/4/8/8/1/10410-01.jpg)](https://www.sparkfun.com/products/10410)

### [Panavise Jr. - Vacuum Base](https://www.sparkfun.com/products/10410) 

[ TOL-10410 ]

The Panavise Jr. is a great vise with a vacuum base. Its jaws open up to about 3\" and have grooves for PCBs. It\'s perfect for...

**Retired**

### Stickvise PCB Vise

- **[Stickvise PCB Vise](https://www.sparkfun.com/products/17235)** - This low profile PCB vise is ideal for holding a PCB flat while soldering, testing, and wiring on a table. They also fit easily under a microscope to keep the PCB consistently in focus. Worried about accidentally melting your standard Nylon jaws with the Stickvise? You may want to upgrade by picking up a pair of the [high temperature PTFE jaws](https://www.sparkfun.com/products/17594). They will not melt or become damaged by incidental contact with a soldering iron.

[![Stickvise PCB Vise](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/2/1/6/17235-Stickvise-02.jpg)](https://www.sparkfun.com/stickvise-pcb-vise.html)

### [Stickvise PCB Vise](https://www.sparkfun.com/stickvise-pcb-vise.html) 

[ TOL-17235 ]

These flat PCB holders are great because your hands can rest directly on the table for fine soldering and probing.

[ [\$66.95] ]

[![Stickvise High Temperature PTFE Jaws](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/6/7/4/17594-Stickvise_High_Temperature_PTFE_Jaws-01.jpg)](https://www.sparkfun.com/stickvise-high-temperature-ptfe-jaws.html)

### [Stickvise High Temperature PTFE Jaws](https://www.sparkfun.com/stickvise-high-temperature-ptfe-jaws.html) 

[ TOL-17594 ]

Concerned about accidentally melting the standard Nylon jaws on a Stickvise? Never fear, these High Temperature PTFE Jaws are...

**Retired**

### PCBite Kit

- **PCBite Kit ([Small](https://www.sparkfun.com/products/19720) and [Large Base Plates](https://www.sparkfun.com/products/19721))** - The PCBite Kits include PCB holders with stainless spring jaws that clamp to the edge of PCBs with varying sizes and shapes. Yellow insulated washers are included to protect the circuit boards. On the bottom of each PCB holder is a powerful magnet that allow the holders that stick to the stainless base plate. While this \"third hand\" does not have flexible arms, it is ideal for clamping PCBs securely for soldering, desoldering, or rework on a flat table. The PCBite Kit is also portable and is not awkwardly shaped like some third hands. Additionally, there are [accessories available to easily probe](https://www.sparkfun.com/categories/tags/pcbite) a circuit board.

[![PCBite Kit (Small Base Plate)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/4/1/8/19720-PCBite_Kit__Small_Base_Plate_-01.jpg)](https://www.sparkfun.com/pcbite-kit-small-base-plate.html)

### [PCBite Kit (Small Base Plate)](https://www.sparkfun.com/pcbite-kit-small-base-plate.html) 

[ TOL-19720 ]

Perfect for holding your PCB for soldering or inspection.

**Retired**

[![PCBite Kit (Large Base Plate)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/4/1/9/19721-PCBite_Kit__Large_Base_Plate_-01.jpg)](https://www.sparkfun.com/pcbite-kit-large-base-plate.html)

### [PCBite Kit (Large Base Plate)](https://www.sparkfun.com/pcbite-kit-large-base-plate.html) 

[ TOL-19721 ]

Perfect for holding your PCB for soldering or inspection.

**Retired**

### Needle Nose Pliers

- **[Needle Nose Pliers](https://www.sparkfun.com/products/8793)** - Mini pliers are a must have for any hobbyist or electrical engineer. Crucial for inserting devices into breadboards and bending pins.

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

### Diagonal Cutters

- **[Diagonal Cutters](https://www.sparkfun.com/products/08794)** - Cutters allow you to trim the legs of components you solder to the PCB. They can also be used to grip, grap, and pry connectors or other various cables such as a [LiPo battery\'s 2-pin JST connector](https://www.sparkfun.com/tutorials/241).

[![Electronic Snippers](https://cdn.sparkfun.com/r/600-600/assets/parts/4/9/3/5/10447-Electronic_Snippers-04.jpg)](https://www.sparkfun.com/products/10447)

### [Electronic Snippers](https://www.sparkfun.com/products/10447) 

[ TOL-10447 ]

While our small diagonal cutters are great for hobby use, sometimes you need something with a little more bite. These electro...

**Retired**

[![Diagonal Cutters](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

### Flush Cutters

- **[Flush Cutters](https://www.sparkfun.com/products/11952)** - Giving you a way to cut leads very cleanly and close to the solder joint. Diagonal cutters are good, but if you really need to get up close and personal, flush cutters are the way to go.

[![Flush Cutters - Hakko](https://cdn.sparkfun.com/r/600-600/assets/parts/8/4/2/2/11952-Hakko-Flush-Cutters-feature.jpg)](https://www.sparkfun.com/flush-cutters-hakko.html)

### [Flush Cutters - Hakko](https://www.sparkfun.com/flush-cutters-hakko.html) 

[ TOL-11952 ]

Tool for a flush cut.

[ [\$10.50] ]

### Safety Glasses

- **[Safety Glasses](https://www.sparkfun.com/products/11046)** - Just in case any clipped leads or molten solder fly toward your eyes. We use these for eye protection in our production lines at SparkFun HQ!

[![SparkFun Safety Glasses](https://cdn.sparkfun.com/r/600-600/assets/parts/6/4/0/8/11046-SparkFun_Safety_Glasses-02.jpg)](https://www.sparkfun.com/sparkfun-safety-glasses.html)

### [SparkFun Safety Glasses](https://www.sparkfun.com/sparkfun-safety-glasses.html) 

[ SWG-11046 ]

With these SparkFun Safety Glasses you\'ll have a pair of lightweight, economical, and stylish lenses to protect your precious...

[ [\$5.10] ]

### Monocle

- **[Monocle](https://www.sparkfun.com/products/09316)** - Useful for inspecting your solder joints and SMD components on a PCB. The LED provides sufficient light at the working distance.

[![Monocle Magnifier - Illuminated](https://cdn.sparkfun.com/r/600-600/assets/parts/2/8/5/7/09316-1.jpg)](https://www.sparkfun.com/monocle-magnifier-illuminated.html)

### [Monocle Magnifier - Illuminated](https://www.sparkfun.com/monocle-magnifier-illuminated.html) 

[ TOL-09316 ]

When working with small parts, sometimes you need magnification and some extra light. This is a monocle we use regularly in o...

[ [\$13.50] ]

**Bundled Kits!** Check out the following tool kits with some of the soldering irons and accessories listed earlier!\
\

[![SparkFun Deluxe Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/2/7/11805-SparkFun_Deluxe_Tool_Kit.jpg)](https://www.sparkfun.com/products/11805)

### [SparkFun Deluxe Tool Kit](https://www.sparkfun.com/products/11805) 

[ TOL-11805 ]

This assortment of tools is great for those of you who have experience with tools but need a fresh set of new parts for your ...

**Retired**

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/2/0/2/TOL-22265-Beginner-Tool-Kit-Feature.jpg)](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html) 

[ TOL-22265 ]

This assortment of tools is great for those who need a solid set of tools to start your workbench on the right foot!

**Retired**

------------------------------------------------------------------------

## Soldering Your First Component

Let\'s put all these tools into action. This first video will go over the basics of soldering your first component \-- headers!

Check out the Vimeo version [here](http://vimeo.com/51538354).

### Recap

It\'s really that easy! Follow Dave\'s simple rules to make every solder connection a good one.

- Be cautious when handling hot irons
- Use third hands or vices to hold boards while you solder
- Set your iron at a good medium heat (325-375 degrees C)
- If you see smoke coming from your solder, turn down the heat
- Tin your tip with solder before each connection to help prep the joint
- Use the side of the tip (aka the sweet spot), not the very tip of the iron
- Heat both the pad and the part you want to solder evenly and at the same time
- Pull the solder away, then the iron
- A good solder joint should look like a volcano or Hersey kiss, not a ball or clump

We\'ve also put together this digram to help you better understand what makes a good solder joint.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/d/a/a/9/523b1189757b7fb36e8b456b.jpg)](https://cdn.sparkfun.com/assets/c/d/a/a/9/523b1189757b7fb36e8b456b.jpg)

*Click for a larger image.*

When you are finished, tin the tip to increase its life before turning your soldering iron off.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/Tin_Solder_Iron_Tip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/Tin_Solder_Iron_Tip.jpg)

------------------------------------------------------------------------

## Tips and Tricks

Besides using a third arm, there are other methods of soldering components to boards. You will also run into issues that require different techniques to get the perfect solder joint. Check out some additional tips and tricks below!

### Tape or Sticky Tack to Hold Down Components

Got some tape or sticky tack? Try using it to hold down wires or headers against the board!

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Soldering_MAX3015-2.jpg)](https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide#hardware-hookup)   [![Soldering with Sticky Tack](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/7/8/GPS_Receiver_LS20031_Assembly_Solder_1.jpg)](https://learn.sparkfun.com/tutorials/ls20031-5hz-66-channel-gps-receiver-hookup-guide#sticky-tack)
  *Sticky tack holding down wires for the [MAX30105 particle sensor breakout board](https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide#hardware-hookup).*              *Sticky tack holding down right angle headers for the [GPS LS20031 module](https://learn.sparkfun.com/tutorials/ls20031-5hz-66-channel-gps-receiver-hookup-guide#sticky-tack).*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Silicone or Pieces of Cardboard as Insulation

Need to hold down a component but it\'s getting too hot to hold down with your fingers against the board? You can always grab a piece of silicone or cut off a piece of cardboard to hold the component down for a few seconds. Below is an example of a [resistor being held down on a shield](https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide#hardware-assembly) with the help of piece of cardboard.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Soldering_Cardboard_Protector.jpg "Piece of Cardboard to Hold Resistor Down when Soldering")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Soldering_Cardboard_Protector.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Pull_Up_Resistor.jpg "Tacking One Pin of the Pullup resistor")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Pull_Up_Resistor.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Old Shields, Development Boards, and Breadboards as a Helping Hand

If you do not have a steady hand, you can use old shields and development boards to align headers before soldering. Here are two examples from the [Arduino Shield](https://learn.sparkfun.com/tutorials/arduino-shields-v2) tutorial when installing female stackable headers or male headers.

  ------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/1/b/d/5/b/51dde3d9ce395f5665000002.JPG)]()   [![](https://cdn.sparkfun.com/r/600-600/assets/0/a/7/6/1/51dde46bce395f7164000000.JPG)]()
  *Installing Stackable Headers with an Old Shield*                                           *Installing Male Headers with a Development board*
  ------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------

If you have a shield or breakout board can fit on a breadboard, you can use the breadboard to hold the pins as you solder as well. We recommend using this method with boards that have two rows of headers. You will want to avoid applying a lot of heat as this can melt the breadboard.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Installing male headers on TeensyView shield for the Teensy with a breadboard.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/0/2/Teensy_View_Hookup_Guide-07.jpg)](https://learn.sparkfun.com/tutorials/teensyview-hookup-guide#hardware-overview-and-assembly)   [![v](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/0/MiniGen_Hookup_Guide-04.jpg)](https://learn.sparkfun.com/tutorials/minigen-hookup-guide)
  *Installing male headers on [TeensyView shield](https://learn.sparkfun.com/tutorials/teensyview-hookup-guide#hardware-overview-and-assembly) for the Teensy with a breadboard.*                                                                                                     *Installing long male headers on the [MiniGen shield](https://learn.sparkfun.com/tutorials/minigen-hookup-guide) for the Pro Mini with a mini-breadboard.*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

### Ground Planes and Large Through Holes

Depending on the design, the plated through hole pad size may be connected to a ground plane or it\'s larger than usual. These require more heat. You may notice that the solder is kind of \"sticking\" but really, it\'s just blobbing up. You may need:

- larger soldering iron tip
- adjust the soldering station to a higher temperature (720 °F)
- add flux
- keep the soldering iron on the joint just a bit longer

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Soldering to a Ground Pin on the Beefcake Relay](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-10.jpg)   [![Solder Blobbing Between Thick Wire and a Large Plated Through Hole on the Beefacke Relay](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-12.jpg)
  *Soldering to a Ground Pin on the Beefcake Relay*                                                                                                                                                                                            *Solder Blobbing Between Thick Wire and a Large Plated Through Hole on the Beefacke Relay*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usually adding some flux and keeping the soldering iron a little longer on the joint will help. Having a higher watt, adjustable soldering station usually helps with the tip recovering after it is in contact with something cold. If you have a friend or extra soldering iron around, you can also try to heat the joint with two soldering irons.

[![Two Soldering Irons on Joint](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/2/Beefcake_Relay_Hookup_Guidfe-21.jpg)

## Advanced Techniques and Troubleshooting

### Advanced PTH

Once you get the basics of creating good solder joints, it\'s time to learn some of the more advanced PTH techniques that you can utilize. This video goes over using flux, removing solder jumpers, desoldering components, along with some other tips and tricks.

Here are some other tips for PTH soldering:

- Desoldering can often be the best way to learn how to solder. There are many reasons to desolder a part: repair, upgrade, salvage, etc. Many of the techniques used in the video aid in the desoldering process.

- There is another method of removing solder from through-holes that we refer to as the [slap method](https://www.sparkfun.com/tutorials/339).

- If you\'re ever unsure if the solder joint you created is making an electrical connection, you can use a multimeter to test for [continuity](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/continuity).

### Holding Headers Against a Board

For those that have the dexterity, you can install a row of headers by holding the pins against the board! You can try to use tape and sticky tack as mentioned earlier. Below is an example of [installing female headers on the ProtoShield](https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide#hardware-assembly). However, you can follow along with male headers or use this technique to solder headers on any board.

Grab a female stackable header and slide it from the top side of a shield. With your soldering hand, pull the header with your index finger and thumb toward the edge of the board. Using your other hand, push against the header using your index finger and grip the board with your thumb. Hold the header down with your middle finger. Make sure to avoid touching any header pins where the soldering iron will touch.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg "Align Header to ProtoShield")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Tutorial_Align_Header.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg "Hold Header Down")](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Hold.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Grab the soldering iron with your soldering hand and tack on one pin. Repeat for each header. After tacking one pin for each header, you will want to ensure that the pins are straight and perpendicular to your board. If they are not, you can try to reheat the header pin and adjust the header\'s alignment.

[![Tack on One Pin on the Header and Repeat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/7/SparkFun_ProtoShield_for_Arduino_Solder_Header.jpg)

If the headers are aligned, you can solder the rest of the header pins on the board to finish installing the headers on the board!

### [][Advanced SMD](#advanced_smd)

Looking for more tips and tricks with just your soldering iron? Check out these advanced techniques to rework SMD components according to Pete.

**Note:** Need to rework surface mount components with several legs on a board? There are also portable hot plates available to heat the board up and easily remove the component. When using the mini hot plate, you may want to get two to easily hold a large PCB up as the board is being heated. We use the mini hot plates in our production department when we need to rework boards!\
\

[![Hot Plate Preheater - MHP50-B5 (Brass)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/5/7/2/TOL-26588-MHP50-B5-Hot-Plate-Preheater-Feature.jpg)](https://www.sparkfun.com/hot-plate-preheater-mhp50-b5-brass.html)

### [Hot Plate Preheater - MHP50-B5 (Brass)](https://www.sparkfun.com/hot-plate-preheater-mhp50-b5-brass.html) 

[ TOL-26588 ]

A small 50mm x 50mm soldering hot plate.

[ [\$209.95] ]

[![Mini Hot Plate Preheater - MHP30](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/5/7/1/TOL-26587-MHP30-Mini-Hot-Plate-Preheater-Feature.jpg)](https://www.sparkfun.com/mini-hot-plate-preheater-mhp30.html)

### [Mini Hot Plate Preheater - MHP30](https://www.sparkfun.com/mini-hot-plate-preheater-mhp30.html) 

[ TOL-26587 ]

A small 30mm x 30mm soldering hot plate.

[ [\$189.95] ]

### Cleaning Flux Residue

When working with lead-free solder, flux tends to get everywhere, be it from the flux in the solder or from external flux applied by the user. Certain types of flux can corrode the PCB and components over time, thus it\'s good to know how to clean your PCBs so they\'re free of any flux residue. This can also cause a high-resistance shorts between pins as a result of the moisture in the air and tiny dendrites forming. Common problems can range from uploading code to an Arduino using a serial-to-USB converter to errors when sending data through I^2^C.

How do they look like? Well, lets take a look at the images below. The image on the left shows water-soluble flux residue on the solder joints. These can appear as a yellow or brown coating on or around the solder joints. The image on the right shows no clean flux that was used on the SparkFun Edge. These can appear gunky and white on the board. It\'s non-conductive so it can be left on the board.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Water-Soluble Flux Residue on SolderJoints](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/4/0/1/assembled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/1/assembled.jpg)   [![No Clean Flux on Pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue.jpg)
  *Water-Soluble Flux Residue on the [8-Pin SOIC to DIP Adapater](https://learn.sparkfun.com/tutorials/8-pin-soic-to-dip-adapter-hookup-guide)*                                                         *No Clean Flux on the [SparkFun Edge\'s Pad](https://learn.sparkfun.com/tutorials/sparkfun-edge-hookup-guide/all#hardware-hookup)*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have water-soluble flux residue on the board, you will want to remove it from the board. No clean flux, you should not need to remove it. The simplest way to clean water soluble-flux from the board is to use a small brush with stiff bristles (toothbrushes work great) or a Q-tip. Then scrub the solder joint with hot, de-ionized water to remove the water-soluble flux. Isopropyl alcohol can be used as a substitute for water. If you must remove no-clean flux from the board, the best approach would be to use isopropyl alcohol, rather than water. Keep in mind, you\'ll have to check the documentation for your solder for the proper cleaning methodology as other types of flux may require acetone.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Removing Water Soluble Flux with a Brush](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/2/How_to_solder_castallated_via_tutorial-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/2/How_to_solder_castallated_via_tutorial-29.jpg)   [![Removing Water Soluble Flux with a Q-Tip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/4/SSOP16_Board_Hookup_Guide-18.jpg)   [![Removing No Clean Flux with a Q-Tip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue-Isopropyl-Alcohol-Cleaning.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/8/SparkFun_Edge-No-Clean-Flux-Residue-Isopropyl-Alcohol-Cleaning.jpg)
  *Removing Water Soluble Flux with a Brush*                                                                                                                                                                                                                          *Removing Water Soluble Flux with a Q-Tip*                                                                                                                                                                                                *Removing No Clean Flux with a Q-Tip*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are soldering more than a few boards, it may be necessary to clean them in batches. For this, we recommend a crock pot filled with distilled water. The distilled water keeps other impurities and contaminants away from your circuit. Below shows an image of a battery holders being cleaned. Not all boards can be dunked in water like this. So you may need to manually clean the solder joints. Having a crock pot full of hot, de-ionized water will make the process faster.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Washing PCBs with Water Soluble Flux Residue](https://cdn.sparkfun.com/r/510-510/assets/0/8/b/8/3/513e99abce395f2762000000.JPG)](https://cdn.sparkfun.com/r/510-510/assets/0/8/b/8/3/513e99abce395f2762000000.JPG)   [![Manually Cleaning an LED Strip\'s Solder Joints](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/2/CleanSolderJoints.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/2/CleanSolderJoints.jpg)
  *Dunking Boards in a Crock Pot*                                                                                                                                                                                         *Manually Cleaning an LED Strip\'s Solder Joints*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Make sure to avoid getting water sensors or components that can retain water. Certain components are sensitive to water, so you should avoid dunking those boards in water and be careful about getting these components wet. Here is a short list of components that should avoid contact with water. If water gets trapped in them and you power the board, it will probably damage the component.

- Character LCDs
- 7-Segment LED Displays
- Batteries
- GPS Modules
- Wireless Modules
- Barometric Pressure Sensors
- Slide Potentiometers
- Microphones
- Speakers
- Heart Rate Monitor ICs

When you are finished cleaning the board, you\'ll want to remove any excess water off the board. Compressed air works wonders so that you do not have to wait for it to evaporate. You can also paper towels to dry a board but it may leave pieces of lint behind. Thus low-lint wipes to dry a board would be better. If you have a hot air gun, you can also use it to heat the board up. Just make sure to not melt anything on the board.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Compressed Air to Dry Board](https://cdn.sparkfun.com/r/400-400/assets/e/e/7/0/3/513e9a25ce395fe362000000.JPG)](https://cdn.sparkfun.com/assets/e/e/7/0/3/513e9a25ce395fe362000000.JPG)   [![Low Lint Wipes Drying a Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/2/How_to_solder_castallated_via_tutorial-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/2/How_to_solder_castallated_via_tutorial-30.jpg)
  *Compressed Air to Dry Board*                                                                                                                                                                *Low Lint Wipes Drying a Board*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It\'s not 100% necessary to clean your board, however, it will increase the life of your circuit tremendously. Additionally, data sent through serial will be reliable when the board is clean. For more information on PCB cleaning, click below.

[Electronics Assembly: Washing](https://learn.sparkfun.com/tutorials/electronics-assembly/washing)

### Testing and Troubleshooting Solder Joints

Once you are done cleaning, feel free to check your solder joints with a [multimeter set to continuity mode](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter#continuity) as stated earlier. This is useful if you run into problems and need to check if a pin is soldered correctly to a board. For more information, check out our tutorial on how to use a multimeter.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

January 9, 2015

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

Looking for troubleshooting tips? Check out the [hardware checklist](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips#hardware-checks) in our tutorial for more information!

[](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips)

### SparkFun Troubleshooting Tips 

October 19, 2017

Not working as expected? In this tutorial, we will be exploring a few general troubleshooting tips and possible solutions that frequently come up with SparkFun\'s Technical Support.

## Interested in learning more foundational topics?

See our **[Engineering Essentials](https://www.sparkfun.com/engineering_essentials)** page for a full list of cornerstone topics surrounding electrical engineering.

[Take me there!](https://www.sparkfun.com/engineering_essentials)

![](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/multimeter-300.png)