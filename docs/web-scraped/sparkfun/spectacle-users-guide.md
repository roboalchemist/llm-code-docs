# Source: https://learn.sparkfun.com/tutorials/spectacle-users-guide

## Introduction

Spectacle is a product ecosystem centered around a simple idea: creative people shouldn\'t have to learn new skills to use electronics in their projects. You\'ve spent years developing the skills you use, and SparkFun wants to recognize that and help you expand your creations to include electronics without requiring you to spend years learning about electronics and programming.

[![Spectacle family portrait](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/Spectacle-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/Spectacle-01.jpg)

Spectacle launched with six modules: the Director Board, an Audio Output Board, a Motor Control Board, a Lighting Control Board, an Inertia Sensing Board, and a Button Input Board. Every Spectacle project consists of at least two boards: one Director Board and at least one of the output-type modules.

#### Director Board

[![Spectacle Director Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/7/9/13912-01.jpg)](https://www.sparkfun.com/products/13912)

### [Spectacle Director Board](https://www.sparkfun.com/products/13912) 

[ DEV-13912 ]

The Spectacle Director Board controls all the actions in a Spectacle project. Though the Director Board doesn\'t do too much o...

**Retired**

The Director Board controls all the actions in a Spectacle project. Input-type modules report data on their state back to it, and output-type modules receive their marching orders from it.

#### Audio Output Board

[![Spectacle Audio Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/5/2/14034-01.jpg)](https://www.sparkfun.com/spectacle-audio-board.html)

### [Spectacle Audio Board](https://www.sparkfun.com/spectacle-audio-board.html) 

[ DEV-14034 ]

The Spectacle Audio Board allows you to add sound from a microSD card to your Spectacle projects. Each board accepts a microS...

**Retired**

The Audio Output Board adds the ability to play sounds from a Micro SD card to your Spectacle system. It provides a line-level output ready to be amplified.

#### Motor Control Board

[![Spectacle Motion Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/6/5/13993-01.jpg)](https://www.sparkfun.com/products/13993)

### [Spectacle Motion Board](https://www.sparkfun.com/products/13993) 

[ DEV-13993 ]

The Spectacle Motion Board makes it easy to add movement to your Spectacle projects. Each Motion Board can control up to five...

**Retired**

The Motor Control Board is made to drive conventional hobby servo motors, either normal type or continuous rotation type. It can be powered via the Director Board connection or via a local input port for higher power servo motors.

#### Light Board

[![Spectacle Light Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/9/1/14052-01.jpg)](https://www.sparkfun.com/spectacle-light-board.html)

### [Spectacle Light Board](https://www.sparkfun.com/spectacle-light-board.html) 

[ DEV-14052 ]

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects in a streamlined ...

**Retired**

The Light Board controls strands of addressable LEDs, allowing it to realize quite a few interesting effects that otherwise wouldn\'t be possible.

#### Inertia Sensing Board

[![Spectacle Inertia Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/6/3/13992-01.jpg)](https://www.sparkfun.com/products/13992)

### [Spectacle Inertia Board](https://www.sparkfun.com/products/13992) 

[ DEV-13992 ]

The Spectacle Inertia Board makes it easy to sense motion or orientation with a Spectacle project. The Spectacle Inertia Boar...

**Retired**

The Inertia Sensing Board allows you to trigger events on motion, stillness, or orientation.

#### Button Input Board

[![Spectacle Button Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/7/1/14044-01.jpg)](https://www.sparkfun.com/products/14044)

### [Spectacle Button Board](https://www.sparkfun.com/products/14044) 

[ DEV-14044 ]

The Spectacle Button Board allows you to add input from buttons, switches or other contact-type sensing devices to your Spect...

**Retired**

The Button Input Board takes its input from all manner of button, switches, or other contact type sensing devices. It has 8 external inputs and one onboard button, allowing for a large number of inputs to a single module.

## Spectacle Director Board 

The Spectacle Director Board is at the core of all Spectacle systems. It stores the program, connects to and sends power to the other boards in the system, and passes messages between the other boards.

### Director Board Hardware Tour

[![Director Buttons](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/director_buttons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/director_buttons.png)

There are two buttons on the Director Board: one labeled RST and one labeled PROG. These buttons allow you to enter programming mode, so new behaviors can be loaded into your Spectacle system.

To enter programming mode, press and hold the RST button, press and hold the PROG button, and then release the RST button.

[![Micro USB Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/director_microusb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/director_microusb.png)

Power for your Spectacle system is delivered via a Micro USB jack on the Director Board. Power is then delivered to additional boards in the system via the cables connecting the other boards together, although some boards (such as the Motion Board and the Light Board) may require locally delivered power.

[![Program Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/director_program_jack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/director_program_jack.png)

The \"Program\" jack is where you\'ll connect the device you use for programming. A cable connecting this jack to the audio output of your programming device is needed to upload a new set of behaviors to your Spectacle system.

[![Direct Jack](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/director_direct_jack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/director_direct_jack.png)

Other Spectacle boards will be connected to the \"Direct\" jack. Power is delivered via this jack to the other boards, and power to those boards is disconnected while the RST button is held down.

## Spectacle Example

Spectacle actions are mediated by \"Channels\", which represent information sent from input modules to output modules by way of the Director Board. More than one board may listen to a single channel, and more than one board may write to a single channel by use of \"virtual\" boards to combine signals.

#### An Example

In our simple example, we\'ve created a system with only two boards: the Director Board and the Audio Output Board. This simple example is going to play a sound at random intervals, with a minimum of 10 seconds between playback.

Here we see the opening screen of the Spectacle App. The default name (in this case) is \"my talented project\" but you can, of course, change this to be anything that you\'d like. We\'ll just leave it as is. Next, we need to add our Audio Output Board to the project. Click the \"ADD A BOARD\" button at the bottom of the page.

[![Blank project](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/blank_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/blank_project.png)

You\'ll now see a list of the various types of boards which are currently available. We\'ve discussed five of these six entries, and we\'ll cover what a virtual board is in a second. For now, just click on \"Audio\" to add our Audio Output Board.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/add_board_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/add_board_list.png)

We\'re now back at the beginning screen, with the addition of another line below the project info line for a \"painstaking sound board\". You can rename this as you please by simply clicking in the text field holding the board\'s name.

[![Main page with a new board](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/new_board_appears.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/new_board_appears.png)

Now click the clapboard icon to bring up a list of actions assigned to the board.

[![This is the edit button](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/edit_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/edit_button.png)

Unsurprisingly, it\'s empty. We have to add something! At the bottom of the page, find the \"ADD AN ACTION\" button. Click it and a list of actions will descend from the top of the page.

[![Audio board empty action page](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/empty_action_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/empty_action_page.png)

For the Audio Output Board, only two options exist: \"Cancel\" and \"Play Sound\". Click on \"Play Sound\" to add that action to our actions list.

[![Audio board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/audio_board_options.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/audio_board_options.png)

You\'ll find this screen has appeared. There are four blanks, for four user inputs, and a slider at the bottom which we\'re going to ignore. Here are the uses of the other fields.\
\* **\"Listen to channel number\...\"** - This is the channel number which triggers the audio to start playing. As long as this channel\'s value is above the threshold level (set by that slider that we\'re not going to mess with), the sound will repeat playing at a rate determined by the two time intervals specified lower down.\
\* **\"wait \... seconds and play\...\"** - This is the first delay in the system. By delaying when a sound plays, you can sequence events however you see fit.\
\* **\"\...and play file number\...\"** - This is where you tell the board which file to play. Remember, when copying the audio files to the Micro SD card, they should be named as 00.ogg, 01.ogg, 02.ogg, etc. The number in this field corresponds to the number in the name of the audio file. If there is no audio file with the corresponding number, no sound will play.\
\* **\"do not allow another sound to interrupt until \... seconds\"** - The number in this field should correspond to the length of the audio file. If this value is less than the length of the sound file, another trigger sent to the audio board will interrupt the sound before it finishes. If it is longer than the sound, there will be a period of silence after playback before another playback can be initiated.

[![Play sound setup page](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/play_sound_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/play_sound_settings.png)

Here are the settings to put into the fields. **Note that we are listening on channel 0, as we\'ll need that information later.** We want to play our sound immediately, play sound file 00.ogg, and not interrupt that sound for at least one second.

[![Setting for play sound action](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/play_sound_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/play_sound_settings.png)

There! We\'ve added the instruction to play back a sound. Now we need to tell the system when to play the sound. Click the \"GO BACK\" button at the bottom of the screen. **Don\'t worry, the action you added has been saved automatically.**

[![This is the go back button](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/go_back_button.png)

We\'re back at the opening screen again, and you can see that \"play sound on channel 0\" has been added to the Sound Board\'s entry. If we had created more actions, they would show up there, as well. Click the \"ADD A BOARD\" button to continue.

[![Audio board in list witih action](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/with_audio_board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/with_audio_board.png)

We\'re back at the list of boards. This time, we\'re going to add a virtual board. This special subset of \"boards\" adds functionality that otherwise isn\'t added by any particular hardware board.

[![List of boards again](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/add_board_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/add_board_list.png)

Now a virtual board entry appears in our project list. The Virtual Board entry is special, in that it can only exist once in the boards list, and it will always \"sink\" to the bottom of the list, even if you try to rearrange boards beneath it or if you create boards after the virtual board. Again, click on the clapboard icon to enter the add/edit actions view.

[![Virtual board in list](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/vb_in_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/vb_in_list.png)

When you click on \"ADD AN ACTION\", you\'ll see a greater variety of options than you did with the Sound Board. The first four allow for input signals from external boards to be combined or changed in some way, while the bottom four require no external hardware to use. Choose \"Random Input\" from the list.

[![Virtual board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/vb_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/vb_actions.png)

There are only two blanks here: one for channel number, and one for timing. Basically, this action flips a coin every few seconds (how often is determined by the value in the blank) and outputs the result to the channel you set in the blank field. Put \'0\' in the channel number field and \'10\' in the \"every \_\_\_ seconds\" field.

Now, click the \"GO BACK\" button at the bottom of the screen to return to the main menu.

[![Random output settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/configure_random.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/configure_random.png)

Congratulations! You\'ve just finished setting up the configuration for our random sound player!

[![Start menu with both boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/start_with_boards.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/start_with_boards.png)

#### Programming the system

Programming the system is done via your headphone output jack. Plug one of the included 3.5mm cables into the headphone jack on your computer, smartphone, or tablet, and plug the other end into the \"Program\" jack on the Director Board.

Supply power to the Director Board via the micro USB jack on the end of the board, then hold down the RST button. Hold down the PROG button, and release the RST button. After a moment, you should see the LED on the board blinking. It should blink three times, pause, blink three times, pause, repeatedly. Turn your system\'s volume up all the way, then touch or click the \"Install Script\" button at the bottom of the screen. That will pull up the page below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/upload_page.png)

Click or touch the \"Install\" button at the bottom. The button will gray out during the installation process. When it has returned to its normal color, the installation is done. If the installation was successful, you should see the LED on the Director Board blink 10 times, then pause, then 10 times, then pause, etc. Press the RST button on the Director. Again, you\'ll see 10 blinks, then a pause on the Director LED. That means the program is loaded and everything is working.

## Spectacle Concepts

#### Momentary versus continuous events

Some events in Spectacle will generate a \"one-and-done\" pulse, and some will generate a continuous signal. What happens with these signals depends upon what sort of action the signal is connected to.

##### Example: Inertia board and Sound board

[![Example configuration 00](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/example_00.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/example_00.png)

Imagine we have system with an inertia board and a sound board, configured as above.

By the settings you can imagine what will happen: a sound will play when the inertia board is moved. But what happens if the inertia board *keeps* moving? It will continue to send its signal on channel 0, and the sound board will continue to receive it, and two seconds after the sound starts playing (*regardless of the actual length of the sound*), the sound will play again. This will continue until the inertia board is allowed to stop moving\--a *continuous* output signal.

To play the sound only once, upon the first motion of the inertia board, what should we change? We would change the check box on the \"sense motion\" action from \"while\" to \"if\".

##### Example: Button board and Light board

[![Example 01 configuration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/9/example_01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/example_01.png)

Now let\'s look at a momentary example, and how **not** to use it.

Consider the system described above. One may assume that, when pressed, the flame effect would begin on strip 1 of the light board. And that\'s true, it will. However, since the flame effect is a continuous effect (that we want to run indefinitely) and the button press is momentary (it only issues a signal when the button is initially pressed), the effect will be brief\--probably so brief as to not even be visible to the user.

So what should we change to get what we want? We have a couple of options, looking at the actions available to the button board:

[![Button board available actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/example_01_02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/9/example_01_02.png)

Looking over our available choices, \"Action while Holding\" and \"Latch On/Latch Off\" sound like they\'ll produce a continuous output suitable for triggering our continuous flame effect. Using one of them (depending on whether you want to have to hold the button or just turn it on and off) will get us the behavior we desire.

## Troubleshooting

Sometimes things just don\'t work out the way we envisioned them working out. Here are some tips for troubleshooting a non-functioning (or malfunctioning) Spectacle project.

### Board order is wrong

A limitation of the Spectacle application and system is that the boards must be attached to the Director Board in the same order in which they appear in the application list. This means that a system with a Button Board as the top item in the list and a Sound Board second is different to and incompatible with a Spectacle script which has the Button Board at the bottom. It also means that no Spectacle system can have unused boards in it. All of the boards in the system **must** be included in the script. It is permissible to have a board in a system with no actions assigned to it, however.

### Insufficient power

All Spectacle boards can be powered over the 1/8\" (3.5mm) TRRS jack cable which connects them. However, a couple of boards (currently, the Motion and Light boards) have a USB micro B connector on board to provide extra power to the motors or LED strips attached to the board.

How do you know if you need to attach another power supply? Well, the easiest way is to try and see. If your system behaves oddly, or doesn\'t work at all, you probably need more power than can be provided by the Director Board and should attach a supply at the output board.

If you are attaching more than 20 LEDs or more than one of the smallest size servos (or any of the larger servo motors), you should power the output board locally.

### Configuration failed to install properly

Sometimes, the upload just doesn\'t take properly. Usually this is due to the volume on the programming device having been set too low, or to another sound (a notification tone, for instance) playing on the programming device during the configuration installation process.

The solution here is simple: try installing again. If your volume **is** all the way up, it\'s possible that your device can\'t make a strong enough signal to work with Spectacle. This may be especially true of cellular phones in the EU, where maximum volume output is limited by statute.

### Single LED blink on Director Board at power up

This means the system failed to initialize properly. This can be because the board order is wrong, there\'s an extra board in the system, one of the cables isn\'t connected firmly, one of the cables has been damaged, or because the installation of the program went badly.

Typically, the best way to fix this is by checking connections and board order, reinstalling the code, and (if possible) swapping out the interboard connection cables with other, known good cables.