# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/motion-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Motion recognition with anomaly detection

In this tutorial, you'll use machine learning to build a gesture recognition system that runs on a microcontroller. This is a hard task to solve using rule-based programming, as people don't perform gestures in the exact same way every time. But machine learning can handle these variations with ease. You'll learn how to collect high-frequency data from real sensors, use signal processing to clean up data, build a neural network classifier, and how to deploy your model back to a device. At the end of this tutorial, you'll have a firm understanding of applying machine learning in embedded devices using Edge Impulse.

There is also a video version of this tutorial:

<iframe src="https://www.youtube.com/embed/FseGCn-oBA0" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

You can view the finished project, including all data, signal processing and machine learning blocks here: [Tutorial: continuous motion recognition](https://studio.edgeimpulse.com/public/14299/latest).

### 1. Prerequisites

For this tutorial, you'll need a [supported device](/hardware).

Alternatively, use the either [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) or [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) SDK to collect data from any other development board, or your [mobile phone](/hardware/devices/mobile-phone).

If your device is connected (green dot) under **Devices** in the studio you can proceed:

<Frame caption="Devices tab with the device connected to the remote management interface.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-connected-device.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=20632be2b221f097207f28930586679e" width="1600" height="997" data-path=".assets/images/tutorial-connected-device.png" />
</Frame>

<Info>
  **Data ingestion**

  Edge Impulse can ingest data from many sources and any device - including embedded devices that you already have in production. See the documentation for the [Data acquisition](/studio/projects/data-acquisition) for more information.
</Info>

### 2. Collecting your first data

With your device connected, we can collect some data. In the studio go to the **Data acquisition** tab. This is the place where all your raw data is stored, and - if your device is connected to the remote management API - where you can start sampling new data.

Under **Record new data**, select your device, set the label to `updown`, the sample length to `10000`, the sensor to `Built-in accelerometer` and the frequency to `62.5Hz`. This indicates that you want to record data for 10 seconds, and label the recorded data as `updown`. You can later edit these labels if needed.

<Frame caption="Record new data screen.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/33ec36b-screenshot_2020-01-24_at_092057.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=5ef2311178bdf7a479a6330d86b545f4" width="555" height="489" data-path=".assets/images/33ec36b-screenshot_2020-01-24_at_092057.png" />
</Frame>

After you click **Start sampling** move your device up and down in a continuous motion. In about twelve seconds the device should complete sampling and upload the file back to Edge Impulse. You see a new line appear under 'Collected data' in the studio. When you click it you now see the raw data graphed out. As the accelerometer on the development board has three axes you'll notice three different lines, one for each axis.

<Warning>
  **Continuous movement**

  It's important to do continuous movements as we'll later slice up the data in smaller windows.
</Warning>

<Frame caption="Updown movement recorded from the accelerometer.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7333392-screenshot_2019-10-07_at_195335.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4df163e499768d66bbebca09ba1a401a" width="562" height="506" data-path=".assets/images/7333392-screenshot_2019-10-07_at_195335.png" />
</Frame>

Machine learning works best with lots of data, so a single sample won't cut it. Now is the time to start building your own dataset. For example, use the following four classes, and record around 3 minutes of data per class:

* Idle - just sitting on your desk while you're working.
* Snake - moving the device over your desk as a snake.
* Wave - waving the device from left to right.
* Updown - moving the device up and down.

<Info>
  **Variations**

  Make sure to perform variations on the motions. E.g. do both slow and fast movements and vary the orientation of the board. You'll never know how your user will use the device. It's best to collect samples of \~10 seconds each.
</Info>

**Prebuilt dataset**

Alternatively, you can load an example test set that has about ten minutes of data in these classes (but how much fun is that?). See the [Continuous gestures dataset](/datasets/time-series/continuous-motion-recognition) for more information.

### 3. Designing an impulse

With the training set in place, you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the 'Spectral analysis' signal processing block. This block applies a filter, performs spectral analysis on the signal, and extracts frequency and spectral power data. Then we'll use a 'Neural Network' learning block, that takes these spectral features and learns to distinguish between the four (idle, snake, wave, updown) classes.

In the studio go to **Create impulse**, set the window size to `2000` (you can click on the `2000 ms.` text to enter an exact value), the window increase to `80`, and add the 'Spectral Analysis' and 'Classification (Keras)' blocks. Then click **Save impulse**.

<Frame caption="First impulse, with one processing block and one learning block.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-create-impulse.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=9f1c75962834180ce64f577516300eae" width="1600" height="764" data-path=".assets/images/tutorial-continuous-motion-create-impulse.png" />
</Frame>

#### Configuring the spectral analysis block

To configure your signal processing block, click **Spectral features** in the menu on the left. This will show you the raw data on top of the screen (you can select other files via the drop down menu), and the results of the signal processing through graphs on the right. For the spectral features block you'll see the following graphs:

* Filter response - If you have chosen a filter (with non zero order), this will show you the response across frequencies. That is, it will show you how much each frequency will be attenuated.
* After filter - the signal after applying the filter. This will remove noise.
* Spectral power - the frequencies at which the signal is repeating (e.g. making one wave movement per second will show a peak at 1 Hz).

<Info>
  See the dedicated page for the [Spectral features](/studio/projects/processing-blocks/blocks/spectral-analysis) pre-processing block.
</Info>

A good signal processing block will yield similar results for similar data. If you move the sliding window (on the raw data graph) around, the graphs should remain similar. Also, when you switch to another file with the same label, you should see similar graphs, even if the orientation of the device was different.

<Info>
  **Bonus exercise: filters**

  Try to reason about the filter parameters. What does the cut-off frequency control? And what do you see if you switch from a low-pass to a high-pass filter?
</Info>

Set the filter to low pass with the following parameters:

<Frame caption="Spectral features parameters">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-spectral-features.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=b3ba7a3943890adea86f85c10626b599" width="820" height="1000" data-path=".assets/images/tutorial-continuous-motion-spectral-features.png" />
</Frame>

Once you're happy with the result, click **Save parameters**. This will send you to the 'Feature generation' screen. In here you'll:

1. Split all raw data up in windows (based on the window size and the window increase).
2. Apply the spectral features block on all these windows.
3. Calculate feature importance. We will use this later to set up the anomaly detection.

Click **Generate features** to start the process.

Afterward the 'Feature explorer' will load. This is a plot of all the extracted features against all the generated windows. You can use this graph to compare your complete data set. A good rule of thumb is that if you can visually identify some clusters by classes, then the machine learning model will be able to do so as well.

<Frame caption="Spectral features - Generate features">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-spectral-features-generate.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=4a52a6a27448d4c3cbb47e0162517b42" width="964" height="1000" data-path=".assets/images/tutorial-continuous-motion-spectral-features-generate.png" />
</Frame>

#### Configuring the neural network

With all data processed it's time to start training a neural network. Neural networks are a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns. The network that we're training here will take the signal processing data as an input, and try to map this to one of the four classes.

So how does a neural network know what to predict? A neural network consists of layers of neurons, all interconnected, and each connection has a weight. One such neuron in the input layer would be the height of the first peak of the X-axis (from the signal processing block); and one such neuron in the output layer would be `wave` (one the classes). When defining the neural network all these connections are initialized randomly, and thus the neural network will make random predictions. During training, we then take all the raw data, ask the network to make a prediction, and then make tiny alterations to the weights depending on the outcome (this is why labeling raw data is important).

This way, after a lot of iterations, the neural network learns; and will eventually become much better at predicting new data. Let's try this out by clicking on **NN Classifier** in the menu.

<Info>
  See the dedicated page for the [Classification (Keras)](/studio/projects/learning-blocks/blocks/classification) learning block.
</Info>

Set 'Number of training cycles' to `1`. This will limit training to a single iteration. And then click **Start training**.

<Frame caption="Training performance after a single iteration. On the top-right, is a summary of the accuracy of the network, and in the middle, a confusion matrix. This matrix shows when the network made correct and incorrect decisions. You see that idle is relatively easy to predict. Why do you think this is?">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-nn-1-epoch.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=9dd6aa3561ed649f37089deba3cf869f" width="824" height="1000" data-path=".assets/images/tutorial-continuous-motion-nn-1-epoch.png" />
</Frame>

Now change 'Number of training cycles' to `2` and you'll see performance go up. Finally, change 'Number of training cycles' to `30` and let the training finish.

You've just trained your first neural networks!

<Frame caption="Neural network trained with 30 epochs">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-nn-20-epochs.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=54f170956f3df51239882b730d9f46be" width="1064" height="1000" data-path=".assets/images/tutorial-continuous-motion-nn-20-epochs.png" />
</Frame>

<Warning>
  **100% accuracy**

  You might end up with 100% accuracy after training for 100 training cycles. This is not necessarily a good thing, as it might be a sign that the neural network is too tuned for the specific test set and might perform poorly on new data (overfitting). The best way to reduce this is by adding more data or reducing the learning rate.
</Warning>

### 4. Classifying new data

From the statistics in the previous step we know that the model works against our training data, but how well would the network perform on new data? Click on **Live classification** in the menu to find out. Your device should (just like in step 2) show as online under 'Classify new data'. Set the 'Sample length' to `10000` (10 seconds), click **Start sampling** and start doing movements. Afterward, you'll get a full report on what the network thought you did.

<Frame caption="Classification result. Showing the conclusions, the raw data and processed features in one overview.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-live-classification.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=1eb20b49d42d027f481a8c8bcf807d11" width="675" height="1000" data-path=".assets/images/tutorial-continuous-motion-live-classification.png" />
</Frame>

If the network performed great, fantastic! But what if it performed poorly? There could be a variety of reasons, but the most common ones are:

1. There is not enough data. Neural networks need to learn patterns in data sets, and the more data the better.
2. The data does not look like other data the network has seen before. This is common when someone uses the device in a way that you didn't add to the test set. You can add the current file to the test set by clicking `⋮`, then selecting **Move to training set**. Make sure to update the label under 'Data acquisition' before training.
3. The model has not been trained enough. Up the number of epochs to `200` and see if performance increases (the classified file is stored, and you can load it through 'Classify existing validation sample').
4. The model is overfitting and thus performs poorly on new data. Try reducing the learning rate or add more data.
5. The neural network architecture is not a great fit for your data. Play with the number of layers and neurons and see if performance improves.

As you see there is still a lot of trial and error when building neural networks, but we hope the visualizations help a lot. You can also run the network against the complete validation set through 'Model validation'. Think of the model validation page as a set of unit tests for your model!

With a working model in place, we can look at places where our current impulse performs poorly.

### 5. Anomaly detection

Neural networks are great, but they have one big flaw. They're terrible at dealing with data they have never seen before (like a new gesture). Neural networks cannot judge this, as they are only aware of the training data. If you give it something unlike anything it has seen before it'll still classify as one of the four classes.

Let's look at how this works in practice. Go to 'Live classification' and record some new data, but now vividly shake your device. Take a look and see how the network will predict something regardless.

So, how can we do better? If you look at the feature explorer, you should be able to visually separate the classified data from the training data. We can use this to our advantage by training a new (second) network that creates clusters around data that we have seen before, and compares incoming data against these clusters. If the distance from a cluster is too large you can flag the sample as an anomaly, and not trust the neural network.

<Frame caption="Shake data is easily separated from the training data.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-live-classification-explorer.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=f1531d11c99fa52c767f444f94273f0c" width="1328" height="1000" data-path=".assets/images/tutorial-continuous-motion-live-classification-explorer.png" />
</Frame>

To add this block go to **Create impulse**, click **Add learning block**, and select 'Anomaly Detection (K-Means)'. Then click **Save impulse**.

<Frame caption="Add anomaly detection block to Create impulse tab">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-create-impulse-2.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=48672587732feba4850791a5931750a8" width="1600" height="971" data-path=".assets/images/tutorial-continuous-motion-create-impulse-2.png" />
</Frame>

To configure the clustering model click on **Anomaly detection** in the menu. Here we need to specify:

* The number of clusters. Here use `32`.
* The axes that we want to select during clustering. Click on the **Select suggested axes** button to harness the results of the [feature importance](/studio/projects/processing-blocks#feature-importance) output. Alternatively, the data separates well on the accX RMS, accY RMS and accZ RMS axes, you can also include these axes.

<Info>
  See the dedicated page for the [anomaly detection (K-means)](/studio/projects/learning-blocks/blocks/anomaly-detection-k-means) learning block. We also provide the [anomaly detection (GMM)](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm) learning block that is compatible with this tutorial.
</Info>

Click **Start training** to generate the clusters. You can load existing validation samples into the anomaly explorer with the dropdown menu.

<Frame caption="Known clusters in blue, the shake data in orange. It's clearly outside of any known clusters and can thus be tagged as an anomaly.">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-continuous-motion-anomaly-explorer.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=9cfeb26536534dc67734d3a17c1be3e7" width="800" height="1000" data-path=".assets/images/tutorial-continuous-motion-anomaly-explorer.png" />
</Frame>

<Info>
  **Axes**

  The anomaly explorer only plots two axes at the same time. Under 'average axis distance' you see how far away from each axis the validation sample is. Use the dropdown menu's to change axes.
</Info>

If you now go back to 'Live classification' and load your last sample, it should now have tagged everything as anomaly. This is a great example where signal processing (to extract features), neural networks (for classification) and clustering algorithms (for anomaly detection) can work together.

### 6. Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the signal processing code, neural network weights, and classification code - up in a single C++ library that you can include in your embedded software.

<Info>
  **Mobile phone**

  Your mobile phone can build and download the compiled impulse directly from the mobile client. See 'Deploying back to device' on the [Using your mobile phone](/hardware/devices/mobile-phone) page.
</Info>

To export your model, click on **Deployment** in the menu. Then under 'Build firmware' select your development board, and click **Build**. This will export the impulse, and build a binary that will run on your development board in a single step. After building is completed you'll get prompted to download a binary. Save this on your computer.

#### Flashing the device

When you click the **Build** button, you'll see a pop-up with text and video instructions on how to deploy the binary to your particular device. Follow these instructions. Once you are done, we are ready to test your impulse out.

#### Running the model on the device

We can connect to the board's newly flashed firmware over serial. Open a terminal and run:

```
$ edge-impulse-run-impulse
```

<Warning>
  **Serial daemon**

  If the device is not connected over WiFi, but instead connected via the Edge Impulse serial daemon, you'll need stop the daemon. Only one application can connect to the development board at a time.
</Warning>

This will sample data from the sensor, run the signal processing code, and then classify the data:

```
Starting inferencing in 2 seconds...
Sampling... Storing in file name: /fs/device-classification261
Tensor shape: 4
Predictions (DSP: 17 ms., Classification: 1 ms., Anomaly: 0 ms.):
    idle: 0.00004
    snake: 0.00012
    updown: 0.00009
    wave: 0.99976
    anomaly score: 0.032
Finished inferencing, raw data is stored in '/fs/device-classification261'. Use AT+UPLOADFILE to send back to Edge Impulse.
```

<Warning>
  **Continuous movement**

  We trained a model to detect continuous movement in 2 second intervals. Thus, changing your movement while sampling will yield incorrect results. Make sure you've started your movement when 'Sampling...' gets printed. In between sampling, you have two seconds to switch movements.

  To run the continuous sampling, run the following command:

  ```
  $ edge-impulse-run-impulse --continuous
  ```
</Warning>

Victory! You've now built your first on-device machine learning model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4eed33c-ezgif-3-8cebec2be387.gif?s=57b978fa5888ca591a8c2f1e4ea67b3a" width="480" height="360" data-path=".assets/images/4eed33c-ezgif-3-8cebec2be387.gif" />
</Frame>

### 7. Conclusion

Congratulations! You have used Edge Impulse to train a machine learning model capable of recognizing your gestures and understand how you can build models that classify sensor data or find anomalies. Now that you've trained your model you can integrate your impulse in the firmware of your own embedded device, see the [Deployments](/hardware/deployments) tutorials. There are examples for Mbed OS, Arduino, STM32CubeIDE, and any other target that supports a C++ compiler.

Or if you're interested in more, see our tutorials on [Sound recognition](/tutorials/end-to-end/sound-recognition) or [Image classification](/tutorials/end-to-end/image-classification). If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).