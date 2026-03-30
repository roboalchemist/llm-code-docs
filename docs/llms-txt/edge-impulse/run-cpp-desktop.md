# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-desktop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on desktop

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build a desktop application to classify sensor data.

Even though this is a C++ library you can link to it from C applications. See 'Using the library from C' below.

<Info>
  **Knowledge required**

  This tutorial assumes that you know how to build C++ applications, and works on macOS, Linux and Windows. If you're unfamiliar with these tools you can build binaries directly for your development board from the **Deployment** page in the studio.
</Info>

**Note:** This tutorial provides the instructions necessary to build the C++ SDK library locally on your desktop. If you would like a full explanation of the Makefile and how to use the library, please see the [deploy your model as a C++ library tutorial](/hardware/deployments/run-cpp).

**Looking for examples that integrate with sensors?** See the Edge Impulse [C++ SDK](/tools/libraries/sdks/inference/linux/cpp) for Linux.

### Prerequisites

Make sure you followed the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial, and have a trained impulse. Also install the following software:

**macOS, Linux**

* [GNU Make](https://www.gnu.org/software/make/) - to build the application. `make` should be in your PATH.
* A modern C++ compiler. The default LLVM version on macOS works, but on Linux upgrade to LLVM 9 ([installation instructions](https://apt.llvm.org)).

**Windows**

* [MinGW-W64](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download) which includes both GNU Make and a compiler. Make sure `mingw32-make` is in your PATH.

### Cloning the base repository

We created an example repository which contains a Makefile and a small CLI example application, which takes the raw features as an argument, and prints out the final classification. Clone or download this repository at [example-standalone-inferencing](https://github.com/edgeimpulse/example-standalone-inferencing).

### Deploying your impulse

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **C++ library**, and click **Build** to create the library.

Download the `.zip` file and place the contents in the 'example-standalone-inferencing' folder (which you downloaded above). Your final folder structure should look like this:

```
example-standalone-inferencing
|_ build.bat
|_ build.sh
|_ CMakeLists.txt
|_ edge-impulse-sdk/
|_ LICENSE
|_ Makefile
|_ model-parameters/
|_ README.md
|_ README.txt
|_ source/
|_ tflite-model/
```

### Add data sample to main.cpp

To get inference to work, we need to add raw data from one of our samples to main.cpp. Head back to the studio and click on **Live classification**. Then load a validation sample, and click on a row under 'Detailed result'. Make a note of the classification results, as we want our local application to produce the same numbers from inference.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the local application classifies the same, we need the raw features for this timestamp. To do so click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

Open *source/main.cpp* in an editor of your choice. Find the following line:

```
// Raw features copied from test sample
static const float features[] = {
    // Copy raw features here (e.g. from the 'Model testing' page)
};
```

Paste in your raw sample data where you see `// Copy raw features here`:

```
// Raw features copied from test sample
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

**Note:** the raw features will likely be longer than what I listed here (the `...` won't compile--I just wanted to demonstrate where the features would go).

In a real application, you would want to make the `features[]` buffer non-const. You would fill it with samples from your sensor(s) and call `run_classifier()` or `run_classifier_continuous()`. See [deploy your model as a C++ library tutorial](/hardware/deployments/run-cpp) for more information.

Save and exit.

### Running the impulse

Open a terminal or command prompt, and build the project:

**macOS, Linux**

```
$ sh build.sh
```

**Windows**

```
$ build.bat
```

This will first build the inferencing engine, and then build the complete application. After building succeeded you should have a binary in the *build/* directory.

Then invoke the local application by calling the binary name:

**macOS, Linux**

```
./build/app
```

**Windows**

```
build\app
```

This will run the signal processing pipeline using the values you provided in the `features[]` buffer and then give you the classification output:

```
run_classifier_returned: 0
Timing: DSP 0 ms, inference 0 ms, anomaly 0 ms
Predictions (time: 0 ms.):
  idle:   0.015319
  snake:  0.000444
  updown: 0.006182
  wave:   0.978056
Anomaly score (time: 0 ms.): 0.133557
```

Which matches the values we just saw in the studio. You now have your impulse running locally!

<Info>
  **Hardware Acceleration**

  If you have a device with a GPU, you can enable hardware acceleration, see the [example-standalone-inferencing-linux](https://github.com/edgeimpulse/example-standalone-inferencing-linux) repository for an example of how to do this. This will speed up the inferencing process significantly.
</Info>

### Using the library from C

Even though the impulse is deployed as a C++ application, you can link to it from C applications. This is done by compiling the impulse as a shared library with the `EIDSP_SIGNAL_C_FN_POINTER=1` and `EI_C_LINKAGE=1` macros, then link to it from a C application. The `run_classifier` can then be invoked from your application. An end-to-end application that demonstrates this and can be used with this tutorial is under [example-standalone-inferencing-c](https://github.com/edgeimpulse/example-standalone-inferencing-c).


Built with [Mintlify](https://mintlify.com).