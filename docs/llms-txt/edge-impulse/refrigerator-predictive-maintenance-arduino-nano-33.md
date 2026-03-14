# Source: https://docs.edgeimpulse.com/projects/expert-network/refrigerator-predictive-maintenance-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refrigerator Predictive Maintenance - Arduino Nano 33 BLE Sense

Created By: Swapnil Verma

Public Project Link: [https://studio.edgeimpulse.com/public/115503/latest](https://studio.edgeimpulse.com/public/115503/latest)

GitHub Repo: [https://github.com/sw4p/Refrigerator\_Predictive\_Maintenance](https://github.com/sw4p/Refrigerator_Predictive_Maintenance)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/refrigerator-predictive-maintenance/intro.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=a469a7c7e1f11ad7b3ef80fcb9b7b9cc" width="900" height="675" data-path=".assets/images/refrigerator-predictive-maintenance/intro.jpg" />
</Frame>

## Story

### Problem

A refrigerator is one of our home's most common and useful appliances. It has changed society and culture by improving the quality of life for people. Refrigerator has increased food accessibility, and food preservation has become so much easier, thus also reducing food wastage.

Refrigerator has another significant impact on the medical sector. It has made preserving and transporting certain medicines, including vaccines, easier, thus increasing accessibility. If a refrigerator storing medicine fails, it will spoil the medicines or reduce their effectiveness.

Considering the importance of a refrigerator in our lives, I am trying to make something to predict a refrigerator failure allowing predictive maintenance in this project.

### My Solution

My proposed solution is to use a machine learning (ML) model to identify a failure as soon as possible using the temperature and humidity changes in a refrigerator. Project Link: [https://studio.edgeimpulse.com/public/115503/latest](https://studio.edgeimpulse.com/public/115503/latest)

### Data

A good machine learning model starts with a good dataset. Sadly, I could not find any open dataset of temperature and humidity levels inside a refrigerator, so I decided to build one.

A machine learning model needs at least two kinds of data to identify refrigerator failure.

* Normal operation data - Time-series data from a normally working refrigerator.
* Abnormal operation data - Time-series data from a faulty refrigerator.

Different kinds of faults may generate a different pattern in data. For example, a non-working [compressor](https://www.hunker.com/12000409/how-does-a-refrigerator-compressor-work) will never decrease the temperature when it stops working. In contrast, a clogged or dirty coil may force the compressor to work harder than usual, taking more time to achieve the target temperature.

Unfortunately, I do not have access to a faulty refrigerator for data collection; therefore, I have simulated "abnormal operation" data by

* Keeping the fridge door open for an extended period.

This event should increase the temperature and hopefully force the compressor to work harder, thus simulating a fault state.

`1. Dataset Preparation`

The parameters I want to capture are:

* Temperature
* Humidity
* Illumination - To check the door open/close status. The ML model will not use this parameter, and it is only to help us in visualising and understanding the data.

To capture the above data, I need:

* A temperature sensor
* A humidity sensor
* A light intensity sensor
* A microcontroller board
* An SD card module
* A battery

I already have an Arduino BLE sense with a temperature and a humidity sensor attached to an nRF52840 microcontroller; however, I did not have an SD card module for permanent data recording. For this, I used an Arduino portenta with a vision shield which has SD card support. My convoluted data collection and recording setup is illustrated in the figure below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/dataset-1.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=0cde32cf039654153fc8dacbc379fcf3" width="1280" height="400" data-path=".assets/images/refrigerator-predictive-maintenance/dataset-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/dataset-2.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=37fd37bdce43fb973d6fa987de0ac163" width="720" height="960" data-path=".assets/images/refrigerator-predictive-maintenance/dataset-2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/dataset-3.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=d754e3e2e9b05bac4d640a722c018f79" width="720" height="960" data-path=".assets/images/refrigerator-predictive-maintenance/dataset-3.jpg" />
</Frame>

So this is my convoluted setup. The Arduino BLE sense does the data collection and data formatting and sends it over BLE to the Arduino Portenta, which then permanently records that data in a microSD card.

`2. Software for Dataset Preparation`

The software used in the Arduino BLE sense and Arduino portenta for the data collection is available from [this](https://github.com/sw4p/Refrigerator_Predictive_Maintenance) GitHub page.

`https://github.com/sw4p/Refrigerator_Predictive_Maintenance`

The *Dataset\_Collector.ino* is for the Arduino BLE sense, and the *Data\_Recorder.ino* is for the Arduino Portenta H7 with a Vision Shield.

The Arduino BLE sense records temperature, humidity and illumination reading every 200ms. The *illumination* data is used to detect when the fridge door is open. If *illumination* is greater than 0, then the fridge door is open.

`3. Data Visualization`

The recorded data is in CSV (Comma Separated Value) format, and it looks like this.

```
timestamp,temperature,humidity,illumination
1,9.68,69.01,0
2,9.68,69.03,0
3,9.66,68.96,0
4,9.68,69.07,0
5,9.69,68.96,0
6,9.68,68.98,0
7,9.69,68.95,0
8,9.69,69.06,0
9,9.68,69,0
10,9.68,68.99,0
11,9.64,68.97,0
12,9.71,68.89,0
13,9.64,68.99,0
14,9.69,69,0
15,9.69,68.94,0
16,9.69,68.96,0
17,9.66,68.95,0
18,9.64,68.9,0
19,9.64,68.89,0
20,9.66,68.93,0
21,9.64,68.92,0
22,9.73,68.92,0
```

Most of the data is collected continuously for 7 to 8 hours at an interval of roughly 200ms. Let's see what the data looks like by plotting it.

<Frame caption="Normal operation of the fridge">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/fridge-1.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=41225d1625e66692ffbc42505f283d02" width="1280" height="391" data-path=".assets/images/refrigerator-predictive-maintenance/fridge-1.jpg" />
</Frame>

Here the orange plot is humidity, blue is temperature and grey (not visible because it is on top of the X-axis) is the illumination level in the fridge. Section A shows the temperature and humidity settling in a rhythm, and Section B shows the data in a rhythm after they have settled. Let's check another set of data.

<Frame caption="Normal operation of the fridge">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/fridge-2.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=89a8315d25cfa5d8821bc3bf75c99db6" width="1280" height="182" data-path=".assets/images/refrigerator-predictive-maintenance/fridge-2.jpg" />
</Frame>

<br />

<Frame caption="Normal operation of the fridge">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/fridge-3.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=750307a6db065a5a04dc071a3cb69f6a" width="1280" height="327" data-path=".assets/images/refrigerator-predictive-maintenance/fridge-3.jpg" />
</Frame>

The above graph also shows data collected for 7-8 hours. In the first graph, only temperature (blue) and humidity (orange) levels are shown, whereas, in the second graph, the illumination (grey) is also illustrated. As mentioned before, illumination is recorded to capture the door opening and closing of the refrigerator. Section A is temperature and humidity levels settling, and section B is the normal working of the refrigerator, showing the rhythm of heating and cooling cycles. Section C shows the sudden rise in temperature and humidity levels because I opened the refrigerator door in the morning.

<Frame caption="Zoomed-in view of the normal operation">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/fridge-4.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=17bc0cd7ee3d0be8726b179ccae2158e" width="1280" height="449" data-path=".assets/images/refrigerator-predictive-maintenance/fridge-4.jpg" />
</Frame>

The above image shows a zoomed-in view of the normal operation of a refrigerator. We can clearly see a cooling and heating cycle. Please note that this cooling and heating cycle takes place over a long duration.

So far, we have seen data showing the normal operation; let's check data showing the abnormal operation of a refrigerator.

<Frame caption="Simulated abnormal operation of the fridge">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/abnormal.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=d5bd9ec7cff31edc0dd9c7675e2bc312" width="1280" height="305" data-path=".assets/images/refrigerator-predictive-maintenance/abnormal.jpg" />
</Frame>

In the above graph, section A is the settling period, and section B is the normal operation period. Section C is the simulated "abnormal operation" period, where the fridge door was kept open for a long duration. Section D shows the data after the fridge door was closed.

<Frame caption="Zoomed-in view of the abnormal operation">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/abnormal-2.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=fbf92752b4348cb5c64d8539103a06b7" width="1280" height="898" data-path=".assets/images/refrigerator-predictive-maintenance/abnormal-2.jpg" />
</Frame>

The temperature and humidity levels rose quickly when the fridge door was kept open. We can also see that compressor is trying to bring the temperature down, but it is taking a very long time, and as soon as the compressor stops working, the temperature level rise again quickly. It's almost inverse to the cooling-heating cycle of the normal operation.

`4. Data Classes`

As mentioned previously, due to the unavailability of a faulty refrigerator, I have simulated the abnormal operation using just one technique. That gives me only two classes of data - normal operation and abnormal operation. Let's make most of what I have got.

### Training

For training my ML model, I used [Edge Impulse](https://edgeimpulse.com/). Edge impulse is a fantastic tool for building ML solutions quicker.

Edge Impulse has many excellent features for all stages of building an ML solution. One such cool feature is [*Data Explorer*](/studio/projects/data-acquisition/data-explorer). It makes visualising the data points very easy.

<Frame caption="Data explorer">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/data-explorer.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=9f6f87efe3d8b1f777359925baad9db2" width="1280" height="797" data-path=".assets/images/refrigerator-predictive-maintenance/data-explorer.jpg" />
</Frame>

The above image shows the data explorer feature of the Edge Impulse. As you can see, I have three types of data a) normal\_operation, which captures only the normal working of the refrigerator. b) Anomalous\_DO, which captures only the abnormal operation and c) Combined, which captures normal and abnormal operation.

For the kind of data I have, an anomaly detection model would be perfect for this project. Thankfully, Edge Impulse provides a [K-means anomaly detection](/studio/projects/learning-blocks/blocks/anomaly-detection-k-means) model out of the box, so there is no need to prepare my own.

<Frame caption="Impulse creation">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/refrigerator-predictive-maintenance/impulse.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=54b5b10b5cf0a583f2d2db7e1d08b794" width="1280" height="674" data-path=".assets/images/refrigerator-predictive-maintenance/impulse.jpg" />
</Frame>

Please follow edge impulse documentation for [Impulse creation](/studio/projects/impulse-design), data [pre-processing](/studio/projects/processing-blocks) and [training](/studio/projects/learning-blocks) an ML model.

### Testing

For testing the ML model, Edge Impulse provides two methods:

a) [Model testing](/studio/projects/model-testing)

b) [Live classification](/studio/projects/live-classification)

In this project, I have primarily used the model testing method because I already had a lot of data captured. In the [data acquisition](/studio/projects/data-acquisition) tab, I assigned some data as test data, which are only used in the model testing.

<Frame caption="Model testing">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/refrigerator-predictive-maintenance/model-testing.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=fcbaf734557b7c5b8c5f28142a1e584a" width="1280" height="659" data-path=".assets/images/refrigerator-predictive-maintenance/model-testing.jpg" />
</Frame>

In the model testing tab, click on the *classify all* to test the model. You can also set the [confidence thresholds](/studio/projects/model-testing#setting-confidence-threshold) by clicking on the three dots beside *classify all*.

<Frame caption="Set Confidence Thresholds">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/confidence.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=366ee13c50ded488516ebd9c6908ea37" width="1280" height="582" data-path=".assets/images/refrigerator-predictive-maintenance/confidence.jpg" />
</Frame>

As you can see from the *model testing* image above that the ML model is performing amazingly well. It is properly classifying a *normal\_operation* sample as *no anomaly* and *Anomalous\_DO* as *all anomaly*. It is also correctly classifying the *combined* samples into some anomaly and some no anomaly data points.

To closely examine a classified sample, click on the three dots on a sample and select *show classification*.

<Frame caption="Show Classification">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/classification.gif?s=592815f8f6d4d51a606b6a3ae032335a" width="1106" height="426" data-path=".assets/images/refrigerator-predictive-maintenance/classification.gif" />
</Frame>

That will open a classification result page where you can scroll through the data points to evaluate individual classification window and their anomaly score. This page also has helpful graphs for visualising raw, pre-processed and classified samples.

<Frame caption="Classification Result">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/classification-results.gif?s=bc931146f512bd7ece310dc4f088b8f2" width="1572" height="1126" data-path=".assets/images/refrigerator-predictive-maintenance/classification-results.gif" />
</Frame>

As you can see from the above *classification result*, the ML model has absolutely nailed the classification. It is correctly detecting anomalous data from a combined sample.

It is not always this perfect, though. There are some outliers which slip through. For example, in the classification result below, the model has detected some anomalies and inspecting the raw data shows that they should not be an anomaly. However, it gives me great relief that such outliers are very low in number and can easily be removed using better sensors and improving the data quality.

<Frame caption="Wrong Classification">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/refrigerator-predictive-maintenance/wrong-classification.jpg?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=9627728847244659f0439e16a708140e" width="1258" height="960" data-path=".assets/images/refrigerator-predictive-maintenance/wrong-classification.jpg" />
</Frame>

### Deployment

Edge Impulse fully supports the Arduino Nano BLE sense development board, so the best way to [deploy](/studio/projects/deployment) this ML model would be to build firmware.

<Frame caption="Prepare a firmware">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/deployment.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=88d85a8d195b32a7e787d92f89d0f713" width="1280" height="865" data-path=".assets/images/refrigerator-predictive-maintenance/deployment.jpg" />
</Frame>

Go to the deployment page -> click on the microcontroller board or environment of choice and click build. After building the firmware, the download should start automatically.

<Frame caption="Flash scripts and firmwares">
  <img src="https://mintcdn.com/edgeimpulse/tNkJb9FywquQpS7r/.assets/images/refrigerator-predictive-maintenance/firmware.jpg?fit=max&auto=format&n=tNkJb9FywquQpS7r&q=85&s=c76c43598869c59ccf8af3cf6fb14261" width="920" height="364" data-path=".assets/images/refrigerator-predictive-maintenance/firmware.jpg" />
</Frame>

After extracting the zip folder, run the script\_\<os\_name> file corresponding to your computer's operating system to flash the firmware onto the microcontroller board.


Built with [Mintlify](https://mintlify.com).