# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/sound-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sound recognition

In this tutorial, you'll use machine learning to build a system that can recognize when a particular sound is happening—a task known as *audio classification*. The system you create will be able to recognize the sound of water running from a faucet, even in the presence of other background noise.

You'll learn how to collect audio data from microphones, use signal processing to extract the most important information, and train a deep neural network that can tell you whether the sound of running water can be heard in a given clip of audio. Finally, you'll deploy the system to an embedded device and evaluate how well it works.

At the end of this tutorial, you'll have a firm understanding of how to classify audio using Edge Impulse.

There is also a video version of this tutorial:

<iframe src="https://www.youtube.com/embed/ckD3InrSXo0" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

You can view the finished project, including all data, signal processing and machine learning blocks here: [Tutorial: recognize sounds from audio](https://studio.edgeimpulse.com/public/14301/latest).

<Info>
  **Detecting human speech?**

  Do you want a device that listens to your voice? We have a specific tutorial for that! See [Keyword spotting](/tutorials/end-to-end/keyword-spotting).
</Info>

### 1. Prerequisites

For this tutorial, you'll need a [supported device](/hardware).

If you don't see your supported development board listed here, be sure to check the hardware specific [tutorials](/tutorials) page for the appropriate tutorial.

If your device is connected under **Devices** in the studio you can proceed:

<Frame caption="Devices tab with the device connected to the remote management interface.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/a3bb87e-screen_shot_2020-01-22_at_32647_pm.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=fef1b88e8e60506c5161a957da9829cc" width="995" height="260" data-path=".assets/images/a3bb87e-screen_shot_2020-01-22_at_32647_pm.png" />
</Frame>

<Info>
  **Device compatibility**

  Edge Impulse can ingest data from any device - including embedded devices that you already have in production. See the documentation for the [Ingestion API](/apis/ingestion) for more information.
</Info>

### 2. Collecting your first data

To build this project, you'll need to collect some audio data that will be used to train the machine learning model. Since the goal is to detect the sound of a running faucet, you'll need to collect some examples of that. You'll also need some examples of typical background noise that *doesn't* contain the sound of a faucet, so the model can learn to discriminate between the two. These two types of examples represent the two *classes* we'll be training our model to detect: background noise, or running faucet.

You can use your device to collect some data. In the studio, go to the **Data acquisition** tab. This is the place where all your raw data is stored, and - if your device is connected to the remote management API - where you can start sampling new data.

Let's start by recording an example of background noise that doesn't contain the sound of a running faucet. Under **Record new data**, select your device, set the label to `noise`, the sample length to `1000`, and the sensor to `Built-in microphone`. This indicates that you want to record 1 second of audio, and label the recorded data as `noise`. You can later edit these labels if needed.

<Frame caption="Record new data screen.">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2b59a5a-screen_shot_2020-01-22_at_40224_pm.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=904cb3e2347d19a8578b6a446ab49805" width="588" height="482" data-path=".assets/images/2b59a5a-screen_shot_2020-01-22_at_40224_pm.png" />
</Frame>

After you click **Start sampling**, the device will capture a second of audio and transmit it to Edge Impulse. The LED will light while recording is in progress, then light again during transmission.

When the data has been uploaded, you will see a new line appear under 'Collected data'. You will also see the waveform of the audio in the 'RAW DATA' box. You can use the controls underneath to listen to the audio that was captured.

<Frame caption="Audio waveform">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/69ef343-screen_shot_2020-01-22_at_40810_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=ebd33707708342e3cf90c4542bebf211" width="588" height="585" data-path=".assets/images/69ef343-screen_shot_2020-01-22_at_40810_pm.png" />
</Frame>

### 3. Build a dataset

Since you now know how to capture audio with Edge Impulse, it's time to start building a dataset. For a simple audio classification model like this one, we should aim to capture around 10 minutes of data. We have two classes, and it's ideal if our data is balanced equally between each of them. This means we should aim to capture the following data:

* 5 minutes of background noise, with the label "noise"
* 5 minutes of running faucet noise, with the label "faucet"

**Real world data**

In the real world, there are usually additional sounds present alongside the sounds we care about. For example, a running faucet is often accompanied by the sound of dishes being washed, teeth being brushed, or a conversation in the kitchen. Background noise might also include the sounds of television, kids playing, or cars driving past outside.

It's important that your training data contains these types of real world sounds. If your model is not exposed to them during training, it will not learn to take them into account, and it will not perform well during real-world usage.

For this tutorial, you should try to capture the following:

* Background noise
  * 2 minutes of background noise without much additional activity
  * 1 minute of background noise with a TV or music playing
  * 1 minute of background noise featuring occasional talking or conversation
  * 1 minutes of background noise with the sounds of housework
* Running faucet noise
  * 1 minute of a faucet running
  * 1 minute of a different faucet running
  * 1 minute of a faucet running with a TV or music playing
  * 1 minute of a faucet running with occasional talking or conversation
  * 1 minute of a faucet running with the sounds of housework

It's okay if you can't get all of these, as long as you still obtain 5 minutes of data for each class. However, your model will perform better in the real world if it was trained on a representative dataset.

<Info>
  **Dataset diversity**

  There's no guarantee your model will perform well in the presence of sounds that were not included in its training set, so it's important to make your dataset as diverse and representative of real-world conditions as possible.
</Info>

**Data capture and transmission**

The amount of audio that can be captured in one go varies depending on a device's memory. The ST B-L475E-IOT01A developer board has enough memory to capture 60 seconds of audio at a time, and the Arduino Nano 33 BLE Sense has enough memory for 16 seconds. To capture 60 seconds of audio, set the sample length to `60000`. Because the board transmits data quite slowly, it will take around 7 minutes before a 60 second sample appears in Edge Impulse.

Once you've captured around 10 minutes of data, it's time to start designing an Impulse.

**Prebuilt dataset**

Alternatively, you can load an example test set that has about ten minutes of data in these classes (but how much fun is that?). See the [Running faucet dataset](/datasets/audio/faucet-vs-noise) for more information.

### 4. Design an Impulse

With the training set in place you can design an impulse. An impulse takes the raw data, slices it up in smaller windows, uses signal processing blocks to extract features, and then uses a learning block to classify new data. Signal processing blocks always return the same values for the same input and are used to make raw data easier to process, while learning blocks learn from past experiences.

For this tutorial we'll use the "MFE" signal processing block. MFE stands for Mel Frequency Energy. This sounds scary, but it's basically just a way of turning raw audio—which contains a large amount of redundant information—into simplified form.

<Warning>
  **Spectrogram block**

  Edge Impulse supports three different blocks for audio classification: MFCC, MFE and spectrogram blocks. If your accuracy is not great using the MFE block you can switch to the spectrogram block, which is not tuned to frequencies for the human ear.
</Warning>

We'll then pass this simplified audio data into a Neural Network block, which will learn to distinguish between the two classes of audio (faucet and noise).

In the studio, go to the **Create impulse** tab. You'll see a *Raw data* block, like this one.

<Frame caption="The Raw data block with updated parameters.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/a8e2bfe-screenshot_2020-05-31_at_093127.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=6b76bd3afaca1d9bccc7f7a14c9dea74" width="578" height="902" data-path=".assets/images/a8e2bfe-screenshot_2020-05-31_at_093127.png" />
</Frame>

As mentioned above, Edge Impulse slices up the raw samples into *windows* that are fed into the machine learning model during training. The *Window size* field controls how long, in milliseconds, each window of data should be. A one second audio sample will be enough to determine whether a faucet is running or not, so you should make sure *Window size* is set to 1000 ms. You can either drag the slider or type a new value directly.

Each raw sample is sliced into multiple windows, and the *Window increase* field controls the offset of each subsequent window from the first. For example, a *Window increase* value of 1000 ms would result in each window starting 1 second after the start of the previous one.

By setting a *Window increase* that is smaller than the *Window size*, we can create windows that overlap. This is actually a great idea. Although they may contain similar data, each overlapping window is still a unique example of audio that represents the sample's label. By using overlapping windows, we can make the most of our training data. For example, with a *Window size* of 1000 ms and a *Window increase* of 100 ms, we can extract 10 unique windows from only 2 seconds of data.

Make sure the *Window increase* field is set to 300 ms. The *Raw data* block should match the screenshot above.

Next, click **Add a processing block** and choose the 'MFE' block. Once you're done with that, click **Add a learning block** and select 'Classification (Keras)'. Finally, click **Save impulse**. Your impulse should now look like this:

<Frame caption="The impulse, with one processing block and one learning block.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6ffb0a7-screenshot_2021-07-14_at_104609.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=99759e6d71f7084408b101aee3a4f523" width="1147" height="653" data-path=".assets/images/6ffb0a7-screenshot_2021-07-14_at_104609.png" />
</Frame>

### 5. Configure the MFE block

Now that we've assembled the building blocks of our Impulse, we can configure each individual part. Click on the **MFE** tab in the left hand navigation menu. You'll see a page that looks like this:

<Frame caption="The MFE page.">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/0799fa6-screenshot_2021-07-14_at_104710.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=8537a0346d08936c84346efca59d8067" width="1054" height="1000" data-path=".assets/images/0799fa6-screenshot_2021-07-14_at_104710.png" />
</Frame>

This page allows you to configure the MFE block, and lets you preview how the data will be transformed. The right of the page shows a visualization of the MFE's output for a piece of audio, which is known as a [spectrogram](/studio/projects/processing-blocks/blocks/spectrogram).

The MFE block transforms a window of audio into a table of data where each row represents a range of frequencies and each column represents a span of time. The value contained within each cell reflects the amplitude of its associated range of frequencies during that span of time. The spectrogram shows each cell as a colored block, the intensity which varies depends on the amplitude.

The patterns visible in a spectrogram contain information about what type of sound it represents. For example, the spectrogram in this image shows a pattern typical of background noise:

<Frame caption="Spectrogram of background noise.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3f66ee2-screenshot_2021-07-14_at_105147.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=19ec3eaa70eed5897090ff5e2e71e115" width="482" height="197" data-path=".assets/images/3f66ee2-screenshot_2021-07-14_at_105147.png" />
</Frame>

You can tell that it is slightly different from the following spectrogram, which shows a pattern typical of a running faucet:

<Frame caption="Spectrogram of a running faucet.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/50a0cdb-screenshot_2021-07-14_at_105221.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=389c58c44d11020ddbc7fe988298f09b" width="483" height="196" data-path=".assets/images/50a0cdb-screenshot_2021-07-14_at_105221.png" />
</Frame>

These differences are not necessarily easy for a person to describe, but fortunately they are enough for a neural network to learn to identify.

It's interesting to explore your data and look at the types of spectrograms it results in. You can use the dropdown box near the top right of the page to choose between different audio samples to visualize, and drag the white window on the audio waveform to select different windows of data:

<Frame caption="Audio waveform and sample dropdown box.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9e69c0f-screen_shot_2020-01-23_at_124438_pm.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=cee0f489453c87400900a80b89b33635" width="1600" height="255" data-path=".assets/images/9e69c0f-screen_shot_2020-01-23_at_124438_pm.png" />
</Frame>

There are a lot of different ways to configure the MFCC block, as shown in the Parameters box:

<Frame caption="The MFE parameters box.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/8089784-screenshot_2021-07-14_at_105247.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=7b3d71f1d6f18ef119bf25b5737da91d" width="548" height="691" data-path=".assets/images/8089784-screenshot_2021-07-14_at_105247.png" />
</Frame>

Handily, Edge Impulse provides sensible defaults that will work well for many use cases, so we can leave these values unchanged. You can play around with the noise floor to quickly see the effect it has on the spectrogram.

The spectrograms generated by the MFE block will be passed into a neural network architecture that is particularly good at learning to recognize patterns in this type of tabular data. Before training our neural network, we'll need to generate MFE blocks for all of our windows of audio. To do this, click the *Generate features* button at the top of the page, then click the green *Generate features* button. If you have a full 10 minutes of data, the process will take a while to complete:

<Frame caption="Running the feature generation process.">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/e5c68bc-screen_shot_2020-01-23_at_125821_pm.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=39a328d479a9df3279574782df6c7fa9" width="805" height="1000" data-path=".assets/images/e5c68bc-screen_shot_2020-01-23_at_125821_pm.png" />
</Frame>

Once this process is complete the feature explorer shows a visualization of your dataset. Here dimensionality reduction is used to map your features onto a 3D space, and you can use the feature explorer to see if the different classes separate well, or find mislabeled data (if it shows in a different cluster). You can find more information in [visualizing complex datasets](https://edgeimpulse.com/blog/visualizing-complex-datasets-in-edge-impulse/).

Next, we'll configure the neural network and begin training.

### 6. Configure the neural network

With all data processed it's time to start training a neural network. Neural networks are algorithms, modeled loosely after the human brain, that can learn to recognize patterns that appear in their training data. The network that we're training here will take the MFE as an input, and try to map this to one of two classes—noise, or faucet.

Click on **NN Classifier** in the left hand menu. You'll see the following page:

<Frame caption="The NN Classifier page.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8db3def-screen_shot_2020-01-23_at_10928_pm.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=775247e152f1760dee777bcab1d87454" width="1600" height="911" data-path=".assets/images/8db3def-screen_shot_2020-01-23_at_10928_pm.png" />
</Frame>

A neural network is composed of layers of virtual "neurons", which you can see represented on the left hand side of the NN Classifier page. An input—in our case, an MFE spectrogram—is fed into the first layer of neurons, which filters and transforms it based on each neuron's unique internal state. The first layer's output is then fed into the second layer, and so on, gradually transforming the original input into something radically different. In this case, the spectrogram input is transformed over four intermediate layers into just two numbers: the probability that the input represents noise, and the probability that the input represents a running faucet.

During training, the internal state of the neurons is gradually tweaked and refined so that the network transforms its input in *just* the right ways to produce the correct output. This is done by feeding in a sample of training data, checking how far the network's output is from the correct answer, and adjusting the neurons' internal state to make it more likely that a correct answer is produced next time. When done thousands of times, this results in a trained network.

A particular arrangement of layers is referred to as an *architecture*, and different architectures are useful for different tasks. The default neural network architecture provided by Edge Impulse will work well for our current project, but you can also define your own architectures. You can even import custom neural network code from tools used by data scientists, such as TensorFlow and Keras.

The default settings should work, and to begin training, click **Start training**. You'll see a lot of text flying past in the *Training output* panel, which you can ignore for now. Training will take a few minutes. When it's complete, you'll see the *Model* panel appear at the right side of the page:

<Frame caption="The Model panel.">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8b5049f-screenshot_2021-07-14_at_110807.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=57ba452be5f7d5dd47dd236e0626c70a" width="550" height="888" data-path=".assets/images/8b5049f-screenshot_2021-07-14_at_110807.png" />
</Frame>

Congratulations, you've trained a neural network with Edge Impulse! But what do all these numbers mean?

At the start of training, 20% of the training data is set aside for *validation*. This means that instead of being used to train the model, it is used to evaluate how the model is performing. The *Last training performance* panel displays the results of this validation, providing some vital information about your model and how well it is working. Bear in mind that your exact numbers may differ from the ones in this tutorial.

On the left hand side of the panel, *Accuracy* refers to the percentage of windows of audio that were correctly classified. The higher number the better, although an accuracy approaching 100% is unlikely, and is often a sign that your model has *overfit* the training data. You will find out whether this is true in the next stage, during model testing. For many applications, an accuracy above 80% can be considered very good.

The *Confusion matrix* is a table showing the balance of correctly versus incorrectly classified windows. To understand it, compare the values in each row. For example, in the above screenshot, all of the *faucet* audio windows were classified as *faucet*, but a few *noise* windows were misclassified. This appears to be a great result though.

The *On-device performance* region shows statistics about how the model is likely to run on-device. *Inferencing time* is an estimate of how long the model will take to analyze one second of data on a typical microcontroller (here: an Arm Cortex-M4F running at 80MHz). *Peak memory usage* gives an idea of how much RAM will be required to run the model on-device.

### 7. Classifying new data

The performance numbers in the previous step show that our model is working well on its training data, but it's extremely important that we test the model on new, unseen data before deploying it in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence.

Edge Impulse provides some helpful tools for testing our model, including a way to capture live data from your device and immediately attempt to classify it. To try it out, click on **Live classification** in the left hand menu. Your device should show up in the 'Classify new data' panel. Capture 5 seconds of background noise by clicking **Start sampling**:

<Frame caption="The Classify new data panel.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4074b41-screen_shot_2020-01-24_at_14801_pm.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=3e1b71b8c855895bedd731358f73209e" width="1438" height="832" data-path=".assets/images/4074b41-screen_shot_2020-01-24_at_14801_pm.png" />
</Frame>

The sample will be captured, uploaded, and classified. Once this has happened, you'll see a breakdown of the results:

<Frame caption="The results of classifying a new sample.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/874f2db-screen_shot_2020-01-24_at_15754_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4781437f7ab698d783d5e93d33d70963" width="1548" height="1000" data-path=".assets/images/874f2db-screen_shot_2020-01-24_at_15754_pm.png" />
</Frame>

Once the sample is uploaded, it is split into windows–in this case, a total of 41. These windows are then classified. As you can see, our model classified all 41 windows of the captured audio as *noise*. This is a great result! Our model has correctly identified that the audio was background noise, even though this is new data that was not part of its training set.

Of course, it's possible some of the windows may be classified incorrectly. Since our model was 99% accurate based on its validation data, you can expect that at least 1% of windows will be classified wrongly—and likely much more than this, since our validation data doesn't represent every possible type of background or faucet noise. If your model didn't perform perfectly, don't worry. We'll get to troubleshooting later.

<Warning>
  **Misclassifications and uncertain results**

  It's inevitable that even a well-trained machine learning model will sometimes misclassify its inputs. When you integrate a model into your application, you should take into account that it will not always give you the correct answer.

  For example, if you are classifying audio, you might want to classify several windows of data and average the results. This will give you better overall accuracy than assuming that every individual result is correct.
</Warning>

### 8. Model testing

Using the *Live classification* tab, you can easily try out your model and get an idea of how it performs. But to be really sure that it is working well, we need to do some more rigorous testing. That's where the *Model testing* tab comes in. If you open it up, you'll see the sample we just captured listed in the *Test data* panel:

<Frame caption="The Test data panel.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/70289d3-screen_shot_2020-01-24_at_24408_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=cd8b7fc03fdd6eff7dbf1cd35a5effde" width="1600" height="485" data-path=".assets/images/70289d3-screen_shot_2020-01-24_at_24408_pm.png" />
</Frame>

In addition to its training data, every Edge Impulse project also has a test dataset. Samples captured in *Live classification* are automatically saved to the test dataset, and the *Model testing* tab lists all of the test data.

To use the sample we've just captured for testing, we should correctly set its expected outcome. Click the `⋮` icon and select **Edit expected outcome**, then enter `noise`. Now, select the sample using the checkbox to the left of the table and click **Classify selected**:

<Frame caption="Test data classification results.">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/c324c29-screen_shot_2020-01-24_at_35606_pm.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=8fa38b0fe8e016c0c60fb7e2fb02fa26" width="1600" height="313" data-path=".assets/images/c324c29-screen_shot_2020-01-24_at_35606_pm.png" />
</Frame>

You'll see that the model's accuracy has been rated based on the test data. Right now, this doesn't give us much more information that just classifying the same sample in the *Live classification* tab. But if you build up a big, comprehensive set of test samples, you can use the *Model testing* tab to measure how your model is performing on real data.

Ideally, you'll want to collect a test set that contains a minimum of 25% the amount of data of your training set. So, if you've collected 10 minutes of training data, you should collect at least 2.5 minutes of test data. You should make sure this test data represents a wide range of possible conditions, so that it evaluates how the model performs with many different types of inputs. For example, collecting test audio for several different faucets is a good idea.

You can use the *Data acquisition* tab to manage your test data. Open the tab, and then click **Test data** at the top. Then, use the *Record new data* panel to capture a few minutes of test data, including audio for both background noise and faucet. Make sure the samples are labelled correctly. Once you're done, head back to the *Model testing* tab, select all the samples, and click **Classify selected**:

<Frame caption="Test results for a large number of samples.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7c0f6f0-screen_shot_2020-01-24_at_41301_pm.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=0996313a1169245b2f3d27d35f2b35ca" width="1600" height="783" data-path=".assets/images/7c0f6f0-screen_shot_2020-01-24_at_41301_pm.png" />
</Frame>

The screenshot shows classification results from a large number of test samples (there are more on the page than would fit in the screenshot). The panel shows that our model is performing at 85% accuracy, which is 5% less than how it performed on validation data. It's normal for a model to perform less well on entirely fresh data, so this is a successful result. Our model is working well!

For each test sample, the panel shows a breakdown of its individual performance. For example, one of the samples was classified with only 62% accuracy. Samples that contain a lot of misclassifications are valuable, since they have examples of types of audio that our model does not currently fit. It's often worth adding these to your training data, which you can do by clicking the `⋮` icon and selecting **Move to training set**. If you do this, you should add some new test data to make up for the loss!

Testing your model helps confirm that it works in real life, and it's something you should do after every change. However, if you often make tweaks to your model to try to improve its performance on the test dataset, your model may gradually start to overfit to the test dataset, and it will lose its value as a metric. To avoid this, continually add fresh data to your test dataset.

<Danger>
  **Data hygiene**

  It's extremely important that data is never duplicated between your training and test datasets. Your model will naturally perform well on the data that it was trained on, so if there are duplicate samples then your test results will indicate better performance than your model will achieve in the real world.
</Danger>

### 9. Model troubleshooting

If the network performed great, fantastic! But what if it performed poorly? There could be a variety of reasons, but the most common ones are:

1. The data does not look like other data the network has seen before. This is common when someone uses the device in a way that you didn't add to the test set. You can add the current file to the test set by adding the correct label in the 'Expected outcome' field, clicking `⋮`, then selecting **Move to training set**.
2. The model has not been trained enough. Increase number of epochs to `200` and see if performance increases (the classified file is stored, and you can load it through 'Classify existing validation sample').
3. The model is overfitting and thus performs poorly on new data. Try reducing the number of epochs, reducing the learning rate, or adding more data.
4. The neural network architecture is not a great fit for your data. Play with the number of layers and neurons and see if performance improves.

As you see, there is still a lot of trial and error when building neural networks. Edge Impulse is continually adding features that will make it easier to train an effective model.

### 10. Deploying to your device

With the impulse designed, trained and verified you can deploy this model back to your device. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the MFE algorithm, neural network weights, and classification code - in a single C++ library that you can include in your embedded software.

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

This will capture audio from the microphone, run the MFE code, and then classify the spectrogram:

```
Starting inferencing in 2 seconds...
Recording
Recording OK
Predictions (DSP: 399 ms., Classification: 175 ms., Anomaly: 0 ms.):
    faucet: 0.03757
    noise: 0.96243
Starting inferencing in 2 seconds...
```

Great work! You've captured data, trained a model, and deployed it to an embedded device. It's time to celebrate—by pouring yourself a nice glass of water, and checking whether the sound is correctly classified by you model.

<Frame caption="Machine learning is thirsty work.">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7767b5d-cat_water.gif?s=5a8f5c39f998a6672b4f273d4c0f8ba6" width="500" height="250" data-path=".assets/images/7767b5d-cat_water.gif" />
</Frame>

### 11. Conclusion

Congratulations! you've used Edge Impulse to train a neural network model capable of recognizing a particular sound. There are endless applications for this type of model, from monitoring industrial machinery to recognizing voice commands. Now that you've trained your model you can integrate your impulse in the firmware of your own embedded device, see the [Deployments](/hardware/deployments) tutorials. There are examples for Mbed OS, Arduino, STM32CubeIDE, and any other target that supports a C++ compiler.

Or if you're interested in more, see our tutorials on [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) or [Image classification](/tutorials/end-to-end/image-classification). If you have a great idea for a different project, that's fine too. Edge Impulse lets you capture data from any sensor, build [custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) to extract features, and you have full flexibility in your Machine Learning pipeline with the learning blocks.

We can't wait to see what you'll build! 🚀


Built with [Mintlify](https://mintlify.com).