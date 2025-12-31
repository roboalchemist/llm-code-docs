# Source: https://learn.sparkfun.com/tutorials/nuclear-battery-assembly-guide

## A Healthy Green Glow

[![](https://cdn.sparkfun.com/assets/custom_pages/2/6/9/sparkx-logo.png)](https://www.sparkfun.com/sparkx)

\
**Experimental Products:** [SparkX products](https://www.sparkfun.com/sparkx) are rapidly produced to bring you the most cutting edge technology as it becomes available. These products are tested but come with no guarantees. Live technical support is not available for SparkX products.

We were inspired to develop the [Nuclear Battery Kit](https://www.sparkfun.com/products/14773) after finding [some very cool folks](https://hackaday.com/2016/12/01/make-your-own-nuclear-battery/) making their very own homemade nuclear batteries. The following assembly guide will take you through the construction of this project step by step and even discuss some of the chemistry that makes nuclear batteries possible!

[![Nuclear Battery Kit (Bring Your Own Tritium)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/2/1/14773-Nuclear_Battery_Kit-01.jpg)](https://www.sparkfun.com/products/14773)

### [Nuclear Battery Kit (Bring Your Own Tritium)](https://www.sparkfun.com/products/14773) 

[ SPX-14773 ]

After we caught sight of \[some very cool folks\](https://hackaday.com/2016/12/01/make-your-own-nuclear-battery/) online making...

**Retired**

These devices are actually known as \"*Radioisotope Photovoltaic Generators*\" or \"*Photobetavoltaic Generators*,\" and they\'re a pretty clever design: glowing glass pills filled with tritium gas and coated in a phosphorescent material are sandwiched between two photovoltaic cells. The beta radiation emitted by the tritium is blocked by the glass walls of the pill, but they cause the phosphorescent coating to glow. This light has no trouble passing through the glass and lands on the photovoltaic cells where it produces a small amount of electricity!

[![a commercially available betavoltaic generator, a 28-pin DIP package with a white body and a prominent radiation warning symbol](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/28-Pin-CERDIP-2-400x300.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/28-Pin-CERDIP-2-400x300.jpg)

*Image courtesy of [citylabs.net](http://citylabs.net)*

Commercial tritium batteries --- like those produced by [City Labs](http://citylabs.net/products/) --- cut out the middleman by using betavoltaic (as opposed to photovoltaic) cells in direct contact with tritium gas. Those commercial devices are more rugged and efficient, but come with a very large price tag (thousands of USD per unit).

[![A number of tiny glass tubes are shown sandwiched between two small solar cells. The assembly is held together with clear packaging tape.](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/7/8/8/thu1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/thu1.png)

*Image courtesy of [NurdRage\'s Video](https://www.youtube.com/watch?v=KKdzhPiOqqg)*

On the other hand, homemade devices constructed using the packing tape sandwich method are as cheap as it gets, but aren\'t particularly sturdy.

This kit provides a good compromise between price and quality of construction. We\'ve designed carrier boards for both of the photovoltaic cells which we supply pre-soldered and fixed to the boards with chipbonder. We have also designed and cast custom silicone rubber grommets which cushion the tritium vials between the two photovoltaic cells, preventing the cells from getting scratched or chipped and --- most importantly --- the vials from getting broken. The carrier boards also allow you to choose whether the photovoltaic cells are wired in series or parallel and provide you with breadboard compatible pin spacing for the battery terminals.

### Required Materials

Now that we\'ve explained the science behind this kit, it\'s time to start on the construction. To create nuclear batteries of your own, you will need the following materials in addition to the tritium that must be purchased elsewhere:

[![Breadboard - Mini Modular (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/3/0/12047-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-black.html)

### [Breadboard - Mini Modular (Black)](https://www.sparkfun.com/breadboard-mini-modular-black.html) 

[ PRT-12047 ]

This black Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to b...

[ [\$4.60] ]

[![Nuclear Battery Kit (Bring Your Own Tritium)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/2/1/14773-Nuclear_Battery_Kit-01.jpg)](https://www.sparkfun.com/products/14773)

### [Nuclear Battery Kit (Bring Your Own Tritium)](https://www.sparkfun.com/products/14773) 

[ SPX-14773 ]

After we caught sight of \[some very cool folks\](https://hackaday.com/2016/12/01/make-your-own-nuclear-battery/) online making...

**Retired**

The breadboard is not needed for this project but it will simplify the required soldering. For information on finding and purchasing tritium vials, please reference the next section \"[A Brief Word on Tritium Gas Lights](https://learn.sparkfun.com/tutorials/nuclear-battery-assembly-guide#a-brief-word-on-tritium-gas-lights).\" You will need at least ten vials for this guide.

### Tools

You will also need some basic soldering equipment and a couple simple tools. The following products are a great starting point:

[![Tweezers - Curved (ESD Safe)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/4/5/10602-01.jpg)](https://www.sparkfun.com/tweezers-curved-esd-safe.html)

### [Tweezers - Curved (ESD Safe)](https://www.sparkfun.com/tweezers-curved-esd-safe.html) 

[ TOL-10602 ]

You can tell by our large assortment of tweezers that we here at SparkFun are way into picking up tiny things. To make sure w...

[ [\$4.75] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

Please note the tweezers and pliers are not required but will make the construction process easier. In addition, a soft cloth is recommended for cleaning various components of the kit and masking tape may be useful in keeping parts of the battery stationary during the assembly.

### Suggested Reading

If you\'re new to soldering or want to brush up on your soldering skills before beginning this project, please check out the following tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

## A Brief Word on Tritium Gas Lights

Before you get started, you\'ll need to get your hands on some 2x12mm Tritium glow vials.

[![Several glowing green tritium tubes on a black background](https://cdn.sparkfun.com/r/550-550/assets/learn_tutorials/7/8/8/14773-Nuclear_Battery_Kit-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/14773-Nuclear_Battery_Kit-04.jpg)

Remember that you will need 10x of them. These are sold under various tradenames such as:

- Mixglo
- DaxLight
- BETALight
- Gaseous Tritium Light Source (GTLS)
- Tritium Glow Tube
- Tritium Gas Tube
- Tritium Glow Vial

They\'re easily found on sites such as [ebay](https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=2x12+tritium&_sacat=0), [banggood](https://www.banggood.com/Wholesale-Tritium-Gadgets-c-4596.html), [aliexpress](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20180608115530&SearchText=tritium+2x12), etc. as well as certain [specialty websites](https://www.mixglo.com/store/p4/T2b_2x12mm_Vials.html). Although their sale is regulated in many countries --- and you should be aware of your local laws before attempting to procure any radioisotope --- we didn\'t have any trouble mail-ordering a small number of them in the US.

These Tritium Glow Tubes are perfectly safe to handle as the beta radiation generated from the Tritium decay cannot pass through the glass wall of the vial. Incidentally, the collision of the beta particles with the glass *does* produce a very tiny amount of x-rays, but not enough to harm anything. The only danger associated with Tritium gas is if it is inhaled, injected, or otherwise inserted into the body, which can only happen if you break the glass vial. If a vial *does* break, evacuate the room for a while to allow the gas to dissipate. Tritium occurs naturally in very small quantities and has a very short half-life compared with other glow products (such as radium) so breaking a glow vial will not turn your home into a superfund site.

If you\'d like to learn more about Tritium Glow Tubes, you can check out [this excellent blog post](https://www.ablogtowatch.com/how-glow-dark-tritium-gas-tubes-made-mb-microtec/) on how they\'re made and how they\'re used in watchmaking!

## Some Assembly Required

### Hardware Overview

Before beginning the assembly, let\'s talk a little bit more about what\'s included in your [Nuclear Battery Kit](https://www.sparkfun.com/products/14773). Each kit includes the following:

- Top and Bottom PCB with Amorphous Silicon PV Cells. These will harness the energy produced from the tritium vials.

[![highlighting power and ground on the PCB board](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/7/8/8/PCB_detail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/PCB_detail.jpg)

*Boards labeled with headers corresponding to Power (+) and Ground (-)*

[![highlighting the PCB board](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/7/8/8/Battery_Mat_PCB_sized.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/Battery_Mat_PCB_sized.jpg)

- Two Silicone Rubber Gaskets. These will hold the vials in place and help keep them safe.

[![Highlight of rubber gaskets](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/7/8/8/Battery_Mat_silicone_sized.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/Battery_Mat_silicone_sized.jpg)

- Strip of Long Breakaway Headers. Just add some solder and these headers will bridge the two boards!

[![Highlight of breakaway headers](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/7/8/8/Battery_Mat_head_sized.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/Battery_Mat_head_sized.jpg)

### Step 1 - Gather Materials

Grab ten 2x12mm tritium gas tubes, the contents of your kit, the various tools we talked about earlier, and a breadboard (optional). And don\'t forget about the soft cloth! It\'s not a bad idea to polish the PV cells and maybe your tritium vials just to remove any smudges or dust that could effect the efficiency of the battery.

[![All of the parts of the kit laid out on a gray background. Two white PCBs with PV cells centered on each, a pair of beige rectangular silicone gaskets, a strip of long pin headers, and a small pile of tritium glow tubes.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/Battery_Mat_sized.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/Battery_Mat_sized.jpg)

### Step 2 - Attach Headers to the Top PCB

Use your pliers to break off a few individual headers. You really just need four of them, but they sometimes get bent or don\'t break off cleanly so we tossed in a bunch just to be safe.

[![A hand holds a strip of pin headers while snipping one away using wire snips](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/clip_headers_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/clip_headers_crop.jpg)

This next part is easier if you have a breadboard to hold the pins in place while you work, but you can manage without one. In the picture below, I\'ve stuck the pin headers into my breadboard long-side-down in preparation to solder them to my top PCB. You can tell which one is the top because it will have the SparkX logo as well as some solder jumpers on the side opposite the PV cell.

[![Four separate pin headers protrude from a small black breadboard.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/breadboard_setup_high.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/breadboard_setup_high.jpg)

Now simply solder each pin into place with a generous solder joint:

[![A hand holds a soldering iron in position to solder the pins in place on a white PCB](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/solder1_scale.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/solder1_scale.jpg)

You can now remove your soldered assembly and flip it upside-down in preparation for the next step.

### Step 3 - Make the Stack

Now you need to grab one of the silicone rubber gaskets. It doesn\'t matter which one because they\'re identical. Place it with the flat side down and the pips facing up in the area marked \"gasket\" on the PCB.

[![The white PCB now has a beige rubber gasket on top.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/stack_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/stack_crop.jpg)

This step can be a little finicky, but take your time and use the tweezers if you need to. Place each of the 10x Tritium gas tubes into the rubber gasket. It helps to start at one end and move across. Place one end of each tube gently into a ridge on one side of the gasket and then gently press down until the other side slides into its corresponding ridge.

[![Tweezers being used to place Tritium gas tubes into grooves in the rubber gasket.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/IMG_20180608_123839.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/IMG_20180608_123839.jpg)

After all of the tubes are in place, you can press on them gently with a flat object to make sure they\'re seated. They should look like this:

[![a row of glass vials rest on top of the rubber gasket, suspended above the PV cell underneath.](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/vials_done_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/vials_done_crop.jpg)

Now cap the tubes with the other rubber gasket, being sure to align the holes and pips so that they mate together.

[![A second rubber gasket has been added to the stack.](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/more_silicone_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/more_silicone_crop.jpg)

Finally, you can slide the bottom PCB onto the stack. **Careful!** Make sure that the board is oriented correctly. The \"**NC**,\" \"**+**,\" and \"**\--**\" pin labels on both boards should line up!

[![The second white PCB has been added to the stack](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/top_board_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/top_board_crop.jpg)

### Step 4 - Solder It All Together

For this step, you\'ll want to apply some clamping force to the stack. Too much force will deform the rubber gaskets, causing the tubes to rattle loose in the assembly. In this case, you will need to re-build your stack. A small weight or a very weak binder clip should work, but I find masking tape is also acceptable.

[![The PCB on the top of the stack has been taped down to the workbench using masking tape to apply clamping force to the stack.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/tape_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/tape_crop.jpg)

Now solder each of the four pins, these provide both the electrical connection between the PV cells and the mechanical connection which holds the generator together. **DO NOT** clip the headers after soldering as they will act as the leads for your battery.

[![A hand holds a soldering iron in position to solder the pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/solder2_crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/solder2_crop.jpg)

Once you\'re finished soldering, your battery is complete!

[![The completed battery stands upright on its pin headers.](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/8/8/done_scale.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/done_scale.jpg)

## A Little Bit of Power

So how much power does it make? Not much. The best measurement we were able to make (using the method outlined by NurdRage) suggests that the maximum power point of this arrangement is 25nW, if you can build a circuit that loads it properly (between 20 and 30nA at about 0.6v).

[![a graph shows the calculated maximum power point of the PV cells in this configuration as described below.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/8/chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/chart.png)

*Having a hard time seeing the graph? Click on the image for a closer look.*

Further experiments show that the battery will --- given enough time --- charge a capacitor to a voltage of 1.5 volts. Using this battery to do any work will likely involve a clever energy harvesting circuit, but keep in mind that this tiny amount of power will continue to flow for about 20 years --- the half life of Tritium being 12 years.

[![This image is an invisible square but it\'s here so that I can ask you a favor if you\'re enjoying this tutorial using a screen reader. I\'m trying to improve our site\'s accessibility, so I would love to hear your feedback about the image alt tags in this article. You can email me at nick.poole@sparkfun.com and please put the phrase \"image tags\" in the subject line. Thank you so much. Happy Hacking!](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/FFFFFF-0.0.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/8/FFFFFF-0.0.png)