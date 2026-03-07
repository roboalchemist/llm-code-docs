# Source: https://docs.silabs.com/openthread/3.0.0/mesh-network-performance-comparison/02-comparison-of-results.md

# Comparison of Results

## Throughput and Latency

Throughput and latency is tested in a controlled network (wired configuration) to test each hop against different packet payloads.

The normal configuration is to test to 6 hops. Testing is done with 1 source node and a series of routing nodes to allow the number of hops to be varied.

![Throughput and Latency Test Configuration](/mesh-network-performance-comparison/0.1/images/sld785-throughput-and-latency-test-configuration.png)

### Mesh Multi-Hop Throughput

Throughput testing uses the same single setup to evaluate the expected application level throughput of different payload sizes across a different number of hops.

For smaller payload sizes, the throughput is lower as the network spends more time sending packet overhead versus application data.

![Small Packet Throughput 8-byte BT Seg and UnSeg and 10-byte Thread](/mesh-network-performance-comparison/0.1/images/sld785-small-packet-throughput-8-byte-bt-seg-and-unseg-and-10-byte-thread.png)

For larger payload sizes, the throughput is increased overall for Zigbee and Thread; however, the smaller payload size of Bluetooth Mesh does not result in the same increase in throughput. Note that all three technologies are fragmenting packets at this size.

![Throughput Comparison vs Hops 100-byte Payload Zigbee, Thread, and 96-byte Bluetooth](/mesh-network-performance-comparison/0.1/images/sld785-throughput-comparison-vs-hops-100-byte-payload-zigbee-thread-and-96-byte-bluetooth.png)

If we measure latency instead of throughput, we look at the small payloads first and see similar latency numbers between the different technologies. Adding segmentation to Bluetooth increases the latency but everything stays below 200 milliseconds in round trip time.

![Small Payload - Latency vs Hops](/mesh-network-performance-comparison/0.1/images/sld785-small-payload-latency-vs-hops.png)

If we look at a 4-hop chart versus a different payload size, we can see the increase in latency versus payload for the different technologies. All different mesh networks increase latency as the application payload increases. How well the network does under these conditions is related to the underlying fragmentation method as well as the congestion in the network when sending the data. Bluetooth must send many more packets as the payload size increases, so this segmentation adds more latency.

![Zigbee, Thread, and Bluetooth Latency - 4-hop versus Payload Size](/mesh-network-performance-comparison/0.1/images/sld785-zigbee-thread-and-bluetooth-latency-4-hop-versus-payload-size.png)

## Multicast Network Tests versus Network Size

The throughput and latency results shown in [Mesh Multi-Hop Throughput](02-comparison-of-results#mesh-multi-hop-throughput) are somewhat constrained by the nature of the testing since it is a single string of devices. Open-air testing is required to validate stack performance under less controlled conditions. These networks are configured within Silicon Labs office space with normal Wi-Fi interference, other network operations, and building control systems. No attempt is made to isolate this network’s RF conditions.

Because this testing is all multicast delivery, the Bluetooth flooding mesh is behaving the same as Zigbee and Thread because all-device multicasts generally flood the network with three re-broadcasts from each router. These tests are all for relatively lightly loaded networks where the multicast is sent every 3 seconds. In our individual testing, we noted that some network performances deteriorate further as this multicast load is increased.

The networks to be tested for each stack include:

- Small network: 24 devices
- Medium network: 1 – 48 devices
- Medium network: 2 – 96 devices
- Large network: 1 – 144 devices
- Large network: 2 – 192 devices

For any of these tests, any number of devices within +/- 10% of these network targets is acceptable. These networks are all configured as powered devices. For each of these networks, the testing will validate reliability and latency for a set of traffic conditions. Testing is intended for over 100 packets.

### Small Networks and Different Packet Sizes

For each of these networks, we want to start testing with a small network and small payload sizes as the simplest comparison point. As shown below, all three mesh networks provide very good performance with latency well under 200 milliseconds.

![Zigbee, Thread, and Bluetooth Multicast Latency 24 Node Network - 5 (or 8 Bluetooth) -byte Payload](/mesh-network-performance-comparison/0.1/images/sld785-24-node-network-5-or-8-bluetooth-byte-payload.png)

As the packet size increases, we start to see some differences in the multicast latency where it increases and spreads out. Thread latency increases slightly, Zigbee increases and spreads out, and Bluetooth Mesh becomes very distributed in latencies from 20 millseconds up to 220 milliseconds.

![Zigbee, Thread, and Bluetooth Multicast Latency 24 Node Network - 50 (or 32 Bluetooth) -byte Payload](/mesh-network-performance-comparison/0.1/images/sld785-24-node-network-50-or-32-bluetooth-byte-payload.png)

### Large Networks and Different Packet Sizes

As the network scales up, we expect an increase in latency due to added congestion and increased number of hops in the network. Since this is an open-air network, we do not control the number of hops a particular message takes, we only record the actual results. The chart below shows that for small packet sizes, all three networks behave reasonably with an increase and spreading of the latency to slightly longer latencies. The only point of note is the ~3% of Bluetooth packets that end up with latency larger than 250 milliseconds.

![Zigbee, Thread, and Bluetooth Multicast Latency 192 Node Network - 5 (or 8 Bluetooth) -byte Payload](/mesh-network-performance-comparison/0.1/images/sld785-192-node-network-5-or-8-bluetooth-byte-payload.png)

As the packet payload increases, we expect to see further increases in latencies across each of the mesh networks, particularly in the larger networks where fragmentation of packets will result in even more congestion due to the multicast flooding. We increase the payload only slightly and see the latencies spread substantially. In the graph below, we have increased the X axis to better show the latency spreading in this larger network. All the networks spread out, but the Bluetooth network spreads well past 500 milliseconds. Further increases in packet size only make this spreading worse.

![Zigbee, Thread, and Bluetooth Multicast Latency 192 Node Network - 25 (or 16 Bluetooth) -byte Payload](/mesh-network-performance-comparison/0.1/images/sld785-192-node-network-25-or-16-bluetooth-byte-payload.png)
