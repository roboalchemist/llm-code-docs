# Source: https://learn.sparkfun.com/tutorials/hackers-in-residence-the-sound-visualizer-pt-2

## Introduction

This guide is a follow up to the [first write up](https://learn.sparkfun.com/tutorials/hackers-in-residence-the-sound-visualizer) I did for [my participation in the SparkFun HIR program](https://www.sparkfun.com/news/1598). This guide shows how to setup a music visualizer for PCs/laptops. It uses an RGB LED panel to display the music visualization. It plays MP3s and is Java powered. This project differs from the first one in that it samples the data output to the computer's sound card versus sampling ambient noise with a [microphone](https://www.sparkfun.com/products/9964) or a [Sparkfun sound detector](https://www.sparkfun.com/products/12642).

[![sound visualizer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/2/Roberto-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/2/Roberto-01.jpg)

### Required Materials

This project assumes you have access to a [PIXEL board](http://ledpixelart.com/pixelv2board/). Please note that I have no afiliation with the [PIXEL project](http://ledpixelart.com/) other than I write software for it and Al gives me PIXEL hardware as incentive to write more software.

The PIXEL usually comes with an RGB LED panel, but the board alone is also available. If only the PIXEL board was acquired, then this [panel from Sparkfun](https://www.sparkfun.com/products/12583) can be used with this project.

Other than a PIXEL unit, you need a PC or laptop that supports Java 8. To play the demo songs, an Internet connection is required. If no Internet connection is available, then select some MP3s on the filesystem for use with the music visualizer. More details on selecting MP3s from the local filesystem are below.

### Suggested Reading

Before diving into this project, you may want to check out these other tutorials first.

- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
- [Light-emitting Diodes (LEDS)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)
- [How LEDs Are Made](https://learn.sparkfun.com/tutorials/how-leds-are-made)
- [RGB Panel Hookup Guide](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)

## Hardware Assembly

### Pixel

Use this [quick start guide](http://ledpixelart.com/downloads/PIXEL-Guts-Quick-Start-Guide.pdf) to get familiar with the PIXEL hardware.

This project can use either Bluetooth or serial (USB) for communication between the PC and the PIXEL. Before continuing, make sure you can pair/connect with the PIXEL from your computer and run the [sample 'PC application'](http://ledpixelart.com/support/get-the-apps/).

Here is what the PIXEL could look like once assembled:

[![pixel attached to led panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/2/Roberto-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/2/Roberto-02.jpg)

## Software Prerequisites and Installation

### JRE

This project requires Java 8 Standard Edition. Fortunately, Java runs on many platforms. Download and install the [JRE (Java Runtime Environment)](http://www.oracle.com/technetwork/java/javase/downloads/index.html) for your PC/laptop's operating system.

### Java Application

This project reuses an existing app to sample data from the computer's sound card. The app uses the modern media API for Java, JavaFX, to play MP3s. The original developer is Jasper Pots.\

[Download the Application](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/2/onebeartoe-fx-experieince-player-0.0.1-SNAPSHOT.jar)

## Software Usage

### Running the App

Once Java 8 SE is installed, run the application by double clicking the JAR file you downloaded above. This will bring up the user interface for the application.

[![UI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/2/UI.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/2/UI.jpg)

If Bluetooth is used, then a system tray popup is shown, prompting for the passcode to pair with the PIXEL. Enter the passcode for your PIXEL board (0000 for V2, 4545 for V1), before the popup dismisses itself. Otherwise, an application restart is needed to try pairing again.

Once the PIXEL connection is initialized, a yellow message scrolls across the RGB LED panel. Then a sample music file is downloaded and the music visualization begins on the RGB LED panel.

Here is a quick demo:

### Playing Local MP3 Files

Use the 'Load' button to play MP3s on the local filesystem.

[![UI2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/4/2/UI2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/2/UI2.jpg)