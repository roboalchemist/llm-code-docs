# Source: https://docs.edgeimpulse.com/hardware/boards/ambiq-apollo4.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ambiq Apollo4 evaluation boards

Ambiq®, the leader in low-power System-on-Chip (SoC) solutions, has once again raised the bar with the [Apollo4 Family of SoCs](https://ambiq.com/apollo4/). With the lowest dynamic and sleep mode power on the market, the Apollo4 allows designers of next-generation edge AI devices to take their innovative products to the next level. Built upon Ambiq’s proprietary Subthreshold Power-Optimized Technology (SPOT®) platform, the Apollo4 Family of SoCs is a complete hardware and software solution that enables the battery-powered endpoint devices of tomorrow to achieve a higher level of intelligence without sacrificing battery life. Edge Impulse support is available on the [Apollo4 Plus](https://ambiq.com/apollo4-plus/), [Apollo4 Blue Plus](https://ambiq.com/apollo4-blue-plus/), [Apollo4 Lite](https://ambiq.com/apollo4-lite/), and [Apollo4 Blue Lite](https://ambiq.com/apollo4-blue-lite/). See below for how to get started on the Apollo4 Plus and Apollo4 Blue Plus SoCs.

The Apollo4 Plus is built on the 32-bit Arm® Cortex®-M4 core with Floating Point Unit (FPU). With up to 2 MB of NVM and 2.75 MB of SRAM, the Apollo4 Plus has more than enough compute and storage to handle complex algorithms and neural networks while displaying vibrant, crystal clear, and smooth graphics. If additional memory is required, an external memory is supported through Ambiq’s multi-bit SPI and eMMC interfaces. The Apollo4 Plus is purpose-built to serve as both an application processor and a co-processor for battery-powered endpoint devices,  including predictive health and maintenance sensors, smart home devices, livestock trackers, wrist-based wearables, smart rings, smart voice devices, and more. The Apollo4 Plus is available now in BGA packaging. The Apollo4 Blue Plus incorporates an optional BLE 5.4 radio.

<Frame caption="Ambiq Apollo4 Blue Plus KXR Eval Board">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-blue-plus.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=e90592a804e34040ad565eda3ccba8cb" width="1585" height="1000" data-path=".assets/images/ambiq/ambiq-apollo4-blue-plus.png" />
</Frame>

## Deployment options

<Info>
  **Edge Impulse firmware**

  There is a firmware deployment option in Studio for the Apollo4 Blue Plus EVB. For the other Apollo4 boards, you will need to modify and recompile the firmware found in the Edge Impulse [firmware-ambiq-apollo4](https://github.com/edgeimpulse/firmware-ambiq-apollo4) GitHub repo.
</Info>

<AccordionGroup>
  <Accordion title="Ambiq Apollo4 Blue Plus EVB firmware">
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

### Connecting the Apollo4 Audio Add-on Board (Models with Audio Input Only)

This step is only needed when using models requiring microphone input, such as the example below. Skip this section if you are testing other models that do not need audio input.

Remove the pin header protectors on the Apollo4 Plus EVB (AMAP4PEVB) or Apollo4 Blue Plus KXR EVB (AMAP4BPXEVB), and carefully plug the Apollo4 Audio Add-onBoard (AMA4AUD) into the development board. Pay special attention to the highspeed connector with film tape, which must be removed before connecting the boards. Place the digital and analog microphone modules onto the shield, as shown in the image below, and connect cables to both type-C connectors on the evaluation board.

<Frame caption="Apollo4 Blue Plus and Apollo4 Audio Add-on Board connected to computer">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-connected.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=fbcb1fa71b0b7504953af4c487f35ef5" width="451" height="554" data-path=".assets/images/ambiq/ambiq-apollo4-connected.png" />
</Frame>

### Connecting an ArduCam Mega 5MP SPI

This step is only needed when using models requiring camera input. Skip this section if you are testing other models that do not need camera input.

The [ArduCam Mega 5MP SPI](https://www.arducam.com/product/presale-mega-5mp-color-rolling-shutter-camera-module-with-autofocus-lens-for-any-microcontroller/) connects to the Apollo4 Plus EVB and Apollo4 Blue Plus KXR EVB pins as shown in the table below:

| Camera Pin | EVB Pin     |
| ---------- | ----------- |
| GND        | Any EVB GND |
| 5V/VDD     | Any EVB 5V  |
| SCK        | Pin 8       |
| MISO       | Pin 10      |
| MOSI       | Pin 9       |
| CS         | Pin 11      |

<Frame caption="ArduCam connected">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-plus-arducam-5mp-spi.jpg?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=655feecba6e2a358487a6e9be39402c2" width="1001" height="1000" data-path=".assets/images/ambiq/ambiq-apollo4-plus-arducam-5mp-spi.jpg" />
</Frame>

<Warning>
  **The wiring harness provided with the camera can be sensitive, so pin jumpers or another wiring harness may help**
</Warning>

### Flashing pre-built firmware

Pre-built image with only audio support and "Hello World" detector example [here](https://cdn.edgeimpulse.com/build-system/ambiq-apollo4.zip)

Pre-built image with full video and audio data collection and FOMO Face detector example [here](https://cdn.edgeimpulse.com/build-system/firmware-ambiq-apollo4plus.041124.zip)

Get started by extracting the archive and choose the appropriate script for your system architecture to flash the firmware:

<Frame caption="Flashing new firmware">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-flash.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=e1286a32a863469fc3572d7e90478494" width="501" height="980" data-path=".assets/images/ambiq/ambiq-apollo4-flash.png" />
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
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-daemon-connect.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=19b7946db2e2e62bd16d6eac2af306c4" width="687" height="334" data-path=".assets/images/ambiq/ambiq-apollo4-daemon-connect.png" />
</Frame>

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-device-connected.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=bad5d478ef40d31ae33ac462bb7e100f" width="1600" height="180" data-path=".assets/images/ambiq/ambiq-apollo4-device-connected.png" />
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

If you flashed the pre-built binary with FOMO Face Detection example from above then just connect your board and run `edge-impulse-run-impulse` to see an output similar to this:

<Frame caption="FOMO Face detect output">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-fomo.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=49331a4ec11ab8df58d577cb2459cfd2" width="678" height="686" data-path=".assets/images/ambiq/ambiq-apollo4-fomo.png" />
</Frame>

### Example project

Start by going to [your Studio projects](https://studio.edgeimpulse.com/studio/profile/projects) then create a new project and navigate to the `Create impulse` section of `Impulse design`, at which point you will be prompted to select your target, choose the Apollo4 Plus:

<Frame caption="Choosing target hardware">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-target-select.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=7f4da9f4fc66fb4b19d41cbae5316b10" width="694" height="787" data-path=".assets/images/ambiq/ambiq-apollo4-target-select.png" />
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

Navigate to the `Deployment` section and choose the **Apollo4 Blue Plus**:

<Frame caption="Selecting the Apollo4">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-deploy-select.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=5d5d81bd634ab0a036e017734722113b" width="560" height="204" data-path=".assets/images/ambiq/ambiq-apollo4-deploy-select.png" />
</Frame>

Now click `Build` and wait for the job to finish, when it does a zip archive will be downloaded to your computer:

<Frame caption="Building the binary">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-deploy.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=0a157d24d296f861ba49425c0c987158" width="1577" height="886" data-path=".assets/images/ambiq/ambiq-apollo4-deploy.png" />
</Frame>

#### Flashing

See the previous section on flashing the board.

#### Running the impulse

You can run your impulse by using `edge-impulse-run-impulse`:

<Frame caption="Running the impulse">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/ambiq/ambiq-apollo4-run-impulse.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=642d5b0989194ac2b09176ff336bf770" width="472" height="411" data-path=".assets/images/ambiq/ambiq-apollo4-run-impulse.png" />
</Frame>

## Troubleshooting

If you have problems with the flashing script make sure you are using USB cables with data and not just power-only cables.

Reach out to us on the [forum](https://forum.edgeimpulse.com/) and have fun making machine learning models on the [Apollo4 Family of SoCs](https://ambiq.com/apollo4/) from Ambiq!


Built with [Mintlify](https://mintlify.com).