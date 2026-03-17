# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/build-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/build-a-workflow.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/build-a-workflow.md

# Source: https://docs.roboflow.com/workflows/build-a-workflow.md

# Build a Workflow

A workflow is made up of blocks, which perform specific tasks, such running model inference, performing logic, or interfacing with external services.

For a deeper dive on the list of available block, view our [block documentation](https://inference.roboflow.com/workflows/blocks/).

### Overview

This guide will go over creating a four block workflow to run an object detection model, count predictions, and visualize the model results. Here’s the [final workflow template](https://app.roboflow.com/workflows/embed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3JrZmxvd0lkIjoiMmdqakJxMDV3Q01ac1hHM3hkeFAiLCJ3b3Jrc3BhY2VJZCI6ImtyT1RBYm5jRmhvUU1DZExPbGU0IiwidXNlcklkIjoiSW1GTElaU2tHYk55OXpiNFV1cWxNelBScHBRMiIsImlhdCI6MTczODE4ODk5MH0.f72WI5bdjtnwC8iqXF_XiUVarfOktIAH1egpsI0Oh4Q) to follow along.

{% embed url="<https://app.roboflow.com/workflows/embed/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3JrZmxvd0lkIjoiMmdqakJxMDV3Q01ac1hHM3hkeFAiLCJ3b3Jrc3BhY2VJZCI6ImtyT1RBYm5jRmhvUU1DZExPbGU0IiwidXNlcklkIjoiSW1GTElaU2tHYk55OXpiNFV1cWxNelBScHBRMiIsImlhdCI6MTczODE4ODk5MH0.f72WI5bdjtnwC8iqXF_XiUVarfOktIAH1egpsI0Oh4Q>" fullWidth="false" %}

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3320b2627ac743a17afb97f63c70993b4cbe3b51%2FCleanShot%202025-01-29%20at%2015.25.03%402x.png?alt=media" alt="" width="563"><figcaption><p>Detect, Count, and Visualize Workflow</p></figcaption></figure>

### Block Connections

Before we start building, it's important to understand how block connections work.

To add a block in a location, it has to use the previous block as an input. For example, in the workflow shown above, the *Property Definition* block comes after the *Object Detection* block since it uses the model block as an input. The *Bounding Box Visualization* block is to the right, since it doesn't use the output of the *Property Definition* block, but does reference the model output.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-79fa8c10219b4a7e8e0696acceae5e297f05f70f%2FCleanShot%202025-01-29%20at%2016.31.28%402x.png?alt=media" alt=""><figcaption><p>Model Comparison Workflow</p></figcaption></figure>

In the example workflow above, we have four distinct pathways, since each branch executes in parallel at runtime, and doesn't rely on the other branch blocks as inputs.

### Building a Workflow

#### Object Detection Model

First, add an *Object Detection Model* block. You can choose between a public pre-trained model, such as YOLOv8n trained on [COCO](https://universe.roboflow.com/microsoft/coco), or a fine-tuned model in your workspace. I’ll go ahead with the pre-trained *yolov8n* model to detect people and vehicles.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-bc18512f57a057976473b7d03cc7ee3a884e67e3%2FCleanShot%202025-01-29%20at%2015.30.31%402x.png?alt=media" alt="" width="344"><figcaption></figcaption></figure>

The object detection block has a required image parameter that determines what the model is inferring on. There are several optional parameters, the core ones are described in detail below:

* Class Filter: List of classes that the model will return. Note: the model will always only return classes it’s trained on, this allows you to filter out unneeded classes.
* Confidence: objects below that confidence will not be returned.
* IoU threshold: a higher threshold will return more overlapping predictions. 0.9 means that objects with 90% or less overlap will be returned, while 0.1 means objects with more than 10% overlap will not be included.
* Max Detections: the maximum number of objects the model will return
* Class Agnostic NMS: whether overlap filtering should compare and exclude objects with just the same class, or all classes

#### Property Definition

The property definition block allows you to extract relevant information from your data, such as the image size, predicted classes, or number of detected objects. For this example, we’ll be counting the number of objects found by the object detection model.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXc507UbRnkEH6XMdrfmwVZbHcK6x6K5THwnt1RmEk8iXSojwvmiA_q6KwRXV9bJudYnW7NMTQKKb9GqGxm_P0VjbuOoGWcDsM5NoQckl9jV4YcjYQFIvYoCgvd_YnQTNJLlwdbZwA?key=yGJPQzp1abf4J7pT0mnBw8w4" alt="" width="375"><figcaption></figcaption></figure>

For the *Data* property, reference the model predictions. For the *Operations*, select Count Items. This configuration will return the number of predictions made by the object detection model.

#### Bounding Box Visualization

Add a bounding box visualization block to visualize the model results. For the *image* parameter, select the input image. For the predictions, select the model results. You can optionally change the color and size of the bounding boxes using the optional configuration properties.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c02309fdf720d80b86c1de59ed126c7b7d9a2f9d%2FCleanShot%202025-01-29%20at%2015.31.50%402x.png?alt=media" alt="" width="342"><figcaption></figcaption></figure>

#### Label Visualization

In addition to drawing bounding boxes, we’ll also want to display the class names of the predictions. To do this, add a *Label Visualization* block after the bounding box visualization. In order to draw both bounding boxes and labels on the same image, you’ll want to set the reference input image as the *bounding\_box\_visualization* image, instead of referencing the input image. This will draw the labels on top of the bounding boxes.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cdcb7551292e790e706a1451b75bd3dcca6b28eb%2FCleanShot%202025-01-29%20at%2016.17.06%402x.png?alt=media" alt="" width="343"><figcaption></figcaption></figure>

You can change the optional *Text* parameter to change the display text from class name, to confidence, to class name and confidence.

### Save Changes

When you have finished building your Workflow, click "Save Workflow." If you have deployed the Workflow, your saved Workflow will start running on all devices where the Workflow has been deployed.

Now that you have a completed workflow, it's time to test it.
