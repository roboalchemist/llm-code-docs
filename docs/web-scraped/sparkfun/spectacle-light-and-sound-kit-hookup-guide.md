# Source: https://learn.sparkfun.com/tutorials/spectacle-light-and-sound-kit-hookup-guide

## Introduction

The [Spectacle Light and Sound Kit](https://www.sparkfun.com/products/14486) allows you to add button-activated sound and light effects to your projects with ease.

[![Spectacle Light and Sound Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/5/4/4/14486_Light_and_Sound_Kit-01.jpg)](https://www.sparkfun.com/products/14486)

### [Spectacle Light and Sound Kit](https://www.sparkfun.com/products/14486) 

[ KIT-14486 ]

The Spectacle Light and Sound Kit makes it easy to incorporate button-activated sound and light effects into your projects wi...

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

The Spectacle Audio Board uses a microSD card to store the audio files to be played. The files should be stored as .ogg Vorbis encoded files. This free audio file format can be played and created on any type of computer. Later in the tutorial we\'ll show you how to convert from MP3, WAV, or other file formats to the .ogg format.

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

## Spectacle Light Board

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects. It has connections for up to three strands of addressable LEDs and a connector for external power.

[![Spectacle Light Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/9/1/14052-01.jpg)](https://www.sparkfun.com/spectacle-light-board.html)

### [Spectacle Light Board](https://www.sparkfun.com/spectacle-light-board.html) 

[ DEV-14052 ]

The Spectacle Light Board allows you to add some fairly complex lighting effects to your Spectacle projects in a streamlined ...

**Retired**

### tl;dr

1.  If more than approximately 10 pixels will be on at once, we recommend powering the Light Board through the onboard micro-B USB port.
2.  For smaller numbers of pixels, it is possible to power them directly over the Spectacle control cable.
3.  Most of the LED effects want a continuous type signal, such as the Button board \"Latch On/Latch Off\" function.
4.  Only WS2812 (NeoPixel) type addressable LED strips will work with the Spectacle Light Board.

### Meet the Spectacle Light Board

Designed to make it easy to add relatively complex lighting effects to your Spectacle projects, the Spectacle Light Board integrates with the rest of the Spectacle ecosystem to allow you to control lighting effects relatively effortlessly.

It has two 1/8\" (3.5mm) jacks for Spectacle control signals. **Pay attention to the directionality of the jacks!** The one labeled \"In\" should be plugged into a board that is closer to the Director Board than the Light Board is, or into the Director Board itself.

[![Signal jacks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_jacks.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_jacks.png)

The Light Board supports up to three strands of [addressable LEDs](https://www.sparkfun.com/products/12025). Each strand can have up to 60 individual pixels. **Not all types of addressable LEDs are compatible with the Spectacle Light Board.** If you have questions about whether or not a particular type of LED strip is compatible with the Light Board, contact SparkFun technical support.

[![LED Strand Connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_connectors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_connectors.png)

The Light Board has a Micro B USB connector to allow it to be directly powered by an external power supply. The relatively slender cables the Spectacle data travels over are not adequate for the large amount of current drawn by more than a few pixels.

[![USB Power Jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/light_usb_jack.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/light_usb_jack.png)

## The Configuration Utility

### Spectacle Audio Board

[![Sound interface](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/spectacle_app_audio_play_1.png)

The Spectacle Audio Board only supports one action: Play Sound. As you can see above, there are a number of settings associated with this action.

- **\"listen to channel number \_\_\"** - This is the channel number which triggers the audio to start playing. As long as this channel\'s value is above the threshold level (see below), the sound will repeat playing at a rate determined by the two time intervals specified lower down.
- **\"wait \_\_ seconds and play\"** - This is the first delay in the system. You can sequence events however you see fit by delaying when a sound plays.
- **\"file number \_\_\"** - This is where you tell the board which file to play. Remember, when copying the audio files to the microSD card, they should be named as 00.ogg, 01.ogg, 02.ogg, etc. The number in this field corresponds to the number in the name of the audio file. If there is no audio file with the corresponding number, no sound will play.
- **\"do not allow another sound to interrupt until \_\_ seconds\"** - The number in this field should correspond to the length of the audio file. If this value is less than the length of the sound file, another trigger sent to the audio board will interrupt the sound before it finishes. If it is longer than the sound, there will be a period of silence after playback before another playback can be initiated.
- **\"activation threshold\"** - As it says in the app, most of the time you don\'t need to adjust this. Adjusting the slider can set the angle at which the Spectacle Accelerometer Board triggers a sound, or the frequency with which a Random Trigger Virtual Board causes a sound to play.

### Spectacle Button Board

[![Button board action options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/button_board_actions_1.png)

For the Button board, there are five options: three which produce a momentary pulse type output and two that produce a continuous switch type output.

##### Action on press

[![Action on press options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_1.png)

Trigger an action when a button is first pressed, regardless of how long it is subsequently held down.

- **\"When button number \_\_ is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \_\_\"** - A single, momentary pulse will be sent out on this channel. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip. This feature is not intended for continuous sound playback or for turning on a light strip effect.

##### Action on release

[![action on release options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_release_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_release_1.png)

Trigger an action when a button is released, regardless of how long it has been held down prior to being released.

- **\"When button number \_\_ is released\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \_\_\"** - A single, momentary pulse will be sent out on this channel. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip, but not for continuous sound playback or for turning on a light strip effect, for instance.

##### Action on press or release

[![Action on press or release options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_release_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_on_press_release_2.png)

Trigger an action when a button is pressed, then trigger the same action again when the button is released.

- **\"When button number \_\_ is either pressed or released\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"trigger channel number \_\_\"** - A single, momentary pulse will be sent out on this channel both at the time the button is pressed and at the time it is released. It is suitable for starting a sound, initiating a motion, or setting the color of a light strip, but not for continuous sound playback or for turning on a light strip effect, for instance.

##### Action while holding

[![Action while holding options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_while_holding_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/action_while_holding_1.png)

Trigger an event as soon as a button is pressed, then continue to trigger that event as long as the button is held down.

- **\"While button number \_\_ is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"activate channel number \_\_\"** - A continuous will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on (at least, while the button is held) a lighting effect.

##### Latch On/Latch Off

[![Latch On/Off options](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/1/8/latch_on_off_1.png)

This action is like a latching power switch. One press turns the signal on, another later press turns the signal off.

- **\"While button number \_\_ is pressed\"** - This is the number of the button we wish to assign to this action. The button numbers are printed on the board, and run from 0 through 8.
- **\"activate channel number \_\_ until button is pressed again\"** - A continuous will be sent out on this channel. It is suitable for triggering and repeating a sound, or for turning on and keeping on a lighting effect.

### Spectacle Light Board

[![Action list for light board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)

The Light Board supports 9 different actions. Most of them want a continuous-type signal input, although a couple of them can be used with momentary input signals. We\'ll cover the difference under each action. Each action will have a field for the number of pixels the lightstrip that action is being applied to has, and we won\'t mention it again.

##### Rainbow Effect

[![Rainbow effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/rainbow_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/rainbow_effect.png)

The rainbow effect displays a rainbow of colors across the strip, changing the color of each pixel indvidually to make it appear as though the rainbow is scrolling along the lightstrip.

- **\"While channel number \_\_ is active\"** - The rainbow effect persists only while the channel is active, so a continuous input signal is needed.
- **\"rainbow scroll lightstrip number \_\_\"** - Select which lightstrip you wish the rainbow effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **scroll speed slider** - controls how fast the pattern moves as it scrolls past.

##### Theater chase

[![Theater chase settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/theater_chase.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/theater_chase.png)

Theater chase mode behaves like a marquee light border. The lights will march along making it appear as though the lightstrip is moving in steps.

- **\"While channel number \_\_ is active\"** - The theater chase effect persists only while the channel is active, so a continuous input signal is needed.
- **\"theater chase lightstrip number \_\_\"** - Select which lightstrip you wish the theater chase effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **chase speed slider** - controls how fast the pattern moves as it scrolls past.
- **color picker input** - allows you to select the color of the lights.

##### Scanning effect

[![Scanning effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/scanning_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/scanning_effect.png)

Scanning mode sees a small group of lights bouncing back and forth along the length of the lightstrip, reminiscent of Cylons from Battlestar Galactica.

- **\"While channel number \_\_ is active\"** - The scanning effect persists only while the channel is active, so a continuous input signal is needed.
- **\"scan lightstrip number \_\_\"** - Select which lightstrip you wish the scanning effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **scan speed slider** - controls how fast the pattern moves as it scrolls past.
- **color picker input** - allows you to select the color of the lights.

##### Twinkle effect

[![Twinkle effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/twinkle_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/twinkle_effect.png)

Causes individual lights on the selected strip to perform a twinkling action.

- **\"While channel number \_\_ is active\"** - The twinkle effect persists only while the channel is active, so a continuous input signal is needed.
- **\"twinkle lightstrip number \_\_\"** - Select which lightstrip you wish the twinkle effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights.
- **speed slider** - controls how fast the twinkles are moves as it scrolls past.
- **magic slider** - controls how magical the twinkles are. Play with it!

##### Lightning effect

[![Lightning effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/lightning_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/lightning_effect.png)

Causes the entire strip to strobe in a manner that looks a lot like a lightning flash.

- **\"While channel number \_\_ is active\"** - The lightning effect persists only while the channel is active, so a continuous input signal is needed.
- **\"lightning on lightstrip number \_\_\"** - Select which lightstrip you wish the lightning effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights.
- **speed slider** - controls how often the lightning strike occur moves as it scrolls past.
- **fury slider** - controls how furious the lightning is. Play with it!

##### Flame effect

[![Flame effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/flame_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/flame_effect.png)

Causes the entire strip to crackle like a fire.

- **\"While channel number \_\_ is active\"** - The flame effect persists only while the channel is active, so a continuous input signal is needed.
- **\"make fire on lightstrip number \_\_\"** - Select which lightstrip you wish the flame effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **color picker input** - allows you to select the color of the lights. Experiment with different colors!

##### Fade effect

[![Fade effect settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fade_effect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fade_effect.png)

The lightstrip will change from one color to another over time, then back to the first.

- **\"While channel number \_\_ is active\"** - The fade effect persists only while the channel is active, so a continuous input signal is needed.
- **\"fade lightstrip number \_\_ back and forth\"** - Select which lightstrip you wish the fade effect to operate on. To have the same effect on multiple lightstrips, you must create multiple actions.
- **\"from color\" color picker** - This is the initial color that the lightstrip will power up with.
- **\"to color\" color picker** - The other color, which the strip fades to and from periodically.
- **\"fade speed\" slider** - Controls how fast the fading action occurs.

##### Fill

[![Fill settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill.png)

Fills some number of lights on the light strip with a single color. Blanks the other lights to off.

- **\"listen to channel number \_\_\"** - A momentary signal on this channel is all that is needed to trigger a fill operation, and the fill will persist until another effect starts.
- **\"wait for \_\_ seconds\"** - This delay allows for sequencing effects. Most often you\'ll probably set it to 0.
- **\"clear lightstrip number \_\_\"** - Select the lightstrip to operate upon.
- **\"and fill \_\_ pixels\"** - The number of pixels, from closest to the Light board out, to turn on.

##### Light pixel

[![Pixel settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/pixel.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/pixel.png)

Turns on one light and blanks the rest of the lights to off.

- **\"listen to channel number \_\_\"** - A momentary signal on this channel is all that is needed to trigger a light pixel operation, and the lit pixel will persist until another effect starts.
- **\"wait for \_\_ seconds\"** - This delay allows for sequencing effects. Most often you\'ll probably set it to 0.
- **\"clear lightstrip number \_\_\"** - Select the lightstrip to operate upon.
- **\"and light pixel number \_\_ \"** - The number of the pixel, from closest to the Light board out, to turn on.

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

Let\'s use the contents of the Spectacle Light and Sound Kit to put together a working project! We\'re going to set up a laser gun type setting, where a light comes on and a sound plays when a button is pressed, then the light goes off when the button is released.

#### Connect the boards

Start by connecting up the boards. All of the required hardware is included with the kit.

First, plug one end of one of the TRRS cables into the \"Direct\" jack on the Director Board.

[![The direct jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_direct_jack.jpg)

Next, take the other TRRS cable and plug it into the \"Program\" jack on the Director Board.

[![The program jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/director_program_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/director_program_jack.jpg)

Take the other end of this cable and plug it into the audio jack of the phone, tablet, or computer that you\'ll be using to program the system.

[![Into the phone jack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/9/phone_audio_jack.jpg)

Then take the other end of the first TRRS cable (the one plugged into the \"Direct\" jack on the Director Board) and plug it into the \"In\" jack on the Button Board.

[![In jack on button board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-27.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-27.jpg)

Grab another of the TRRS cables and plug it into the \"Out\" jack on the Button Board.

[![Out jack on the director board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-28.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-28.jpg)

Plug the other end of that cable into the \"In\" jack on your Audio Board.

[![In jack on audio board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-32.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-32.jpg)

Now plug the speaker into the \"Audio Out\" jack on the Audio Board.

[![Plug the speaker into the audio board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-33.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-33.jpg)

Insert the micro SD card into the Audio Board.

[![Inserting the micro SD card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-34.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-34.jpg)

Plug another of the TRRS cables into the \"Out\" jack on your Audio Board.

[![Out jack on the Audio Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-35.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-35.jpg)

Plug the other end of that cable into the \"In\" jack on your Light Board.

[![Plugging into the in jack on the light board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-36.jpg)

Connect the light strip adapter cable to the Light Board.

[![Connecting the light strip adapter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-37.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-37.jpg)

Connect the other end of the adapter cable to the light strip.

[![Connecting the light strip](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/1/Spectacle-38.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/Spectacle-38.jpg)

Finally, plug the Micro B end of the USB cable into the Director Board and the other end into the power adapter. Plug the power adapter into the wall. You should see one solid light and one blinking light on the Light Board, the Audio Board, and the Button Board. On the Director Board, you\'ll see one solid light and one light which blinks one time, then pauses, then repeats. This shows that power is present and the boards are up and running.

#### Setting up the board configuration

We\'re going to assume that you followed the instructions on the previous page about converting sounds to OGG Vorbis format, and that there is a sound on the Micro SD card inserted into the Sound board named \"00.ogg\". If this is *not* the case, take a few minutes to go back to that page and prepare a sound.

When you first open the Spectacle app webpage, this is what you\'ll see. Your project name will differ from mine, as Spectacle assigns a random name to each project.

[![Blank project page](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/bare_project_1.png)

To continue, we must tell the project which boards we wish to use. Start by clicking the \"Add a board\" button at the bottom of the page.

[![add a board button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_board_1.png)

This will bring up a list of the available boards. We\'re going to add our Button Board first of all, so click anywhere in the \"Button\" box to add it.

Now, repeat this process two more times, adding an Audio Board and a Light Board.

[![List of available boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_1.png)

You should now have a list that looks like this, showing all three of the boards we\'re going to use in this project. **Pay attention to the order of the boards in the list!** They must match the order of the boards in hardware! If the order of your boards differs from that in the image above, you can use the up and down carets (in the board name bar) to change the order of the boards.

[![All boards in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/all_boards.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/all_boards.png)

Now you\'ll need to add actions to each board, to tell the Spectacle system what sort of behavior you want. Click on the clapboard icon (highlighted above) for the Button Board to pull up the \"Edit actions\" frame.

[![Edit action buttons](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/edit_buttons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/edit_buttons.png)

This will pull up a window that looks like the above. I\'ve highlighted the \"Add an action\" button. Click it to pull up a list of actions for the Button Board.

[![Add an action button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_an_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/add_an_action.png)

This list will pop up after you click the \"Add an action\" button. We\'re going to add two actions: \"Action on Press\" and \"Action on Release\". Click the \"Action on Press\" list item, then click \"Add an action\" again to pull the list back up, then click the \"Action on Release\" list item to add that action to the list.

[![Button board action list](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_options_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_options_1.png)

Here you can see that we\'ve added the two actions we want for our project. Note that, when added, the inputs default to being blank. You need to put a value in every field for the design to be valid.

[![Button board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_actions.png)

Here are the settings you\'ll want to put into place for this project. You can see that the \"Action on Press\" is tied to channel 0, and we\'re using button 8 (the onboard button) as the input signal. \"Action on Release\" is tied to channel 1, and also to button 8.

[![Button actions, filled in](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_actions_filled_in.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/button_actions_filled_in.png)

Once you\'ve filled in the fields for both actions, click the \"Go Back\" button to return to your list of boards. This will automatically save the changes you\'ve made.

[![Go back button](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/go_back_button.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/go_back_button.png)

You can see here that the actions we added for the Button Board appear in the main board list, as a reminder of what each board has been configured to do.

[![Board list with actions on Button board](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_button_actions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/board_list_button_actions.png)

Now, add a \"Play Sound\" action to the Audio Board. It\'s the only action the Audio Board supports. Fill in the blanks on the play sound page as shown above.

[![Play sound options](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/play_sound_action.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/play_sound_action.png)

Back in the main frame, you\'ll see that the play sound action has been added to the Audio Board\'s section of the list.

[![Main frame with play sound action in place](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/main_window_play_sound.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/main_window_play_sound.png)

Finally, we\'ll configure the Light Board. The picture above shows the full list of actions that the Light Board supports. We\'re going to use the \"Fill Color\" option, twice, for our project.

[![Light board actions](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/light_actions_1.png)

Below are the settings for the first \"Fill Color\" effect to be added. This turns the pixels on when the button is depressed.

[![Settings for the first fill effect](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill_1.png)

Here are the settings for the second fill effect. This turns the pixels off when the button is released.

You can now click the \"Go Back\" button to return to the main page.

[![Settings for second fill effect](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/fill_2.png)

Congratulations! You\'ve completed configuration of your first Spectacle project! Now let\'s cover loading the configuration onto your Director Board.

[![Completed project](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/final_project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/1/final_project.png)

#### Uploading

Now that you\'ve created your Spectacle program it\'s time to upload it to the Director Board. If you followed the instructions above, your uploading device is connected to the board and ready to go, so all you need to do is touch the \"Install Script\" button at the bottom of the page. That will bring up the page seen below.

[![Upload page](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/2/upload_page.png)

Make sure the volume on your device is turned all the way up, and that no other audio source (music, video, etc) is playing in the background. Then press and hold the \"RST\" button on the Director Board, press and hold the \"PROG\" button, then release the \"RST\" button.

This will put the Director Board into program mode. You\'ll see the light on the board blink three times, pause, then repeat. This is your visual indicator that the board is in program mode. Once you\'ve established that the board is in program mode, you can begin programming by touching the \"Install\" button on the Spectacle app screen. The button will gray out during the programming process, which should only last for a few seconds. Once programming is done, you\'ll see the light on the Director Board blink 10 times, pause, then repeat. That\'s your cue that the program was uploaded successfully.

Press the \"RST\" button again to reset the system and begin the program!

If you have any troubles, visit the [troubleshooting page](https://learn.sparkfun.com/tutorials/spectacle-users-guide#troubleshooting) for help resolving your issues.