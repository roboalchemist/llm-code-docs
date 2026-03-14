# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-silabs-thunderboard-sense-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on SiLabs Thunderboard Sense 2

Impulses can be deployed as a C++ library. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial you'll export an impulse, and build an application in Simplicity Studio to classify sensor data on the [SiLabs Thunderboard Sense 2](/hardware/boards/silabs-thunderboard-sense-2) development board.

<Info>
  **Knowledge required**

  This tutorial assumes that you're familiar with compiling applications with Simplicity Studio. If you're unfamiliar with this you can build binaries directly for your development board from the **Deployment** page in the studio.
</Info>

**Note:** Are you looking for an example that has all sensors included? The Edge Impulse firmware for the SiLabs Thunderboard Sense 2 has that. See [edgeimpulse/firmware-silabs-thunderboard-sense-2](https://github.com/edgeimpulse/firmware-silabs-thunderboard-sense-2).

### Prerequisites

Make sure you followed the \[Continuous motion recognition] (tutorials/continuous-motion-recognition.md) tutorial, and have a trained impulse. Also install the following software:

* [Simplicity Studio 5](https://www.silabs.com/developers/simplicity-studio).
* Python 3.6.8 or higher.
* Java 64 bit JVM 11 or higher: - available at [Amazon Corretto](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html) or [releases page](https://github.com/corretto/corretto-11/releases).

Alternatively you can build this application from the command line or through Docker, see the build instructions in [example-standalone-inferencing-silabs-tb-sense-2](https://github.com/edgeimpulse/example-standalone-inferencing-silabs-tb-sense-2).

### Cloning the base repository

We created an example repository which contains a small Simplicity Studio application, which takes the raw features as an argument, and prints out the final classification. You can either [download the application](https://github.com/edgeimpulse/example-standalone-inferencing-silabs-tb-sense-2/archive/main.zip) or import this repository using Git:

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-standalone-inferencing-silabs-tb-sense-2.git
```

### Deploying your impulse

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **C++ library** and click **Build** to create the library.

Download the `.zip` file and place the contents in the 'example-standalone-inferencing-silabs-tb-sense-2/ei-workspace/edgeimpulse' folder (which you downloaded above).

### Importing the workspace into Simplicity Studio

With the model downloaded you can import the project into Simplicity Studio.

1. Generate the Simplicity Studio project by opening a command prompt or terminal, navigating to the `'example-standalone-inferencing-silabs-tb-sense-2` folder and running:

```
$ pip3 install pyyaml
$ python3 update-slcp.py
```

1. Open Simplicity IDE and install the Gecko SDK 3.2.x.
2. Create a new project via **File > New > Silicon Labs Project Wizard...**
3. In the New Project Wizard select **Simplicity Studio > Silicon Labs MCU Project** and click **Next**
4. Under 'board' select **Thunderboard Sense 2**.
5. Select the correct SDK you installed in #1 and click **Next**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/a756a87-target-sdk-toolchain-selection.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=92b4265cc5da729a625c115263e8ba79" width="942" height="920" data-path=".assets/images/a756a87-target-sdk-toolchain-selection.png" />
</Frame>

1. Select **Empty C++ Program** and click **Next**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/717d488-example-project-selection.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=1ee40841bf5ee8ad90eff26525af87fc" width="936" height="915" data-path=".assets/images/717d488-example-project-selection.png" />
</Frame>

1. Name the project `example-standalone-inferencing-silabs-tb-sense-2` (exactly this) and make sure **Copy contents** is selected before clicking **Finish**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1a40365-project-configuration.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=016416ac84d8a409f4a8eb1aaf423bc2" width="1600" height="918" data-path=".assets/images/1a40365-project-configuration.png" />
</Frame>

1. Under 'Project Explorer' select all files, except for *Includes* and delete them:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/5c5e4c9-delete-files.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=6189fa7e6a698089eb7931f308e90b44" width="318" height="220" data-path=".assets/images/5c5e4c9-delete-files.png" />
</Frame>

1. Then, navigate to the `example-standalone-inferencing-silabs-tb-sense-2/ei-workspace` folder (in this repository), and drag all files and folders into the 'Project explorer' window in Simplicity Studio. When prompted select **Copy files and folders** for this operation.
2. Then close, and reopen the project via: **Project > Close Project**, then **Project > Open Project**.
3. Double-click on `example-standalone-inferencing-silabs-tb-sense-2.slcp` to show the Simplicity Configurator.
4. Edit 'Project Generators' and disable 'IAR EMBEDDED WORKBENCH PROJECT' (if it's listed):

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/8d3af53-no-iar.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=2974f3dde3f844bcdfb652faae78e601" width="517" height="1000" data-path=".assets/images/8d3af53-no-iar.png" />
</Frame>

1. Click **Force Generation** to regenerate all links and include paths.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/402ff38-project-details.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=82601a9c6020bd343418f404dccfb33b" width="1505" height="659" data-path=".assets/images/402ff38-project-details.png" />
</Frame>

1. The project is now imported!

### Running the impulse

With the project ready it's time to verify that the application works. Head back to the studio and click on **Live classification**. Then load a validation sample, and click on a row under 'Detailed result'.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

To verify that the local application classifies the same, we need the raw features for this timestamp. To do so click on the 'Copy to clipboard' button next to 'Raw features'. This will copy the raw values from this validation file, before any signal processing or inferencing happened.

<Frame caption="Copying the raw features.">
  <img src="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/f2e53b5-wave.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=6f8d0ba48d5dd5894b887a600011753a" width="469" height="381" data-path=".assets/images/f2e53b5-wave.png" />
</Frame>

In the example directory open `main.cpp` and paste the raw features inside the `static const float features[]` definition, for example:

```cpp  theme={"system"}
static const float features[] = {
    -19.8800, -0.6900, 8.2300, -17.6600, -1.1300, 5.9700, ...
};
```

With everything set up, you can now build the application using Simplicity Studio, the command line, or with Docker.

### Building and flashing the application

1. In Simplicity Studio v5, select **Project > Build Project** to build the firmware.
2. Then, right click on the development board in the *Debug adapters* section of Simplicity Studio and select **Upload application**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/a62496b-upload_application.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=05c5c7fcec52adca738238b394bf9928" width="371" height="359" data-path=".assets/images/a62496b-upload_application.png" />
</Frame>

1. Under *Application image path* select the `GNU ARM v10.2.1 - Default/example-standalone-inferencing-silabs-tb-sense-2.bin` file and click **OK** to flash.

(Alternatively you can drag and drop the `GNU ARM v10.2.1 - Default/example-standalone-inferencing-silabs-tb-sense-2.bin` file onto the `TB004` mass-storage device to flash the binary.

### Seeing the output

To see the output of the impulse, connect to the development board over a serial port on baud rate 115,200 and reset the board. You can do this with your favourite serial monitor or with the Edge Impulse CLI:

```
$ edge-impulse-run-impulse --raw
```

This will run the signal processing pipeline, and then classify the output:

```
Edge Impulse standalone inferencing (Silicon Labs Thunderboard Sense 2)
Running neural network...
Predictions (time: 1 ms.):
idle:   0.015319
snake:  0.000444
updown: 0.006182
wave:   0.978056
Anomaly score (time: 0 ms.): 0.133557
Predictions (DSP: 21 ms., Classification: 1 ms., Anomaly: 0 ms.):
[0.01532, 0.00044, 0.00618, 0.97806, 0.134]
```

Which matches the values we just saw in the studio. You now have your impulse running on your Thunderboard Sense 2 development board!


Built with [Mintlify](https://mintlify.com).