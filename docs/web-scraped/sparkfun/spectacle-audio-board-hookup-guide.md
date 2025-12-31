# Source: https://learn.sparkfun.com/tutorials/spectacle-audio-board-hookup-guide

## Spectacle Audio Board

The Spectacle Audio Board allows you to add sound to your Spectacle projects. It accepts a microSD card with sounds in .ogg format (more on this later), and has a 1/8\" (3.5mm) audio jack to connect to external amplifiers.

[![Spectacle Audio Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/5/2/14034-01.jpg)](https://www.sparkfun.com/spectacle-audio-board.html)

### [Spectacle Audio Board](https://www.sparkfun.com/spectacle-audio-board.html) 

[ DEV-14034 ]

The Spectacle Audio Board allows you to add sound from a microSD card to your Spectacle projects. Each board accepts a microS...

**Retired**

### tl;dr (essentials)

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

### Suggested Reading

Before proceeding, you should read through the [Spectacle User\'s Guide](https://learn.sparkfun.com/tutorials/spectacle-users-guide). It will give you the basics you\'ll need to know about how Spectacle works to follow the rest of this tutorial.

## The Configuration Utility

### Spectacle Audio Board

[![Sound interface](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)

The Spectacle Audio Board only supports one action: Play Sound. As you can see above, there are a number of settings associated with this action.

- **\"Listen to channel number\...\"** - This is the channel number which triggers the audio to start playing. As long as this channel\'s value is above the threshold level (see below), the sound will repeat playing at a rate determined by the two time intervals specified lower down.
- **\"wait \... seconds and play\...\"** - This is the first delay in the system. By delaying when a sound plays, you can sequence events however you see fit.
- **\"\...and play file number\...\"** - This is where you tell the board which file to play. Remember, when copying the audio files to the Micro SD card, they should be named as 00.ogg, 01.ogg, 02.ogg, etc. The number in this field corresponds to the number in the name of the audio file. If there is no audio file with the corresponding number, no sound will play.
- **\"do not allow another sound to interrupt until \... seconds\"** - The number in this field should correspond to the length of the audio file. If this value is less than the length of the sound file, another trigger sent to the audio board will interrupt the sound before it finishes. If it is longer than the sound, there will be a period of silence after playback before another playback can be initiated.
- **\"activation threshold\"** - As it says in the app, most of the time you don\'t need to adjust this. By tweaking this, you can set the angle at which the Spectacle Accelerometer Board triggers a sound, or the frequency with which a Random Trigger Virtual Board causes a sound to play.

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

Let\'s use the Spectacle Audio Board to play a single sound at random intervals.

#### Connect the boards

You\'ll need the following hardware for this tutorial:

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

[![microSD USB Reader](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

[![Spectacle Audio Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/5/2/14034-01.jpg)](https://www.sparkfun.com/spectacle-audio-board.html)

### [Spectacle Audio Board](https://www.sparkfun.com/spectacle-audio-board.html) 

[ DEV-14034 ]

The Spectacle Audio Board allows you to add sound from a microSD card to your Spectacle projects. Each board accepts a microS...

**Retired**

[![Audio Cable TRRS - 3ft](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/0/7/8/14164-01.jpg)](https://www.sparkfun.com/products/14164)

### [Audio Cable TRRS - 3ft](https://www.sparkfun.com/products/14164) 

[ CAB-14164 ]

This is a 3-foot-long white audio cable that has been terminated with two TRRS connectors at each end. TRRS connectors are th...

**Retired**

[![Spectacle Director Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/7/9/13912-01.jpg)](https://www.sparkfun.com/products/13912)

### [Spectacle Director Board](https://www.sparkfun.com/products/13912) 

[ DEV-13912 ]

The Spectacle Director Board controls all the actions in a Spectacle project. Though the Director Board doesn\'t do too much o...

**Retired**

[![microSD Card with Adapter - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/3/0/13833-02.jpg)](https://www.sparkfun.com/products/13833)

### [microSD Card with Adapter - 16GB (Class 10)](https://www.sparkfun.com/products/13833) 

[ COM-13833 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

**You will need two of the TRRS cables. Make sure the speaker is charged before the first time you try to use it!**

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

You\'ll now need to connect the other end of the first TRRS cable (the one connected to the \"Direct\" jack) to the \"In\" jack on the Audio Board.

[![In jack on Audio Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/Spectacle-14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/Spectacle-14.jpg)

Connect the speaker to the \"Audio Output\" port on the Audio Board.

[![Audio jack to speaker connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/Spectacle-15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/Spectacle-15.jpg)

Finally, insert the microSD card with the files you prepared on it into the slot on the back side of the Audio Board.

[![MicroSD card insertion](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/3/Spectacle-16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/Spectacle-16.jpg)

Finally, plug the micro-B end of the power adapter into the Director Board, and the other end into the wall. You should see one solid light and one blinking light on the Audio board, and on the director board, you\'ll see one solid light and one light which blinks one time, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

We\'re going to assume that you followed the instructions on the [previous page](https://learn.sparkfun.com/tutorials/spectacle-audio-board-hookup-guide#converting-sounds-to-ogg-vorbis-format) about converting sounds to OGG Vorbis format, and that there is a sound named \"00.ogg\" on the Micro SD card which is inserted into the Audio Board. If this is *not* the case, take a few minutes to go back to that page and prepare a sound.

When you first open the Spectacle app webpage, this is what you\'ll see. Your project name will differ from mine, as Spectacle assigns a random name to each project.

[![Blank project page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/bare_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/bare_project.png)

The very first thing you\'ll do is add an Audio Board to the project. To do this, click on the \"Add a Board\" button, highlighted in the image below.

[![Add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/add_new_board_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/add_new_board_button.png)

Clicking on that button will bring up a list of available boards. Click anywhere in the \"Audio\" box to add an Audio Board to your system.

[![Board list](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/board_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/board_list.png)

We now need to tell the system what we want this board to do.

In the screen that pops up after you click in the \"Audio\" box, you\'ll find this little clapboard icon. Click that icon to add actions to the Audio Board.

[![Edit button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/sound_board_edit_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/sound_board_edit_button.png)

This will bring up the \"Actions\" list for this board, which is currently empty. To add an action, click the \"Add an Action\" button, highlighted below.

[![Add action button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/add_action_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/add_action_button.png)

Clicking on the \"Add an Action\" button will pull down this short menu, with only two options on it. Click \"Play Sound\" to add a sound playback action to the board.

[![Actions list for the audio board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/actions_list.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/actions_list.png)

This is the \"Play Sound\" action settings page. We\'ve covered the meaning of these fields [elsewhere in this tutorial](https://learn.sparkfun.com/tutorials/spectacle-audio-board-hookup-guide#the-configuration-utility), so I\'m just going to tell you what to enter in these fields.

[![Play sound action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/play_sound_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/play_sound_action.png)

Copy the settings from the image below into the fields.

[![Settings for the play sound action](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/play_sound_action_filled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/play_sound_action_filled.png)

Now click the \"Go Back\" button at the bottom of the page. The settings you just put in will be automatically saved, and you\'ll return to the main page of the project.

[![Go Back Button highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/go_back_button.png)

Now you\'re back to the main page, and you can see that the action set up in the Audio Board configuration we just did shows up in the list of boards as well, as a reminder of what that board is configured to do.

[![Main page with new actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/main_page_with_board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/main_page_with_board.png)

Now, click \"Add a Board\" to bring up the board list again, then click on \"Virtual\" to add a virtual board to the system. This \"board\" will generate the signal which randomly triggers the audio playback.

Virtual Boards provide a number of functions outside of the normal operation of Spectacle boards. In this case, we want \"Random Input\", which generates a signal at a fixed timing rate.

Again, click the clapboard icon on the virtual board list item to bring up the action add and edit page.

Here\'s the list of possible actions for the virtual board. Click on \"Random Input\" to get the randomizing function we want.

[![Virtual board actions list](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/virtual_board_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/virtual_board_actions.png)

Configure the random input settings as shown in the image below, then click the \"Go Back\" button to return to the main page.

[![Random function settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/random_input.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/random_input.png)

Congratulations! You\'ve finished configuring the system. Now it\'s time to install the settings onto the Director board.

[![Final project screen](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/all_board_all_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/3/all_board_all_actions.png)

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.