# Source: https://docs.edgeimpulse.com/projects/expert-network/iv-drip-fluid-level-monitoring-arduino-portenta-h7.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IV Drip Fluid-Level Monitoring - Arduino Portenta H7

Created By: Manivannan Sivan

Public Project Link: [https://studio.edgeimpulse.com/public/107293/latest](https://studio.edgeimpulse.com/public/107293/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/4W37gOTlnjk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Problem Statement

An empty IV bag can pose several issues, both medical and operational:

* Extra pressure on the bag may exceed atmospheric within the bag, allowing air to continue to infuse into the patient once the bag is empty (if gravity fed). For the same reason, a bag that has been disconnected from the IV set should never be re-connected, as any extra air that may enter the flask could lead to embolism.
* Periodic monitoring by staff can be challenging depending upon staffing level and size of facility.

## Solution

The prototype for this project will classify the IV fluid level into three categories:

1. Adequate
2. Less than 50%
3. Low level

This simple categorization can allow for the output or results of this model to be integrated via communication protocols like BLE or LoRa, to stream the results to a central system in a hospital. The nursing staff can monitor the IV fluid levels of all patients in one place. Hence, it can save a lot of effort and time going to monitor or check the fluid level of each individually.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/intro.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=1bd7d41b9e9d32931ace630422cdca56" width="822" height="568" data-path=".assets/images/iv-drip/intro.jpg" />
</Frame>

In this prototype hardware setup, the Portenta H7 with Vision Shield is placed 15cm from the IV drips fluid. Then, connect the Portenta to the host system, and type the below command.

`edge-impulse-daemon`

Now, the Portenta is connected to your Edge Impulse account.

<Info>
  For initial setup of the Portenta, follow the steps outlined [here](/hardware/boards/arduino-portenta-h7).
</Info>

## Dataset

I have collected 117 images of an IV fluid bag in various states, consisting of “adequate”, “less than 50%”, and “low level”.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/data-collection.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=92143b35c04494711e354140e57e7584" width="836" height="690" data-path=".assets/images/iv-drip/data-collection.jpg" />
</Frame>

In the above image , you can visualize that the adequate has more than 50% fluid and low level is almost empty.

## Create Impulse:

In the “Create Impulse” section, configure the settings as shown here.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/impulse.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=69b4204df784eb6f5e29238fc169ec8a" width="1172" height="428" data-path=".assets/images/iv-drip/impulse.jpg" />
</Frame>

## Neural Network

In “Neural Network”, I have used a single 2D convolution layer with flatten – DNN (10 neurons). The reason to go with one set of 2D Conv instead of more layers in 2D Conv, is memory consumption.

Due to memory constraints on the device, I have one included one 2D Conv layer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/neural-network.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=083f8faa87fb3851e0df0fefc61449a6" width="808" height="674" data-path=".assets/images/iv-drip/neural-network.jpg" />
</Frame>

The model achieved an accuracy of 95% with loss of 0.2

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/accuracy.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=346f77692775d4702610d4fcf777e67f" width="902" height="714" data-path=".assets/images/iv-drip/accuracy.jpg" />
</Frame>

The reason for deviation in the “less than 50 percent” category is due to different light exposure, which created a drop in accuracy. Additional images, images taken at various times of day, and other lighting conditions could help build a stronger model if needed. However, the focus for the project is detecting “low level” fluid bags, so that is where effort should be spent improving accuracy and dataset.

## Deployment

In the “Deployment” section , select “Firmware – Portenta H7” and download it.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/deployment.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=7e21c238b79602de984240b605ae429b" width="800" height="568" data-path=".assets/images/iv-drip/deployment.jpg" />
</Frame>

Once the firmware is flashed to the board, then open a Command Prompt window and type the below command to start inferencing:

```
edge-impulse-run-impulse
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/iv-drip/inferencing.jpg?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=01a10d48689fac57d9694740498d689f" width="902" height="510" data-path=".assets/images/iv-drip/inferencing.jpg" />
</Frame>

## Summary

This project demonstrated a cost effective solution to detect the fluid level in an IV bag, using an Arduino Portenta H7 and Vision Shield plus Edge Impulse. The concept could even be expanded, and applied to machinery, industry, or other places; using computer vision to translate or interpret the analog, legacy, or physical world. The computer vision portion of the project is demonstrated, and it could easily be expanded or scaled to more units. The last piece would be to investigate aggregating data from the devices and rendering on a dashboard, to help reduce the burden on medical staff and improve efficiency in a hospital or medical facility.


Built with [Mintlify](https://mintlify.com).