# Source: https://docs.edgeimpulse.com/studio/projects/impulse-design.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Impulse design

After collecting data for your project, you can now create your **Impulse**. A complete Impulse will consist of 3 main building blocks: an *input block*, a *processing block* and a *learning block*. A project can contain multiple impulses, also known as [experiments](/studio/projects/experiments).

The Impulse view is one of the most important as an impulse represents the machine learning pipeline that will be packaged in one of the [deployments](/studio/projects/deployment) and run on your edge device. Example impulses are shown below.

**Impulse example for motion classification and anomaly detection (multi-model) using accelerometer data:**

<Frame caption="Completed impulse for accelerometer motion classification.">
  <img src="https://mintcdn.com/edgeimpulse/YmjKhgkCrlx3Nxh9/.assets/images/create-impulse-motion-anomaly.png?fit=max&auto=format&n=YmjKhgkCrlx3Nxh9&q=85&s=b5a7f2f178d6118820b768d1c93e8f23" width="1600" height="996" data-path=".assets/images/create-impulse-motion-anomaly.png" />
</Frame>

**Impulse example for motion classification using multi-label sample accelerometer data:**

<Frame caption="Completed impulse for multi-label sample accelerometer motion classification.">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/impulse-multi-label-sample-input-block.png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=88fb89bd55fd63f70e2f74061b9262a8" width="1445" height="722" data-path=".assets/images/impulse-multi-label-sample-input-block.png" />
</Frame>

**Impulse example for object detection using images:**

<Frame caption="Completed impulse for object detection.">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/db5e959-objectdetect03.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=602342768c74979f64f5f76f4100bce5" width="1363" height="470" data-path=".assets/images/db5e959-objectdetect03.png" />
</Frame>

### Input block

The input block indicates the type of input data you are training your model with. This can be time series (audio, vibration, movements) or images.

#### Time series (audio, vibration, movements)

* The *Input axes* field lists all the axis referenced from your training dataset.
* The *Window size* field is the amount of raw data from your sample that is used to generate features for model training.
* The *Window increase* field is used to determine the starting point for the next window.
* The *Frequency (Hz)* field is automatically calculated based on your training samples. Changing this value will downsample or upsample the raw data.
* The *Zero-pad data* field adds zero values when there is not enough raw data to fit the window size.

If your project contains multi-label samples, there will be another field.

* The *Handling multi-label samples* field allows you to configure which label is used for your window when it contains multiple labels.
  * `Use label at end of window`: Sets the window label to the label of the last data point in the window.
  * `Use label X if anywhere present in window`: Sets the window label to one of the selected label values if that label is found anywhere within the window. If multiple selected labels are found within the window, the selected label that is found the most within the window is used. If no checked labels are found within the window, the label at the end of the window is used.

Below is a sketch to summarize the role of window size and increase.

<Frame caption="Window size vs. window increase.">
  <img src="https://mintcdn.com/edgeimpulse/cMDYCG0TzQNU7yvn/.assets/images/window-size-vs-increase.png?fit=max&auto=format&n=cMDYCG0TzQNU7yvn&q=85&s=e3235a2ca52f792d0ef3e549aab4fb2b" width="1600" height="857" data-path=".assets/images/window-size-vs-increase.png" />
</Frame>

#### Images

* The *Input axes* field list all the axis referenced from your training set (image).
* The *Image width* and *Image height* fields set the dimensions for resizing the raw images.
* The *Resize mode* field sets the method for how the raw images are resized.
  * `Fit longest axis`: Add letterboxes (padding) to the shorter axis to match the aspect ratio of the target size.  Then downsample to the target size.
  * `Fit shortest axis`: Crop the longer axis to match the aspect ratio of the target size.  Then downsample to the target size.
  * `Squash`: Resize the image to the target size, without preserving the aspect ratio.  (This may distort the image)

### Processing blocks

A [processing block](/studio/projects/processing-blocks) is basically a feature extractor. It consists of DSP (Digital Signal Processing) operations that are used to extract features that our model learns on. These operations vary depending on the type of data used in your project.

You don't have much experience with DSP? No problem, Edge Impulse usually uses a star to indicate the most recommended processing block based on your input data as shown in the image below.

<Frame caption="Processing blocks available.">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/processing-blocks-create-impulse.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=2d1aa516e60e9ccd35ad25143f405c7c" width="763" height="1000" data-path=".assets/images/processing-blocks-create-impulse.png" />
</Frame>

In the case where the available processing blocks aren't suitable for your application, you can [build your own custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) and import into your project.

### Learning blocks

After adding your [processing block](/studio/projects/processing-blocks), it is now time to add a [learning block](/studio/projects/learning-blocks) to make your impulse complete. A learning block is simply a neural network that is trained to learn on your data.

[Learning blocks](/studio/projects/learning-blocks) vary depending on what you want your model to do and the type of data in your training dataset. Algorithms include: [classification](/studio/projects/learning-blocks/blocks/classification), [regression](/studio/projects/learning-blocks/blocks/regression), [anomaly detection](/studio/projects/learning-blocks/blocks/anomaly-detection-k-means), [image transfer learning](/studio/projects/learning-blocks/blocks/transfer-learning-images), [keyword spotting](/studio/projects/learning-blocks/blocks/transfer-learning-keyword) or [object detection](/studio/projects/learning-blocks/blocks/object-detection). You can also create your own [custom learning block](/studio/organizations/custom-blocks/custom-learning-blocks) (enterprise feature).

#### Learning blocks available with time-series projects

<Frame caption="Learning blocks available with time-series projects.">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/learning-blocks-create-impulse.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=40bcada888ee9e353ec9f83781ae51ef" width="1231" height="1000" data-path=".assets/images/learning-blocks-create-impulse.png" />
</Frame>

#### Learning blocks available with image projects

<Frame caption="Learning blocks available with image projects.">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/learning-blocks-create-impulse-images.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=0aa65c47f71f53453db1a1e48ecb0a20" width="1426" height="988" data-path=".assets/images/learning-blocks-create-impulse-images.png" />
</Frame>

#### Learning blocks available with object detection projects

<Frame caption="Learning blocks available with object detection projects.">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/learning-blocks-create-impulse-objects.png?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=83b38cc29eb80ad47150599acb26ccfa" width="1426" height="612" data-path=".assets/images/learning-blocks-create-impulse-objects.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).