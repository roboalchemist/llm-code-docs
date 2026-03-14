# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/object-detection-centroids.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Object detection with centroids

[FOMO (Faster Objects, More Objects)](/studio/projects/learning-blocks/blocks/object-detection/fomo) is a brand-new approach to run object detection models on constrained devices. FOMO is a ground-breaking algorithm that brings real-time object detection, tracking and counting to microcontrollers for the first time. **FOMO is 30 times faster than MobileNet SSD and can run under 200K of RAM.**

In this tutorial, we will explain how to count cars to estimate parking occupancy using FOMO.

View the finished project, including all data, signal processing and machine learning blocks here: [Car Parking Occupancy Detection - FOMO](https://studio.edgeimpulse.com/public/711906/latest).

<Info>
  **Limitations of FOMO**

  * FOMO does not output bounding boxes but will give you the object's location using centroids. Hence the size of the object is not available.
  * FOMO works better if the objects have a similar size.
  * Objects shouldn’t be too close to each other, although this can be optimized when increasing the image input resolution.

  If you need the size of the objects for your project, head to the default [object detection](/tutorials/end-to-end/object-detection-bounding-boxes). tutorial.
</Info>

### 1. Prerequisites

For this tutorial, you'll need a [supported device](/hardware).

If you don't have any of these devices, you can also upload an existing dataset through the [Uploader](/tools/clis/edge-impulse-cli/uploader) or use your [mobile phone](/hardware/devices/mobile-phone) to connect your device to Edge Impulse. After this tutorial, you can then deploy your trained machine learning model as a C++ library or as a WebAssembly package and run it on your device.

### 2. Building a dataset

#### Capturing data

You can collect data from the following devices:

* [Collecting image data from the Studio](/tutorials/topics/data/collect-image-data-studio) - for the Raspberry Pi 4 and the Jetson Nano.
* [Collecting image data with your mobile phone](/tutorials/topics/data/collect-image-data-phone)
* Collecting image data from any of the [fully-supported development boards](/hardware) that have a camera.

Alternatively, you can capture your images using another camera, and then upload them directly from the studio by going to **Data acquisition** and clicking the 'Upload' icon or using Edge Impulse CLI [Uploader](/tools/clis/edge-impulse-cli/uploader).

With the data collected, we need to label this data. Go to **Data acquisition**, verify that you see your data, then click on the 'Labeling queue' to start labeling.

#### Labeling data

<Info>
  **Why use bounding box inputs?**

  To keep the interoperability with other models, your training image input will use bounding boxes although we will output centroids in the inference process. As such FOMO will use in the background translation between bounding boxes and segmentation maps in various parts of the end-to-end flow. This includes comparing sets between the bounding boxes and the segmentation maps to run profiling and scoring.
</Info>

All our collected images will be staged for annotation at the "labeling queue". Labeling your objects is as easy as dragging a box around the object, and entering a label. However, when you have a lot of images, this manual annotation method can become tiresome and time consuming. To make this task even easier, Edge impulse provides [3 AI assisted labeling](https://edgeimpulse.com/blog/3-ways-to-do-ai-assisted-labeling-for-object-detection) methods that can help you save time and energy. The AI assisted labeling techniques include:

* Using YoloV5 - Useful when your objects are part of the common objects in the [COCO dataset](https://cocodataset.org/#home).
* Using your own trained model - Useful when you already have a trained model with classes similar to your new task.
* Using Object tracking - Useful when you have objects that are similar in size and common between images/frames.

For our case, since the 'car' object is part of the COCO dataset, we will use the YoloV5 pre-trained model to accelerate this process. To enable this feature, we will first click the Label suggestions dropdown,then select “Classify using YOLOv5.”

<Frame caption="YoloV5 AI Assisted labelling">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/503f3af-ai.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=362cfe5df5844a5bf318e13c9bbfba09" width="985" height="631" data-path=".assets/images/503f3af-ai.png" />
</Frame>

From the image above, the YOLOV5 model can already help us annotate more than 90% of the cars without us having to do it manually by our hands.

#### Rebalancing your dataset

To validate whether a model works well you want to keep some data (typically 20%) aside, and don't use it to build your model, but only to validate the model. This is called the 'test set'. You can switch between your training and test sets with the two buttons above the 'Data collected' widget. If you've collected data on your development board there might be no data in the testing set yet. You can fix this by going to **Dashboard > Perform train/test split**.

### 3. Designing an impulse

One of the beauties of FOMO is its fully convolutional nature, which means that just the ratio is set. Thus, it gives you more flexibility in its usage compared to the classical [object detection](/tutorials/end-to-end/object-detection-bounding-boxes). method. For this tutorial, we have been using **96x96 images** but it will accept other resolutions as long as the images are square.

To configure this, go to Create impulse, set the image width and image height to 96, the 'resize mode' to Fit shortest axis and add the 'Images' and 'Object Detection (Images)' blocks. Then click **Save Impulse**.

<Frame caption="96\*96 input image size">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/impulse.PNG?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=a8fba6d8c5feaff6980f44b7d0e4452a" width="1127" height="588" data-path=".assets/images/impulse.PNG" />
</Frame>

#### Configuring the processing block

To configure your processing block, click Images in the menu on the left. This will show you the raw data on top of the screen (you can select other files via the drop-down menu), and the results of the processing step on the right. You can use the options to switch between `RGB` and `Grayscale` modes. Finally, click on **Save parameters**.

<Frame caption="Configuring the processing block">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/raw.PNG?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=15319a4be865725b3043957bbb9294b5" width="1354" height="620" data-path=".assets/images/raw.PNG" />
</Frame>

This will send you to the 'Feature generation' screen. In here you'll:

* Resize all the data.
* Apply the processing block on all this data.
* Create a 3D visualization of your complete dataset.
* Click Generate features to start the process.

Afterward, the **Feature explorer** will load. This is a plot of all the data in your dataset. Because images have a lot of dimensions (here: 96x96x1=9216 features for grayscale) we run a process called 'dimensionality reduction' on the dataset before visualizing this. Here the 9216 features are compressed down to 2, and then clustered based on similarity as shown in the feature explorer below.

<Frame caption="Feature explorer">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-fomo-feature-explorer.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=65adc504d9f6d3aab50a745304007193" width="1052" height="1000" data-path=".assets/images/studio-fomo-feature-explorer.png" />
</Frame>

#### Configuring the object detection model with FOMO

With all data processed it's time to start training our FOMO model. The model will take an image as input and output objects detected using centroids. For our case, it will show centroids of cars detected on the images.

FOMO is fully compatible with any MobileNetV2 model, and depending on where the model needs to run you can pick a model with a higher or lower alpha. Transfer learning also works (although you need to train your base models specifically with FOMO in mind). Another advantage of FOMO is that it has very few parameters to learn from compared to normal SSD networks making the network even much smaller and faster to train. Together this gives FOMO the capabilities to scale from the smallest microcontrollers to full gateways or GPUs.

To configure FOMO, head over to the ‘**Object detection**’ section, and select '**Choose a different model**' then select one of the FOMO models as shown in the image below.

<Frame caption="Selecting FOMO model">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/ecdcc66-fom1.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=9af93bf70c4c1237f455388adbadecee" width="883" height="641" data-path=".assets/images/ecdcc66-fom1.png" />
</Frame>

Make sure to start with a **learning rate of 0.001** then click start training. After the model is done you'll see accuracy numbers below the training output. You have now trained your FOMO object detection model!

<Frame caption="Training results">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d47241d-eval.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=b49a141f8b9b29af3fb195a9fcfb4168" width="478" height="505" data-path=".assets/images/d47241d-eval.png" />
</Frame>

As you may have noticed from the training results above, FOMO uses **F1 Score** as its base evaluating metric as compared to SSD MobileNetV2 which uses Mean Average Precision (mAP). Using Mean Average Precision (mAP) as the sole evaluation metric can sometimes give limited insights into the model’s performance. This is particularly true when dealing with datasets with imbalanced classes as it only measures how accurate the predictions are without putting into account how good or bad the model is for each class. The combination between F1 score and a confusion matrix gives us both the balance between precision and recall of our model as well as how the model performs for each class.

### 4. Validating your model

With the model trained let's try it out on some test data. When collecting the data we split the data up between a training and a testing dataset. The model was trained only on the training data, and thus we can use the data in the testing dataset to validate how well the model will work in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence. To validate our model, we will go to **Model Testing** and select **Classify all**.

<Frame caption="Model testing results">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2577da3-test.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=b64f152a729053021092c12c046a87fa" width="992" height="472" data-path=".assets/images/2577da3-test.png" />
</Frame>

Given the little training data we had and the few cycles we trained on, we got an accuracy of **84.62%** which can be improved further. To see the classification in detail, we will head to *Live Classification*\* and select one image from our test sample. Click the three dots next to an item, and select Show classification. We can also capture new data directly from your development board from here.

##### Live Classification Result

<Frame caption="Live Classification - Side by Side">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-side-by-side.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=3c5c03cd78a0710906bdc7a4979f03ae" width="1600" height="826" data-path=".assets/images/fomo-side-by-side.png" />
</Frame>

From the test image above, our model was able to detect 16 cars out of the actual possible 18 which is a good performance. This can be seen in side by side by default, but you can also switch to overlay mode to see the model's predictions against the actual image content.

##### Overlay Mode for the Live Classification Result

<Frame caption="Live Classification - Overlay">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-overlay.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=324a4706830131c252f51adca73ebbb4" width="1600" height="826" data-path=".assets/images/fomo-overlay.png" />
</Frame>

A display option where the original image and the model's detections overlap, providing a clear juxtaposition of the model's predictions against the actual image content.

##### Summary Table

<Frame caption="Summary Table">
  <img src="https://mintcdn.com/edgeimpulse/8gSv6x4dEVbIP2Vj/.assets/images/fomo-predictions-right.png?fit=max&auto=format&n=8gSv6x4dEVbIP2Vj&q=85&s=97abae0ff12efe43733291e85789bf09" width="1600" height="826" data-path=".assets/images/fomo-predictions-right.png" />
</Frame>

The summary table for a FOMO classification result provides a concise overview of the model's performance on a specific sample file, such as 'Parking\_data\_2283.png.2tk8c1on'. This table is organized as follows:

**CATEGORY:** Metric, Object category, or class label, e.g., car.
**COUNT:** Shows detection accuracy, frequency, e.g., car detected 7 times.

**INFO:** Provides performance metrics definitions, including F1 Score, Precision, and Recall, which offer insights into the model's accuracy and efficacy in detection:

**Table Metrics**
**F1 Score:** (77.78%): Balances precision and recall.
**Precision:** (100.00%): Accuracy of correct predictions.
**Recall:** (63.64%): Proportion of actual objects detected.

##### Viewing Options

Bottom-right controls adjust the visibility of ground truth labels and model predictions, enhancing the analysis of the model's performance:

**Prediction Controls:** Customize the display of model predictions, including:

* Show All: Show all detections and confidence scores.
* Show Correct Only: Focus on accurate model predictions.
* Show incorrect only: Pinpoint undetected objects in the ground truth.

**Ground Truth Controls:** Toggle the visibility of original labels for direct comparison with model predictions.

* Show All: Display all ground truth labels.
* Hide All: Conceal all ground truth labels.
* Show detected only: Highlight ground truth labels detected by the model.
* Show undetected only: Identify ground truth labels missed by the model.

### 5. Running the model on your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the preprocessing steps, neural network weights, and classification code - in a single C++ library or model file that you can include in your embedded software.

#### Running the impulse on a Linux-based device

From the terminal just run `edge-impulse-linux-runner`. This will build and download your model, and then run it on your development board. If you're on the same network you can get a view of the camera, and the classification results directly from your dev board. You'll see a line like:

```
Want to see a feed of the camera and live classification in your browser? Go to http://192.168.8.117:4912
```

Open this URL in a browser to see your impulse running!

<Frame caption="Running FOMO object detection on a Raspberry Pi 4">
  <img src="https://mintcdn.com/edgeimpulse/M1w1EVa0Cr_xPADa/.assets/images/b743a20-fomokim.png?fit=max&auto=format&n=M1w1EVa0Cr_xPADa&q=85&s=a0dfe044a8d65bf930d45797025d3570" width="1103" height="589" data-path=".assets/images/b743a20-fomokim.png" />
</Frame>

#### Running the impulse on a fully supported MCU

Go to the **Deployment tab**, on **Build firmware** section and select the board-compatible firmware to download it.

<Frame caption="Compiling firmware for Arduino Portenta H7">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f3ef00b-Screenshot_2022-03-30_at_15.05.37.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=b689543109e5cff7895effd5cc8cc1cc" width="1600" height="827" data-path=".assets/images/f3ef00b-Screenshot_2022-03-30_at_15.05.37.png" />
</Frame>

Follow the instruction provided to flash the firmware to your board and head over to your terminal and run the `edge-impulse-run-impulse --debug` command:

<Frame caption="Running impulse using edgeimpulse CLI on terminal">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/162b3e9-757421b-Selection_019_1.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=f457945beb95d9df72f4f43bd34f6426" width="1306" height="686" data-path=".assets/images/162b3e9-757421b-Selection_019_1.png" />
</Frame>

You'll also see a URL you can use to view the image stream and results in your browser:

```
Want to see a feed of the camera and live classification in your browser? Go to http://192.168.8.117:4912
```

#### Running the impulse using a generated Arduino Library

To run using an Arduino library, go to the studio **Deployment tab** on **Create Library** section and select **Arduino Library** to download your custom Arduino library. Go to your Arduino IDE, then click on **Sketch** >> **Include Library** >> **Add .Zip** ( Your downloaded Arduino library). Make sure to follow the instruction provided on [Arduino's Library usage](/hardware/deployments/run-arduino-2-0). **Open Examples** >> **Examples from custom library** and select your library. Upload the ''Portenta\_H7\_camera'' sketch to your Portenta then open your serial monitor to view results.

<Frame caption="Running FOMO model using Arduino Library">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/8547014-portfomo.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=6f1d74d7f86f965fe674510d9e15cc8d" width="1300" height="701" data-path=".assets/images/8547014-portfomo.png" />
</Frame>

#### Integrating the model in your own application

Congratulations! You've added object detection using FOMO to your sensors. Now that you've trained your model you can integrate your impulse in the firmware of your own edge device, see [Deploy your model as a C++ library](/hardware/deployments/run-cpp) or the [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) documentation for the Node.js, Python, Go and C++ SDKs that let you do this in a few lines of code and make this model run on any device.

[Here's an example of sending a text message through Twilio](https://github.com/edgeimpulse/example-linux-with-twilio) when an object is seen.

Or if you're interested in more, see our tutorials on [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) or [Image classification](/tutorials/end-to-end/image-classification). If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).