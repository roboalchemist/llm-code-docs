# Source: https://learn.adafruit.com/creating-accurate-footprints-in-eagle/tracing-your-footprint.md

# Creating Accurate Footprints in Eagle

## Tracing Your Footprint

The most labour intensive part is here, since you need to trace the image out on an appropriate layer (I use layer 51 for this kind of information, but some people may prefer layer 21 for certain parts).  
  
There's no real shortcut (that I've found) to just zooming in and starting to trace the image out using the different variations of the line tool to draw angles, arcs, etc., where appropriate. &nbsp;Obviously the level of detail you need will vary, but at the very least be sure to create an accurate mechanical outline of the outer-most borders since those are the most important.

Info: 

A lot of the outline can be done with the line options (curves, angles, etc.):

![](https://cdn-learn.adafruit.com/assets/assets/000/002/062/medium800/manufacturing_LineOptions.png?1396778761)

Some more complex angles, however, may need to drawn as straight line segments, and then you'll need to do a bit of guesswork with the curve option, which you can see by right-clicking on a line segment and clicking 'properties' in the popup dialogue box:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/063/medium800/manufacturing_Trace_Curve1.png?1396778786)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/064/medium800/manufacturing_Trace_Curve2.png?1396778813)

After about 25 minutes of work (again the level of detail you need or want depends on how severe your OCD is), you should end up with something similar to this:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/065/medium800/manufacturing_EndResults.png?1396778839)

Next you need to delete all the garbage left over on layer 200 (or whatever you selected during import) to only leave your outline ... importing bitmaps is incredibly wasteful since there are hundreds and hundreds of lines versus a couple dozen for even a reasonably complex part traced during this method.  
  
Go into your 'Display' options by clicking the display icon the the top-left corner (three filled squares) and disabling layer 51 (or 21 if you used that) as follows:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/066/medium800/manufacturing_Disable51.png?1396778855)

Click OK, and then select everything on the screen using the 'Group' tool (dotted rectangle):

![](https://cdn-learn.adafruit.com/assets/assets/000/002/067/medium800/manufacturing_Group.png?1396778879)

Then select the 'Delete' tool (an X), right click on your group and select 'delete group':

![](https://cdn-learn.adafruit.com/assets/assets/000/002/068/medium800/manufacturing_DeleteGroup.png?1396778902)

Now if you go back and turn layer 51 back on, you should see only a reasonably efficient part outline&nbsp;(in terms of data stored in the library) that is a very close approximation of the part in question. &nbsp;Now you simply need to add in your pads as you would for any other footprint, save the part, and you'll have a far better sense of the mechanical boundaries of your parts and connectors.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/070/medium800/manufacturing_Layer51On.png?1396778924)

# OK, nice outline .. but what about the pads?
The actual pads for your part should still be defined solely from the footprint suggestions in the datasheet, and not based on the graphical outline used here since this is only a graphical representation and may have some segments&nbsp;exaggerated&nbsp;for illustration purposes. &nbsp;Be sure to follow the datasheet exactly to place the pads, based on numerical entry for size and position,&nbsp;and then align the part outline created above&nbsp;as accurately as possible over the pads.- [Previous Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/importing-the-bitmap-into-eagle.md)
- [Next Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/results.md)

## Related Guides

- [How to Sign Windows Drivers & Executables](https://learn.adafruit.com/how-to-sign-windows-drivers-installer.md)
- [Make your own PCB with Eagle, OSH Park, and Adafruit!](https://learn.adafruit.com/making-pcbs-with-oshpark-and-eagle.md)
- [Metal Parts from 3D Prints](https://learn.adafruit.com/metal-parts-from-3d-prints.md)
- [All About Laser Cutters](https://learn.adafruit.com/all-about-laser-cutters.md)
- [Adafruit Pinguin for EAGLE CAD](https://learn.adafruit.com/adafruit-pinguin-for-eagle-cad.md)
- [Maker Business & Manufacturing Software - Our Tips & Tricks](https://learn.adafruit.com/maker-business-manufacturing-software-our-tips-and-tricks.md)
- [SMT Manufacturing](https://learn.adafruit.com/smt-manufacturing.md)
- [How to Make a Pogo Pin Test Jig](https://learn.adafruit.com/how-to-make-a-pogo-pin-test-jig.md)
- [How we designed an injection-molded case](https://learn.adafruit.com/how-we-designed-an-injection-molded-case-for-raspberry-pi.md)
- [How to convert Eagle PCBs to 3D Models in Fusion 360](https://learn.adafruit.com/how-to-convert-eagle-pcbs-to-3d-models-in-fusion-360.md)
- [DIY 3D Printing Filament](https://learn.adafruit.com/diy-3d-printing-filament.md)
- [Laser-Cut Enclosure Design](https://learn.adafruit.com/laser-cut-enclosure-design.md)
- [Shop Tips & Tricks](https://learn.adafruit.com/shop-tips-and-tricks.md)
- [Standalone AVR Chip Programmer](https://learn.adafruit.com/standalone-avr-chip-programmer.md)
- [KTOWN's Ultimate Creating Parts in Eagle Tutorial](https://learn.adafruit.com/ktowns-ultimate-creating-parts-in-eagle-tutorial.md)
