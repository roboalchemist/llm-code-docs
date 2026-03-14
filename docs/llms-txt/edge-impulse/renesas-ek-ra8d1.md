# Source: https://docs.edgeimpulse.com/hardware/boards/renesas-ek-ra8d1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas EK-RA8D1

The RA8 is the first Cortex-M85 microcontroller in the market. The EK-RA8D1, an Evaluation Kit for the RA8D1 MCU Group, enables users to seamlessly evaluate the features of the RA8D1 MCU group and develop embedded systems applications using the Renesas Flexible Software Package (FSP) and e2 studio IDE. Users can use rich on-board features along with their choice of popular ecosystems add-ons to bring their big ideas to life.

The evaluation kit comes with a MIPI graphics expansion board mounted with an LCD display and a camera expansion board mounted with the OV3640 CSI camera. The kit can be assembled as follows:

<Frame caption="Renesas EK-RA8D1 Hardware">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-expansion.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=6b4c5f66b7871cf65acc7121a8e42f23" width="1600" height="872" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-expansion.png" />
</Frame>

This kit is put together primarily for image based applications. This document will get you started so you can create your own image based applications using Edge Impulse.

### Installing dependencies

The RA8D1 supports all of Edge Impulse’s device features, including ingestion, remote management and inferencing. To set the device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. [JLink Flashing Tools](https://www.segger.com/downloads/jlink)

<Info>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Info>

#### Updating the firmware

Edge Impulse Studio can collect image data directly from your EK-RA8D1 and also help you trigger in-system inferences to debug your model. In order to allow Edge Impulse Studio to interact with your device, you first need to flash it with our base firmware image.

##### 1. Download the base firmware image

[Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/renesas-ek-ra8d1.zip), and unzip the file. Within this folder, you will find several flashing files for different operating systems (MacOS, Linux and Windows). Locate the file for your respective OS, and follow the next steps.

##### 2. Connect the EK-RA8D1 to your computer

To flash the board, you need to connect to the debug port J10:

<Frame caption="EK-RA8D1 Debug Port">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-debug-port.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=d7f9451fb8bf80cedbc2b66142b3d629" width="1600" height="872" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-debug-port.png" />
</Frame>

The LCD screen will turn on and display the home screen as shown.

#### 3. Load the base firmware image

Open the flash script for your operating system (`flash_win.bat`, `flash_mac.command` or `flash_linux.sh`) to flash the firmware. Once you flash the firmware, the display will switch to show the default Edge Impulse Face Detection using FOMO project.

<Frame caption="Default FOMO Firmware">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-display-screen.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=8935c63165a400270b8161522ee91709" width="1209" height="1000" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-display-screen.png" />
</Frame>

Now you are ready to connect the RA8D1 to the studio and create your own project.

### Connecting to Edge Impulse

To connect to the Edge Impulse Studio, you need to connect to the USB Full Speed port J11. Please make sure that the jumpers J12 and J15 are in the correct position (J12 in position 2-3 and J15 connected). The correct configuration is shown in the image below:

<Frame caption="Default FOMO Firmware">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-correct-jumpers.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=b6a113df073005b63c96fd6134eb6385" width="750" height="1000" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-correct-jumpers.png" />
</Frame>

It is important to remember that to run inference, to collect data from the RA8D1, and use the Edge Impulse CLI tools,  you **have** to connect via port J11. Port J10 is only used for flashing the firmware.

> Note that it is safe to connect two cables to your board at ports J10 and J11 simultaneously. Then you can flash it and run inference without having to change ports.

#### 1. Setting up your account

After connecting to port J11, from a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### 2. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices** on the left sidebar. The device will be listed there:

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/renesas-ek-ra8d1/ek-ra8d1-device-connected.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=f60923f7f1d25db7b976840a68b29668" width="1600" height="387" data-path=".assets/images/renesas-ek-ra8d1/ek-ra8d1-device-connected.png" />
</Frame>

#### 3. Collecting data

Once the device is connected, you can proceed to the data acquisition tab and start collecting your image data directly from the device.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

### Next steps: building a machine learning model

With everything set up you can now build your first image based machine learning model with these tutorials:

* [Detecting objects with FOMO](/tutorials/end-to-end/object-detection-centroids).
* [Image classification](/tutorials/hardware/sony-spresense-image-classification).

### Running NVIDIA TAO models on the RA8D1

You can now also take advantage of NVIDIA TAO models for your machine learning applications for improved performance. TAO models typical occupy more space than is internally available on the RA8. For this reason, flashing the RA8D1 with a TAO model is slightly more involved than simply downloading the firmware. For instructions on how to accomplish this please refer to the [NVIDIA TAO on RA8 tutorial](/tutorials/hardware/renesas-ra8d1-nvidia-tao) for using your RA8D1 with TAO models.


Built with [Mintlify](https://mintlify.com).