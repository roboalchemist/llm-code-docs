# Source: https://docs.edgeimpulse.com/projects/expert-network/traffic-analysis-tao-jetson-orin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart City Traffic Analysis - NVIDIA TAO + Jetson Orin Nano

Created By: Jallson Suryo

Public Project Link: [https://studio.edgeimpulse.com/public/310628/live](https://studio.edgeimpulse.com/public/310628/live)

GitHub Repo: [https://github.com/Jallson/Traffic\_Analysis\_Orin\_Nano/](https://github.com/Jallson/Traffic_Analysis_Orin_Nano)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo01.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=3c409067ac947faae87cc4dd42bdf4f6" width="1199" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo01.png" />
</Frame>

## Problem Statement

In a smart-city system, analyzing vehicle and traffic flow patterns is crucial for a range of purposes, from city planning and road design, to setting up traffic signs and supporting law enforcement. Current systems often depend on manpower, police or separate devices like speed sensors and vehicle counters, making them less practical. Even when object detection is applied, it typically requires powerful, energy-hungry computers or cloud-based systems, limiting widespread adoption of traffic analysis systems. To address this, a low-energy, edge-based Object Detection Traffic Analysis system can be developed. By integrating this into existing cameras at intersections, highways, and bridges, traffic data can be collected more efficiently, enabling broader implementation at lower costs and energy use.

## Our Solution

An object detection model from Edge Impulse is one way of addressing this problem, as model inference output will contains data labels, object coordinates, and timestamps. From this data, we will derive the object's speed and direction, as well as count objects entering or exiting. To simplify the process, we will use an NVIDIA TAO - YOLOv4 pre-trained neural network to build our model, then deploy on to an NVIDIA Jetson Orin Nano. This method grants access to a wide range of pre-trained models, enabling you to leverage existing neural network architectures and weights for your specific tasks. Therefore, the amount of data we need to collect is less than what's typically required when training and building an object detection model from scratch. The Edge Impulse model, combined with NVIDIA TAO, are optimized for efficient performance, achieving faster inference speeds through the Tensor RT library embedded in Orin Nano, which is essential for real-time applications. Overall, this approach can greatly accelerate the development cycle, enhance model performance, and streamline the process for Edge AI applications.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo02.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=72fb51dad06de2f096b71ad79f2b8fd1" width="890" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo02.png" />
</Frame>

### Hardware Requirements

* NVIDIA Jetson Orin Nano Developer Kit (8GB)
* USB Camera/webcam (eg. Logitech C270/ C920)
* DisplayPort to HDMI cable
* Display/monitor
* Tripod
* Keyboard, mouse or PC/Laptop via ssh
* Orin Nano case ( 3D print file available at [https://www.thingiverse.com/thing:6068997](https://www.thingiverse.com/thing:6068997) )

<Frame caption="Hardware">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo03.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=232d6ab010feb068e159067abe5f1da1" width="1121" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo03.png" />
</Frame>

### Software & Online Services

* NVIDIA Jetpack (5.1.2)
* Edge Impulse Studio
* Edge Impulse Linux CLI & Python SDK
* Terminal

## Steps

### 1. Collecting Data (Images/Video)

In the initial stage of building a model in Edge Impulse Studio, we need to prepare the data, which can be in the form of images or videos that will later be split into images. The image and video data can be sourced from free-license databases such as the COCO dataset or Roboflow, which can then be used for object detection training. Alternatively, you can collect your own data to better suit the purposes of your project. Here, I will provide an example of how to upload data in Edge Impulse Studio for both scenarios (see the images below). For those who are not familiar with Edge Impulse Studio, simply visit [https://studio.edgeimpulse.com](https://studio.edgeimpulse.com), login or create an account, then create a new Project. Choose *Images* when given a choice of project type, then *Object detection*. In Dashboard > Project Info, choose *Bounding Boxes* for the labeling method and **NVIDIA Jetson Orin Nano** for the target device. Then move to Data acquisition (on the left hand navigation menu), and click on the *Upload Data* tab.

> Note: When collecting data samples, it's important to remember that the images of vehicles (trucks or cars) to be labeled should not be too small, as the model we're building can only recognize objects with a minimum size of 32x32 pixels.

<Frame caption="Collect\_data">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo04.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=f760ddb509127d822c332715a47a8189" width="960" height="720" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo04.png" />
</Frame>

<br />

<Frame caption="Upload\_COCO-json">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo05.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=7f119a261d87a69166169d757732824a" width="570" height="737" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo05.png" />
</Frame>

<br />

<Frame caption="Upload\_video">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo06.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=d01020638bc0c80ac5dc95d82dedbf73" width="723" height="638" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo06.png" />
</Frame>

### 2. Labeling

The next step is labeling. If you're using data from a COCO JSON dataset that has already been annotated, you can skip this step or simply review or edit the existing labels. For other methods, click on *Data acquisition*, and before labeling video data, you’ll need to split the video into images. Right-click on the three dots to the right, select *Split Into Images*, then click *Yes, Split*. Enter the number of frames per second from the video — usually around 1 or 2 — to avoid having too many nearly identical images.

Once the images are ready, you'll see a labeling queue, and you can begin the process. To simplify this, you can select Label suggestions: Classify using YOLOv5, since cars and trucks will be automatically recognized. Turn off other objects if YOLOv5 detects them incorrectly, then click *Save label*. Repeat this process until all images are labeled.

After labeling, it's recommended to split the data into Training and Testing sets, using around an 80/20 ratio. If you haven't done this yet, you can go back to the Dashboard, and click on *Train / Test Split* and proceed. As shown here, I only used 150 images, as we'll be training the model with the help of pre-trained NVIDIA TAO-YOLO based models.

<Frame caption="Split\_into\_image">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo07.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=8db56799bc8034e3d64ae5c9782c9a0f" width="748" height="429" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo07.png" />
</Frame>

<br />

<Frame caption="Labeling\_with\_Yolo">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo08.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=c0c6b6ddf25a5aa51c51ea80834e93fc" width="1009" height="895" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo08.png" />
</Frame>

<br />

<Frame caption="Train\_and\_Test">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo09.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=21e69194c726d9bc997b6d22fcf60c8d" width="763" height="520" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo09.png" />
</Frame>

### 3. Train and Build Model

Once your labelled dataset is ready, go to Impulse Design > Create Impulse, and set the image width and height to 320x320. Choose *Fit shortest axis*, then select **Image** and **Object Detection** as the Learning and Processing blocks, and click *Save Impulse*. Next, navigate to the Image Parameters section, select *RGB* as the color depth, and press *Save parameters*. After that, click on *Generate*, where you'll be able to see a graphical distribution of the two classes (car and truck).

Now, move to the *Object Detection* navigation on the left, and configure the training settings. Select **GPU** as the compute option and **MobileNet v2 (3x224x224)** as the backbone option. Set the training cycles to around 400 and the minimum learning rate to 0.000005. Choose **NVIDIA TAO YOLOv4** as the neural network architecture — for higher resolutions (eg. 640x640), you can try YOLOv5 (Community blocks) with a model size of medium (YOLOv5m) — Once done, start training by pressing *Start training*, and monitor the progress.

If everything goes well and the precision result is around 80%, proceed to the next step. Go to the *Model Testing* section, click *Classify all*, and if the result is around 90%, you can move on to the final step — Deployment.

<Frame caption="Learning\_blocks">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo10.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=b0558713e1e6c932470d89923f422616" width="1287" height="469" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo10.png" />
</Frame>

<br />

<Frame caption="Save\_parameters">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo11.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=28c8f7539efea3857b1d027c506894c3" width="1264" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo11.png" />
</Frame>

<br />

<Frame caption="Generate\_features">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo12.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=696f417c909b6b0a9d6dcb35bc1b3434" width="1307" height="785" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo12.png" />
</Frame>

<br />

<Frame caption="NN\_setting\_and\_result">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo13.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=838be2df7f25f53a1275014fba061cad" width="1266" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo13.png" />
</Frame>

<br />

<Frame caption="Live\_classification">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo13a.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=ac76fc305d9a662ac5e710f0024c2292" width="1469" height="1000" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo13a.png" />
</Frame>

<br />

<Frame caption="Model\_test">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo14.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=1a20436885760d1fcc0cf05b8eaf9d9a" width="1267" height="783" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo14.png" />
</Frame>

### 4. Deploy Model Targeting Jetson Orin Nano GPU

Click on the *Deployment* tab, then search for **TensorRT**, select *(Unoptimized) Float32*, and click *Build*. This will generate the NVIDIA TensorRT library for running inference on the Orin Nano's GPU. Once downloaded, unzip the file, and you'll be ready to deploy the model using the Edge Impulse SDK on to the NVIDIA Jetson Orin Nano.

Alternatively, there's an easier method: simply ensure that the model has been built in Edge Impulse Studio. From there, you can test, download the model, and run everything directly from the Orin Nano.

<Frame caption="TensorRT\_build\_library">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo15.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=3247a1f7ae618d0966df3d38dcb86fda" width="715" height="936" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo15.png" />
</Frame>

On the Orin Nano side, there are several things that need to be done. Make sure the unit uses JetPack — we use Jetpack v5.1.2 — which is usually pre-installed on the SD card. Then open a Terminal on the Orin Nano, or ssh to the Orin via your PC/laptop and setup Edge Impulse tooling in the terminal.

```
wget -q -O - https://cdn.edgeimpulse.com/firmware/linux/orin.sh | bash
```

You also need to install the Linux Python SDK library (you need Python >=3.7, which is included in JetPack), and it is possible you may need to install Cython to build the Numpy package: `pip3 install Cython`, then install the Linux Python SDK: `pip3 install pyaudio edge_impulse_linux`. You'll also need to clone the examples: `git clone https://github.com/edgeimpulse/linux-sdk-python`

Next, build and download the model.

#### Option A. Build .eim Model with C++ SDK:

Install Clang as a C++ compiler: `sudo apt install -y clang`

Clone the following repository and install these submodules:

`git clone https://github.com/edgeimpulse/example-standalone-inferencing-linux`

`cd example-standalone-inferencing-linux && git submodule update --init --recursive`

Then install OpenCV:

`sh build-opencv-linux.sh`

Now make sure the contents of the TensorRT folder from the Edge Impulse Studio `.zip` file download have been unzipped and moved to the `example-standalone-inferencing-linux` directory.

Build a specific model targeting Orin Nano GPU with TensorRT:

`APP_EIM=1 TARGET_JETSON_ORIN=1 make -j`

The resulting file will be in `./build/model.eim`

#### Option B. Download the Model via the Linux Runner:

Open a terminal on the Orin Nano or ssh from your PC/laptop then run `edge-impulse-linux-runner --clean`, which will allow you to select your project. Log in to your account and choose your project. This process will download the `model.eim` file, which is specifically built with the TensorRT library targeting the Orin Nano GPU. During the process, the console will display the path where the `model.eim` has been downloaded. For example, in the image below, it shows the file located at `/home/orin/.ei-linux-runner/models/310628/v15`.

For convenience, you can copy this file to the same directory as the Python program you'll be creating in the next steps. For instance, you can use the following command to copy it to the home directory: `cp -v model.eim /home/orin`

<Frame caption="Check\_progress">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo16.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=fec5fc74e20611ff8e09a8255ed96bfd" width="955" height="404" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo16.png" />
</Frame>

Now the model is ready to run in a high-level language such as the Python program used in the next step. To ensure this model works, we can run the Edge Impulse Linux Runner with a camera attached to the Orin Nano. You can see a view from the camera via your browser (the IP address location is provided when the Edge Impulse Linux Runner is started). Run this command to start it now: `edge-impulse-linux-runner --model-file <path to directory>/model.eim`

<Frame caption="Live\_stream">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Video01.gif?s=879d9d72b13c152a0cbed4f28aabcc71" width="480" height="480" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Video01.gif" />
</Frame>

The inferencing time is around 6ms, which is incredibly fast for object detection projects.

### 5. Build a Simple Traffic Analysis Program (Python)

With the impressive performance of live inferencing using the Linux Runner, we can now create a Python-based Traffic Analysis program to calculate cumulative counts, and track the direction and speed of vehicles. This program is a modification of the `Classify.py` script from Edge Impulse's examples in the `linux-python-sdk` directory. We have adapted it into an object tracking program by integrating a tracking library, which identifies whether the moving object is the same vehicle or a different one by assigning different IDs. This prevents miscounts or double counts.

For speed calculation, we also use this tracking library by adding two horizontal lines on the screen. We measure the actual distance between these lines and divide it by the timestamp of the object passing between the lines. The direction is determined by the order in which the lines are crossed, for example, A —> B is IN, while B —> A is OUT.

In the first code example, we use a USB camera connected to the Orin Nano and run the program with the following command:

```
python3 traffic.py <path to modelfile>/model.eim
```

If we want to run the program using a video file as input (e.g., video.mp4), we use the path to the video file when executing the program:

```
python3 traffic2.py <path to modelfile>/model.eim <path to videofile>/video.mp4
```

> Note: For video/camera capture display, you cannot use the headless method from a PC/laptop. Instead, connect a monitor directly to the Orin Nano to view the visuals, including the lines, labeled bounding boxes, IN and OUT counts, and vehicle speeds.

<Frame caption="Python\_code">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo17.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=971c0bbdc948740c2530c10f677182e4" width="1045" height="889" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo17.png" />
</Frame>

<br />

<Frame caption="Camera\_feed">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/traffic-analysis-tao-jetson-orin/Photo18.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=e6bf88bc7f015220241216f329c95c62" width="782" height="654" data-path=".assets/images/traffic-analysis-tao-jetson-orin/Photo18.png" />
</Frame>

The Python code and the tracking library is available and can be accessed at [https://github.com/Jallson/Traffic\_Analysis\_Orin\_Nano](https://github.com/Jallson/Traffic_Analysis_Orin_Nano)

Here are two demo videos, showing the results:

<iframe src="https://www.youtube.com/embed/rRZKyNIsXXA" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<br />

<iframe src="https://www.youtube.com/embed/5k3w7zxV6QY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Conclusion

In conclusion, we have successfully implemented an Edge Impulse model using pre-trained **NVIDIA TAO - Yolo** object detection within a Vehicle Traffic Analysis program, running locally on the Orin Nano. It's important to note that the speed figures provided may not be entirely accurate, as they are based on estimates without on-site measurements. To ensure accuracy, measurements should be taken on-site at the camera deployment location. However, this project serves to simulate a concept that can be further developed. The positions of the lines, distance values, angle settings, and other parameters can be easily adjusted in the Python code to better fit the specific conditions of the environment. Finally, it's worth mentioning that we achieved this with a minimal amount of data, and the low memory requirements of the implemented model result in extremely fast inference times. So, we can confidently say that the project's objectives — to enhance speed, simplify processes, and operate with low energy and cost — have been successfully met, making this method suitable for widespread application.


Built with [Mintlify](https://mintlify.com).