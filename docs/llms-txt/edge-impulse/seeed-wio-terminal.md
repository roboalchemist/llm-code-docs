# Source: https://docs.edgeimpulse.com/hardware/boards/seeed-wio-terminal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed Wio Terminal

<Info>
  **Community board**

  This is a community board by Seeed Studios, and it's not maintained by Edge Impulse. For support head to the [Seeed Forum](https://forum.seeedstudio.com).
</Info>

The Seeed Wio Terminal is a development board from Seeed Studios with a Cortex-M4 microcontroller, motion sensors, an LCD-display, and Grove connectors to easily connect external sensors. Seeed Studio has added support for this development board to Edge Impulse, so you can sample raw data and build machine learning models from the studio.

<Frame caption="Seeed Wio Terminal">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/33b2400-102991299-1.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=c7505bbf20b9349973e113a46f6a2034" width="700" height="525" data-path=".assets/images/33b2400-102991299-1.png" />
</Frame>

### Connecting to Edge Impulse

To set up your Seeed Wio Terminal, follow this guide: [Wio Terminal Edge Impulse Getting Started - Seeed Wiki](https://wiki.seeedstudio.com/Wio-Terminal-TinyML-EI-1/).

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with this full end-to-end course from Seeed's EDU team: [TinyML with Wio Terminal Course](https://wiki.seeedstudio.com/Wio-Terminal-TinyML/).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your Wio Terminal. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the signal processing code, neural network weights, and classification code - up in a single library that you can run on your development board.

The easiest way to deploy your impulse to the Seeed Wio Terminal is via an Arduino library. See [Run on Arduino](/hardware/deployments/run-arduino-2-0) for more information.

### Troubleshooting

#### ESP-NN conflict

<Warning>
  **ESP-NN Conflict Workaround**

  With the recent addition of ESP-NN acceleration, the Wio Terminal will attempt to build the ESP-NN files in the Arduino library, which results in several errors during linking. While we work on a permanent solution, remove the ESP-NN folder to compile Wio Terminal applications with the Edge Impulse SDK.
</Warning>

If you see an error like the following Arduino, it means the Wio Terminal build process is attempting to link to the ESP-NN library (which is not supported):

```
...
/Users/shawnhymel/Library/Arduino15/packages/Seeeduino/tools/arm-none-eabi-gcc/7-2017q4/bin/../lib/gcc/arm-none-eabi/7.2.1/../../../../arm-none-eabi/bin/ld: error: /private/var/folders/0j/x5ptl26j45v1tk3s8bb3cqyw0000gn/T/arduino/sketches/ECF7D69B795FD172E07BD549315696FA/libraries/Snake_v2_inferencing/edge-impulse-sdk/porting/espressif/ESP-NN/src/pooling/objs.a(esp_nn_max_pool_s8_esp32s3.S.o): Conflicting CPU architectures 13/0
/Users/shawnhymel/Library/Arduino15/packages/Seeeduino/tools/arm-none-eabi-gcc/7-2017q4/bin/../lib/gcc/arm-none-eabi/7.2.1/../../../../arm-none-eabi/bin/ld: failed to merge target specific data of file /private/var/folders/0j/x5ptl26j45v1tk3s8bb3cqyw0000gn/T/arduino/sketches/ECF7D69B795FD172E07BD549315696FA/libraries/Snake_v2_inferencing/edge-impulse-sdk/porting/espressif/ESP-NN/src/pooling/objs.a(esp_nn_max_pool_s8_esp32s3.S.o)
...
```

While we work on a permanent solution, the workaround is to remove the *ESP-NN/* folder found in *Arduino/libraries/\<ei-project-name>/src/edge-impulse-sdk/porting/espressif/*


Built with [Mintlify](https://mintlify.com).