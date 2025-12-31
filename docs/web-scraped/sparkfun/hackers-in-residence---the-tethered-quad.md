# Source: https://learn.sparkfun.com/tutorials/hackers-in-residence---the-tethered-quad

## Getting Started

By: [Tara Tiger Brown](http://taratigerbrown.com/) and [Sean Bonner](http://seanbonner.com/) SparkFun Hackers-in-Residence

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/6/4/f/9/7/5239bbae757b7fb8118b456d.jpg)](https://cdn.sparkfun.com/assets/6/4/f/9/7/5239bbae757b7fb8118b456d.jpg)

**Important: Voiding Warranties**

This should go without saying, but by hacking these off the shelf devices you are voiding all warranties. This is important because if you kill your drone by cutting it up you have to know ahead of time that you won't be able to call anyone at the company to help you troubleshoot. Same goes for the Dropcam - it's intended for indoor use in a controlled environment not to be flown all over the place outside strapped to a drone. So just know going into this you are on your own.

**What You'll Need**

- Parrot AR Drone 2.0 Quadcopter @ \$299
- Dropcam WiFi HD Camera @ \$149 (use this option for wifi/live web streaming) or HackHD Camera @ \$160 (use this option to record to SD card and view later)
- Monoprice 50ft 14AWG Enhanced Loud Oxygen-Free Copper Speaker Wire Cable @ \$21
- 4 x Deans Connectors @ \$0.95 ea
- few small zip ties
- Power Supply (we used a power supply from a PC, which requires two 4 pin Molex Connectors @ \$0.95 each, but anything that supplies 12v at around/up to 8A should work.)
- 5v Power Regulator @ \$1.25 or 3.3v Power Regulator if using HackHD instead of Dropcam
- Heat Sync plus Mounting Parts (Screw, Nut, Locknut) @ \$0.95 ea
- Thermal Tape @ \$3.95
- Micro USB cable that you are willing to cut up (to power the Dropcam)

**Tools**

- Soldering Iron/Station - we prefer variable temp but there are lots of options that should work.
- Lead solder (easier to de-solder if you need to)
- Scissors
- Knife (xacto or similar)
- Wire Stripper
- Hot Glue Gun and Glue

**References**

- All project photos are [here](http://www.flickr.com/photos/tarabrown/sets/72157635189456634)
- Project Video #1 is [here](http://www.youtube.com/watch?v=9ez9qUD6pzc)
- Project Video #2 is [here](http://www.youtube.com/watch?v=7NcTuAtdn3c)

## Part 1 - Preppin\' the Parrot

**Prep Work**

- Setup Dropcam Account [here](http://support.dropcam.com/entries/21661697). Make sure it can connect properly and you can access it. Decide if you want the feed to be private or public.

- Install one of the Parrot AR Drone apps on your smartphone of choice. Ensure your drone works and you can fly it around. Say goodbye to all that mobility and fancy handling

**Part 1 - Parrot**

([Teardown reference on iFixit](http://www.ifixit.com/Teardown/Parrot+AR.Drone+Teardown/3984/1))

Take off the top hull (the piece with the blue and orange stickers). You won't need it and getting rid of it gives you more lift.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/7/f/b/b/5/5239bcc4757b7f4b118b456b.jpg)](https://cdn.sparkfun.com/assets/7/f/b/b/5/5239bcc4757b7f4b118b456b.jpg)

*Parrot without the hull and battery*

Peel off the plastic plate on the bottom of the drone from the back, but not all the way.

- You'll see that there's a rather large cavity in the drone, you'll be shoving your camera in there.

- Cut a circle hole in that plastic cover large enough for your camera lens to pop out, but small enough to hold the rest of the camera guts inside. Note that we didn't glue the dropcam into the hull, it's just kind of in there.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/e/9/c/9/5239bd37757b7fd44f8b4570.jpg)](https://cdn.sparkfun.com/assets/d/e/9/c/9/5239bd37757b7fd44f8b4570.jpg)

*Parrot with the Dropcam inside the hull and a piece cut out for the cable.*

Cut about a half inch notch in the side hull, to allow cables to get to your camera.

Mod the power connector to use Deans connectors - this way you'll be able to use the battery or the power tether.

Soldering to the Deans connectors can take some time and lots of heat, so be patient and persistent. We used a male (M) connector on the drone, however this is **very dangerous**. If the male leads come into contact with anything conductive, you can short that battery and cause a fire. Don\'t do what Donny Don\'t does, and always connect the famle end to any battery or other power source! Also, be sure to not solder on two of the same ends. Nothing worse than finishing up and finding both ends of the wire you are trying to connect are female.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/a/5/a/1/0/5239be3d757b7f97108b456d.jpg)](https://cdn.sparkfun.com/assets/a/5/a/1/0/5239be3d757b7f97108b456d.jpg)

*Parrot power connector modded with the Dean's connector*

## Part 2 - Connector for Tethered Power

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/7/f/8/6/5239be89757b7f44118b456b.jpg)](https://cdn.sparkfun.com/assets/b/7/f/8/6/5239be89757b7f44118b456b.jpg)

*Connectors, voltage regulator and speaker wire ready to be soldered*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/6/c/6/3/5239beb8757b7f06118b4573.jpg)](https://cdn.sparkfun.com/assets/3/6/c/6/3/5239beb8757b7f06118b4573.jpg)

*Connectors soldered*

This is the piece that will connect your Parrot and Cam to the single line of power running up the tether.

Remember what we said earlier about the Deans connectors, make sure you keep that in mind here.

**Make sure you have:**

- Deans connector to connect to power connector on the Parrot (F)
- Deans connector to connect to the speaker wire/power cable (M)
- Power Regulator
- Heatsink
- Speaker wire - Cut two lengths - 6" and 4" should be good
- Mini USB - Cut at about 5"

See photos 4a/b for clear explanation, but the flow here will be from the power cord to split (from M Deans connector) with A side (6" wire) going to the Parrot (F Deans Connector), and B side (4" wire) going to the power regulator then mini USB to the cam.

Remember to watch polarity when soldering! ProTip: Speaker wire usually has a marker/indicator to show the + line.

When soldering the Mini USB, you only need to solder the RED (power) and BLACK (ground) lines, since there's no data being transferred over that cable thanks to the built in wifi on the Dropcam, or SD card on the HackHD.

## Part 3 - Powerline (Tether)

With 18 AWG speaker wire we were able to get a tether of 10' and fly indefinitely. We tested 30' with 14 AWG and were able to stay in-flight for about 10 minutes. More testing to do!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/e/d/f/7/5239bf9d757b7fdc108b456c.jpg)](https://cdn.sparkfun.com/assets/0/e/d/f/7/5239bf9d757b7fdc108b456c.jpg)

*18-gauge speaker wire*

Create a 2nd short connector piece that has a (F) Deans connector on end, and an adapter to connect to whatever power source on the other. For our purposes that meant 2x Molex connectors to snap onto 2 power leads from the PC power source. You can use whatever you want here so long as enough voltage. The value to doing this is that you can keep changing the length of the tether without soldering new cables every time.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/3/6/c/6/3/5239beb8757b7f06118b4573.jpg)](https://cdn.sparkfun.com/assets/3/6/c/6/3/5239beb8757b7f06118b4573.jpg)

*Speaker wire, Molex and Dean's connectors*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/1/b/0/d/5239c028757b7fb2118b456e.jpg)](https://cdn.sparkfun.com/assets/2/1/b/0/d/5239c028757b7fb2118b456e.jpg)

*Soldered connector with hot glue*

Measure out length of 14 AWG speaker wire for tether, solder (F) Deans connector to one end (to connect to Parrot) and (M) Deans connector to the other (to connect to power).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/3/5/9/c/5239c543757b7f30118b456e.jpg)](https://cdn.sparkfun.com/assets/e/3/5/9/c/5239c543757b7f30118b456e.jpg)

*Computer power source with the new connector*

Remember to watch polarity when soldering!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/1/b/0/d/5239c028757b7fb2118b456e.jpg)](https://cdn.sparkfun.com/assets/2/1/b/0/d/5239c028757b7fb2118b456e.jpg)

*Sean soldering a Dean's connector and very frustrated!*