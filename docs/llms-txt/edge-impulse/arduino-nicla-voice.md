# Source: https://docs.edgeimpulse.com/hardware/boards/arduino-nicla-voice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arduino Nicla Voice

The [Arduino Nicla Voice](https://docs.arduino.cc/hardware/nicla-voice/) is a development board with a high-performance microphone and IMU, a Cortex-M4 [Nordic](https://www.nordicsemi.com/) nRF52832 MCU and the [Syntiant® NDP120 Neural Decision Processor™ (NDP)](https://www.syntiant.com/). The NDP120 supports multiple Neural Network architectures and is ideal for always-on low-power speech recognition applications. You'll be able to sample raw data, build models, and deploy trained embedded machine learning models directly from the Edge Impulse studio to create the next generation of low-power, high-performance audio interfaces.

The Edge Impulse firmware for this development board is open source and hosted on [GitHub](https://github.com/edgeimpulse/firmware-arduino-nicla-voice).

<Frame caption="Arduino Nicla Voice">
  <img src="https://mintcdn.com/edgeimpulse/ZTVcrLfO8Bn7QR9I/.assets/images/nicla-voice.png?fit=max&auto=format&n=ZTVcrLfO8Bn7QR9I&q=85&s=f33ee3ccc1d56e0bd20d3efad0abe20c" width="910" height="512" data-path=".assets/images/nicla-voice.png" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

* [Arduino CLI](https://arduino.github.io/arduino-cli/latest/installation/)
* [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation)

### Connecting to Edge Impulse

#### 1. Download the firmware

Download the Nicla Voice firmware for audio or IMU below and connect the USB cable to your computer:

* [Audio firmware](https://cdn.edgeimpulse.com/firmware/arduino-nicla-voice-firmware.zip)
* [IMU firmware](https://cdn.edgeimpulse.com/firmware/arduino-nicla-voice-imu-firmware.zip)

The archive contains different scripts to flash the firmware on your OS, ie for macOS:

* *install\_lib\_mac.command*: script will install the Arduino Core for the Nicla board and the pyserial package required to update the NDP120 chip. **You only need to run this script once**.
* *flash\_mac.command*: to flash both the MCU and NDP120 chip. You should use this script on a brand new board

The additional scripts below can be used for specific actions:

* *flash\_mac\_mcu.command*: to flash only the Nordic MCU, ie if you recompiled the firmware and doesn't need to update the NDP120 model.
* *flash\_mac\_model.command*: to flash only the NDP120 model.
* *format\_mac\_ext\_flash.command*: to format the external flash that contains the NDP120 model

#### 2. Setup the Arduino Nicla Voice Board to collect data

After flashing the MCU and NDP chips, connect the Nicla Voice directly to your computer's USB port. Linux, Mac OS, and Windows platforms are supported. From a command prompt or terminal, run:

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

<Info>
  **Use syntiant compatible pre-processing blocks**

  The Arduino Nicla Voice is based on the Syntiant NDP120 Neural Decision Processor™ and needs to use dedicated Syntiant DSP blocks.
</Info>

With everything set up you can now build your first machine learning model and evaluate it using the Arduino Nicla Voice Board with this tutorial:

* [Syntiant / Syntiant-RC-Go-Stop-NDP120](https://studio.edgeimpulse.com/studio/412552)
* [Motion Recognition - Syntiant](/tutorials/hardware/syntiant-ndp-motion-recognition)

### FAQ

* How to use Arduino-CLI with macOS M1 chip? You will need to install Rosetta2 to run the Arduino-CLI. See details on [Apple website](https://support.apple.com/en-us/HT211861).
* How to label my classes? The NDP chip expects one and only negative class and it should be the last in the list. For instance, if your original dataset looks like: `yes, no, unknown, noise` and you only want to detect the keyword 'yes' and 'no', merge the 'unknown' and 'noise' labels in a single class such as `z_openset` (we prefix it with 'z' in order to get this class last in the list).
* If you get quarantine warnings on MacOS when flashing the device try this command to unquarantine the files and then rerun the flashing command

```
sudo xattr -r -d com.apple.quarantine *
```

### End User License Agreement

In order to work with Syntiant models on Edge Impulse you will be asked to accept this [End User License Agreement (EULA)](https://cdn.edgeimpulse.com/eula/syntiant-ei-eula-2025-03-24.pdf) inside your Edge Impulse Project.


Built with [Mintlify](https://mintlify.com).