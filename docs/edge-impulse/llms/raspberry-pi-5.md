# Source: https://docs.edgeimpulse.com/hardware/boards/raspberry-pi-5.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Raspberry Pi 5

The Raspberry Pi 5 with 2–3× the speed of the previous generation, and featuring silicon designed in‑house for the best possible performance, we’ve redefined the Raspberry Pi experience. The Pi5 is a versatile Linux development board with a quad-core processor running at 2.4GHz a GPIO header to connect sensors, and the ability to easily add an external microphone or camera - and it's fully supported by Edge Impulse. You'll be able to sample raw data, build models, and deploy trained machine learning models directly from the Studio.

In addition to the Raspberry Pi 5 we recommend that you also add a camera and / or a microphone. Most popular USB webcams and the [Camera Module](https://www.raspberrypi.org/products/camera-module-v2/) work fine on the development board out of the box.

<Frame caption="Raspberry Pi 5">
  <img src="https://mintcdn.com/edgeimpulse/AQr6kHeg-keHHzV6/.assets/images/pi5_top.png?fit=max&auto=format&n=AQr6kHeg-keHHzV6&q=85&s=a97c79c5ddf4167871729124e7c57551" width="1037" height="676" data-path=".assets/images/pi5_top.png" />
</Frame>

### Prerequisites

In this documentation, we will detail the steps to set up your Raspberry Pi 5 with the new Bookworm release OS for Edge Impulse. This guide includes headless setup instructions and how to connect to Edge Impulse, along with troubleshooting tips.
For more detailed Raspberry Pi setup instructions please see their official documentation: [Getting started with Raspberry Pi](https://www.raspberrypi.org/documentation/computers/getting-started.html).

<Tabs>
  <Tab title="Headless Setup">
    You can set up your Raspberry Pi without a screen. To do so:

    1. Flash the [Raspberry Pi OS](https://www.raspberrypi.org/software/) image to an SD card using the latest Raspberry Pi Imager.

       <Warning>
         **You must use 64-bit OS as 32-bit OS is no longer supported**
         Raspberry Pi 5 uses [aarch64](https://en.wikipedia.org/wiki/AArch64), which is a 64-bit CPU. If you are installing Raspberry Pi OS for the RPi 5, make sure you use the **64-bit version**. Raspberry Pi 5 cannot run armv7 images
       </Warning>

    2. During the flashing process, access the Customisation options menu in the Raspberry Pi Imager to preconfigure the following options:
       * Set your hostname to something memorable (e.g., `raspberrypi`).
       * Choose a username and password (as of Bookworm, the default `pi`/`raspberry` is no longer available).
       * Configure your WiFi settings for network architecture (SSID, password).
         <Warning>`wpa_supplicant.conf` cannot be used from Bookworm onward to set up WiFi and networking. You must use the Pi Imager or the advanced menu`raspi-config` tool to set up WiFi.</Warning>
       * Configure Remote Access by enabling SSH, set the SSH to use password authentication.
         <Note> You can also create an empty file called `ssh` in the boot drive to enable SSH if you have not set up SSH through the Raspberry Pi Imager options. </Note>

    3. Insert the SD card into your Raspberry Pi 5, and let the device boot up.

    4. Find the IP address of your Raspberry Pi. You can either do this through the DHCP logs in your router or by scanning your network.

       You can scan your network on macOS and Linux via:

       ```bash  theme={"system"}
       arp -na | grep -i dc:a6:32
       ```

       which should return something like:

       ```
       ? (192.168.1.19) at dc:a6:32:f5:b6:7e on en0 ifscope [ethernet]
       ```

       Here `192.168.1.19` is your IP address.

    5. Connect to the Raspberry Pi over SSH. Open a terminal window on MacOS or Linux and run (replace `username` with your chosen username). If you're using Windows, you can use [PuTTY](https://www.putty.org/) or the Windows Subsystem for Linux (WSL) to access SSH:

       ```bash  theme={"system"}
       ssh <username>@192.168.1.19
       ```

       You can also try using `<username>@<hostname>` instead of the IP address if your system supports mDNS.
       If you are prompted with a security warning about the authenticity of the host, type `yes` and press Enter then enter your chosen password.

    6. You can now run commands directly on your Raspberry Pi through the terminal. Please continue to the next section to install Edge Impulse dependencies.
  </Tab>

  <Tab title="Setup with a screen">
    If you have a screen and a keyboard/mouse attached to your Raspberry Pi:

    1. Flash the [Raspberry Pi OS](https://www.raspberrypi.org/software/) image to an SD card. During the flashing process, access the Customisation options menu in the Raspberry Pi Imager to preconfigure the following options:
       * Set your hostname to something memorable (e.g., `raspberrypi`).
       * Choose a username and password (as of Bookworm, the default `pi`/`raspberry` is no longer available).
       * Configure your WiFi settings for network architecture (SSID, password).
         <Warning>`wpa_supplicant.conf` cannot be used from Bookworm onward to set up WiFi and networking. You must use the Pi Imager or the advanced menu`raspi-config` tool to set up WiFi.</Warning>
    2. Insert the SD card into your Raspberry Pi 5, and let the device boot up.
    3. Connect to your WiFi network if not already set up during the flashing process.
    4. Click the 'Terminal' icon in the top bar of the Raspberry Pi.
    5. You can now run commands directly on your Raspberry Pi through the terminal. Please continue to the next section to install Edge Impulse dependencies.
  </Tab>
</Tabs>

### Installing dependencies

To set this device up in Edge Impulse, run the following commands:

```bash  theme={"system"}
sudo apt update
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
```

Then to update npm packages:

```bash  theme={"system"}
sudo npm install -g npm@10.8.1
```

For CSI cameras (like the Raspberry Pi Camera Module), you also need to install the `gstreamer1.0-libcamera` package:

```bash  theme={"system"}
sudo apt install gstreamer1.0-libcamera
```

If you have a Raspberry Pi Camera Module, you also need to activate it first. Run the following commands:

```bash  theme={"system"}
sudo raspi-config
```

Use the cursor keys to select and open Interfacing Options, then select Camera, and follow the prompt to enable the camera. Reboot the Raspberry Pi.

#### Install with Docker

If you want to install Edge Impulse on your Raspberry Pi using Docker, run the following commands:

```bash  theme={"system"}
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo docker run -it --rm --privileged --network=host -v /dev/:/dev/ --env UDEV=1 --device /dev:/dev --entrypoint /bin/bash ubuntu:20.04
```

Once in the Docker container, run:

```bash  theme={"system"}
apt-get update

apt-get install wget -y
wget https://deb.nodesource.com/setup_20.x
bash setup_20.x
apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps vim v4l-utils usbutils udev
apt-get install npm -y
```

### Connecting to Edge Impulse

With all software set up, connect your camera or microphone to your Raspberry Pi (see 'Next steps' further on this page if you want to connect a different sensor).

To connect your Raspberry Pi 5 to Edge Impulse, run the following command:

```bash  theme={"system"}
edge-impulse-linux
```

This command connects your Raspberry Pi 5 to Edge Impulse Studio. It will prompt you to log in and select a project. Once authenticated, your Raspberry Pi 5 will appear in the Edge Impulse Studio under Devices. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/089cc72-screenshot_2021-02-23_at_114202.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=99d98296ca59ffa50e898cfab79105a6" width="1225" height="291" data-path=".assets/images/089cc72-screenshot_2021-02-23_at_114202.png" />
</Frame>

You can now sample raw data, build models, and deploy trained machine learning models directly from the Studio. Please let us know if you have any questions or need further assistance: [forum.edgeimpulse.com](https://forum.edgeimpulse.com).

If you want to switch projects run the command with `--clean`.

### Troubleshooting

#### Wrong OS bits

If you see the following error when trying to deploy a .eim model to your Raspberry Pi:

```
Failed to run impulse Error: Unsupported architecture “aarch64”
```

It likely means you are attempting to deploy a .eim Edge Impulse model file to a 32-bit operating system running on a 64-bit CPU. To check your hardware architecture and OS in Linux, please run the following commands:

```bash  theme={"system"}
uname -m
uname -a
getconf LONG_BIT
```

If you see something like this as the output:

```
uname -m
aarch64
uname -a
Linux raspberrypi 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:20 BST 2023 aarch64 GNU/Linux
getconf LONG_BIT
32
```

It means that you are running a 32-bit OS on a 64-bit CPU. To run .eim models on *aarch64* CPUs, you *must* use a 64-bit operating system. Please download and install the 64-bit version of Raspberry Pi OS if you see `aarch64` when you run `uname -m`.

#### CSI Camera Issues

When using RPi OS Bookworm and RPi camera module you need to install gstreamer1.0-libcamera package first. However once gstreamer1.0-libcamera is installed it hides v4l2deviceproviders, as a result it hides webcam.

To resolve this issue, you need to install the gstreamer1.0-libcamera package and use the latest edge-impulse-linux >=v1.9.2 to fix this issue.


Built with [Mintlify](https://mintlify.com).