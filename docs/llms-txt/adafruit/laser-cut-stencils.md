# Source: https://learn.adafruit.com/smt-manufacturing/laser-cut-stencils.md

# SMT Manufacturing

## DIY Solder Paste Stencils

If you want to make a lot of PCBs using SMT technique, its key to use reflowing instead of soldering - so that the entire board is 'soldered' at once. But to do that you'll need to deposit paste precisely on the pads. For starting out, you can use a DIY stencil such as a laser cut kapton/mylar sheet. This is a low cost technique you can do yourself or order online!Thanks to&nbsp;[Ryan O'Hara at Ohararp.com](http://ohararp.com/ "Link: http://ohararp.com/")&nbsp;for this information, he provides a stencil cutting service and is recommended!

Supplies you'll need:

1. A laser cutter
2. Kapton film, I like the 2 mil thick 1 ft square sheets from&nbsp;[McMaster-Carr](http://www.mcmaster.com/#2271K2)
3. Solder paste such as&nbsp;[Kester No-Clean](https://www.kester.com/products/product/r276-solder-paste "Link: https://www.kester.com/products/product/r276-solder-paste")

Software you'll need:

1. PCB layout software (well, thats how I do it) - this example will use EagleCAD
2. [Pentalogix ViewMate Gerber viewer software](http://www.pentalogix.com/Download/download.html "Link: http://www.pentalogix.com/Download/download.html")
3. [PDFCreator](http://sourceforge.net/project/showfiles.php?group_id=57796)&nbsp;or some other free&nbsp;PDF&nbsp;printer

## Create Gerber files of cream layer
This is the PCB we'll be making a stencil for. It only has one chip but of course you can use a more complex layout.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/174/medium800/manufacturing_eagle.gif?1447974840)

Your PCB software should be able to create/export the Cream Layer (solder paste layer) in Gerber RS274x format. In Eagle you can make your own Job for this quite easily.![](https://cdn-learn.adafruit.com/assets/assets/000/000/175/medium800/manufacturing_creamjob.gif?1447974853)

Also export the Dimension layer (PCB outline) since that will help a lot in registration.## Import Cream Gerber in Viewmate
Start up Viewmate and File\>Import\>Gerber one of the Gerber files generated.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/176/medium800/manufacturing_import_%281%29.gif?1447974862)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/177/medium800/manufacturing_swelled.gif?1447974874)

You can zoom in using the Magnifying glass tool.![](https://cdn-learn.adafruit.com/assets/assets/000/000/178/medium800/manufacturing_closeup.gif?1447974884)

## Swell Pads

Next we will make minor adjustnents to shrink the pads a little

Select Setup\>D Codes

![](https://cdn-learn.adafruit.com/assets/assets/000/000/179/medium800/manufacturing_dcodes.gif?1447974896)

Which will bring up a list of all the pads used. You will probably just want to select all of them.![](https://cdn-learn.adafruit.com/assets/assets/000/000/180/medium800/manufacturing_pads.gif?1447974908)

Then select Operations \> Swell.![](https://cdn-learn.adafruit.com/assets/assets/000/000/181/medium800/manufacturing_swelling.gif?1447974918)

and input somewhere around -0.002 (2 mil) to shrink all the pads by 0.002 inches in each direction.![](https://cdn-learn.adafruit.com/assets/assets/000/000/182/medium800/manufacturing_2mil.gif?1447974929)

You'll now see that your pads are thinner. This prevents bridging since the laser is not perfectly precise and tends to 'go over' the boundaries by a few mils.![](https://cdn-learn.adafruit.com/assets/assets/000/000/183/medium800/manufacturing_postswell.gif?1447974940)

## Export
Now we'll export to&nbsp;PDF&nbsp;which will allow for easy importing into Corel Draw. The free version of Viewate doesnt seem to permit exporting, but you can print to&nbsp;PDF&nbsp;which is just as good.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/184/medium800/manufacturing_pdfprint.gif?1447974950)

## Cut!
Import into Corel Draw and use raster not vector, to burn away the kapton film. For a 35W or 45W epilog, 30% speed and 100% power at 600 dpi made for a nice clean edge. Be sure to gently rub the stencil with water and a paper towel to get rid of the burnt kapton.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/185/medium800/manufacturing_cutstencil.jpg?1396761070)

I usually use the Dimension layer info to make a jig for silkscreening by cutting out the PCB outline in a 0.062'' (1/16th) clear acrylic sheet

Here is a LFCSP 16 (4mm on each side) cut out of 2 mil kapton as above.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/186/medium800/manufacturing_lfcspkapton.jpg?1396761074)

- [Previous Page](https://learn.adafruit.com/smt-manufacturing/solder-paste-storage.md)
- [Next Page](https://learn.adafruit.com/smt-manufacturing/framed-stencils.md)

## Featured Products

### Fine tip curved tweezers - ESD safe

[Fine tip curved tweezers - ESD safe](https://www.adafruit.com/product/422)
When soldering small surface-mount (SMD/SMT) components, one thing you'll need is a good pair of tweezers. These are a great pair of every-day tweezers. They're anti-static, anti-magnetic and made of hard stainless steel. The tips are fine and pointy to pick up any size component. This...

In Stock
[Buy Now](https://www.adafruit.com/product/422)
[Related Guides to the Product](https://learn.adafruit.com/products/422/guides)
### Fine tip straight tweezers - ESD safe

[Fine tip straight tweezers - ESD safe](https://www.adafruit.com/product/421)
When soldering small surface-mount (SMD/SMT) components, one thing you'll need is a good pair of tweezers. These tweezers are a great pair of every-day tweezers. They're anti-static, anti-magnetic and made of hard stainless steel. The tips are fine and pointy to pick up any size...

In Stock
[Buy Now](https://www.adafruit.com/product/421)
[Related Guides to the Product](https://learn.adafruit.com/products/421/guides)
### USB Microscope - 5MP interpolated 220x magnification / 8 LEDs

[USB Microscope - 5MP interpolated 220x magnification / 8 LEDs](https://www.adafruit.com/product/636)
As electronics get smaller and smaller, you'll need a hand examining PCBs and this little USB microscope is the perfect tool. Its smaller and lighter than a large optical microscope but packs quite a bit of power in its little body. There's a 2 megapixel sensor inside and an optical...

Out of Stock
[Buy Now](https://www.adafruit.com/product/636)
[Related Guides to the Product](https://learn.adafruit.com/products/636/guides)

## Related Guides

- [Reindeer Solder Kit by Phyx](https://learn.adafruit.com/reindeer-solder-kit-by-phyx.md)
- [3D-Printed Solder Paste Dispenser Hand Switch ](https://learn.adafruit.com/3d-printed-solder-paste-dispenser-hand-switch.md)
- [USB Rechargeable Mini Solder Fume Extractor](https://learn.adafruit.com/usb-rechargeable-mini-solder-fume-extractor.md)
- [How to Sign Windows Drivers & Executables](https://learn.adafruit.com/how-to-sign-windows-drivers-installer.md)
- [Desktop Fume Extractor](https://learn.adafruit.com/desktop-fume-extractor.md)
- [Chinese Dragon Puppet with Motion-Reactive Flame Effect](https://learn.adafruit.com/chinese-dragon-puppet-with-motion-reactive-flame-effect.md)
- [16-Step Drum Sequencer](https://learn.adafruit.com/16-step-drum-sequencer.md)
- [Color Sensing Music Player](https://learn.adafruit.com/color-sensing-music-player.md)
- [Light-Up Costumes in Harsh Environments](https://learn.adafruit.com/light-up-costumes-in-harsh-environments.md)
- [Garden Path Lights with WLED and a Sunset Timer](https://learn.adafruit.com/garden-path-lights-with-sunset-timer.md)
- [CNC Rotary Macropad](https://learn.adafruit.com/cnc-rotary-macropad.md)
- [Blinka Says Tabletop Arcade Game](https://learn.adafruit.com/blinka-says-tabletop-arcade-game.md)
- [IoT Moon Phase Guide](https://learn.adafruit.com/moon-phase.md)
- [KTOWN's Ultimate Creating Parts in Eagle Tutorial](https://learn.adafruit.com/ktowns-ultimate-creating-parts-in-eagle-tutorial.md)
- [Shop Tips & Tricks](https://learn.adafruit.com/shop-tips-and-tricks.md)
