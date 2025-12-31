# Source: https://learn.adafruit.com/smt-manufacturing/framed-stencils.md

# SMT Manufacturing

## Framed Stencils

If you want to make a lot of PCBs using SMT technique, its key to use reflowing instead of soldering - so that the entire board is 'soldered' at once. But to do that you'll need to deposit paste precisely on the pads. For starting out, you can use a&nbsp;[DIY stencil such as a laser cut kapton/mylar sheet (low cost)](http://learn.adafruit.com/smt-manufacturing/laser-cut-stencils)&nbsp;or depositing the paste by hand using a syringe.

However, if you ever decide to make a few hundred boards especially those with very fine pitch type parts (say 0.4 or 0.5mm pitch) it may be time to move to a framed stencil!

## Framed v. Unframed
The1 key benefit of framed stencils is that they are 'pre-stretched'. Especially with large PCB panels, having the stencil-board-alignment off by even a mm can cause bridges or opens. With DIY stencils, alignment is a pain and takes care by the operator for each pass.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/187/medium800/manufacturing_framedstencil.jpg?1396761082)

With a framed stencil, the thin stainless steel sheet is laser cut and then stretched into a solid cast aluminum frame. Its less likely to have misalignment because the sheet cant slide around

If you have the right equipment you can use unframed metal stencils and stretch them into a frame yourself, but unless you're a board fab house its unlikely that this is cost effective.

## In a Machine
Framed stencils are used in a 'screenprinting' PCB stencil machine (we'll have another tutorial about this one). The frame is bolted in place onto a hinge so you can move the stencil up (to replace the PCB) and down (to stencil).  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/188/medium800/manufacturing_stenciler.jpg?1396761088)

Since the stencil is stretched and flat, as long as it is bolted into the stenciller solidly, you will have minimal adjustment from one PCB to the next. This is what makes it ideal for multi-PCB runs. We do 10-50 PCB panels (of up to 20 pieces per panel) at a time with about 5 seconds between screenprints.## Where to Get Stencils Made

We get our&nbsp;[framed stencils made by stencils unlimited](http://www.stencilsunlimited.com/)&nbsp;. Its pretty easy to make a stencil, just export the Cream Top (or Bottom) layer from your PCB layout software and upload it during your order. They will calculate the best stencil thickness (you want a thicker stencil for large-pitch parts and thinner for fine pitch so an average is taken)\* and ship it the next day.

If you have a board fab house with stencil-making capabilities, you can also ask them to make you the stencil. Don't forget to have a tiled Cream gerber if you are having panels made - so if your design is tiled get them to tile the GBC file for you!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/189/medium800/manufacturing_framedstencilcloser.jpg?1396761097)

\*[&nbsp;IPC 7525](http://www.ipc.org/TOC/IPC-7525.pdf)&nbsp;has a long detailed document on calculating stencil thickness. It should be approximately&nbsp; **2.64 + 0.0831 \* pitch-of-component** &nbsp;then averaged.

- [Previous Page](https://learn.adafruit.com/smt-manufacturing/laser-cut-stencils.md)
- [Next Page](https://learn.adafruit.com/smt-manufacturing/stenciling-machines.md)

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

- [How To Solder Mask PCBs](https://learn.adafruit.com/how-to-solder-mask-pcbs.md)
- [Creating Accurate Footprints in Eagle](https://learn.adafruit.com/creating-accurate-footprints-in-eagle.md)
- [Adafruit Guide To Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering.md)
- [SMT Breadboard Prototyping Using Breakout PCBs](https://learn.adafruit.com/smt-prototyping-using-breakout-pcbs.md)
- [PB Gherkin 30% keyboard with KMK, CircuitPython, & KB2040](https://learn.adafruit.com/pb-gherkhin-30-keyboard-with-kmk-circuitpython-kb2040.md)
- [NeXT Bus Mouse to USB HID with CircuitPython](https://learn.adafruit.com/next-bus-mouse-to-usb-hid-with-circuitpython.md)
- [Light-Up Costumes in Harsh Environments](https://learn.adafruit.com/light-up-costumes-in-harsh-environments.md)
- [Lighting LED Nets with WLED and xLights](https://learn.adafruit.com/lighting-led-nets-with-wled-and-xlights.md)
- [EZ Make Oven](https://learn.adafruit.com/ez-make-oven.md)
- [Make your own PCB with Eagle, OSH Park, and Adafruit!](https://learn.adafruit.com/making-pcbs-with-oshpark-and-eagle.md)
- [Shop Tips & Tricks](https://learn.adafruit.com/shop-tips-and-tricks.md)
- [Magic Storybook with ChatGPT](https://learn.adafruit.com/magic-storybook-with-chatgpt.md)
- [16-Step Drum Sequencer](https://learn.adafruit.com/16-step-drum-sequencer.md)
- [Glowing Birthday Number Crown](https://learn.adafruit.com/glowing-birthday-number-crown.md)
- [LED Noodle Shop Sign](https://learn.adafruit.com/led-noodle-shop-sign.md)
