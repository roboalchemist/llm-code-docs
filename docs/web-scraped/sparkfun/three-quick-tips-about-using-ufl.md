# Source: https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl

## Introduction

Since the number of SparkFun products with wireless or radio-frequency (RF) applications continues to increase we thought it would be helpful to make a crash course in one of the most ubiquitous players: the U.FL connector.

U.FL and the host of compatible connectors (like I-PEX, IPX, or UMCC) are all designed to allow attachment of small [coaxial cables](https://en.wikipedia.org/wiki/Coaxial_cable) that are preferable in wireless applications because of the shielding that the outer conductor provides. We use these connectors because they are small and inexpensive and because the smaller coaxial cables used with them are much easier to deal with. They are, however, a little bit harder to use and more fragile than their larger step-cousin (the [SMA connector](https://en.wikipedia.org/wiki/SMA_connector)) so it doesn\'t hurt to get a quick primer on how to use them.

This photo shows off both the male and female ends of a U.FL connector. On the left and attached to the cable is the female side while the male side is soldered to the board. (By the way, a connector\'s gender is always determined by the gender of the electrical contacts rather than the gender of plastic shrouds or other extraneous materials).

![Male and Female U.FL Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/MandWman.jpg)

In the hands of an eager inventor, exposed U.FLs get plugged/unplugged much more often than those that live deep inside a consumer\'s cell phone. A [Hirose datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/UFL_dat.pdf) shows that they only bothered to test repetitive use to 30 cycles, so follow these tips to keep your connectors working well for as long as possible!

## Connect

Caring for your U.FL connector is all about keeping that shiny electrical contact pristine and contacting! Grime, oxidation, and mountain dew will increase the impedance to/from the antenna and will reduce range. Bent contacts won\'t let any of the electric pixies through at all and those \"it works if I hold it just right\" problems are definitely the worst to debug!

![Crooked Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/Crooked.jpg)

When connecting the parts of the U.FL, first make sure your finger is relatively clean. To avoid putting pressure on the connection, pinch the cable one or two cm from the end and try to align it so that the female connector rests evenly across the surface of the male connector. You can then lightly put your finger on top of the stacked connectors \-- if it feels like your elementary school\'s old see-saw then try again, you want this to be stable. Also be sure that the two connectors are centered on one another left-to-right and up-to-down when you look at the connector from above the board.

[![Finger gently holding the connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/PushDown.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/PushDown.jpg)

If everything is good to go, use the very center of your finger to press firmly down - you\'ll feel a satisfying \"lock sensation\" as the datasheet puts it! (P.S. I had to move my finger off to the side so that you could see the connector in there, but you should really make an effort to push down right in the center of the connector)

The end result should look like this very happy ESP32 LoRa 1-Channel Gateway:

![Happily connected U.FL](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/ConnectedHappy.jpg)

## Protect

You can kind of think of the outside gripping portion of the female U.FL connector as being made out of dragonfly wings - very pretty to look at but also fragile. Putting unnecessary forces on them, for example a torque from pulling the cable in a funky way, could cause them to bend away from the male side of the connector and no longer make a reliable connection. Keeping this from happening should also be a priority when moving a project or creating a final installation.

![Torquing a U.FL Connection. No!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/BadJibesNO.jpg)

Preventing this weird torque is called ***strain relief*** and there are a couple ways to do it:

- Tape down the cable
- Put the cable through a strain-relief hole on the board (if applicable)
- Glue down the cable
- Or think of something else as long as it relieves any forces that might be accidentally applied to the cable

With any of the strain relief methods you should allow the cable to bend naturally to the securing location so as not to transmit any forces or torques to the connector. The ESP32 Gateway has a really convenient channel right below the ESP32 module that you can use to make a *tape tent.* This keeps the connection nice and secure without having to press down on the cable at all!

![Protected U.FL Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/StrainTape.jpg)

If there is a through hole nearby that is not being used and wide enough, you can also thread the u.FL connector before connecting. Below is an example of threading the u.FL cable through a mounting hole before being attached to NEO-M9U GPS board. Feel free to add additional strain relief using hot glue or tape against the board to reduce the amount of forces on the small connector.

[![u.FL connector Threaded Through Mounting Hole.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/6/SparkFun_GPS_Untethered_Dead_Reckoning_NEO-M8U_uFL.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/6/SparkFun_GPS_Untethered_Dead_Reckoning_NEO-M8U_uFL.jpg)

## Disconnect

Inevitably you will want to switch out your lunchbox radio kit antenna for something with a little more pizazz (who doesn\'t want a Yagi\...) Though tempting (and definitely easy) to just rip the cable off like a band-aid we highly recommend you do not do this. Remember the dragonfly wings? Yup, those outside connectors could be bent enough to make a loose connection or the center pin of the male connector could be bend to the side making it hard to connect the next time. Or worse, the connector rips off the PCB!

There is actually a \'specialized\' tool to disconnect these! Different manufacturers have different shaped tools. We will go over some of these specialized tools below and how to use them.

If you have the [U.FL push/pull tool](https://www.sparkfun.com/products/20687), the tool includes teeth that hold onto the U.FL connector. This can be used to help push in or pull out the connector. We found that it was more useful to use it to pull out the U.FL connector from the board.

[![U.FL Push/Pull Tool](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/5/3/0/TOL-20687_IPEX_Tool_01.jpg)](https://www.sparkfun.com/u-fl-push-pull-tool.html)

### [U.FL Push/Pull Tool](https://www.sparkfun.com/u-fl-push-pull-tool.html) 

[ TOL-20687 ]

This tool is used for connecting or the disconnecting of a U.FL mating condition.

[ [\$23.95] ]

With the tool, slide the end with the teeth labeled around the U.FL connector. Pull the U.FL connector up and away from the board. You will want to avoid pulling the U.FL connector at an angle like a crowbar as this can potentially bend the connector.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![U.FL Tool Sliding Around U.FL Connector](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_uFL_IPEX_Tool_Slide_In.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_uFL_IPEX_Tool_Slide_In.jpg)   [![U.FL Connector Removed with Tool](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_uFL_IPEX_Tool_Holding_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_uFL_IPEX_Tool_Holding_Connector.jpg)   [![U.FL Connector Removed with Tool](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_IPEX_Tool_uFL_Connector_removed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TOL-20687_IPEX_Tool_uFL_Connector_removed.jpg)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** If there are components around the U.FL connector, you may need to rotate the cable around when sliding the U.FL tool around the U.FL connector.

If you have the [U.FL extraction tool](https://www.sparkfun.com/products/20687), the tool includes teeth to hold onto the U.FL connector only from the bottom. Compared to the other U.FL tool shown above, this can only be used to help pull out the connector. The teeth are not as thick so it can slide underneath the U.FL connector better when there are a lot more SMD components in the vicinity but it does not grip onto the U.FL connector as well as well as the other tool.

[![U.FL Removal Tool](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/6/3/19929-U.FL_Removal___Insertion_Tool-01.jpg)](https://www.sparkfun.com/u-fl-removal-tool.html)

### [U.FL Removal Tool](https://www.sparkfun.com/u-fl-removal-tool.html) 

[ TOL-19929 ]

This tool is used for extraction from a U.FL mating condition.

**Retired**

[ ![U.FL Plug Extraction Tool with KeyChain](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/8/2/7/20060-U.FL_Plug_Extraction_Tool_with_KeyChain.jpeg) ]

### U.FL Plug Extraction Tool with KeyChain 

[ TOL-20060 ]

This tool is used for extraction from a U.FL mating condition.

**Retired**

With the tool, slide the end with the two teeth labeled as \"U.FL\" around the U.FL connector. Pull the U.FL connector up and away from the board. You will want to avoid pulling the u.FL connector at an angle like a crowbar as this can potentially bend the connector.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![U.FL Tool under U.FL Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/U.FL_Removal_Tool_Slide_Under_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/U.FL_Removal_Tool_Slide_Under_Connector.jpg)   [![U.FL Connector Removed with Tool](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/U.FL_Removal_Tool_Pull_Up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/U.FL_Removal_Tool_Pull_Up.jpg)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Don\'t have a specialized tool to remove the U.FL? There are alternatives which include:

- A pair of tweezers
- Right angle cutters (whoa there, not too hard!)
- A flat \'spudger\' like tool
- Your imagination (well not directly\...)

Here\'s a before and after image of the tweezers technique:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Tweezers Under u.FL connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/Tweezers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/Tweezers.jpg)   [![Tweezers removing u.FL connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/TweezersLifted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/4/5/TweezersLifted.jpg)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Just like when you connected the two halves the name of the game is \"torque is lava,\" meaning of course that you don\'t want to twist the connector as it is coming off. Get a firm (but not crushing) grip on the female connector just below the thick top part (there will be a nice little lip to hold on to as you pull up). Then all you need to do is pull away from the board. When the female part is separate it no longer has the male part to keep the outside contacts from bending inward so be gentle.

Really any tool that can catch the lip underneath the female connector will do the trick. When using these right-angle clippers I just made sure that the thick part of my palm was keeping them open so as not to crush the connector. Then I used my thumb as a fulcrum (the further from the connector the better for a straighter pull) and popped the two halves apart.

![Using right-angle clippers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/Clippers.jpg)

In case you don\'t have a two-sided tool you could also try the \"spudger\" technique. It\'s a little harder to get just right but it is also possible to minimize torque on the connector this way. To do it put something thin an rigid underneath the cable and get the tip right up against the barrel of the connector. Now hold down the cable onto the flat thing as close to the connector as possible. If you can, tug the cable directly away from the connector a little (this helps counteract the torque you generate from pulling up from one side only). Finally use your flat rigid piece to lift the connector up and away.

![using a board as a spudger](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/4/5/Spudger.jpg)

Now you know the basics of how to connect, protect, and disconnect a U.FL connector. Go rule the airwaves!