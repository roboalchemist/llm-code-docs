# Source: https://docs.edgeimpulse.com/projects/expert-network/high-speed-counting-jetson-nano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# High-resolution, High-speed Object Counting - Nvidia Jetson Nano (TensorRT)

Created By: Jallson Suryo

Public Project Link: [https://studio.edgeimpulse.com/public/207728/live](https://studio.edgeimpulse.com/public/207728/live)

GitHub Repo: [https://github.com/Jallson/High\_res\_hi\_speed\_object\_counting\_FOMO\_720x720](https://github.com/Jallson/High_res_hi_speed_object_counting_FOMO_720x720)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo01.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=48ad336c3940affeebf3e8c3226e62a7" width="630" height="787" data-path=".assets/images/high-speed-counting-jetson-nano/Photo01.png" />
</Frame>

## Problem Statement

The object counting systems in the manufacturing industry are essential to inventory management and supply chains. They mostly use proximity sensors or color sensors to detect objects for counting. Proximity sensors detect the presence or absence of an object based on its proximity to the sensor, while color sensors can distinguish objects based on their color or other visual characteristics. There are some limitations of these systems though; they typically have difficulty detecting small objects in large quantities, especially when they are not in a row or orderly manner. This can be compounded by a relatively fast conveyor belt. These conditions make the object counting inaccurate.

## Our Solution

After experimenting with computer vision on the Jetson Nano [in a previous project](/projects/expert-network/quality-control-jetson-nano), I believe that a computer vision system with its object detection capabilities can explore its potential to accurately count small objects in large quantities and on fast-moving conveyor belts. Basically, we'll explore the capability of [Edge Impulse's FOMO models](/studio/projects/learning-blocks/blocks/object-detection/fomo) that have been optimized for the GPU in the Jetson Nano. In this project, the production line / conveyor belt will run quite fast, with lots of small objects in random positions, and the number of objects will be counted live and displayed on a 16x2 LCD display. Speed and accuracy are the goals of the project.

<Frame caption="Schematic diagram">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo02.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=1d4b45ef2be4222ca9936fd83d706c55" width="714" height="918" data-path=".assets/images/high-speed-counting-jetson-nano/Photo02.png" />
</Frame>

## How Does It Work?

This project utilizes Edge Impulse's FOMO algorithm, which can quickly detect objects in every frame that a camera captures on a running conveyor belt. FOMO's ability to know the number and position of coordinates of an object is the basis of this system. The project aims to assess the Nvidia Jetson Nano's GPU capabilities in processing higher-resolution imagery (720x720 pixels), compared to typical FOMO object detection projects (which often target lower resolutions such as 96x96 pixels), all while maintaining optimal inference speed.

The machine learning model (named `model.eim`) will be deployed using the TensorRT library, configured with GPU optimizations and integrated through the Linux C++ SDK. Additionally, the Edge Impulse model will be seamlessly integrated into our Python codebase to facilitate cumulative object counting. Our proprietary algorithm compares current frame coordinates with those of previous frames to identify new objects and avoid duplicate counting.

<Frame caption="Jetson Nano, camera, and conveyor belt">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo03.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=4c4c4243c68c4d3795f81c7482ba4964" width="591" height="591" data-path=".assets/images/high-speed-counting-jetson-nano/Photo03.png" />
</Frame>

### Hardware Requirements:

* NVIDIA Jetson Nano Developer Kit
* USB Camera (eg. Logitech C922)
* Mini conveyor belt system with camera stand
* Objects: eg. bolt
* Ethernet cable
* PC/Laptop to access Jetson Nano via SSH

### Software & Online Services:

* Edge Impulse Studio
* Edge Impulse Linux, Python & C++ SDK
* NVIDIA Jetpack SDK
* Terminal

## Steps

### 1. Prepare Data / Images

In this project we use a Logitech C922 USB camera capable of 720p at 60 fps connected to a PC/laptop to capture the images for data collection, for ease of use. Take pictures from above the parts, at slightly different angles and lighting conditions to ensure that the model can work under different conditions (to prevent overfitting). Object size is a crucial aspect when using FOMO, to ensure the performance of this model. You must keep the camera distance from the objects consistent, because significant difference in object sizes will confuse the algorithm and cause difficulty in the auto-labelling process.

<Frame caption="Data variation">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo04.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=8432449da746f033ebb2b647de5a9497" width="870" height="870" data-path=".assets/images/high-speed-counting-jetson-nano/Photo04.png" />
</Frame>

### 2. Data Acquisition and Labeling

Open studio.edgeimpulse.com, login or create an account then create a new project.

Choose the *Images* project option, then *Object detection*. In *Dashboard > Project Info*, choose *Bounding Boxes* for the labeling method and *NVIDIA Jetson Nano* for the target device. Then in *Data acquisition*, click on *Upload Data* tab, choose your photo files, automatically split them between Training and Testing, then click on *Begin upload*.

Next,

* For Developer accounts: click on the *Labeling queue* tab then drag a bounding box around an object and label it, then click Save. Repeat this until all images labelled. It goes quickly though, as the bounding boxes will attempt to follow an object from image to image.
* For Enterprise accounts: click on *Auto-Labeler* in *Data Acquisition*. This auto-labeling segmentation / cluster process will save a lot of time over the manual process above. Set min/max object pixels and sim threshold (0.9 - 0.999) to adjust the sensitivity of cluster detection, then click *Run*. If something doesn't match or if there is additional data, labeling can be done manually as well.

<Frame caption="Upload data">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo05.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=e669580b985da9881433588d4085bd41" width="1122" height="803" data-path=".assets/images/high-speed-counting-jetson-nano/Photo05.png" />
</Frame>

<br />

<Frame caption="Auto-labeling">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo06.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=031db97975cbfd819efa891e37668370" width="947" height="987" data-path=".assets/images/high-speed-counting-jetson-nano/Photo06.png" />
</Frame>

<br />

<Frame caption="Label cluster">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo07.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=9e692e3662f7954adc72efa11bd24a78" width="900" height="1000" data-path=".assets/images/high-speed-counting-jetson-nano/Photo07.png" />
</Frame>

<br />

<Frame caption="Manual labeling">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo08.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=2b2e7c5dd0127d9b4f0a03913619ed48" width="960" height="890" data-path=".assets/images/high-speed-counting-jetson-nano/Photo08.png" />
</Frame>

<br />

<Frame caption="Balance ratio\_80/20">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo09.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=1556342c270babf2dca16ae46c99eaa5" width="630" height="524" data-path=".assets/images/high-speed-counting-jetson-nano/Photo09.png" />
</Frame>

### 3. Train and Build Model Using FOMO Object Detection

Once you have the dataset ready, go to *Create Impulse* and set 720 x 720 as the image width and height. Then choose *Fit shortest axis*, and choose *Image* and *Object Detection* as Learning and Processing blocks.

In the Image block configuration, select Grayscale as the color depth and click *Save parameters*. Then click on *Generate features* to get a visual representation of the features extracted from each image in the dataset. Navigate to the Object Detection block setup, and leave the default selections as-is for the Neural Network, but perhaps bump up the number of training epochs to 120. Then we choose *FOMO (MobileNet V2 0.35)*, and train the model by clicking the *Start training* button. You can see the progress on the right side of the page.

If everything is OK, then we can test the model, go to *Model Testing* on the left navigation and click *Classify all*. Our result is above 90%, so we can move on to the next step — Deployment.

<Frame caption="Blocks">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo10.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=507968573854f9d01506205489bd6ebc" width="1263" height="475" data-path=".assets/images/high-speed-counting-jetson-nano/Photo10.png" />
</Frame>

<br />

<Frame caption="Save parameters">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo11.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=60773219b44d431601590e12d296e383" width="1252" height="729" data-path=".assets/images/high-speed-counting-jetson-nano/Photo11.png" />
</Frame>

<br />

<Frame caption="Generate features">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo12.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=6751f4b66907e930d47122f5a7d20b2e" width="1255" height="775" data-path=".assets/images/high-speed-counting-jetson-nano/Photo12.png" />
</Frame>

<br />

<Frame caption="Result">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo13.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=3757e17d337812a3cf117bda3b365e0f" width="1257" height="1000" data-path=".assets/images/high-speed-counting-jetson-nano/Photo13.png" />
</Frame>

<br />

<Frame caption="Test">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/high-speed-counting-jetson-nano/Photo14.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=177e9c48194706c471d68b5d0a91e250" width="1261" height="907" data-path=".assets/images/high-speed-counting-jetson-nano/Photo14.png" />
</Frame>

### 4. Deploy Model Targeting Jetson Nano's GPU

Click on the *Deployment* navigation item, then search for *TensorRT*. Select *Float32* and click *Build*. This will build an NVIDIA TensorRT library for running inferencing targeting the Jetson Nano's GPU. After it has downloaded, open the `.zip` file and then we're ready for model deployment with the Edge Impulse C++ SDK directly on the NVIDIA Jetson Nano.

<Frame caption="TensorRT build library">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/high-speed-counting-jetson-nano/Photo15.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=5b9dcd6356af41a7e1623990d27a87e4" width="722" height="817" data-path=".assets/images/high-speed-counting-jetson-nano/Photo15.png" />
</Frame>

On the Jetson Nano, there are several things that need to be done to get ready for our project. Make sure the device is running it's native Ubuntu OS and JetPack which are usually pre-installed on the SD card. More information on [downloading and flashing the SD Card is available here](https://developer.nvidia.com/jetpack-sdk-463). Then `ssh` via a PC or laptop with Ethernet and setup Edge Impulse firmware in the terminal:

```
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/jetson.sh | bash
```

Then install Clang as a C++ compiler:

```
sudo apt install -y clang
```

Clone from this repository and install these submodules:

```
git clone https://github.com/edgeimpulse/example-standalone-inferencing-linux
cd example-standalone-inferencing-linux && git submodule update --init --recursive
```

Then install OpenCV and dependencies:

```
sh build-opencv-linux.sh
```

Build a specific model targeting NVIDIA Jetson Nano GPU with TensorRT using clang:

```
APP_EIM=1 TARGET_JETSON_NANO=1 make -j
```

The result will be a file that is ready to run: `/build/model.eim`

If your Jetson Nano is running on a dedicated power supply (as opposed to a battery), its performance can be maximized by this command:

`sudo /usr/bin/jetson_clocks`

Now the model is ready to run in a high-level language such as the Python program in the next step. To ensure this model works, we can run the Edge Impulse Runner with the camera setup on the Jetson Nano and run the conveyor belt. You can the see the camera stream via your browser (the IP address is provided when Edge Impulse Runner first starts up). Run this command:

```
edge-impulse-linux-runner --model-file <path to directory>/model.eim
```

<Frame caption="Video stream from your browser">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/high-speed-counting-jetson-nano/Video01.gif?s=6d7b2bd70a595a8a0e9d8733ad7f8d87" width="1280" height="720" data-path=".assets/images/high-speed-counting-jetson-nano/Video01.gif" />
</Frame>

The inferencing time is around 15ms, which is an incredibly fast detection speed.

To compare these results, I have also deployed with the standard CPU-based deployment option (Linux AARCH64 model), and run with the same command above. The inferencing time is around 151ms with a Linux model that targets the CPU.

<Frame caption="Deploy to CPU">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/high-speed-counting-jetson-nano/Photo16.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=a01bb4230ebb297f23eb96bc4038e283" width="657" height="1000" data-path=".assets/images/high-speed-counting-jetson-nano/Photo16.png" />
</Frame>

<br />

<Frame caption="CPU vs GPU">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/high-speed-counting-jetson-nano/Photo17.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=5660925582146cff20b5c37528dcde96" width="1600" height="838" data-path=".assets/images/high-speed-counting-jetson-nano/Photo17.png" />
</Frame>

You can see the difference in inferencing time is about 10x faster when we target the GPU for the process. Impressive!

### 5. Build Cumulative Count Program (Python)

Before we start with Python, we need to install the Edge Impulse Python SDK and clone the repository from the previous Edge Impulse examples. Follow the steps [here](/tools/libraries/sdks/inference/linux/python).

With the impressive performance of live inferencing in the Runner, now we will create a Python program to be able to calculate the cumulative count of moving objects taken from camera capture. The program is a modification of Edge Impulse's `classify.py` in `examples/image` from the `linux-python-sdk directory`. We turned it into an object tracking program by solving a bipartite matching problem so the same object can be tracked across different frames to avoid double counting. For more detail, you can download and check the python program at this link, [https://github.com/Jallson/High\_res\_hi\_speed\_object\_counting\_FOMO\_720x720](https://github.com/Jallson/High_res_hi_speed_object_counting_FOMO_720x720)

<Frame caption="count\_moving\_bolt.py">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/high-speed-counting-jetson-nano/Photo18.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=ea4f5503cb3b599a0d3ef28d3e717bd2" width="1478" height="1000" data-path=".assets/images/high-speed-counting-jetson-nano/Photo18.png" />
</Frame>

You can git clone the repo, or then run the program with the command pointing to the path where `model.eim` is located:

```
python3 count_moving_bolt.py <path to modelfile>/model.eim
```

Here is a demo video of the results:

<iframe src="https://www.youtube.com/embed/ouqvACe48ts" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

The delay visible in the video stream display and its corresponding output calculation is caused by the OpenCV program rendering a 720x720 display resolution window, not by the inference time of the object detection model. This demo test uses 30 bolts per cycle attached to the conveyor belt to show a comparison with the output on the counter.

## Conclusion

We have successfully implemented object detection on a high-speed conveyor belt, with high-resolution video captured, and run a cumulative counting program locally on an Nvidia Jetson Nano. With the speed and accuracy obtained, we are confident in the scalability of this project to various scenarios, including high-speed conveyor belts, multiple object classes, and sorting systems.


Built with [Mintlify](https://mintlify.com).