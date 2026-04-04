# Source: https://docs.edgeimpulse.com/hardware/boards/himax-ism-wise-eye-2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Himax WiseEye2 Module and ISM Devboard

WiseEye™ seamlessly integrates the Himax proprietary ultralow power AI processors, always-on CMOS image sensors, and advanced CNN-based AI algorithms, revolutionizing battery-powered, on-device vision AI applications. With power consumption of just a few milliwatts, WiseEye™ targets battery-powered endpoint AI device markets to drive AI for everyday life. Such devices typically demand extended battery life to minimize maintenance and enhance usability. WiseEye™ delivers intuitive and intelligent user interactions, making advanced AI sensing possible even in power-constrained environments. By bringing advanced, user-friendly AI capabilities, WiseEye™ sets a new standard for endpoint AI, offering unmatched performance and extended operational lifetimes.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=514e70d627a2a1cac1d2941cb6b52de8" width="722" height="353" data-path=".assets/images/himax-wise-eye-2-ism.png" />
</Frame>

*Quick links access:*

* Information about [Himax WiseEye2 module and ISM board](https://www.himax.com.tw/products/wiseeye-ai-sensing/wiseeye-solutions/)
* Himax [Github SDK Repo for WiseEye](https://github.com/edgeimpulse/firmware-himax-ism)

### Installing dependencies

#### Preparing your Windows environment for the Himax WiseEye2 ISM Devboard

To set this board up in Edge Impulse, you will need to install the following software:

1. Start with an x64-based Windows image and install git

2. Clone the Himax WiseEye-Module-G1 SDK:

   ```bash  theme={"system"}
   git clone https://github.com/HimaxWiseEyePlus/Himax-WiseEye-Module-G1-SDK/
   ```

3. Follow the [SDK setup instructions](https://github.com/HimaxWiseEyePlus/Himax-WiseEye-Module-G1-SDK/blob/main/_Documents/1_SDK_User_Guide_GNU_V1.1.pdf) to setup and prepare the Himax WiseEye-Module-G1 SDK for use.

4. Follow the setup instructions [EVK and PC Tool User Guide](https://github.com/HimaxWiseEyePlus/Himax-WiseEye-Module-G1-SDK/blob/main/_Documents/2_EVK_and_PC_Tool_User_Guide_HX6538_ISM028_03M_V1.1.pdf) to setup and prepare the WE2\_DEMO\_TOOL for flashing.

5. Now that your Himax WiseEye2 ISM Devboard is ready and you've configured the WE2\_DEMO\_TOOL, lets proceed to install the Edge Impulse dependencies (you will typically do this on a Linux or MacOS platform). This will be to RUN the Edge Impulse model once its flashed using the Windows platform.

#### Installing Edge Impulse dependencies (MacOS/Linux)

To set this board up in Edge Impulse, you will need to install the following software - typically on a linux or macos based system.

Please install the "edge-impulse-cli" package. Full documentation on installing the edge impulse CLI can be found here: [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation)

**Note:** Make sure that you have the CLI tools version **at least 1.27.1**. You can check it with:

edge-impulse-daemon --version

<Warning>
  **Problems installing the Edge Impulse CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

Next, we head to the Edge Impulse Studio to build our ML "impulse".

### Next steps: building a machine learning model

First, lets build and run our first machine learning model with these tutorials:

#### Image models

* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

For the Himax WiseEye2 ISM Devboard, you will choose "Himax ISM" for the Target type in Edge Impulse. When performing the "Deployment" step, please also select and choose the "Himax ISM" platform as the deployment platform target.  You will also need to ensure that you create  your impulse/model with "Int8 Profiling" enabled. You will need to select the "Quantized int8" checkbox when you perform the model deployment.

#### Utilizing the ISM Devboard for data capture

You can utilize the Himax WiseEye2 ISM Devboard itself to help with image capturing/data collection for your project by connecting your ISM Devboard to your development platform and then run the "edge-impulse-daemon" as follows (this can be done on Linux/MacOS or Windows if you have the "edge-impulse-cli" package installed):

edge-impulse-daemon --clean

When launched, you will be prompted to log into your Edge Impulse account, select a project, select the associated USB port that the ISM Devboard is connected to, and finally give the device a name. You can then look in your Edge Impulse "Devices" tab to see the device by going to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here:

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-connected.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=4290a80dc9e5ccec6ede7ec8a1077789" width="1164" height="225" data-path=".assets/images/himax-wise-eye-2-ism-connected.png" />
</Frame>

You can then select your device, within Edge Impulse Studio, to use the camera/sensors to capture data for your project's data.

### Deploying back to device

When the deployment is complete, you will receive a zip file that will contain two files:

* firmware.img - the OTA image you will use to publish to your ISM Devboard via the "ota.exe" tool you reviewed above.
* readme.txt - text file will a link to this page to to review the steps if needed.

We'll take the "firmware.img" file and proceed to the next step

#### Flash the ISM Devboard to install the Edge Impulse model and its runtime

You will next run the WE\_DEMO\_TOOL on Windows:

<Frame caption="WE2_DEMO_TOOL">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-devtool.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=4ef3cc5287a46f504bdb0216bb24ffe0" width="1045" height="868" data-path=".assets/images/himax-wise-eye-2-ism-devtool.png" />
</Frame>

Select "Burn Flash", then next we press "Select File" to select the directory and file where we have placed our Edge Impulse contents (namely firmware.img and readme.txt from above). Select that directory and the "firmware.img" file:

<Frame caption="EI Firmware Selected">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-firmware.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=ad1cd994744dfc744025f0b06b6f3c32" width="1039" height="864" data-path=".assets/images/himax-wise-eye-2-ism-firmware.png" />
</Frame>

We then press the "Start" button and allow the flashing process to complete:

<Frame caption="Flashing Process">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-flash.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=3d0aa5d105d3fce6d42182915c25f59f" width="1038" height="860" data-path=".assets/images/himax-wise-eye-2-ism-flash.png" />
</Frame>

You can now disconnect the board and proceed to the Linux/MacOS platform to run the model in the next step.

#### Running the Model on the ISM Devboard (MacOS/Linux)

To run the model on your ISM Devboard now that the flashing has finished, you plug in the board via USB and then run the following in a bash shell:

edge-impulse-run-impulse --clean

After logging in and selecting the appropriate USB port that represents your board, You will now see your model's inference output displayed as data is entered (images captured/etc...)

<Frame caption="Device Running Model">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-inferences.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=0e89c2bb9a27502f2384bd7a304628f2" width="856" height="514" data-path=".assets/images/himax-wise-eye-2-ism-inferences.png" />
</Frame>

Alternatively, you can connect directly to the USB serial port and then directly interact with the AT command interpreter that is running the Edge Impulse model:

<Frame caption="Edge Impulse AT Command Interpreter">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/himax-wise-eye-2-ism-atcommand.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=62914dc11b8a903e7ad80d0a0d451f90" width="756" height="676" data-path=".assets/images/himax-wise-eye-2-ism-atcommand.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).