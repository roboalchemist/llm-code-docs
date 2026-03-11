# Source: https://docs.edgeimpulse.com/hardware/devices/seeed-sensecap-a1101.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed SenseCAP A1101

[Seeed SenseCAP A1101](https://www.seeedstudio.com/SenseCAP-A1101-LoRaWAN-Vision-AI-Sensor-p-5367.html) - LoraWAN Vision AI Sensor is an image recognition AI sensor designed for developers. SenseCAP A1101 - LoRaWAN Vision AI Sensor combines TinyML AI technology and LoRaWAN long-range transmission to enable a low-power, high-performance AI device solution for both indoor and outdoor use.

This sensor features Himax high-performance, low-power AI vision solution which supports the Google LiteRT (previously Tensorflow Lite) framework and multiple TinyML AI platforms.

<Frame caption="Seeed SenseCAP A1101">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p1.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=c6bdea3ed2df34294bde44498c13ce3d" width="1333" height="1000" data-path=".assets/images/seeed-sensecap-a1101/p1.jpg" />
</Frame>

It is fully supported by Edge Impulse which means you will be able to sample raw data from the camera, build models, and deploy trained machine learning models to the module directly from the studio without any programming required. SenseCAP - Vision AI Module is available for purchase directly from [Seeed Studio Bazaar](https://www.seeedstudio.com/SenseCAP-A1101-LoRaWAN-Vision-AI-Sensor-p-5367.html).

### Installing dependencies

To set A1101 up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. On Linux:
   * GNU Screen: install for example via sudo apt install screen.
3. Download the latest [Bouffalo Lab Dev Cube-All-Platform](https://dev.bouffalolab.com/download)

<Warning>
  **Problems installing the Edge Impulse CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place, it's time to connect the A1101 to Edge Impulse.

#### 1. Update BL702 chip firmware

BL702 is the USB-UART chip which enables the communication between the PC and the Himax chip. You need to update this firmware in order for the Edge Impulse firmware to work properly.

1. [Get the latest bootloader firmware](https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/releases) (**tinyuf2-sensecap\_vision\_ai\_X.X.X.bin.**)

2. Connect the A1101 to the PC via a USB Type-C cable while holding down the **Boot** button on the A1101.

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p2.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=b3ec3d039ebf921f0c63f03d4adb43af" width="600" height="326" data-path=".assets/images/seeed-sensecap-a1101/p2.png" />
   </Frame>

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p3.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=3d6742014bd3e51a37e6c33010d84f20" width="600" height="218" data-path=".assets/images/seeed-sensecap-a1101/p3.png" />
   </Frame>

3. Open previously installed Bouffalo Lab Dev Cube software, select **BL702/704/706**, and then click **Finish**

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=39243473d4bcaf28035875a0064575e9" width="349" height="454" data-path=".assets/images/3.jpg" />
   </Frame>

4. Go to the **MCU** tab. Under **Image file**, click **Browse** and select the firmware you just downloaded.

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p5.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=c33dc766a95496b43530b2e08b820cf3" width="1323" height="346" data-path=".assets/images/seeed-sensecap-a1101/p5.png" />
   </Frame>

5. Click **Refresh**, choose the **Port** related to the connected A1101, set **Chip Erase** to **True**, click **Open UART**, click **Create & Download** and wait for the process to be completed .

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5.jpg?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=587b555996948d8e628a38415befd105" width="363" height="557" data-path=".assets/images/5.jpg" />
   </Frame>

You will see the output as **All Success** if it went well.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p7.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=13464f4bbe1cf4d9e3cecb9e8c0b29b3" width="1549" height="560" data-path=".assets/images/seeed-sensecap-a1101/p7.png" />
</Frame>

<Info>
  If the flashing throws an error, click **Create & Download** multiple times until you see the **All Success** message.
</Info>

#### 2. Update Edge Impulse firmware

A1101 does not come with the right Edge Impulse firmware yet. To update the firmware:

1. Download the latest [Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/seeed-sensecap-a1101.zip) and extract it to obtain **firmware.uf2** file
2. Connect the A1101 again to the PC via USB Type-C cable and double-click the **Boot** button on the A1101 to enter **mass storage mode**
3. After this you will see a new storage drive shown on your file explorer as **SENSECAP**. Drag and drop the **firmware.uf2** file to **SENSECAP** drive

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p8.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=1448dfe5cc33d6b8705b488e19af8721" width="265" height="68" data-path=".assets/images/seeed-sensecap-a1101/p8.png" />
   </Frame>

Once the copying is finished **SENSECAP** drive will disappear. This is how we can check whether the copying is successful or not.

#### 3. Setting keys

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This will start a wizard which will ask you to log in, and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your A1101, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 4. Verifying that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p9.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=d13a8adc20974178a1b37d2b442fc5f9" width="1600" height="262" data-path=".assets/images/seeed-sensecap-a1101/p9.png" />
</Frame>

Device connected to Edge Impulse correctly!

### Next steps: building a machine learning model

With everything set up, you can now build and run your first machine learning model with these tutorials:

* [object detection](/tutorials/end-to-end/object-detection-bounding-boxes)..
* [Object detection with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

#### Collecting data from Seeed SenseCAP A1101

Frames from the onboard camera can be directly captured from the studio:

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p16.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=f872645b9e8cae012a2703a61011e5ea" width="1600" height="836" data-path=".assets/images/seeed-sensecap-a1101/p16.png" />
</Frame>

Finally, once a model is trained, it can be easily deployed to the A1101 – Vision AI Module to start inferencing!

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p17.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=7d7344d3b2521eeaabfaa20b971566a5" width="1462" height="1000" data-path=".assets/images/seeed-sensecap-a1101/p17.png" />
</Frame>

### Deploying back to device

After building the machine learning model and downloading the Edge Impulse firmware from Edge Impulse Studio, deploy the model uf2 to SenseCAP - Vision AI by following **steps 1 and 2** under [Update Edge Impulse firmware](/hardware/devices/seeed-sensecap-a1101#2-update-edge-impulse-firmware).

Drag and drop the **firmware.uf2** file from EDGE IMPULSE to **SENSECAP** drive.

When you run this on your local interface:

```
edge-impulse-daemon --debug
```

it will ask you to click a URL, then you will see a live preview of the camera on your device.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p21.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=94bac404238e45467b2f8ab36e9daa28" width="1600" height="840" data-path=".assets/images/seeed-sensecap-a1101/p21.png" />
</Frame>

#### Compile Edge Impulse firmware from source

If you want to compile the Edge Impulse firmware from the source code, you can visit [this GitHub repo](https://github.com/edgeimpulse/firmware-seeed-grove-vision-ai) and follow the instructions included in the README.

The model used for the official firmware can be found in this [public project](https://studio.edgeimpulse.com/public/87291/latest).

### Connect to the LoraWAN® Network

In addition to connecting directly to a computer to view real-time detection data, you can also transmit these data through LoraWAN® and finally upload them to the [SenseCAP cloud platform](https://sensecap.seeed.cc/) or a third-party cloud platform. On the SenseCAP cloud platform, you can view the data in a cycle and display it graphically through your mobile phone or computer. The SenseCAP cloud platform and SenseCAP Mate App use the same account system.

Since our focus here is on describing the model training process, we won't go into the details of the cloud platform data display. But if you're interested, you can always visit the SenseCAP cloud platform to try adding devices and viewing data. It's a great way to get a better understanding of the platform's capabilities!

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p22.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=abe2ff43c67ed78272263b8fa3bd499b" width="1430" height="848" data-path=".assets/images/seeed-sensecap-a1101/p22.png" />
</Frame>

You can get more information on [how to use SenseCAP A1101 here](https://wiki.seeedstudio.com/Train-Deploy-AI-Model-A1101).

#### How to Select a LoRaWAN Gateway

LoRaWAN® network coverage is required when using sensors, there are two options.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p23.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=80e32a1b68323a35ccbe95390d0adae0" width="1408" height="724" data-path=".assets/images/seeed-sensecap-a1101/p23.png" />
</Frame>

Seeed provides:

* [SenseCAP M2](https://www.seeedstudio.com/SenseCAP-M2-Light-Hotspot-and-Software-License.html) for Helium network
* [SenseCAP M2 Multi-Platform](https://www.seeedstudio.com/SenseCAP-M2-Light-Hotspot-and-Software-License.html) for standard LoraWAN® network

### Configure your model on the SenseCraft App

1. Download [SenseCraft App](https://wiki.seeedstudio.com/sensecraft-app/overview/) (formerly SenseCAP Mate App)
   * [Android](https://play.google.com/store/apps/details?id=cc.seeed.sensecapmate)
   * [iOS](https://apps.apple.com/us/app/sensecraft/id1619944834)

2. Open SenseCraft and login

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p10.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=6dafa703e99298de0279ed028f61135c" width="600" height="617" data-path=".assets/images/seeed-sensecap-a1101/p10.png" />
   </Frame>

3. Under **Config** screen, select **Vision AI Sensor**

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p11.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=169160ac3ffdc9ddfb601bfb42505247" width="400" height="865" data-path=".assets/images/seeed-sensecap-a1101/p11.jpg" />
   </Frame>

4. Press and hold the configuration button on the SenseCap A1101 for 3 seconds to enter bluetooth pairing mode

   <Columns cols={2}>
     <Frame caption="">
       <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p12.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=0df9f303b57d4abe0b13944ad3188d59" width="400" height="865" data-path=".assets/images/seeed-sensecap-a1101/p12.jpg" />
     </Frame>

     <Frame caption="">
       <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p13.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=ef9697eb767f17f774631249ad0fccee" width="400" height="865" data-path=".assets/images/seeed-sensecap-a1101/p13.jpg" />
     </Frame>
   </Columns>

5. Click **Setup** and it will start scanning for nearby SenseCAP A1101 devices- Go to **Settings** and make sure **Object Detection** and **User Defined 1** is selected. If not, select it and click **Send**

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p14.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=8cf5f9c6e50e79da4d8ff83fc6928cd9" width="400" height="865" data-path=".assets/images/seeed-sensecap-a1101/p14.jpg" />
   </Frame>

6. Go to **General** and click **Detect**, you'll see the actual data here.

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p15.jpg?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=5adfb111b58ba3e53efcd87908c20c44" width="400" height="865" data-path=".assets/images/seeed-sensecap-a1101/p15.jpg" />
   </Frame>

7. [Click here](https://files.seeedstudio.com/grove_ai_vision/index.html) to open a preview window of the camera stream

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p18.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=2ebeb580c0fe4a95829432e90f051efc" width="1600" height="873" data-path=".assets/images/seeed-sensecap-a1101/p18.png" />
   </Frame>

8. Click **Connect** button. Then you will see a pop up on the browser. Select **SenseCAP Vision AI - Paired** and click **Connect**

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p19.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=76052a6ca72e97e8034ac5d46210f6bd" width="1600" height="642" data-path=".assets/images/seeed-sensecap-a1101/p19.png" />
   </Frame>

9. View real-time inference results using the preview window!

   <Frame caption="">
     <img src="https://mintcdn.com/edgeimpulse/ZICERtDzIAbaSxxe/.assets/images/seeed-sensecap-a1101/p20.png?fit=max&auto=format&n=ZICERtDzIAbaSxxe&q=85&s=d8bbd1662f0085a3fc0576dc2e4b3f26" width="1374" height="862" data-path=".assets/images/seeed-sensecap-a1101/p20.png" />
   </Frame>

The cats are detected with bounding boxes around them. Here "0" corresponds to each detection of the same class. If you have multiple classes, they will be named as `0, 1, 2, 3, 4` and so on. Also the confidence score for each detected object (0.72 in above demo) is displayed!


Built with [Mintlify](https://mintlify.com).