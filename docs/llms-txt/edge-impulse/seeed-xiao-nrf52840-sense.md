# Source: https://docs.edgeimpulse.com/hardware/boards/seeed-xiao-nrf52840-sense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed XIAO nRF52840 Sense

<Info>
  **Community board**

  This is a community board by Seeed Studios, and it's not maintained by Edge Impulse. For support head to the [Seeed Forum](https://forum.seeedstudio.com).
</Info>

The Seeed Studio XIAO nRF52840 Sense incorporates the Nordic nRF52840 chip with FPU, operating up to 64 MHz, mounted multiple development ports, carrying Bluetooth 5.0 wireless capability and can operate with low power consumption. Featuring onboard IMU and PDM, it can be your best tool for embedded Machine Learning projects. Seeed Studio has added support for this development board to Edge Impulse, so you can sample raw data and build machine learning models from the studio.

<Frame caption="Seeed XIAO nRF52840 Sense">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/102010469_Front-14.jpeg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=2568d88559607fff74f072a2860f8cb1" width="1333" height="1000" data-path=".assets/images/102010469_Front-14.jpeg" />
</Frame>

### Connecting to Edge Impulse

To set up your Seeed Studio XIAO nRF52840 Sense, follow this guide: [Seeed Studio XIAO nRF52840 Sense Edge Impulse Getting Started - Seeed Wiki](https://wiki.seeedstudio.com/XIAOEI/).

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model: [Building a machine learning model - Seeed Wiki](https://wiki.seeedstudio.com/XIAOEI/#building-a-machine-learning-model).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your XIAO nRF52840 Sense. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the signal processing code, neural network weights, and classification code - up in a single library that you can run on your development board.

The easiest way to deploy your impulse to the Seeed XIAO nRF52840 Sense is via an Arduino library. See [Run on Arduino](/hardware/deployments/run-arduino-2-0) for more information.


Built with [Mintlify](https://mintlify.com).