# Source: https://docs.edgeimpulse.com/hardware/boards/ambiq-apollo5.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ambiq Apollo5 evaluation boards

Introducing [Apollo510 System-on-Chip (SoC)](https://ambiq.com/apollo510/), a cutting-edge solution engineered to revolutionize the landscape of ultra-low-power performance in conventional edge and AI applications. Leveraging Ambiq's advanced Subthreshold Power Optimized Technology (SPOT®), Apollo510 delivers exceptional energy efficiency, operating on minimal power while providing unparalleled performance. Equipped with an Arm® Cortex®-M55 application processor running at up to 250MHz, this SoC enables efficient and high-performance computing, empowering developers to design innovative devices with ease.

Apollo510 incorporates advanced security features in secureSPOT® 3.0 with TrustZone® technology, such as secure boot and secure firmware updates, ensuring the integrity and confidentiality of data transmitted and processed by connected devices, making it an ideal choice for secure deployment in bodyworn and ambient AI applications. Designed to meet the evolving needs of conventional edge and AI devices, the Apollo510 represents a significant leap forward in energy efficiency, performance, and security. With its unparalleled combination of ultra-low power operation, high-performance computing capabilities, and robust security features, this wireless SoC is designed to drive innovation and enable the next generation of smart and connected devices.

**Features**

* Up to 250 MHz Arm Cortex-M55 application processor with turboSPOT® and Helium™ technology
* Enhanced memory performance with 64KB I-Cache and 64KB D-Cache, 3.75MB of system RAM, and 4MB of embedded non-volatile memory for code/data
* Ultra-low power ADC and stereo digital microphone PDM interfaces for truly always-on voice
* High-fidelity telco-quality audio
* High-speed USB 2.0
* Wide range of integrated sensor interfaces including ADC, SPI, I²C, and UART

<Frame caption="Ambiq Apollo5 SoC">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-SoC.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=6e182af32b419bb448ef8f4362523814" width="300" height="260" data-path=".assets/images/ambiq/ambiq-apollo5-SoC.png" />
</Frame>

## Deployment options

<AccordionGroup>
  <Accordion title="Ambiq Apollo510 EVB firmware">
    A binary containing both the Edge Impulse data acquisition client and your full impulse.
  </Accordion>
</AccordionGroup>

## Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation)
2. [Segger JLink](https://www.segger.com/downloads/jlink/)

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting the Apollo 5 Audio Add-on Board (Models with Audio Input Only)

This step is only needed when using models requiring microphone input, such as the example below. Skip this section if you are testing other models that do not need audio input.

Connect the microphone board to the Apollo510-EVB as shown below.

<Frame caption="Apollo510-EVB With Microphone">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-plus-PDM.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=1947dec615068a1248af65ca66250e93" width="1097" height="1000" data-path=".assets/images/ambiq/ambiq-apollo5-plus-PDM.png" />
</Frame>

### Connecting an ArduCam Mega 5MP SPI

This step is only needed when using models requiring camera input. Skip this section if you are testing other models that do not need camera input.

The [ArduCam Mega 5MP SPI](https://www.arducam.com/product/presale-mega-5mp-color-rolling-shutter-camera-module-with-autofocus-lens-for-any-microcontroller/) connects to the Apollo510-EVB pins as shown in the table below:

| Camera Pin | EVB Pin     |
| ---------- | ----------- |
| GND        | Any EVB GND |
| 5V/VDD     | Any EVB 5V  |
| SCK        | Pin 47      |
| MISO       | Pin 49      |
| MOSI       | Pin 48      |
| CS         | Pin 60      |

<Frame caption="ArduCam connected">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-plus-arducam-5mp-spi.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=ac5f518d6d9d2eec8f1629131bcd7cfd" width="954" height="1000" data-path=".assets/images/ambiq/ambiq-apollo5-plus-arducam-5mp-spi.png" />
</Frame>

<Warning>
  **The wiring harness provided with the camera can be sensitive, so pin jumpers or another wiring harness may help**
</Warning>

### Flashing pre-built firmware

Pre-built image with only audio support and "Hello World" detector example [here](https://cdn.edgeimpulse.com/build-system/firmware-ambiq-apollo510-audio.zip)

Get started by extracting the archive and choose the appropriate script for your system architecture to flash the firmware:

<Frame caption="Flashing new firmware">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-flash.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=dbd6b6444c8bcb6f83ada26480584e5a" width="591" height="1000" data-path=".assets/images/ambiq/ambiq-apollo5-flash.png" />
</Frame>

## Connecting to Edge Impulse

### Using the daemon

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, you can access the project API Key as shown below by navigating to the **Dashboard** section on the left pane of your Studio project and select the **Keys** tab, then click the copy/paste icon next to the API Key to copy the entire text to your clipboard, then run:

```
edge-impulse-daemon --api-key [paste your key here]
```

<Frame caption="edge-impulse-api-key">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/API-Key-annotated.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=e347035d11c0117f84244ec5badba18a" width="1188" height="336" data-path=".assets/images/API-Key-annotated.png" />
</Frame>

### Connecting to Studio

Run the `edge-impulse-daemon` and connect to your project, you will be prompted to name your device:

<Frame caption="Connecting to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-daemon-connect.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=0d431a13dc7160bc4f1dd2d935bdc151" width="1544" height="1000" data-path=".assets/images/ambiq/ambiq-apollo5-daemon-connect.png" />
</Frame>

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-device-connected.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=b830ebb3ad89f7044989ff38a02b56cd" width="910" height="100" data-path=".assets/images/ambiq/ambiq-apollo5-device-connected.png" />
</Frame>

### Collecting data

#### Audio

With the device connected to Studio, you can use it to collect audio data up to 5 seconds in length for training and testing your model. Navigate to the Data acquisition tab and start collecting samples:

<Frame caption="How to collect an audio sample">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-sample-audio.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=5c760035f115dd604150708d84078a16" width="1088" height="862" data-path=".assets/images/ambiq/ambiq-apollo4-sample-audio.png" />
</Frame>

Daemon output during sampling:

<Frame caption="Collecting an audio sample">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-daemon-sample.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=9c9a878fb7c75bb402e8ded339450a67" width="636" height="359" data-path=".assets/images/ambiq/ambiq-apollo4-daemon-sample.png" />
</Frame>

<br />

<Frame caption="Example sample">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-audio-sample.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=d281a50f3a42f10116e74708af05e25b" width="1030" height="694" data-path=".assets/images/ambiq/ambiq-apollo4-audio-sample.png" />
</Frame>

##### Video

<Frame caption="How to collect an image sample">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-camera-sample.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=ff5356f702535662915934f0846529a4" width="921" height="335" data-path=".assets/images/ambiq/ambiq-apollo4-camera-sample.png" />
</Frame>

Sampling images:

<Frame caption="Collecting an image sample">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-camera-ingest.gif?s=215354109424eec9331b87b928eede8d" width="800" height="554" data-path=".assets/images/ambiq/ambiq-apollo4-camera-ingest.gif" />
</Frame>

Three supported sizes 96x96, 128x128, 160x160:

<Frame caption="Three different options">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-samples-camera.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=38e4e012d39d96981d1025509bc09729" width="1134" height="438" data-path=".assets/images/ambiq/ambiq-apollo4-samples-camera.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Recognizing sounds from audio](/tutorials/end-to-end/sound-recognition)
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Detecting objects with FOMO](/tutorials/end-to-end/object-detection-centroids)

### Example project

Start by going to [your Studio projects](https://studio.edgeimpulse.com/studio/profile/projects) then create a new project and navigate to the `Create impulse` section of `Impulse design`, at which point you will be prompted to select your target, choose the Apollo5:

<Frame caption="Choosing target hardware">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-target-select.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=b491818fffa66deed56ae86696472c82" width="897" height="1000" data-path=".assets/images/ambiq/ambiq-apollo5-target-select.png" />
</Frame>

Then add the DSP block:

<Frame caption="DSP">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-add-dsp.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=ed270af68819e601cbfb611d27249525" width="1152" height="1000" data-path=".assets/images/ambiq/ambiq-apollo4-add-dsp.png" />
</Frame>

Then the keyword spotting learn block:

<Frame caption="KWS">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-add-learn.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=73defab8d031043913a2ec5aa0d5b53f" width="1078" height="1000" data-path=".assets/images/ambiq/ambiq-apollo4-add-learn.png" />
</Frame>

And finally save the impulse:

<Frame caption="Saving it all">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-impulse.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=6a7bb83f0fb393833bd7ed484de4d4a5" width="1600" height="625" data-path=".assets/images/ambiq/ambiq-apollo4-impulse.png" />
</Frame>

#### Processing

Now select the DSP block:

<Frame caption="Select DSP">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-dsp-select.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=caa0c8ff9ba6726c09d1c4554a5a1180" width="309" height="1000" data-path=".assets/images/ambiq/ambiq-apollo4-dsp-select.png" />
</Frame>

And go to `Generate features`:

<Frame caption="Generate features">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-dsp-gen.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=388b6bc572388f53995cabc4a8fdcb95" width="1600" height="788" data-path=".assets/images/ambiq/ambiq-apollo4-dsp-gen.png" />
</Frame>

Click the button and wait for the job to finish, when it does you'll see something like this:

<Frame caption="DSP complete">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-dsp.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=2e1190ec04db2962752d61d257f6b28a" width="1600" height="793" data-path=".assets/images/ambiq/ambiq-apollo4-dsp.png" />
</Frame>

#### Training

Select the learning block:

<Frame caption="Select learning block">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-train-select.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=bce356e7c14437640f3907fa339dd367" width="370" height="920" data-path=".assets/images/ambiq/ambiq-apollo4-train-select.png" />
</Frame>

Then click `Save & train` and you'll eventually see an output like this:

<Frame caption="Training">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-train.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=507d4d42a0a40b126d4384d69d3808c7" width="1600" height="989" data-path=".assets/images/ambiq/ambiq-apollo4-train.png" />
</Frame>

#### Testing

Go to the `Model testing` section and enable int8 testing:

<Frame caption="Select int8 testing">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-test-select.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=283638412aa476a040dc99f00e37649e" width="205" height="140" data-path=".assets/images/ambiq/ambiq-apollo4-test-select.png" />
</Frame>

And run the test:

<Frame caption="Test results">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-test.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=eca51d0ddf8019a3536b1fb26f26ef9e" width="1600" height="727" data-path=".assets/images/ambiq/ambiq-apollo4-test.png" />
</Frame>

#### Deploying

Navigate to the `Deployment` section and choose the **Apollo 5**:

<Frame caption="Selecting the Apollo5">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/ambiq/ambiq-apollo5-deploy-select.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=4dd98dcada3b907a72f1014b08ef3d89" width="1402" height="654" data-path=".assets/images/ambiq/ambiq-apollo5-deploy-select.png" />
</Frame>

Now click `Build` and wait for the job to finish, when it does a zip archive will be downloaded to your computer.

#### Flashing

See the previous section on flashing the board.

#### Running the impulse

You can run your impulse by using `edge-impulse-run-impulse`:

<Frame caption="Running the impulse">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-run-impulse.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=642d5b0989194ac2b09176ff336bf770" width="472" height="411" data-path=".assets/images/ambiq/ambiq-apollo4-run-impulse.png" />
</Frame>

## Troubleshooting

If you have problems with the flashing script make sure you are using USB cables with data and not just power-only cables.

Reach out to us on the [forum](https://forum.edgeimpulse.com/) and have fun making machine learning models on the [Apollo510-EVB](https://ambiq.com/apollo510/) from Ambiq!


Built with [Mintlify](https://mintlify.com).