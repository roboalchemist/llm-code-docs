# Source: https://learn.sparkfun.com/tutorials/making-custom-footprints-in-eagle

## Introduction

This is a tutorial for the Eagle cad program, designed for intermediate level users. The idea is to import images of parts to create a customized footprint that matches the footprint on the component, and it can be done simply using the tools that Eagle provides.

As always, necessity is the mother of invention, and is what sparked using this Eagle tool here at SparkFun. Too many times we encountered problems with footprints having incorrect proportions, incorrect measurements, and often-times were too busy (too many things too close to each other). This led to reflow problems in our ovens, caused shifted parts, tombstones, and many, many jumpers to ground, especially on our [QFN package ICs](https://learn.sparkfun.com/tutorials/integrated-circuits/ic-packages).

Our Testing and Quality Control Manager, Pete Lewis, figured out a good system to utilize Eagle\'s built-in image importer so that we could get exact footprints created for the problem parts.

### Suggested Reading

As mentioned, this tutorial requires some intermediate skills with Eagle. If you would like a refresher on how to use Eagle as well as a few other skills, please visit these other tutorials.

- [PCB Basics](https://learn.sparkfun.com/tutorials/pcb-basics)
- [How to Read a Schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic)
- [How to install and setup Eagle PCB software](https://learn.sparkfun.com/tutorials/how-to-install-and-setup-eagle)
- [How to layout PTH PCBs: Schematic](https://learn.sparkfun.com/tutorials/using-eagle-schematic)
- [How to layout PTH PCBs: Board Layout](https://learn.sparkfun.com/tutorials/using-eagle-board-layout)
- [Creating SMD Footprints](https://learn.sparkfun.com/tutorials/designing-pcbs-smd-footprints)
- [How to layout SMD PCBs](http://learn.sparkfun.com/tutorials/designing-pcbs-advanced-smd)

## Creating a Bitmap Image of the Footprint

The first step is the creation of a monochromatic Bitmap (\*.bmp) image of the part you are customizing. Eagle really only likes to import images with solid colors, and black and white works very well. In this tutorial I will be using a Microstep Motor Driver (IC A4983SETTR-T) in a 28-QFN package. This IC can be found on the [Quadstepper Motor Driver Board](https://www.sparkfun.com/products/10507).

Using the macro setting on a digital camera (I recommend 8Mp or higher) take a picture of the underside of your part (where the legs or pads will be touching your board).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/4/5/d/b/51edc25cce395f9565000003.jpg)](https://cdn.sparkfun.com/assets/e/4/5/d/b/51edc25cce395f9565000003.jpg)

*Notice that Macro is enabled.*

Try to position the part as straight and as centered as possible in the camera lens so that there will be less correction needed later. Use flash if necessary, but try to minimize shadows as much as possible.

[![alt text](https://cdn.sparkfun.com/assets/b/a/b/6/b/51edc351ce395f3965000004.jpg)](https://cdn.sparkfun.com/assets/5/7/d/d/4/51edc25cce395f8765000007.jpg)

*As straight as possible with minimal shadows.*

Once a picture of your liking has been taken, it\'s time to correct it, convert it to a Bitmap, and prepare it to be imported into Eagle. I used a program called [Digital Photo Professional](http://en.wikipedia.org/wiki/Digital_Photo_Professional), because I like that it has a grid feature, but any program with an incremental rotate function and a saturation and contrast adjustment will work.

The goal is to make sure the part is absolutely straight/square in the frame so that it will be on-grid for Eagle.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/3/9/d/e/51edc25cce395f5f65000003.jpg)](https://cdn.sparkfun.com/assets/1/3/9/d/e/51edc25cce395f5f65000003.jpg)

Next, adjust the contrast (usually higher) and the saturation (always as low as it can be) to get the picture as close to black and white as possible.

At this point, it\'s a good idea to save a new version of the picture, and open that with the Windows default MS Paint, or something similar in Mac OS.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/6/9/4/2/2/51edc25cce395feb65000003.jpg)](https://cdn.sparkfun.com/assets/6/9/4/2/2/51edc25cce395feb65000003.jpg)

*Contrast: 75%, Saturation: 0%.*

To clean up the shadows, use the CUT function (ctrl + X). Notice the righthand side, the black body is flush with the white pad. That is how you want the lefthand side to be as well. Simply highlight along the edge of the pads, and cut the shadow off.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/c/5/e/7/51edc25ece395ffd65000002.jpg)](https://cdn.sparkfun.com/assets/e/c/5/e/7/51edc25ece395ffd65000002.jpg)

*Image before shadow removal.*

After that, use the ERASE tool to clean up the stray bits of black as much as possible. We want the white in the picture to be the metal pads, and we want them to be as clear as possible. This helps immensely when imported into Eagle, and it prevents a lot of confusion later on. The more pixels that are fixed now, the less time there will be spent trying to figure out where pads begin or end in Eagle.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/1/a/f/6/0/51edc25cce395f5465000002.jpg)](https://cdn.sparkfun.com/assets/1/a/f/6/0/51edc25cce395f5465000002.jpg)

*Image after shadow removal and clean-up.*

Saving the image as a monochromatic BMP is the easiest way to convert the picture into a usable form for Eagle.Click File → Save-As → and select Monochromatic Bitmap. Some programs have a dropdown menu, and this can be selected under "Type".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/8/6/e/7/51edc25cce395fe365000005.jpg)](https://cdn.sparkfun.com/assets/9/8/6/e/7/51edc25cce395fe365000005.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/7/6/d/9/8/51edc25cce395f4765000003.jpg)](https://cdn.sparkfun.com/assets/7/6/d/9/8/51edc25cce395f4765000003.jpg)

Now you have a single-layer (monochromatic), black and white Bitmap image or your part, ready to be inserted into Eagle.

## Importing the Bitmap Image into Eagle

Go ahead and open Eagle, and navigate to whichever library your part lives in. As stated in the title, this tutorial is not for building a footprint from scratch ([although you can quite easily](https://learn.sparkfun.com/tutorials/designing-pcbs-smd-footprints)), rather it is for customizing an existing footprint to be exactly the right size and shape.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/4/7/1/6/51edc25cce395f5a65000002.jpg)](https://cdn.sparkfun.com/assets/e/4/7/1/6/51edc25cce395f5a65000002.jpg)

Once open, select your package using the little IC icon in your menu bar.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/a/9/4/7/2/51edc25cce395fb365000007.jpg)](https://cdn.sparkfun.com/assets/a/9/4/7/2/51edc25cce395fb365000007.jpg)

It will open something like this.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/0/9/6/c/51edc25dce395fba65000000.jpg)](https://cdn.sparkfun.com/assets/9/0/9/6/c/51edc25dce395fba65000000.jpg)

There are a couple of layers available here: **red** is the copper layer that represents the metal that will be exposed on your board, **white stripes** represents the stencil layer where solder paste will go if you decide to use reflow ovens as your soldering method (we use this method for all of our SMD components), and **plain white** represents the top silk layer that will print on your board.

We want to focus on the copper layer: the large center pad and the smaller foot-pads around it.

Before you do anything, it\'s a good idea to create a new package, copying the existing footprint from the one you just opened. Use the Group-Select tool (alt + F7) to highlight everything, and use the Copy tool to copy everything.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/9/4/4/3/f/51edc25dce395f2865000006.jpg)](https://cdn.sparkfun.com/assets/9/4/4/3/f/51edc25dce395f2865000006.jpg)

Open the Package list again, and, in the "New" bar, type the new name of your package. I always use the old name and then add "1:1" so that I know this is the one-to-one measured footprint.

Once you have created this new package, use the Paste tool to place everything from the old package.

Next, measure your part with a pair of digital calipers. Pick the spot of the piece you measured in your Eagle package, and draw a line of precisely that length.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/b/e/2/0/51edc25dce395f6365000007.jpg)](https://cdn.sparkfun.com/assets/4/b/e/2/0/51edc25dce395f6365000007.jpg)

This is for reference purposes (I used the Reference Layer \-- purple) so that we can scale our imported .bmp image.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/e/d/b/e/51edc25dce395f6565000001.jpg)](https://cdn.sparkfun.com/assets/2/e/d/b/e/51edc25dce395f6565000001.jpg)

When you have your reference line laid out, click on the ULP button on your toolbar, and select "import-bmp".This let\'s you set up parameters and run a script to plot pixels in Eagle based on a Bitmap image.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/6/b/0/c/6/51edc25dce395f7565000006.jpg)](https://cdn.sparkfun.com/assets/6/b/0/c/6/51edc25dce395f7565000006.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/1/5/3/6/51edc25dce395fc465000007.jpg)](https://cdn.sparkfun.com/assets/c/1/5/3/6/51edc25dce395fc465000007.jpg)

Select your Bitmap image, and then select the colors you wish to include.

[![alt text](https://cdn.sparkfun.com/assets/5/0/d/3/b/51edc25dce395f9065000003.jpg)](https://cdn.sparkfun.com/assets/5/0/d/3/b/51edc25dce395f9065000003.jpg)

I always select only the first box, so that I only have one layer to work with on the imported image.

Next, you have to select your scale.

[![alt text](https://cdn.sparkfun.com/assets/f/b/b/c/c/51edc25dce395f3565000007.jpg)](https://cdn.sparkfun.com/assets/f/b/b/c/c/51edc25dce395f3565000007.jpg)

This is where the reference line comes into play. I always have to estimate the scale, run the script, and then measure the image against the reference line. If the image is too small, I select it all (alt + F7), delete it (F3), and re-import the image using a larger scale to run the script. If the image is too large, I use a smaller scale.

Sometimes it takes 5 or 6 importations to get the size exactly right, but it is worth it. Once you have the image in place, the rest is just fitting the copper layer to the pads in the image.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/0/a/b/2/c/51edc25dce395f8a65000004.jpg)](https://cdn.sparkfun.com/assets/0/a/b/2/c/51edc25dce395f8a65000004.jpg)

*Imported image too small.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/e/2/a/3/0/51edc25dce395fb865000004.jpg)](https://cdn.sparkfun.com/assets/e/2/a/3/0/51edc25dce395fb865000004.jpg)

*Imported image too large.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/8/4/3/d/2/51edc25dce395fdb65000001.jpg)](https://cdn.sparkfun.com/assets/8/4/3/d/2/51edc25dce395fdb65000001.jpg)

*Imported image correct size \-- flipped it horizontally for better visibility.*

As you can see, the reference line matches the outside edges of the IC image. Also note that the color of the imported image is the color of the Eagle layer on which it was imported (200 is the default) and that by selecting only the first box of colors we get the component as positive space (blue) and the pads as negative space.

Moving the imported image over the center of the footprint might seem a bit tricky. First, note that the image is broken up into individual pixels that are each their own object. This means you cannot simply select one and move the whole image. It means you have to isolate the layer 200, select the whole image (alt + F7), and then move it over the rest of the footprint (F7). I used the large center pad as my reference point, making sure it is lined up with the center negative space on my imported image.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/3/f/e/0/51edc25dce395f0466000001.jpg)](https://cdn.sparkfun.com/assets/d/3/f/e/0/51edc25dce395f0466000001.jpg)

With that, you should now have an image of the correct footprint sizes and dimensions. Now let\'s see how to edit our part to match this 1:1 image.

## Editing the Existing Footprint 

Chances are the existing footprint will be fairly close to the right size and spacing, but there are always better ways to set things up. For instance, in this example, the pads on the footprint are square, while the pads on the part are round.

Always match metal to metal wherever possible. This means that all the pads on the footprint should be the same size and shape as their counterparts on the part on which you are working.

Using the Change tool on the left toolbar, select Roundness and type 100 (for 100%). Then select each pad, and they will change from square to round.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/b/5/5/8/6/51edc25dce395f0d65000004.jpg)](https://cdn.sparkfun.com/assets/b/5/5/8/6/51edc25dce395f0d65000004.jpg)

After all the pads are round, move each individual pad into place, using the imported image as a reference. Note the righthand pads are lined up correctly while the upper and lower pads have not yet been moved.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/5/c/0/4/a/51edc25ece395f0a65000006.jpg)](https://cdn.sparkfun.com/assets/5/c/0/4/a/51edc25ece395f0a65000006.jpg)

Remember that for the most part, footprints are quite small, so little moves in Eagle are even smaller in the real world. It\'s ok to just get things as close as you can. It doesn\'t have to be exactly right. I always make symmetrical moves when dealing with a symmetrical part (what I do to one side I do to all four sides), so I end up having to move pads into positions that look the best overall, and maybe not the best per individual pad.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/6/f/9/e/7/51edc25ece395fdf65000001.jpg)](https://cdn.sparkfun.com/assets/6/f/9/e/7/51edc25ece395fdf65000001.jpg)

*Footprint before changes.*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/9/3/7/3/51edc25ece395f9666000002.jpg)](https://cdn.sparkfun.com/assets/4/9/3/7/3/51edc25ece395f9666000002.jpg)

*Finsihed footprint after changes.*

## Connecting the New Package to the Device

In order for you to be able to use the new package in Eagle, it must be connected to a device. Since we are just customizing an existing part, it\'s a pretty simple thing to do.

Open the Device list (next to Package on the toolbar), and select your device.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/4/7/c/2/9/51edc25ece395f1666000003.jpg)](https://cdn.sparkfun.com/assets/4/7/c/2/9/51edc25ece395f1666000003.jpg)

This opens a schematic picture of your device, along with all of the packages connected to it.

On the righthand side, select "New".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/5/7/3/c/51edc25ece395f2165000006.jpg)](https://cdn.sparkfun.com/assets/d/5/7/3/c/51edc25ece395f2165000006.jpg)

This brings up the package list, and you can select the one you just created.

You just created what Eagle calls a Variant. It\'s an alternate package associated with a device. Right-click on it and hit Rename.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/4/0/7/f/51edc25ece395f3e65000003.jpg)](https://cdn.sparkfun.com/assets/f/4/0/7/f/51edc25ece395f3e65000003.jpg)

I always rename this new Variant "1:1" so that all the Library files are consistent, but you can call it whatever you like.

Notice that there is that little yellow circle with an exclamation point next to the variant. This means that a package has been added to the device, but Eagle is not sure how to connect the pins associated with the pads.

With your variant selected, hit the Connect button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/c/f/e/5/d/51edc25ece395f0d66000004.jpg)](https://cdn.sparkfun.com/assets/c/f/e/5/d/51edc25ece395f0d66000004.jpg)

This brings up a list of all the pins on the Device, and all the pins on the package.

From the little dropdown menu, scroll to the original package name (if there is more than one package already associated with this device -- in my case there are two more).

This connects your variant exactly like the original package, which is how you want it to be.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/7/2/9/4/8/51edc25ece395f1f65000007.jpg)](https://cdn.sparkfun.com/assets/7/2/9/4/8/51edc25ece395f1f65000007.jpg)

Once you click OK, you have completed the connections and your variant should get a check mark.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/7/2/b/7/51edc25ece395f1466000006.jpg)](https://cdn.sparkfun.com/assets/2/7/2/b/7/51edc25ece395f1466000006.jpg)

Now all that remains is to use this new package and on a board, or replace an existing package on a board if you have already used the library part somewhere in your designs.