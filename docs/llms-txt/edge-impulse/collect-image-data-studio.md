# Source: https://docs.edgeimpulse.com/tutorials/topics/data/collect-image-data-studio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect image data using Studio

This page is part of [Image classification](/tutorials/topics/data/collect-image-data-openmv-h7-plus) and describes how you can use development boards with an integrated camera to import image data into Edge Impulse.

First, make sure your device is connected on the **Devices** page in the Edge Impulse Studio. Then, head to **Data acquisition**, and under 'Record new data', set a label and select 'Camera' as a sensor (most devices have multiple resolutions). This shows you a nice preview of the camera. Then click **Start sampling**.

<Frame caption="Record new data from a camera">
  <img src="https://mintcdn.com/edgeimpulse/M1w1EVa0Cr_xPADa/.assets/images/ba2ebd9-screenshot_2021-03-10_at_101457.png?fit=max&auto=format&n=M1w1EVa0Cr_xPADa&q=85&s=7f766c2a4d5ab8470fb3597bcbec147b" width="1098" height="952" data-path=".assets/images/ba2ebd9-screenshot_2021-03-10_at_101457.png" />
</Frame>

A few moments later - depending on the speed of the development board and the resolution - you'll now have an image collected!

<Frame caption="You now have collected data from your development board">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5822469-screenshot_2021-03-10_at_101517.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=96c6b9056792a542896f831a8ee847c5" width="1420" height="1000" data-path=".assets/images/5822469-screenshot_2021-03-10_at_101517.png" />
</Frame>

Do this until you have captured 30 images per class from a variety of angles. Also make sure to vary the things you capture for the unknown class.


Built with [Mintlify](https://mintlify.com).