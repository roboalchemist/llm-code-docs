# Source: https://learn.sparkfun.com/tutorials/setting-up-the-pi-zero-wireless-pan-tilt-camera

## Introduction

This tutorial will show you how to assemble, program, and access the [Raspberry Pi Zero Wireless Pan-Tilt Camera](https://www.sparkfun.com/products/14329).

[![SparkFun Raspberry Pi Zero W Camera Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/0/3/Pi-Cam_Kit_14329-_01.jpg)](https://www.sparkfun.com/products/14329)

### [SparkFun Raspberry Pi Zero W Camera Kit](https://www.sparkfun.com/products/14329) 

[ KIT-14329 ]

The SparkFun Raspberry Pi Zero W Camera Kit provides you with a pan/tilt camera controlled via a Raspberry Pi Zero W. This ki...

**Retired**

### Required Materials

You\'ll need a microSD card, a sufficient power supply, and a micro-B USB Cable. We do not recommend the pre-installed NOOBS card, as it may not include a recent enough version of the Pi operating system to support the Pi Zero W.

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/2/8/13831-01a.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html) 

[ TOL-13831 ]

This is a high-quality switching \'wall wart\' AC to DC 5.1V 2,500mA USB Micro-B wall power supply manufactured specifically fo...

[ [\$13.95] ]

[![microSD Card with Adapter - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/3/0/13833-02.jpg)](https://www.sparkfun.com/products/13833)

### [microSD Card with Adapter - 16GB (Class 10)](https://www.sparkfun.com/products/13833) 

[ COM-13833 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

### Required Tools

You\'ll need a few tools to assemble this kit: just a standard soldering iron, solder, a small screwdriver, and a pair of side cutters.

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Tool Kit - Screwdriver and Bit Set](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/7/10865-01.jpg)](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html)

### [Tool Kit - Screwdriver and Bit Set](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html) 

[ TOL-10865 ]

There\'s nothing worse than getting ready for a good hack and then realizing that you can\'t even get the box open because you ...

[ [\$16.50] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Flush Cutters - Xcelite](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/3/6/14782-Flush_Cutters_-_Xcelite-02.jpg)](https://www.sparkfun.com/products/14782)

### [Flush Cutters - Xcelite](https://www.sparkfun.com/products/14782) 

[ TOL-14782 ]

These are simple flush cutters from Excelite that give you a way to cut leads very cleanly and close to the solder joint.

**Retired**

### Suggested Reading

Very little of this kit requires anything but following our step-by-step guide; however, you might want to check out our [through hole soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) tutorial as you\'ll need to do some soldering to put the pins in place on the Pi Zero W and the Pi Servo Hat. Other, tutorials you might be interested in reading include:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)

### Hobby Servo Tutorial 

Servos are motors that allow you to accurately control the rotation of the output shaft, opening up all kinds of possibilities for robotics and other projects.

[](https://learn.sparkfun.com/tutorials/pi-servo-hat-hookup-guide)

### Pi Servo Hat Hookup Guide 

This hookup guide will show you how to connect and use the Pi Servo Hat in a project.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

## Prepare the MicroSD Card

To prepare the microSD card, we need to:

- Download the latest Raspberry Pi Raspbian Jessie image.
- Create an microSD card that contains this boot image.
- Edit the \"config.txt\" file on the microSD card to enable the serial debug console.
- Create a \"wpa_supplicant.conf\" file on the SD card to enable WiFi.

Let\'s walk through these steps in more detail!

### Download the Latest Raspbian Jessie Image

You can find the image on the [Raspberry Pi Foundation Website](https://www.raspberrypi.org/downloads/raspbian/). It\'s a fairly large download so go get a snack or play a game or something.

**Note**: Make sure that you don\'t download \"RASPBIAN XYZ LITE\", as the Lite installation is lacking several utilities and programs we\'ll need to get things moving. Note that XYZ is a placeholder for the release name of the distribution; at the time of this writing, that name is \"Stretch\".

### Burn the Image to an MicroSD Card

To write the image to the card, there exists an [excellent utility for Mac/Linux/Windows called Etcher](https://etcher.io/). Simply download and install it to your computer. Then select the image you downloaded earlier, the drive you want to install to (Etcher won\'t let you install to anything but a removable drive, and if only one drive is available, it will select it automatically!), and click \"Flash!\"

[![Etcher screenshot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/etcher.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/etcher.png)

This is another long-ish process, requiring several minutes to complete. Once complete, the window will display a \"Flash Complete!\" message.

[![Etcher done](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/etcher_done.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/etcher_done.png)

By default, Etcher \"ejects\" the card after it has created the image, so you\'ll need to pull it out and reinsert it to get your computer to reload the disk.

### Edit the \"config.txt\" File on the MicroSD Card

To continue, we\'re going to need to edit a file on the microSD card. This file will be visible from any operating system, although on a Linux system it\'s in a slightly different location.

On a Windows or Macintosh, the files will be loaded in the root directory of the microSD card, so when you open a window of the drive, you\'ll see them directly. In Linux, the card will be mounted, and you\'ll have to navigate to the \"Boot\" directory on the card to find the file we\'re looking for.

Here\'s a list of all the files in the directory of interest.

[![Boot directory ls](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/drive_ls.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/drive_ls.png)

*Click the image for a closer look.*

Open the file \"config.txt\" in your favorite text editor (i.e. [Notepad++](https://notepad-plus-plus.org/), [TextWrangler](https://www.barebones.com/products/textwrangler/), [ConTEXT Editor](http://www.contexteditor.org/index.php), etc.) and add this line to the very end:

    enable_uart=1

**Note**: Despite the presence of a hash (\'#\') in front of the other lines in this file, you **must not** put one in front of this line. That would comment it out, causing it to be ignored. Adding this line will enable the UART on the GPIO pins so you can complete the rest of the process without having to hook your Pi Zero W up to a monitor and keyboard. Pretty nifty!

### Create a \"wpa_supplicant.conf\" File on the MicroSD Card to Enable WiFi

[] **Troubleshooting Tip:** For users having difficulty enabling WiFi on Pi Zero in this step, you could use the PIXEL desktop GUI if you access to a monitor and mini-HDMI adapter to connect to your network. You can also enable the camera, I2C, and SSH through **Preferences \> Raspberry Pi Configuration** from the desktop menu.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/RaspberryPi_PIXEL_Desktop_View.jpg "Raspberry Pi PIXEL Desktop View")](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/RaspberryPi_PIXEL_Desktop_View.jpg)

The last thing we need to do to prepare the microSD card is to create a \"wpa_supplicant.conf\" file on the card. This file contains the information needed for your local wireless network setup.

Create a new file using your favorite text editor. On Windows we recommend Notepad, as it provides WYSIWYG content and allows you to save a file with an arbitrary file extension. On MacOS, TextWrangler seems to be the easiest. For Linux, your default system text editor should be fine.

The contents of the file can be quite simple. Most likely, you can get away with something that looks like this:

    language:bash
    network=

Once added, modify the network ID and password for your WiFi network. Then save the file as \"wpa_supplicant.conf\" to the microSD card.

**Important Note:** On the on the \"Save As\...\" screen for Windows users, you\'ll need to change the file extension type under the field \"Save as type:\" from \"\*.txt file\" to \"All files\". Then you will need to explicitly name the file **\"wpa_supplicant.conf\"**, or Notepad will automatically append \".txt\" to the file name, breaking this functionality. See the image below.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/notepad_saveas.png)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/notepad_saveas.png)

\

*Click the image for a closer look.*

\
Some variation of this \"Save as\...\" and removing the appended \".txt\" suffix is necessary in Mac OS and Linux as well, but should be equally simple.

### Pull the MicroSD Card and Insert It into the Pi Zero W

This is all we need to do in preparation of our first boot. You can now remove the card from your computer and put it into the Pi Zero W. Don\'t power it up yet, though!

## Hardware Assembly

To assemble the hardware, we need to:

- Solder headers to the Raspberry Pi Zero W.
- Solder headers to the Pi Servo Hat.
- Install the Pi Servo Hat on the Pi Zero W.
- Assemble the pan-tilt hardware and connect the servos to the hat.

Let\'s walk through these steps in more detail!

### Solder Headers to the Raspberry Pi Zero W and the Pi Servo Hat

We recommend soldering the male header to the Pi Zero W and the female to the Pi Servo Hat. If you have any issues with soldering, please check out our [learn to solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) tutorial.

### Assemble the Pan-Tilt Mechanism

Assembly of the pan-tilt mechanism is fairly straightforward. The trickiest part is making sure the servo motors are centered during assembly.

Here\'s the family portrait of the stuff that comes in the kit. You won\'t be needing the servo horns that come packaged with the servo motors, just the ones that come packaged separately.

[![Don\'t need these](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-01.jpg)

**Heads up!** The servo hardware may vary depending on the supplier. You may need to clip the arm servo horn with 6 holes and use the screws that were packaged separately.

Start by identifying the servo horn with two long arms and two short arms. You\'ll need to clip off the long arms, as shown below.

[![Clip off the long arms](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-03.jpg)

Identify the smallest screws in the baggie of screws that came with the kit. These will be used to affix this horn to the base of the pan-tilt mechanism.

[![Screws for the pan-tilt base](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-04.jpg)

Place the horn in the base as shown, then screw it down by inserting the screws from the bottom and threading them into the horn. Note that there will be extra screws, even beyond the ones to be used later. This is generally true of all the screws in this set.

[![Pan-tilt base with horn](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-05.jpg)

Next, identify the larger self-tapping screws. These will be used for assembling the next part of the mechanism.

[![Larger self tapping screws](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-06.jpg)

Find the two pieces pictured below that will sandwich the first servo. Note the orientation of the servo in these pieces.

[![Servo sandwich](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-07.jpg)

Here\'s the sandwiched servo. Again, note the orientation for proper assembly.

[![Servo sandwich, picture 2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-08.jpg)

Here, you can see where the screws identified a couple of steps ago fit into our servo sandwich. Tighten them down, but not too much.

[![Servo sandwich with screws](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-09.jpg)

Now fit the shaft of the servo into the fitting on the horn that you previously installed into the base. This is the point where you need to make sure that the shaft is roughly centered in order for the entire assembly to work properly. I do this by turning the shaft all the way to one extreme, then turning it 90 degrees back in the other direction. Then, I remove the base and line it up with the body of the servo motor.

[![Attaching the base](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-11.jpg)

Find the two longer screws that came with the horn kit in the set to attach the base to the servo. There will likely be only two of these, and you need both, so don\'t lose one! Insert the screw to the bottom and tighten the screw to attach the two parts together.

[![Screws to attach the servo horn](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-13.jpg)

You\'ll now need the single arm servo horn with 5 holes, as shown in the image below on the left. If the single arm servo with 5 holes was not included in the kit, you will need to modify one of the servo horn with 6 holes that was packaged separately. Shorten the horn by clipping off one hole as shown in the image below on the right and checking to see if it fits the mold on the tilt bracket. Be careful when clipping and make sure that you do not clip off too much of the horn.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-14.jpg "Single arm servo horn")](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-14.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Zero_Pan-Tilt_Bracket_Servo_Arm_Modification.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Zero_Pan-Tilt_Bracket_Servo_Arm_Modification.jpg)
  *Single arm servo horn with 5 holes.*                                                                                                                                                                       *Single arm servo horn with 6 holes being clipped.*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Install the single arm servo horn as shown below. You\'ll need two of the small self-tapping screws from the first step to affix it to the mechanism.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-16.jpg "Where to put the single arm servo horn")](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-16.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Zero_Pan-Tilt_Bracket_Attach_Servo_Arm_SelfTapping_Screws.jpg "Where to put the clipped single arm servo horn")](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Zero_Pan-Tilt_Bracket_Attach_Servo_Arm_SelfTapping_Screws.jpg)
  *Attaching the single arm servo horn.*                                                                                                                                                                                       *Attaching the clipped single arm servo horn.*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** If necessary, you can loosen screws on the brackets placed around the servo in order to attach the clipped single arm servo horn to the bracket. This will keep the screws straight when tightening the screws.

You\'ll now need the second servo motor and the last piece of the mechanism. The image below shows the relative orientation of these two pieces.

[![Assembly orientation of last servo and last piece of mechanism](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-17.jpg)

Here\'s a picture of the two pieces assembled to one another.

[![Putting the last two pieces together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-18.jpg)

Now, find the longest machine screws in the baggie, as shown below. Once again, you\'ll find that there are more of these than you need.

[![Long machine screws](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-19.jpg)

Thread these screws through the stand off wings on the servo motor and into the last piece of the mechanism. You can use nuts for these if you like, but I\'ve found it to be unnecessary as they thread into the mechanism quite snugly without the nut.

[![Threading in the long screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-20.jpg)

**Note:** For this tutorial, we used the longer screws. The shorter screws found in the baggie can also work. Depending on your personal preference, you can also use the shorter screws. They are long enough to hold the servo in place and reduces the possibility of the wires snagging against the longer screw.

Now connect the two major pieces of the assembly together. The image below shows the orientation of these two parts.

[![Orientation of last two parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-21.jpg)

You may need to assemble and disassemble these two parts a couple of times to find the right rotational position of the servo motor so that the tilting portion has its full range of motion. Here\'s an image of the two bits put together.

[![Final assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-22.jpg)

Take the final screw that you identified above as a horn attaching screw and use it to secure the horn to the servo motor.

[![Affixing the final horn to the servo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-23.jpg)

Congratulations, you\'ve finished assembly of the pan-tilt mechanism!

[![The finished assembly](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-24.jpg)

### Solder the Headers onto the Pi Zero W and Pi Servo Hat

We suggest soldering the male headers onto the Pi Zero W.

[![Male headers with Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-25.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-25.jpg)

My favorite trick for this type of situation is to solder down one pin, then melt the solder on that pin with the iron held in my right hand and use my left hand to adjust the header until it sits flat as shown below. Make sure that you are soldering with the header\'s shorter side and the longer pins are on the component side. After tacking down one pin, finish soldering all the pins down to the Pi Zero W.

[![Soldering on the Pi Zero W](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-26.jpg)

Repeat the steps with the female header and the Pi Servo Hat.

[![Female header](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-27.jpg)

Make sure to insert the short pins from the bottom of the board and add solder to the component side so that the Pi Servo Hat stacks on top of the Pi Zero W\'s male header pins. You will also need to make sure that the header is sitting level before soldering down all the pins.

[![Soldering to the servo shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-28.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-28.jpg)

### Affix the Camera Module to the Pan-Tilt Mechanism

Start by affixing the double stick foam tape to the pan-tilt mechanism as shown in the image below.

[![Placing the tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-29.jpg)

Next, attach the flex cable to the camera module. Take note of the copper \"fingers\" on the end of the cable. The side with the fingers on it should be **facing** the camera module circuit board. See the image below.

[![Flex tape in camera module](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-30.jpg)

Thread the flex cable through the pan-tilt mechanism as shown below, then press the back of the camera board against the double stick tape to adhere it to the pan-tilt mechanism.

[![Threading the camera flex cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-31.jpg)

Insert the flex cable from the camera into the Pi Zero W. As was the case with the other end, the side of the cable with the copper fingers should be facing the circuit board. Don\'t forget to close the clamping mechanism!

[![Camera ribbon into Pi Zero W](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-32.jpg)

You may now attach the Pi Servo Hat to the header on the Pi Zero W.

[![Shield on Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-34.jpg)

### Connect the Servo Motors to the Pi Servo Hat

The servo motors need to be connected to channels 0 and 1 on the Pi Servo Hat. Connect the \"pan\" servo (the one on the bottom) to channel 0 and the \"tilt\" servo to channel 1.

  -------------------------------------------------------------------------------------------------------------------
  Pi Servo Hat (CH 0)\   Pan Servo (Bottom of Pan-Tilt Mechanism)\   Pi Servo Hat (CH 1)\   Tilt Servo\
  ---------------------- ------------------------------------------- ---------------------- -------------------------
  SIG                    Control Signal (Orange)                     SIG                    Control Signal (Orange)

  POW                    Vcc (Red)                                   POW                    Vcc (Red)

  GND                    GND (Brown)                                 GND                    GND (Brown)
  -------------------------------------------------------------------------------------------------------------------

Once connected, your setup should look like the image below.

[![Assembled kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/Pi_Servo_Cam_Guide-36.jpg)

This completes the necessary steps of the hardware assembly!

## Configure the Raspberry Pi

Now that we\'ve hooked up our Pi Servo Hat and assembled the hardware, we\'re ready to boot the Raspberry Pi Zero W for the first time! To configure the Raspberry Pi, we need to:

- Power the Pi Zero W.
- Connect the Pi Servo Hat\'s Serial-to-USB Converter.
- Connect to the serial debugging console on the Pi Zero W.
- Enable camera interface, I2C, and SSH on the Pi Zero W.
- Update the software on the Pi Zero W.
- Download and install the camera interface software from GitHub.
- Make some changes to enable the pan-tilt control functionality.
- Download the Pi Servo Hat interface software from GitHub.
- Make some changes to start the Pi Servo Hat interface software on boot.

Let\'s walk through these steps in more detail!

### Power the Pi Zero W

Using a sufficient 5V wall adapter, we can power the Pi Zero W. Plug the wall adapter into a wall outlet for power. Then connecting the micro-b from the power supply to the Pi Zero W\'s micro-b connector labeled as \"PWR IN.\"

### Connect the Pi Servo Hat\'s Serial-to-USB Converter

With the Pi Servo Hat stacked on the Pi Zero W, take a micro-B USB cable and connect it to the Pi Servo Hat\'s micro-B connector. Insert the other end to a computer\'s standard USB port. This will allow you to connect the Pi through a serial port connection.

### Open a Serial Terminal

[] **Tip:** This setup uses a [headless setup](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/#serial-terminal) to configure the Raspberry Pi Zero. You could use the PIXEL desktop GUI if you access to a monitor and mini-HDMI adapter to enable the camera, I2C, and SSH through **Preferences \> Raspberry Pi Configuration** from the desktop menu.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/RaspberryPi_PIXEL_Desktop_View.jpg "Raspberry Pi PIXEL Desktop View")](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/RaspberryPi_PIXEL_Desktop_View.jpg)

Start by checking out our [serial terminal basics](https://learn.sparkfun.com/tutorials/terminal-basics) tutorial. This will get you up and running with a serial terminal. Open a serial terminal program (i.e. PuTTY) to connect.

When you make your connection to the Raspberry Pi, you\'ll need to connect the serial terminal to the COM port that it enumerated on and connect at a baudrate of 115200. Failure to use the proper baud rate setting will result in weird characters and your connection failing to work.

To figure out which port to connect to, I recommend using the Arduino IDE. Under the \"Tools\" menu, there is a sub-menu for \"Port\". Since we had connected the USB cable to a computer\'s COM port already, make note of the items on the listed COM Ports. Then unplug a micro-B USB cable from your computer. Give it a few seconds, then re-open that sub-menu to see what item has disappeared. By process of elimination, we can determine the COM port that the Raspberry Pi enumerated to. Reconnect the cable to the COM port to verify. The COM port should reappear as the same COM number in the sub-menu.

**Installing FTDI Drivers**: It\'s possible that you\'ll need to install FTDI drivers to get the COM port to appear. If the following instructions don\'t result in a port appearing in the list, visit our [FTDI driver installation tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers).

#### Windows

If you don\'t have the Arduino IDE installed and don\'t want to install it, you can find the same information using built in tools. Under Windows, open up your device manager (if you don\'t know how to do this, do a search online for OS specific information on how to do it since it\'s slightly different under various versions of Windows). Take note of the devices on the list, then unplug the Pi and see which port on the list disappears. The port which disappeared from the list is the one you want.

[![Windows device manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/dev_manager_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/dev_manager_1.png)

#### Mac

Using a Mac OS, you\'ll need to open a terminal window. To figure out which port the Pi has connected to, type this command:

    language:bash
    ls /dev/cu.usbserial-*

This will return a list of USB-Serial converter ports on the system. Take note of the devices on the list, then unplug the Pi and see which port on the list disappears. The port which disappeared from the list is the one you want. You can then connect to the port in question by typing

    language:bash
    screen /dev/cu.usbserial-XXXXXXXX 115200

where the XXXXXXXXX is replaced by information gleaned from the first command.

#### Linux

Under Linux, the process is similar to Mac OS, only use this command to identify the serial port:

    language:bash
    ls /dev/ttyUSB*

You may use \"screen\" to connect to the Pi:

    language:bash
    screen /dev/ttyUSBX 115200

Again, the \"X\" should be replaced with information gleaned from the `ls` command above. If you receive an error about screen not being installed, you can install `screen` by typing this command:

    language:bash
    sudo apt-get install screen

Then re-enter the above command to connect via `screen`.

### Log In to the Pi

When the Pi finishes booting (about 30 seconds) you should see a prompt on your serial terminal screen that looks like the image below. If you don\'t, try hitting the enter (or return) key. This will bring up the login information if it printed before you had your serial terminal ready.

[![Raspi login prompt](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/raspi_login.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/raspi_login.png)

Log in to the system using the username \"pi\" and the password \"raspberry\". You\'re now logged in to the Raspberry Pi, and everything else we do we\'ll do from this command prompt.

### Use the raspi-config Utility to Enable Camera, I2C, and SSH

There\'s a nifty text-only utility called \"raspi-config\" that will allow you to enable the camera interface, I2C, and remote access via SSH. To use it simply type this command:

    language:bash
    sudo raspi-config

If you\'re curious, the \"sudo\" portion of the command tells the OS to run the command as a superuser \-- basically, a user with full system permissions. This is the menu that you\'ll then be presented with:

[![raspi config menu](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/raspi-config-menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/raspi-config-menu.png)

From here you can make several changes. The first change you should make is to change the password for the default user. Highlight option 1 and hit enter. You\'ll get a warning that you will be asked to change the password, then a prompt will appear at the bottom of the screen asking you to enter a new password. You\'ll be asked to repeat it, just to make sure that the password is as you intended, then you\'ll receive a message that the password has been changed.

**Please change your user password!** Leaving the default user password with SSH enabled is a security risk that could allow a malicious user to take over your device remotely.

Now, use the arrow keys to move down to choice 5, \"Interfacing Options\". You\'ll be presented with this menu:

[![Interfacing options](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/interfacing_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/interfacing_options.png)

Highlight option \"P1 Camera\", and hit enter. That will bring up this screen:

[![Camera enable](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/camera_enable_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/camera_enable_1.png)

Highlight \"Yes\" and hit enter. You\'ll receive a confirmation message:

[![Camera enabled](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/camera_enabled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/camera_enabled.png)

Hit enter to leave this screen. You\'ll be back at the main menu. Return to the \"Interfacing Options\" menu again and repeat the process two more times, once for the \"I2C\" option and once for the \"SSH\" option.

This concludes the work you need to do with the raspi-config utility. From the main menu, press tab twice to highlight \"Finish\", then hit enter. If you\'re asked whether to reboot now, select \"Yes\" and hit enter. Again, it will take as much as 30 seconds for the login prompt to reappear.

### Configure the /etc/network/interfaces File

You\'ll now need to tell the Raspberry Pi to use the \"wpa_supplicant.conf\" file that you created earlier. Type the following command in the serial terminal:

    language:bash
    sudo nano /etc/network/interfaces

Add the following lines to the end of the file:

    language:bash
    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

Hit [CTRL]+[O] and enter to save the file, then [CTRL]+[X] to quit the nano text editor.

Now reboot the Raspberry Pi by typing:

    language:bash
    sudo reboot

### Update the Pi

You must now update your Pi\'s software to the latest version. To do this, enter these two commands at the command prompt:

    language:bash
    sudo apt-get update
    sudo apt-get dist-upgrade

This will ensure that your Pi software is up-to-date. The first command takes a minute or two to run, but the second will take much longer. Be patient!

### Install the Remote Camera Web Interface Software

You\'ll now want to download and install the camera interface software. To do so, execute the following four commands in order:

    language:bash
    git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
    cd RPi_Cam_Web_Interface
    chmod u+x *.sh
    ./install.sh

The first command fetches the software from GitHub. You don\'t need a GitHub account for this to work. However, if you enter the command or URL wrong, `git` may ask for a username. The second enters the directory that was just fetched from GitHub. The third changes the user permission of the shell scripts in that directory so a user can execute them. The fourth runs the install script for the software.

Running the fourth command will launch an interactive script allowing you to change various settings about how the software is set up. We\'ll walk you through it so your setup mirrors ours for the sake of the rest of the tutorial. It takes a minute or two for the interactive section to come up. Again, patience!

Here\'s the interactive interface for the installation script. **Use the arrow keys, not TAB, to move through the fields!** Note that we\'ve left everything the same. The only exception is that we added a username and password (but that\'s not shown). Once you\'ve finished entering a username and password, you may hit the TAB key to go to the \"OK\" button and hit \"Enter\" to select it.

[![Install script interface](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/install_sh.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/install_sh.png)

The installation script will download and install all of the dependencies for the project. This can take some time (up to several minutes) so be patient. When everything is finished, you\'ll be asked if you want to start the service now. Select \"Yes\".

[![Start now prompt](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/start_now.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/start_now.png)

## Test the Camera Web Interface 

Now let\'s make sure the camera is working before adding in the pan-tilt functionality. To do so, we first must determine the IP address of the Pi Zero W. Type this command:

    language:bash
    ifconfig

Doing so should bring up the following information:

[![ifconfig results](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/ifconfig.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/ifconfig.png)

There\'s lots of information here but we\'re only concerned with one small chunk: the \"inet addr\" entry in the \"wlan0\" section. In the example image above, that value is 10.8.252.217. This is the **IP address** of your camera.

Open up a web browser and type in that number plus \"/html\", for the web address. For example, I\'d type in \"10.8.252.217/html\" in the address bar. If everything works as expected, you should be presented with a login request. **This is the username and password that you entered when setting up the camera web interface, not the login information for the Pi itself!** You\'ll be rewarded with an interface screen similar to the one below.

[![RPi Cam Interface](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/8/picam_interface.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/picam_interface.png)

### Adding Pan-Tilt Support

The RPi Cam Interface software supports pan-tilt functionality, but it needs to be enabled. To do this, there are several steps required.

First, we must tell the software that we wish to enable pan-tilt functionality. This is done by renaming a file hidden deep within the directory structure using this command:

    language:bash
    sudo mv /var/www/html/pipan_off /var/www/html/pipan_on

After running this command, go back to your web browser and refreshing the camera interface. Upon reloading, the page should now have four directional arrows directly beneath the image, as seen below.

[![Pi Cam interface with arrows](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/directionial_arrows.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/8/directionial_arrows.png)

Next, we need to create a system pipe in order to send commands to the interface software that controls the pan-tilt functionality. A pipe is like a file, only it has no static contents. Only contents defined at run time by the program will control the motors.

    language:bash
    sudo mknod /var/www/html/FIFO_pipan p
    sudo chmod 666 /var/www/html/FIFO_pipan

### Controlling Motors on the Pi Hat

Now that we\'ve created the pipe from the interface software, we need to fetch the control software that runs the servo motors. We\'ve created a simple python program that does just that. Again, we\'re going to fetch that file from GitHub, using the following commands:

    language:bash
    cd
    git clone https://github.com/sparkfun/RPi_PanTilt_Camera_Kit.git
    python RPi_PanTilt_Camera_Kit/Firmware/pantilt.py &

The first command ensures that you are in the **/pi** user home directory; later instructions will depend upon that being the case. The second command fetches the program from GitHub, and the third executes it. As soon as you enter the third command, you should see and hear the motors twitch a little as the software centers them.

Now go back to the interface webpage and click on the various arrows. As you click on them, you should see the pan-tilt mechanism respond.

Finally, we need to set up our system to launch the pan-tilt software with the startup of the computer. To do this, we need to edit the \"rc.local\" file, which handles various on-boot functionality. To open the \"rc.local\" file, enter this command:

    language:bash
    sudo nano /etc/rc.local

This will launch the nano text editor with \"rc.local\" loaded into it. Use the down arrow key to scroll to the bottom of the file and add the following text **just above the line that reads \"exit 0\"**:

    language:bash
    python /home/pi/RPi_PanTilt_Camera_Kit/Firmware/pantilt.py &

It\'s important that you place that line above the \"exit 0\" line or it will never be executed. Now, hit [CTRL]+[o] to save the file and [CTRL]+[x] to quit nano text editor.

[] **Troubleshooting Tip:** This tutorial was written to control servo motors with **200Hz** PWM. For users having issues with the "loud" buzzing, try dropping the PWM signal down to **50Hz**. It should be less noticeable. To adjust:\
\

- Head to the [pantilt_50Hz.py](https://github.com/sparkfun/RPi_PanTilt_Camera_Kit/blob/master/Firmware/pantilt_50Hz.py) example in the **RPi_PanTilt_Camera_Kit/Firmware/** folder.

- Then modify the **rc.local** file using the following command as explained earlier:\
  \

      sudo nano /etc/rc.local

- Finally, either comment out or change the line you added to:\
  \

      python /home/pi/RPi_PanTilt_Camera_Kit/Firmware/pantilt_50Hz.py &

  \

*For more details on modifying the code, try checking out the [Pi Servo Hat Hookup Guide](https://learn.sparkfun.com/tutorials/pi-servo-hat-hookup-guide) and [PCA9685\'s datasheet](http://www.nxp.com/docs/en/data-sheet/PCA9685.pdf) for the I2C registers and settings needed to configure the Pi Servo Hat\'s PWM signals.*

------------------------------------------------------------------------

### Congratulations!

You\'ve completed the initial setup of your Raspberry Pi Zero W Pan-Tilt Camera! This is outside the scope of the tutorial but there are a few more things you might want to do:

- **Set up motion activation** - The [page documenting the interface software](http://elinux.org/RPi-Cam-Web-Interface) has useful information about setting up motion activated image capture.
- **Set a static IP address** - By default, the Pi Zero W may be assigned different IP addresses by the DHCP server on your network each time it boots. This can make interacting with the camera difficult, as you need to check the camera to figure out its IP address after each reboot. Setting up a static IP address is a complex topic and dependent upon the settings of your network, and is left as an exercise for the reader.
- **Communicate with the camera over SSH** - Now that the camera is up and connected to your WiFi network, you no longer need to connect to it via the serial cable. Connecting via SSH is relatively simple, and we won\'t go into the details here.

------------------------------------------------------------------------