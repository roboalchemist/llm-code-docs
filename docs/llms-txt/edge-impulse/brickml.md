# Source: https://docs.edgeimpulse.com/hardware/devices/brickml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# BrickML

Industrial device monitoring and predictive maintenance are becoming crucial aspects of industries relying on heavy machinery and equipment. Predictive maintenance, in particular, has emerged as a critical approach to optimizing maintenance strategies and minimizing costly equipment failures. By leveraging IoT sensors and machine learning on the edge, the landscape of predictive maintenance has undergone significant transformation. This shift allows for real-time data collection, analysis, and decision-making at the edge, enabling faster response times and proactive maintenance actions. Unlike traditional predictive maintenance techniques, which often rely on periodic inspections or time-based schedules, this new framework takes advantage of continuous monitoring, anomaly detection, and predictive analytics to anticipate and even prevent equipment failures, resulting in increased operational efficiency, reduced downtime, and significant cost savings.

The market for IoT devices dedicated to predictive maintenance faces a gap of efficient devices that are able to collect multiple streams of sensor data, enable efficient data analysis and incorporate decision-making capabilities all in one. Edge Impulse has partnered with [ReLoc](https://www.reloc.it/) to design our first industrial reference design device - the BrickML. BrickML is small form-factor device powered by a Renesas RA6M5, designed specifically to operate in industrial environments.

<Frame caption="The BrickML">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml/the-brick.jpg?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=7f3eaffdc7472c468938d648735fab83" width="1600" height="868" data-path=".assets/images/brickml/the-brick.jpg" />
</Frame>

The RA6M5 comes equipped with a 32-bit 200MHz Arm Cortex-M33 microcontroller, 2MB flash memory, 8kB data flash to store data as in EEPROM and 512kB SRAM, making it an extremely powerful device for real-time data processing. Complete integration with the Edge Impulse ecosystem enables machine learning based smart decision making at the tips of users' fingers. The BrickML comes encased in a protective enclosure that allows for installation in various industrial conditions with little effort. Loaded with sensors - microphone, inertial, environmental (temperature and humidity) - BrickML makes monitoring of equipment as closely as possible extremely simple. In addition, expanded ADC functionality allows the BrickML to be used in conjunction with a non-invasive current sensor which can be used to carry out motor current signal analyses (MCSA) on various equipment. The BrickML comes pre-loaded with a motion detection model.

The firmware for the BrickML is open source and hosted on GitHub: [edgeimpulse/brickml](https://github.com/edgeimpulse/firmware-brickml)

### Installing dependencies

To start using the BrickML with the Edge Impulse studio, no additional software is required. Simply install the [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation), create a project on the [Edge Impulse Studio](https://studio.edgeimpulse.com/login), and you're ready to go.

<Warning>
  **Problems installing the CLI?**

  See the [Installation and troubleshooting](/tools/clis/edge-impulse-cli/installation) guide.
</Warning>

### Connecting to Edge Impulse

#### 1. Connect your Brick to the daemon

Connect the BrickML to your computer and start the [Edge Impulse daemon](/tools/clis/edge-impulse-cli/serial-daemon) from a command prompt or terminal:

```
edge-impulse-daemon
```

This starts a wizard which asks you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

If prompted to select a device, choose `BRICKML`:

```
? Which device do you want to connect to?
❯ /dev/tty.usbmodem** (BRICKML)
```

Alternatively, recent versions of Google Chrome and Microsoft Edge can collect data directly from your development board, without the need for the Edge Impulse CLI. See [this blog post](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser) for more information.

#### 2. Choose your project

Once logged in, the wizard will ask which project the device should be connected to. From this list, choose the project that you created in step one.

#### 3. Connect to the Studio

After the project is selected, the daemon will update to let you know that the connection is successful. Enter a name for your device at the prompt, and your device is now connected to the studio. The devices tab in your project on the studio will also indicate successful connection of the BrickML with a green indicator. You can now start collecting your data.\\

<Frame caption="BrickML successfully connected">
  <img src="https://mintcdn.com/edgeimpulse/93IfWNUOFrBPiHbi/.assets/images/brickml/brick-connected.png?fit=max&auto=format&n=93IfWNUOFrBPiHbi&q=85&s=1c5ef52432c4162000ca84cb46b00c4c" width="1341" height="376" data-path=".assets/images/brickml/brick-connected.png" />
</Frame>

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Building a continuous motion recognition system](/tutorials/end-to-end/motion-recognition)
* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)

Looking to connect different sensors? The [data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

Predictive maintenance powered by IoT sensors and machine learning on the edge, has become a game-changer, empowering businesses to embrace a more proactive and precise approach to asset management. BrickML is an all-in-one approach to predictive maintenance, empowering organizations with accurate insights and enabling proactive asset management.

### Deploying back to device

#### Build with Docker

> **Note:** Docker build can be done with MacOs, Windows10 & Windows11 and Linux machines with x86\_64 architecture only.

If you are building with Docker, you will need to have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed. You will need to do this is you want to build a wrapper application around your BrickML project while taking advantage of the Edge Impulse provided ingestion and inference libraries.

1. Run the Docker Desktop executable, or start the docker daemon from a terminal as shown below:

```
dockerd
```

2. From the [BrickML firmware directory](https://github.com/edgeimpulse/firmware-brickml) build the docker container

```
docker build -t edge-impulse-brickml .
```

3. Build the firmware as follows and flash your device with your application (as described below)

```
docker run --rm -v $PWD:/app/workspace/firmware-brickml edge-impulse-brickml
```

The default firmware for the BrickML is available [here](https://cdn.edgeimpulse.com/firmware/brickml.zip). To update the firmware or return to the default version with which the BrickML is shipped, use the provided `ei_uploader.py` script as follows:

```
python3 ei_uploader.py -s <serial_port> -f <bin to update>
```

The -f parameter is optional and is assigned to the filename `firmware-brickml.bin.signed` by default.

The data sheet for the BrickML can be found here:

[Download pdf](https://cdn.edgeimpulse.com/documentation/brickml-data-sheet.pdf)

#### Bootloader mode

To enter in bootloader mode, keep the button on the BrickML pressed while powering on the device.


Built with [Mintlify](https://mintlify.com).