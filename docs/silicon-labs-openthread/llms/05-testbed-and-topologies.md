# Source: https://docs.silabs.com/openthread/3.0.0/multi-pan-rcp-performance-for-openthread-and-zigbee/05-testbed-and-topologies.md

# Testbed and Topologies

The Multiprotocol RCP DuT uses Silicon Labs’ wireless starter kit (WSTK) debug adapter and a Raspberry Pi as the host.

It is important to use a sufficiently fast serial link between the RCP and the host to handle the 250 kbps over-the-air bitrate of 802.15.4 radios. For a UART interface, Silicon Labs recommends a baud rate of 921kpbs with hardware flow control enabled, which is what is used for this testing. With a slower baud rate or without flow control, data may be lost over the serial link.

The test topology used for this document is the open wireless network in the Silicon Labs Boston office. This office space is approximately 20,000 square feet with hundreds of test devices uniformly distributed.

The 18-node tests in this document use the three clusters shown below (E5, E8, E9). The red ‘X’ identifies the location of the DuT.The 96 node tests use clusters E2-E23, excluding cluster E4, E12, E15, E16, E19, and E21.

![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image2.png)