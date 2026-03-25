# Source: https://docs.edgeimpulse.com/projects/expert-network/predictive-maintenance-using-audio-classification-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Predictive Maintenance Using Audio Classification - Arduino Nano 33 BLE Sense

Created By: Shebin Jose Jacob

Public Project Link: [https://studio.edgeimpulse.com/public/162492/latest](https://studio.edgeimpulse.com/public/162492/latest)

## Intro

Every manufacturing environment is equipped with machines. For a better-performing manufacturing unit, the health of machines plays a major role and hence maintenance of the machines is important. We have three strategies of maintenance namely - Preventive maintenance, Corrective maintenance, and Predictive maintenance.

If you want to find the best balance between preventing failures and avoiding over-maintenance, Predictive Maintenance (PdM) is the way to go. Equip your factory with relatively affordable sensors to track temperature, vibrations, and motion data, use predictive techniques to schedule maintenance when a failure is about to occur, and you'll see a nice reduction in operating costs.

In the newest era of technology, teaching computers to make sense of the acoustic world is now a hot research topic. So in this project, we use sound to do some predictive maintenance using an Arduino Nano 33 BLE Sense.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/intro.jpeg?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=eb02af4252367c9a73facaf3d8cf6b9b" width="1500" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/intro.jpeg" />
</Frame>

## How Does It Work?

We use the Nano 33 BLE Sense to listen to the machine continuously. The MCU runs an ML model which is trained on two sets of acoustic anomalies and a normal operation mode. When the ML model identifies an anomaly, the operator is immediately notified and the machine may be shut down for maintenance after proper inspection. Thus, we can reduce the possible damage caused and can reduce the downtime.

## Hardware Requirements

* Nano 33 BLE Sense
* LED

## Software Requirements

* Edge Impulse
* Arduino IDE

## Hardware Setup

The hardware setup consists of a Nano 33 BLE Sense, which is placed beside an old AC motor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/motor.jpeg?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=e5bc31fae2455ef7e13e5d639f530453" width="740" height="493" data-path=".assets/images/predictive-maintenance-with-sound/motor.jpeg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/nano.jpeg?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=3b91a4ff2b5be612e19c829919e6d7d4" width="1568" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/nano.jpeg" />
</Frame>

## Software Setup

If you haven't connected the device to Edge Impulse dashboard, follow [this tutorial](/hardware/boards/arduino-nano-33-ble-sense) to get it connected. After a successful connection, it should be present in the **Devices** tab.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/devices.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=cd37e13e77e2567edcaecd3d6021ba0d" width="1600" height="923" data-path=".assets/images/predictive-maintenance-with-sound/devices.png" />
</Frame>

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. Follow [this tutorial](https://www.edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) to learn more about it.

## TinyML Model Generation

### 1. Data Collection

Clean data is the most important requirement to train a well-performing model. In our case, we have collected 3 classes of sound - two classes of anomalies, one normal operation class, and a noise class. Each sample is 2 seconds long. The raw data of these classes is visualised below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/data-1.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=a736239dd6afbf1917e07db62669bd74" width="1359" height="880" data-path=".assets/images/predictive-maintenance-with-sound/data-1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/data-2.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=6a028563f49c921212e9c634f67f9409" width="1367" height="885" data-path=".assets/images/predictive-maintenance-with-sound/data-2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/data-3.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=6429ce30f94676acf01caa2d453b0e92" width="1370" height="881" data-path=".assets/images/predictive-maintenance-with-sound/data-3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/data-4.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=d6217c4a12531e663fcee12546d8cb07" width="1375" height="882" data-path=".assets/images/predictive-maintenance-with-sound/data-4.png" />
</Frame>

If the data is not split into training and testing datasets, split the dataset into training and testing datasets in the ratio 80:20, which forms a good dataset for model training.

### 2. Impulse Design

An Impulse is the machine learning pipeline that takes raw data, uses signal processing to extract features, and then uses a learning block to classify new data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/impulse.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=090510edec580e16f7556f57df60d341" width="1600" height="924" data-path=".assets/images/predictive-maintenance-with-sound/impulse.png" />
</Frame>

Here we are using the **Time Series data** as the input block. Now, we have two choices for the processing block - MFCC and MFE. As we are dealing with non-vocal audio and MFE performs well with non-vocal audio, we have chosen **MFE** as our processing block. We have used **Classification** as our learning block since we have to learn patterns and apply them to new data to categorize the audio into one of the given 4 classes.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/parameters.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=8a4ed77f8765a2d52f9c5776b9908fd9" width="1600" height="926" data-path=".assets/images/predictive-maintenance-with-sound/parameters.png" />
</Frame>

In the **MFE** tab, you can tweak the parameters if you're good with audio handling, else leave the settings as it is and generate features.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/features.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=09154e4f69b374bd2a5bca0b63098994" width="1600" height="925" data-path=".assets/images/predictive-maintenance-with-sound/features.png" />
</Frame>

### 3. Model Training and Testing

Now that we have our Impulse designed, let's proceed to train the model. The settings we employed for model training are depicted in the picture. You can play about with the model training settings so that the trained model exhibits a higher level of accuracy, but be cautious of overfitting.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/training.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=6df1cadf3a7a5555d4cd65546fcff4d0" width="939" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/training.png" />
</Frame>

A whopping 94.7% accuracy is achieved by the trained model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yRS4dkKDI2LDSlCA/.assets/images/predictive-maintenance-with-sound/accuracy.png?fit=max&auto=format&n=yRS4dkKDI2LDSlCA&q=85&s=61dec3802b94038b8ae3bf54ac42ea54" width="1600" height="926" data-path=".assets/images/predictive-maintenance-with-sound/accuracy.png" />
</Frame>

Let's now use some unknown data to test the model's functionality. To assess the model's performance, move on to **Model Testing** and **Classify All**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/model-testing.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=387478374076af12dd8e60ba90eac6c4" width="1600" height="925" data-path=".assets/images/predictive-maintenance-with-sound/model-testing.png" />
</Frame>

We have got 95.07% testing accuracy, which is pretty awesome. Now let's test the model with some real-world data. Navigate to **Live Classification** and collect some data from the connected device.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yRS4dkKDI2LDSlCA/.assets/images/predictive-maintenance-with-sound/classification-1.jpeg?fit=max&auto=format&n=yRS4dkKDI2LDSlCA&q=85&s=5a28b0a1ba641d52dae92b5410ede7e7" width="1600" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/classification-1.jpeg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yRS4dkKDI2LDSlCA/.assets/images/predictive-maintenance-with-sound/classification-2.jpeg?fit=max&auto=format&n=yRS4dkKDI2LDSlCA&q=85&s=a2bb594f8b211711f72ae5100a65c8db" width="1600" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/classification-2.jpeg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yRS4dkKDI2LDSlCA/.assets/images/predictive-maintenance-with-sound/classification-3.jpeg?fit=max&auto=format&n=yRS4dkKDI2LDSlCA&q=85&s=7b9c500612e3312d726b70d07bbf30f9" width="1600" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/classification-3.jpeg" />
</Frame>

We have collected some real-world data of **Normal Operation Mode**, **Anomaly 1**, and **Anomaly 2** respectively, and all of them are correctly classified. So our model is ready for deployment.

## Deployment

For deployment, navigate to the **Deployment** tab, select **Arduino Library** and build the library. It will output a zip library, which can be added to **Arduino IDE**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/deployment.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=d7e88667e8c9ccc7180e6775bb35b2dd" width="1164" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/deployment.png" />
</Frame>

## Final Product

Nano 33 BLE Sense along with an LED is enclosed in a 3D printed case, which is our final product. The device is capable of identifying acoustic anomalies in a machine and alerts the user using the alert LED.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/product.jpeg?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=ef84491b52ef5fb150c6cb0b5b05492a" width="1500" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/product.jpeg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/predictive-maintenance-with-sound/intro.jpeg?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=eb02af4252367c9a73facaf3d8cf6b9b" width="1500" height="1000" data-path=".assets/images/predictive-maintenance-with-sound/intro.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).