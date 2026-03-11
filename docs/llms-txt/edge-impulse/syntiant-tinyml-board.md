# Source: https://docs.edgeimpulse.com/hardware/boards/syntiant-tinyml-board.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Syntiant Tiny ML Board

The [Syntiant](https://www.syntiant.com) TinyML Board is a [tiny development board](https://www.syntiant.com/hardware) with a microphone and accelerometer, USB host microcontroller and an always-on Neural Decision Processor™, featuring ultra low-power consumption, a fully connected neural network architecture, and fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained embedded machine learning models directly from the Edge Impulse studio to create the next generation of low-power, high-performance audio interfaces.

The Edge Impulse firmware for this development board is open source and hosted on [GitHub](https://github.com/edgeimpulse/firmware-syntiant-tinyml).

<Frame caption="Syntiant TinyML Board">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2800463-tinyml_front.jpg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=d374d7310527634f0c1975a2b3923c1f" width="865" height="1000" data-path=".assets/images/2800463-tinyml_front.jpg" />
</Frame>

<Info>
  **IMU data acquisition - SD Card**

  An SD Card is required to use IMU data acquisition as the internal RAM of the MCU is too small. You don't need the SD Card for inferencing only or for audio projects.
</Info>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

* [Arduino CLI](https://arduino.github.io/arduino-cli/latest/installation/)
* [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation)

### Connecting to Edge Impulse

#### 1. Download the firmware

Select one of the 2 firmwares below for audio or IMU projects:

* [Audio firmware](https://cdn.edgeimpulse.com/firmware/syntiant-tinyml.zip)
* [IMU firmware](https://cdn.edgeimpulse.com/firmware/syntiant-tinyml-imu.zip)

Insert SD Card if you need IMU data acquisition and connect the USB cable to your computer. Double-click on the script for your OS. The script will flash the Arduino firmware and a default model on the NDP101 chip.

<Info>
  **Flashing issues**

  **0x000000: read 0x04 != expected 0x01**

  Some flashing issues can occur on the Serial Flash. In this case, open a Serial Terminal on the TinyML board and send the command: **:F**. This will erase the Serial Flash and should fix the flashing issue.
</Info>

#### 2. Connect the development board to your computer

Connect the Syntiant TinyML Board directly to your computer's USB port. Linux, Mac OS, and Windows 10 platforms are supported.

#### 3. Setup the Syntiant TinyML Board to collect data

**Audio - USB microphone (macOS/Linux only)**

Check that the Syntiant TinyML enumerates as "TinyML" or "Arduino MKRZero". For example, in Mac OS you'll find it under System Preferences/Sound:

<Frame caption="Syntiant TinyML Board Enumerated as Arduino MKRZero">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/285488d-screen_shot_2021-03-29_at_70613_pm.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=a22709af04177c54835f94aaa491c40d" width="1318" height="984" data-path=".assets/images/285488d-screen_shot_2021-03-29_at_70613_pm.png" />
</Frame>

<Info>
  **Audio acquisition - Windows OS**

  Using the Syntiant TinyML board as an external microphone for data collection doesn't currently work on Windows OS.
</Info>

**IMU**

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntiant-connected.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=0608ae471c6e6d5393c3d01f825e539f" width="1600" height="376" data-path=".assets/images/syntiant-connected.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model and evaluate it using the Syntiant TinyML Board with this tutorial:

* [Keyword spotting - Syntiant (RC Commands)](/tutorials/hardware/syntiant-ndp-keyword-spotting)
* [Motion recognition - Syntiant](/tutorials/hardware/syntiant-ndp-motion-recognition)

### FAQ

* Using the Arduino-CLI with a macOS M1 chip? You will need to install Rosetta2 to run the Arduino-CLI. See details on [Apple website](https://support.apple.com/en-us/HT211861).
* How to label my classes? The NDP101 chip expects one and only negative class and it should be the last in the list. For instance, if your original dataset looks like: `yes, no, unknown, noise` and you only want to detect the keyword 'yes' and 'no', merge the 'unknown' and 'noise' labels in a single class such as `z_openset` (we prefix it with 'z' in order to get this class last in the list).

### End User License Agreement

In order to work with Syntiant models on Edge Impulse you will be asked to accept this [End User License Agreement (EULA)](https://cdn.edgeimpulse.com/eula/syntiant-ei-eula-2025-03-24.pdf) inside your Edge Impulse Project.


Built with [Mintlify](https://mintlify.com).