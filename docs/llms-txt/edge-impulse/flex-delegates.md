# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux/flex-delegates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flex delegates

On Linux platforms without a GPU or neural accelerator your model is run using LiteRT (previously Tensorflow Lite). Not every model can be represented using native LiteRT (previously Tensorflow Lite) operators. For these models, 'Flex' ops are injected into the model. To run these models you'll need to have the flex delegate library installed on your Linux system. This is a shared library that you need to install once.

If your model contains flex ops you'll see this in a few places:

* During deployment in the Studio (e.g. "WARN: This model contains ops that require flex delegates (FlexErf). You will need to install the flex delegates shared library to run this model.").
* When running a model using the Linux CLI (e.g. "error while loading shared libraries: libtensorflowlite\_flex\_2.16.1.so. You will need to install the flex delegates shared library to run this model.").

### Installing the flex delegate library

To install the flex delegate library:

1. Download the shared library for your target architecture and operating system:
   * [macOS x86](https://cdn.edgeimpulse.com/build-system/flex-delegates/mac-x86_64/libtensorflowlite_flex_2.16.1.dylib) (also runs on M1/M2 using Rosetta)
   * [Linux armv7](https://cdn.edgeimpulse.com/build-system/flex-delegates/linux-armv7/libtensorflowlite_flex_2.16.1.so) (most 32-bits Arm-based Linux systems, e.g. Raspberry Pi 4 running 32-bits Raspbian)
   * [Linux aarch64](https://cdn.edgeimpulse.com/build-system/flex-delegates/linux-aarch64/libtensorflowlite_flex_2.16.1.so) (most 64-bits Arm-based Linux systems, e.g. Jetson Nano)
   * [Linux x86\_64](https://cdn.edgeimpulse.com/build-system/flex-delegates/linux-x86/libtensorflowlite_flex_2.16.1.so) (Intel/AMD based Linux systems)
2. Place the `libtensorflowlite_flex_2.16.1.so` (or `.dylib` on macOS) file in `/usr/lib` or `/usr/local/lib`.

### Linking the flex delegate library using the C++ SDK

If your model has flex ops, and you're building using the Linux C++ SDK, then pass the `LINK_TFLITE_FLEX_LIBRARY=1` flag when building the application.

When using the Node.js, Go or Python SDK then the .eim file already has the flex delegates library linked in.


Built with [Mintlify](https://mintlify.com).