# Source: https://docs.edgeimpulse.com/hardware/boards/nvidia-jetson.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA Jetson

> '**NVIDIA Jetson Orin**' refers to the following devices:
>
> * Jetson AGX Orin Series, Jetson Orin NX Series, Jetson Orin Nano Series
>
> '**NVIDIA Jetson**' refers to the following devices:
>
> * Jetson AGX Xavier Series, Jetson Xavier NX Series, Jetson TX2 Series, Jetson TX1, Jetson Nano
>
> '**Jetson**' refers to all NVIDIA Jetson devices.

The NVIDIA Jetson and NVIDIA Jetson Orin devices are embedded Linux devices featuring a GPU-accelerated processor (NVIDIA Tegra) targeted at edge AI applications. You can easily add a USB external microphone or camera - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the Edge Impulse Studio.

In addition to the NVIDIA Jetson and NVIDIA Jetson Orin devices we also recommend that you add a camera and/or a microphone. Most popular USB webcams work fine on the development board out of the box.

<Warning>
  **Powering your Jetson**

  Although powering your Jetson via USB is technically supported, some users report on forums that they have issues using USB power. If you have any issues such as the board resetting or becoming unresponsive, consider powering via the DC barrel connector.
  **Don't forget to change the jumper!** See your target's manual for more information.

  An added bonus to powering via the DC barrel plug: you can carry out your first boot w/o an external monitor or keyboard.
</Warning>

<Frame caption="NVIDIA Jetson Orin">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/nvidia-orin.jpeg?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=53fca186d3a2460ae52f93aea30adfca" width="630" height="354" data-path=".assets/images/nvidia-orin.jpeg" />
</Frame>

### Installing dependencies

Follow NVIDIA's setup instructions found at [NVIDIA Jetson Getting Started Guide](https://developer.nvidia.com/embedded/learn/getting-started-jetson) depending on your hardware.

For example:

* [NVIDIA Jetson Orin Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
* [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-agx-orin-devkit)
* [NVIDIA Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)

#### JetPack

For NVIDIA Jetson Orin:

* use SD Card image with [JetPack 5.1.2](https://developer.nvidia.com/embedded/jetpack-sdk-512) or
* use SD Card image with [JetPack 6.0](https://developer.nvidia.com/embedded/jetpack-sdk-60)

> Note that you may need to update the UEFI firmware on the device when
> migrating to JetPack 6.0 from earlier JetPack versions. See [NVIDIA's Initial
> Setup Guide for Jetson Nano Development
> Kit](https://www.jetson-ai-lab.com/initial_setup_jon.html) for instructions on
> how to get JetPack 6.0 GA on your device.

For NVIDIA Jetson devices use SD Card image with [Jetpack
4.6.4](https://developer.nvidia.com/jetpack-sdk-464). See also [JetPack
Archive](https://developer.nvidia.com/embedded/jetpack-archive) or [Jetson
Download Center](https://developer.nvidia.com/embedded/downloads).

When finished, you should have a bash prompt via the USB serial port, or using an external monitor and keyboard attached to the Jetson. You will also need to connect your Jetson to the internet via the Ethernet port (there is no WiFi on the Jetson). (After setting up the Jetson the first time via keyboard or the USB serial port, you can SSH in.)

#### Make sure your ethernet is connected to the Internet

Issue the following command to check:

```bash  theme={"system"}
ping -c 3 www.google.com
```

The result should look similar to this:

```bash  theme={"system"}
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
```

#### Running the setup script

To set this device up in Edge Impulse, run the following commands (from any folder). When prompted, enter the password you created for the user on your Jetson/Orin in step 1. The entire script takes a few minutes to run (using a fast microSD card).

For Jetson:

```bash  theme={"system"}
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/jetson.sh | bash
```

For Orin:

```bash  theme={"system"}
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/orin.sh | bash
```

### Connecting to Edge Impulse

With all software set up, connect your camera or microphone to your Jetson (see 'Next steps' further on this page if you want to connect a different sensor), and run:

```bash  theme={"system"}
edge-impulse-linux
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9d5f41e-screenshot_2021-04-14_at_123509.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=b2eb27438eaa91770f9005bb6a45b65f" width="1331" height="292" data-path=".assets/images/9d5f41e-screenshot_2021-04-14_at_123509.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification)
* [Object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Choose the deployment target according to your device and JetPack version. See table below.

| JetPack version |           EIM Deployment           |                   Docker Deployment                   |
| :-------------: | :--------------------------------: | :---------------------------------------------------: |
|      4.6.4      |    NVIDIA Jetson (JetPack 4.6.4)   |    Docker container (NVIDIA Jetson - JetPack 4.6.4)   |
|      5.1.2      | NVIDIA Jetson Orin (JetPack 5.1.2) | Docker container (NVIDIA Jetson Orin - JetPack 5.1.2) |
|       6.0       |  NVIDIA Jetson Orin (JetPack 6.0)  |  Docker container (NVIDIA Jetson Orin - JetPack 6.0)  |

For more information on Docker deployment see [run inference using a Docker container](/hardware/deployments/run-docker).

Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

### Deploying back to device

To run your impulse locally, just connect to your Jetson again, and run:

```bash  theme={"system"}
edge-impulse-linux-runner
```

This will automatically compile your model with full **GPU and hardware acceleration**, download the model to your Jetson, and then start classifying. Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the model with your favourite programming language.

#### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f5ecd66-demo1.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=00d19c1d3f0ca1adfc5123c3370374b6" width="400" height="440" data-path=".assets/images/f5ecd66-demo1.png" />
</Frame>

### Troubleshooting

#### edge-impulse-linux reports "OOM killed!"

Using make -j without specifying job limits can overtax system resources, causing "OOM killed" errors, especially on resource-constrained devices this has been observed on many of our supported Linux based SBCs.

Avoid using make -j without limits. If you experience OOM errors, limit concurrent jobs. A safe practice is:

```
make -j`nproc`
```

This sets the number of jobs to your machine's available cores, balancing performance and system load.

##### edge-impulse-linux reports "\[Error: Input buffer contains unsupported image format]"

This is probably caused by a missing dependency on libjpeg. If you run:

```bash  theme={"system"}
vips --vips-config
```

The end of the output should show support for file import/export with libjpeg, like so:

```bash  theme={"system"}
file import/export with libjpeg: yes (pkg-config)
image pyramid export: no
use libexif to load/save JPEG metadata: no
alex@jetson1:~$
```

If you don't see jpeg support as "yes", rerun the setup script and take note of any errors.

##### edge-impulse-linux reports "Failed to start device monitor!"

If you encounter this error, ensure that your entire home directory is owned by you (especially the .config folder):

```bash  theme={"system"}
sudo chown -R $(whoami) $HOME
```

#### Long warm-up time and under-performance

By default, the Jetson enables a number of aggressive power saving features to disable and slow down hardware that is detected to be not in use. Experience indicates that sometimes the GPU cannot power up fast enough, nor stay on long enough, to enjoy best performance. You can run a script to enable maximum performance on your Jetson.

**ONLY DO THIS IF YOU ARE POWERING YOUR JETSON FROM A DEDICATED POWER SUPPLY. DO NOT RUN THIS SCRIPT WHILE POWERING YOUR JETSON THROUGH USB.**

Your Jetson device device can operate in different power modes, a set of power budgets with several predefined configurations CPU and GPU frequencies and number of cores online. To enable maximum performance:

1. Switch to a mode with the maximum power budget and/or frequencies.
2. Then set the clocks to maximum.

To determine the maximum mode for your device visit the **Supported Modes and Power Efficiency** section in Jetson Linux Developer Guide for your L4T.

For example for [R35.4.1](https://developer.nvidia.com/embedded/jetson-linux-r3541):

* [NVIDIA Jetson Orin, Jetson  Orin NX and Jetson AGX Orin](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html)
* [NVIDIA Jetson Xavier NX and Jetson AGX Xavier](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonXavierNxSeriesAndJetsonAgxXavierSeries.html#supported-modes-and-power-efficiency)

For [R32.7.5](https://developer.nvidia.com/embedded/linux-tegra-r3275):

* [Jetson Nano and Jetson TX1](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3275/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/power_management_nano.html#wwpID0E0FL0HA)
* [Jetson TX2](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3275/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/power_management_tx2_32.html#wwpID0E0OO0HA)

To enable maximum performance, switch to **mode ID 0** and set the maximum frequencies of the clocks as follows.

```bash  theme={"system"}
sudo /usr/sbin/nvpmodel -m 0
sudo /usr/bin/jetson_clocks
```

> For NVIDIA Jetson Xavier NX use **mode ID 8**

Additionally, due to Jetson GPU internal architecture, running small models on it is less efficient than running larger models. E.g. the continuous gesture recognition model runs faster on Jetson CPU than on GPU with TensorRT acceleration.

According to our benchmarks, running vision models and larger keyword spotting models on GPU will result in faster inference, while smaller keyword spotting models and gesture recognition models (that also includes simple fully connected NN, that can be used for analyzing other time-series data) will perform better on CPU.

#### Program fails to find shared library

If you see an error similar to this when running Linux C++ SDK examples with GPU acceleration,

```bash  theme={"system"}
jetson@localhost:~/example-standalone-inferencing-linux$ ./build/custom
./build/custom: error while loading shared libraries: libnvinfer.so.8: cannot open shared object file: No such file or directory
```

then please download and use the SD card image version for your target see JetPack section above. The error is likely caused by an incompatible version of NVidia's GPU libraries - or the absence of these libraries.


Built with [Mintlify](https://mintlify.com).