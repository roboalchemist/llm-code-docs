# Source: https://docs.edgeimpulse.com/hardware/porting/linux-inference/linux-inference-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inferencing with Edge Impulse Linux CLI

Edge Impulse provides a set of command line interface (CLI) tools that make running models on Linux targets easier than building with Python or C++. Using the CLI tools lets you run model inference without writing any code by simply by running an executable in the command line or a script. It is the most straightforward way to deploy and run an impulse on a Linux machine. You can find detailed information about the CLI on its [GitHub repository](https://github.com/edgeimpulse/edge-impulse-linux-cli) and [documentation page](/tools/clis/edge-impulse-linux-cli).

<Frame caption="Edge Impulse Linux CLI Process">
  <img src="https://mintcdn.com/edgeimpulse/F0XbRxP1bJiYpXHo/.assets/images/porting/cli-process.png?fit=max&auto=format&n=F0XbRxP1bJiYpXHo&q=85&s=74f735d8f91076b024e9a7615a745404" width="266" height="440" data-path=".assets/images/porting/cli-process.png" />
</Frame>

## 0. Prerequisites

* The CLI assumes that cameras and microphones are discoverable in the /dev/ directory
* The device should have internet connectivity to download the model via edge-impulse-linux. Internet connection at inference time is not required.
* Access to the target from the host via SSH to copy a model file in case it's downloaded through a host computer.

## 1. Install dependencies and Edge Impulse Linux CLI on target

<Accordion title="Debian Based Systems">
  ###

  These commands install the Edge Impulse Linux CLI for your Debian based distribution (except Qualcomm and NVIDIA devices, see below):

  ```bash  theme={"system"}
  # Download and install nvm
  $ sudo apt install -y curl
  $ curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -

  # Verify the Node.js version
  $ node -v

  # Verify npm version
  $ npm -v

  # Install the CLI base requirements
  $ sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps

  # Install the CLI
  $ sudo npm install edge-impulse-linux -g --unsafe-perm
  ```

  <Warning>
    **Important:** Edge Impulse requires Node.js version 20.x or later. Using older versions may lead to installation issues or runtime errors. Please ensure you have the correct version installed before proceeding with the setup.
  </Warning>

  Once successfully installed please proceed to the “[Download model and run inference with edge-impulse-linux-runner](#2-download-model-and-run-inference-with-edge-impulse-linux-runner)" section.
</Accordion>

<Accordion title="Qualcomm Devices only">
  ###

  To install the CLI components for Qualcomm devices running Qualcomm Linux or Ubuntu:

  ```bash  theme={"system"}
  $ wget https://cdn.edgeimpulse.com/firmware/linux/setup-edge-impulse-qc-linux.sh
  $ sh setup-edge-impulse-qc-linux.sh
  ```

  Once successfully installed please proceed to the “[Download model and run inference with edge-impulse-linux-runner](#2-download-model-and-run-inference-with-edge-impulse-linux-runner)" section.
</Accordion>

<Accordion title="NVIDIA Devices only">
  ###

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
</Accordion>

<Accordion title="Systems without Package Manager">
  ###

  Before you install the CLI you will need to install node first, then the other CLI requirements like sox and gstreamer, and finally the CLI. It is recommended that you set up your buildroot or yocto processes with the base requirements listed previously (gstreamer, sox, etc). You may find examples root buildroot and yocto from the Microchip guides. Once successfully installed please proceed to the “Test Inference Example” section
</Accordion>

## 2. Download model and run inference with edge-impulse-linux-runner

There are two ways to download the model to the device.

<Accordion title="Directly on the target, using edge-impulse-linux-runner (requires authentication to edge impulse on target)">
  ###

  Running the command below on the target will prompt you to log in to your edge impulse account, select the project, download the model and start inference in one go.
  Here you can select the project that you copied [in the beginning of this guide](./linux-inference-process). When the runner is working correctly you should get output on the terminal like shown below. A webserver will be started on port 1337 to which you can upload this [test-image.jpg](/hardware/porting/test-image.jpg) to test an inference.

  ```bash  theme={"system"}
  $ edge-impulse-linux-runner --clean --mode http-server
  Edge Impulse Linux runner v1.18.2
  ? What is your user name or e-mail address (edgeimpulse.com)? <username>
  ? What is your password? [hidden]
  ? Enter a code from your authenticator app [hidden]

  ? From which project do you want to load the model? (🔍 type to search) 820244
  ? Which impulse do you want to run? (🔍 type to search) 36
  ? What model variant do you want to run? Quantized (int8)
  [RUN] Downloading model...

  ...

  [RUN] Starting HTTP server for ei-ready-device-testing / cars-in-parking-garage (v27) on port 1337
  [RUN] Parameters image size 320x320 px (3 channels) classes [ 'vehicle' ]
  [RUN] Thresholds: 194.min_score=0.5 (override via --thresholds <value>)
  [RUN]
  [RUN] HTTP Server now running at http://localhost:1337

  ```

  The runner will start a preview http server locally where you can view your live inference results. The IP address of the server is printed in the terminal when the impulse starts. Typically the address is [http://localhost:1337](http://localhost:1337). Upload this [test-image.jpg](/hardware/porting/test-image.jpg) to test an inference.

  <Frame caption="Live inference preview">
    <img src="https://mintcdn.com/edgeimpulse/F0XbRxP1bJiYpXHo/.assets/images/porting/http-server.png?fit=max&auto=format&n=F0XbRxP1bJiYpXHo&q=85&s=7db3b4bc22eae9035d48ce8a72d34a09" width="1833" height="956" data-path=".assets/images/porting/http-server.png" />
  </Frame>
</Accordion>

<Accordion title="Pre-load the model externally and copy on the target (no internet and authentication required on the target)">
  ###

  In this method the same CLI tool is used on the target, but it will not require internet connection or authentication.

  First, on the host computer go to the deployment page of the project in Edge Impulse platform and select Linux option appropriate for your architecture. You will notice that a lot of different flavours ara available, so if your target falls into one of them (e.g., its a Qualcomm SoC with Hexagon NPU) - select that one.

  If its a general core without accelerators - select AARCH64 or other one that matches your architecture.

  <Frame caption="Linux Deployment Options">
    <img src="https://mintcdn.com/edgeimpulse/F0XbRxP1bJiYpXHo/.assets/images/porting/linux-deployment-options.png?fit=max&auto=format&n=F0XbRxP1bJiYpXHo&q=85&s=d50f64178692a11250cf7fa001663575" width="891" height="587" data-path=".assets/images/porting/linux-deployment-options.png" />
  </Frame>

  Click “Deploy”. You will receive a .zip archive with a .eim executable file.
  Copy this file over to your target linux device (e.g. to \~/models/my\_model.eim)

  After this run the following command - and the inference will start in the same way as in the previous method if everything is correct:

  ```bash  theme={"system"}
  edge-impulse-linux-runner --model-file ~/models/my_model.eim --mode http-server

  ...

  [RUN] Starting HTTP server for ei-ready-device-testing / cars-in-parking-garage (v27) on port 1337
  [RUN] Parameters image size 320x320 px (3 channels) classes [ 'vehicle' ]
  [RUN] Thresholds: 194.min_score=0.5 (override via --thresholds <value>)
  [RUN]
  [RUN] HTTP Server now running at http://localhost:1337
  ```

  The runner will start a preview http server locally where you can view your live inference results. The IP address of the server is printed in the terminal when the impulse starts. Typically the address is [http://localhost:1337](http://localhost:1337). Upload this [test-image.jpg](/hardware/porting/test-image.jpg) to test an inference.

  <Frame caption="Live inference preview">
    <img src="https://mintcdn.com/edgeimpulse/F0XbRxP1bJiYpXHo/.assets/images/porting/http-server.png?fit=max&auto=format&n=F0XbRxP1bJiYpXHo&q=85&s=7db3b4bc22eae9035d48ce8a72d34a09" width="1833" height="956" data-path=".assets/images/porting/http-server.png" />
  </Frame>
</Accordion>


Built with [Mintlify](https://mintlify.com).