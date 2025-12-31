# Source: https://learn.sparkfun.com/tutorials/spectacle-sound-kit-hookup-guide

## Introduction

The [Spectacle Sound Kit](https://www.sparkfun.com/products/14487) contains everything you need to make a button-triggered sound-playback project.

[![Spectacle Sound Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/5/4/5/14487_Sound_Kit-01.jpg)](https://www.sparkfun.com/products/14487)

### [Spectacle Sound Kit](https://www.sparkfun.com/products/14487) 

[ KIT-14487 ]

The Spectacle Sound Kit makes it easy to incorporate sounds, tunes and other audio ideas into your next project and to activa...

**Retired**

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## Spectacle Audio Board

The Spectacle Audio Board allows you to add sound to your Spectacle projects. It accepts a microSD card with sounds in .ogg format (more on this later), and has a 1/8\" (3.5mm) audio jack to connect to external amplifiers.

[![Spectacle Audio Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/5/2/14034-01.jpg)](https://www.sparkfun.com/spectacle-audio-board.html)

### [Spectacle Audio Board](https://www.sparkfun.com/spectacle-audio-board.html) 

[ DEV-14034 ]

The Spectacle Audio Board allows you to add sound from a microSD card to your Spectacle projects. Each board accepts a microS...

**Retired**

### tl;dr

1.  Audio files for Spectacle should be formatted as .ogg files.
2.  Audio files should have names 00.ogg, 01.ogg, 02.ogg, etc.
3.  The audio jack on the Audio Board produces output suitable for amplification only. *It is not suited to headphones or unpowered speakers.*

### Meet the Spectacle Audio Board

Designed to be a low-cost and easy to use method of adding sound to projects, the Spectacle Audio Board integrates with the rest of the Spectacle ecosystem to provide sound effects on demand.

It has three 1/8\" (3.5mm) jacks: two for Spectacle control signals and one for the audio output. **Be certain you are plugging cables into the right jacks!** Plugging an audio device into one of the Spectacle jacks could cause damage to the audio device. Note that the Spectacle data jacks are directional: the one marked \"In\" should be plugged into the \"upstream\" board (i.e., closer to the Director Board than this one) and the one marked \"Out\" connects to the next downstream board. **The \"Out\" jack is not for audio signals.**

[![Spectacle IO jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/audio_io_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/audio_io_jacks.png)

The audio output is designed for amplified devices only. This means that any attempt to use the Spectacle Audio Board with headphones or unamplified speakers will fail to produce audible output. SparkFun sells a [small, amplified, rechargeable speaker](https://www.sparkfun.com/products/14023) which is specifically intended for use with the Spectacle Audio Board.

[![Audio jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/audio_audio_jack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/audio_audio_jack.png)

The Spectacle Audio Board uses a Micro SD card to store the audio files to be played. The files should be stored as .ogg Vorbis encoded files. This free audio file format can be played and created on any type of computer. Later in the tutorial we\'ll show you how to convert from MP3, WAV, or other file formats to the .ogg format.

[![SD Card Slot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/audio_sd.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/audio_sd.png)

The files must be named by number, which is how they will be referred to from within the configuration application. Filename examples are 00.ogg, 01.ogg, 02.ogg, and so forth.

## Spectacle Button Board

The Spectacle Button Board allows you to add input from buttons or switches to your Spectacle projects. It has a total of 9 signal inputs, eight of which can come from external buttons and one button directly on the board.

[![Spectacle Button Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/7/1/14044-01.jpg)](https://www.sparkfun.com/products/14044)

### [Spectacle Button Board](https://www.sparkfun.com/products/14044) 

[ DEV-14044 ]

The Spectacle Button Board allows you to add input from buttons, switches or other contact-type sensing devices to your Spect...

**Retired**

### tl;dr

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

## The Configuration Utility

### Spectacle Sound Board

[![Sound interface](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)

The Spectacle Audio Board only supports one action: Play Sound. As you can see above, there are a number of settings associated with this action.

- **\"Listen to channel number\...\"** - This is the channel number which triggers the audio to start playing. As long as this channel\'s value is above the threshold level (see below), the sound will repeat playing at a rate determined by the two time intervals specified lower down.
- **\"wait \... seconds and play\...\"** - This is the first delay in the system. By delaying when a sound plays, you can sequence events however you see fit.
- **\"\...and play file number\...\"** - This is where you tell the board which file to play. Remember, when copying the audio files to the Micro SD card, they should be named as 00.ogg, 01.ogg, 02.ogg, etc. The number in this field corresponds to the number in the name of the audio file. If there is no audio file with the corresponding number, no sound will play.
- **\"do not allow another sound to interrupt until \... seconds\"** - The number in this field should correspond to the length of the audio file. If this value is less than the length of the sound file, another trigger sent to the audio board will interrupt the sound before it finishes. If it is longer than the sound, there will be a period of silence after playback before another playback can be initiated.
- **\"activation threshold\"** - As it says in the app, most of the time you don\'t need to adjust this. By tweaking this, you can set the angle at which the Spectacle Accelerometer Board triggers a sound, or the frequency with which a Random Trigger Virtual Board causes a sound to play.

### Spectacle Button Board

[![Button board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)

For the Button board, there are five options: three which produce a momentary pulse type output and two that produce a continuous switch type output.

##### Action on press

[![Action on press options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)

Trigger an action when a button is first pressed, regardless of how long it is subsequently held down.

- **\"When button number \... is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \...\"** - A single, momentary pulse will be sent out on this channel. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip, but not for continuous sound playback or for turning on a light strip effect, for instance.

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
- **\"activate channel number \...\"** - A continuous will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on (at least, while the button is held) a lighting effect.

##### Latch On/Latch Off

[![Latch On/Off options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)

This action is like a latching power switch. One press turns the signal on, another later press turns the signal off.

- **\"While button number \... is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"activate channel number \... until button is pressed again\"** - A continuous will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on a lighting effect.

## Converting Sounds to OGG Vorbis Format

The files used by the Spectacle Audio Board must be in OGG Vorbis format. This free, lossy codec has a higher compression ratio than MP3, and, more importantly, can be used without paying a licensing fee to any third part organization.

#### Download and Install Audacity

We\'ll be using the [free, open source program \"Audacity\"](http://www.audacityteam.org/) to convert from whatever your file\'s current format is to OGG Vorbis.

[![Audacity website](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_website.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_website.png)

Audacity is available across all three major operating systems, so you shouldn\'t have any trouble getting it installed.

When you start Audacity, you\'ll see this screen, or one very like it. While at first blush it seems extremely complex, **none of this crap is important to us,** so don\'t panic.

[![Audacity main screen](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_5.png)

#### Load a file

Like most programs, \"loading a file\" just means selecting \"Open\" from the File menu and choosing which file you wish to convert. Audacity is capable of editing most types of audio files: WAV, AIFF, FLAC, MP3, and others.

[![Audacity file menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_open.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_open.png)

By default, Audacity shows all files, not just compatible audio files, when you bring up the open dialog. There\'s a dropdown menu that allows you to change that so it shows only compatible audio files along the bottom edge of the window.

[![Audacity open file dialog](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_open_window.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_open_window.png)

Once you select which file you wish to edit, a rather alarmist message may pop up warning you about editing files without making a copy of them. Just click \"OK\".

[![Audacity edit file warning](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_warning.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_warning.png)

You\'ll see, then, something like this show up. This is what your audio file looks like, to the computer. **Again, don\'t panic!** Unless you want to edit the sound in some way (which we don\'t), none of the settings or pieces of information that have popped up here matter to us.

[![Audacity with open file](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_file_open.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_file_open.png)

#### Convert to OGG

Now that you have the file loaded, you need to convert it to OGG Vorbis format. To do so, open the \"File\" menu and select the \"Export Audio\...\" menu item about halfway down. A familiar looking save window should pop up.

[![Export command in file menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_export_audio_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_export_audio_1.png)

Right below the \"File name:\" field you\'ll see a drop-down menus labeled \"Save as type:\". Select \"Ogg Vorbis Files\" in that drop down.

A slider will appear at the bottom of the window. The default value of \'5\' is probably good enough for most purposes. Click \"Save\" and another window will pop up.

[![Export audio frame](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_export_audio_frame.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_export_audio_frame.png)

This one allows you to set metadata about the file. You can ignore everything and just click \"OK\" to skip past this.

Congratulations! You\'ve successfully converted a file to OGG Vorbis format. You may now copy that file to the Micro SD card (don\'t forget to rename it to a number!) for use with the Spectacle Audio Board.

[![Set metadata window](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/metadata.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/metadata.png)

#### Extra credit- trimming the fat and making the sound louder

As you can see in my file above, there\'s a great deal of room between the extents of the sound and the extents of the window. In the time (horizontal) axis, this manifests as flat lines before and after the content of the sound file. In the \"loudness\" (vertical) axis, this manifests as space between the top and bottom of the waveform file and the top and bottom of the playback position window.

[![File open in Audacity](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_file_open.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_file_open.png)

Let\'s eliminate some of that dead time before and after the sound plays. To do so, simply click inside the playback position window and drag, as though you are trying to select a section of text. The part you\'ve selected will be highlighted, as above. Now, just hit the \"Delete\" key on your keyboard, and that section will be removed. Repeat the process at the other end of the sound.

[![Extra dead time highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/audacity_highlighted_extra.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/audacity_highlighted_extra.png)

Now, let\'s see what we can do about volume. Under the \"Edit\" menu, look for the \"Select\" submenu, and choose \"All\" to select the entire sound. You can also just use the drag-and-highlight method from above.

[![Finding the \"Select All\" menu option](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/select_all.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/select_all.png)

Now that you\'ve got the entire sound selected, click on the \"Effect\" menu and select the \"Amplify\...\" option.

[![Effects menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/effects_menu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/effects_menu.png)

A new window will pop up with a slider, a couple of text boxes, and one checkbox. The slider will be pre-positioned to amplify the sound as much as possible without \"clipping\" it. \"Clipping\" occurs when you try to amplify a sound more than the system you\'re playing it through can stand, and it results in a sort of grating buzzing noise during playback.

[![Amplify dialog box](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/amplify_dialog.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/amplify_dialog.png)

You have a choice, now: you can either accept the system\'s suggested level, or you can click on the \"Allow Clipping\" check box and increase the amplification more with the slider. I\'ve chosen to accept the clipping limitation for the image above; comparing it to the image of the file higher up, you can see how I\'ve trimmed the dead time at the ends and increased the amplitude vertically.

Why would you want to allow your sound to clip? Well, first of all, the preset amplification only takes into account the peak value of your sound, so if one small section of the audio is allowed to clip, it may allow the vast majority of the sound to be substantially louder. Secondly, if you\'re playback device is of relatively poor quality, or the sound file itself is, allowing clipping may increase volume significantly without making the sound quality too much worse than it already is. Thirdly, volume intensity may be far more important than sound quality, and allowing clipping lets you push the volume as high as you can.

[![Edited sound](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/edited_sound.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/edited_sound.png)

Now that you\'ve successfully edited the sound, export it to OGG Vorbis as we covered above.

## Example Project

Let\'s use the contents of the Spectacle Sound Kit to put together a working project!

#### Connect the boards

All of the required hardware for this tutorial is included in the kit.

Start by connecting up the boards. You\'ll need the included TRRS audio cables, the power supply, and the small, rechargeable speaker. Make sure the speaker is charged before the first time you try to use it!

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

Then take the other end of the first TRRS cable (the one connected to the \"Direct\" jack on the Director Board) and plug it into the \"In\" jack on the Button board.

[![Connecting the button board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/Spectacle-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/Spectacle-27.jpg)

Grab another of the TRRS cables and plug it into the \"Out\" jack on the button board.

[![Connecting to the output of the button board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/Spectacle-28.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/Spectacle-28.jpg)

Plug the other end of that cable into the \"In\" jack on your Audio board.

[![Connecting to the input of the Audio board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/Spectacle-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/Spectacle-32.jpg)

Now plug the speaker into the \"Audio Out\" jack on the Audio board.

[![Connecting the speaker](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/Spectacle-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/Spectacle-33.jpg)

You can now insert the micro SD card into the slot on the back of the board.

[![Inserting the sd card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/1/8/Spectacle-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/Spectacle-34.jpg)

Finally, plug the Micro B end of the power adapter into the Director board, and the other end into the wall. You should see one solid light and one blinking light on both the Audio board and the Button board. On the Director board, you\'ll see one solid light and one light which blinks eight times, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

We\'re going to assume that you followed the instructions on the previous page about converting sounds to OGG Vorbis format, and that there is a sound on the Micro SD card inserted into the Sound board named \"00.ogg\". If this is *not* the case, take a few minutes to go back to that page and prepare a sound.

Here\'s a new project in the spectacle app screen. Feel free to rename yours (it will have a different default name than the example does), as the name of the project has no effect on the rest of the process.

[![Bare new project window](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/bare_project_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/bare_project_1.png)

Click the button highlighted below to add a board to our system\'s configuration.

[![Add board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/add_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/add_board_1.png)

Click anywhere in the \"Button\" box in the list that pops up to add a Button Board to your project. Now, repeat the process and click in the \"Audio\" box to add an Audio Board to your project.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/board_list_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/board_list_1.png)

You\'ll be back to the main page, then, but there will be a couple of new lines present: one for the Button Board and one for the Audio Board.

[![Main page, showing boards added](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_boards_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_boards_1.png)

To edit the actions assigned to these boards, click on the clapboard icon in the row of the board you wish to edit. We\'ll start by editing the Button Board\'s actions.

[![Board edit highlight buttons](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/highlight_edit_buttons_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/highlight_edit_buttons_1.png)

Any time you bring up a new board to add actions, you\'ll see the same screen as below. To add an action, click the \"Add An Action\" button in the center bottom of the frame.

[![Blank add an action page](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/blank_action_page_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/blank_action_page_1.png)

This will present you with a list of actions that the current board is capable of implementing. In the case of the button board, there are five different options. Click on the first one, \"Action on Press\".

[![Options for button board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_options_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_options_1.png)

You\'ll now see the window as above. Put a \'0\' in the two fields indicated, causing a trigger pulse to be sent out on channel 0 whenever button 0 is pressed. Then click the \"Go Back\" button at the bottom of the page to save the action and return to the main page.

[![Setting up the button board action](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_action_setup_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_action_setup_1.png)

Back on the main page, you can see that the action you added is visible on the Button Board\'s row in the window. Let\'s edit the actions for the Sound board next.

[![Main page with button action in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_button_action_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_button_action_1.png)

There\'s only one option for actions for the Audio Board, and that\'s \"Play Sound\". Once you\'ve clicked through to the configuration window for \"Play Sound\", you\'ll see a page like this. Fill in the blanks as shown above, then click the \"Go Back\" button again.

[![Sound board action setup](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/sound_board_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/sound_board_actions_1.png)

You\'ll be back on the main page, now, and you\'ll see the actions you\'ve added under each of the lines in the project. It\'s time to upload the configuration to your hardware!

[![Main page with all boards and actions in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_done_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/main_page_done_1.png)

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.