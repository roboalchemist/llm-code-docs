# Source: https://docs.silabs.com/openthread/3.0.0/concurrent-mp-soc/03-concurrent-multiprotocol-cmp-sample-application-matter-zigbee-light.md

# Concurrent Multiprotocol (CMP) Sample Application Matter Zigbee Lighting Example

This sample app demonstrates the usage of the Matter Stack over Thread, alongside the Silicon Labs Zigbee stack. As such, the lighting device represented by select EFR parts are able to receives On/Off commands from both a Zigbee Switch ([Z3 Switch](https://www.silabs.com/support/training/Zigbee-application-layer-concepts/building-a-Zigbee-3-0-switch-and-light-from-scratch) sample app) and a Matter Controller (Google, Apple, Chip-tool) as represented in the diagram below.

![image info](/concurrent-mp-soc/0.1/images/sld678-image28.png)

## Building

### Prerequisites

The following prerequisites need to be installed on the host machine:

- ARM GCC 12.2
- ZAP (version 2024.05.07 or greatest)
- SLC-CLI
- Various environment variables set like:  
  - ARM_GCC_DIR  
  - TOOLDIR  
  - STUDIO_ADAPTER_PACK_PATH

### Build Variants

As of now, this sample app supports two different build variants:

- Sequential Zigbee & Matter
- Concurrent Zigbee & Matter

#### Sequential Zigbee and Matter

In this scenario, the node will initially act as a Zigbee device with the full set of working Zigbee features. Once the device is commissioned onto a Matter fabric, the device will switch into being a full Matter Node on the network.

#### Concurrent Zigbee and Matter

In this scenario, the node will act as both a Zigbee device and a Matter device capable of receiving commands from both protocols at the same time.

## Known Limitations

- CLI and Log outputs are defaulted to the uart interface. Instead of having logs on RTTViewer and CLI/ Matter shell on the UART, everything is forwarded to the uart to prevent weird routing of log messages and uart commands. Issue is present with SISDK 2024.6.0.
- Single Channel listening: In concurrent mode, with SISDK 2024.6.0, the radio mux only supports a single channel for listening. This means that when the device is commissioned on the Matter network, both Zigbee and OpenThread need to operate on the same channel. Since the OTBR can be a fully closed product like a Google Nest Hub, an Apple TV, or an Amazon Echo, there is no control over which channel is going to be selected. This makes channel steering features, like Touchlink, incompatible with this sample app because of this limitation in concurrent mode.

> **Note**: As of SiSDK 2024.12.0 for MG26 parts and SiSDK 2025.6.1 for SiMG301 parts, support for Fast Channel Switching is available. This allows that both Zigbee and OpenThread can operate on different channels.

## Expected Behavior

Once the application is build and flashed onto the device, you should see the Matter QR code displayed and if you're using a BLE sniffer like the EFRConnect app you should be able to see the Silabs-Light being advertised and ready to be commissioned into a Matter network.

### Sequential Zigbee and Matter Behavior

With this build variant, your device will act as a Zigbee device as long as no Matter fabric is present on the device. Once the device is successfully commissioned with Matter, the Zigbee network will be shut down until the next factory reset.

Features like Touchlink will work with this build variant since there is no need to listen on multiple channels at once.

### Concurrent Zigbee and Matter Behavior

With this build variant, the light can be controlled simultaneously from the Matter side or the Zigbee side. For the best user experience, it is advised to commission the Matter side **first** as the OTBR will trigger a channel switch on the Zigbee side. Should Zigbee be commissioned first, then upon completion of the Matter commissioning process, a network leave followed by a network start will be issued to the Zigbee stack in order to achieve a successful channel switch without missing any packets from the Matter side. As such, all previously paired devices on the Zigbee side will have to be re-paired with the device. Again, this is a limitation present in SiSDK 2024.6.0.

## Building Command

You can build this application from going to the Matter Extension repo by running the following commands:

```c
./slc/build.sh slc/sample-app/zigbee-matter-light/efr32/zigbee-matter-light.slcp brd4116a,matter_zigbee_sequential\;matter

./slc/build.sh slc/sample-app/zigbee-matter-light/efr32/zigbee-matter-light.slcp brd4187c,matter_zigbee_concurrent\;matter
```

Building it without any extra component will default to the concurrent version:

```c
./slc/build.sh slc/sample-app/zigbee-matter-light/efr32/zigbee-matter-light.slcp brd4187c
```

If you are building through Simplicity Studio, you need to install the latest SiSDK along with including the Matter Extension. You can then select a supported radio part (ie. MG24, MG26, SiMG301) and select the Zigbee Matter Light Application. You can then generate the project and build the application.

## Customizing

This sample app can be customized to fit most of your needs.

### Matter

Just like any other Matter sample app, you can add and remove the Matter extension components that you need.

### Zigbee

Just like any other Zigbee sample app, you can add and remove the Matter extension components that you need. However, if you want to support install code, you need to actually modify the configuration file present within this project to set `SL_MATTER_CMP_SECURE_ZIGBEE` to 1. This will disable TouchLink and use the provided install code and EUI64 present in the same configuration file (`sl_cmp_config.h`).

## DataModel

Since the Matter and Zigbee data models are quite similar, this project only needs one single zap file for both protocols. For the best user experience, the endpoint configuration should match as closely as possible on the two protocols (except for endpoint 0 which is protocol specific).
