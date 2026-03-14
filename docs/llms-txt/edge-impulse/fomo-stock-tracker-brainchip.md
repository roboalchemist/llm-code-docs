# Source: https://docs.edgeimpulse.com/projects/expert-network/fomo-stock-tracker-brainchip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inventory Stock Tracker - FOMO - BrainChip Akida

Created By: Christopher Mendez

Public Project Link: [https://studio.edgeimpulse.com/public/425288/live](https://studio.edgeimpulse.com/public/425288/live)

## Introduction

Industries, stores, workshops and many other professional environments have to manage an inventory. Whether of products or tools, this need is normally addressed with a limited digital or manual solution. This project aims to contribute to the cited need with a smart approach that will let you know the products/tools quantity and their exact location in the rack, box or drawer.

<Frame caption="Project overview">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/thumbnail.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=05d43651aac8c3a3c2e19278ffadc667" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/thumbnail.png" />
</Frame>

The system will be constantly tracking the terminal blocks on a tray, counting them and streaming a live view in a web server. In addition, you will have real-time location feedback on an LED matrix.

## Hardware and Software Requirements

To develop this project we will use the following hardware:

* [Akida™ PCIe Board](https://shop.brainchipinc.com/products/akida%E2%84%A2-development-kit-pcie-board)
* [PCIe Slot For Raspberry Pi 5 Extension Adapter Board](https://52pi.com/products/p02-pcie-slot-for-rpi5)
* [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)
* [Camera Module 3 - IMX708](https://www.raspberrypi.com/products/camera-module-3/)
* [RGB LED Matrix](https://wiki.seeedstudio.com/Grove-RGB_LED_Matrix_w-Driver/)
* [Grove Base Hat for Raspberry Pi (Optional)](https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html)
* [Custom 3D parts](https://github.com/mcmchris/brainchip-inventory-check/tree/main/3D_files)

<Frame caption="Hardware required for the project">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/materials.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=b01a0a4b89cc1adc857176b528b59c82" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/materials.png" />
</Frame>

### Akida™ PCIe Board

It should be noted that the **AKD1000 Neuromorphic Hardware Accelerator** is the main component of this project thanks to some interesting characteristics that make it ideal for this use case.

Considering that our project will end up being deployed in industrial and commercial environments, it's crucial that it can do its job efficiently and with very low energy consumption. This is where BrainChip's technology makes sense. Akida™ neuromorphic processor mimics the human brain to analyze only essential sensor inputs at the point of acquisition - processing data with unparalleled performance, precision, and economy of energy.

### Software

To develop the project model we are going to use:

* [Edge Impulse Studio](https://studio.edgeimpulse.com/)

## Hardware Setup

To fully assemble the project:

* Stack the PCIe Slot Extension Adapter Board under the Raspberry Pi and connect the flat cable accordingly ([dedicated instructions](https://wiki.52pi.com/index.php?title=EP-0219)).
* Screw the 3D-printed arm to the Raspberry Pi using the available spacers thread.
* Screw the MIPI camera to the 3D-printed arm and connect the flat cable from the camera to the CAM0 slot on the Raspberry Pi.
* Stack the Grove Base Hat on the Raspberry Pi 40 pins header.
* Connect the Grove cable from the LED Matrix to an I2C connector on the Grove Base Hat.
* Screw the cooling fan holder in the PCIe Slot Extension Adapter Board and connect it to +5V and GND on the 40 pins header (Optional).

<Frame caption="Hardware Setup Final Result">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/hardware.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=575aafa239f7dc5ef688e6ac3a001cbf" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/hardware.png" />
</Frame>

## Raspberry Pi 5 Setup

With the Raspberry Pi Imager, flash a micro-SD card with the Raspberry Pi OS Lite (64-bit), enter the OS Customisation menu by typing `Ctrl + Shift + X` and add your login credentials, enable the wireless LAN by adding your WiFi credentials and verify that the **SSH** connection is enabled in the **Services** settings.

<Frame caption="Raspberry Pi image settings">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/pi5-image.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=71423faef7c3c9531cdcd38ee1fd9412" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/pi5-image.png" />
</Frame>

Once the micro-SD card is flashed and verified, eject it and install it in your Raspberry Pi 5.

## Setting up the Development Environment

Once the system is powered up and connected to the internet (I used WiFi), you can access it by an SSH connection: you will need to know the device's local IP address, in my case, I got it from the list of connected devices of my router.

<Frame caption="Device IP Address">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/raspberry-ip.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=e609186f006acaca7d685ed2de740846" width="1600" height="293" data-path=".assets/images/fomo-stock-tracker-brainchip/raspberry-ip.png" />
</Frame>

To start setting up the device for a custom model deployment, let's verify we have installed all the packages we need.

I am using Putty for the SSH connection. Log in using the set credentials, in this case, the username is **raspberrypi** and the password is **raspberrypi**.

<Frame caption="SSH Connection through Putty">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/putty.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=d8c8c669cf5d8dbc3d1ea47304dcdd4b" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/putty.png" />
</Frame>

Once in, verify that the Akida PCIe board is detected:

```bash  theme={"system"}
lspci | grep Co-processor # will check if the PCIe card is plugged in correctly.
```

Create a **virtual environment**:

```bash  theme={"system"}
python3 -m venv .venv --system-site-packages #create virtual env
source .venv/bin/activate  #enter virtual env
```

Install the Akida driver:

```bash  theme={"system"}
apt-get install -y git # install git to be able to clone the driver repository
git clone https://github.com/Brainchip-Inc/akida_dw_edma # clone the repository
sudo apt install build-essential linux-headers-$(uname -r) # install system dependencies
cd akida_dw_edma # enter the repository
sudo ./install.sh # run the driver installation script
apt-get install python3-pip -y # install the pip tool
```

With the driver modules already mounted and the tools ready, install the Akida driver:

```bash  theme={"system"}
python3 -m pip install akida
```

Once installed, verify it is installed correctly and if it detects the mounted AKD1000 PCIe card.

```bash  theme={"system"}
pip show akida # prints out the driver version
akida devices # search for compatible Akida devices
```

<Frame caption="Akida driver verification">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/akida-driver.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=05e511bcb295eb84ca2c699b75f1121c" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/akida-driver.png" />
</Frame>

Install some specific project dependencies:

```bash  theme={"system"}
python3 -m pip install scipy
python3 -m pip install --upgrade pip setuptools wheel
pip install h5py --only-binary h5py
python3 -m pip install tensorflow
python3 -m pip install matplotlib
python3 -m pip install imageio
python3 -m pip install IPython
python3 -m pip install opencv-python
python3 -m pip install Flask
```

> **You can clone the public Edge Impulse project if you'd like, from [this link](https://studio.edgeimpulse.com/public/425288/live).**

## Data Collection

First, we need to create an [Edge Impulse Studio](https://studio.edgeimpulse.com) account if we haven't yet, and create a new project:

<Frame caption="New project creation">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/new-project.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=9f9f4a664efaf78b8af660c4932788a3" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/new-project.png" />
</Frame>

For the creation of the dataset of our model, we have several options, uploading the images from the Raspberry Pi with a USB camera or using our computer or phone. In this case, I chose to take them from the phone using its camera.

<Frame caption="Dataset creating source">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/pc_upload.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=1906d29d8406bc88abd9ede0820b8ed7" width="1038" height="510" data-path=".assets/images/fomo-stock-tracker-brainchip/pc_upload.png" />
</Frame>

The dataset consists of 1 class in which we capture the "piece", a terminal block in this case, from several angles and perspectives. Use the **Labeling queue** to easily label all the pieces in one frame.

<Frame caption="Raw image and labeled image">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/dataset-creation.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=580d90183de69f771bed6e0ae484d4e7" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/dataset-creation.png" />
</Frame>

> **Taking at least +95 pictures of the piece class will let you create a robust enough model**

## Impulse Design

After having the dataset ready, it is time to define the structure of the model.

In the left side menu, we navigate to **Impulse design** > **Create impulse** and define the following settings for each block, respectively:

### Input block (Image data):

* Image width: 224
* Image height: 224
* Resize mode: Fit shortest axis

### Processing block (Image):

Add an **Image** processing block since this project will work with images as inputs.

### Learning block (BrainChip Akida)

We are going to use an **Object Detection** learning block developed for Brainchip Akida hardware.

Finally, we save the **Impulse design**, it should end up looking like this:

<Frame caption="Final impulse design">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/impulse-design.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=40ff52d05e83369b5be3163869d09f78" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/impulse-design.png" />
</Frame>

## Model Training

After having designed the impulse, it's time to set the processing and learning blocks.

In the **Image** processing block, we set the "Color depth" parameter to **RGB**, click on **Save parameters** and then **Generate features**.

In the **Object Detection** learning block, define the following settings:

* Number of training cycles: 60
* Learning rate: 0.0005

In the Neural network architecture, select the **Akida FOMO AkidaNet(alpha=0.5 @224x224x3)**.

Click on the **Start training** button and wait for the model to be trained and the confusion matrix to show up.

### Confusion Matrix

<Frame caption="Confusion matrix results">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/confusion.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=0adf5eb44c2a1adc05adfad46309f726" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/confusion.png" />
</Frame>

The results of the confusion matrix can be improved by adding more samples to the dataset. After some trial and error testing different models I was able to get one stable and robust enough for the application.

## Project Setup

To be able to run the project, we need to go back to our SSH connection with the device and clone the project from the [Github repository](https://github.com/mcmchris/brainchip-inventory-check.git), for this, use the following command:

```bash  theme={"system"}
git clone https://github.com/mcmchris/brainchip-inventory-check.git
```

Enter the repository directory:

```bash  theme={"system"}
cd brainchip-inventory-check
```

We are going through the content in detail later.

> **It is recommended that you install Edge Impulse for Linux following this [link](/hardware/boards/raspberry-pi-5#installing-dependencies) or the steps below:**

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

```bash  theme={"system"}
edge-impulse-linux --version
```

It should show you the installed version (1.8.0 at writing time)

To activate the MIPI camera support run the following command:

```bash  theme={"system"}
sudo raspi-config
```

Use the cursor keys to select and open Interfacing Options, then select Camera, and follow the prompt to enable the camera. Reboot the Raspberry Pi.

## Deployment

> **If you want to test the model as it is without any modification, jump to the [Run Inferencing](/projects/expert-network//fomo-stock-tracker-brainchip#run-inferencing) section.**

Once the project is cloned locally on the Raspberry Pi, you can download the project model from Edge Impulse Studio by navigating to the **Dashboard** section and downloading the **MetaTF** `.fbz` file.

<Frame caption="Downloading the project model">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/model-download.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=65282fd73d7659c3308514506a245c6c" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/model-download.png" />
</Frame>

Once downloaded, from the model download directory, open a new terminal and copy the model to the Raspberry Pi using `scp` command as follows:

```bash  theme={"system"}
scp <model file>.fbz raspberrypi@<Device IP>:~ # command format
scp akida_model_2.fbz raspberrypi@10.0.0.207:~ # actual command in my case
```

> *You will be asked for your Raspberry Pi login password.*

<Frame caption="Copying the model to the Raspberry Pi">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/model-copy.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=a098f2e735f186373e509fb53aff490e" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/model-copy.png" />
</Frame>

Now, the model is on the Raspberry Pi's local storage `(/home/raspberrypi)`, and you can verify it by listing the directory content using `ls`.

Move the model to the project directory with the following command `(from /home/raspberrypi)`:

```bash  theme={"system"}
mv akida_model_2.fbz /root/brainchip-inventory-check/model
```

Here we have the model on the project directory, so now everything is ready to be run.

<Frame caption="Project directory">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/model-located.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=74ab575dc2c08205ae8ceea04fa38488" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/model-located.png" />
</Frame>

## Run Inferencing

In the project directory, there are several script options with the following characteristics:

* `inventory.py`: is the original program, it uses a MIPI camera feed to run the inference.
* `stock.py`: is an optimized version of the original program, also uses a MIPI camera but the object markers are bigger.
* `low-power.py`: is a lower-power program with half of energy consumption, and also uses a MIPI camera.
* `usb-inference.py`: is a version that uses a USB camera instead of a MIPI camera (no Matrix control).

There are other auxiliary scripts for testing purposes:

* `mipi_inference.py`: this program runs the FOMO model without controlling the LED Matrix.
* `matrix_test.py`: this program tests the LED matrix displaying colors and patterns.

To run the project, type the following command:

```bash  theme={"system"}
python3 <your prefered program>
# to run the original program:
python3 inventory.py
```

> **The .fbz model is hard coded in the script, so if you want to use the custom one you downloaded, update the "model\_file" variable in the python script**.

The project will start running and streaming a live view of the camera feed plus showing you in the LED matrix the location of detected objects alongside the FOMO inference results, object count, frames per second and energy consumption. To watch a preview of the camera feed, open your favorite browser and enter `http://<Raspberry Pi IP>:8080`.

<Frame caption="Project running | Inference results">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-stock-tracker-brainchip/preview.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=035bb4ff41b6bbaa319d28f9b607e2f7" width="1600" height="900" data-path=".assets/images/fomo-stock-tracker-brainchip/preview.png" />
</Frame>

## Demo

Here I show you the whole project working and running.

<iframe src="https://www.youtube.com/embed/lefxCvfzw4s" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

This project leverages the Brainchip Akida Neuromorphic Hardware Accelerator to propose an innovative solution to inventory stock tracking. It showed a very good performance running at 56 FPS, with less than 100 mW of power consumption and tracking a lot of pieces at a time.


Built with [Mintlify](https://mintlify.com).