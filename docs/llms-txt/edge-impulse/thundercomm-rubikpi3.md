# Source: https://docs.edgeimpulse.com/hardware/boards/thundercomm-rubikpi3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Thundercomm Rubik Pi 3

The [Thundercomm Rubik Pi 3](https://rubikpi.ai) is a powerful Linux-based development board based on the Qualcomm Dragonwing QCS6490 SoC. It has a Kryo™ 670 CPU, Adreno™ 643L GPU and 12 TOPS Hexagon™ 770 NPU. It also has onboard WiFi and Bluetooth, as well as common ports such as CSI camera inputs, USB3, a 4k HDMI video output, ethernet, and GPIO pins for interacting with external hardware.  It also has 128gb of onboard storage for the Operating System and applications.  The Rubik Pi 3 ships with either Qualcomm Linux or Ubuntu 24.04 pre-installed, and Edge Impulse supports both platforms.

<Frame caption="Thundercomm Rubik Pi 3">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/thundercomm-rubikpi3.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=795292fb93898512d7396d9ee57426d3" width="1000" height="564" data-path=".assets/images/qualcomm/thundercomm-rubikpi3.png" />
</Frame>

<iframe src="https://www.youtube.com/embed/E0kwTcZiTdk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Setting Up Your Thundercomm Rubik Pi 3 - Ubuntu 24.04

### 1. Setup and connecting to the internet

1. Attach a USB keyboard and mouse, as well as an HDMI monitor.  For computer vision projects, also attach a USB camera.

2. Connect power to the USB-C port on the right hand side of the board.

3. Press the power button, which is the front button (nearer the ports):

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rubikpi-ports.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=2c37d2fc4b11087eff698e47091ff1b2" alt="" width="375" data-path=".assets/images/qualcomm/rubikpi-ports.png" />
   </Frame>

4. Once the board has booted up, you are brought to the console login.  Login with the username `ubuntu` and the password `ubuntu`.  (You might be required to change the password if this is the first boot.

5. Run the command `sudo nmtui`, and and navigate through the menu to add your WiFi.  Alternatively, you can simply plug in an ethernet cable if available.

<Info>
  After connecting the board to the internet, reboot it. This will refresh the system clock (through the NTP), resolving an issue with invalid certificates when installing the Edge Impulse CLI.
</Info>

### 2. Installing the Edge Impulse Linux CLI

Once rebooted, open up the terminal once again, and install the Edge Impulse CLI and other dependencies via:

```bash  theme={"system"}
sudo apt update
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
```

### 3. Connecting to Edge Impulse

With all dependencies set up, run:

```bash  theme={"system"}
$ edge-impulse-linux
```

This will start a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects, or use a different camera (e.g. a USB camera) run the command with the `--clean` argument.

### 4. Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Rubik Pi 3 connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rubikpi-connected.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=fd9db88d3661780acb0746219218233d" width="1516" height="1000" data-path=".assets/images/qualcomm/rubikpi-connected.png" />
</Frame>

## Setting Up Your Thundercomm Rubik Pi 3 - Qualcomm Linux

### 1. Setup and connecting to the internet

1. Attach a USB keyboard and mouse, as well as an HDMI monitor.  For computer vision projects, also attach a USB camera.

2. Connect power to the USB-C port on the right hand side of the board.

3. Press the power button, which is the front button (nearer the ports):

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rubikpi-ports.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=2c37d2fc4b11087eff698e47091ff1b2" alt="" width="375" data-path=".assets/images/qualcomm/rubikpi-ports.png" />
   </Frame>

4. Once the board has booted up, open a terminal by clicking on the icon at the top-left of the screen.

5. Change to the 'root' user with `su root`

6. Run the command `rubikpi_config`, and navigate through the menu to add your WiFi.  Alternatively, you can simply plug in an ethernet cable if available.

<Info>
  After connecting the board to the internet, reboot it. This will refresh the system clock (through the NTP), resolving an issue with invalid certificates when installing the Edge Impulse CLI.
</Info>

### 2. Installing the Edge Impulse Linux CLI

Once rebooted, open up the terminal once again, and install the Edge Impulse CLI and other dependencies via:

```bash  theme={"system"}
$ wget https://cdn.edgeimpulse.com/firmware/linux/setup-edge-impulse-qc-linux.sh
$ sh setup-edge-impulse-qc-linux.sh
```

<Info>
  Make note of the additional commands shown at the end of the installation process; the `source ~/.profile` command will be needed prior to running Edge Impulse in subsequent sessions.
</Info>

### 3. Connecting to Edge Impulse

With all dependencies set up, run:

```bash  theme={"system"}
$ edge-impulse-linux
```

This will start a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects, or use a different camera (e.g. a USB camera) run the command with the `--clean` argument.

### 4. Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Rubik Pi 3 connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/rubikpi-connected.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=fd9db88d3661780acb0746219218233d" width="1516" height="1000" data-path=".assets/images/qualcomm/rubikpi-connected.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Responding to your voice](/tutorials/end-to-end/keyword-spotting)
* [Recognize sounds from audio](/tutorials/end-to-end/sound-recognition)
* [Adding sight to your sensors](/tutorials/end-to-end/image-classification)
* [Object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Visual anomaly detection with FOMO-AD](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad)

Looking to connect different sensors? Our [Linux SDK](/tools/libraries/sdks/inference/linux) lets you easily send data from any sensor and any programming language (with examples in Node.js, Python, Go and C++) into Edge Impulse.

## Deploying back to device

### Using the Edge Impulse Linux CLI

To run your Impulse locally on the Rubik Pi 3, open a terminal and run:

```bash  theme={"system"}
$ edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration, download the model to your Rubik Pi 3, and then start classifying (use `--clean` to switch projects).

Alternatively, you can select the **Linux (AARCH64 with Qualcomm QNN)** option in the **Deployment** page.

<Frame caption="Qualcomm deployment options">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/qualcomm/studio-qc-deployment-options-3.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=3975b7e607c98d35b8d08f5d677c72bc" width="1266" height="748" data-path=".assets/images/qualcomm/studio-qc-deployment-options-3.png" />
</Frame>

This will download an `.eim` model that you can run on your board with the following command:

```bash  theme={"system"}
edge-impulse-linux-runner --model-file downloaded-model.eim
```

### Using the Edge Impulse Linux Inferencing SDKs

Our [Linux SDK](/tools/libraries/sdks/inference/linux) has examples on how to integrate the `.eim` model with your favorite programming language.

<Info>
  You can download either the quantized version and the float32 versions of your model, but the Qualcomm NN accelerator only supports quantized models. If you select the float32 version, the model will run on CPU.
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