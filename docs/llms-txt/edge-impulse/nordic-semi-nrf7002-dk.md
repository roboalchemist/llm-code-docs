# Source: https://docs.edgeimpulse.com/hardware/boards/nordic-semi-nrf7002-dk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Nordic Semi nRF7002 DK

The Nordic Semiconductor nRF7002 DK is the development kit for the nRF7002 WiFi 6 companion IC. The kit contains everything you need to get started with your development on a single board. It features an nRF5340 multiprotocol System-on-a-Chip (SoC) as a host processor for the nRF7002 - and it is now supported by Edge Impulse.

The nRF7002 is a Wi-Fi 6 companion IC, providing seamless connectivity and Wi-Fi-based locationing (SSID sniffing of local Wi-Fi hubs). It is designed to be used alongside Nordic’s existing nRF52 and nRF53 Series Bluetooth SoCs, and nRF91 Series cellular IoT Systems-in-Package (SiPs). The nRF7002 can also be used in conjunction with non-Nordic host devices.

With its integration with Edge Impulse, you will be able to sample raw data, build models, and deploy trained machine learning models directly from the studio. As the nRF7002 DK does not have any built-in sensors, we recommend pairing this development board with the [X-NUCLEO-IKS02A1](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html) shield (with a MEMS accelerometer).

If you don't have access to the X-NUCLEO-IKS02A1 shield, you can use our [data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) to capture data from any other sensor, and then follow the [Run on Zephyr-based Nordic Semiconductor development boards](/hardware/deployments/run-cpp-zephyr-nordic) tutorial to run your impulse. Or, you can modify the example firmware (based on nRF Connect) to interact with other accelerometers or PDM microphones that are supported by Zephyr.

The Edge Impulse firmware for this development board is open source and hosted on GitHub: [edgeimpulse/firmware-nordic-nrf7002dk](https://github.com/edgeimpulse/firmware-nordic-nrf7002dk).

<Frame caption="Nordic Semiconductors nRF7002 DK development board">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF7002-DK.jpeg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=24e4bd4d97ac46317a3387f92882eb76" width="754" height="350" data-path=".assets/images/nordic/nRF7002-DK.jpeg" />
</Frame>

### Installing dependencies

To set this device up in Edge Impulse, you will need to install the following software:

1. [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
2. On Linux:
   * GNU Screen: install for example via `sudo apt install screen`.
3. Install [J-Link](https://www.segger.com/downloads/jlink/) for your device.
   * Note that for the nRF7002 DK, the required J-Link version is V7.94e

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

With all the software in place it's time to connect the development board to Edge Impulse.

<iframe src="https://www.youtube.com/embed/MKQIQ2lvJfk" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

#### 1. Plugging in the X-NUCLEO-IKS02A1 MEMS expansion shield

Remove the pin header protectors on the nRF7002 DK and plug the X-NUCLEO-IKS02A1 shield into the development board.

<Frame caption="X-NUCLEO-IKS02A1 shield plugged in to the nRF7002 DK">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF7002-connect-shield.jpg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=fe8350d9cb10a540ee6edda5f61154e3" width="1333" height="1000" data-path=".assets/images/nordic/nRF7002-connect-shield.jpg" />
</Frame>

**Note:** Make sure that the shield does not touch any of the pins in the middle of the development board. This might cause issues when flashing the board or running applications.

<Frame caption="Make sure the shield does not touch any of the pins in the middle of the development board.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF7002-shield-safety.jpg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=b5ccbe24b9abf495b5f1ee2e8edfa747" width="1400" height="757" data-path=".assets/images/nordic/nRF7002-shield-safety.jpg" />
</Frame>

#### 2. Connect the development board to your computer

Use a micro-USB cable to connect the development board to your computer. There are two USB ports on the development board, use the one on the *short* side of the board. **Then, set the power switch on the bottom left to 'on'**.

<Frame caption="Connect a micro USB cable to the short USB port on the short side of the board (red). Make sure the power switch is toggled on.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF7002-connect-to-pc.jpg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=ca39afd04b87b4f76d15bac77de66bed" width="1333" height="1000" data-path=".assets/images/nordic/nRF7002-connect-to-pc.jpg" />
</Frame>

#### 3. Update the firmware

The development board does not come with the right firmware yet. To update the Firmware + Networking Component:

<Info>
  **Firmware + Networking Component** This firmware contains both the application and the networking core firmware component.
</Info>

1. The development board is mounted as a USB mass-storage device (like a USB flash drive), with the name `JLINK`. Make sure you can see this drive.
2. [Download the latest Edge Impulse firmware](https://cdn.edgeimpulse.com/firmware/nrf7002-dk.zip).
3. Install and open the [nRF Connect for Desktop](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-Desktop) and go to the Programmer application
4. Drag and drop the `nrf7002-dk-full.hex` firmware from the downloaded zip in this Programmer application (this firmware contains both application and networking core firmware).
5. Click “Erase & Write” and wait for device to boot up.

#### 4. Connecting to Edge Impulse Studio

From a command prompt or terminal, run:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

The nRF5340 DK exposes multiple UARTs. If prompted, choose the bottom one:

```
? Which device do you want to connect to? (Use arrow keys)
  /dev/tty.usbmodem0010507661753 (SEGGER)
❯ /dev/tty.usbmodem0010507661751 (SEGGER)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 5. Setting up WiFI connection

Once the nRF7002 DK is connected to a project in your profile, it will prompt to setup a WiFi connection:

```
? To which project do you want to connect this device? USERNAME / Project-1
  Setting device ID... OK
  Setting upload host in device... OK
  Configuring remote management settings... OK
  Configuring API key in device... OK
  Configuring HMAC key in device... OK
? WiFi is not connected, do you want to set up a WiFi network now? (Y/n)
```

Select 'Yes' at this step to connect your device to your local WiFi network. After selecting 'Yes', the daemon will scan for WiFi networks in the vicinity and print out a list for you to choose:

```
? WiFi is not connected, do you want to set up a WiFi network now? Yes
Scanning WiFi networks... OK
? Select WiFi network (Use arrow keys)
❯ SSID: Vodafone-174C, Security: WPA2-PSK (1),RSSI: -52 dBm
  SSID: Vodafone-7047, Security: WPA2-PSK (1),RSSI: -67 dBm
  SSID: Vodafone-174C, Security: WPA2-PSK (1),RSSI: -72 dBm
  SSID: FRITZ!Box 7590 SH, Security: WPA2-PSK (1),RSSI: -73 dBm
  SSID: FRITZ!Repeater 1200, Security: WPA2-PSK (1),RSSI: -78 dBm
  SSID: Vodafone-7047, Security: WPA2-PSK (1),RSSI: -85 dBm
```

Navigate to your WiFi network to select it and enter password when prompted. Your kit will then connect to the WiFi and then connect to the project you selected in step 4.

```
[SER] Verifying whether device can connect to remote management API...
[SER] Device is not connected to remote management API, will use daemon
[WS ] Connecting to wss://remote-mgmt.edgeimpulse.com
[WS ] Connected to wss://remote-mgmt.edgeimpulse.com
? What name do you want to give this device? nRF7002-dk

[WS ] Device "nRF7002-dk" is now connected to project "Project-1". To connect to another project, run `edge-impulse-daemon --clean`.
[WS ] Go to https://studio.edgeimpulse.com/studio/252393/acquisition/training to build your machine learning model!
```

#### 6. Verify that the device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/nordic/nRF7002-connect-to-studio-2.jpg?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=0882438c8e3c9be7a4bcaceefdc5d8de" width="1600" height="367" data-path=".assets/images/nordic/nRF7002-connect-to-studio-2.jpg" />
</Frame>

Since your device is now connected via WiFi, you should be able to disconnect the daemon and collect your sensor data over the WiFi connection.

#### 7. Flashing your model

When using the nRF7002 DK, you will not be able to connect to the **Nordic nRF Edge Impulse** app on your phone. The best way to flash your model is by navigating to the **Deployment** tab of your project in the studio on your PC and downloading the built firmware from there. You can follow the instructions in [this section](https://docs.nordicsemi.com/bundle/ncs-2.6.3/page/nrf/device_guides/working_with_nrf/nrf70/gs.html#programming_the_sample) of the Nordic docs to flash the model onto your device.

#### 8. Inferencing

The default firmware for the nRF7002 DK provided above, ships with a default motion detection model. This model is created from the [Tutorial: Continuous motion recognition](/tutorials/end-to-end/motion-recognition) and it's [corresponding Edge Impulse project](https://studio.edgeimpulse.com/public/14299/latest). To see the inferencing results of this model, reconnect the the device to your computer with a USB cable and run:

```
edge-impulse-run-inference
```

This will then display the inference results, in this case classify the motion of the nRF7002 DK board, in the terminal:

```
Inferencing settings:
	Interval: 16.0000ms.
	Frame size: 375
	Sample length: 2000.00 ms.
	No. of classes: 4
Starting inferencing in 2 seconds...
Predictions (DSP: 25 ms., Classification: 0 ms., Anomaly: 0 ms.):
    idle: 	0.996094
    snake: 	0.000000
    updown: 	0.000000
    wave: 	0.000000
    anomaly score: -0.375301
```

Note: In order to receive and view these inference results, you will need to have the X-NUCLEO-IKS02A1 shield connected to the DK since there are no sensors on the DK board itself.

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with this tutorial:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Troubleshooting

#### Failed to flash

If your board fails to flash new firmware (a `FAIL.txt` file might appear on the `JLINK` drive) you can also flash using `nrfjprog`.

1. Install the [nRF Command Line Tools](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).
2. Flash new firmware via:

```
nrfjprog --program path-to-your.bin -f NRF53 --sectoranduicrerase
```


Built with [Mintlify](https://mintlify.com).