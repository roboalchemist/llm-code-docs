# Source: https://docs.silabs.com/openthread/3.0.0/multi-pan-rcp-performance-for-openthread-and-zigbee/06-test-results-summary.md

# Test Results Summary

The following results are from a 9x9 topology, meaning 9 OT nodes and 9 ZigBee nodes sending traffic to the DuT. The DuT uses a UART baud rate of 921kbps with hardware flow control.

The rate column is the number of milliseconds between transmits, and the JIT column is the offset between successive senders in milliseconds. The Min/Avg/Max columns give the latency in milliseconds.

Four packet sizes are tested, S, M, L, and XL. The size of the payload is indicated in the SIZE column. S corresponds to 8 byte payloads for both protocols. M corresponds to maximal payload sizes without causing fragmentation, 78 bytes for OT and 82 bytes  for ZigBee.  L corresponds to a 256 byte payload for OT, resulting in fragmentation into 4 packets. XL corresponds to a 1024 byte payload for OT, resulting in fragmentation into 14 packets. For L and XL the ZigBee payload size remains at 82.

The first table shows results for the single channel case, when both the OT and ZigBee networks are on the same channel.  The second table shows results for the dual channel case, when the OT and ZigBee networks are on different channels. This tests the Concurrent Listening feature of the Multiprotocol RCP.

Performance is excellent with no packet loss in all single channel tests, and no significant latency spikes. In the dual channel tests, performance is excellent for S, M, and L packet size. For the XL packet size test, where OT is using 1024 byte payloads, some packet loss and increased latency is observed on the ZigBee side. This is explained by the very high amount of traffic on the OT network, which monopolizes the radio on the OT channel resulting in missed receptions on the ZigBee side.

**Table: 9 OT x 9 Zig Network, Single Channel**

|Size|Results|
|---|---|
|S|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image3.png)|
|M|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image4.png)|
|L|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image5.png)|
|XL|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image6.png)|

**Table: 9 OT x 9 Zig Network, Dual Channel**

|Size|Results|
|---|---|
|S|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image7.png)|
|M|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image8.png)|
|L|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image9.png)|
|XL|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image10.png)|

The following results are from a large network topology of 48 OT devices and 48 Zig devices. All devices send 8 byte payloads to the DuT at a rate of one every five seconds. Performance is excellent for both single and dual channel tests. Reliability is almost perfect and there are only a few latency spikes, which are expected under the traffic stress of 96 devices sending and receiving from 1 device.

**Table: 48 OT x 48 Zig Network, Single Channel**

| |
|---|
|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image11.png)|
|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image12.png)|

**Table: 48 OT x 48 Zig Network, Dual Channel**

| |
|---|
|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image13.png)|
|![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image14.png)|