# Source: https://docs.edgeimpulse.com/hardware/boards/avenet-rz-v2l.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AVNET RZBoard V2L

The [AVNET RZBoard V2L](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rzboard-v2l/) is a power efficient, vision-AI accelerated development board in popular single board computer format with well supported expansion interfaces. This Renesas RZ/V2L processor-based platform is ideal for development of cost-efficient Vision-AI and a range of energy-efficient Edge AI applications. It’s RZ/V2L processor has two 1.2GHz Arm® Cortex®-A55 cores plus a 200MHz Cortex-M33 core, a MALI 3D GPU and Image Scaling Unit. This processor SoC further differentiates itself with an on-chip DRP-AI accelerator plus H.264 video (1920 x 1080) encode/decode function in silicon, making it ideal for implementing cost-effective embedded-vision applications.

RZBoard V2L is engineered in a compact Raspberry Pi form-factor with a versatile set of expansion interfaces, including Gigabit Ethernet, 801.11ac Wi-Fi and Bluetooth 5, two USB 2.0 host and a USB 2.0 OTG interface, MIPI DSI and CSI camera interfaces, CANFD interface, Pi-HAT compatible 40-pin expansion header and Click Shuttle expansion header.

The board supports analog audio applications via it’s audio codec and stereo headphone jack. It also pins-out five 12bit ADC inputs for interfacing with analog sensors. 5V input power is sourced via a USB-C connector and managed via a single-chip Renesas RAA215300 PMIC device.

Onboard memory includes 2GB DDR4, 32GB eMMC and 16MB QSPI flash memory, plus microSD slot for removable media.

Software enablement includes CIP Kernel based Linux BSP (maintained for 10 years+) plus reference designs that highlight efficient vision AI implementations using the DRP-AI core. Onboard 10-pin JTAG/SWD mini-header and 4-pin UART header enable the use of an external debugger and USB-serial cable.

Available accessory options include a MIPI 7-inch display, MIPI CSI camera and 5V/3A USB Type C power supply.

<Frame caption="AVNET RZBoard V2L">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-v2l-top.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=2421442fbe38f25cf9f6192abda4f0b6" width="762" height="432" data-path=".assets/images/rz-v2l-top.png" />
</Frame>

### Connecting to Edge Impulse

Please visit AVNET's RZBoard [website for detailed documentation about the RZBoard](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rzboard-v2l/). For succinct documentation to create a board image please visit [Build an RzBoard Yocto Image integrated with FreeRTOS](https://www.hackster.io/bernard-ngabonziza/build-an-rzboard-yocto-image-integrated-with-freertos-085ceb).


Built with [Mintlify](https://mintlify.com).