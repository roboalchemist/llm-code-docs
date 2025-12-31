# Source: https://learn.adafruit.com/timesquare-watch-kit/kit-assembly.md

# TIMESQUARE Watch Kit

## Kit Assembly

First up, check that you have all the electronic parts laid out on your table and ready for soldering!

![adafruit_products_parst.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/749/medium640/adafruit_products_parst.jpg?1396786687)

Start by placing the PCB in a vise to keep it steady. We'll be soldering parts on TOP, where the silkscreen shows the component placing. The first part we'll place is the 10K resistor. This resistor is marked **brown black orange gold**. (It's also the only single resistor of that color)  
  
Bend the resistor into a staple and slip the wire leads into the two holes so that the resistor covers the outline labeled **R10** in the bottom right corner shown here

![adafruit_products_10kplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/750/medium640/adafruit_products_10kplace.jpg?1396786691)

Bend the wire leads out so the resistor sits flat against the PCB. Then you can flip it over and it wont fall out!

![adafruit_products_10kflip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/751/medium640/adafruit_products_10kflip.jpg?1396786703)

With your soldering iron heated up and ready, solder in both leads of the resistor. To do this, heat up the round ring pad and the wire lead at the same time for 2 or 3 seconds, then dip the end of the solder into the heated joint to melt it in.

Then remove the solder and the soldering iron.

  
![adafruit_products_10ksolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/752/medium640/adafruit_products_10ksolder.jpg?1396786713)

![adafruit_products_10ksolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/753/medium640/adafruit_products_10ksolder2.jpg?1396786723)

![adafruit_products_10ksoldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/756/medium640/adafruit_products_10ksoldered.jpg?1396786755)

Once the soldering is complete, we can clean up by clipping the leads of the resistor. This keeps them from shorting to something else. Use diagonal or flush cutters to clip the wires right above where the solder joint ends.  
![adafruit_products_10kclip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/754/medium640/adafruit_products_10kclip.jpg?1396786733)

![adafruit_products_10kclipping.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/755/medium640/adafruit_products_10kclipping.jpg?1396786744)

Next we'll solder in the yellow blobby 0.1uF capacitor. This capacitor is part of the reset circuitry as well, and is used to help reset the chip when we want to reprogram it.  
  
Ceramic capacitors, like resistors, are not directional. So put it in any way it fits, next to the **R10** resistor, so its surrounded by the **C1** outline  
  
Then bend the leads and flip over the board.

![adafruit_products_capplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/758/medium640/adafruit_products_capplace.jpg?1396786766)

![adafruit_products_capflip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/759/medium640/adafruit_products_capflip.jpg?1396786778)

Solder in the capacitor's two legs just like you did with the resistor

![adafruit_products_capsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/760/medium640/adafruit_products_capsolder.jpg?1396786789)

![adafruit_products_capsolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/761/medium640/adafruit_products_capsolder2.jpg?1396786800)

You did great with the first two parts, now we will solder in the remaining resistors **R1-R8**. These resistors are the LED 'choke' resistors - they keep the LED matrix's light even and avoids having too much current draw that would kill the battery off!  
  
All the resistors are the same 47 ohm value - **Yellow Violet Black Gold**  
  
Here we placed and soldered all 8 at once but you can go one at a time if you want to take it a little slower!

![adafruit_products_resplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/765/medium640/adafruit_products_resplace.jpg?1396786837)

![adafruit_products_resflip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/766/medium640/adafruit_products_resflip.jpg?1396786848)

Solder in all the resistors, either one at a time or all 8 at once! Make sure you don't forget any solder points, though.

![adafruit_products_ressolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/767/medium640/adafruit_products_ressolder.jpg?1396786859)

![adafruit_products_ressolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/768/medium640/adafruit_products_ressolder2.jpg?1396786870)

![adafruit_products_ressolder3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/769/medium640/adafruit_products_ressolder3.jpg?1396786881)

![adafruit_products_ressoldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/773/medium640/adafruit_products_ressoldered.jpg?1396786921)

Next clip all the leads!

![adafruit_products_resclip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/770/medium640/adafruit_products_resclip.jpg?1396786891)

![adafruit_products_resclip2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/771/medium640/adafruit_products_resclip2.jpg?1396786901)

![adafruit_products_resclipped.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/772/medium640/adafruit_products_resclipped.jpg?1396786912)

Next up we will put in the first chip. This chip has 8 legs and has the label **DS1337** on top. Make sure you've got the right label on the chip.  
  
This chip is the "real time clock" - the timekeeper. It is a ultra-lo-power circuit, whose only task is to keep track of the time, so its pretty good at it. It's possible to have the main microcontroller chip (the next one we'll do) keep track of the time, but its not as good at it (both in terms of power and precision) so we splurged on having a seperate RTC  
  
The important thing about chips is that they are not like resistors and capacitors in that they **can't** be placed 'either way'. It **must** be placed the right way or the chip wont work. Look for the end of the chip with a notch and a dot. These must match up the silkscreened image on the PCB so make sure the notches line up.

![adafruit_products_rtcplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/775/medium640/adafruit_products_rtcplace.jpg?1396786943)

![adafruit_products_rtflip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/780/medium640/adafruit_products_rtflip.jpg?1396786989)

Solder all eight pins of the RTC  
  
No need to clip them after they're done

![adafruit_products_rtcsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/778/medium640/adafruit_products_rtcsolder.jpg?1396786971)

![adafruit_products_rtcsolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/779/medium640/adafruit_products_rtcsolder2.jpg?1396786981)

Next we'll do the big microcontroller chip. This chip is the brains, it does all of the displaying and button handling. Most of the time its 'sleeping' and when you press a button it wakes up and shows the time. It has a lot of pins because the matrix requires 16 pins to draw, and then you need some more pins for buttons, the RTC chip, reprogramming, etc.  
  
The chip is an **ATMEGA328P** that has been pre-programmed at the Adafruit factory to have an Arduino-compatible bootloader and our default watch display code.  
  
To begin, flatten the pins to make them more parallel || shaped intsead of A shaped. Hold the chip in your hand and press all the pins one side at a time against a flat table.  
  
Then when you press it into the holes, make sure each pin has made it into a matching hole, and its sitting flat against the PCB  
  
Like the RTC, this chip **must** be put in the right way. The notch on the chip must go on the left side as in these photos. Check twice to make sure you have the chip in right!

![adafruit_products_chipplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/781/medium640/adafruit_products_chipplace.jpg?1396786997)

![adafruit_products_flatchips.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/782/medium640/adafruit_products_flatchips.jpg?1396787007)

Solder all 28 pins!  
  
No need to clip them after they're done

![adafruit_products_chipsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/783/medium640/adafruit_products_chipsolder.jpg?1396787018)

![adafruit_products_chipsolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/784/medium640/adafruit_products_chipsolder2.jpg?1396787030)

![adafruit_products_chipsolder3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/785/medium640/adafruit_products_chipsolder3.jpg?1396787039)

Next we'll place both the battery holder, and the timing crystal. The battery of course is how we power the watch, and this holder keeps it in place. The timing crystal is the "Quartz Crystal" in watches, that keeps time by resonating  
  
The battery holder does have a special way it must go, make sure you can slide the battery in by having the open side facing out  
  
The crystal can go in either way, its symmetric, like the resistors

![adafruit_products_batxtalplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/786/medium640/adafruit_products_batxtalplace.jpg?1396787051)

The battery holder will slip out if you flip over the board, so before flipping the board, solder one leg side from the top. The holder is a great heatsink so it may take a little longer than usual to solder in

![adafruit_products_battack.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/787/medium640/adafruit_products_battack.jpg?1396787062)

![adafruit_products_battacked.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/788/medium640/adafruit_products_battacked.jpg?1396787073)

Flip it over and solder in the other battery pin, then go back and do the first one.  
  
Also, solder and clip the two crystal pins

![adafruit_products_batsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/789/medium640/adafruit_products_batsolder.jpg?1396787083)

![adafruit_products_xtalsolder.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/790/medium640/adafruit_products_xtalsolder.jpg?1396787093)

![adafruit_products_xtalclip.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/791/medium640/adafruit_products_xtalclip.jpg?1396787099)

Lastly, place the two interface buttons. You'll use these to set the time, display the time, and change watch faces.  
  
Both go on either side of the board, and they'll snap in.  
  
Then flip the board over and solder in all 4 pins of each

![adafruit_products_buttonplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/792/medium640/adafruit_products_buttonplace.jpg?1396787110)

![adafruit_products_butsolder1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/793/medium640/adafruit_products_butsolder1.jpg?1396787120)

![adafruit_products_butsolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/794/medium640/adafruit_products_butsolder2.jpg?1396787129)

Danger: 

Finally, the fun part! The matrix!   
  
The LED matrix is what you'll be looking at - 64 individual LEDs in a plastic case.   
  
The Matrix is not symetric, it **must** go in the right way on the right side.   
Look for the writing on the side of the matrix, this side must go on the side of the PCB with a dot as you see here. Also the matrix goes on the OPPOSITE side of the other parts!  
  
Check that the 28-pin microcontroller pins aren't in the way of the matrix, it should sit nice and flat

![adafruit_products_matrixdot.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/803/medium640/adafruit_products_matrixdot.jpg?1396787220)

![adafruit_products_matrixplace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/808/medium640/adafruit_products_matrixplace.jpg?1396787270)

Now solder in all the pins of the matrix, you may have to angle the iron tip a bit to avoid burning other parts  
  
You can clip the leads but you don't have to (they're less long than the height of all the other parts!

![adafruit_products_matrixsolder1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/804/medium640/adafruit_products_matrixsolder1.jpg?1396787230)

![adafruit_products_matrixsolder2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/805/medium640/adafruit_products_matrixsolder2.jpg?1396787236)

![adafruit_products_matrixsolder3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/806/medium640/adafruit_products_matrixsolder3.jpg?1396787248)

![adafruit_products_matrixsoldered.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/807/medium640/adafruit_products_matrixsoldered.jpg?1396787259)

Get the remaining parts out of the kit - a 20mm coin battery, silicone band and optional clear plastic back

![adafruit_products_bandready.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/809/medium640/adafruit_products_bandready.jpg?1396787283)

Insert a 20mm (CR2032) coin cell battery so that the&nbsp; flat **+** side is facing up and the bumpy side is facing down into the PCB

![adafruit_products_battery.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/810/medium640/adafruit_products_battery.jpg?1396787296)

Place the clear back first into the band so it's at the bottom. Then stretch the band and scootch the assembly in, pulling the rubber to fit around!  
  
When you've got it all in, you may need to pull/press the band around the PCB to have the 'nubs' fit into the notches that are molded into the band

![adafruit_products_bandinsert1.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/811/medium640/adafruit_products_bandinsert1.jpg?1396787306)

![adafruit_products_bandinsert2.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/812/medium640/adafruit_products_bandinsert2.jpg?1396787313)

![adafruit_products_bandinsert3.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/813/medium640/adafruit_products_bandinsert3.jpg?1396787326)

![adafruit_products_bandpress.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/815/medium640/adafruit_products_bandpress.jpg?1396787347)

That's it! You can now continue on to set the time and/or adjust your fit

![adafruit_products_bandfit.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/816/medium640/adafruit_products_bandfit.jpg?1396787337)

![adafruit_products_clearback.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/817/medium640/adafruit_products_clearback.jpg?1396787360)

## ADJUSTING FIT
  
After you've assembled your watch there are a few ways to change the fit of the band around the PCB. First is trimming down the nubs on the PCB. These are there to help keep the board inside the rubber band. However, they may be long depending on your wrist size, and band (all the bands are slightly different)  
  
Simply trim them down a millimeter at a time to help avoid them from sticking out too much  
![adafruit_products_pcbtrim.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/818/medium640/adafruit_products_pcbtrim.jpg?1396787373)

![adafruit_products_pcbtrimmed.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/819/medium640/adafruit_products_pcbtrimmed.jpg?1396787380)

Another easy way to adjust the fit is to remove the plastic back - its not essential and for smaller wrists it may make the watch a little bulkier than desired.

![adafruit_products_blankback.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/820/medium640/adafruit_products_blankback.jpg?1396787392)

# 

## OTHER TWEAKS

_Kapton tape_ is a heat-resistant and electrically insulative&nbsp;tape that's used a lot in electronics. This isn’t included with the watch, but if you’ve been in this hobby for a while there’s a good chance you already have a roll handy. Wonderful stuff.

One or two&nbsp;layers of Kapton tape applied to the watch face make it less prone to washing out under bright light.&nbsp;The tape’s color is similar enough to the red LEDs that they shine through with little difficulty, while most ambient light is blocked.

_Rubylith film_ (from a decent old-school art supply store) would probably work as well, if not better.

![adafruit_products_kapton-watch.jpg](https://cdn-learn.adafruit.com/assets/assets/000/003/173/medium640/adafruit_products_kapton-watch.jpg?1396792843)

![adafruit_products_kapton-tape.jpg](https://cdn-learn.adafruit.com/assets/assets/000/003/174/medium640/adafruit_products_kapton-tape.jpg?1396792850)

- [Previous Page](https://learn.adafruit.com/timesquare-watch-kit/parts-list.md)
- [Next Page](https://learn.adafruit.com/timesquare-watch-kit/setting-the-time.md)

## Featured Products

### TIMESQUARE DIY Watch Kit - Red Display Matrix

[TIMESQUARE DIY Watch Kit - Red Display Matrix](https://www.adafruit.com/product/1106)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1106)
[Related Guides to the Product](https://learn.adafruit.com/products/1106/guides)
### TIMESQUARE DIY Watch Kit - Tangerine Display Matrix

[TIMESQUARE DIY Watch Kit - Tangerine Display Matrix](https://www.adafruit.com/product/1223)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1223)
[Related Guides to the Product](https://learn.adafruit.com/products/1223/guides)
### TIMESQUARE DIY Watch Kit - Lime Display Matrix

[TIMESQUARE DIY Watch Kit - Lime Display Matrix](https://www.adafruit.com/product/1224)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1224)
[Related Guides to the Product](https://learn.adafruit.com/products/1224/guides)
### TIMESQUARE DIY Watch Kit - Blue Display Matrix

[TIMESQUARE DIY Watch Kit - Blue Display Matrix](https://www.adafruit.com/product/1225)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1225)
[Related Guides to the Product](https://learn.adafruit.com/products/1225/guides)
### TIMESQUARE DIY Watch Kit - White Display Matrix

[TIMESQUARE DIY Watch Kit - White Display Matrix](https://www.adafruit.com/product/1226)
Show up stylish AND on time to any event with this awesome looking DIY watch. We have a few watch kits here at Adafruit but we finally have one that looks good and fits well, even for ladies and kids and others with smaller wrists and hands. Its got an 8x8 bit matrix display and a repurposed...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1226)
[Related Guides to the Product](https://learn.adafruit.com/products/1226/guides)
### TIMESQUARE silver parts bag

[TIMESQUARE silver parts bag](https://www.adafruit.com/product/1227)
No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1227)
[Related Guides to the Product](https://learn.adafruit.com/products/1227/guides)

## Related Guides

- [MicroLipo v2 Case](https://learn.adafruit.com/microlipo-case.md)
- [Adafruit DotStar FeatherWing](https://learn.adafruit.com/adafruit-dotstar-featherwing-adafruit.md)
- [The Pixif](https://learn.adafruit.com/the-pixif.md)
- [Adafruit VL53L0X Time of Flight Micro-LIDAR Distance Sensor Breakout](https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout.md)
- [Adafruit MENTA Kit](https://learn.adafruit.com/adafruit-menta-kit-mint-tin-arduino-compatible.md)
- [Adafruit RGB Matrix Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi.md)
- [Raspberry Pi Care and Troubleshooting](https://learn.adafruit.com/raspberry-pi-care-and-troubleshooting.md)
- [Adafruit FONA 808 Cellular + GPS Shield for Arduino](https://learn.adafruit.com/adafruit-fona-808-cellular-plus-gps-shield-for-arduino.md)
- [Adafruit PCM5122 I2S DAC](https://learn.adafruit.com/adafruit-pcm5122-i2s-dac.md)
- [Use an art canvas to diffuse an RGB matrix](https://learn.adafruit.com/use-an-art-canvas-to-diffuse-rgb-matrix.md)
- [Bluetooth-Controlled Matrix LED Sign using Bluefruit Connect](https://learn.adafruit.com/bluetooth-controlled-matrix-led-sign-using-bluefruit-connect.md)
- [Adafruit AW9523 GPIO Expander and LED Driver](https://learn.adafruit.com/adafruit-aw9523-gpio-expander-and-led-driver.md)
- [Adafruit DPI Display Kippah](https://learn.adafruit.com/adafruit-dpi-display-kippah-ttl-tft.md)
- [DIY Pocket LED Gamer - Tiny Tetris!](https://learn.adafruit.com/diy-3d-printed-handheld-pocket-game-tiny-tetris-snake.md)
- [Adafruit MagTag](https://learn.adafruit.com/adafruit-magtag.md)
