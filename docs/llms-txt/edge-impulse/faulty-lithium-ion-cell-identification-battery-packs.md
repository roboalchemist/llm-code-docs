# Source: https://docs.edgeimpulse.com/projects/expert-network/faulty-lithium-ion-cell-identification-battery-packs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Faulty Lithium-Ion Cell Identification in Battery Packs - Seeed Wio Terminal

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/102553/latest](https://studio.edgeimpulse.com/public/102553/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/intro.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=7bfd26f9390e381d3fb5d8b746d2bc3c" width="900" height="640" data-path=".assets/images/lithium-ion/intro.jpg" />
</Frame>

## Faulty Lithium ion Cell BMS Pack

This prototype uses a Wio Terminal and Edge Impulse to predict overheated faulty cells in a BMS pack. For this project, I used an MLX 90640 Thermal Camera with the Wio Terminal to collect thermal data from a BMS pack.

A working demo of my prototype is available on YouTube here:

<iframe src="https://www.youtube.com/embed/0fzT5PdRwiQ" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Problem Statement

In an existing BMS pack, a temperature sensor is integrated with each cell pack, consisting of 14 cells, for identifying an overheated cell pack. But there is no system to identify an individual faulty cell that is overheating in a BMS pack.

<Frame caption="Existing BMS pack architecture">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/diagram-1.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=12eb23709f94697a737384ef1511f6d8" width="936" height="570" data-path=".assets/images/lithium-ion/diagram-1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/diagram-2.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=16e853ffb7dff4e7733452cf43d6871d" width="936" height="426" data-path=".assets/images/lithium-ion/diagram-2.jpg" />
</Frame>

* Only one temperature sensor is deployed to detect the overall temperature of battery packs (14 \* Li-ion Cells).
* Identifying the individual cell temperature is challenging due to infrastructure cost for a BMS pack.

Cost for deploying Temperature sensor for each cell:

* Number of cells in BMS pack: 112
* Cost of Temperature sensor: 500 INR (\$0.75 USD)
* Total cost: 112 \* 500 INR = 56,000 INR (\$760 USD) \*approx

Additionally, there is no interface support in a microcontroller to support 112 individual temperature sensor readings.

## Solution using TinyML model

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/architecture-1.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=e21bd880513279567e56fa3885c66c10" width="936" height="486" data-path=".assets/images/lithium-ion/architecture-1.jpg" />
</Frame>

I have developed a prototype by using the MLX90640 thermal camera and Wio Terminal to collect the thermal data of the BMS pack and uploaded the data sets (Label: Faulty Battery 1.....6 and "Normal" to Edge Impulse).

## Hardware Setup

In this prototype, 6 lithium-ion cells are connected to the load (Rheostat) and the MLX90640 and Wio Terminal are attached to the stand where the MLX90640 thermal camera is facing downwards over the lithium-ion cells.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/prototype.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=31d9bb6da2a10dcd363ad625caf2f9d0" width="936" height="602" data-path=".assets/images/lithium-ion/prototype.jpg" />
</Frame>

## Algorithm

The MLX90640 sends 32x24 thermal data to the Wio Terminal through I2C. Since this project focuses on identifying an overheated cell in the pack, I have used simple filtering logic to filter out the normal cell temperature by setting it to zero.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/algorithm.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=e0851e6b953673cd974b47a47a4928cf" width="936" height="690" data-path=".assets/images/lithium-ion/algorithm.jpg" />
</Frame>

Upload the datasets created for this project from the below link.

Go to Edge Impulse -> Data acquisition and then the Uploader option to upload the datasets.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/acquisition.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=211d39a70756a058978ee02495faf311" width="936" height="334" data-path=".assets/images/lithium-ion/acquisition.jpg" />
</Frame>

If you want to develop new datasets from scratch, flash the below code to the Wio Terminal using the Arduino IDE. For that, you need to configure Wio Terminal setup in the Arduino IDE. Please follow this link to get setup: [https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)

This code will print the thermal data in array format, later it can be converted to .csv format as mentioned in the above datasets. Ideally the .csv data looks like this:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/csv.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=d23e4582839d746e373f0cc1e6e44169" width="442" height="954" data-path=".assets/images/lithium-ion/csv.jpg" />
</Frame>

Once the datasets are uploaded, then in the "Create impulse" section change the Window size to 768 ( 24\*32 = 768 ).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/impulse.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=673df6bf2d797147ce75db00aa98aa87" width="936" height="390" data-path=".assets/images/lithium-ion/impulse.jpg" />
</Frame>

Next, in Feature Explorer, we can see the generated raw features of thermal data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/features.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=0bfdf1ef76faa50857c77bc41d70f915" width="936" height="330" data-path=".assets/images/lithium-ion/features.jpg" />
</Frame>

## Neural Network Configuration

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/neural-network.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=ae8f4dc1c4ce98de8aea3c226a29a1d9" width="936" height="416" data-path=".assets/images/lithium-ion/neural-network.jpg" />
</Frame>

I have used reshape to change the 1D data to 2D data with 24 columns (due to placement of the thermal camera) , in some cases it might be 32 to get the best accuracy.

Then I have included couple of 2D conversion layers with pool layers, followed by a Flatten layer. Then 2 DNN (30 neurons , 10 neurons) in sequential is used.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/layers.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=d7daf9e66e2235aa9940748476b52dfa" width="936" height="624" data-path=".assets/images/lithium-ion/layers.jpg" />
</Frame>

## Deployment

In the Deployment section , select Arduino code and download the firmware package.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/deployment-1.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=1551c77f61df2678b93fb753c5b7d746" width="936" height="612" data-path=".assets/images/lithium-ion/deployment-1.jpg" />
</Frame>

Then add the Zip file as a Library in Arduino IDE.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/deployment-2.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=3be5648bc35fe3f50dbb550a5ed0f05e" width="936" height="352" data-path=".assets/images/lithium-ion/deployment-2.jpg" />
</Frame>

Once it is added, download the final application code from this GitHub link (repo has since been deleted), and flash it to the Wio Terminal.

## Output

In a model training, 100% accuracy is achieved, and in model testing 87.5% accuracy is achieved.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/accuracy.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=15d5f100532bc33dc53e78b0877c930d" width="936" height="472" data-path=".assets/images/lithium-ion/accuracy.jpg" />
</Frame>

In normal case, when all the battery in the pack is operating in normal temperature.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/normal.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=0c358a944e63cc4f2822b69e9f4b769a" width="586" height="512" data-path=".assets/images/lithium-ion/normal.jpg" />
</Frame>

In a faulty battery condition, the model will predict the cell location index and display it with a predicted value. In this particular setup, a faulty cell is placed in location 5 and discharged for 1 hour. The cell gets overheated, and the model predicts the overheated cell location, number 5 in this battery pack.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/faulty-1.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=e7d1ec2f725af01b9930fdbee9322fce" width="622" height="872" data-path=".assets/images/lithium-ion/faulty-1.jpg" />
</Frame>

If you cannot create a faulty cell for testing, you can simulate it using this method. Place a heated soldering iron on top of (near, but do not touch!) a battery cell, or move the soldering iron from across the battery pack from cell 1 to cell 6 in the pack. The model will predict the overheated cell locations as 1 to 6, as the soldering iron moves from 1 to 6. By adding the heat from the soldering iron, you can simulate the faulty battery condition and test it.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/faulty-2.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=1f7e17febfbd0eab03eaebdd9f7139dd" width="694" height="680" data-path=".assets/images/lithium-ion/faulty-2.jpg" />
</Frame>

## Schematics

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_c2MlV3xqBGAqJST/.assets/images/lithium-ion/schematics.jpg?fit=max&auto=format&n=_c2MlV3xqBGAqJST&q=85&s=cc3d8a16010af437ba3dbbe2c286f246" width="936" height="696" data-path=".assets/images/lithium-ion/schematics.jpg" />
</Frame>

## Summary

This project demonstrated a cheap and effective way to use computer vision and thermal imaging using the Wio Terminal, to identify lithium ion battery cells that are overheating, in more granular fashion than would be normally possible. This is a prototype of course, but could be used in robotics, automated warehouse and forklift devices, electric vehicles, or other places where batteries are arranged into packs.


Built with [Mintlify](https://mintlify.com).