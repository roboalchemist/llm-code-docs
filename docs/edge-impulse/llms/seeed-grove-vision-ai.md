# Source: https://docs.edgeimpulse.com/hardware/boards/seeed-grove-vision-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed Grove - Vision AI Module

[Grove - Vision AI Module](https://wiki.seeedstudio.com/Grove-Vision-AI-Module) is a thumb-sized board based on Himax HX6537-A processor which is equipped with a 2-Megapixel OV2640 camera, microphone, 3-axis accelerometer and 3-axis gyroscope. It offers storage with 32 MB SPI flash, comes pre-installed with ML algorithms for face recognition and people detection and supports customized models as well. It is compatible with the XIAO ecosystem and Arduino, all of which makes it perfect for getting started with AI-powered machine learning projects!

It is fully supported by Edge Impulse which means you will be able to sample raw data from each of the sensors, build models, and deploy trained machine learning models to the module directly from the studio without any programming required. Grove - Vision AI Module is available for purchase directly from [Seeed Studio Bazaar](https://www.seeedstudio.com/Grove-Vision-AI-Module-p-5457.html).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/1.jpg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=676397cbfc1d927ef4dc29951cf08a50" width="1250" height="1000" data-path=".assets/images/1.jpg" />
</Frame>

*Quick links access:*

* Firmware source code: [GitHub repository](https://github.com/edgeimpulse/firmware-seeed-grove-vision-ai)
* Pre-compiled firmware: [seeed-grove-vision-ai.zip](https://cdn.edgeimpulse.com/firmware/seeed-grove-vision-ai.zip)

### Installing dependencies

To set this board up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.
3. Download the latest [Bouffalo Lab Dev Cube](https://dev.bouffalolab.com/download)

<Warning>
  **Problems installing the Edge Impulse CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the board to Edge Impulse.

#### 1. Update BL702 chip firmware

BL702 is the USB-UART chip which enables the communication between the PC and the Himax chip. You need to update this firmware in order for the Edge Impulse firmware to work properly.

1. [Get the latest bootloader firmware](https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/releases) (**tinyuf2-grove\_vision\_ai\_vX.X.X.bin**)
2. Connect the board to the PC via a USB Type-C cable while holding down the **Boot** button on the board

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/2.jpg?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=cb97ca7c91ea3cf89eae099295b6e697" width="1200" height="380" data-path=".assets/images/2.jpg" />
   </Frame>
3. Open previously installed Bouffalo Lab Dev Cube software, select **BL702/704/706**, and then click **Finish**

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p4.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=6ce3e8f93218756eda97c75a4d1ead3f" width="349" height="454" data-path=".assets/images/seeed-sensecap-a1101/p4.png" />
   </Frame>
4. Go to **MCU** tab. Under **Image file**, click **Browse** and select the firmware you just downloaded.

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/4.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=2556a60fe3a185cfb5aabe711fa3778f" width="1553" height="432" data-path=".assets/images/4.jpg" />
   </Frame>
5. Click **Refresh**, choose the **Port** related to the connected board, set **Chip Erase** to **True**, click **Open UART**, click **Create & Download** and wait for the process to be completed .

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p6.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=523d5df40a4e88444c686621f145d370" width="363" height="557" data-path=".assets/images/seeed-sensecap-a1101/p6.png" />
   </Frame>

You will see the output as **All Success** if it went well.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/6.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=4bbfe2e3814f45ea1ceb91427442135a" width="1549" height="560" data-path=".assets/images/6.jpg" />
</Frame>

**Note:** If the flashing throws an error, try to click **Create & Download** multiple times until you see the **All Success** message.

#### 2. Update Edge Impulse firmware

The board does not come with the right Edge Impulse firmware yet. To update the firmware:

1. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/seeed-grove-vision-ai.zip) and extract it to obtain **firmware.uf2** file
2. Connect the board again to the PC via USB Type-C cable and double-click the **Boot** button on the board to enter **mass storage mode**
3. After this you will see a new storage drive shown on your file explorer as **GROVEAI**. Drag and drop the **firmware.uf2** file to GROVEAI drive

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/7.jpg?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=7fcc3066a853d9d9571151301d915fda" width="269" height="93" data-path=".assets/images/7.jpg" />
</Frame>

Once the copying is finished **GROVEAI** drive will disappear. This is how we can check whether the copying is successful or not.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/8.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=1d06e843aa95cd2c155caa9d2cc5bfc0" width="1458" height="441" data-path=".assets/images/8.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build and run your first machine learning model with these tutorials:

#### Image models

* [Image classification](/tutorials/end-to-end/image-classification)
* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes).
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

#### Audio models

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)

#### IMU models

* [Continuous motion recognition](/tutorials/end-to-end/motion-recognition)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

After building the machine learning model and downloading the Edge Impulse firmware from Edge Impulse Studio, deploy the model uf2 to Grove - Vision AI by following **steps 1 and 2** under [**Update Edge Impulse firmware section**](/hardware/boards/seeed-grove-vision-ai#2-update-edge-impulse-firmware).

#### Compile Edge Impulse firmware from source

If you want to compile the Edge Impulse firmware from the source code, you can visit [this GitHub repo](https://github.com/edgeimpulse/firmware-seeed-grove-vision-ai) and follow the instructions included in the README.

The model used for the official firmware can be found in this [public project](https://studio.edgeimpulse.com/public/87291/latest).


Built with [Mintlify](https://mintlify.com).