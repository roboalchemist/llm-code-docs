# Source: https://docs.edgeimpulse.com/projects/expert-network/warehouse-shipment-monitoring-silabs-thunderboard-sense-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Warehouse Shipment Monitoring - SiLabs Thunderboard Sense 2

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/142224/latest](https://studio.edgeimpulse.com/public/142224/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/thunderboard.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=d3129415442d030fc6590fb631137ffd" width="382" height="360" data-path=".assets/images/warehouse-shipment-monitoring/thunderboard.jpg" />
</Frame>

## Problem Statement

Monitoring fragile objects during shipment require more time, care, labor effort, and infrastructure support.

In an ideal scenario, shipments would travel from the warehouse directly into the hands of the customer. However, that is not always the case. In between, a shipment / package will be handled many times, and you can’t always expect the people doing the transportation to handle them in a manner that will not lead to damage.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/intro.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=1649bbc01d063d567f3285545af6a43f" width="1600" height="609" data-path=".assets/images/warehouse-shipment-monitoring/intro.jpg" />
</Frame>

Here are a few challenges with logistics of fragile items:

* In a warehouse, storing fragile objects in the wrong position can damage the product.
* No real time monitoring of the shipments *inside* a warehouse about placement of products.
* Handling the shipment in the wrong position during transferring to the destination might cause damage to the product.
* Computer Vision-based shipment monitoring requires infrastructure to support it. For example, poor lightning conditions might affect the prediction.

## TinyML Solution

I have created a TinyML model which can be attached to a fragile package and it tracks and predicts the position of the package, with the results communicated to a Mobile application through BLE.

For hardware, I have used the [SiLabs Thunderboard Sense 2](https://www.silabs.com/development-tools/thunderboard/thunderboard-sense-two-kit?tab=overview) and Edge Impulse to train the model and deploy it to the Thunderboard Sense 2.

The predicted result will be one of four categories:

* Correct position
* Incorrect position - Upside-down
* Incorrect position - Tilted forward
* Incorrect position - Tilted backward

## Data Acquisition

Connect the Thunderboard Sense 2 board to the system and flash the firmware from this [link](/hardware/boards/silabs-thunderboard-sense-2).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/load-firmware.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=4eb518d2a271590e8b466ec81b1eff1c" width="1562" height="428" data-path=".assets/images/warehouse-shipment-monitoring/load-firmware.jpg" />
</Frame>

Once it is flashed, run the below command:

`edge-impulse-daemon`

Now the board is connected to your Edge Impulse account. Then place the hardware in a case, and attach it to the shipment package. In the below picture, you'll notice that the Thunderboard is placed inside the case and mounted *on top* of the package. Now collect the accelerometer data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/acquisition-1.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=df5cff5e713759e8370dc3bd27645458" width="1333" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/acquisition-1.jpg" />
</Frame>

Now it’s time to collect the dataset for each of the categories.

### Correct Position

Let’s assume the package with fragile object is orientated correctly. Place the Thunderboard on top of it, for data acquisition. Now start moving the package with this position, while data acquisition is running. Collect a dataset of around 2 minutes 30 seconds.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/acquisition-1.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=df5cff5e713759e8370dc3bd27645458" width="1333" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/acquisition-1.jpg" />
</Frame>

### Incorrect Position - Upside-down

Turn the package over so that it is upside down, with the hardware still on it. Now start moving the package in this position, while data acquisition is running. Collect a dataset of around 2 minutes 30 seconds.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/upside-down.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=46e75a97a6789ac0464e26777582c231" width="1333" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/upside-down.jpg" />
</Frame>

### Incorrect Position - Tilted Forward

Turn the package on it's side, with the hardware still on it, facing forward. Now start moving the package in this position, while data acquisition is running. Collect a dataset of around 2 minutes 30 seconds.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/tilt.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=0171e1c4a5bf9f6ea9d5dd9f07aa7150" width="750" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/tilt.jpg" />
</Frame>

### Incorrect Position - Tilted Backward

Turn the package on it's side, with the hardware still on it, facing backward. Now start moving the package in this position, while data acquisition is running. Collect a dataset of around 2 minutes 30 seconds.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/tilt-back.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=a40972a4962dac83fb8ca41144db11e9" width="750" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/tilt-back.jpg" />
</Frame>

Back in the Studio, move approximately 30 seconds of data from each category to Test data. The [Training and Test dataset](/studio/projects/data-acquisition#dataset-train%2Ftest-split-ratio) ratio should be split about 80:20.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/train-test.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=2ce94193ef5b75a21954cb536bb9039d" width="1600" height="761" data-path=".assets/images/warehouse-shipment-monitoring/train-test.jpg" />
</Frame>

After data collection is completed, now go the Impulse settings and select Raw data in Processing. A Window size of 3000ms and Window increase of 500 ms is good.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/impulse.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=ff09021d1e3342af183498c791724d84" width="1600" height="767" data-path=".assets/images/warehouse-shipment-monitoring/impulse.jpg" />
</Frame>

The generated Feature map from the raw data should look similar to this:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/feature-explorer.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=40de1208ea1e7e6587bb833bf088e6cc" width="1390" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/feature-explorer.jpg" />
</Frame>

## Neural Network Training

In the Neural network training, I have used sequential layers with a Dense neural network layer and drop out of 0.1 to avoid the over fitting. I have chosen the learning rate as 0.0005 and 200 training cycles.

Upon completion, the training model Accuracy is 100%:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/training.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=ba8b300f20b44c5093d1ec89075e7e27" width="1422" height="712" data-path=".assets/images/warehouse-shipment-monitoring/training.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/training-2.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=49d111ac4a5fced9de13073ad40e5625" width="867" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/training-2.jpg" />
</Frame>

## Model Testing

In the Model testing section, I have tested the trained model with the 30-second dataset that we set aside earlier for each category.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/testing.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=bdc0ca5fa18bee976ac2c8301f5fc8f0" width="1600" height="452" data-path=".assets/images/warehouse-shipment-monitoring/testing.jpg" />
</Frame>

The trained model achieved 100% accuracy using the unseen testing data. This confirms the model performs great in predictions. Now the next stage is to test it in real use-case scenario.

For this, we need to deploy this model directly to the SiLabs Thunderboard Sense 2.

## Deployment

Go to the Deployment section, and select Firmware option "Thunderboard Sense 2". This will generate and download the firmware to your local system.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/deployment.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=3c49731524ba7863b7ad266383b4262d" width="1600" height="642" data-path=".assets/images/warehouse-shipment-monitoring/deployment.jpg" />
</Frame>

Once the firmware is downloaded, copy the `.bin` file and paste it in the TB004 drive attached to your PC. This will flash the software onto the Thunderboard Sense 2 board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/firmware.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=dff21a3ae89f8677327e8ca7230a730a" width="252" height="282" data-path=".assets/images/warehouse-shipment-monitoring/firmware.jpg" />
</Frame>

Once it is flashed, Reset the board. Connect the 3v battery into it.

## Testing in the Real World

To test it out in a real scenario, download the ["LightBlue"](https://apps.apple.com/us/app/lightblue/id557428110) app from the iOS App Store or Google Play store. This app will be used to communicate to with the Thunderboard Sense 2.

Open the App and connect to the Edge Impulse service (Make sure board is powered on).

Input settings in the application:

* Subscribe to the `2A56` characteristic.
* Decode the message as UTF-8 (click on `HEX` in the top right corner in LightBlue to switch).
* Place the package in different positions and start moving the package.
* The app will notify the Thunderboard.

Enable the "Listening" option in the app. You will be notified only when the previous prediction result differs from current prediction result.

For different positions of a shipment package, the predicted resulted is mentioned below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/sensor.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=2d81ad073c80ec9efb4c46bf5204d993" width="463" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/sensor.jpg" />
</Frame>

## Results

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/correct-position.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=17777c34ee1bb14415aaaf1941038a3a" width="1182" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/correct-position.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/incorrect-position.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=fc0e8b5a41b8bc57e0a7461322f53766" width="1189" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/incorrect-position.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/incorrect-position-2.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=14ebd5786e311d948e870a2c1864e118" width="694" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/incorrect-position-2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/du1D1m9DE2GAQokN/.assets/images/warehouse-shipment-monitoring/incorrect-position-3.jpg?fit=max&auto=format&n=du1D1m9DE2GAQokN&q=85&s=16d91cb6502c1674453e40a91cb9952a" width="689" height="1000" data-path=".assets/images/warehouse-shipment-monitoring/incorrect-position-3.jpg" />
</Frame>

## Summary

We have seen that a TinyML-based model using accelerometer input will able to predict the placement / orientation of fragile shipments, to help avoid damage or monitor packages in a warehouse.


Built with [Mintlify](https://mintlify.com).