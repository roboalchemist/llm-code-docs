# Source: https://docs.edgeimpulse.com/hardware/devices/seeed-recomputer-jetson.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed reComputer Jetson

reComputer for Jetson series are compact edge computers built with NVIDIA advanced AI embedded systems: Jetson-10 (Nano) and Jetson-20 (Xavier NX). With rich extension modules, industrial peripherals, thermal management combined with decades of Seeed’s hardware expertise, reComputer for Jetson is ready to help you accelerate and scale the next-gen AI product emerging in diverse AI scenarios.

<Frame caption="Seeed reComputer for Jetson Series">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/reComputerheadline.png?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=dcad3440c8b742c5c82471b628503931" width="1600" height="853" data-path=".assets/images/reComputerheadline.png" />
</Frame>

You can easily add a USB external microphone or camera - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the Studio. Currently, four versions have been launched. See [reComputer Series Introduction](https://wiki.seeedstudio.com/reComputer_Jetson_Series_Introduction) web page.

**This guide has only been tested with the** [**reComputer J1020**](https://www.seeedstudio.com/Jetson-10-1-H0-p-5335.html).

| Product                 | [reComputer J1010](https://www.seeedstudio.com/Jetson-10-1-A0-p-5336.html)         | [reComputer J1020](https://www.seeedstudio.com/Jetson-10-1-H0-p-5335.html)       | [reComputer J2011](https://www.seeedstudio.com/Jetson-20-1-H1-p-5328.html)       | [reComputer J2012](https://www.seeedstudio.com/Jetson-20-1-H2-p-5329.html)       |
| ----------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| SKU                     | 110061362                                                                          | 110061361                                                                        | 110061363                                                                        | 110061401                                                                        |
| Side View               | ![](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/frontview3_1.png) | ![](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/frontview5.png) | ![](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/frontview5.png) | ![](https://files.seeedstudio.com/wiki/recomputer-Jetson-20-1-H1/frontview5.png) |
| Equipped Module         | Jetson Nano 4GB                                                                    | Jetson Nano 4GB                                                                  | Jetson Xavier NX 8GB                                                             | Jetson Xavier NX 16GB                                                            |
| Operating carrier Board | J1010 Carrier Board                                                                | Jetson A206                                                                      | Jetson A206                                                                      | Jetson A206                                                                      |
| Power Interface         | Type-C connector                                                                   | DC power adapter                                                                 | DC power adapter                                                                 | DC power adapter                                                                 |

In addition to the Jetson Nano we recommend that you also add a camera and / or a microphone. Most popular USB webcams work fine on the development board out of the box.

### Installing dependencies

You will also need the following equipment to complete your first boot.

* A monitor with HDMI interface. (For the A206 carrier board, a DP interface monitor can also be used.)
* A set of mouse and keyboard.
* An ethernet cable or an external WiFi adapter (there is no WiFi on the Jetson)

The reComputer is shipped with the an operating system burned in. Before we use it, it is required to complete some necessary configuration steps: Follow [reComputer Series Getting Started](https://wiki.seeedstudio.com/reComputer_Jetson_Series_Initiation) web page. When completed, open a new Terminal by pressing CTRL + Alt + T. It will look as shown:

<Frame caption="reComputer Terminal">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/reComputer-terminal.png?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=b499fe66ad9dce0efd7613fcd3a08c5f" width="1920" height="1080" data-path=".assets/images/reComputer-terminal.png" />
</Frame>

#### Make sure your ethernet is connected to the Internet

Issue the following command to check:

```
ping -c 3 www.google.com
```

The result should look similar to this:

```
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
```

#### Running the setup script

To set this device up in Edge Impulse, run the following commands (from any folder). When prompted, enter the password you created for the user on your Jetson in step 1. The entire script takes a few minutes to run (using a fast microSD card).

```
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/jetson.sh | bash
```

### Connecting to Edge Impulse

With all software set up, connect your camera or microphone to your Jetson (see 'Next steps' further on this page if you want to connect a different sensor), and run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-device-recomputer.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=e3e0e0ff0d4bf627cb874575a10bc3de" width="1600" height="360" data-path=".assets/images/studio-device-recomputer.png" />
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

To run your impulse locally, just connect to your Jetson again, and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration, download the model to your Jetson, and then start classifying. Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the model with your favourite programming language.

#### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>

#### Running models on the GPU

Due to some incompatibilities we don't run models on the GPU by default. You can enable this by following the [TensorRT instructions](/tools/libraries/sdks/inference/linux/cpp) in the C++ SDK.

### Troubleshooting

#### edge-impulse-linux reports "OOM killed!"

Using make -j without specifying job limits can overtax system resources, causing "OOM killed" errors, especially on resource-constrained devices this has been observed on many of our supported Linux based SBCs.

Avoid using make -j without limits. If you experience OOM errors, limit concurrent jobs. A safe practice is:

```
make -j`nproc`
```

This sets the number of jobs to your machine's available cores, balancing performance and system load.

#### edge-impulse-linux reports "\[Error: Input buffer contains unsupported image format]"

This is probably caused by a missing dependency on libjpeg. If you run:

```
vips --vips-config
```

The end of the output should show support for file import/export with libjpeg, like so:

```
file import/export with libjpeg: yes (pkg-config)
image pyramid export: no
use libexif to load/save JPEG metadata: no
alex@jetson1:~$
```

If you don't see jpeg support as "yes", rerun the setup script and take note of any errors.

#### edge-impulse-linux reports "Failed to start device monitor!"

If you encounter this error, ensure that your entire home directory is owned by you (especially the .config folder):

```
sudo chown -R $(whoami) $HOME
```

#### Long warm-up time and under-performance

By default, the Jetson Nano enables a number of aggressive power saving features to disable and slow down hardware that is detected to be not in use. Experience indicates that sometimes the GPU cannot power up fast enough, nor stay on long enough, to enjoy best performance. You can run a script to enable maximum performance on your Jetson Nano.

**ONLY DO THIS IF YOU ARE POWERING YOUR JETSON NANO FROM A DEDICATED POWER SUPPLY. DO NOT RUN THIS SCRIPT WHILE POWERING YOUR JETSON NANO THROUGH USB.**

To enable maximum performance, run:

```
sudo /usr/bin/jetson_clocks
```

### Further resources

Hackster.io [tutorial](https://www.hackster.io/SeeedStudio/hard-hat-detection-on-recomputer-j1010-using-edge-impulse-52e63c): Train an embedded Machine Learning model based on Edge Impulse to detect hard hat and deploy it to the reComputer J1010 for Jetson Nano.


Built with [Mintlify](https://mintlify.com).