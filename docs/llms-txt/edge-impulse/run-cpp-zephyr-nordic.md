# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-zephyr-nordic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on Zephyr-based Nordic Semiconductor development boards

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build a Zephyr RTOS application for the nRF52840 DK / nRF5340 DK / nRF9160DK / Thingy:91 development board to classify sensor data.

<Warning>
  **A working Zephyr RTOS build environment is required**

  This tutorial assumes that you're already familiar with building applications for the [nRF52840DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html) or other **Zephyr RTOS** supported board, and that you have your environment set up to compile applications for this platform. For this tutorial, you can use the [nRF Connect SDK v1.6.0](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/1.6.0/zephyr/index.html) or higher.
</Warning>

### Prerequisites

Make sure you followed the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial, and have a trained impulse. Also, make sure you have a working Zephyr build environment, including the following tools:

* Either the [nRF Connect SDK](https://www.nordicsemi.com/Software-and-tools/Software/nRF-Connect-SDK) which includes Zephyr and all its dependencies (v1.6.0 or higher), or a [manual installation of the Zephyr build environment](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/installation/install_ncs.html#set_up_the_command-line_build_environment).
* The [GNU ARM Embedded Toolchain (version 9-2019-q4-major)](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).
* Optional: The [nRF command line tools](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools/download) and [Segger J-Link tools](https://www.segger.com/downloads/jlink). These command line tools are required if you use the [`west` command line interface](https://docs.zephyrproject.org/latest/guides/west/index.html) to upload firmware to your target board.

### Cloning the base repository

We created an example repository which contains a small application that compliments the [Continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial. This application can take raw, hard-coded inputs as an argument, and print out the final classification to the serial port so it can be read from your development computer. You can either [download the application](https://github.com/edgeimpulse/example-standalone-inferencing-zephyr/archive/master.zip) or import the repository using Git:

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-standalone-inferencing-zephyr.git
```

<Info>
  **Fully featured open source repos are also available**

  If you are looking for sample projects showcasing all sensors and features supported by Edge Impulse out of the box, we have public firmware repos available for the Nordic Semiconductor nRF52840, nRF5340 and nRF9160 development kits as well as for the Thingy:91 and Thingy:53. See

  * [edgeimpulse/firmware-nordic-nrf52840dk-nrf5340dk](https://github.com/edgeimpulse/firmware-nordic-nrf52840dk-nrf5340dk)
  * [edgeimpulse/firmware-nordic-nrf9160dk](https://github.com/edgeimpulse/firmware-nordic-nrf9160dk)
  * [edgeimpulse/firmware-nordic-thingy91](https://github.com/edgeimpulse/firmware-nordic-thingy91)
  * [edgeimpulse/firmware-nordic-thingy53](https://github.com/edgeimpulse/firmware-nordic-thingy53)
</Info>

### Deploying your impulse

Head over to your Edge Impulse project, and go to the **Deployment** page. From here you can obtain a packaged library containing the Edge Impulse C++ SDK, your impulse, and all required external dependencies. Select **C++ library** and click **Build** to create the library.

Download the `.zip` file and extract the contents. Now copy the following directories to the 'example-standalone-inferencing-zephyr' folder (which you downloaded above).

* `edge-impulse-sdk`
* `model-parameters`
* `tflite-model`

Your final folder structure should look like this:

```bash  theme={"system"}
 example-standalone-inferencing-zephyr
 ├── CMakeLists.txt
 ├── edge-impulse-sdk
 ├── model-parameters
 ├── prj.conf
 ├── README.md
 ├── sample.yaml
 ├── src
 ├── tflite-model
 └── utils
```

### Running the impulse

With the project ready it's time to verify that the application works. Head back to the studio and click on **Live classification** in the project you created for the [continuous motion recognition](/tutorials/end-to-end/motion-recognition) tutorial, then load a testing sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the Zephyr application performs the same classification when running locally on your board, we need to use the same raw inputs as those provided to the **Live classification** for any given timestamp. To do so, click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

Next, open `src/main.cpp` in the example directory and paste the raw features inside the `static const float features[]` definition. For example:

```cpp  theme={"system"}
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

And use west or your usual method to build the application:

```
# nRF52840 DK
$ west build -b nrf52840dk_nrf52840

# nRF5340 DK
$ west build -b nrf5340dk_nrf5340_cpuapp

# nRF9160DK
$ west build -b nrf9160dk_nrf9160ns

# Thingy:91
$ west build -b thingy91_nrf9160
```

<Warning>
  **Invalid choice: 'build'**

  If you try to build the application but it throws an 'invalid choice' error like:

  ```
  $ west build -b nrf52840dk_nrf52840
  usage: west [-h] [-z ZEPHYR_BASE] [-v] [-V] <command> ...
  west: error: argument <command>: invalid choice: 'build' (choose from 'init', 'update', 'list', 'manifest', 'diff', 'status', 'forall', 'help', 'config', 'topdir', 'selfupdate')
  ```

  You'll need to set up your environment variables correctly ([more info](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/installation/install_ncs.html#set_up_the_command-line_build_environment)). You can do so by opening a command prompt or terminal window and running the commands below from the zephyr parent directory: **On Windows**

  ```
  $ zephyr\zephyr-env.cmd
  ```

  **On macOS / Linux**

  ```
  $ source zephyr/zephyr-env.sh
  ```
</Warning>

If you have set up the Segger J-LINK tools and the board that comes with J-LINK debug probe, you can also flash this application with:

```
$ west flash
```

otherwise if your board shows up as a mass storage device, you can find the `build/zephyr/zephyr.bin` file and drag it to the `JLINK` USB mass-storage device in the same way you do with a USB flash drive.

For the nRF9160DK, you also have to make sure the [board controller has been flashed](/hardware/boards/nordic-semi-nrf9160-dk#3-update-the-firmware) at least once.

<Warning>
  Boards such as Thingy:91 and Thingy:53 do not come with in built J-LINK debug probe, and cannot be used with `west flash` directly. They do include connector that enable users to connect with external J-LINK debug probe and take advantage of `west flash` command.
</Warning>

### Seeing the output

To see the output of the impulse, connect to the development board over a serial port on baud rate 115,200 and reset the board. You can do this with your favourite serial monitor or with the Edge Impulse CLI:

```
$ edge-impulse-run-impulse --raw
```

This will show you the output of the signal processing pipeline and the results of the classification:

```
Edge Impulse standalone inferencing (Zephyr)
Running neural network...
Predictions (time: 1 ms.):
idle:   0.015319
snake:  0.000444
updown: 0.006182
wave:   0.978056
Anomaly score (time: 0 ms.): 0.133557
Predictions (DSP: 18 ms., Classification: 1 ms., Anomaly: 0 ms.):
[0.01532, 0.00044, 0.00618, 0.97806, 0.134]
```

The output should match the values you just saw in the studio. If it does, you now have your impulse running on your Zephyr development board!

<Info>
  **Connecting live sensors?**

  Now that you have verified that the impulse works with hard-coded inputs, you should be ready to plug live sensors from your board. A demonstration on how to plug sensor values into the classifier can be found here: [Data forwarder - classifying data (Zephyr)](/tools/clis/edge-impulse-cli/data-forwarder).
</Info>


Built with [Mintlify](https://mintlify.com).