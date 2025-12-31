# Source: https://learn.sparkfun.com/tutorials/spectacle-button-board-hookup-guide

## Spectacle Button Board

The Spectacle Button Board allows you to add input from buttons or switches to your Spectacle projects. It has a total of 9 signal inputs, eight of which can come from external buttons and one button directly on the board.

[![Spectacle Button Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/7/1/14044-01.jpg)](https://www.sparkfun.com/products/14044)

### [Spectacle Button Board](https://www.sparkfun.com/products/14044) 

[ DEV-14044 ]

The Spectacle Button Board allows you to add input from buttons, switches or other contact-type sensing devices to your Spect...

**Retired**

### tl;dr (essentials)

1.  Buttons or switches can be connected to the board by pushing wires into the \"poke home\" type connectors on the board.
2.  Up to nine signals are available.
3.  Button signals can be either momentary or continuous.

### Meet the Spectacle Button Board

Designed to bring simple signals from the world into your Spectacle projects, the Spectacle Button Board provides input for any of your Spectacle projects.

It has two 1/8\" (3.5mm) jacks for connecting to other boards in a Spectacle system. Note that the Spectacle data jacks are directional: the one marked \"In\" should be plugged into the \"upstream\" board (i.e., closer to the Director Board than this one) and the one marked \"Out\" connects to the next downstream board.

[![Audio jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/button_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/button_jacks.png)

There are 8 \"poke home\" connectors on the Button Board. Each one can be connected to one (or more) buttons. To add a connection, simply push the stripped end of a wire into the hole on the connector. The connector will automatically grab on and hold the wire in place. If you need to remove the wire later, an small object (bobby pin, ballpoint pen, etc.) can be used to depress the release button, allowing the wire to be extracted without damage.

[![Poke home connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/button_poke_home.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/button_poke_home.png)

There is an input button on the button board itself which can be used to provide an input signal if no other buttons are available. It functions like any other normal button that might be attached. **Be certain you\'re pressing the button labeled \'8\' and not the one labeled \'Reset\'!** Pressing the reset button will reset your button board, probably causing your entire system to stop working properly until you reset your Director Board!

[![Onboard Button 8](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/button_button_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/button_button_8.png)

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## The Configuration Utility

### Spectacle Button Board

[![Button board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)

For the Button board, there are five options: three which produce a momentary pulse type output and two that produce a continuous switch type output.

##### Action on press

[![Action on press options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)

Trigger an action when a button is first pressed, regardless of how long it is subsequently held down.

- **\"When button number \... is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \...\"** - A single, momentary pulse will be sent out on this channel. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip. It is not suitable for continuous sound playback or for turning on a light strip effect, for instance.

##### Action on release

[![action on release options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_release_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_release_1.png)

Trigger an action when a button is released, regardless of how long it has been held down prior to being released.

- **\"When button number \... is released\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \...\"** - A single, momentary pulse will be sent out on this channel. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip, but not for continuous sound playback or for turning on a light strip effect, for instance.

##### Action on press or release

[![Action on press or release options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_release_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_release_2.png)

Trigger an action when a button is pressed, then trigger the same action again when the button is released.

- **\"When button number \... is either pressed or released\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \...\"** - A single, momentary pulse will be sent out on this channel both at the time the button is pressed and at the time it is released. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip, but not for continuous sound playback or for turning on a light strip effect, for instance.

##### Action while holding

[![Action while holding options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_while_holding_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_while_holding_1.png)

Trigger an event as soon as a button is pressed, then continue to trigger that event as long as the button is held down.

- **\"While button number \... is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"activate channel number \...\"** - A continuous signal will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on (at least, while the button is held) a lighting effect.

##### Latch On/Latch Off

[![Latch On/Off options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)

This action is like a latching power switch. One press turns the signal on, another later press turns the signal off.

- **\"While button number \... is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"activate channel number \... until button is pressed again\"** - A continuous will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on a lighting effect.

## Example Project

Let\'s use the Spectacle Button Board to make a project! Obviously, we need to have some kind of output board as well, so we\'ll use a Light Board. The project will use the button board to turn the Light Board\'s Scanning Effect on and off.

#### Connect the boards

For this tutorial, you\'ll need the following products:

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

[![Audio Cable TRRS - 3ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/8/14164-01.jpg)](https://www.sparkfun.com/products/14164)

### [Audio Cable TRRS - 3ft](https://www.sparkfun.com/products/14164) 

[ CAB-14164 ]

This is a 3-foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are th...

**Retired**

[![JST to JST-SM Wire - 1ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/9/14165-01.jpg)](https://www.sparkfun.com/products/14165)

### [JST to JST-SM Wire - 1ft](https://www.sparkfun.com/products/14165) 

[ CAB-14165 ]

This simple 24AWG wire is terminated with a male JST connector at one end and a male JST-SM connector at the other. Each wire...

**Retired**

**You will need three of the TRRS cables!**

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

Then take the other end of the first TRRS cable and plug it into the \"In\" jack on the Button Board.

[![Cable into button board in jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/Spectacle-17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/Spectacle-17.jpg)

Grab another of the TRRS cables and plug it into the \"Out\" jack on the Button Board.

[![Cable into out on button board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/Spectacle-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/Spectacle-18.jpg)

Plug the other end of that cable into the \"In\" jack on your Light Board.

[![Cable into IN jack on light board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/Spectacle-19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/Spectacle-19.jpg)

Now plug your lightstrip adapter cable into the Light Board\...

[![Light strip adapter into light board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/Spectacle-20.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/Spectacle-20.jpg)

\...and plug the lightstrip into the other end of that adapter.

[![light strip adapter into light strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/5/Spectacle-21.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/5/Spectacle-21.jpg)

Finally, plug the Micro B end of the power adapter into the Director Board, and the other end into the wall. You should see one solid light and one blinking light on the Light board and the Button board. On the Director Board, you\'ll see one solid light and one light which blinks eight times, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

When you first open the Spectacle app webpage, this is what you\'ll see. Your project name will differ from mine, as Spectacle assigns a random name to each project.

[![Blank project page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)

To continue, we must tell the project which boards we wish to use. Start by clicking the \"Add a Board\" button at the bottom of the page.

[![add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)

This will bring up a list of the available boards. We\'re going to add our Button Board first of all, so click anywhere in the \"Button\" box to add it.

Now, repeat this process one more time to add a Light Board.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)

You should now have a list that looks like this. **Order is important,** so make sure your boards are in the same order as shown above. Names are *not* important, however, and your boards will have different names than mine do, as Spectacle assigns names randomly.

[![All boards in list](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/all_boards.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/all_boards.png)

Each board has a clapboard icon associated with it. To add or edit actions, click this icon. We\'re going to start by adding an action to the Button Board.

[![Edit buttons highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/highlight_edit_buttons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/highlight_edit_buttons.png)

The window that pops up will look like the image below. Click the button highlighted in the image below to add an action to the Button Board.

[![Add an action button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/add_an_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/add_an_action.png)

This list will come up. It represents all the different actions which can be performed by a Button Board.

Click on the list entry which says \"Latch On/Latch Off\".

[![Action list for button board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/button_options_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/button_options_1.png)

You\'ll then see this screen, which presents the various options for the Latch On/Latch Off action. Every action will have different settings.

[![latch on latch off options](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/latch_on_off_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/latch_on_off_1.png)

Here are the settings we need to use for this project. We want button 8 (the button on the Button Board) to activate channel 0 when pressed. Later on, we\'ll tell our Light Board to watch channel 0 and do something when it\'s active.

[![Latch mode button options](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/latching_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/latching_settings.png)

Now click on the \"Go Back\" button to return to the main page. Your action changes will be saved automatically.

[![Go back button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/go_back_button.png)

We\'re back at the main page, now, and you can see that the action we added appears under the Button Board in the boards list. Now click on the clapboard icon for the Light Board to add an action for the button to trigger.

[![Main page with both boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/both_boards_with_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/both_boards_with_action.png)

When you click the \"Add an Action\" button, you\'ll be presented with this list of actions that the Light Board can perform. We\'re going to choose the \"Scanning Effect\" action.

[![Light board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/light_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/light_board_actions.png)

This screen will pop up, albeit without any of the entries in the fields. Go ahead and set up the fields as I\'ve shown them below, then click the \"Go Back\" button.

[![Scan action settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/scan_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/scan_settings.png)

Congratulations! You\'ve finished the configuration step of the process. Now it\'s time to move on to loading the project onto your Director Board.

[![Project, completed](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/done_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/4/done_project.png)

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.