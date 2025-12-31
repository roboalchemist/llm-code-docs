# Source: https://learn.sparkfun.com/tutorials/spectacle-inertia-board-hookup-guide

## Spectacle Inertia Board

The Spectacle Inertia Board makes it easy to sense motion or orientation with a Spectacle project.

[![Spectacle Inertia Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/6/3/13992-01.jpg)](https://www.sparkfun.com/products/13992)

### [Spectacle Inertia Board](https://www.sparkfun.com/products/13992) 

[ DEV-13992 ]

The Spectacle Inertia Board makes it easy to sense motion or orientation with a Spectacle project. The Spectacle Inertia Boar...

**Retired**

### tl;dr (essentials)

1.  The Inertia Board can sense motion, lack of motion, orientation, or acceleration.
2.  It\'s capable of either momentary triggers or continuous triggers.

### Meet the Spectacle Inertia Board

The Spectacle Inertia Board is designed to allow a Spectacle project to detect its orientation, whether it is moving or stationary, or whether it is under acceleration.

It has two 1/8\" (3.5mm) jacks for Spectacle control signals. **Pay attention to the directionality of the jacks!** The one labeled \"In\" should be plugged into a board that is closer to the Director Board than the Inertia Board is, or into the Director Board itself.

[![IO Jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/4/inertia_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_jacks.png)

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## The Configuration Utility 

[![Inertia board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_actions.png)

There are three different actions which can be assigned to the inertia board, allowing you to sense several different options of motion and orientation. We\'ll explain them one at a time below.

#### Sense All Motion

[![Sense all motion options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_all_motion.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_all_motion.png)

This action sends out a trigger when the board is either moving or stationary. When the board is moved, the trigger signal will be sent nearly immediately. When the board goes from moving to stationary, however, there is a delay of a couple of seconds before the trigger signal comes out.

- **\"if / while\"** - Determines whether the signal should happen only once, when the board starts or stops moving, or whether it should be constant any time the board is moving or not moving.
- **\"moving / stationary\"** - Should the signal be activated when the board starts moving, or when it stops moving?
- **\"activate channel number \...\"** - Which channel do we want the signal to be on?

#### Sense Orientation

[![Sense orientation settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_orientation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_orientation.png)

Another sensing application for the Inertia Board is orientation. Each face and edge of the Inertia Board has a name associated with it (A-D, Top, or Bottom). The board can output a signal when any of these sides is up, either only when it initially becomes face up or continually as long as it is face up.

- **\"if / while\"** - Determines whether the signal should happen only once, when the board first attains the orientation, or constantly, so long as the orientation is held.
- **\" a b c d top bottom\"** - This is the side/face of the board which causes a signal to be sent when it\'s on top.
- **\"activate channel number \...\"** - Which channel do we want the signal to be on?

#### Measure Acceleration

[![Measure acceleration options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/measure_acceleration.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/measure_acceleration.png)

The final sensing option is to measure acceleration. The output can be between 0 and 1000, depending on the acceleration of the board. The axis along which the acceleration is being measured is defined by the check boxes, and acceleration in a positive direction will be greater than 500 while a negative acceleration will be less than 500.

We recommend experimentation as the best way to figure out how this mode works.

## Example Project

Let\'s make a simple project using the Spectacle Audio Board and the Spectacle Inertia Board! We\'ll set it up so that a sound is played whenever the Inertia Board is moved.

#### Connect the boards

To follow this tutorial, you\'ll need this hardware:

[![Hamburger Mini Speaker](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/3/1/14023-01.jpg)](https://www.sparkfun.com/hamburger-mini-speaker.html)

### [Hamburger Mini Speaker](https://www.sparkfun.com/hamburger-mini-speaker.html) 

[ COM-14023 ]

This will be a treat for your ears! The Hamburger Mini Speaker is a 3W economical speaker option for any project needing stan...

[ [\$7.95] ]

[![Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/2/8/13831-01a.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5.1V DC 2.5A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5-1v-dc-2-5a-usb-micro-b.html) 

[ TOL-13831 ]

This is a high-quality switching \'wall wart\' AC to DC 5.1V 2,500mA USB Micro-B wall power supply manufactured specifically fo...

[ [\$13.95] ]

[![Spectacle Director Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/7/9/13912-01.jpg)](https://www.sparkfun.com/products/13912)

### [Spectacle Director Board](https://www.sparkfun.com/products/13912) 

[ DEV-13912 ]

The Spectacle Director Board controls all the actions in a Spectacle project. Though the Director Board doesn\'t do too much o...

**Retired**

[![Spectacle Inertia Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/6/3/13992-01.jpg)](https://www.sparkfun.com/products/13992)

### [Spectacle Inertia Board](https://www.sparkfun.com/products/13992) 

[ DEV-13992 ]

The Spectacle Inertia Board makes it easy to sense motion or orientation with a Spectacle project. The Spectacle Inertia Boar...

**Retired**

[![Spectacle Audio Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/5/2/14034-01.jpg)](https://www.sparkfun.com/spectacle-audio-board.html)

### [Spectacle Audio Board](https://www.sparkfun.com/spectacle-audio-board.html) 

[ DEV-14034 ]

The Spectacle Audio Board allows you to add sound from a microSD card to your Spectacle projects. Each board accepts a microS...

**Retired**

[![microSD USB Reader](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

[![Audio Cable TRRS - 3ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/8/14164-01.jpg)](https://www.sparkfun.com/products/14164)

### [Audio Cable TRRS - 3ft](https://www.sparkfun.com/products/14164) 

[ CAB-14164 ]

This is a 3-foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are th...

**Retired**

[![microSD Card with Adapter - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/3/0/13833-02.jpg)](https://www.sparkfun.com/products/13833)

### [microSD Card with Adapter - 16GB (Class 10)](https://www.sparkfun.com/products/13833) 

[ COM-13833 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

**Note that you will need three of the TRRS cables!**

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

Plug the other end of that cable into the \"In\" jack on your Audio Board.

[![Plugging into the in jack on the audio board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/4/Spectacle-22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/Spectacle-22.jpg)

Plug the speaker into the Audio Out port on the Audio Board.

[![Plugging in the speaker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/4/Spectacle-23.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/Spectacle-23.jpg)

Take another one of the TRRS cables and plug one end into the \"Out\" port on the Audio Board\...

[![Plugging into the out jack on the audio board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/4/Spectacle-25.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/Spectacle-25.jpg)

\...and plug the other end of that cable into the \"In\" port on the Inertia Board.

[![Plug the other end into the inertia board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/4/Spectacle-26.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/Spectacle-26.jpg)

Finally, plug the Micro B end of the power adapter into the Director Board and the other end of the adapter into the wall. You should see one solid light and one blinking light on the Inertia Board and the Audio Board. On the Director Board, you\'ll see one solid light and one light which blinks one time, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

When you first visit the Spectacle configuration website, you\'ll be presented with a screen that looks like this. Your project name will differ, however, as Spectacle assigns a new name to each project. To continue, we\'re going to have to add our Audio Board to the project.

[![Blank project](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/blank_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/blank_project.png)

Click on the \"Add a Board\" button, as highlighted above, to bring up a list of available boards.

[![Add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/add_a_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/add_a_board_1.png)

In the list, click anywhere in the \"Audio\" box to add an Audio Board to our project.

[![Board list](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/board_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/board_list.png)

You\'ll be returned to the main project page, but this time, an Audio Board will appear in the list on the page. Repeat these two steps to add an Inertia Board to the project.

[![Main page with audio board](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/added_audio_board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/added_audio_board.png)

Here you can see both boards in the list in place. Next we\'ll need to add actions to the boards.

[![List with both boards in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_too.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_too.png)

You can see highlighted above the clapboard icons which, when clicked, will take you to the \"Actions\" page, where you can assign an action to your board. Let\'s start by assigning an action to the Audio Board.

[![Add actions buttons](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/add_actions_buttons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/add_actions_buttons.png)

An empty page will come up. There are no currently assigned actions, so we\'ll need to assign some. Click the \"Add an Action\" button at the bottom of the page.

[![Empty actions page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/empty_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/empty_actions.png)

As you can see, the Audio Board only has one action. Click on \"Play Sound\" to add this action to your Audio Board.

[![There\'s only one action for the sound board](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/only_one_option.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/only_one_option.png)

Here are the various settings for the \"Play Sound\" action. Copy the settings as I\'ve entered them into you project.

[![Settings for play sound](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/play_sound_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/play_sound_action.png)

Click on the \"Go Back\" button at the bottom of the page to return to the main page, then click on the clapboard icon for the Inertia Board to add an action. When the empty list pops up, click the \"Add an Action\" button at the bottom to bring up the list of actions for the Inertia Board.

[![The Go Back button](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/go_back_button.png)

Here\'s the list of actions for the Inertia Board. We want to detect when motion occurs, so click the first option, \"Sense All Motion\".

[![Inertia board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/inertia_board_actions.png)

Here\'s the options page for the sense motion action. Note the choices I\'ve made and duplicate them for your project, then click \"Go Back\".

[![Sense motion options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_motion_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/sense_motion_options.png)

Congratulations! Your project is completed. Now let\'s upload it to the Director Board.

[![Project done](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/project_done.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/4/project_done.png)

#### Installing a project on the Director Board

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.