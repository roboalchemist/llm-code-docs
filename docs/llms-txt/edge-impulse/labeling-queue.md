# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/labeling-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Labeling queue

In object detection projects, labeling is the process of defining regions of interest in the image frame. Manually labeling images can become tedious and time-consuming, especially when dealing with large datasets. This is why Edge Impulse Studio provides an AI-assisted labeling tool to help you in your labeling workflows.

The **Labeling queue** streamlines the process of defining bounding boxes for your dataset. Other types of image annotations, such as segmentation masks, are not supported. Only images that have not yet been labelled will be shown in the queue.

To access the Labeling queue, go to the **Data acquisition** page and click on the Labeling queue tab.

<Info>
  **Can't see the labeling queue?**

  To use the Labeling queue, you will need to set your project to an "object detection" project. Go to the project Dashboard and under "Project info > Labeling method" select `Bounding boxes (object detection)`.
</Info>

<Frame caption="Labeling queue tab on Data acquisition page.">
  <img src="https://mintcdn.com/edgeimpulse/vaoj7REk_f18Kg-b/.assets/images/studio-labeling-queue.png?fit=max&auto=format&n=vaoj7REk_f18Kg-b&q=85&s=5595b0aa0ea08d5cca43b29e5d59667f" width="1600" height="956" data-path=".assets/images/studio-labeling-queue.png" />
</Frame>

## AI-assisted labeling

<Info>
  **Already have a labeled dataset?**

  If you already have a labeled dataset containing bounding boxes, you can use the [uploader](/tools/clis/edge-impulse-cli/uploader#bounding-boxes) to import your data.
</Info>

The labeling queue supports four different operation modes:

* Track objects between frames
* Classify using YOLOv5
* Classify using YOLO-Pro
* Classify using your current impulse
* Classify using any pretrained object detection model

### Track objects between frames

If you have objects that are a similar size or common between images, you can also track your objects between frames within the Edge Impulse Labeling Queue, reducing the amount of time needed to re-label and re-draw bounding boxes over your entire dataset.

Draw your bounding boxes and label your images, then, after clicking Save labels, the objects will be tracked from frame to frame:

<Frame caption="Tracking objects between frames.">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-queue-tracking-frames.gif?s=3955f1b24b5bdd4a99f685b3942933f7" width="800" height="450" data-path=".assets/images/labeling-queue-tracking-frames.gif" />
</Frame>

Now that your object detection project contains a fully labeled dataset, learn how to train and deploy your model to your edge device: check out our tutorial!

We are excited to see what you build with the AI-Assisted Labeling feature in Edge Impulse, please post your project on our forum or tag us on social media, @EdgeImpulse!

### Classify using YOLOv5

Common objects in your images can quickly be identified and labeled in seconds without needing to write any code by using a pre-trained YOLOv5 object detection model, trained on 80 classes from the COCO dataset.

To label your objects with YOLOv5, click the Label suggestions dropdown and select “Classify using YOLOv5.” If your object is more specific than what is auto-labeled by YOLOv5, e.g. “coffee” instead of the generic “cup” class, you can modify the auto-generated labels.

<Frame caption="Classifying objects using YOLOv5.">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-queue-using-yolov5.gif?s=c47acade388cb0b89f48a0cf841f2d97" width="800" height="450" data-path=".assets/images/labeling-queue-using-yolov5.gif" />
</Frame>

Click Save labels to move on to your next raw image, and see your fully labeled dataset ready for training in minutes!

### Classify using YOLO-Pro

To identify a greater number of objects than YOLOv5, a pre-trained YOLO-Pro object detection model has been made available in the labeling queue. This YOLO-Pro model was trained on 589 classes from the Open Images Dataset (11 of the 600 classes were left out due to having too few images).

To use YOLO-Pro for labeling, click the Label suggestions dropdown and select “Classify using YOLO-Pro.” The model will automatically suggest bounding boxes and class labels for objects in your images, leveraging its extensive class library. If your object is more specific than what is auto-labeled by YOLO-Pro, e.g. “coffee” instead of the generic “cup” class, you can modify the auto-generated labels.

<Frame caption="Classifying objects using YOLO-Pro.">
  <img src="https://mintcdn.com/edgeimpulse/ZGWFGdLEqJWn-YyK/.assets/images/labeling-queue-using-yolopro.png?fit=max&auto=format&n=ZGWFGdLEqJWn-YyK&q=85&s=446e7aefade13d43f2ac1778618dd20e" width="1538" height="1000" data-path=".assets/images/labeling-queue-using-yolopro.png" />
</Frame>

Click Save labels to move on to your next raw image, and quickly build a fully labeled dataset with the help of YOLO-Pro’s broad object recognition capabilities.

### Classify using your current impulse

You can also use your own trained model to predict and label your new images. From an existing (trained) Edge Impulse object detection project, upload new unlabeled images from the Data Acquisition tab.

<Info>
  Currently, this only works with models trained with MobileNet SSD transfer learning.
</Info>

From the “Labeling queue”, click the Label suggestions dropdown and select “Classify using ”:

<Frame caption="Classifying objects using your current impulse.">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-queue-using-current-impulse.png?fit=max&auto=format&n=BkCfxv-ghnIJglm7&q=85&s=6430e1df976fd37b857e53b990e27100" width="1083" height="1000" data-path=".assets/images/labeling-queue-using-current-impulse.png" />
</Frame>

You can also upload a few samples to a new object detection project, train a model, then upload more samples to the Data Acquisition tab and use the AI-Assisted Labeling feature for the rest of your dataset. Classifying using your own trained model is especially useful for objects that are not in YOLOv5, such as industrial objects, etc.

Click Save labels to move on to your next raw image, and see your fully labeled dataset ready for training in minutes using your own pre-trained model!

### Classify using any pretrained object detection model

*This only works with object detection models outputting bounding boxes. Centroid-based models (such as FOMO) won't work.*

To label using a pretrained objection model:

1. Create a new (second) Edge Impulse project.
2. Choose Upload your model.
3. Select your model file (e.g. in ONNX or TFLite format), tell a bit about your model, and verify that the model gives correct suggestions via "Check model behavior".

<Frame caption="Verifying that an uploaded model gives correct suggestions.">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-queue-using-pretrained-model-1.png?fit=max&auto=format&n=BkCfxv-ghnIJglm7&q=85&s=f76a58f4643f09a5481c606820ac1747" width="1600" height="917" data-path=".assets/images/labeling-queue-using-pretrained-model-1.png" />
</Frame>

4. Click Save model.

While still in this (second) project:

1. Go to **Data acquisition** and upload your unlabeled dataset.
2. Click **Labeling queue**, and under 'Label suggestions' choose "Classify using 'your project name'". You now get suggestions based on your uploaded model:

<Frame caption="Classifying objects using a pretrained model.">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-queue-using-pretrained-model-2.png?fit=max&auto=format&n=BkCfxv-ghnIJglm7&q=85&s=8208b4cdefb935a4c6fa0607bdc4fd4b" width="1258" height="966" data-path=".assets/images/labeling-queue-using-pretrained-model-2.png" />
</Frame>

3. When you're done labeling, go to **Data acquisition > Export data** and export your (now labeled) dataset.
4. Import the labeled dataset into your original project.


Built with [Mintlify](https://mintlify.com).