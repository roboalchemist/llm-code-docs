# Source: https://docs.edgeimpulse.com/hardware/boards/nxp-imx8-evk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NXP i.MX 8M Plus EVK

The NXP I.MX 8M Plus is a popular SoC found in many single board computers, development kits, and finished products. When prototyping, many users turn to the [official NXP Evaluation Kit for the i.MX 8M Plus](https://www.nxp.com/design/design-center/development-boards-and-designs/8MPLUSLPD4-EVK), known simply as the i.MX 8M Plus EVK. The board contains many of the ports, connections, and external components needed to verify hardware and software functionality. The board can also be used with Edge Impulse, to run machine learning workloads on the edge.

<Frame caption="i.MX 8M Plus EVK">
  <img src="https://mintcdn.com/edgeimpulse/ZmJxJ83AI9AZ1Kqd/.assets/images/nxp-imx8-plus-evk.png?fit=max&auto=format&n=ZmJxJ83AI9AZ1Kqd&q=85&s=71a19e73b5d3b98623ade28d10cefc7e" width="1600" height="900" data-path=".assets/images/nxp-imx8-plus-evk.png" />
</Frame>

The board contains:

* i.MX 8M Plus Quad applications processor
* 4x Arm® Cortex-A53 up to 1.8 GHz
* 1x Arm® Cortex-M7 up to 800 MHz
* Cadence® Tensilica® HiFi4 DSP up to 800 MHz
* Neural Processing Unit
* 6 GB LPDDR4
* 32 GB eMMC 5.1

> Special Note: The NPU is not currently used by Edge Impulse by default, but CPU-inferencing alone is adequate in most situations. The NPU can be leveraged however, if you export the Tensorflow from your Block Output after your model has been trained, by following these instructions: [Edge Impulse Studio -> Dashboard -> Block outputs](/studio/projects/dashboard#7-block-outputs). Once download, you can build an application, or use Python, to run the model accelerated via the i.MX8's NPU.

**Accessories included in the Evaluation Kit:**

* i.MX 8M Plus CPU module​
* Base board ​
* USB 3.0 to Type C cable.​
* USB A to micro B cable​
* USB Type C power supply

In addition to the i.MX 8M Plus EVK we recommend that you also add a camera and / or a microphone. Most popular USB webcams work fine on the development board out of the box.

### Installing dependencies

A few steps need to be performed to get your board ready for use.

#### Prerequisites

You will also need the following equipment to complete your first boot.

* Monitor
* Mouse and keyboard
* Ethernet cable or WiFi

#### Operating System Installation

NXP provides a ready-made operating system based on Yocto Linux, that can be downloaded from the NXP website. However, we'll need a Debian or Ubuntu-based image for Edge Impulse purposes, so you'll have to run an OS build and come away with a file that can be flashed to an SD Card and then booted up. The instructions for building the Ubuntu-derived OS for the board are located here: [https://github.com/nxp-imx/meta-nxp-desktop](https://github.com/nxp-imx/meta-nxp-desktop)

Follow the instructions, and once you have an image built, flash it to an SD Card, insert into the i.MX 8M Plus EVK, and power on the board.

Once booted up, open up a Terminal on the device, and run the following commands:

```
sudo su
wget https://nodejs.org/dist/latest-v20.x/node-v20.12.1-linux-arm64.tar.gz
tar -xvf node-v20.12.1-linux-arm64.tar.gz
sudo cp -r node-v20.12.1-linux-arm64/{bin,include,lib,share} /usr/
node --version
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
edge-impulse-linux
```

<Warning>
  **Important:** Edge Impulse requires Node.js version 20.x or later. Using older versions may lead to installation issues or runtime errors. Please ensure you have the correct version installed before proceeding with the setup.
</Warning>

### Connecting to Edge Impulse

You may need to reboot the board once the dependencies have finished installing. Once rebooted, run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your i.MX 8M Plus EVK is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=17ae3d5dc93a5d8d4f1fad186309b323" width="1600" height="463" data-path=".assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

### Deploying back to device

To run your impulse locally on the i.MX 8M Plus EVK, open up a terminal and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model, download the model to your i.MX 8M Plus EVK, and then start classifying. Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the model with your favourite programming language.

#### Image model?

If you have an image model then you can get a peek of what your i.MX 8M Plus EVK sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>

## Conclusion

The i.MX 8M Plus EVK is a fully-featured development kit, making it a great option for machine learning on the edge. With it's Ubuntu-based OS flashed, it is capable of both collecting data, as well as running local inference with Edge Impulse.

If you have any questions, be sure to reach out to us on [our Forums](https://forum.edgeimpulse.com/)!


Built with [Mintlify](https://mintlify.com).