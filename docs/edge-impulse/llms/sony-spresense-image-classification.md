# Source: https://docs.edgeimpulse.com/tutorials/hardware/sony-spresense-image-classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sony Spresense - image classification

In this tutorial, you'll use machine learning to build a system that can recognize objects in your house through your Sony Spresense - a task known as *image classification* - connected to your device. Adding sight to your embedded devices can make them see the difference between poachers and elephants, do quality control on factory lines, or let your RC cars drive themselves. In this tutorial you'll learn how to collect images for a well-balanced dataset, how to apply transfer learning to train a neural network, and deploy the system to your Spresense.

At the end of this tutorial, you'll have a firm understanding of how to classify images using Edge Impulse.

You can view the finished project, including all data, signal processing and machine learning blocks here: [Tutorial: adding sight to your sensors](https://studio.edgeimpulse.com/public/14227/latest).

### 1. Prerequisites

For this tutorial you'll need a Sony's Spresense with camera add-on.

If you don't have a device yet, you can also upload an existing dataset through the [Uploader](/tools/clis/edge-impulse-cli/uploader). After this tutorial you can then deploy your trained machine learning model as a C++ library and run it on your device by following the [Run on Sony Spresense](/hardware/deployments/run-cpp-sony-spresense) tutorial.

You also may want to create a new Edge Impulse project for this tutorial, or use an existing one. You can create a new project on your [project dashboard](https://studio.edgeimpulse.com/studio/select-project)

### 2. Building a dataset

In this tutorial we'll build a model that can distinguish between two objects in your house - we've used a plant and a lamp, but feel free to pick two other objects. To make your machine learning model see it's important that you capture a lot of example images of these objects. When training the model these example images are used to let the model distinguish between them. Because there are (hopefully) a lot more objects in your house than just lamps or plants, you also need to capture images that are *neither* a lamp or a plant to make the model work well.

Capture the following amount of data - make sure you capture a wide variety of angles and zoom levels:

* 50 images of a lamp.
* 50 images of a plant.
* 50 images of neither a plant nor a lamp - make sure to capture a wide variation of random objects in the same room as your lamp or plant.

You can collect data from your Spresense using the Edge Impulse CLI. Make sure you followed the [Getting Started](/hardware/boards/sony-spresense) guide for the Spresense, then run the edge impulse daemon.

```
edge-impulse-daemon --clean
```

Once connected follow the guide on [Collecting Image Data from Studio](/tutorials/topics/data/collect-image-data-studio) to build your dataset. Alternatively, you can capture your images using another camera, and then upload them by going to **Data acquisition** and clicking the 'Upload' icon.

Afterwards you should have a well-balanced dataset listed under **Data acquisition** in your Edge Impulse project. You can switch between your training and testing data with the two buttons above the 'Data collected' widget.

<Frame caption="Data acquisition showing images of a plant. Data is automatically split in a training and a test set when collecting, thus showing the 221 items in the training set here.">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/eda0014-screen_shot_2021-03-08_at_13011_pm.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=1cce5c8ca9e562ef5c760d40b0c376be" width="1600" height="830" data-path=".assets/images/eda0014-screen_shot_2021-03-08_at_13011_pm.png" />
</Frame>

### 3. Designing an impulse

With the training set in place you can design an impulse. An impulse takes the raw data, adjusts the image size, uses a preprocessing block to manipulate the image, and then uses a learning block to classify new data. Preprocessing blocks always return the same values for the same input (e.g. convert a color image into a grayscale one), while learning blocks learn from past experiences.

For this tutorial we'll use the 'Images' preprocessing block. This block takes in the color image, optionally makes the image grayscale, and then turns the data into a features array. If you want to do more interesting preprocessing steps - like finding faces in a photo before feeding the image into the network -, see the [Building custom processing blocks](/tutorials/topics/feature-extraction/build-custom-processing-blocks) tutorial. Then we'll use a 'Transfer Learning' learning block, which takes all the images in and learns to distinguish between the three ('plant', 'lamp', 'unknown') classes.

In the studio go to **Create impulse**, set the image width and image height to `96`, and add the 'Images' and 'Transfer Learning (Images)' blocks. Then click Save impulse.

<Frame caption="Designing an impulse">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f3dbcae-screenshot_2020-10-07_at_120923.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=dde3682d27b76c8290ce64d0ce094bb0" width="1305" height="470" data-path=".assets/images/f3dbcae-screenshot_2020-10-07_at_120923.png" />
</Frame>

#### Configuring the processing block

To configure your processing block, click **Images** in the menu on the left. This will show you the raw data on top of the screen (you can select other files via the drop down menu), and the results of the processing step on the right. You can use the options to switch between 'RGB' and 'Grayscale' mode, but for now leave the color depth on 'RGB' and click **Save parameters**.

<Frame caption="Configuring the processing block.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/93f5ca8-screen_shot_2021-03-08_at_12913_pm.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=906659c5f4f09c38f155e4b93d5ce8bc" width="1600" height="926" data-path=".assets/images/93f5ca8-screen_shot_2021-03-08_at_12913_pm.png" />
</Frame>

This will send you to the 'Feature generation' screen. In here you'll:

* Resize all the data.
* Apply the processing block on all this data.
* Create a 3D visualization of your complete dataset.

Click **Generate features** to start the process.

Afterwards the 'Feature explorer' will load. This is a plot of all the data in your dataset. Because images have a lot of dimensions (here: 96x96x3=27,648 features) we run a process called 'dimensionality reduction' on the dataset before visualizing this. Here the 27,648 features are compressed down to just 3, and then clustered based on similarity. Even though we have little data you can already see some clusters forming (lamp images are all on the right), and can click on the dots to see which image belongs to which dot.

<Frame caption="The feature explorer visualizing the data in the dataset. Clusters that separate well in the feature explorer will be easier to learn for the machine learning model.">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/od-feature-explorer-2d.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=0aac0227905477bea8d2195649da94d7" width="799" height="702" data-path=".assets/images/od-feature-explorer-2d.png" />
</Frame>

#### Configuring the transfer learning model

With all data processed it's time to start training a neural network. Neural networks are a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns. The network that we're training here will take the image data as an input, and try to map this to one of the three classes.

It's very hard to build a good working computer vision model from scratch, as you need a wide variety of input data to make the model generalize well, and training such models can take days on a GPU. To make this easier and faster we are using transfer learning. This lets you piggyback on a well-trained model, only retraining the upper layers of a neural network, leading to much more reliable models that train in a fraction of the time and work with substantially smaller datasets.

To configure the transfer learning model, click **Transfer learning** in the menu on the left. Here you can select the base model (the one selected by default will work, but you can change this based on your size requirements), optionally enable data augmentation (images are randomly manipulated to make the model perform better in the real world), and the rate at which the network learns.

Set:

* Transfer learning model to `MobileNetV1 96x96 0.25`
* Number of training cycles to `20`.
* Learning rate to `0.0005`.
* Data augmentation: enabled.
* Minimum confidence rating: 0.7.

And click **Start training**. After the model is done you'll see accuracy numbers, a confusion matrix and some predicted on-device performance on the bottom. You have now trained your model!

**Important:** The full example firmware for the [Sony's Spresense](/hardware/boards/sony-spresense) supports a variety of sensor interfaces, data ingestion, and other capabilities. As a result - this firmware supports image transfer learning networks up to the **MobileNetV1 96x96 0.25**. Custom firmware may allow larger models to run on the device. To learn more, see \[Run on Sony Spresense(/hardware/deployments/run-cpp-sony-spresense) to deploy trained Edge Impulse models with your firmware, and check out the [EON Tuner](/studio/projects/eon-tuner) documentation to learn how to optimize your model's performance and memory usage

<Frame caption="A trained model showing on-device performance estimations.">
  <img src="https://mintcdn.com/edgeimpulse/cU2n98Ml68g1eiRr/.assets/images/bf2187d-screen_shot_2021-03-08_at_12433_pm.png?fit=max&auto=format&n=cU2n98Ml68g1eiRr&q=85&s=ac74f284db3571586591232be82f9c0b" width="704" height="1000" data-path=".assets/images/bf2187d-screen_shot_2021-03-08_at_12433_pm.png" />
</Frame>

### 4. Validating your model

With the model trained let's try it out on some test data. When collecting the data we split the data up between a training and a testing dataset. The model was trained only on the training data, and thus we can use the data in the testing dataset to validate how well the model will work in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence.

To validate your model, go to **Model testing**, select the checkbox next to 'Sample name' and click **Classify selected**. Here we hit 89% accuracy, which is great for a model with so little data.

<Frame caption="Verifying our model on real world data">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/09291bd-screen_shot_2021-03-08_at_12541_pm.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=f21dab6fb641cfc61d82bf12dfb0ed22" width="1600" height="905" data-path=".assets/images/09291bd-screen_shot_2021-03-08_at_12541_pm.png" />
</Frame>

To see a classification in detail, click the three dots next to an item, and select **Show classification**. This brings you to the Live classification screen with much more details on the file (if you collected data with your mobile phone you can also capture new testing data directly from here). This screen can help you determine why items were misclassified.

<Frame caption="An item that could not be classified (as the highest score was under the 0.7 threshold). As the data is very far outside of any known cluster this is likely data that was unlike anything seen before - perhaps due to part of the window being present. It'd be good to add additional images to the training set.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/832658b-screen_shot_2021-03-08_at_12633_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=c3a977e49e5adaa4676710f4267bc0a7" width="1600" height="943" data-path=".assets/images/832658b-screen_shot_2021-03-08_at_12633_pm.png" />
</Frame>

### 5. Running the model on your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the preprocessing steps, neural network weights, and classification code - in a single C++ library that you can include in your embedded software.

To run your impulse click on **Deployment** in the menu. Then under 'Build firmware' select the Spresense development board, and click **Build**. This will export the impulse, and build a binary that will run on your development board in a single step. After building is completed you'll get prompted to download a binary. Save this on your computer.

#### Flashing the device

When you click the **Build** button, you'll see a pop-up with text and video instructions on how to deploy the binary to your particular device. Follow these instructions. Once you are done, we are ready to test your impulse out.

If you run into issues flashing your device, follow the steps and troubleshooting information in the [Getting Started](/hardware/boards/sony-spresense) guide.

#### Running the model on the device

We can connect to the board's newly flashed firmware over serial. Open a terminal and run:

```
$ edge-impulse-run-impulse
```

<Frame caption="The machine learning model running in real-time on device, classifying a plant.">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/open-mv-screenshot.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=ee18c91299279579eacebd941e38622e" width="1447" height="753" data-path=".assets/images/open-mv-screenshot.png" />
</Frame>

Congratulations! You've added sight to your sensors. Now that you've trained your model you can integrate your impulse in the firmware of your own embedded device, see [Run on Sony Spresense](/hardware/deployments/run-cpp-sony-spresense). There are examples for Mbed OS, Arduino, STM32CubeIDE, Zephyr, and any other target that supports a C++ compiler.

Or if you're interested in more, see our tutorials on [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) or [Image classification](/tutorials/topics/data/collect-image-data-openmv-h7-plus). If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).