# Source: https://learn.sparkfun.com/tutorials/sound-page-guide

## Introduction

Ready to make some interactive art?

[![The Sound Page Kit assembled](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-34.jpg)

Yes? Well, let\'s get started!

We will be using a tube of [Bare Conductive Paint](https://www.sparkfun.com/products/11521) that you will use to make shapes, silhouette, and patterns. As long as you connect the ink back to the [LilyPad MP3 board](https://www.sparkfun.com/products/11013) you can interact with the piece. When you touch one of the silhouettes, a sound will play from the speaker. While the paint does conduct electricity, don\'t worry, it\'s very little electricity. It won\'t shock you.

This tutorial is based on the Bare Conductive Paint Wall featured in ElectriCute!

ReplaceMeOpen

ReplaceMeClose

### Materials Used

You will need a few components to follow along with this tutorial. Here is what you will need:

Additionally, you will need:

- Foam Brush
- Canvas (this can be paper, cardstock, etc.)
- Stencils (if you want to make silhouettes, but you can free-hand anything you want!)

We have labeled the materials in this picture, so you know what we are talking about in the rest of the guide.

[![Parts you\'ll need for the Sound Page Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Parts.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Parts.png)

### Recommended Reading

Before getting started with the Sound Page Kit, you might want to read about the technology that goes into it:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) \-- The LilyPad MP3 board works with Arduino! This is useful if you want to reprogram the board to do other things
- [Getting Started with the LilyPad MP3 Player](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player) \-- Learn a little about what the LilyPad MP3 board is. Technically, you are supposed to use conductive thread and sew into the pads around the edge, but we\'re going to use conductive paint instead!

## Attach the Electronics

**IMPORTANT:** Read all of the directions in this section before doing anything first! You will need to perform them relatively quickly so that the paint does not completely dry while you attach the electronics. If some of the paint does dry, simply add more paint when you want to attach the electronics.

[![Touching the conductive paint wall](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Touching_the_wall.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Touching_the_wall.jpg)

*We will be using the printed cardstock in this tutorial, but you can use any surface, like a wall!*

If you do not have the printed cardstock, you can download the artwork here. Just download the file and print it on cardstock or paper!

[Download Printed Cardstock File](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/printed_cardstock.zip)

[![Cardstock artwork](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-02.jpg)

*Printed cardstock*

If you want to create stencils the same way we did, you will need to buy some sticky-but-not-too-sticky label paper. We used [this stuff from onlinelabels.com](http://www.onlinelabels.com/Products/OL176WR.htm?search=OL176WR&st=s). You will also need to download the stencils we made, and print them out on the label sheet. You can use an X-Acto knife to cut the stencil (we did ours with a laser engraver so we could make lots of them).

[Download Electronics Stencils](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/circuit_stencils.zip)

[![Electronics stencils](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-03.jpg)

*Electronics stencils*

### Create the LilyPad Footprint

The first thing we need to do is create the LilyPad board footprint in conductive ink so that we have a place to stick the electronics.

Separate the LilyPad MP3 footprint stencil from the rest of the stencils. Peel off the backing of the footprint stencil, and place it over the outlines. Make sure that the traces are facing toward the top of the page. They will be connected to our silhouettes!

[![Placing a stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-04.jpg)

Squeeze some conductive ink on the stencil, and use the foam brush to fill in the stencil with the ink. Make sure the spaces in the stencil get covered in ink completely! You don\'t want it to be splotchy, otherwise it won\'t conduct electricity very well.

[![Dabbing conductive paint](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-05.jpg)

While the paint is still wet, carefully peel the stencil off the page.

[![Peeling the stencil off the cardstock](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-06.jpg)

### Place the LilyPad Board

If any of the paint has dried, we recommend you add a drop of conductive paint to each of the circles where the LilyPad MP3 board will go.

[![Adding more paint](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-08.jpg)

Carefully place the LilyPad MP3 board so that the holes on the edge line up with the circles of paint that we just made with the stencils.

**IMPORTANT:** Make sure that the SD card slot (the one by the holes labeled \"RIGHT SPEAKER\") is facing down and the headphone jack is facing up. The label \"LEFT SPEAKER\" should be facing the \"LEFT SPEAKER\" text on the cardstock.

[![Placing the LilyPad MP3 board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-07.jpg)

You will want the paint on to squish up into the holes a bit. This is how we make sure electricity can flow from the board to the touchable artwork!

[![LilyPad MP3 board added](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-09.jpg)

We want the board to make a good electrical connection to the traces we just made with the conductive ink. So, add a drop of conductive paint to each of the 12 holes around the edge of the LilyPad board.

[![Adding paint to the holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-10.jpg)

### Add the Speaker

You can use the headphones jack at the top of the LilyPad board to connect to a large set of speakers if you want to pump out some real sound (feel free to skip this step if you are doing that!). We can also add a small speaker to the LilyPad MP3 board to get sound out.

If you want to add the small speaker, add a drop of conductive paint to each of the \"LEFT SPEAKER\" holes.

[![Adding a drop of paint to the speaker holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-33.jpg)

With the paint in the LilyPad holes still wet, insert the pins of the speaker into the holes labeled \"Left Speaker.\" It doesn\'t matter if the + and - of the speaker lines up with the + and - of the holes.

**NOTE:** IF you want to hold the speaker in place, you can add a drop of hot glue underneath the speaker. Don\'t worry, it won\'t hurt the electronics.

[![Attach the speaker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-11.jpg)

**NOTE:** The speaker will be a bit wobbly in the holes. Let the paint dry completely (a few hours) before touching the speaker again. You can complete the rest of the tutorial, but just be careful around the speaker!

[![Speaker added](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-12.jpg)

**IMPORTANT:** Make sure that the pins from the speaker do not touch any of the pins labeled \"5V FTDI\" on the LilyPad board!

[![Make sure the pins do not touch!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-13.jpg)

### Add the Resistors

Using a set of pliers, tweezers, or your fingers, carefully roll the ends of two resistors to make little spirals.

[![Curl resistor leads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-14.jpg)

Bend the curled ends down, and then flatten them so that the resistor is elevated.

[![Bend the resistor leads to elevate the component](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-15.jpg)

Find the resistor locations, which are marked in red on the printed cardstock. Add a drop of paint on each of the circular pads around the resistor locations.

[![Adding more paint to hold the resistors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-16.jpg)

Place one resistor so that it connects the trace from T1 to the trace from T2 (these labels can be found on the LilyPad MP3 board). If you are using the printed cardstock, the location of the resistors are marked in red. Place the second resistor so that it connects the trace from T2 to the trace from T4.

[![Placing the resistors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-17.jpg)

Just like we did with the LilyPad board, we will want to add a drop of paint to each of the curled resistor leads so that they stay in place.

[![Adding a drop of paint on top of the resistor leads](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-18.jpg)

**WAIT:** at least 15 minutes for the paint to dry before moving on to the next step.

## Make Some Art

### Make Some Silhouettes

The next thing we need to do is choose which two of the stencils we want to put on our Sound Page. You are also welcome to print your own stencil or just create whatever are you want! This is art, after all. Just make sure that:

1.  Anything you create is completely filled in with ink. Splotchy areas won\'t conduct!
2.  The shapes/pictures you create are connected to the ink traces coming out of the footprint we just made. If it\'s not connected, it won\'t conduct, and you won\'t be able to interact with it!

Just like with the stencil for the electronics, we used label sheets to create stencils for the silhouettes. You are welcome to print out the ones we made or make your own stencils:

[Download Silhouette Stencils](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/silhouette_stencils.zip)

[![Silhouette stencils](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-19.jpg)

*Silhouette stencils*

Pick one of the stencils, detach it from the sheet, and peel off the backing. Stick it on the page in the desired location (we suggest you make it fairly close to one of the traces coming from the LilyPad footprint).

[![Attaching a stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-20.jpg)

Just like the footprint stencil, dab ink with the foam brush so that it completely fills your stencil.

[![Painting in a stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-21.jpg)

Immediately (but carefully!) peel the stencil off the page while the paint is still wet. If some of the stencil breaks off, you can carefully remove the stuck pieces with tweezers.

[![Peeling off the stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-22.jpg)

Admire your stencil art!

[![First stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-23.jpg)

Repeat the process to add a second silhouette.

[![Two silhouettes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-24.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-24.jpg)

### Fill in the Spots

If a patch of conductive paint is not connected to the LilyPad MP3 board, you won\'t be able to touch it to make sounds!

Using a brush or the squeeze tube of conductive paint, carefully connect all of the black areas in the silhouettes (or at least the patches you want to be able to touch).

[![Connecting all the paint patches in a silhouette](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Annotated_Patches.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Annotated_Patches.png)

**WAIT:** At least 15 minutes before moving on the next step to allow the paint to dry.

### Connect the Silhouettes to the Traces

Make sure that the silhouettes are connected to the traces that lead to the LilyPad MP3 board (with conductive paint, of course). For example, in the silhouette below, the paint around the face has been connected with conductive paint (except for the part above the eyes; you will not be able to touch those unless you connect them with paint!). However, the entire silhouette is not connected to the trace!

[![Silhouette not connected to trace](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-26.jpg)

If you need to create lines with conductive paint to connect the traces to the silhouettes, use the straight line stencils.

[![Straight line stencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-27.jpg)

**WAIT:** Once again, wait at least 15 minutes for the paint to dry before moving on. In the meantime, admire your work!

[![Completed page](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-28.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-28.jpg)

### Protect Your Work

You can use a sealer, like [clear spray paint](http://www.amazon.com/Krylon-6-Ounce-Crystal-Acrylic-Coating/dp/B001K65K26/ref=sr_1_1?ie=UTF8&qid=1431109403&sr=8-1&keywords=krylon+acrylic+crystal+clear) to protect your work. Just be careful not to spray too much on the electronics! If you coat the connections for the SD card, for example, the LilyPad MP3 board might not be able to read it. Don\'t worry, you will still be able to activate the sounds through the clear coat.

[![Sealing the silhouettes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-37.jpg)

Additionally, you can frame your work to protect the edges and display it nicely!

[![Framing the Sound Page](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-39.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-39.jpg)

## Load Some Sounds

We put together a selection of sound clips that correspond to the silhouette stencils that we made. If you would like to learn how to create your own sound clips, see the [Hacking Your Kit](https://learn.sparkfun.com/tutorials/sound-page-guide#hacking-your-kit) section.

### Add Sounds to the Card

Download the sound clips file:

[Download Sound Page Clips](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/sound_page_clips.zip)

Extract the files.

[![Extract files](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_01a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_01a.png)

*Windows: Right-click on the .zip file and select \"Extract All\" or \"Extract Here\"*

Double-click on each of the sound clips to listen to them. The names were kept short (4 characters) to help the LilyPad MP3 board read them. For reference:

  File Name    Description
  ------------ ------------------
  \_bots.wav   Autobots
  \_dlel.wav   Dalek
  \_mkjy.wav   Mockingjay
  \_shld.wav   S.H.I.E.L.D
  \_shlk.wav   Sherlock
  \_wntr.wav   Winter is coming

\

Using a [micro SD card reader](https://www.sparkfun.com/products/13004), insert the card into your computer. Choose the 2 sound clips you want to have played and copy them to the SD card.

[![Copying sound clips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_02.png)

This part is **important**! You need to rename the two sound clips and add a number in front of them. For the silhouette connected to the T1 on the LilyPad MP3 board, add a \'1\' in front of the name of the clip you want associated with it. For the silhouette connected to T4, add a \'2\' in front of the filename.

[![Adding prefix numbers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_03.png)

*Add \'1\' and \'2\' to the front of the sound clip filenames to associate them with the silhouettes on the page*

Eject the SD card from your computer.

[![Eject SD card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_04.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_04.png)

*Windows: Right-click on the drive and select \'Eject\'*

### Insert the SD Card

Remove the SD card from your computer and insert it into the LilyPad MP3 board.

[![Inserting the micro SD card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-29.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-29.jpg)

## Play With Your Art

### Plug It in

Attach the [barrel jack to JST cable](https://www.sparkfun.com/products/8734) to the LilyPad MP3 board\'s JST connector.

[![Plugging in the JST cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-30.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-30.jpg)

Connect the [wall adapter](https://www.sparkfun.com/products/12889) to the barrel jack of the JST cable and plug it into the wall.

[![Plugging in the wall adapter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-31.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-31.jpg)

### Turn It on

Find the power switch on the LilyPad MP3 board and flip it to ON.

[![Turning on the power](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-32.jpg)

### Play!

Touch one of the silhouettes. As soon as you remove your finger, you should hear glorious sounds coming out of the little speaker!

[![Touching a silhouette](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-34.jpg)

### Help! I Don\'t Hear Any Sounds

This might happen. If you don\'t hear any sounds coming out of the little speaker when you touch and remove your finger from one of the silhouettes, check a few things:

- Carefully look underneath the speaker to make sure the speaker nor any paint is touching the ground pin for port labeled \"5V FTDI\". You might have to remove the speaker, remove any globs of paint that might be jumping up to a \"5V FTDI\" pin, add more paint to the \"LEFT SPEAKER\" pads, and replace the speaker.
- Try connecting some headphones to the headphones jack to see if you get any sound.
- Wiggle the resistors to make sure that they are truly connected to the conductive paint traces.

## Hacking Your Kit

Have you had enough of just two silhouettes making sound? Well, read on! We will briefly cover how you can hack the kit to get more out of it.

### More Sound!

If you find that the small speaker is too small, too flimsy, or just not loud enough, you can provide your own speakers! The 1/8\" audio jack at the top of the LilyPad MP3 board can accept any standard headphones or speaker audio plug.

[![All the sound!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-35.jpg)

*Pump up the volume.*

### Adding a Third Silhouette

As it so happens, the LilyPad MP3 board will support a third silhouette. This tutorial was kept simple with only 2 silhouettes, but you can add a third. The problem is that you have to connect the third silhouette with conductive paint traces to T5 and across a resistor to T2. You can either punch a hole through the paper and go behind the other traces, or you can go around the second silhouette, as in the picture below.

**NOTE:** You will need a third [1 MΩ resistor](https://www.sparkfun.com/products/11853).

[![3 silhouettes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/Sound_Page_Kit_Tutorial-38.jpg)

Additionally, you will need to copy a third sound clip to the SD card and rename the file so that a \"3\" is the first character.

[![Rename the third sound clip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_05.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_05.png)

### Making New Sounds

So, you want to make your own sounds, eh? Well, here\'s how it\'s done.

First, find, make, or record some sound. It can be in any format, but for this example, we will download a WAV file.

Download and install [Audacity](http://sourceforge.net/projects/audacity/). If you want to learn how to use Audacity, check out [these tutorials](http://wiki.audacityteam.org/wiki/Category:Tutorial).

We advice making the audio mono, especially if you are using 1 speaker. This can be found under Tracks → Stereo Track to Mono.

[![Combining stereo to mono](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_06a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_06a.png)

If you want to keep the file size small, you can choose a different sampling rate. In the bottom left corner of the Audacity window, select a new sampling rate from \"Project Rate\". As long as the sampling rate is equal to or less than 48000 Hz, the clip should work with the LilyPad MP3.

[![New sampling rate](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_07.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/sound_page_clips.zip)

You can also use Audacity to adjust the volume, add filtering, or crop any piece of the audio clip you want.

Once you are finished, select File → Export Audio or Export Selected Audio. In the Export window, select \"WAV (Microsoft) Signed 16 bit PCM\". The LilyPad MP3 board will play a variety of file formats. Read more about the supported formats [here](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player#supported-audio-formats). Make sure that the new file name begins with a number (1-3, corresponding to the number of the silhouette) and is 6 characters or less.

[![Saving the new file](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/6/6/screen_08.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/6/6/screen_08.png)

Once you click \"Save,\" you might be presented with another window asking for file information. Feel free to fill it out or just click \"OK\" to save the file. Copy the file to your micro SD card, and plug it into your LilyPad MP3 board. Your custom sound is ready to be played!

### Customizing the Code

You will need a [5V FTDI Breakout Board](https://www.sparkfun.com/products/9716) to reprogram the LilyPad MP3 board.

Download and install the Arduino IDE. Read [this tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) to learn how to do that.

Download the Sound Page Kit source code.

[Download Source Code](https://github.com/sparkfun/Sound_Page_Kit/archive/master.zip)

Unzip the file, install the 3 libraries that are in Sound_Page_Kit/Libraries (CapacitiveSensor, SdFat, and SFEMP3Shield). Read [this tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) to learn how to install Arduino libraries.

The code that shipped with the Sound Page Kit can be found in Sound_Page_Kit/Firmware/Sound_Page_Kit/Sound_Page_Kit.ino. Open the Sound_Page_Kit.ino file in the Arduino IDE and hack away!

If you would like to learn more about the LilyPad MP3 board, read [this tutorial](https://learn.sparkfun.com/tutorials/getting-started-with-the-lilypad-mp3-player).

**NOTE:** You must unplug the FTDI board from the LilyPad MP3 board in order to use the T4 and T5 pads.