# Source: https://docs.edgeimpulse.com/hardware/boards/avnet-rasynboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Avnet RASynBoard

<Frame caption="Avnet RASynBoard">
  <img src="https://mintcdn.com/edgeimpulse/iHoev6xDD8x2bVAk/.assets/images/avnet/rasynboard-kit.jpg?fit=max&auto=format&n=iHoev6xDD8x2bVAk&q=85&s=79e0db761c06fe20ace396aa653c478b" width="337" height="225" data-path=".assets/images/avnet/rasynboard-kit.jpg" />
</Frame>

[RASynBoard](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rasynboard/) is a tiny (25mm x 30mm), ultra-low power, edge AI/ML board, based on a [Syntiant® NDP120 Neural Decision Processor™ (NDP)](https://www.syntiant.com/), a Renesas RA6M4 host MCU plus a power efficient DA16600 Wi-Fi/BT combo module. The NDP120 subsystem with on-board digital microphone, IMU motion sensor and SPI Flash memory, achieves highly efficient processing of acoustic and motion events. Battery and USB-C device connectors facilitate standalone use, while a compact under-board connector enables integration with custom OEM boards and additional sensors.

An IO board (50mm x 30mm) is included for implementation of a compact two-board evaluation kit assembly. This pins-out a subset of the NDP120 and RA6M4 I/Os to popular Pmod, Click header and expansion header footprints, enabling connection with additional external microphones and sensor options. An onboard debugger MCU (SWD and UART interfaces), button switches, RGB LED and removable MicroSD storage, further maximize prototyping versatility and utility.

NDP120 AI/ML models for popular use-cases (pre-engineered by [Syntiant®](https://www.syntiant.com/) and other vendors) are loaded from local SPI Flash storage for efficient execution on the ultra-low power NDP120 neural accelerator device.

RA6M4 MCU application software development and debug is supported via the Renesas e2 Studio IDE, interfaced via the E2OB debugger MCU on the IO board.
Key Features

* Accelerated Edge-AI and ML applications
* Battery-powered remote sensor systems
* Industrial smart sensors
* Motor predictive maintenance
* Always-on speech recognition and sensor fusion processing

Getting Started Guides may be found at Avnet's Github repositories:

* [RASynBoard-HUB](https://github.com/Avnet/RASynBoard-HUB)
* [RASynBoard-Out-of-Box-Demo](https://github.com/Avnet/RASynBoard-Out-of-Box-Demo)

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software. The Renesas software will require registration for a Renesas account.

* [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation)
* [Renesas Flash Programmer (RFP)](https://www.renesas.com/us/en/software-tool/renesas-flash-programmer-programming-gui#download)
* [Renesas e2 studio (IDE) + RA family Flexible Software Package](https://www.renesas.com/us/en/software-tool/renesas-flash-programmer-programming-gui#download)

### Connecting to Edge Impulse

#### 1. Download the firmware

Download the Edge Impulse RASynBoard firmware for audio or IMU below and connect the USB cable to your computer:

* [RASynBoard firmware](https://cdn.edgeimpulse.com/firmware/avnet-rasyn.zip)

Follow the instructions in the .zip's for installation instructions

#### 2. Setup the Avnet RASynBoard to collect data

After flashing the MCU per the [RASynBoard Development Guide](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rasynboard/) instructions, please reconnect the Avnet RASynBoard directly to your computer's USB port. Linux, Mac OS, and Windows platforms are supported. From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/rasynboard-connected.png?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=6290855733fa5dca0dc42ba88fafb91b" width="1598" height="251" data-path=".assets/images/rasynboard-connected.png" />
</Frame>

### Next steps: building a machine learning model

<Info>
  **Use syntiant compatible pre-processing blocks**

  The Avnet RASynBoard is based on the Syntiant NDP120 Neural Decision Processor™ and needs to use dedicated Syntiant DSP blocks.
</Info>

With everything set up you can now build your first machine learning model and evaluate it using one of these tutorials:

* [Keyword spotting - Syntiant (RC Commands)](/tutorials/hardware/syntiant-ndp-keyword-spotting)
* [Motion Recognition - RASynBoard](/tutorials/hardware/avnet-rasyn-motion-recognition)
* [Avnet's Videos for Using RASynBoard with Edge Impulse](http://avnet.me/RASynDocsDataIngestion)

### FAQ

* How to label my classes? The NDP chip expects one and only negative class and it should be the last in the list. For instance, if your original dataset looks like: `yes, no, unknown, noise` and you only want to detect the keyword 'yes' and 'no', merge the 'unknown' and 'noise' labels in a single class such as `z_openset` (we prefix it with 'z' in order to get this class last in the list).

* RFP Error(E3000107): This device does not match the connection parameters
  If you encounter this error while programming the Renesas device on the RASynBoard please follow this [workaround](https://github.com/Avnet/RASynBoard-Out-of-Box-Demo/blob/rasynboard_v2_tiny/docs/RASynTroubleshootingGuide.md#renesas-flash-programming-rfp-errors).

### End User License Agreement

In order to work with Syntiant models on Edge Impulse you will be asked to accept this [End User License Agreement (EULA)](https://cdn.edgeimpulse.com/eula/syntiant-ei-eula-2025-03-24.pdf) inside your Edge Impulse Project.


Built with [Mintlify](https://mintlify.com).