# Source: https://docs.edgeimpulse.com/hardware/boards/blues-wireless-swan.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Blues Wireless Swan

<Info>
  **Community board**

  This is a community board by Blues Wireless, and is not maintained by Edge Impulse. For support head to the [Blues Wireless homepage](https://blues.io/).
</Info>

The Blues Wireless Swan is a development board featuring a 120MHz ARM Cortex-M4 from STMicroelectronics with 2MB of flash and 640KB of RAM. Blues Wireless has created an [in-depth tutorial](https://dev.blues.io/guides-and-tutorials/building-edge-ml-applications/blues-swan/) on how to get started using the Swan with Edge Impulse, including how to collect new data from a triple axis accelerometer and how to train and deploy your Edge Impulse models to the Swan. For more details and ordering information, visit the Blues Wireless Swan [product page](https://blues.io/products/swan/).

<Frame caption="Blues Wireless Swan: 120MHz ARM Cortex-M4 from STMicroelectronics with 2MB of flash and 640KB of RAM">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d4e9265-swan_iso.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=2307f25ab37238f6e56e246534e9ed28" width="1000" height="1000" data-path=".assets/images/d4e9265-swan_iso.jpg" />
</Frame>

### Connecting to Edge Impulse

To set up your Blues Wireless Swan, follow this complete guide: [Using Swan with Edge Impulse](https://dev.blues.io/guides-and-tutorials/building-edge-ml-applications/blues-swan/).

### Next steps: building a machine learning model

The Blues Wireless Swan [tutorial](https://dev.blues.io/swan/using-swan-with-edge-impulse) will guide you through how to create a simple classification model with an accelerometer designed to analyze movement over a brief period of time (2 seconds) and infer how the motion correlates to one of the following four states:

1. Idle (no motion)
2. Circle
3. Slash
4. An up-and-down motion in the shape of the letter "W"

For more insight into using a triple axis accelerometer to build an embedded machine learning model visit the [Edge Impulse continuous motion recognition tutorial](/tutorials/end-to-end/motion-recognition).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your Blues Wireless Swan. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package the complete impulse - including the signal processing code, neural network weights, and classification code - up into a single library that you can run on your development board. See the end of the Blues Wireless' \[Using Swan with Edge Impulse] ([https://dev.blues.io/swan/using-swan-with-edge-impulse](https://dev.blues.io/swan/using-swan-with-edge-impulse)) tutorial for more information on deploying your model onto the device.


Built with [Mintlify](https://mintlify.com).