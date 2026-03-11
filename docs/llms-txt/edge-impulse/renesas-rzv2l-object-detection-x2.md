# Source: https://docs.edgeimpulse.com/tutorials/hardware/renesas-rzv2l-object-detection-x2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas RZ/V2L - object detection (x2)

In this tutorial, you will learn how to run multiple cameras with multiple models simultaneously on the Renesas RZ/V2L microprocessor. The models used for this demo are:

* **YOLOv5** - Face detection using DRPAI acceleration
* **ResNet** - Number recognition on AARCH64 (no acceleration)

<Frame caption="Overview of running multiple object detection models on RZ/V2L">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-multi-cam-model-diagram.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=1b466855e864f19cd573577bd8222c38" width="1280" height="720" data-path=".assets/images/rz-multi-cam-model-diagram.png" />
</Frame>

# Prerequisites

To follow this tutorial, you will need a combination of hardware and software tools. You will need an Edge Impulse compatible Renesas RZ board, either the Renesas RZ/V2L smarc board or the Avnet RZBoard. In addition to the board, the following additional items are needed:

* Two webcams - the webcams used for this tutorial are:
  * Logitech C920 HD Pro Webcam
  * Logitech C922 Pro Stream 1080p Webcam
* USB hub (to connect the cameras to the Renesas RZ/V2L board)
* Ethernet cable or USB serial cable

Note that any webcams will suffice for this application. Some details will have to be modified depending on the cameras, this is explained in detail further along in the tutorial.

In order to successfully install and run the application, you need access to the target's Linux terminal. You may require other hardware like ethernet cable or USB to serial cable to achieve this. Detailed instructions on how to set the device up and gain access to the Linux are not provided here. For the Renesas RZ/V2L board, please refer to this page and for the Avnet RZBoard, please refer to this page.

# Example models

The models used for this tutorial can be downloaded as a zip file from this [link](https://drive.google.com/drive/folders/1dBekqxm2SLRrW9t-mHExw3HhjxnB_8uo?usp=sharing). The file (`models-20230921T125858Z-001.zip`) that you download, may be named differently for you. Once the file has been downloaded, go ahead and unzip the files either in the GUI or as follows:

```bash  theme={"system"}
unzip models-20230921T125858Z-001.zip
```

There are two folders in this zip file. The **cpu** directory contains a ResNet model that identifies numbers for a Linux aarch64 target **without** acceleration by the DRPAI. The **drpai** directory contains a YOLOv5 face detection model for the RZ/V2L microprocessor with DRPAI acceleration incorporated. Once the files have been extracted, their permissions need to be changed to make them executable. This can be done as follows:

```bash  theme={"system"}
chmod u+x models/drpai/face-detection-linux-aarch64-rzv2l-v33.eim
chmod u+x models/cpu/detect-numbers-resnet-linux-aarch64-v24.eim
```

# The node.js application

## Setup and installation

The application required to run the two models simultaneously must be downloaded from the Edge Impulse CLI repository. The simplest way to do this is to run the following command in your terminal/command line application:

```bash  theme={"system"}
wget https://github.com/edgeimpulse/edge-impulse-linux-cli/archive/refs/heads/classify-camera-finer-control.zip
```

If you would like to do it manually, it can be downloaded [here](https://github.com/edgeimpulse/edge-impulse-linux-cli/tree/classify-camera-finer-control) at the branch **classify-camera-finer-control**, at commit number: `1fc1639acdfb9e7af3fc8794619334b28dffac00`. Once the application has been downloaded, unzip the contents, navigate to the directory and list the contents to ensure the operation was successful. This can be done as follows:

```bash  theme={"system"}
unzip classify-camera-finer-control.zip
cd edge-impulse-linux-cli-classify-camera-finer-control
ls -l
```

While staying at the same directory, install the dependencies and build the application as follows:

```bash  theme={"system"}
npm install
npm run build
```

Please ensure that you are inside the directory `edge-impulse-linux-cli-classify-camera-finer-control` when installing and running the application.

## Running the application

Before we can run the application, please ensure that the directory structure is as follows:

```bash  theme={"system"}
/home
│
├── edge-impulse-linux-cli-classify-camera-finer-control
│   ├── borc
│   ├── cli
│   ...
├── models
│   ├── drpai
│   │   └── face-detection-linux-aarch64-rzv2l-v33.eim
│   ├── cpu
│   │   └── detect-numbers-resnet-linux-aarch64-v24.eim
...
```

In the previous step, we installed an application called **classify-camera**. To run this app with two cameras and two separate models, the same app needs to be executed twice in two separate terminal instances with different cameras. The arguments required by the app are:

* **model** - name of the model to executed in the current instance (required)
* **camera** - the name of the camera to be used for the instance as detected by the system (required)
* **fps** - frames per second of the input stream. This will affect the speed of the app (default: 5)
* **width** - the width of the input image directed to the respective model (default: 640)
* **height** - the height of the input image directed to the respective model (default: 480)

The syntax of the command to be executed is as follows:

```bash  theme={"system"}
node build/examples/ts/classify-camera.js path_to_model name_of_webcam fps_value image_width image_height
```

Before running the first instance, we first need to determine the names of the webcam(s) that are detected by the system. The correct name is required to direct the stream from camera to the respective models. The easiest way to do this is by running the command with only the model as an argument. In this case:

```bash  theme={"system"}
cd edge-impulse-linux-cli-classify-camera-finer-control/
node build/examples/ts/classify-camera.js ../models/drpai/face-detection-linux-aarch64-rzv2l-v33.eim
```

The command will fail and result in an error with the error message containing names of the connecting cameras. In this case, the output might be as follows:

```bash  theme={"system"}
Starting the image classifier for Renesas / Face Detection (v34)
Parameters image size 320x320 px (3 channels) classes [ 'face' ]
[GST] checking for /etc/os-release
Error: Multiple cameras found ("HD Pro Webcam C920", "C922 Pro Stream Webcam"), add the camera to use to this script (node classify-camera.js model.eim cameraname)
    at /home/root/classify-camera-finer-control/build/examples/ts/classify-camera.js:43:19
```

From this output, we can determine that the names of cameras detected by the system are "HD Pro Webcam C920" and "C922 Pro Stream Webcam". These names can now be used to run the application. Before running the application, ensure that your current working directory is correct - it needs to be the `edge-impulse-linux-cli-classify-camera-finer-control` folder. In this case, the `cd` commands from the following instructions can be omitted.

You will need to open two terminal instances.

In **terminal 1** run the following command:

```bash  theme={"system"}
cd edge-impulse-linux-cli-classify-camera-finer-control/
node build/examples/ts/classify-camera.js ../models/drpai/face-detection-linux-aarch64-rzv2l-v33.eim "HD Pro Webcam C920" 5 320 320
```

And in **terminal 2** run the following command:

```bash  theme={"system"}
cd edge-impulse-linux-cli-classify-camera-finer-control/
node build/examples/ts/classify-camera.js ../models/cpu/detect-numbers-resnet-linux-aarch64-v24.eim "C922 Pro Stream Webcam" 5 240 240
```

Once both these commands have been executed, you will be able to see the results of the models in the terminal similar to the following in terminal 1:

```bash  theme={"system"}
Starting the image classifier for Renesas / Face Detection (v34)
Parameters image size 320x320 px (3 channels) classes [ 'face' ]
[GST] checking for /etc/os-release
Using camera HD Pro Webcam C920 starting...
Connected to camera
boundingBoxes 9ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
...
```

and the following in terminal 2:

```bash  theme={"system"}
Starting the image classifier for Renesas / Detect numbers Resnet (v24)
Parameters image size 224x224 px (3 channels) classes [
  '0', '1', '2', '3',
  '4', '5', '6', '7',
  '8', '9'
]
[GST] checking for /etc/os-release
Using camera C922 Pro Stream Webcam starting...
Connected to camera
classification 1672ms. {
  '0': '0.1046',
  '1': '0.3136',
  '2': '0.3120',
  '3': '0.0294',
  '4': '0.0185',
  '5': '0.0056',
  '6': '0.0084',
  '7': '0.1623',
  '8': '0.0071',
  '9': '0.0385'
}
```

Running the application in this way will not provide a visual output. To see a visual result of this inference, please see the following section.

## Running the application with WebServer

The above steps are enough to execute both models and see their outputs in the terminal. However, it is always better to see a visual output of the image detection models that are being executing. With a slight modification of the execution commands, it is possible to run the application using WebServer and see the visual output.

The arguments to run the application using WebServer are as follows:

* **model** - name of the model to executed in the current instance (required)
* **camera** - the name of the camera to be used for the instance as detected by the system (required)
* **fps** - frames per second of the input stream. This will affect the speed of the app (default: 5)
* **width** - the width of the input image directed to the respective model (default: 640)
* **height** - the height of the input image directed to the respective model (default: 480)
* **port** - this is the port to which the output from the cameras and application is directed (default: 4912)

The syntax of the command to be executed is then changed to the following:

```bash  theme={"system"}
node build/examples/ts/classify-camera-webserver.js path_to_model name_of_webcam fps_value image_width image_height port
```

Similar to running the application before, you will need to open two terminal instances.

In **terminal 1** run the following command:

```bash  theme={"system"}
cd edge-impulse-linux-cli-classify-camera-finer-control/
node build/examples/ts/classify-camera-webserver.js ../models/drpai/face-detection-linux-aarch64-rzv2l-v33.eim "HD Pro Webcam C920" 5 320 320 4912
```

The terminal output from this command will be:

```bash  theme={"system"}
Starting the image classifier for Renesas / Face Detection (v34)
Parameters image size 320x320 px (3 channels) classes [ 'face' ]
[GST] checking for /etc/os-release
Using camera HD Pro Webcam C920 starting...
Connected to camera

Want to see a feed of the camera and live classification in your browser? Go to http://192.168.178.30:4912

boundingBoxes 9ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
boundingBoxes 8ms. []
...
```

Navigating to the address mentioned in the output (`http://192.168.178.30:4912` in this case), you will see an output similar to this:

<Frame caption="Face detection with bounding box using DRP-AI">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-face-detection-large-text.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=18e1c5835e6ad54a57504ca065fed076" width="1600" height="873" data-path=".assets/images/rz-face-detection-large-text.png" />
</Frame>

In **terminal 2** run the following command:

```bash  theme={"system"}
cd edge-impulse-linux-cli-classify-camera-finer-control/
node build/examples/ts/classify-camera-webserver.js ../models/cpu/detect-numbers-resnet-linux-aarch64-v24.eim "C922 Pro Stream Webcam" 5 240 240 4913
```

The terminal output from this command will be:

```bash  theme={"system"}
Starting the image classifier for Renesas / Detect numbers Resnet (v24)
Parameters image size 224x224 px (3 channels) classes [
  '0', '1', '2', '3',
  '4', '5', '6', '7',
  '8', '9'
]
[GST] checking for /etc/os-release
Using camera C922 Pro Stream Webcam starting...
Connected to camera

Want to see a feed of the camera and live classification in your browser? Go to http://192.168.178.30:4913

classification 1672ms. {
  '0': '0.1046',
  '1': '0.3136',
  '2': '0.3120',
  '3': '0.0294',
  '4': '0.0185',
  '5': '0.0056',
  '6': '0.0084',
  '7': '0.1623',
  '8': '0.0071',
  '9': '0.0385'
}
```

> Note that the port numbers passed as arguments **must** be different. This allows for the streams to be directed to different ports to be viewed in the browser.

Navigating to the address mentioned in the output (`http://192.168.178.30:4912` in this case), you will see an output similar to this:

<Frame caption="Number detection on CPU.">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-detect-number-5-large-text.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=b70c4c029be241fd3af5f0c20a3eeed1" width="1512" height="824" data-path=".assets/images/rz-detect-number-5-large-text.png" />
</Frame>

Now you have two models running simultaneously. You will notice that the model running on the CPU has a significantly higher inference time (above 1200ms) as opposed to the model running on the DRP-AI (under 10ms). You can see a side by side view of this parallelism:

<Frame caption="Simultaneous execution of two models.">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-bi-model-view-large-text.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=0ca40890ea47603a0bf8d89f49b4ac69" width="1600" height="997" data-path=".assets/images/rz-bi-model-view-large-text.png" />
</Frame>

You can see the two models running simultaneously in the video below:

<iframe src="https://www.youtube.com/embed/1vmLOGEZMkA" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

Congratulations! You have successfully run two Edge Impulse generated models simultaneously on the Renesas RZ/V2L device. You will notice that the model run using the DRP-AI accelerator is orders of magnitude faster than the one running simply on the CPU.

Using this application, you can run any two image-based models simultaneously on the RZV2L device. If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

The possibilities are endless, and we can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).