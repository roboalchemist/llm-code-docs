# Source: https://docs.edgeimpulse.com/hardware/deployments/run-iar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run IAR library

[IAR Embedded Workbench](https://www.iar.com/products/architectures/arm/iar-embedded-workbench-for-arm/) is one of the leading development solutions for Arm processors. Their product offers device support for most of the ARM silicon and development boards and includes a rich set of build and debugging tools. In Edge Impulse studio you can deploy your model to a library format that can be imported into a IAR Embedded Workbench project with ease.

## IAR Project Connection

IAR developed a tool for external applications to contribute into an IAR Embedded Workbench project. This mechanism is called **IAR Project Connection** and allows to define a project config in a XML style config file (`.ipcf`). IAR Embedded Workbench updates the project dynamically if this file is changed.

## Deploy to an IAR Embedded Workbench Library

In the deployment section of Edge Impulse Studio select the IAR deployment option. Depending on your model optimization preferences you can enable the EON compiler and choose between Quantized and Unoptimized data format. Clicking **Build** will initiate the library build process and, when finished, downloads a zip file containing the library to you computer.

<Info>
  **IAR Embedded Version**

  The library export function for IAR is developed and tested using IAR Embedded Workbench **version 9.40**. Please contact us if you see issues with older versions of the IAR product.
</Info>

## Import the library into IAR Embedded Workbench

To import the ML model and inference SDK follow these steps:

1. Place and unzip the downloaded library in the root folder of your project.
2. Open your project in IAR Embedded Workbench.
3. Open the IAR Project Connection by selecting `Project->Add Project Connection->IAR Project Connection`.
4. Select the import file from the library folder.

### Project configuration for Edge Impulse Inference library

Our pre-processing and neural network code relies on CMSIS DSP and NN algorithms for ARM based processors. CMSIS is therefor included in the `edge-impuse-sdk` folder. Multiple instances of the CMSIS library can exist in a single project, but be sure the `edge-impulse-sdk` references and links to the included CMSIS library. Safest way would be either to disable CMSIS in your project, or to build the model and inference code as a library and link to that library in your main project.

<Frame caption="IAR Disable CMSIS">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/IAR-disable-cmsis.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=a7766c016b8237c409e90975e0b7f562" width="570" height="530" data-path=".assets/images/IAR-disable-cmsis.png" />
</Frame>

Compiling the `edge-impulse-sdk` requires the C++ compiler. Check your project settings matches the following image:

<Frame caption="IAR Compiler config">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/IAR-compiler-config.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=3e79d8ddd010d81328eb071c45f5aa7f" width="571" height="531" data-path=".assets/images/IAR-compiler-config.png" />
</Frame>

## ST example project

To get started with Edge Impulse in IAR quickly, we've created an [example project](https://github.com/edgeimpulse/iar-export-stm32). This project is based on a STM32F4 Nucleo board and allows running inference over a static buffer.

Follow the instructions from the [Readme](https://github.com/edgeimpulse/iar-export-stm32/blob/master/README.md) to get started.

### Standalone example

This standalone example project contains minimal code required to run the imported impulse on a STMicroelectronics MCU. This code is located in `ei_standalone.cpp`. In this minimal code example, inference is run from a static buffer of input feature data. To verify that our embedded model achieves the exact same results as the model trained in Studio, we want to copy the same input features from Studio into the static buffer in `ei_standalone.cpp`.

To do this, first head back to the studio and click on the **Live classification** tab. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the local application classifies the same result, we need the raw features for this timestamp. To do so click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw input values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

In `ei_standalone.cpp` paste the raw features inside the `static const float features[]` definition, for example:

```cpp  theme={"system"}
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

The project will repeatedly run inference on this buffer of raw features once built. This will show that the inference result is identical to the **Live classification** tab in Studio. From this starting point, the example project is fully compatible with existing SimpleLink SDK plugins, drivers or custom firmware. Use new sensor data collected in real time on the device to fill a buffer. From there, follow the same code used in `ei_standalone.cpp` to run classification on live data.


Built with [Mintlify](https://mintlify.com).