# Source: https://docs.edgeimpulse.com/hardware/boards/qualcomm-rb3-gen-2-dev-kit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Qualcomm Dragonwing RB3 Gen 2 Dev Kit

The Qualcomm Dragonwing RB3 Gen 2 Development Kit is a powerful Linux-based development board based around the QCS6490 SoC. It has two built-in cameras, a Kryo™ 670 CPU, Adreno™ 643L GPU and 12 TOPS Hexagon™ 770 NPU. It's fully supported by Edge Impulse - you'll be able to sample raw data, build models, and deploy trained machine learning models directly from the Studio. Other QCS6490-based kits are available from various manufacturers such as [Advantech](/hardware/boards/advantech-aom2721-osm), [Tria](/hardware/boards/tria-vision-ai-kit-6490), [Thundercomm](/hardware/boards/thundercomm-rubikpi3), and [Quectel](/hardware/boards/quectel-pi-sg565d).

<Frame caption="Qualcomm Dragonwing RB3 Gen 2 Development Kit">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/qualcomm-dragonwing-rb3-gen2.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=85b3be4c187768471457298d5fb780c0" width="1221" height="1000" data-path=".assets/images/qualcomm/qualcomm-dragonwing-rb3-gen2.png" />
</Frame>

<iframe src="https://www.youtube.com/embed/oQe06yTahoI" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Setting Up Your Qualcomm Dragonwing RB3 Gen 2 Dev Kit

### 1. Starting up your development board and connecting to the internet

1. Install the [Edge Impulse CLI](/tools/clis/edge-impulse-cli) on your computer.

2. Connect power to the back of the RB3 Development Kit.

3. Connect the RB3 to your computer using a micro-USB cable (using the port highlighted in yellow):

   <Frame caption="Connect the dev kit to your computer using a micro-USB cable">
     <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rb3gen2-visionkit-serial.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=becfb5f9410f30a76c06803e4cf309bf" alt="" width="375" data-path=".assets/images/qualcomm/rb3gen2-visionkit-serial.png" />
   </Frame>

4. Open a serial connection between your host computer and the board.

<Info>
  You can do this directly using the Edge Impulse CLI by running the following command from your command prompt or terminal:
</Info>

```bash  theme={"system"}
edge-impulse-run-impulse --raw
```

5. Hold the rightmost push button (seen from the front, highlighted in red) for \~2 seconds. You should see output in the terminal indicating that the board is starting up.

   <Frame caption="Press the 'On' button for ~2 seconds">
     <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rb3gen2-visionkit-power-btn.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=65544584b63dc4ded8d5e69c904e9211" alt="" width="563" data-path=".assets/images/qualcomm/rb3gen2-visionkit-power-btn.png" />
   </Frame>

6. After 30-60 seconds you should see a login prompt in your terminal. Log in with:

   * Username: `root`
   * Password `oelinux123`

7. Next, set up a network connection, either:
   1. Connect an Ethernet cable.
   2. Or, if you want to connect over WiFi:
      * Qualcomm Linux \<1.3: [edit the wpa\_supplicant.conf](https://docs.qualcomm.com/bundle/publicresource/topics/80-70014-253/ubuntu_host.html#sub\$set_up_wifi).
      * Qualcomm Linux 1.3: [use nmcli](https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-253/set_up_the_device.html#panel-0-vwj1bnr1tab\$using-wi-fi).

<Info>
  After connecting the board to the internet, reboot it. This will refresh the system clock (through the NTP), resolving an issue with invalid certificates when installing the Edge Impulse CLI.
</Info>

8. If you want to continue setting up over ssh (so you can unplug the device from your computer), find your IP address via:

   ```bash  theme={"system"}
   $ ifconfig | grep "inet addr:" | grep -v "127.0.0.1"
   inet addr:192.168.1.38 Bcast:192.168.1.255 Mask:255.255.255.0
   ```

   Then log in via ssh (password: `oelinux123`):

   ```bash  theme={"system"}
   $ ssh root@192.168.1.38
   ```

### 2. Installing the Edge Impulse Linux CLI

On the RB3 install the Edge Impulse CLI and other dependencies via:

```bash  theme={"system"}
$ wget https://cdn.edgeimpulse.com/firmware/linux/setup-edge-impulse-qc-linux.sh
$ sh setup-edge-impulse-qc-linux.sh
$ source ~/.profile
```

### 3. Connecting to Edge Impulse

With all dependencies set up, run:

```bash  theme={"system"}
$ edge-impulse-linux
```

This will start a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects, or use a different camera (e.g. a USB camera) run the command with the `--clean` argument.

### 4. Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="RB3 Connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rb3-connected.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=ebe0c0aa62b5d280a4470d624eeaecbb" width="1600" height="223" data-path=".assets/images/qualcomm/rb3-connected.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Responding to your voice](/tutorials/end-to-end/keyword-spotting)
* [Recognize sounds from audio](/tutorials/end-to-end/sound-recognition)
* [Adding sight to your sensors](/tutorials/end-to-end/image-classification)
* [Object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Visual anomaly detection with FOMO-AD](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad)

Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

## Profiling your models

To profile your models for the Qualcomm Dragonwing RB3 Gen2 Development Kit:

* Make sure to select the Qualcomm Dragonwing RB3 Gen 2 Development Kit as your target device. You can change the target at the top of the page near your user's logo.
* Head to your [Learning block](/studio/projects/learning-blocks) page in Edge Impulse Studio.
* Click on the **Calculate performance** button.

To provide the on-device performance, we use [Qualcomm AI Hub](https://aihub.qualcomm.com/) in the background (see the image below) which run the compiled model on a physical device to gather metrics such as the mapping of model layers to compute units, inference latency, and peak memory usage. See more on Qualcomm® AI Hub [documentation](https://app.aihub.qualcomm.com/docs/) page.

<Frame caption="Qualcomm profiling using Qualcomm AI Hub">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/qc-profiling-qc-ai-hub.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=78a743f1dba051b9e476cd2c244ef54e" width="1510" height="1000" data-path=".assets/images/qualcomm/qc-profiling-qc-ai-hub.png" />
</Frame>

## Deploying back to device

### Using the Edge Impulse Linux CLI

To run your impulse locally on the RB3, open a terminal and run:

```bash  theme={"system"}
$ edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration, download the model to your RB3 Gen 2, and then start classifying (use `--clean` to switch projects).

Alternatively, you can select the **Linux (AARCH64 with Qualcomm QNN)** option in the **Deployment** page.

<Frame caption="Qualcomm deployment options">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/studio-qc-deployment-options-3.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=3975b7e607c98d35b8d08f5d677c72bc" width="1266" height="748" data-path=".assets/images/qualcomm/studio-qc-deployment-options-3.png" />
</Frame>

This will download an `.eim` model that you can run on your board with the following command:

```bash  theme={"system"}
edge-impulse-linux-runner --model-file downloaded-model.eim
```

### Using the Edge Impulse Linux Inferencing SDKs

Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the `.eim` model with your favourite programming language.

<Info>
  You can download either the quantized version and the float32 versions but Qualcomm NN accelerator only supports quantized models. If you select the float32 version, the model will run on CPU.
</Info>

### Using the IM SDK GStreamer option

When selecting this option, you will obtain a `.zip` folder. We provide instructions in the `README.md` file included in the compressed folder.

See more information on [Qualcomm IM SDK GStreamer pipeline](/hardware/deployments/run-qualcomm-im-sdk-gstreamer).

### Image model?

If you have an image model then you can get a peek of what your device sees by being on the same network as your device, and finding the 'Want to see a feed of the camera and live classification in your browser' message in the console. Open the URL in a browser and both the camera feed and the classification are shown:

<Frame caption="Live feed with classification results">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/demo1.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=f5d180c10366b2d54c7aec5f6c2187cc" width="400" height="440" data-path=".assets/images/demo1.png" />
</Frame>

## Troubleshooting

### Capture process failed with code 255

If you start the CLI, and see:

```
Failed to initialize linux tool Capture process failed with code 255
```

You'll need to restart the camera server via:

```bash  theme={"system"}
$ systemctl restart cam-server
```


Built with [Mintlify](https://mintlify.com).