# Source: https://docs.edgeimpulse.com/projects/expert-network/face-tracking-yolo-pro-rubik-pi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Object Following Pan-Tilt Camera System - Rubik Pi 3

Created By: Jallson Suryo

Public Project Links

* Face Detection: [https://studio.edgeimpulse.com/public/859925/live](https://studio.edgeimpulse.com/public/859925/live)
* Hand Gestures: [https://studio.edgeimpulse.com/public/766818/live](https://studio.edgeimpulse.com/public/766818/live)

Demo Videos

* Hand Gestures to Control LEDs: [https://youtu.be/fLNyrCrappE](https://youtu.be/fLNyrCrappE)
* Face Tracking to Control Pan-Tilt Camera: [https://youtu.be/jhEqjuGd8-A](https://youtu.be/jhEqjuGd8-A)

GitHub Repo: [https://github.com/Jallson/YOLO-based-Vision-Driven-Pan-Tilt-Camera-System-on-Rubik-Pi](https://github.com/Jallson/YOLO-based-Vision-Driven-Pan-Tilt-Camera-System-on-Rubik-Pi)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo01.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=b6ca656b92192d0c075ddd267c8aed77" width="1364" height="1063" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo01.png" />
</Frame>

## Introduction

This project is relatively simple, but very useful: it translates the location of an object or a person's face, into movements of two servos (pan–tilt) that control a camera. In essence, this creates a camera that can automatically follow its target. The system uses an object detection model trained with Edge Impulse, specifically YOLO-Pro to leverage transfer learning and pre-trained weights. This approach significantly reduces the amount of training data required while improving object recognition accuracy. The model is deployed as an embedded .eim model, run by our Python program. The entire system runs locally on a Thundercomm Rubik Pi 3, which has GPIO compatibility similar to a Raspberry Pi. This allows the use of the PCA9685 via I²C communication to control LED lights or servo motors. The Rubik Pi 3 has proven to be highly reliable, delivering real-time inference performance in our previous projects.

<Frame caption="Project Setup w/ LEDs">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo02.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=56e1b7ccc04751bdab6c0f9573376993" width="1683" height="994" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo02.png" />
</Frame>

In this implementation, we first control a row of 16 LEDs that illuminate from left to right following the horizontal movement of the detected object (hand gestures), while the brightness level corresponds to the objects vertical movement. Once this is successfully achieved, it is extended to control a pan–tilt camera platform driven by two servo motors, allowing the camera to dynamically follow detected objects in real-time. Horizontal object movement controls the pan axis, while vertical movement controls the tilt axis, resulting in intuitive tracking behavior.

## Hardware Components

* [Thundercomm Rubik Pi 3](https://rubikpi.ai)
* USB-C Power Adaptor (eg. 27W Raspberry Pi 5 Power adapter)
* Raspberry Pi 5 Active Cooler (optional)
* PC/laptop (for ssh and EDL mode firmware flash)
* USB-C/A to USB-C (for firmware flash)
* USB-C/A to micro-USB (for firmware flash)
* USB Camera/webcam (eg. Logitech C920/C922)
* LCD/monitor with HDMI cable + keyboard & mouse
* 2 DOF pan & tilt camera arm servo bracket
* 2 pcs servos (SG90 or MG995/996r)
* PCA9685 (I2C servo/LED driver)
* 16 pcs LEDs
* Breadboard + jumper cables
* 4x 1.5V battery, or 6V power supply

<Frame caption="Hardware">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo03.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=f38b022510ad29ad5fc754947cb90b28" width="985" height="1169" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo03.png" />
</Frame>

## Software & Online Services

* Edge Impulse Studio
* Edge Impulse Linux & Python SDK
* Ubuntu OS (24.04)
* OpenCV

## Steps

### 1. Preparation of Rubik Pi 3

When we receive the Rubik Pi 3, we will find it pre-installed with either Qualcomm Linux, or a minimal Ubuntu OS version. If yours comes with QC Linux, you need to switch to Ubuntu OS, because it lacks 'apt' and 'dpkg' package managers, and has limited OpenCV and GStreamer support without rebuilding the OS. (Qualcomm Linux is intended to be used for final products, not development purposes).

Prepare a USB-C and a micro USB cable, then follow this link — [https://softwarecenter.qualcomm.com/catalog/item/Qualcomm\_Launcher](https://softwarecenter.qualcomm.com/catalog/item/Qualcomm_Launcher) — to download Qualcomm Launcher (flashing utility). Next, follow the instructions here: [https://www.thundercomm.com/rubik-pi-3/en/docs/rubik-pi-3-user-manual/1.0.0-u/Update-Software/3.2.Flash-using-Qualcomm-Launcher](https://www.thundercomm.com/rubik-pi-3/en/docs/rubik-pi-3-user-manual/1.0.0-u/Update-Software/3.2.Flash-using-Qualcomm-Launcher) to flash the board with Ubuntu OS.

<Frame caption="Qualcomm Launcher">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/QC01.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=350c4fd6549aa4aea82b17ce081b6733" width="1190" height="1005" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/QC01.png" />
</Frame>

<br />

<Frame caption="Put in EDL mode">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/QC02.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=90e399bd3cd35baed4de130dbe051d17" width="1162" height="1065" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/QC02.png" />
</Frame>

<br />

<Frame caption="WIFI Config">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/QC03.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=1711c80b6a7bf8d1d93ee2386272fdd6" width="1149" height="743" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/QC03.png" />
</Frame>

<br />

<Frame caption="Setup Complete">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/QC04.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=1b11eb796fe4806de95154fffcfe8b38" width="1012" height="920" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/QC04.png" />
</Frame>

Once successfully flashed, connect to network, reboot, and login (ubuntu/ubuntu for user/password), open up the terminal or ssh to the device, then you can proceed to install the Edge Impulse CLI with the following commands:

```
sudo apt update
curl -sL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g —unsafe-perm
```

As a display is required for this project, we will install the Desktop version of Ubuntu. Given that Ubuntu OS is already installed on the Rubik Pi 3, the process is simple: just execute the following commands in the Terminal:

```
sudo apt install qcom-adreno1- libgbm-msm1- libegl-mesa0 libegl1 libgles2 libglvnd0 libvulkan1 weston-
sudo apt install ubuntu-desktop
sudo reboot
```

> Note: For the Python SDK and other dependencies, follow the instruction as described in Step 5.

### 2. Collecting Data (Images)

In this project, we're using Generative AI assistants like Gemini and ChatGPT to create a diverse set of facial photos. This allows us to get the variety we need — covering different expressions, ethnicities, haircuts, and backgrounds — while keeping privacy in mind. We'll save these images into a folder to use in just a moment. For those who are not familiar with Edge Impulse Studio, please follow these steps —> Open [studio.edgeimpulse.com](https://studio.edgeimpulse.com), login or create an account, then create a new project. Choose the **Images** project option, then **Object detection**. In Dashboard > Project Info, choose Bounding Boxes for the labeling method, and Rubik Pi 3 as the target device. Then in Data acquisition, click on the Upload Data tab. Choose your saved folder then upload the files.

<Frame caption="AI-generated face">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo04.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=16713043a0d002eb20b357b6fb52b487" width="530" height="539" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo04.png" />
</Frame>

<br />

<Frame caption="Upload Data">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo05.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=01c6c8c122932de92732d91fe32107de" width="1140" height="916" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo05.png" />
</Frame>

### 3. Labeling

The next step is labeling. Click on Data acquisition, click on the Labeling queue tab, then start by dragging a box around an object to label it. Click Save and repeat the process until all images are labeled. Alternatively, you can try out the AI auto labeling feature to help speed up the process.

After labeling, it's recommended to split the data into Training and Testing sets, around an 80/20 ratio. If you haven't done this yet, click on Train / Test Split to automatically split the data.

<Frame caption="AI labeling">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo06.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=acfe39980f0d923492410821a3cc7ce3" width="1635" height="1187" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo06.png" />
</Frame>

<br />

<Frame caption="Manual labeling">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo07.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=936010ccda6b89b4c8cc27ddb2e42a61" width="1022" height="1019" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo07.png" />
</Frame>

<br />

<Frame caption="Train/Test Split Data Ratio">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/photo08.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=3ee00fd4b0b2ee1daf758c42565f2f63" width="806" height="564" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo08.png" />
</Frame>

### 4. Train and Build

Once your labeled dataset is ready, go to Impulse Design > Create Impulse, and set the image width and height (eg. 320x320). Choose Fit shortest axis, then select Image and Object Detection as the Learning and Processing blocks, and click Save Impulse. Next, navigate to the Image Parameters section, select RGB as the color depth, and press Save parameters. After that, click on Generate, where you'll be able to see a graphical distribution of the features.

Now, move to the Object Detection section and configure the training settings. Select GPU and set the training cycles to around 100, learning rate to 0.001, and Medium for the model size. Choose YOLO-Pro as the NN architecture. Once done, start training by pressing Start, and monitor the progress.

If everything goes well and the precision result is more than 90%, proceed to the next step. Go to the Model Testing section, click Classify all, and if the result is around 90%, you can move on to the final step — Deployment.

<Frame caption="Learning blocks">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo09.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=9f4aec5645c3732ff353fb3b87b9f8bd" width="1130" height="474" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo09.png" />
</Frame>

<br />

<Frame caption="Save parameters">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo10.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=83eadd70d33cf6799aa86c15d3f9085d" width="992" height="768" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo10.png" />
</Frame>

<br />

<Frame caption="Generate features">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo11.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=d195d3ae5c6bde35b0d4352f14fd317d" width="989" height="597" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo11.png" />
</Frame>

<br />

<Frame caption="NN settings & results">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo12.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=894e2ec26f59e9444aee11e605310144" width="1288" height="968" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo12.png" />
</Frame>

<br />

<Frame caption="Model Test">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo13.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=f42d78984fb20dc09a6d406a426460b8" width="1045" height="793" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo13.png" />
</Frame>

### 5. Deploy & Test on Rubik Pi

With the model built in Edge Impulse Studio you can now test, download the model, and run everything directly from the Rubik Pi 3 (Ubuntu 24.04).

On the Rubik Pi, there are several things that need to be done.

Install a recent version of Python 3 (>= 3.7) if none is present. Ubuntu 24.04 comes with with Python 3.12 installed, so that should already be done for you. You can verify this by running this command: `python3 -version`

Ensure you have the latest Edge Impulse Linux CLI installed (as provided in Step 1). Then install the Linux Python SDK, OpenCV, ffmpeg, Gstreamer, numpy and other dependencies, by running these commands:

```
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-opencv ffmpeg \
  gstreamer1.0-tools gstreamer1.0-plugins-base \
  gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly gstreamer1.0-libav \
  libportaudio2
pip3 install numpy
pip3 install edge_impulse_linux
```

You can clone this repository to get the Linux Python SDK examples:

```
git clone https://github.com/edgeimpulse/linux-sdk-python
```

Then install dependencies:

```
pip install -r requirements.txt
```

Next, download and deploy/run the model via the Edge Impulse Linux runner. Plug in your USB camera, then open a terminal on the Rubik Pi (or ssh from your PC/laptop) then simply type `edge-impulse-linux-runner --clean` to select your project. Log in to your account then choose your project (Hand Gestures or Face Detection). Then choose your specific Impulse (if any) and select the Int8 quantized model. This process will download the .eim model file, which is specifically built for the Qualcomm Hexagon (QNN) architecture. During this process, the console will display the path where the model file .eim has been downloaded. For example, in the image below, it shows the file located at `/home/ubuntu/.ei-linux-runner/models/859925/v1-quantized-runner-linux-aarch64-qnn/model.eim`

Once this model.eim is downloaded, you can cancel the inference process by pressing Ctrl-C.

For convenience, copy the model file to the home directory for easier access: `cp -v model.eim /home/ubuntu`

<Frame caption="EI runner terminal">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo14.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=d6d9c38b77b3700f058268d9b33dcb75" width="767" height="413" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo14.png" />
</Frame>

Now the model is ready to run in a high-level language such as Python. To ensure the model works, we can re-launch the EI Runner with a USB camera connected to the Rubik Pi. You can view the camera's output in a browser at `http://your-Rubik-Pi-IP-address:4912`. Run this command: `edge-impulse-linux-runner` then navigate to the Rubik Pi's IP address, port 4912.

<Frame caption="Live inferencing">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/video01.gif?s=a4d9b9391366f5d0b4caa3f2ee73e82a" width="320" height="349" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/video01.gif" />
</Frame>

The inferencing time is around 1-3ms on the Rubik Pi 3, which is a super fast for object detection speed.

### 6. Build Your System: Rubik Pi + Servos and LEDs

In this project, we will develop two different output setups and their corresponding programs: one featuring a series of LEDs and another utilizing two servos to control a camera's pan and tilt movements. Begin by assembling the components according to Diagram 1 below. This specific setup is designed to trigger a row of LEDs based on the detected object's horizontal position (in this case, hand gestures). The brightness of the LEDs will be determined by the hand's vertical position. Once you have confirmed that the Rubik Pi, USB webcam, PCA9685, breadboard, LEDs, and power supply are all correctly connected, proceed with the 'smbus' library installation: `pip3 install smbus2` (add `sudo` if you run Python as root). Now, try to verify the PCA9685 I²C connection: `sudo i2cdetect -a -y -r 1`. Here is the expected result:

```
0 1 2 3 4 5 6 7 8 9 a b c d e f
00: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: 70 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
```

The detected address of your PCA9685 is 0x40 (0x70 is I²C multiplexer), and we will use this address later in our Python code.

<Frame caption="PCA9685 with LEDs setup">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/diagram01.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=763b40531aa7e72b6184405c0a0181e2" width="1476" height="1063" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/diagram01.png" />
</Frame>

This program uses bounding boxes detected by the YOLO-Pro model. It continuously updates and maps the x-coordinate to the sequence of LEDs that turn on, and the y-coordinate to the brightness value. Download it from the GitHub link below and then test out the program by running: `python3 gesture_control_led.py` (again add `sudo` if needed).

<Frame caption="Gestures controlled LEDs code">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo15.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=8091a6c7dd0d52b20334996fcf849e4f" width="758" height="867" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo15.png" />
</Frame>

If successful, we can then proceed by moving on to the second setup (diagram 2): Pan & Tilt Servos. This time, our Python program will generate servo angle movements that correspond to the movement of the object (face). As a result, the camera mounted on the servo arm bracket will follow our face.

Download from our Github then run: `python3 face_tracking_camera.py`

This completes our Vision-Driven Pan-Tilt Camera System project.

<Frame caption="PCA9685 with pan-tilt servos setup">
  <img src="https://mintcdn.com/edgeimpulse/dB37JgJFzK7jX7TS/.assets/images/face-tracking-yolo-pro-rubik-pi/diagram02.png?fit=max&auto=format&n=dB37JgJFzK7jX7TS&q=85&s=71987eb28b037d91152843c8d1fe0d98" width="1403" height="1019" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/diagram02.png" />
</Frame>

<br />

<Frame caption="Face Tracking Camera code">
  <img src="https://mintcdn.com/edgeimpulse/1qgOdrs5xeDyQh1l/.assets/images/face-tracking-yolo-pro-rubik-pi/photo16.png?fit=max&auto=format&n=1qgOdrs5xeDyQh1l&q=85&s=e80346d3678c7cac8e762f2b05ce1cb1" width="854" height="1109" data-path=".assets/images/face-tracking-yolo-pro-rubik-pi/photo16.png" />
</Frame>

Our Python code can be accessed from this link:

[https://github.com/Jallson/YOLO-based-Vision-Driven-Pan-Tilt-Camera-System-on-Rubik-Pi](https://github.com/Jallson/YOLO-based-Vision-Driven-Pan-Tilt-Camera-System-on-Rubik-Pi)

<iframe src="https://www.youtube.com/embed/fLNyrCrappE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<br />

<iframe src="https://www.youtube.com/embed/jhEqjuGd8-A" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

This project successfully demonstrates a complete edge AI vision system that connects real-time object detection to physical actuation. By deploying an Edge Impulse YOLO-Pro model on the Rubik Pi 3, the system is able to track targets such as faces and hand gestures with reliable accuracy and low latency. The integration of the PCA9685 PWM controller proved to be fully compatible with the Rubik Pi 3, enabling flexible control of multiple actuators through I²C communication. The project validated the end-to-end pipeline from camera input, AI inference, spatial mapping, and actuator control in a single embedded system.

A key strength of this design is its output flexibility. The same detection results can be mapped to different actuators, such as LEDs for visualization and debugging, or pan–tilt servos for mechanical tracking, without changing the core perception logic. This modular approach allows the system to be easily adapted for different applications. This project highlights the practical integration of Edge AI with robotics and serves as a foundation for more advanced applications such as autonomous tracking, human–machine interaction, and intelligent surveillance systems.


Built with [Mintlify](https://mintlify.com).