# Source: https://docs.edgeimpulse.com/hardware/boards/seeed-xiao-esp32s3-sense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Seeed XIAO ESP32 S3 Sense

<Info>
  **Community board**

  This is a community board by Seeed Studios, and it's not maintained by Edge Impulse. For support head to the [Seeed Forum](https://forum.seeedstudio.com).
</Info>

The Seeed Studio XIAO ESP32S3 Sense is a powerful development board that utilizes the dual-core ESP32S3 chip, featuring an Xtensa processor running at speeds of up to 240 MHz. This board offers support for both 2.4GHz Wi-Fi and Bluetooth Low Energy (BLE) connectivity. Additionally, it is equipped with a detachable OV2640 camera sensor, boasting an impressive resolution of 1600\*1200, and a digital microphone.

<Frame caption="Seeed Studio XIAO ESP32S3 Sense">
  <img src="https://mintcdn.com/edgeimpulse/Y4Lfo5IVCYFA4G8k/.assets/images/xiao_esp32s3_sense.png?fit=max&auto=format&n=Y4Lfo5IVCYFA4G8k&q=85&s=8aa94c3e1b69a8d6b2fd88a83a299c17" width="1333" height="1000" data-path=".assets/images/xiao_esp32s3_sense.png" />
</Frame>

With 8MB of PSRAM and 8MB of FLASH, as well as an external SD card slot, the XIAO ESP32S3 Sense provides ample memory and storage capacity, making it well-suited for embedded machine learning (ML) applications.

Seeed Studio has integrated support for this development board into Edge Impulse, allowing users to sample raw data and build machine learning models directly from the studio. This integration simplifies the process of leveraging the XIAO ESP32S3 Sense for ML projects.

With its impressive specifications and Edge Impulse compatibility, the XIAO ESP32S3 Sense is an excellent choice for developers seeking to explore embedded machine learning applications.

### Connecting to Edge Impulse

To set up your Seeed XIAO ESP32S3 Sense, follow this guide: [Seeed XIAO XIAO ESP32S3 Sense](https://wiki.seeedstudio.com/xiao_esp32s3_keyword_spotting#getting-started)

### Next steps: building a machine learning model

With everything set up you can now build your first machine learning model: [XIAO ESP32S3 Sense & Edge Impulse Keywords Spotting - Seeed Wiki](https://wiki.seeedstudio.com/xiao_esp32s3_keyword_spotting).

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.

### Deploying back to device

With the impulse designed, trained and verified you can deploy this model back to your XIAO ESP32S3 Sense. This makes the model run without an internet connection, minimizes latency, and runs with minimum power consumption. Edge Impulse can package up the complete impulse - including the signal processing code, neural network weights, and classification code - up in a single library that you can run on your development board.

The easiest way to deploy your impulse to the XIAO ESP32S3 Sense is via an Arduino library. See [Run on Arduino](/hardware/deployments/run-arduino-2-0) for more information.


Built with [Mintlify](https://mintlify.com).