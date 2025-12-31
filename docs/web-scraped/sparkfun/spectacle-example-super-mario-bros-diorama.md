# Source: https://learn.sparkfun.com/tutorials/spectacle-example-super-mario-bros-diorama

## Introduction

Spectacle is designed to make complicated electronics projects simple, so you can focus on what you do best: making cool things!

In this tutorial, we\'ll show you how to make an animated diorama (with sound effects!) using Spectacle.

[![Gif of mario box in action](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/Mario_box.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/Mario_box.gif)

#### Techniques of note

We created the tiles for the diorama using [this project from Thingiverse](http://www.thingiverse.com/thing:1183157). We 3D printed the tiles, then painted them accordingly.

[![Picture of the project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/8/Spectacle-40.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/Spectacle-40.jpg)

The layout was designed in Inkscape, then etched into the wood with a laser cutter. The laser cutter was also used to cut out the slots that the moving pieces ride up and down in. Of course, this step is optional. The tiles could easily be placed by hand, and the cuts could be made with a hobby knife or similar woodworking tool.

#### Prior Reading

This tutorial assumes a basic familiarity with the Spectacle system. If you haven\'t yet, read the following tutorials for all the basic information you\'ll need to know to get this project going:

[](https://learn.sparkfun.com/tutorials/spectacle-users-guide)

### Spectacle User\'s Guide 

The Spectacle system is designed to help those without electronics or programming experience integrate electronics into projects.

[](https://learn.sparkfun.com/tutorials/spectacle-audio-board-hookup-guide)

### Spectacle Audio Board Hookup Guide 

All the information you need to use the Spectacle Audio Board in one place.

[](https://learn.sparkfun.com/tutorials/spectacle-button-board-hookup-guide)

### Spectacle Button Board Hookup Guide 

All the information you need to use the Spectacle Button Board in one place.

[](https://learn.sparkfun.com/tutorials/spectacle-motion-board-hookup-guide)

### Spectacle Motion Board Hookup Guide 

All the information you need to use the Spectacle Motion Kit in one place.

## Animating the Diorama

To animate the diorama, we 3D printed a longer arm for the servo motor. The length of the arm must be approximately equal to the linear distance the moving component is expected to cover.

We then attached a piece of 0.020\" (0.5mm) music wire to the end of the arm. The wire must be affixed in such a way that it can rotate freely as the arm moves. We passed it through a hole in the arm and bent it to a shape that will be retained by the hole.

[![Close up of the longer arm with wire in place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/8/Spectacle-42.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/Spectacle-42.jpg)

The other end of the wire was affixed to the slide mechanism to which the tiles were glued. In that case, a small loop is printed on the back of the slide mechanism and the wire is again bent into a shape that will be retained by that loop. The wire is rigid enough to push the tiles into a new position, but flexible enough to bend when the stop is hit.

[![Shuttle back](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/8/Spectacle-44.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/Spectacle-44.jpg)

### Adding Sound

We elected to keep the sound simple for this project, using the delaying mechanism of the Audio Board to trigger the sounds at the appropriate time rather than trying to trigger the sound by having Mario hit another switch.

Finding sound effects is left as an exercise for the reader, to prevent possible copyright or trademark issues. A quick web search will turn up sound effects for most projects, however.

## Spectacle Project

The Spectacle project for this setup is very simple. It consists of a Button Board, a Motion Board, and an Audio Board. We\'ll just give you the pages of the project here, rather than walk you step-by-step through making a Spectacle project. Below, find the main page of the app, with all the boards in place. Remember that the order the boards are connected in must match the order they appear in the app list in.

[![Main Window showing boards](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/main_window.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/main_window.png)

Here are the settings for the Button Board. Note that, although we\'re triggering four separate actions, we only need to have a signal on one channel.

[![Button Board settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/button_board_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/button_board_settings.png)

Here we see the Motion Board settings. You\'ll note that there\'s a slight delay between receipt of the triggering signal and activation of the first motion. That accounts for the brief delay between triggering the Sound Board and the sound actually playing. The sliders are opposite because the position of the motors is mirrored on the inside of the project.

[![Motion Board settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/3/8/motion_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/motion_settings.png)

Finally, here are the settings for the two sound events on the Sound Board. By layering them like this, we create the illusion of triggering the second sound when Mario hits the block without having to put a switch on that block.

[![Audio Board settings](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/audio_settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/8/audio_settings.png)

Note that these are timing values for my system and you\'ll probably have to change them if you do your own. I figured these out by playing around with it a bit.