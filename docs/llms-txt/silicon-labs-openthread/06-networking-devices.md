# Source: https://docs.silabs.com/openthread/3.0.0/wireless-networking-application-development-fundamentals/06-networking-devices.md

# Networking Devices

Silicon Labs has developed networking hardware (the EFR32xG family) and SDKs containing protocol libraries, application examples, and development tools  to facilitate implementation of a wireless personal area network of devices for sensing and control applications. The following figure represents a typical wireless device using Zigbee, one of the Silicon Labs networking technologies. The RF data modem is the hardware responsible for sending and receiving data on the network. The microcontroller represents the computer control element that originates messages and responds to any information received. The sensor block can be any kind of sensor or control device. Such a system can exist as a node on a network without any additional equipment. Any two such nodes, with compatible software, can form a network. Large networks can contain thousands of such nodes.

![Typical Zigbee Device Block Diagram](/wireless-networking-application-development-fundamentals/0.2/images/typical-zigbee-device-block-diagram.png)

Chips such as the EFR32xG family provide both the RF and microcontroller portions of the figure above. When used as "network coprocessors," the chips provide only the RF and networking part of the system, acting as a co-processor to any microcontroller, Digital Signal Processing (DSP), or similar device required for the application.

For details of the various networking technologies, see the specific Fundamentals document(s) for that technology.