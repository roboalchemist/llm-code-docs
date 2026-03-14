# Source: https://docs.edgeimpulse.com/hardware/deployments/run-openmv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run OpenMV library or firmware

Impulses can be deployed as an optimized OpenMV library or firmware. This packages all your signal processing blocks, configuration and learning blocks up into a single package. You can include this package in your own application to run the impulse locally. In this tutorial, you'll export an impulse and run the application on one of the OpenMV compatible boards.

### Prerequisites

Make sure you followed either the [Image classification](/tutorials/end-to-end/image-classification/) or the [FOMO: Object detection for constrained devices](/studio/projects/learning-blocks/blocks/object-detection/fomo) tutorials, have a trained impulse, and can have the **latest** [**OpenMV IDE v2.9.0**](https://openmv.io/pages/download) **or above**.

### Compatible camera-boards

* OpenMV Cam M7
* OpenMV Cam H7
* [OpenMV Cam H7 Plus](/hardware/boards/openmv-cam-h7-plus)
* OpenMV Pure Thermal
* [Arduino Portenta H7 + Vision shield](/hardware/boards/arduino-portenta-h7)
* Arduino Nicla Vision
* OpenMV Cam RT1062

### Deploying your impulse as an OpenMV library

*This method only works on **small image classification models**, if you run into a memory issue, please head to* [*Deploying your impulse as an OpenMV firmware*](/hardware/deployments/run-openmv#deploying-your-impulse-as-an-openmv-firmware) *section (preferred method).*

Head over to your Edge Impulse project, and go to **Deployment**. From here you can create the full library which contains the impulse and all external required libraries. Select **OpenMV library** and click **Build** to create the library. Then download and extract the .zip file.

To add the model to your OpenMV camera copy the `trained.tflite` and `labels.txt` files to the 'OpenMV Cam' volume (like a USB drive).

<Frame caption="Uploading the trained model to your OpenMV camera">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6fc8f98-ezgif-2-55f9767e00d1.gif?s=a42af046c0b2ef39c98bad63d653aa28" width="800" height="468" data-path=".assets/images/6fc8f98-ezgif-2-55f9767e00d1.gif" />
</Frame>

Next, open the `ei_image_classification.py` file in the OpenMV IDE, and press the 'Play' icon to run the script.

<Frame caption="Running your impulse on your OpenMV camera.">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/open-mv-screenshot.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=ee18c91299279579eacebd941e38622e" width="1447" height="753" data-path=".assets/images/open-mv-screenshot.png" />
</Frame>

### Deploying your impulse as an OpenMV firmware

*This method is preferred.*

In this section, we will flash a new firmware to the board that contains only what is necessary to run your impulse. This firmware includes your custom edge impulse model.

Head over to your Edge Impulse project, go to **Deployment**, click on **OpenMV firmware** and **Build**:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/de86a3e-45ad44c-Screenshot_2022-03-22_at_18.01.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=26782b743929a6e41dfd1053ba00b588" width="1498" height="1000" data-path=".assets/images/de86a3e-45ad44c-Screenshot_2022-03-22_at_18.01.png" />
</Frame>

Save the generated .zip file, extract it and you should see the following structure:

```
.
├── edge_impulse_firmware_niclav.bin
├── edge_impulse_firmware_openmv3.bin
├── edge_impulse_firmware_openmv4.bin
├── edge_impulse_firmware_openmv4P.bin
├── edge_impulse_firmware_openmvPT.bin
├── edge_impulse_firmware_portenta.bin
├── edge_impulse_firmware_openmv_rt1060.bin
└── ei_object_detection.py
```

<Info>
  **Firmware naming**

  The naming is likely to change soon to be more explicit. In the meantime, here is the firmware-board correspondence:

  * NICLAV - Arduino Nicla Vision
  * OPENMV3 - OpenMV Cam M7
  * OPENMV4 - OpenMV Cam H7
  * OPENMV4P - OpenMV Cam H7 Plus
  * OPENMVPT - OpenMV Pure Thermal
  * PORTENTA - Arduino Portenta
  * RT1060 - OpenMV Cam RT1062
</Info>

Plug your device into your computer. *Note: If you are using one of the Arduino boards, **double press on the RESET button**.*

Then, on your OpenMV IDE, go to **Tools->Run Bootloader (Load Firmware)**.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/91114f1-Screenshot_2022-03-22_at_16.16.47.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=566e5bae531e1d39e0beeb41c5c130c8" width="1532" height="584" data-path=".assets/images/91114f1-Screenshot_2022-03-22_at_16.16.47.png" />
</Frame>

Select **Erase internal file system**:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/qzz8ALldRag_9UsW/.assets/images/ae7326a-Screenshot_2022-03-22_at_18.43.04.png?fit=max&auto=format&n=qzz8ALldRag_9UsW&q=85&s=fadf92e8cc4fc53b792e58a7806aa636" width="1032" height="236" data-path=".assets/images/ae7326a-Screenshot_2022-03-22_at_18.43.04.png" />
</Frame>

Click on **Run** and wait until the board's blue LED blinks. You should see one of the following screen:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/956a46e-Screenshot_2022-03-22_at_16.32.44.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=639fc36339bbf33ab5b126352c29e211" width="832" height="666" data-path=".assets/images/956a46e-Screenshot_2022-03-22_at_16.32.44.png" />
</Frame>

Click on **OK** and open **(File->Open File)** the `ei_image_classification.py` or `ei_object_detection.py` script provided in the downloaded .zip.

To run the script, click on the "Play" button on the bottom-left corner of the OpenMV IDE.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/9d3b58a-Screenshot_2022-03-22_at_16.50.58.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=06897b9abe71589be7f0a678776c0b1b" width="1600" height="882" data-path=".assets/images/9d3b58a-Screenshot_2022-03-22_at_16.50.58.png" />
</Frame>

Voilà! You now have your impulse running on your OpenMV camera!

### Troubleshooting

#### Only quantized (int8) models are supported

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cU2n98Ml68g1eiRr/.assets/images/bc53ad3-Screenshot_2022-03-22_at_12.01.42.png?fit=max&auto=format&n=cU2n98Ml68g1eiRr&q=85&s=5ae8b3009ebaddb8acf8ad781e49b84f" width="1338" height="978" data-path=".assets/images/bc53ad3-Screenshot_2022-03-22_at_12.01.42.png" />
</Frame>

OpenMV only supports quantized models. However, if you encounter this issue, here is a quick fix: Click on C++ library, select Quantized (int8) at the bottom of the Deployment page and select again the OpenMV firmware to build again. This issue will be fixed in the next release, OpenMV deployment jobs will be forced to use int8 models.

#### No DFU settings for the selected board type!

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/d021a8f-Screenshot_2022-03-22_at_20.14.25.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=01bcb9a97d02a79b085bbf372588414b" width="816" height="290" data-path=".assets/images/d021a8f-Screenshot_2022-03-22_at_20.14.25.png" />
</Frame>

Your board has not been put in bootloader mode. This happens on Arduino boards if you have not **double press the RESET button** before uploading the firmware.

#### RuntimeError: Sensor control failed.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/083f254-Screenshot_2022-03-22_at_16.25.36.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=835a1a8ec1cd0b9a522b80a0d039d1f4" width="722" height="258" data-path=".assets/images/083f254-Screenshot_2022-03-22_at_16.25.36.png" />
</Frame>

The Arduino Portenta only supports greyscale images, change:

```
sensor.set_pixformat(sensor.RGB565)
```

to

```
sensor.set_pixformat(sensor.GRAYSCALE)
```


Built with [Mintlify](https://mintlify.com).