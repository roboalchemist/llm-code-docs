# Source: https://docs.edgeimpulse.com/hardware/deployments/run-drpai-rzv2h.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run DRP-AI TVM i8 library on Renesas RZ/V2H

Your trained ML model in the Edge Impulse Studio can be downloaded as a DRP-AI TVM i8 library. This library is provided to you as a C++ header-only that does not require any dependencies and can be integrated into your project and compiled into your application.

The library contains the model parameters, model weights that run on the `DRP-AI3` accelerator and the Edge Impulse SDK that contains the necessary function calls to the inferencing engine.

In order to benefit from the hardware acceleration provided by the RZ/V2H board we need to download the **DRP-AI TVM i8 library** from the deployment page. This will allow you to run your model efficiently on the RZ/V2H.

In the studio, we define the *Impulse* as a combination of any preprocessing code necessary to extract features from your raw data along with inference using your trained machine learning model. Similarly, with the `drp-ai-tvm-i8` library, we provide the library with raw data from your sensor, and it will return the output of your model. It performs feature extraction and inference, just as you configured in the Edge Impulse Studio!

Currently, in the following tutorial, we are focusing on vision applications and will try to build an object detection app. We recommend working through the steps in this guide to see how to run the application on a Linux operating system. However, you can build the application using any operating system, but eventually you need to cross-compile the application with the Renesas SDK to make it work on the RZ/V2H.

<Info>
  **Knowledge required**

  This guide assumes you have some familiarity with C and the GNU Make build system. We will demonstrate how to run an impulse (e.g. inference) on Linux, macOS, or Windows using a C program and Make. We want to give you a starting point for porting the C++ library to your own build system.
</Info>

The [Inference SDK](/tools/libraries/sdks/inference/cpp) reference details the available macros, structs, variables, and functions for the C++ SDK library.

A working demonstration of this project can be found [here](https://github.com/edgeimpulse/example-standalone-inferencing-linux).

### Prerequisites

You will need to have the Renesas RZ/V2H SDK that is built when creating the Yocto image. This SDK contains the necessary toolchain that can be used to compile the app and make it work on the RZ/V2H. For more information see [Renesas RZ/V2H](/hardware/boards/renesas-rz-v2h).

Then you will need to install the SDK, the full instruction can be found in section 6 of the same manual used for building the Yocto image. So the SDK will provide you with the necessary tooling.

### Download the DRP-AI TVM i8 Library from Edge Impulse

You need to download a DRP-AI TVM i8 library from your own project. If you use the public project, you will need to click **Clone this project** in the upper-right corner to clone the project to your own account.

Head to the **Deployment** page for your project. Select **DRP-AI TVM i8 library**. Scroll down, and click **Build**. Note that you must have a fully trained model in order to download any of the deployment options.

<Frame caption="DRP-AI TVM i8 library option">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/drp-ai-lib.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=88c0b096be2208f0dc85b48905e80115" width="308" height="196" data-path=".assets/images/drp-ai-lib.png" />
</Frame>

Your impulse will download as a C++ library in a .zip file.

### Create a Project

The easiest way to test the `drp-ai-tvm-i8` library is to use raw features from one of your test set samples. When you run your program, it should print out the class probabilities that match those of the test sample in the Studio.

Create a directory to hold your project (e.g., `my-project`). Unzip the `drp-ai-tvm-i8` library file into the project directory. Your directory structure should look like the following:

```shell  theme={"system"}
my-project/
|-- edge-impulse-sdk/
|-- model-parameters/
|-- tflite-model/drpai_model.h
|-- CMakeLists.txt
|-- Makefile
|-- main.cpp
```

**Note:** You can write in C or C++ for your main application. Because portions of the Impulse library are written in C++, you must use the Renesas SDK C++ compiler for your main application (see this [FAQ](https://isocpp.org/wiki/faq/mixing-c-and-cpp) for more information). A more advanced option would be to use bindings for your language of choice (e.g. [calling C++ functions from Python](https://realpython.com/python-bindings-overview/)). We will stick to C for this demonstration. We highly recommend keeping your main file as a *.cpp* or *.cc* file so that it will compile as C++ code.

At this stage, you can have a look inside the `tflite-model/` directory. You will see the `drp-ai` model that is going to be used by the Edge Impulse SDK to run this model on the hardware accelerator. If you do not find the file called `drpai_model.h` then you have probably downloaded the C++ library or your build was not successful and it fell back to the normal library.

In order to build an app you need to use the same code that is described starting from the following [section](/hardware/deployments/run-cpp#create-an-application) until the end of the tutorial.


Built with [Mintlify](https://mintlify.com).