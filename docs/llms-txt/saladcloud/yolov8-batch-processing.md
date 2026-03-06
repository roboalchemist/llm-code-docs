# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/yolov8-batch-processing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch Processing

*Last Updated: October 10, 2024*

## Introduction

This guide is a continuation of our previous article, focusing on deploying the YOLO model for batch processing on
SaladCloud. This approach is ideal for processing large volumes of data where real-time analysis is not required, or if
you want to process multiple streams not worrying’s which node will pick the job up.

You can check more detailed project overview in our previous guide **Fast API for Real-Time Processing**
[here](/container-engine/tutorials/computer-vision/yolov8-deployment-tutorial).

## Reference Architecture for Batch Processing for Asynchronous Workloads

* **Objective**: Set up a batch processing system that reacts to new video stream links stored in Azure.
* **Process Flow**:
  * Video stream links are saved in an Azure storage container.
  * An event grid with subscriptions is configured to monitor the storage container and create a message in a storage
    queue whenever a new file is added.
  * A Python script for batch processing is containerized and deployed across multiple SaladCloud compute nodes.
  * This batch process routinely checks the storage queue. When a new message appears, it picks up the corresponding
    stream for processing.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=68aad623c83ac62b492ce5dfdbf4fe30" data-og-width="975" width="975" data-og-height="1047" height="1047" data-path="container-engine/images/yolov8-batch-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=b6dbb976de385dd6cea91587f3ec9c5f 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=9dc2cab050e5a0f3737463e1ff436df6 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d79ed88de4fde0f4872abd9696746120 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=06937b6c09856db1cb9219a9e5b0aaad 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=b1dbbcf96c20f1141ee44c9120112b05 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-architecture.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=fcbc93000e2a98b30b879729c9b99365 2500w" />

## Folder Structure

Our full solution is stored here: [git repo](https://github.com/SaladTechnologies/yolov8-on-salad)

Here is the folder structure we will have once the project is done:

```text  theme={null}
yolo8-video-stream/
├─ src/
│  ├─ infrastructure/
│  │  ├─ main.bicep (azure resources deployment for batch)
│  ├─ python/
│  │  ├─ api (architecture 1)/
│  │  │  ├─ inference/
│  │  │  │  ├─ dev/
│  │  │  │  │  ├─ setup
│  │  │  │  ├─ fast.py (single link)
│  │  │  │  ├─ fast_multi.py (multi-threading)
│  │  │  ├─ docker.sh/
│  │  │  ├─ Dockerfile
│  │  ├─ batch (architecture 2)/
│  │  │  ├─ inference/
│  │  │  │  ├─ dev/
│  │  │  │  │  ├─ setup
│  │  │  │  ├─ batch.py (Batch processing script)
│  │  │  │  ├─ batch-multi-thread.py (Batch processing script with multi threading)
│  │  │  │  ├─ requirements.txt
│  │  │  ├─ .dockerignore
│  │  │  ├─ docker.sh
│  │  │  ├─ Dockerfile

```

## Deploy Azure Resources

It's essential to first deploy the necessary infrastructure on Azure.

We will deploy:

* Storage Account for storing input and output data
  * Blob Containers for organizing the data within the Storage Account (default names: requests, yolo-results,
    failed-requests)
  * Storage Queue for storing messages (default names: `requestqueue`, `poison-requestqueue`). Our batch process will be
    checking if there are any new messages in the queue.
  * Event Grid System Topic and Event Subscription for triggering events when new blobs are created in the input
    container. Every time a new file is created in the requests container a message will be created in the queue.

Here’s a step-by-step guide to deploying these resources:

1. **Create an Azure Subscription and Resource Group**: If you haven't already, sign up for Azure and create a
   subscription. Within this subscription, create a resource group that will contain all the resources for your project.
2. **Login to Azure**:
   * Open your command line interface (CLI).
   * Use the Azure CLI command to log in:
     ```shell  theme={null}
     az login --tenant <tenant_id>
     ```
   * Set your subscription:
     ```shell  theme={null}
     az account set --subscription <subscription_name>
     ```
3. **Deploy resources**:
   * Navigate to the main.bicep file inside of infrastructure folder and run the following command:
     ```shell  theme={null}
     az deployment group create \
       --resource-group <resource group name> \
       --template-file main.bicep
     ```
   * All resource names are set as parameters, so you can override them:
     ```shell  theme={null}
      az deployment group create \
       --resource-group <resource group name> \
       --template-file main.bicep \
       --parameters RequestsQueueName=<NewName>
     ```
4. **Check resources**:
   * Open your resource group in azure and check the resources. You should see something similar to this:
     <img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=82b13af88d9934982fe5eecbe421f447" data-og-width="1318" width="1318" data-og-height="64" height="64" data-path="container-engine/images/yolov8-azure-resource-group-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=8dc2f7bb67734b9e92be1f02060f62b4 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=f10e5907fa519863ecd3b6235c804628 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a5a3dd4798885671af3e8a3c5efe0c09 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=fe4bd65cf96ad1817023da64c2621fbf 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4c2ce2c52c7294bce24a2874dccc8297 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-resource-group-preview.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3fe58f527d4a324859f4654fa914a3be 2500w" />

## Local Environment

Before we deploy solution on SaladCloud's infrastructure, it's crucial to evaluate YOLOv8's capabilities in a local
setting. This allows us to troubleshoot any issues and make any make our solution meet our needs.

### Local Development Setup: Installing Necessary Libraries

Setting up an efficient local development environment is essential for a smooth workflow. We ensure this by preparing
[setup](https://github.com/SaladTechnologies/yolov8-on-salad/tree/main/src/python/batch/inference/dev) and
[requirements](https://github.com/SaladTechnologies/yolov8-on-salad/blob/main/src/python/batch/inference/requirements.txt)
files to facilitate the installation of all dependencies. These files help verify that the dependencies function
correctly during the development phase. We provide the complete contents of the requirements file and the setup script
below.

The Setup Script:

```bash  theme={null}
#! /bin/bash

set -e

echo "setup the curent environment"
CURRENT_DIRECTORY="$( dirname "${BASH_SOURCE[0]}" )"
cd "${CURRENT_DIRECTORY}"
echo "current directory: $( pwd )"
echo "setup development environment for inference"
YOLOv8_SRC_BATCH_DIR="$( cd .. && pwd )"
echo "dev directory set to: ${YOLOv8_SRC_BATCH_DIR}"
echo "remove old virtual environment"
rm -rf "${YOLOv8_SRC_BATCH_DIR}/.venv"
echo "create new virtual environment"
python3.9 -m venv "${YOLOv8_SRC_BATCH_DIR}/.venv"
echo "activate virtual environment"
source "${YOLOv8_SRC_BATCH_DIR}/.venv/bin/activate"
echo "installing dependencies ..."

(cd "${YOLOv8_SRC_BATCH_DIR}" && python -m pip install pip==21.1.1)
(cd "${YOLOv8_SRC_BATCH_DIR}" && pip install numpy)
(cd "${YOLOv8_SRC_BATCH_DIR}" && pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git")
(cd "${YOLOv8_SRC_BATCH_DIR}" && pip install lap==0.4.0)
(cd "${YOLOv8_SRC_BATCH_DIR}" && pip install --upgrade pip && pip install -r requirements.txt)
```

To establish a clean virtual environment and install all the necessary libraries, you simply need to execute the script
using following command:

```bash  theme={null}
bash dev/setup
```

## Exploring YOLOv8's Capabilities and Data Compatibility

As we delve into the practicalities of implementing YOLOv8 for object detection, a fundamental step is to understand the
range of its capabilities and the types of data it can process effectively. This knowledge will shape our approach to
solving the problem at hand. Here is a list of possible inputs:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=cf7324ae7b2c344810a950db73611f35" data-og-width="919" width="919" data-og-height="691" height="691" data-path="container-engine/images/yolov8-inputs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=21cfc8d39b04e512d32270740b7d8fb1 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=7ced276833de7cae31032e0bde825607 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a1fb755175eecc185b244ff70d616c93 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0207029c098722be212e629bd571d611 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=34e3af4b59354afaaad1e5046ccff337 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-inputs.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=87f7bec178e9bb19fdf4ec12e337b318 2500w" />

Our project's scope now narrows to the realm of video processing, with a particular focus on YouTube videos and live
stream data.

## Video processing

We'll begin by experimenting with an example straight from the
[Ultralytics documentation](https://docs.ultralytics.com/modes/predict/#inference-sources), which illustrates how to
apply the basic object detection model provided by YOLO on video sources. This example uses the 'yolov8n' model, which
is the YOLOv8 Nano model known for its speed and efficiency.

Here's the starting code snippet provided by Ultralytics for running inference on a video:

```python  theme={null}
from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')
# Define source as YouTube video URL
source = 'https://youtu.be/LNwODJXcvt4 '
# Run inference on the source
results = model(source)
```

To better understand processing capabilities of YOLOv8, we will integrate it with OpenCV (cv2), a powerful library for
computer vision tasks. This setup will allow us to visualize object detection as it happens. Before running the script,
ensure that you have installed the necessary packages, **opencv-python**, **ultralytics**, and **cap\_from\_youtube**, the
last of which addresses OpenCV's current limitations with YouTube video streams.

```python  theme={null}
from ultralytics import YOLO
import cv2
from cap_from_youtube import cap_from_youtube

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open youtube video
link = "https://www.youtube.com/watch?v=yHP-zGsoqRA "
cap = cap_from_youtube(link, "720p")

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break
# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
```

With this script, as YOLO processes the video frames and identifies objects, bounding boxes will be drawn around them.
You'll see a display window pop up showing the video feed with the detections overlaid. Pay attention to the output
displayed at the bottom of the screen for additional insights. Let’s run our code and see what happens.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-video-stream-1.gif?s=d500fcaec999ec6b6a59295ba5e737ff" data-og-width="600" width="600" data-og-height="400" height="400" data-path="container-engine/images/yolov8-video-stream-1.gif" data-optimize="true" data-opv="3" />

## Processing Live Video Stream from Youtube

Now we move on to the task of processing live video streams. While **cap\_from\_youtube** works well for YouTube videos by
loading them into memory, live streams require a different approach due to their continuous and unbounded nature.

Pafy is a Python library that interfaces with YouTube content, providing various streams and metadata around YouTube
videos and playlists. To make it work in the virtual environment we had to solve a few libraries issues we discussed
earlier. To make the process easier for you run the dev/setup file we also mentioned earlier. For live video streams,
Pafy allows us to access the stream URL, which we can then pass to OpenCV for real-time processing. Here's how we can
use Pafy to open a live YouTube stream:

```python  theme={null}
import pafy

# Open youtube video with a live stream
link = "https://www.youtube.com/watch?v=GSmCh4DrbWY "
video = pafy.new(link)
best = video.getbest(preftype="mp4")
cap = cv2.VideoCapture(best.url)
```

## Processing Live Video Stream (RTSP, RTMP, TCP, IP address)

Ultralytics gives us an example of running inference on remote streaming sources using RTSP, RTMP, TCP and IP address
protocols. If multiple streams are provided in a `*.streams` text file then batched inference will run, i.e. 8 streams
will run at batch-size 8, otherwise single streams will run at batch-size 1. We will include it in our code as well.
Based on specific link parameters our process will pick which way to process the link. You can check that in the full
script

```python  theme={null}
from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Single stream with batch-size 1 inference
source = 'rtsp://example.com/media.mp4'  # RTSP, RTMP, TCP or IP streaming address

# Multiple streams with batched inference (i.e. batch-size 8 for 8 streams)
source = 'path/to/list.streams'  # *.streams text file with one streaming address per row

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects

```

## Implementing Object Tracking

Having established the method to process live streams, the next crucial feature of our project is to track the
identified objects. YOLOv8 comes equipped with a built-in tracking system that assigns unique IDs to each detected
object, enabling us to follow their movement across frames. There is a way to pick between 2 tracking models, but for
now we will just use the default one.

**Enabling Tracking with YOLOv8:**

To utilize the tracking functionality, we simply need to modify our inference call. By adding **.track** to our model
call and setting **persist=True**, we instruct the model to maintain object identities consistently over time. This
addition to the code will look like this:

```python  theme={null}
results = model.track(frame, persist=True)
```

Let’s try it:

<img src="https://mintlify.s3.us-west-1.amazonaws.com/salad/container-engine/images/yolov8-video-stream-2.gif" />

That is great, but our main goal is to get a summary of how long an object was present on the video. I will now remove
the appearing window with the bounding boxes and we will pay more attention to the data. For this part of the project we
are using Jupyter in vscode and pandas. Let’s check what results object is:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=2b35d3bcc855dd85f4c1c6afa7082eae" data-og-width="975" width="975" data-og-height="503" height="503" data-path="container-engine/images/yolov8-results-object.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=daeedb6e25a731d212f202f17054bb9a 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=9f24d70f9e88291e3630b11ba6a6a419 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=1ae6a3bde57540b09c5b73239de6a12a 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=dbd013a60068f99f009ee8dbb01e7842 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4063006e2a2269d91b0907778c3586c5 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-results-object.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=369cc87610a9b0391ca14ee7f90aeb6c 2500w" />

We can see that results object has some metadata and all the detections. Let’s only keep the detections and convert them
to a more readable format:

```python  theme={null}
json.loads(results[0].tojson())
```

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d9892d3f9ad1596e2c57bfe719941588" data-og-width="915" width="915" data-og-height="406" height="406" data-path="container-engine/images/yolov8-json-results-object.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=92789fa1714263693be5e5380fef4f6f 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=810e475dad77169ed5db504bc2968096 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=49b59156877565eb3bbee551ffc8c890 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=215488ef28bf8cb8b075d4acdb748867 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=944d7cab0bae24a1e7e00ef25da129d6 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-json-results-object.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=840843a2d50ec180b9881327f2bd6294 2500w" />

To get a detailed summary of object detections, we'll collate all the individual detection data into a pandas DataFrame.
We will not only include the basic detection details provided by YOLOv8, such as bounding box coordinates, class ID,
class name, and tracking ID, but also additional contextual information for a richer analysis.

**Calculating Additional Metrics:**

We defined a function to calculate the percentage of the frame that each detection occupies. Alongside this, we’ll
record the video link, frame timestamp, original frame shape, and the processing speed for each frame.

Here's how we'll assemble our results into a DataFrame and enrich it with the additional data:

```python  theme={null}
import datetime
import json
import pandas as pd

def calculate_percentage(bbox, original_shape):

    bbox_area = (bbox['x2'] - bbox['x1']) * (bbox['y2'] - bbox['y1'])

    original_shape_area = original_shape[0] * original_shape[1]

    percentage = (bbox_area / original_shape_area) * 100

    return percentage

# we will store all the results as a list of dictionaries
all_results = []

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        # Run YOLOv8 inference on the frame
        results = model.track(frame, persist=True)
        timestamp = datetime.datetime.now()
        # save every box with label
        for box in json.loads(results[0].tojson()):
            box["input"] = link
            box["timestamp"] = timestamp
            box["date"] = timestamp.strftime("%Y-%m-%d")
            box["time"] = timestamp.time().strftime("%H:%M:%S")
            box["origin_shape"] = results[0].orig_shape
            box["box_percentage"] = calculate_percentage(box["box"], results[0].orig_shape)

            box["full_process_speed"] = sum(results[0].speed.values())
            all_results.append(box)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            df = pd.DataFrame(all_results)
            break
```

After the loop is interrupted (by pressing 'q'), we convert the list of dictionaries into a pandas DataFrame. This
DataFrame will then contain a complete log of every detection across the video's frames, enriched with the additional
data points we've calculated.

Let’s see what we’ve got.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=2961d1d0bf4fdb074133b0315f61cde8" data-og-width="975" width="975" data-og-height="213" height="213" data-path="container-engine/images/yolov8-dataframe-results-object.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0433a4b743ea8f4225ff74a1233efd22 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0e8686b1d6f61638418aec37a5c86688 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=f90d8794b8bf98fdbf687faae5c73358 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a9aeb47967df761bd6282d1d477bb1ab 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=1771ed7ad23214c56425f02cb0dc4cec 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-dataframe-results-object.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=27675abc201bd119c6de10974bea9159 2500w" />

## Readable summary

With the DataFrame populated with tracking and detection data, we're now ready to create a summary that achieves our
main goal: calculating the duration each object was present in the video. We'll start by filtering out any irrelevant
data and then proceed to group the valid detections to summarize our findings.

**Filter data**

We need to ensure that we only include rows with valid tracking IDs. This means filtering out any detections that do not
have a tracking ID or where the tracking ID is 0, which may indicate an invalid detection or an object that wasn't
tracked consistently.

**Grouping Detections for Summary:**

With a DataFrame of filtered results, we'll group the data by tracking ID to find the earliest and latest timestamps for
each object. Our object will get a new tracking ID if it leaves and re-enters the video. If in your project you need to
track a specific label, you will need to add additional logic of grouping by class and summing the durations.

We'll also determine the most commonly assigned class for each object, in case there are discrepancies in classification
across frames, and calculate the average size of the object within the frame.

The **summary** function will perform these operations and output a readable string

```python  theme={null}
def summary(df, filename, result_blob):
    if (
        "track_id" in df.columns
        and df["track_id"].notna().any()
        and df["track_id"].ne(0).any()
    ):
        df_filtered = df[(df["track_id"] != 0) & (df["track_id"].notna())].copy()
        # Group by 'track_id' and calculate duration, most frequent class and
        # corresponding name for each group
        # Group by track_id and calculate average box_percentage, min and max timestamp
        summary_df = (
            df_filtered.groupby("track_id")
            .agg(
                average_box_percentage=("box_percentage", "mean"),
                min_timestamp=("timestamp", "min"),
                max_timestamp=("timestamp", "max"),
                most_common_class=(
                    "name",
                    lambda x: x.value_counts().index[0],
                ),  # Most common class per track_id
            )
            .reset_index()
        )
        # Calculate duration
        summary_df["duration"] = (
            summary_df["max_timestamp"] - summary_df["min_timestamp"]
        )

        # Convert the DataFrame to a string
        output_string = "\n".join(
            f"{row['most_common_class']} with id {row['track_id']} was present in the video for {row['duration']} from {row['min_timestamp']} to {row['max_timestamp']} and was taking  {row['average_box_percentage']:.2f}% of the screen"
            for _, row in summary_df.iterrows()
        )
    else:
        output_string = "No objects were detected in the video"

```

**Results:**

Executing the function will produce output like the following:

```text  theme={null}
person with id 1.0 was present in the video for 0 days 00:01:34.273634 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:26:30.139664 and was taking  8.28% of the screen
person with id 2.0 was present in the video for 0 days 00:00:52.874862 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:48.740892 and was taking  3.87% of the screen
person with id 3.0 was present in the video for 0 days 00:01:02.194742 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:58.060772 and was taking  6.97% of the screen
person with id 4.0 was present in the video for 0 days 00:00:13.343196 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:09.209226 and was taking  1.07% of the screen
person with id 5.0 was present in the video for 0 days 00:00:12.491371 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:08.357401 and was taking  1.42% of the screen
person with id 6.0 was present in the video for 0 days 00:00:37.937545 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:33.803575 and was taking  1.60% of the screen
person with id 7.0 was present in the video for 0 days 00:00:12.994483 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:08.860513 and was taking  2.12% of the screen
car with id 8.0 was present in the video for 0 days 00:00:05.370814 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:25:01.236844 and was taking  3.89% of the screen
car with id 9.0 was present in the video for 0 days 00:00:01.655127 from 2023-11-08 03:24:55.866030 to 2023-11-08 03:24:57.521157 and was taking  2.39% of the screen
```

## Run process on GPU

In our metadata Dataframe the last column “full\_process\_speed“ reflects a combination of preprocessing, inference and
post-processing time. We can see that now we have the processing speed from 60 to 400 milliseconds per frame which is
impressive, but we can do better. To unlock the full potential of our solution, we've added a simple enhancement: CUDA
device detection. With just a few lines of code, our process now intelligently determines if a CUDA-compatible GPU is
available and adjusts accordingly.:

```python  theme={null}
# Check for CUDA device and set it
device = "0" if torch.cuda.is_available() else "cpu"
if device == "0":
    torch.cuda.set_device(0)
```

This adjustment ensures that if the system has the capability, it will leverage the GPU, thus significantly boosting the
processing speed.

The results speak for themselves. After running a live stream through our enhanced process for about 40 minutes, we
observed a dramatic improvement in processing speed. The times dropped to a stunning 5 to 15 milliseconds per frame.
This enhancement means our YOLOv8 solution is now processing frames up to 10 times faster on a GPU compared to CPU
processing.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3dba9b1e25c5d127b2e8dddfa0c326d4" data-og-width="1283" width="1283" data-og-height="357" height="357" data-path="container-engine/images/yolov8-gpu-vs-cpu-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3078bc47b65f77cdf1b53a08837c2a46 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a610da15395fce82e9e35f8c537ab38e 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=8441ca390bbd15a528956439a7ea3224 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0d2ba867483512214a9213b4e646d9e4 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=bc0d04f9685b5a14bddc37f776845cdf 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-gpu-vs-cpu-table.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=95c818f2de9a31ee94d5a2531c6dbe87 2500w" />

**Files format and naming**

Next we need to save our and summary into a suitable format for storage, such as CSV, JSON, or plain text. We picked csv
for the DataFrame and txt for the summary. For Filename convention we use timestamp of when the process started and a
part of the incoming link. That helps us easily identify where the stream is coming from and make file name unique.

**Saving Results Incrementally:**

1. **Timed Saves**: We implement logic within the processing loop to save interim results at intervals that will be
   specified as environment variable. Since stream might be infinite we need to be able to check the results without
   breaking the connection to the stream.
2. **Final Save**: Ensure all results are saved once the process is completed:

Function to save our Dataframe to Azure container:

```Python  theme={null}
def save_df(df, filename, result_blob):
    results_csv_file_name = f"{filename}.csv"
    results_blob_client = result_blob.get_blob_client(results_csv_file_name)
    csv_stream = io.StringIO()
    df.to_csv(csv_stream, index=False)
    # Convert the CSV data to bytes
    csv_bytes = csv_stream.getvalue().encode("utf-8")
    results_blob_client.upload_blob(csv_bytes, overwrite=True)
```

Add this part of code to the summary function to save the summary results to azure:

```python  theme={null}
    results_txt_file_name = f"{filename}.txt"
    results_blob_client_txt = result_blob.get_blob_client(results_txt_file_name)
    results_blob_client_txt.upload_blob(output_string, overwrite=True)
```

## Integrating with Azure for batch processing

To enable efficient batch processing using YOLO on Salad, establishing a connection between the Python code and Azure
Storage resources is crucial. We will start with initiating and maintaining connections to containers and storage queue:

```python  theme={null}
from azure.storage.blob import ContainerClient
from azure.storage.queue import QueueClient

def connect_to_storage(storage_type: str, name: str, connection_str: str):
    """Connect to Azure Storage Container or Queue."""
    if storage_type.lower() == "container":
        client = ContainerClient
    elif storage_type.lower() == "queue":
        client = QueueClient
    else:
        raise ValueError("Storage type should be 'container' or 'queue'")

    return client.from_connection_string(connection_str, name)

def azure_initiate(input_blob, output_blob, storage_queue, storage_connection_string):
    request = connect_to_storage("container", input_blob, storage_connection_string)
    result = connect_to_storage("container", output_blob, storage_connection_string)
    queue = connect_to_storage("queue", storage_queue, storage_connection_string)

    return request, result, queue
```

To ensure continuous monitoring of the queue for new messages, we implement an infinite loop in our main processing
script. This loop will periodically check the queue for new messages, process them if available, and wait before
checking again if the queue is empty:

```Python  theme={null}
while True:
    queue_length = (
        request_queue_client.get_queue_properties().approximate_message_count
    )
    if queue_length > 0:
        queue_messages = request_queue_client.receive_messages()
    ...
    else:
        time.sleep(args.queue_check_timer)
```

Next our script will loop through messages in the Azure storage queue, decode the message, remove the message from queue
to ensure that multiple containers do not process the same message and read the file we’ve put in the requests storage
container. We'll specifically handle JSON files containing video links, along with metadata indicating whether each
video is pre-recorded or live:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=45c7c0b55b07693259981460920a9816" data-og-width="517" width="517" data-og-height="124" height="124" data-path="container-engine/images/yolov8-youtube-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6eab9ad7fee822c63288db678b63d5bc 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=50d9af9553f9d50e6f4ddcb1fa83326a 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=91c04dfc11614f642acfc20d3f1ffaa2 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d16bdfb8ba60b3ae8ca2fb2091393758 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d9682ca8c9c6a70504d3354579068973 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-youtube-metadata.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=7702e0e1ede47d26c723949da62d8944 2500w" />

Here is a link to the
[full script](https://github.com/SaladTechnologies/yolov8-on-salad/blob/main/src/python/batch/inference/batch.py)

## Environment Variables

When deploying a batch processing solution using YOLO on Salad, leveraging environment variables provides a flexible and
secure way to configure your application. These variables can be defined during the deployment process and accessed
within your container. Here's how you can integrate environment variables into your Python script for key
configurations:

```python  theme={null}
import argparse
parser = argparse.ArgumentParser()
        parser.add_argument(
            "--storage_connection_string",
            default=os.environ.get("STORAGE_CONNECTION_STRING"),
            type=str,
        ),
args = parser.parse_args()
```

In this example, the script retrieves the `STORAGE_CONNECTION_STRING` environment variable. If it's not set, it defaults
to `None`.

#### Environment Variables Table

|                             |                                                                                                                                                           |          |                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------- |
| Environment Variable Name   | Functionality                                                                                                                                             | Required | Default Value   |
| `STORAGE_CONNECTION_STRING` | Connection string for Azure Storage Account. Should be pulled from azure storage account access keys.                                                     | Yes      | None            |
| `INPUT_CONTAINER_NAME`      | Name of the input container in Azure Blob Storage where request files be saved to start the process. Value should match name of resource created in Azure | No       | "requests"      |
| `OUTPUT_CONTAINER_NAME`     | Name of the output container where the result files be saved to. Value should match name of resource created in Azure                                     | No       | "yolo-results"  |
| `INPUT_QUEUE_NAME`          | Name of the queue for incoming requests. Value should match name of resource created in Azure                                                             | No       | "requestsqueue" |
| `SAVE_EVERY_MINS`           | Interval for saving results (in minutes).                                                                                                                 | No       | 30              |
| `QUEUE_CHECK_TIMER`         | Interval for checking the queue (in seconds).                                                                                                             | No       | 60              |

This table provides an overview of the environment variables used in the script, outlining their purpose, whether they
are mandatory, and their default values if not explicitly set. This setup ensures that your batch processing application
can be tailored to specific needs and conditions of the deployment environment on Salad.

## Containerizing code with Docker

The next crucial step is to package our solution into a Docker image. This approach is key to facilitating deployment to
our cloud clusters. Containerizing with Docker not only streamlines the deployment process but also ensures that our
application runs reliably and consistently in the cloud environment, mirroring the conditions under which it was
developed and tested.

When creating the Dockerfile, it's crucial to select a base image that includes all the necessary system dependencies,
because that might cause some networking issues. We’ve tested our solution with “python3.9“ base image, so if possible
stick to it. If you have to use a different base image for any reason check out SaladCloud documentation on networking.
Here is the full Dockerfile we will use to build an image:

```Dockerfile  theme={null}
# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the inference folder to /app/inference
COPY /inference /app/inference

# Update pip and install requirements
RUN apt-get update && apt-get install -y git gcc python3-dev build-essential libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6
# RUN apt-get install -y socat
RUN python -m pip install pip==21.1.1
RUN pip install numpy
RUN pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
RUN pip install lap==0.4.0
RUN pip install --upgrade pip
RUN pip install  -r inference/requirements.txt

WORKDIR /app/inference

# Set the entrypoint to run inference.py
ENTRYPOINT ["python3.9", "batch.py"]
```

We’ve also put together a bash script to easily publish your image to azure container registry. The script is located
side by side with the Dockerfile in the git repo. You can use the following command to build and deploy your image:

```bash  theme={null}
bash docker.sh <image name> <image version> <acr name>
```

## Deploying Solution to Salad

We finally got to the last and most exiting part of our project. We will now deploy our full solution to the cloud.

Deploying your containerized application to SaladCloud's GPU Cloud is a very efficient and cost-effective way to run
your object detection solution. SaladCloud has a very user-friendly interface as well as an API for deployment. Let’s
deploy our solution using SaladCloud portal.

First create your account and log into [https://portal.salad.com/](https://portal.salad.com/) Create your organization and let’s deploy our container
app.

Under container groups click “Deploy a Container Group“:

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=52c15ce4638023369c6433afa9459b51" data-og-width="888" width="888" data-og-height="1140" height="1140" data-path="container-engine/images/create-container-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=ccd7e6c237feac0a2e643bd26febd556 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=0b2e01f717c5714c16cb8b070715778a 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=d74e87f3e12d3186849ee8c5d33b4ea1 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=09cda9194fdc8f26a185fbe23412eb17 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=9e2ff96b813f8a034a7e5234257ea42d 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/create-container-group.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=726db57a298c3a17632e76313f2363e6 2500w" />

We now need to set up all of our container group parameters:

**Configure Container Group:**

1. **Create a unique name for your Container group**

2. **Pick the Image Source:** In our case we are using a private Azure Container Registry. Click Edit next to Image
   source. Now switch to “Private Registry“, under “What Service Are You Using“ pick Azure Container Registry. Get back
   to your azure portal and find the image name, username and password of our container registry repository. Find your
   acr in azure and click “repositories“ on the left

   <img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=27ccd2000399f6def4b5690d27c7a7e8" data-og-width="1584" width="1584" data-og-height="1051" height="1051" data-path="container-engine/images/azure-container-registry-repositories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=9dff195e6c7653147acc738166323347 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=555df8077f470e6c447ce9d151e27990 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=6050d691197059ed9261546121ce46cd 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=48a814922654a6d1b73c55825aeb0bf9 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=be337c07368c9d45da693f9a211f243b 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/azure-container-registry-repositories.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4761ee7032800c1a8dd6b5eee65652b0 2500w" />

   Chose the image repository and click on the version you want to pull. Now under “Manifest“ you will see a Docker pull
   command in the followings format: `docker pull {image name}`:

   <img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=857cf9d2e56611298df7965b6fedc16f" data-og-width="1427" width="1427" data-og-height="171" height="171" data-path="container-engine/images/yolov8-azure-container-image-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=224c0a846b69b0c3a4f1cfd6169e82a1 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=020a5bb3091b189702f8a5a9e5ec0ed2 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=95a5f4875c05e643fb75053d91ff3b02 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4c7212d0d992a3763b2ae1a3b6eafc75 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=e89aa72be7efe5a866284299c6c3c0d6 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-container-image-name.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=506de101ccfb9611065ec0034d05055f 2500w" />

   Copy the “image name“ and paste back to SaladCloud portal. Now let’s find acr username and password back in azure
   portal. Get back to your azure container registry page and click Access keys on the left. If your “Admin user” is not
   enabled, do so. Now copy the username and password and pass it back to SaladCloud portal.

3. **Replica count**: This will define how many videos can be processed simultaneously. For example if we have 10
   containers we can put 10 files with links and they will all be picked up one by one.

4. **Pick compute resources:** That is the best part. Pick how much cpu, ram and gpu you want to allocate to your
   process. The prices are very low in comparison to all the other cloud solutions, so be creative.

5. **Environment variables:** This is where we need to add our environment variables we went through above. Specify them
   in a key-value format:

   <img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=bd00a6a4d991798398ac210e57b7760e" data-og-width="526" width="526" data-og-height="490" height="490" data-path="container-engine/images/environment-variables-portal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c1e63c620769c4b2186dab4fd1843c38 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3d6d9ddbfe80507d717ef8156f6357ba 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=4eb0f1a218e283bc7885751d179a095a 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=50b250b3537bd572cba74efc43a81bea 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=17b9747687f710324fbf50c104778563 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/environment-variables-portal.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=411599fbe80dedd41598ea7e77517e25 2500w" />

With everything in place, deploying your application on SaladCloud is just a few clicks away. By taking advantage of
SaladCloud's platform, you can ensure that your object detection API is running on reliable infrastructure that can
handle intensive tasks at a fraction of the cost. Now check “AutoStart container group once image is pulled“ and hit
“Deploy“. We are all set let’s wait till our solution deploys and test it.

## Benefits of Using Salad

* **Cost-Effectiveness**: SaladCloud offers GPU cloud solutions at a more affordable rate than many other cloud
  providers, allowing you to allocate more resources to your application for less.
* **Ease of Use**: With a focus on user experience, SaladCloud's interface is designed to be intuitive, removing the
  complexity from deploying and managing cloud-based applications.
* **Documentation and Support**: SaladCloud provides detailed documentation to assist with deployment, configuration,
  and troubleshooting, backed by a support team to help you when needed.

## Test Full Solution deployed to Salad

Once your solution deployed on SaladCloud you can put a file in the requests container and check the results.

Ones the video is processed 2 files will be saved to results container:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5d9202c0c28c46e7071b4d030d203877" data-og-width="975" width="975" data-og-height="64" height="64" data-path="container-engine/images/yolov8-azure-results-blob.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a2aa511b051821a89f90d457e487532c 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=8df3db8cd1a7bfcf492bc7c2fe4d1c2f 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=66afce9b4c5d37c46bb06ee0efba4866 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=070739aee585237128397f367e993f52 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=415f442d76431684911b5bd9041178a3 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-azure-results-blob.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=f76b28d9b1f7be309d15cfb5bd838d0f 2500w" />

And our solution is now deployed to cloud compute and successful writes the results to our storage account.

## Conclusions

Our journey into the realm of object detection using YOLOv8 and deploying it on SaladCloud's GPU cloud has been both
challenging and rewarding. We've successfully navigated through all stages of development and deployment of our
solution. Batch processing with SaladCloud is a great solution that can provide simultaneous processing of files
together with cost savings.

For those who might be interested we’ve also implemented **multithreading functionality** to our solution. With
multithreading you can process several streams simultaneously at one node by providing multiple links in the request
file:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=582295ec3862e707b2ba4412f1a5667a" data-og-width="508" width="508" data-og-height="336" height="336" data-path="container-engine/images/yolov8-batch-youtube-submit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=67bd6874aab4229f4430ecfbc1ce6f18 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=168fb04b28eadc869f2b635b21e0eed3 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=9a9413d952cf8cafb5a63821b0c3099a 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6786020ddd067fbe7a9aa65eba2b9e8f 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5634d96b1e1926934d08c2e633f31613 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolov8-batch-youtube-submit.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=3b7ce05b80bd5eb28bafe71b9e21fddb 2500w" />

Here is a link to the multi-threading
[code](https://github.com/SaladTechnologies/yolov8-on-salad/blob/main/src/python/batch/inference/batch-multi-thread.py)

If you are going to deploy the multi-threading solution, remember to change the python script name in the Dockerfile.
Also make sure you have right hardware configurations for the number of threads you want to run.
