# Source: https://docs.edgeimpulse.com/projects/expert-network/posture-detection-for-worker-safety-silabs-thunderboard-sense-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Posture Detection for Worker Safety - SiLabs Thunderboard Sense 2

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/148375/latest](https://studio.edgeimpulse.com/public/148375/latest)

## Problem Statement

Working in manufacturing can put a lot of stress on a worker's body. Depending on the worker's role in the production process, they might experience issues related to cramped working conditions, heavy lifting, or repetitive stress.

Poor posture is another issue that can cause problems for the health of those who work in manufacturing. Along with that, research suggests that making efforts to improve posture among manufacturing employees can lead to significant increases in production. Workers can improve their posture by physical therapy, or simply by being more mindful during their work day.

Major postures include:

* Posture while sitting
* Posture while lifting

### Posture While sitting

Many manufacturing employees spend much of their day sitting in a workstation, performing a set of tasks. While the ergonomics of the workstation will make a significant difference, it is important for employees to be mindful of their sitting posture.

### Posture while lifting

Lifting can be another issue affecting the posture of those who work in manufacturing. If you are not careful, an improper lifting posture can lead to a back injury. For lifting objects off the ground, the correct posture is a "Squat" type where the incorrect posture is a "bent down" type.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/hardware.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=f7f687e2404650d8e239cc3628c549ae" width="728" height="1000" data-path=".assets/images/worker-safety-posture-detection/hardware.jpg" />
</Frame>

## TinyML Solution

I have created a wearable device using a [SiLabs Thunderboard Sense 2](/hardware/boards/silabs-thunderboard-sense-2) which can be fitted to a worker's waist. The worker can do their normal activities, and the TinyML model running on the hardware will predict the posture and communicate to the worker through BLE communication. The worker can get notified in the Light Blue App on their phone or smartwatch.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/bluetooth-app.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=45a9c00ecb77c72ab8c4501fd06751fb" width="569" height="1000" data-path=".assets/images/worker-safety-posture-detection/bluetooth-app.jpg" />
</Frame>

I have trained a model with several different postures, so that it can classify the correct movement postures while lifting and sitting, as well as incorrect postures. The model will predict results these 5 categories:

1. Correct Lift Posture - Squat
2. Incorrect Lift Posture - Bent Down
3. Correct Sitting Posture
4. Incorrect Sitting Posture
5. Walking

Now let's see how I trained the model and tested on real hardware in detail.

## Data Acquisition

Connect the Thunderboard Sense 2 board to your system and flash the firmware from this [link](/hardware/boards/silabs-thunderboard-sense-2).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/firmware.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=9b101ec180eca4e5d94645805b3cbc42" width="1562" height="428" data-path=".assets/images/worker-safety-posture-detection/firmware.jpg" />
</Frame>

Once it is flashed, run the below command.

`edge-impulse-daemon`

Now your board is connected to your Edge Impulse account.

To start to collect the data for desired postures (Correct , Incorrect) I have worn the belt with the Thunderboard Sense 2 attached, and started recording accelerometer data. The data classes acquired were walking, correct sitting posture, incorrect sitting posture , correct lifting posture (squat), and incorrect lifting posture (bent down).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/data-acquisition.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=3c39047a9ebad7beb39b00dd86ec1a28" width="805" height="1000" data-path=".assets/images/worker-safety-posture-detection/data-acquisition.jpg" />
</Frame>

### Correct Sitting Posture

I have recorded data from the Thunderboard by sitting in the correct sitting posture.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/sitting-correct.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=f3325ffa03a0f25affa1eb0e3cca80e4" width="414" height="573" data-path=".assets/images/worker-safety-posture-detection/sitting-correct.jpg" />
</Frame>

I have collected 1 minute data of correct sitting posture for model training and 20 seconds of data for testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/data-sitting-correct.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=15d88967c936f340889ff957f964271f" width="1600" height="482" data-path=".assets/images/worker-safety-posture-detection/data-sitting-correct.jpg" />
</Frame>

### Incorrect Sitting Posture

For the incorrect sitting posture, I have bent towards the laptop, where my back is not resting on the chair. If an employee works in this position for long hours, it can create back pain or other problems in the future. I have collected 1 minute data of improper sitting posture for model training, and 20 seconds of data for model testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/sitting-incorrect.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=4990efc3bc8b211b249a5683b07f13c0" width="512" height="566" data-path=".assets/images/worker-safety-posture-detection/sitting-incorrect.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/data-sitting-incorrect.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=bff04cd37b186e3a6b9f911c5d4e08ce" width="1600" height="364" data-path=".assets/images/worker-safety-posture-detection/data-sitting-incorrect.jpg" />
</Frame>

### Correct Lifting Posture

For lifting objects off the ground, the correct posture is to squat down to the object to lift it.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/lifting-correct.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=c52d7d088b0b8acd8a869bcc5bccd21e" width="532" height="612" data-path=".assets/images/worker-safety-posture-detection/lifting-correct.jpg" />
</Frame>

I have collected the "squat" type data for around two minutes for model training, and 20 seconds of data for model testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/data-lifting-correct.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=ce7ec0e45e30d31e75112c3e566c64ae" width="1600" height="475" data-path=".assets/images/worker-safety-posture-detection/data-lifting-correct.jpg" />
</Frame>

### Incorrect Lifting Posture

For incorrect lifting ("bent over") data, I have collected 2 minutes 30 seconds of data for model training, and another 30 seconds of data for model testing.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/lifting-incorrect.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=552b8bea8a452517196dbd68ab093df6" width="478" height="518" data-path=".assets/images/worker-safety-posture-detection/lifting-incorrect.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/data-lifting-incorrect.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=5065828d21aa60a0b17e3fe8aa271d43" width="1600" height="527" data-path=".assets/images/worker-safety-posture-detection/data-lifting-incorrect.jpg" />
</Frame>

## Create Impulse

In Edge Impulse, on the Create Impulse section, set the "window sampling size" to 4000ms and the "window increase size" is also set as 4000 ms. The preprocessing is selected as "raw" data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/impulse.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=45521a217743167047b1d89e9e6014ca" width="1600" height="585" data-path=".assets/images/worker-safety-posture-detection/impulse.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/feature-explorer.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=add47bb499ff5f1f2a4c54a7694bdd90" width="1460" height="662" data-path=".assets/images/worker-safety-posture-detection/feature-explorer.jpg" />
</Frame>

## Model Training

In Model training, I have used sequential dense neural networks, and the learning rate is set to 0.005 and the training cycle is 200 epochs.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/training-1.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=fcabe7ddd010eb0a1013d457a2fe8498" width="1451" height="772" data-path=".assets/images/worker-safety-posture-detection/training-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/training-2.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=cd7f21d79be5fd2d2fe9e0452760890c" width="1424" height="341" data-path=".assets/images/worker-safety-posture-detection/training-2.jpg" />
</Frame>

## Model Accuracy

After training was complete, the model achieved 100% accuracy and the F1 score is listed below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/accuracy-1.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=abcd92c2ed35235ad36487b4cab3c3ea" width="1412" height="626" data-path=".assets/images/worker-safety-posture-detection/accuracy-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/accuracy-2.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=1a79caf0c55c862dff36f1230367ddbc" width="1449" height="892" data-path=".assets/images/worker-safety-posture-detection/accuracy-2.jpg" />
</Frame>

The inference time is 7ms, and flash usage is only 78.4K.

## Model Testing

In model testing, I have used the data that we collected and set aside earlier to test the model. Here, the model achieved 87% accuracy. This data is completely new and was not used in training sessions, so it is unseen up to now. The decrease in model accuracy does sometimes occur, it looks like the improper sitting position is being incorrectly classified as "squat" data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/testing.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=ced07935cef0745be29741bf4c5733ac" width="1471" height="620" data-path=".assets/images/worker-safety-posture-detection/testing.jpg" />
</Frame>

## Deployment

Go to the Deployment section in Edge Impulse, and select the firmware option for the Thunderboard Sense 2. This will generate and download the firmware files to your system.

Once the firmware is downloaded, copy the `.bin` file and paste it in the `TB004` drive (or whatever drive label appears when the Thunderboard is connected to your computer). This will flash the software on to the Thunderboard.

Once it is flashed, reset the board, and connect a 3V battery to it.

## Testing in the Real World

To test it in a real scenario, download the LightBlue application from the Apple App Store or Google Play Store. This application will be used to communicate to the Thunderboard Sense 2 over Bluetooth.

Open the App and connect to the Edge Impulse service (Make sure board is powered up).

Some settings in the App might need to be changed to the following values:

* Subscribe to the `2A56` characteristic.
* Decode the message as `UTF8` (click on `HEX` in the top right corner in LightBlue to switch).

Connect the wearable belt and start doing different movements.

Enable the "Listening" option in the App. You will be notified only when the previous prediction result differs from the current prediction result.

You can see the results of the predictions displayed in the App:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/results-1.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=33ba4646793d0b2e5d17f78c6732387f" width="568" height="1000" data-path=".assets/images/worker-safety-posture-detection/results-1.jpg" />
</Frame>

Then open up a Terminal and run the below command to see the model inference in realtime:

`edge-impulse-run-impulse`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VHmrZA9MmYW2Why9/.assets/images/worker-safety-posture-detection/results-2.jpg?fit=max&auto=format&n=VHmrZA9MmYW2Why9&q=85&s=e10fa53c4904026997896d01df167830" width="1453" height="1000" data-path=".assets/images/worker-safety-posture-detection/results-2.jpg" />
</Frame>

## Summary

This TinyML-based wearable can be used in manufacturing warehouses, shipping, or other situations where employees lift objects on a regular basis. While this is a proof-of-concept, this type of approach could help them to correct their posture via local notifications from the mobile application.


Built with [Mintlify](https://mintlify.com).