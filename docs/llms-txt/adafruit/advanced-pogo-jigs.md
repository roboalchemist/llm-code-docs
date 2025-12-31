# Source: https://learn.adafruit.com/how-to-make-a-pogo-pin-test-jig/advanced-pogo-jigs.md

# How to Make a Pogo Pin Test Jig

## Advanced Pogo Jigs

For more complicated projects, you may need to have a complicated testing procedure in which case we can make multi-step testers that also keep the PCB held down with little ears!![](https://cdn-learn.adafruit.com/assets/assets/000/002/532/medium800/manufacturing_pogoears.jpeg?1396784133)

(We totally saw this and stole the idea from someone online but we can't find the link anymore, sorry!)  
  
The plastic pieces hold down the PCB against the pogo bed. This tester, when used with a little batch script, performs the following test:

1. Reprograms the board's fuses and flash with a bootloader (via the ISP port). For this part we're using the Arduino as an ISP programmer (there's a sketch that does this)
2. The computer then bootloads (via USB) a pin-by-pin testing program
3. Once the board indicates the test completed, the computer erases the testing program

## Various Types of Pogo Pins
![](https://cdn-learn.adafruit.com/assets/assets/000/138/575/medium800/manufacturing_Untitled1.png?1753805628)

There are various types, sizes and lengths of pogo pins. When you are designing your particular project, you will want to check the fit of your board against the pins to ensure a good mechanical fit. Pins to short or too long may not make the desired electrical connection you are planning.

![](https://cdn-learn.adafruit.com/assets/assets/000/138/577/medium800/manufacturing_Untitled.png?1753805898)

[This article by DigiKey](https://www.digikey.com/en/articles/the-basics-of-pogo-pin-connectors) is good at explaining pogo pins.

## Pogo Pins – Collin’s Lab Notes
https://youtu.be/NGZ_vd6qmeQ

- [Previous Page](https://learn.adafruit.com/how-to-make-a-pogo-pin-test-jig/testing.md)

## Featured Products

### Pogo Pin Probe Clip

[Pogo Pin Probe Clip](https://www.adafruit.com/product/1969)
The Pogo Pin Probe Clip is a great way to test and connect with pin-point accuracy without soldering! It's sort of like an [alligator clip](https://www.adafruit.com/product/321) with a built-in springy pogo pin - so you can connect to any PCB pad for 'scoping, analyzing, or...

In Stock
[Buy Now](https://www.adafruit.com/product/1969)
[Related Guides to the Product](https://learn.adafruit.com/products/1969/guides)
### Pogo Pins "Spear Head" (10 pack)

[Pogo Pins "Spear Head" (10 pack)](https://www.adafruit.com/product/394)
Pogo pins are little spring-loaded contacts, very handy for making jigs, or making momentary (but electrically solid) contacts. We use them by the dozen for making programming and testing jigs but they're handy also if say you want to JTAG program a board that you cant solder headers to -...

In Stock
[Buy Now](https://www.adafruit.com/product/394)
[Related Guides to the Product](https://learn.adafruit.com/products/394/guides)
### Pogo Pins "Cupped Head" (10 pack)

[Pogo Pins "Cupped Head" (10 pack)](https://www.adafruit.com/product/2428)
Pogo pins are little spring-loaded contacts, very handy for making jigs, or making momentary (but electrically solid) contacts. We use them by the dozen for making programming and testing jigs but they're handy also if say you want to JTAG program a board that you cant solder headers to -...

In Stock
[Buy Now](https://www.adafruit.com/product/2428)
[Related Guides to the Product](https://learn.adafruit.com/products/2428/guides)
### Pogo Pins "Crown Head" (10 pack)

[Pogo Pins "Crown Head" (10 pack)](https://www.adafruit.com/product/2429)
Pogo pins are little spring-loaded contacts, very handy for making jigs, or making momentary (but electrically solid) contacts. We use them by the dozen for making programming and testing jigs but they're handy also if say you want to JTAG program a board that you cant solder headers to -...

In Stock
[Buy Now](https://www.adafruit.com/product/2429)
[Related Guides to the Product](https://learn.adafruit.com/products/2429/guides)
### Pogo Pins "Needle Head" (10 pack)

[Pogo Pins "Needle Head" (10 pack)](https://www.adafruit.com/product/2430)
Pogo pins are little spring-loaded contacts, very handy for making jigs, or making momentary (but electrically solid) contacts. We use them by the dozen for making programming and testing jigs but they're handy also if say you want to JTAG program a board that you cant solder headers to -...

In Stock
[Buy Now](https://www.adafruit.com/product/2430)
[Related Guides to the Product](https://learn.adafruit.com/products/2430/guides)
### Toggle Clamp - Large Size

[Toggle Clamp - Large Size](https://www.adafruit.com/product/2457)
\*Ka-thunk\* Pin down that PCB with our **Toggle Clamp** , a sturdy and reliable way to quickly press and release with precision! A pogo-pin bed is a great way to connect and test boards without any soldering, but you have to somehow get that PCB aligned right and evenly pressed down...

In Stock
[Buy Now](https://www.adafruit.com/product/2457)
[Related Guides to the Product](https://learn.adafruit.com/products/2457/guides)
### Toggle Clamp - Medium Flip-up Style

[Toggle Clamp - Medium Flip-up Style](https://www.adafruit.com/product/2456)
\*Ka-thunk\* Pin down that little PCB with our&nbsp; **Toggle Clamp** , a sturdy and reliable way to quickly press and release with precision! A pogo-pin bed is a great way to connect and test boards without any soldering, but you have to somehow get that PCB aligned right and evenly...

In Stock
[Buy Now](https://www.adafruit.com/product/2456)
[Related Guides to the Product](https://learn.adafruit.com/products/2456/guides)
### Toggle Clamp - Small Flip-down Style

[Toggle Clamp - Small Flip-down Style](https://www.adafruit.com/product/2459)
\*Ka-thunk\* Pin down that PCB with our&nbsp; **Toggle Clamp** , a sturdy and reliable way to quickly press and release with precision! A pogo-pin bed is a great way to connect and test boards without any soldering, but you have to somehow get that PCB aligned right and evenly pressed...

In Stock
[Buy Now](https://www.adafruit.com/product/2459)
[Related Guides to the Product](https://learn.adafruit.com/products/2459/guides)

## Related Guides

- [DIY 3D Printing Filament](https://learn.adafruit.com/diy-3d-printing-filament.md)
- [Standalone AVR Chip Programmer](https://learn.adafruit.com/standalone-avr-chip-programmer.md)
- [How we designed an injection-molded case](https://learn.adafruit.com/how-we-designed-an-injection-molded-case-for-raspberry-pi.md)
- [Metal Parts from 3D Prints](https://learn.adafruit.com/metal-parts-from-3d-prints.md)
- [KTOWN's Ultimate Creating Parts in Eagle Tutorial](https://learn.adafruit.com/ktowns-ultimate-creating-parts-in-eagle-tutorial.md)
- [Maker Business & Manufacturing Software - Our Tips & Tricks](https://learn.adafruit.com/maker-business-manufacturing-software-our-tips-and-tricks.md)
- [Adafruit Pinguin for EAGLE CAD](https://learn.adafruit.com/adafruit-pinguin-for-eagle-cad.md)
- [Laser-Cut Enclosure Design](https://learn.adafruit.com/laser-cut-enclosure-design.md)
- [How to Sign Windows Drivers & Executables](https://learn.adafruit.com/how-to-sign-windows-drivers-installer.md)
- [SMT Manufacturing](https://learn.adafruit.com/smt-manufacturing.md)
- [All About Laser Cutters](https://learn.adafruit.com/all-about-laser-cutters.md)
- [Shop Tips & Tricks](https://learn.adafruit.com/shop-tips-and-tricks.md)
- [How to convert Eagle PCBs to 3D Models in Fusion 360](https://learn.adafruit.com/how-to-convert-eagle-pcbs-to-3d-models-in-fusion-360.md)
- [Creating Accurate Footprints in Eagle](https://learn.adafruit.com/creating-accurate-footprints-in-eagle.md)
- [Make your own PCB with Eagle, OSH Park, and Adafruit!](https://learn.adafruit.com/making-pcbs-with-oshpark-and-eagle.md)
