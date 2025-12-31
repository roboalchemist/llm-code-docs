# Source: https://learn.sparkfun.com/tutorials/spectacle-light-board-hookup-guide

## Spectacle Light Board

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects. It has connections for up to three strands of addressable LEDs and a connector for external power.

[![Spectacle Light Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/9/1/14052-01.jpg)](https://www.sparkfun.com/spectacle-light-board.html)

### [Spectacle Light Board](https://www.sparkfun.com/spectacle-light-board.html) 

[ DEV-14052 ]

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects in a streamlined ...

**Retired**

### tl;dr (essentials)

1.  If more than approximately 10 pixels will be on at once, we recommend powering the Light Board through the onboard micro B USB port.
2.  For smaller numbers of pixels, it is possible to power them directly over the Spectacle control cable.
3.  Most of the LED effects want a continuous type signal, such as the Button board \"Latch On/Latch Off\" function.
4.  Only WS2812 (NeoPixel) type addressable LED strips will work with the Spectacle Light Board.

### Meet the Spectacle Light Board

Designed to make it easy to add relatively complex lighting effects to your Spectacle projects, the Spectacle Light Board integrates with the rest of the Spectacle ecosystem to allow you to control lighting effects relatively effortlessly.

It has two 1/8\" (3.5mm) jacks for Spectacle control signals. **Pay attention to the directionality of the jacks!** The one labeled \"In\" should be plugged into a board that is closer to the Director Board than the Light Board is, or into the Director Board itself.

[![Signal jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_jacks.png)

The Light Board supports up to three strands of [addressable LEDs](https://www.sparkfun.com/products/12025). Each strand can have up to 60 individual pixels. **Not all types of addressable LEDs are compatible with the Spectacle Light Board.** If you have questions about whether or not a particular type of LED strip is compatible with the Light Board, contact SparkFun technical support.

[![LED Strand Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_connectors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_connectors.png)

The Light Board has a Micro B USB connector to allow it to be directly powered by an external power supply. **The relatively slender audio cables the Spectacle data travels over are not adequate for the large amount of current drawn by more than a few pixels.**

[![USB Power Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_usb_jack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_usb_jack.png)

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## The Configuration Utility

### Spectacle Light Board

[![Action list for light board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)

The Light board supports 9 different actions. Most of them want a continuous-type signal input, although a couple of them can be used with momentary input signals. We\'ll cover the difference under each action. Each action will have a field for the number of pixels the lightstrip that action is being applied to has, the use of which should be fairly apparent, and which we won\'t mention again.

#### Rainbow Effect

[![Rainbow effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/rainbow_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/rainbow_effect.png)

The rainbow effect displays a rainbow of colors across the strip, changing the color of each pixel indvidually to make it appear as though the rainbow is scrolling along the lightstrip.

- **\"While channel number \... is active\"** - The rainbow effect persists only while the channel is active, so a continuous input signal is needed.
- **\"rainbow scroll lightstrip number \...\"** - Select which lightstrip you wish the rainbow effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **scroll speed slider** - controls how fast the pattern moves as it scrolls past.

#### Theater chase

[![Theater chase settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/theater_chase.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/theater_chase.png)

Theater chase mode behaves like a marquee light border. The lights will march along making it appear as though the lightstrip is moving in steps.

- **\"While channel number \... is active\"** - The theater chase effect persists only while the channel is active, so a continuous input signal is needed.
- **\"theater chase lightstrip number \...\"** - Select which lightstrip you wish the theater chase effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **chase speed slider** - controls how fast the pattern moves as it scrolls past.
- **color picker input** - allows you to select the color of the lights.

#### Scanning effect

[![Scanning effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/scanning_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/scanning_effect.png)

Scanning mode sees a small group of lights bouncing back and forth along the length of the lightstrip, reminiscent of Cylons from Battlestar Galactica.

- **\"While channel number \... is active\"** - The scanning effect persists only while the channel is active, so a continuous input signal is needed.
- **\"scan lightstrip number \...\"** - Select which lightstrip you wish the scanning effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **scan speed slider** - controls how fast the pattern moves as it scrolls past.
- **color picker input** - allows you to select the color of the lights.

#### Twinkle effect

[![Twinkle effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/twinkle_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/twinkle_effect.png)

Causes individual lights on the selected strip to perform a twinkling action.

- **\"While channel number \... is active\"** - The twinkle effect persists only while the channel is active, so a continuous input signal is needed.
- **\"twinkle lightstrip number \...\"** - Select which lightstrip you wish the twinkle effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights.
- **speed slider** - controls how often the twinkles occur.
- **magic slider** - controls how magical the twinkles are. Play with it!

#### Lightning effect

[![Lightning effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/lightning_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/lightning_effect.png)

Causes the entire strip to strobe in a manner that looks a lot like a lightning flash.

- **\"While channel number \... is active\"** - The lightning effect persists only while the channel is active, so a continuous input signal is needed.
- **\"lightning on lightstrip number \...\"** - Select which lightstrip you wish the lightning effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights.
- **speed slider** - controls how often the lightning strike occurs.
- **fury slider** - controls how furious the lightning is. Play with it!

#### Flame effect

[![Flame effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/flame_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/flame_effect.png)

Causes the entire strip to crackle like a fire.

- **\"While channel number \... is active\"** - The flame effect persists only while the channel is active, so a continuous input signal is needed.
- **\"make fire on lightstrip number \...\"** - Select which lightstrip you wish the flame effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights. Experiment with different colors!

#### Fade effect

[![Fade effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fade_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fade_effect.png)

The lightstrip will change from one color to another over time, then back to the first.

- **\"While channel number \... is active\"** - The fade effect persists only while the channel is active, so a continuous input signal is needed.
- **\"fade lightstrip number \... back and forth\"** - Select which lightstrip you wish the fade effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **\"from color\" color picker** - This is the initial color that the lightstrip will power up with.
- **\"to color\" color picker** - The other color, which the strip fades to and from periodically.
- **\"fade speed\" slider** - Controls how fast the fading action occurs.

#### Fill

[![Fill settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill.png)

Fills some number of lights on the light strip with a single color. Blanks the other lights to off.

- **\"listen to channel number \...\"** - A momentary signal on this channel is all that is needed to trigger a fill operation, and the fill will persist until another effect starts.
- **\"wait for \... seconds\"** - This delay allows for sequencing effects. Most often you\'ll probably set it to 0.
- **\"clear lightstrip number \...\"** - Select the lightstrip to operate upon.
- **\"and fill \... pixels\"** - The number of pixels, from closest to the Light board out, to turn on.

#### Light pixel

[![Pixel settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/pixel.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/pixel.png)

Turns on one light and blanks the rest of the lights to off.

- **\"listen to channel number \...\"** - A momentary signal on this channel is all that is needed to trigger a light pixel operation, and the lit pixel will persist until another effect starts.
- **\"wait for \... seconds\"** - This delay allows for sequencing effects. Most often you\'ll probably set it to 0.
- **\"clear lightstrip number \...\"** - Select the lightstrip to operate upon.
- **\"and light pixel number \... \"** - The number of the pixel, from closest to the Light board out, to turn on.

## Example Project

Let\'s use the Spectacle Light Board to put together a working project! We\'re going to use a \"virtual board\" to blink a lightstrip attached to the Light Board.

#### Connect the boards

To follow along with this tutorial, you\'ll need the following hardware:

[![Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/2/8/13831-01a.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html) 

[ TOL-13831 ]

This is a high-quality switching \'wall wart\' AC to DC 5.1V 2,500mA USB Micro-B wall power supply manufactured specifically fo...

[ [\$13.95] ]

[![LED RGB Strip - Addressable, Bare (1m)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/5/3/12025.jpg)](https://www.sparkfun.com/products/12025)

### [LED RGB Strip - Addressable, Bare (1m)](https://www.sparkfun.com/products/12025) 

[ COM-12025 ]

These are bare addressable 1 meter long 5V RGB LED strips that come packed with 60 WS2812s per meter. As these are bare LED s...

**Retired**

[![Spectacle Director Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/7/9/13912-01.jpg)](https://www.sparkfun.com/products/13912)

### [Spectacle Director Board](https://www.sparkfun.com/products/13912) 

[ DEV-13912 ]

The Spectacle Director Board controls all the actions in a Spectacle project. Though the Director Board doesn\'t do too much o...

**Retired**

[![Spectacle Light Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/1/14052-01.jpg)](https://www.sparkfun.com/spectacle-light-board.html)

### [Spectacle Light Board](https://www.sparkfun.com/spectacle-light-board.html) 

[ DEV-14052 ]

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects in a streamlined ...

**Retired**

[![JST to JST-SM Wire - 1ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/9/14165-01.jpg)](https://www.sparkfun.com/products/14165)

### [JST to JST-SM Wire - 1ft](https://www.sparkfun.com/products/14165) 

[ CAB-14165 ]

This simple 24AWG wire is terminated with a male JST connector at one end and a male JST-SM connector at the other. Each wire...

**Retired**

**Note that you will need two of the TRRS cables!**

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

Now, plug the free end of the first cable into the \"In\" jack on the Light Board. **Pay attention to which jack you plug into, as the two jacks are directional.**

[![Light board input jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/Spectacle-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/Spectacle-11.jpg)

Next, you\'ll need the JST-SM to JST-PH adapter cable. Plug the white end into connector position 0 on the Light Board.

[![Adapter into light board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/Spectacle-12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/Spectacle-12.jpg)

Plug the black end of the adapter into the mating connector on the light strip.

[![Adapter into light strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/Spectacle-13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/Spectacle-13.jpg)

Finally, plug the Micro B end of the power adapter into the Director Board, and the other end into the wall. You should see one solid light and one blinking light on the Light Board. On the Director Board, you\'ll see one solid light and one light which blinks one time, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

[![Blank project page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)

When you first open the Spectacle app webpage, this is what you\'ll see. Your project name will differ from mine, as Spectacle assigns a random name to each project.

[![add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)

To continue, we must tell the project which boards we wish to use. Start by clicking the \"Add a board\" button at the bottom of the page.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)

This will bring up a list of the available boards. Click anywhere in the \"Lights\" box to add a Light Board to the system.

[![Light board edit button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/edit_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/edit_button.png)

Now that you\'ve added the Light Board, it\'s time to add the actions to the light board. To get a blink effect, we\'re going to trigger two events on one signal, and make one delayed slightly. Click the clapboard icon as highlighted in the above picture to bring up the list of actions assigned to that board.

[![No actions assigned](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/no_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/no_actions.png)

Naturally, there are no actions in the list, since we haven\'t added any yet. Click the \"Add an Action\" button at the bottom of the screen to bring up a list of available actions.

[![Actions list for light board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/actions_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/actions_list.png)

Here\'s the list of Light Board actions that will pop up when you hit the \"Add an Action\" button. We want to add an action of the \"Fill Color\" type, so click on that entry.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/fill_blank.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/fill_blank.png)

Here\'s the \"Fill Color\" action list of options. See [the previous page of the tutorial](https://learn.sparkfun.com/tutorials/spectacle-light-board-hookup-guide#the-configuration-utility) for information about the various fields.

[![Fill with settings in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/fill_with_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/fill_with_options.png)

Fill in the blanks of the page as seen above. This sets up the strip to turn on to solid white when an event hits channel 0. Now, add another \"Fill Color\" type action and scroll down so it\'s completely visible.

[![settings for second fill page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/second_fill_with_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/second_fill_with_options.png)

Once you\'ve added the second \"Fill Color\" action, set the fields as shown above. This will cause it to trigger on the same action as the first fill, but it won\'t activate for two seconds. Then, it will set all the lights on the strip to \"black\" (off).

[![Go back button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/go_back_button.png)

Click the \"Go Back\" button to return to the main screen. Clicking this button automatically saves your work, as well.

Now, repeat the steps from above to add a Virtual Board. Click the clapboard icon to edit the list of actions for the Virtual Board.

Virtual Boards provide a number of functions outside of the normal operation of Spectacle boards. In this case, we want \"Periodic Input\", which generates a signal at a fixed timing rate.

[![list of Virtual Board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/vb_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/vb_options.png)

Here are the actions we can use with a Virtual Board. We want a \"Periodic Input\", to create our blinking action.

[![Periodic settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/periodic_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/periodic_settings.png)

You should set up the periodic action to match the settings above. This will generate a short pulse every 10 seconds. Now click \"Go Back\" again to return to the main page.

[![Finished project](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/finished_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/finished_project.png)

Congratulations! You\'ve finished the configuration step of the process. Now it\'s time to move on to loading the project onto your Director Board.

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.