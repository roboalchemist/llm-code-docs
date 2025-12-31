# Source: https://learn.adafruit.com/creating-accurate-footprints-in-eagle/creating-a-scaled-bitmap.md

# Creating Accurate Footprints in Eagle

## Creating a Scaled Bitmap

Once you've located an accurate top view of your part, you need to get a decent-sized copy of the image into your favorite photo editing program. &nbsp;With most PDFs you can just zoom in on the PDF so the image area in question is full screen, take a screenshot and then paste this image into your image editor, removing everything except the top view (you might need to use a white paint-brush&nbsp;for example):

![](https://cdn-learn.adafruit.com/assets/assets/000/002/052/medium800/manufacturing_ImageEditor_Screenshot.png?1396778590)

It's important to have measurements in the image at first since we'll need these to create a properly scaled image. &nbsp;In this particular image, the connector is 14mm across the X axis. &nbsp;Using this number, we'll measure the actual width of the image in pixel across the X axis, which turns out to be 643 pixels from one edge to the other.

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/002/053/medium800/manufacturing_ActualWidth.png?1396778622)

Since we now know that the bitmap image&nbsp;is 643 pixels wide for a&nbsp;real-life width of&nbsp;14mm, it's easy to figure out how to scale the image to a useful size. &nbsp;Simply&nbsp;divide the mechanical part width in mm\*100 by the actual image width of the same&nbsp;segment. &nbsp;In this case (14mm\*100) / 643 pixels = 2.177.  
  
Resize your image using this ratio. &nbsp;The total image above is 1047 pixels wide, so 1047\*2.177 = 2279 pixels wide. &nbsp;Once resized, you need to convert the image to a 1-bit bitmap image and save is somewhere. &nbsp;(As a sanity check before saying, this conversion should give you ~1400 pixels across the 14mm section for 1 pixel =&nbsp;0.01mm).  
  
Again, the way you do this will change from one image editing program to the next, but any decent image editor should support this. &nbsp;You should&nbsp;end up with a bitmap image like this:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/069/medium800/19656.bmp?1347666752)

Save this 1-bit Windows bitmap (.bmp) image somewhere memorable, and open up Eagle.

- [Previous Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/finding-and-accurate-reference.md)
- [Next Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/importing-the-bitmap-into-eagle.md)

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
