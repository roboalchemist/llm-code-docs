# Source: https://docs.edgeimpulse.com/tutorials/hardware/syntiant-ndp-motion-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Syntiant NDPs - motion recognition

<Info>
  **Keyword spotting**

  This tutorial is for the Syntiant hardware only ([Syntiant TinyML](/hardware/boards/syntiant-tinyml-board), [Arduino Nicla Voice](/hardware/boards/arduino-nicla-voice)), and the [Avnet RASynBoard (Renesas RA6 and Syntiant NDP 120)](/hardware/boards/avnet-rasynboard). For other development boards, you can follow the standard [Continuous Motion Recognition](/tutorials/end-to-end/motion-recognition) tutorial
</Info>

In this tutorial, you'll use machine learning to build a gesture recognition system that runs on the Syntiant TinyML board. This is a hard task to solve using rule-based programming, as people don't perform gestures in the exact same way every time. But machine learning can handle these variations with ease. You'll learn how to collect high-frequency data from an IMU, build a neural network classifier, and how to deploy your model back to a device. At the end of this tutorial, you'll have a firm understanding of applying machine learning on Syntiant TinyML board using Edge Impulse.

<Info>
  **Before starting the tutorial**

  After signing up for a free Edge Impulse account, clone the finished project, including all training data, signal processing and machine learning blocks here: [Syntiant - Circular Motion](https://studio.edgeimpulse.com/public/102981/latest). At the end of the process you will have the full project that comes pre-loaded with training and test datasets.
</Info>

## 1. Prerequisites

For this tutorial you'll need the:

* [Syntiant TinyML Board](/hardware/boards/syntiant-tinyml-board)
* An SD Card to perform IMU data acquisition

or

* [Arduino Nicla Voice](/hardware/boards/arduino-nicla-voice)
* [Avnet RASynBoard (Renesas RA6 and Syntiant NDP 120)](/hardware/boards/avnet-rasynboard)

Follow the steps to connect your development board to Edge Impulse.

If your device is connected under Devices in the studio you can proceed:

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntiant-connected.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=0608ae471c6e6d5393c3d01f825e539f" width="1600" height="376" data-path=".assets/images/syntiant-connected.png" />
</Frame>

<Info>
  **Device compatibility**

  Edge Impulse can ingest data from any device - including embedded devices that you already have in production. See the documentation for the [Ingestion API](/apis/ingestion) for more information.
</Info>

## 2. Collecting your first data

With your device connected, we can collect some data. In the studio go to the **Data acquisition** tab. This is the place where all your raw data is stored, and - if your device is connected to the remote management API - where you can start sampling new data.

Under **Record new data**, select your Syntiant device, set the label to `circular`, the sample length to `2000`, the sensor to `Inertial` and the frequency to `100 Hz`. This indicates that you want to record data for 2 seconds, and label the recorded data as `circular`. You can later edit these labels if needed.

<Frame caption="Record new data screen">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-imu.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=06031211c9a06c7cdf74ffd48f84eef6" width="1032" height="882" data-path=".assets/images/syntiant-imu.png" />
</Frame>

After you click **Start sampling** move your device in a circular motion. In about twelve seconds the device should complete sampling and upload the file back to Edge Impulse. You see a new line appear under 'Collected data' in the studio. When you click it you now see the raw data graphed out. As the accelerometer on the development board has three axes you'll notice three different lines, one for each axis.

<Warning>
  **Continuous movement**

  It's important to do continuous movements as we'll later slice up the data in smaller windows. Make sure also to perform variations on the motions. E.g. do both slow and fast movements and vary the orientation of the board. You'll never know how your user will use the device.
</Warning>

<Frame caption="Circular movements recorded from the IMU">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntiant-circular.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=58e8b787a22e948cc3a57be4285f13d1" width="1042" height="746" data-path=".assets/images/syntiant-circular.png" />
</Frame>

Machine learning works best with lots of data, so a single sample won't cut it. Now is the time to start building your own dataset. For example, use the following two classes, and record around 3 minutes of data per class:

* Circular - circular movements
* Z\_Openset - random movements that are not circular

<Info>
  **Negative Class**

  The Syntiant NDP chips require a negative class on which no predictions will occur, in our example this is the Z\_Openset class. Make sure the class name is last in alphabetical order.
</Info>

## 3. Designing an impulse

With the training set in place you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the 'IMU Syntiant' signal processing block. This block rescales raw data to 8 bits values to match the NDP chip input requirements. Then we'll use a 'Neural Network' learning block, that takes these generated features and learns to distinguish between our different classes (circular or not).

In the studio go to **Create impulse**, set the window size to `1800` (you can click on the `1800 ms.` text to enter an exact value), the window increase to `80`, and add the 'IMU Syntiant' and 'Classification (Keras)' blocks. Then click **Save impulse**.

<Frame caption="Impulse with processing and learning blocks">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-impulse.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=4e596582b74df716dd7110dce3a66c31" width="1600" height="958" data-path=".assets/images/syntiant-impulse.png" />
</Frame>

<Info>
  **Window size**

  The Syntiant NDP101 chip requires the number of generated features to be divisible by 4. In our example, we have 6 axis sampled at 100 Hz with a window of 1800ms, leading to 1080 (180x6) features which is divisible by 4.
</Info>

### Configuring the IMU Syntiant block

To configure your signal processing block, click **Syntiant IMU** in the menu on the left. This will show you the raw data on top of the screen (you can select other files via the drop down menu), and the processed features on the right.

The `Scale 16 bits to 8 bits` converts your raw data to 8 bits and normalize it to the range \[-1, 1]. The circular motion public project's dataset is already rescaled so you need to disable the option in this case.

Click **Save parameters**. This will send you to the 'Feature generation' screen.

Click **Generate features** to start the process.

Afterwards the 'Feature explorer' will load. This is a plot of all the extracted features against all the generated windows. You can use this graph to compare your complete data set. A good rule of thumb is that if you can visually separate the data on a number of axes, then the machine learning model will be able to do so as well.

<Frame caption="Examining your full dataset in the feature explorer">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-features.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=73a98a06471ab9dc08c88205a325699d" width="912" height="1000" data-path=".assets/images/syntiant-features.png" />
</Frame>

### Configuring the neural network

With all data processed it's time to start training a neural network. Neural networks are algorithms, modeled loosely after the human brain, that can learn to recognize patterns that appear in their training data. The network that we're training here will take the processing block features as an input, and try to map this to one of the two classes — 'circular' or 'z\_openset'.

Click on **NN Classifier** in the left hand menu. You'll see the following page:

<Frame caption="Syntiant neural network configuration">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-nn.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=26b5784a25ce5f0fbf4aa3d12abeabd1" width="1042" height="945" data-path=".assets/images/syntiant-nn.png" />
</Frame>

With everything in place, click **Start training**. When it's complete, you'll see the *Last training performance* panel appear at the bottom of the page:

<Frame caption="Training performances">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-training.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=d0adef4d31479899a270a804e7d211c2" width="747" height="733" data-path=".assets/images/syntiant-training.png" />
</Frame>

Congratulations, you've trained a neural network with Edge Impulse and ready to deploy on Syntiant hardware! But what do all these numbers mean?

At the start of training, 20% of the training data is set aside for *validation*. This means that instead of being used to train the model, it is used to evaluate how the model is performing. The *Last training performance* panel displays the results of this validation, providing some vital information about your model and how well it is working. Bear in mind that your exact numbers may differ from the ones in this tutorial.

On the left hand side of the panel, *Accuracy* refers to the percentage of windows of audio that were correctly classified. The higher number the better, although an accuracy approaching 100% is unlikely, and is often a sign that your model has *overfit* the training data. You will find out whether this is true in the next stage, during model testing. For many applications, an accuracy above 85% can be considered very good.

The *Confusion matrix* is a table showing the balance of correctly versus incorrectly classified windows. To understand it, compare the values in each row. For example, in the above screenshot, 100% of the *circular* motion samples were classified correctly, and 99.6% for the *openset* samples.

## 4. Classifying new data

From the statistics in the previous step we know that the model works against our training data, but how well would the network perform on new data? Click on **Live classification** in the menu to find out. Your device should (just like in step 2) show as online under 'Classify new data'. Set the 'Sample length' to `2000` (5 seconds), click **Start sampling** and start doing movements. Afterward, you'll get a full report on what the network thought that you did.

<Frame caption="Classification result. Showing the conclusions, the raw data and processed features in one overview">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntiant-classification.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=0e97cc27d3c1a8fc9732ccff7992b8b7" width="1100" height="944" data-path=".assets/images/syntiant-classification.png" />
</Frame>

If the network performed great, fantastic! But what if it performed poorly? There could be a variety of reasons, but the most common ones are:

1. There is not enough data. Neural networks need to learn patterns in data sets, and the more data the better.
2. The data does not look like other data the network has seen before. This is common when someone uses the device in a way that you didn't add to the test set. You can add the current file to the test set by clicking `⋮`, then selecting **Move to training set**. Make sure to update the label under 'Data acquisition' before training.
3. The model has not been trained enough. Up the number of epochs to `50` and see if performance increases (the classified file is stored, and you can load it through 'Classify existing validation sample').

As you see there is still a lot of trial and error when building neural networks, but we hope the visualizations help a lot. You can also run the network against the complete validation set through 'Model validation'. Think of the model validation page as a set of unit tests for your model!

With a working model in place, we can look at places where our current impulse performs poorly.

### 5. Deploying to your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption.

To export your model, click on **Deployment** in the menu. Then under 'Build firmware' select the Syntiant development board,

The final step before building the firmware is to configure the *posterior handler parameters* of the Syntiant chip.

<Info>
  **Pre-configured posterior parameters**

  For the Syntiant Circular Motion project, we've already pre-configured the posterior parameters so you can just go to the 'Build' output step.
</Info>

<Frame caption="Optimizing posterior parameters">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/syntiant-posterior.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=b0ec9e92ea8a6d38ba1614241b0603b9" width="861" height="868" data-path=".assets/images/syntiant-posterior.png" />
</Frame>

Those parameters are used to tune the precision and recall of the neural network activations, to minimize False Rejection Rate and False Activation Rate. You can manually edit those parameters in JSON format or use the *Find posterior parameters* to search for the best values:

* Select the classes you want to detect and make sure to uncheck the last class (Z\_Openset in our example)
* Select a calibration method: either no calibration (**fastest recommended for Syntiant TinyML board**), or FAR optimized (FAR is optimized for an FRR target \< 0.2).

## 6. Flashing the device

Once optimized parameters have been found, you can click **Build**. This will build a Syntiant package that will run on your development board. After building is completed you'll get prompted to download a zipfile. Save this on your computer. A pop-up video will show how the download process works.

After unzipping the downloaded file, run the appropriate flashing script for your platform (Linux, Mac, or Win 10) to flash the board with the Syntiant Circular Motion model and associated firmware. You might see a Microsoft Defender screen pop up when the script is run on Windows 10. It's safe to proceed so select 'More info' and continue.

### Running the model on the device

We can connect to the board's newly flashed firmware over serial. Open a terminal and run:

```
$ edge-impulse-run-impulse
```

<Warning>
  **Serial daemon**

  If the device is connected via the Edge Impulse serial daemon, you'll need to stop the daemon first. Only one application can connect to the development board at a time.
</Warning>

This will sample data from the sensor, run the signal processing code, and then classify the data:

```
[SER] Started inferencing, press CTRL+C to stop...
LSE
Inferencing settings:
        Interval: 10.0000 ms.
        Frame size: 1080
        Sample length: 11 ms.
        No. of classes: 2
Starting inferencing, press 'b' to break
>
Predictions:
    circularClockwise:  1
    z_openset:  0

Predictions:
    circularClockwise:  1
    z_openset:  0
```

Victory! You've now built your first on-device machine learning model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4eed33c-ezgif-3-8cebec2be387.gif?s=57b978fa5888ca591a8c2f1e4ea67b3a" width="480" height="360" data-path=".assets/images/4eed33c-ezgif-3-8cebec2be387.gif" />
</Frame>

## 7. Conclusion

Congratulations! Now that you've trained and deployed your model you can go further and build your own custom firmware, see [Run on Syntiant TinyML Board](/hardware/deployments/run-cpp-syntiant-tinyml-board).

Or if you're interested in audio projects, see our tutorial on [Keyword spotting - Syntiant - RC Commands](/tutorials/hardware/syntiant-ndp-keyword-spotting).

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).