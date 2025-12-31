# Source: https://learn.sparkfun.com/tutorials/how-chip-on-boards-are-made

## Victor DMM

On our 2014 China trip we got the opportunity to visit with Victor, one of our digital multimeter (DMM) manufacturers. We have toured their factory before but this tour was special for two reasons:

[![Yellow DMM from Victor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_1_7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_1_7.jpg)

1.  After the [seizure of yellow multimeters](https://www.sparkfun.com/news/1428), it was important to talk with Victor to figure out our other color options (you can see find our new [gray DMMs here!](https://www.sparkfun.com/products/12966)).
2.  While taking the second tour, I asked how the COB, or chip-on-board, manufacturing process happened. I expected it to be outsourced to a different facility but was surprised to hear it was done on a different floor of the same building. We excitedly asked to see it and our tour guide was nice enough to show us how it\'s done!

[![Workers putting together DMMs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_2.jpg)

Here you can see workers putting the through hole components in to the main PCB of a multimeter. The black blob is the main IC of the device. Many devices use COB or chip-on-board to reduce the cost of components and manufacturing.

## COB Manufacturing

[![Main ICs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_3.jpg)

Shown above is a tray of controller silicon dies that serve as the brain of the multimeter. These ICs are made by a different company and are ordered with features that are desired in the overall feature set of the DMM. While I shouldn\'t have been surprised, it was interesting to think about the fact that there are companies setup to create nothing but DMM controller ICs. What I now understand is that few multimeter companies own the entire tool-chain to create a DMM. Instead, there are companies that specialize in small cottage industries: manufacturing the DMM displays, the batteries, the control ICs, and assembly of the parts into a final DMM.

[![Glue dot on PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_4.jpg)

Very similar to [how LEDs are made](https://learn.sparkfun.com/tutorials/how-leds-are-made), the first step is to glue the silicon die to the PCB. I\'m not entirely sure if the adhesive is conductive or not, but, judging by the exposed pad, it probably is.

[![Silicon die on PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_5.jpg)

With a pair of tweezers the dies are placed by hand(!). The adhesive sets within 5 minutes. This was another moment that caught me off guard: I assumed COB required a clean room with precision tools and ultra-accurate placement. It turns out, just like SMD soldering in a hot plate; you can have a lot of variance and still have a fully functional board.

ReplaceMeOpen

ReplaceMeClose

[Chip On Board Bonding](http://vimeo.com/95597432)

The PCB is then inserted into an amazing automated wire bonding machine that bonds a very thin wire from the IC to the PCB. You can see the operator has to tell the visual recognition system a few alignment spots once in awhile, but in general, the machine quickly solders all the connections.

From one of our readers *manton*:

> It would be unlikely that the wire bonding process is done by soldering the wires. Usually this is done using [thermosonic bonding](http://en.wikipedia.org/wiki/Thermosonic_bonding), which uses a combination of heat, pressure, and ultrasonic vibrations to bond the wires.

Very good point! Thanks Manton. I thought it was soldering because that\'s what I know but this is thermosonic bonding.

ReplaceMeOpen

ReplaceMeClose

[COB Wire Bonding](http://vimeo.com/95597433)

In the video above, you can see that the machine requires some operator input to bond the last connection, completes it, and the board is done. You also get a sense for how rough the boards can be handled without damaging the connections. I expected the hair like connections to be quite fragile, but, instead, the boards can be handled regularly. This is very similar to how liquid solder paste [holds SMD components solidly in place](https://learn.sparkfun.com/tutorials/electronics-assembly/reflow) before they enter the reflow oven.

[![IC with hair like wire connections](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_6.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_6.jpg)

Forty one connections later, and the die is all connected up. As you can see, the small theta rotation of the IC doesn\'t make much of a difference.

[![Potting compound being squirted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_7.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_7.jpg)

The next step is to squirt a small dab of potting compound over the entire structure. This material electrically and physically protects the die and wire bonds from damage.

The viscosity of the compound must be tightly controlled to prevent the hairs from bending over and connecting with neighboring wires.

[![Black blob of compound](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/4/DMM_COB_8.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/DMM_COB_8.jpg)

The liquid compound is then cured in an oven for four hours. Once complete the boards are tested and continue down the process of becoming a multimeter.

[![Back of LCD showing two black COB blobs](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/4/COB_Example.jpg)](https://www.sparkfun.com/products/709)

Now, whenever you see those black blobs on an electronic device, such as the ones on our [16x2 basic LCD](https://www.sparkfun.com/products/709), you\'ll know how they are made!