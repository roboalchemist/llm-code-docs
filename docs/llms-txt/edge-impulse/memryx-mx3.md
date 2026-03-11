# Source: https://docs.edgeimpulse.com/hardware/boards/memryx-mx3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MemryX MX3

The MemryX MX3 is the latest state-of-the-art AI inference co-processor for running trained Computer Vision (CV) neural network models built using any of the major AI frameworks (TensorFlow, LiteRT (previously Tensorflow Lite), ONNX, PyTorch, Keras) and offering the widest operator support. Running alongside any Host Processor, the MX-3 offloads CV inferencing tasks providing power savings, latency reduction, and high accuracy. The MX-3 can be cascaded together optimizing performance based on the model being run. The MX3 Evaluation Board (EVB) consists of PCBA with 4 MX3’s installed. Multiple EVBs can be cascaded using a single interface cable.

MemryX Developer Hub provides simple 1-click compilation. This portal is intuitive and easy-to-use and includes many tools, such as a Simulator, Python and C++ APIs, and example code. Contact [MemryX](https://memryx.com/contact/) to request an EVB and access to the online Developer Hub.

<Frame caption="MX3 EVB">
  <img src="https://mintcdn.com/edgeimpulse/O-6Yv5nSVCNsemg-/.assets/images/memryx/mx3-evb.jpg?fit=max&auto=format&n=O-6Yv5nSVCNsemg-&q=85&s=cd7bb176ad9e41f3d01ca86cef0c6342" width="886" height="1000" data-path=".assets/images/memryx/mx3-evb.jpg" />
</Frame>

### Installing dependencies

To use MemryX devices with Edge Impulse deployments you must install the following dependencies on your Linux target that has a MemryX device installed.

* [Python 3.8+](https://www.python.org/downloads/): This is a prerequisite for the MemryX SDK.

For Debian based Linux devices you may need to install using the following command. For other Linux distributions please use the necessary package manager for installation.

```
sudo add-apt-repository universe
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8 python3.8-dev python3.8-distutils python3.8-venv
```

* MemryX tools and drivers: Please contact [MemryX](https://memryx.com/contact/) for access to their tools and drivers
* [Edge Impulse Linux](/tools/libraries/sdks/inference/linux): This will enable you to connect your development system directly to Edge Impulse Studio

**Ubuntu/Debian x86:**

```
sudo apt install -y curl
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
npm install edge-impulse-linux -g --unsafe-perm
```

<Warning>
  **Important:** Edge Impulse requires Node.js version 20.x or later. Using older versions may lead to installation issues or runtime errors. Please ensure you have the correct version installed before proceeding with the setup.
</Warning>

### Connecting to Edge Impulse

After working through a getting started tutorial, and with all software set up, connect your camera or microphone to your operating system and run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

<Info>
  **Need sudo?**

  Some commands require the use of `sudo` in order to have proper access to a connected camera. If your `edge-impulse-linux` or `edge-impulse-linux-runner` command fails to enumerate your camera please try the command again with `sudo`
</Info>

#### Verifying that your device is connected

Your machine is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=17ae3d5dc93a5d8d4f1fad186309b323" width="1600" height="463" data-path=".assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Counting objects using FOMO](/tutorials/topics/post-processing/count-objects-fomo)

<Info>
  **No need to int8 model**

  MemryX devices only need a float32 model to be passed into the compiler. Therefore, when developing models with Edge Impulse it is better not to profile int8 (quantize) models. You may prevent generation, profiling, and deployment of int8 models by deselecting **Profile int8 model** under the **Advanced training settings** of your Impulse Design model training section.

  <Frame caption="Deselect Profile int8 model">
    <img src="https://mintcdn.com/edgeimpulse/O-6Yv5nSVCNsemg-/.assets/images/memryx/memx-int8-profile.png?fit=max&auto=format&n=O-6Yv5nSVCNsemg-&q=85&s=92d93cd011c550b7661a13ed57b97131" width="1074" height="859" data-path=".assets/images/memryx/memx-int8-profile.png" />
  </Frame>
</Info>

#### Frames per second (FPS), Latency, and Synchronous Calls

The implementation of MemryX MX3 devices into the Edge Impulse SDK uses synchronous calls to the evaluation board. Therefore, frame per second information is relative to that API. For faster performance there is an asynchronous API from MemryX that may be used in place for high performance applications. Please contact Edge Impulse Support for assistance in getting the best performance out of your MemryX MX3 devices!

### Deploying back to device

In order to achieve full hardware acceleration models must be converted from their original format to run on the MX3. This can be done by selecting the MX3 from the Deployment Screen. This will generate a .zip file with models that can be used in your application for the MX3. The block uses the MemryX compiler so that the model will run accelerated on the device.

<Frame caption="MemryX Dataflow Program">
  <img src="https://mintcdn.com/edgeimpulse/O-6Yv5nSVCNsemg-/.assets/images/memryx/memryx-deployment-all.png?fit=max&auto=format&n=O-6Yv5nSVCNsemg-&q=85&s=157b3a6133eaaeac75680b3ebed23a83" width="1184" height="672" data-path=".assets/images/memryx/memryx-deployment-all.png" />
</Frame>

#### MemryX Dataflow Program Deployment Block

The MemryX Dataflow Program Deployment Block generates a .zip file that contains the converted Edge Impulse model usable by MX3 devices (.dfp file). One can use the MemryX SDK to develop applications using this file.

#### Linux (x86\_64 with MemryX MX3)

The output from this Block is an Edge Impulse .eim file that, once saved onto the computer with the MX3 connected, can be run with the following command.

```
edge-impulse-linux-runner --model-file <path-to-model.eim>
```

Running this command will ensure that the model runs accelerated on the MemryX MX3 device.

<Info>
  **Need sudo?**

  Some commands require the use of `sudo` in order to have proper access to a connected camera. If your `edge-impulse-linux` or `edge-impulse-linux-runner` command fails to enumerate your camera please try the command again with `sudo`
</Info>

#### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>

### Troubleshooting

#### UnhandledPromiseRejectionWarning: No response within 5 seconds

Please restart your MX3 evaluation board by using the reset button. Then use the `edge-impulse-linux-runner` command again. If you are still having issues please contact Edge Impulse support.

#### Failed to run impulse Capture process failed with code 1

1. You may need to use `sudo edge-impulse-linux-runner` to be able to access the camera on your system.
2. Ensure that you do not have any open processes still using the camera. For example, if you have the Edge Impulse web browser image acquisition page open or a virtual meeting software, please close or disable the camera usage in those applications.
3. This error could mean that your camera is in use by another process. Check if you have any application open that is using the camera. This error could exist when your previous attempt to run `edge-impulse-linux-runner` failed with exception. In that case, check if you have a `gst-launch-1.0` process running. For example:

```
ps aux | grep gst-launch-1.0
   5615 pts/0    00:01:52 gst-launch-1.0
```

In this case, the first number (here `5615`) is a process ID. Kill the process:

```
kill -9 5615
```

And try to run the model with `edge-impulse-linux-runner` once again.

#### Error: Classifying failed, error code was -23 (other issues)

If the previous step didn't help, try to get additional debug data. With your EIM model downloaded, open one terminal window and do:

```
./model.eim /tmp/ei.socket
```

Then in another terminal:

```
edge-impulse-linux-runner --model-file /tmp/ei.socket
```

This should give you additional info in the first terminal about the possible root of your issue. Contact Edge Impulse Support with the results.


Built with [Mintlify](https://mintlify.com).