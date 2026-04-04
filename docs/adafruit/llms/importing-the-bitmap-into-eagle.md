# Source: https://learn.adafruit.com/creating-accurate-footprints-in-eagle/importing-the-bitmap-into-eagle.md

# Creating Accurate Footprints in Eagle

## Importing the Bitmap into Eagle

Once you're inside Eagle, create a new 'Package' and give it an appropriate name (Library \> Package ...). &nbsp;From here, you need to run the 'import-bmp.ulp' user language program. &nbsp;The quickest way is tp simply&nbsp;type the following command anywhere in the package editor:

```
run import-bmp.ulp
```

Once you run the ULP&nbsp;you should be presented with the following dialogue box, which you can click OK on to continue:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/056/medium800/manufacturing_ImportBMP_1.png?1396778666)

You'll be asked to select your source bitmap image, and you need to point to the 1-bit BMP you created earlier:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/057/medium800/manufacturing_ImportBMP_2.png?1396778685)

Next, you'll be presented with a box showing all of the colors available in the image. &nbsp;Select the 'white' pixel box, and click OK:

![](https://cdn-learn.adafruit.com/assets/assets/000/002/058/medium800/manufacturing_ImportBMP_3.png?1396778695)

The most important step is in the following dialogue, where **you need to change two values** :

- Set the ' **Unit**' radio box to ' **mm**'  
- Set the ' **Scale**' factor to **0.01mm** , the same scale we used when resizing our bitmap image earlier (remember mm\*100?).

![](https://cdn-learn.adafruit.com/assets/assets/000/002/059/medium800/manufacturing_ImportBMP_4.png?1396778715)

Click the **OK** button, which will present the following screen, and then click the **Run script** button.

![](https://cdn-learn.adafruit.com/assets/assets/000/002/060/medium800/manufacturing_ImportBMP_5.png?1396778731)

This should give you something similar to the results below with the imported bitmap placed on layer 200 (the default value, but it can be changed in the import settings dialogue box above):

![](https://cdn-learn.adafruit.com/assets/assets/000/002/061/medium800/manufacturing_ImportBMP_6.png?1396778755)

With all of the done, we can start making our footprint

- [Previous Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/creating-a-scaled-bitmap.md)
- [Next Page](https://learn.adafruit.com/creating-accurate-footprints-in-eagle/tracing-your-footprint.md)

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
