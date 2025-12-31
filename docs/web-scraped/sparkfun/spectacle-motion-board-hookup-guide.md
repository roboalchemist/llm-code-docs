# Source: https://learn.sparkfun.com/tutorials/spectacle-motion-board-hookup-guide

## Spectacle Motion Board

The [Spectacle Motion Board](https://www.sparkfun.com/products/13993) makes it easy to add movement to your Spectacle projects. It can control up to 5 servo motors, either of standard or continuous rotation type.

[![Spectacle Motion Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/6/5/13993-01.jpg)](https://www.sparkfun.com/products/13993)

### [Spectacle Motion Board](https://www.sparkfun.com/products/13993) 

[ DEV-13993 ]

The Spectacle Motion Board makes it easy to add movement to your Spectacle projects. Each Motion Board can control up to five...

**Retired**

### tl;dr (essentials)

1.  The USB Micro B port on the servo board is only for providing power to the attached motors.
2.  A single servo, or a couple of small servos, can be powered over the Spectacle control cable.
3.  Servo motors can be of the standard or continuous rotation type.

### Meet the Spectacle Motion Board

Designed to make it easy to add simple motions to your Spectacle projects, the Spectacle Motion Board integrates with the rest of the Spectacle ecosystem to allow you to control motion effects relatively effortlessly.

[![Motion board IO jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/motor_driver_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motor_driver_jacks.png)

It has two 1/8\" (3.5mm) jacks for Spectacle control signals. **Pay attention to the directionality of the jacks!** The one labeled \"In\" should be plugged into a board that is closer to the Director Board than the Motion Board is, or into the Director Board itself.

[![Servo headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/motion_servo_headers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motion_servo_headers.png)

The Motion Board supports up to 5 servo motors. The servo motors can be either standard motion or continuous rotation servos. There\'s a note on the board (\"O/W/Y\") for the color which should be on the top row of the header: orange, white, or yellow. Most servo motors will have one wire which is one of these colors, and that wire should line up with this note.

[![Micro USB jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/motion_micro_usb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motion_micro_usb.png)

The Motion Board has a Micro B USB connector to allow it to be directly powered by an external power supply. **The relatively slender audio cables the Spectacle data travels over are not adequate for the large amount of current drawn by larger servo motors or by multiple motors.**

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## The Configuration Utility

### Spectacle Motion Board

The Motion Board page in the Utility provides the following options.

[![Motion Board Actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/motion_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/motion_board_actions.png)

There are four actions associated with the Motion Board, all of which should be used with a single trigger pulse type input signal.

##### Sweep to Position

[![Toggle position action](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/toggle_position_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/toggle_position_action.png)

This action moves the motor between two positions, one motion on each trigger event.

- **\"listen to channel number \...\"** - This is the channel which triggers the action.
- **\"control servo number \...\"** - The servo to be controlled, numbered from 0-4.
- **\"wait \... seconds and move to\"** - Delay before motion for the first position.
  - **slider control** - Choose the position for the first motion. The servo starts at 90° on power up and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.
- **\"wait \... seconds and move to\"** - Delay before motion for the second position.
  - **slider control** - Choose the position for the second motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.

##### Sweep and Return

[![Sweep and return action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/action_sweep_and_return.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/action_sweep_and_return.png)

This action waits for a moment, moves the servo to a position, then waits for a moment at the new position, then moves back to the first position.

- **\"listen to channel number \...\"** - Which channel controls this action.
- **\"control servo number \...\"** - The servo to be controlled, numbered from 0-4.
- **\"wait \... seconds and move to\"** - Delay before motion for the first position.
  - **slider control** - Choose the position for the first motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.
- **\"wait \... seconds and move to\"** - Delay before motion for the second position.
  - **slider control** - Choose the position for the second motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.

##### Wagging Effect

[![Wagging action](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/wag_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/wag_action.png)

This action behaves much like sweep and return, but runs continuously until turned off by receipt of another signal pulse on the designated channel.

- **\"listen to channel number \...\"** - Which channel controls this action.
- **\"control servo number \...\"** - The servo to be controlled, numbered from 0-4.
- **\"wait \... seconds and move to\"** - Delay before motion for the first position.
  - **slider control** - Choose the position for the first motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.
- **\"wait \... seconds and move to\"** - Delay before motion for the second position.
  - **slider control** - Choose the position for the second motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.

##### Go to Position

[![Go to position options](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/go_to_position.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/1/go_to_position.png)

Move the servo motor from where ever it currently is to this new location after some delay.

- **\"listen to channel number \...\"** - Which channel controls this action.
- **\"control servo number \...\"** - The servo to be controlled, numbered from 0-4.
- **\"wait \... seconds and move to\"** - Delay before motion for the first position.
  - **slider control** - Choose the position for the first motion. The servo starts at 90° and can be rotated to 0° in one direction or to 180° in the other direction. This is equivalent to starting at 12 o\'clock and turning to either 9 o\'clock or 3 o\'clock.

## Example Project

Let\'s use the Spectacle Motion Board to make a project! We\'re going to program the project to move the servo from one position to another and back at regular intervals.

#### Connect the boards

Start by connecting up the boards. You\'ll need the following hardware:

[![Servo - Generic (Sub-Micro Size)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/2/09065-01a.jpg)](https://www.sparkfun.com/servo-generic-sub-micro-size.html)

### [Servo - Generic (Sub-Micro Size)](https://www.sparkfun.com/servo-generic-sub-micro-size.html) 

[ ROB-09065 ]

Here is a simple, low-cost, high quality servo for all your mechatronic needs. This servo is very similar in size and specifi...

[ [\$12.95] ]

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

[![Spectacle Motion Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/6/5/13993-01.jpg)](https://www.sparkfun.com/products/13993)

### [Spectacle Motion Board](https://www.sparkfun.com/products/13993) 

[ DEV-13993 ]

The Spectacle Motion Board makes it easy to add movement to your Spectacle projects. Each Motion Board can control up to five...

**Retired**

[![Audio Cable TRRS - 3ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/8/14164-01.jpg)](https://www.sparkfun.com/products/14164)

### [Audio Cable TRRS - 3ft](https://www.sparkfun.com/products/14164) 

[ CAB-14164 ]

This is a 3-foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are th...

**Retired**

**Note that you\'ll need two of the TRRS cables.**

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![Cable into direct port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/director_direct_jack.jpg)

Next, plug a cable into the \"Program\" jack on the Director Board.

[![Cable into program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/director_program_jack.jpg)

Plug the end of this cable into the audio output jack on your phone, tablet, or whatever device you\'re using to program the system.

[![Into the phone audio jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/phone_audio_jack.jpg)

Plug the other end of the first cable (the one plugged into the \"Direct\" jack) into the \"In\" jack on your Motion Board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/motion_board_input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motion_board_input.jpg)

Now, plug the servo connector onto the Motion Board

[![Servo connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/2/Spectacle-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/Spectacle-09.jpg)

Finally, plug the Micro B end of the USB cable into the Director Board, and the other end into the wall adapter. Plug the adapter into the wall. You should see one solid light and one blinking light on the Motion Board. On the Director Board, you\'ll see one solid light and one light which blinks one time, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

When you first open the Spectacle app webpage, this is what you\'ll see.

Your project name will differ from mine, as Spectacle assigns a random name to each project.

[![Blank project page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)

To continue, we must tell the project which boards we wish to use. Start by clicking the \"Add a Board\" button at the bottom of the page.

[![add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)

This brings up a list of available boards. We\'re going to start with a Motion Board and add a Virtual Board later. Click anywhere in the \"Motion\" box to add it to the project.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)

Here you can see that the Motion Board has been added to the list of boards in the main window.

[![Motion board added to list](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motion_board_added.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/motion_board_added.png)

To add actions to a board, click on the clapboard icon highlighted below.

[![Add action button](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/add_actions_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/add_actions_button.png)

This is the action list, empty. To add an action click the highlighted \"Add an Action\" button at the bottom of the page.

[![Empty action list](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/empty_action_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/empty_action_list.png)

You\'ll be presented with this list of available actions. Select the \"Sweep and Return\" action.

[![List of available actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/action_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/action_list.png)

There are a number of settings needed for the Sweep and Return action. In the image below, you\'ll find that I\'ve already entered the data needed to drive the servo actions we want for our system.

[![Sweep and return settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/sweep_return_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/sweep_return_settings.png)

Click the \"Go Back\" button at the bottom of the screen to return to the main board list. This will automatically save your work.

Now, click the \"Add a Board\" button again to bring up the boards list and this time, choose \"Virtual\".

Virtual Boards provide a number of functions outside of the normal operation of Spectacle boards. In this case, we want \"Periodic Input\", which generates a signal at a fixed timing rate.

Here\'s the board list with the Virtual Board added to it. Again, click the clapboard icon followed by \"Add an Action\" to bring up the actions menu.

[![Boards list with virtual board](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/add_virtual_board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/add_virtual_board.png)

[![Virtual board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/virtual_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/virtual_board_actions.png)

Here are the options for \"Periodic Input\". We tied the action on the Motion Board to channel 0, so we\'ll do the same here. We only need a short signal to trigger the Motion Board, so we\'ll set it to 0.1 seconds. Finally, we want the motor to activate every 10 seconds.

Again, click the \"Go Back\" button to return to the main page and save your actions.

[![Periodic input](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/periodic_input.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/periodic_input.png)

Congratulations! You\'ve finished the configuration step of the process. Now it\'s time to move on to loading the project onto your Director Board.

[![Finished project](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/final_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/final_project.png)

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.