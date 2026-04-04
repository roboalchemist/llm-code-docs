# Source: https://docs.edgeimpulse.com/hardware/devices/linux-x86_64.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux x86_64 devices

You can use your Linux x86\_64 device or computer as a fully-supported development environment for Edge Impulse for Linux. This lets you sample raw data, build models, and deploy trained machine learning models directly from the Studio. If you have a webcam and microphone plugged into your system, they are automatically detected and can be used to build models.

<Frame caption="Linux x86">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6941fbd-ubuntu-x86_64.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=cea9611905d943cf9e7a85e8278126be" width="1501" height="1000" data-path=".assets/images/6941fbd-ubuntu-x86_64.png" />
</Frame>

<Info>
  **Instruction set architectures**

  If you are not sure about your instruction set architectures, use:

  ```
  $ uname -m
  x86_64
  ```
</Info>

### Installing dependencies

To set this device up in Edge Impulse, run the following commands:

**Ubuntu/Debian:**

```
sudo apt install -y curl
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
```

<Warning>
  **Important:** Edge Impulse requires Node.js version 20.x or later. Using older versions may lead to installation issues or runtime errors. Please ensure you have the correct version installed before proceeding with the setup.
</Warning>

### Connecting to Edge Impulse

With all software set up, connect your camera or microphone to your operating system (see 'Next steps' further on this page if you want to connect a different sensor), and run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your machine is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=17ae3d5dc93a5d8d4f1fad186309b323" width="1600" height="463" data-path=".assets/images/dcbbb78-screenshot_2022-01-18_at_105616.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids) Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

### Deploying back to device

To run your impulse locally run on your Linux platform:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration, download the model to your local machine, and then start classifying. Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the model with your favourite programming language.

#### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).