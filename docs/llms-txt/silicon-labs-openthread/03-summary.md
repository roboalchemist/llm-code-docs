# Source: https://docs.silabs.com/openthread/3.0.0/mesh-network-performance-comparison/03-summary.md

# Summary

Comparing different mesh technologies allows designers to review expected performance under different conditions. To allow as fair a comparison as possible, we ran these tests using the same wireless devices under generally the same open office conditions. We also attempted to minimize other factors impacting the testing such as the backchannel timing from the development kits, latency within the testing infrastructure, and differences in radio architecture or MCU speeds, which can all impact results. Even when controlling these factors, we must caution that these results are our first attempt and further optimizations and improvements are likely possible within the standard or within our implementation. We have been running tests like these with our Zigbee stack since 2006, with Thread since 2015, and on Bluetooth only within the past year.

Each mesh network is designed differently and behaves differently. One network is not expected to be perfect for all conditions, so the selection of a particular technology involves criteria such as battery life, expected ecosystem and preferred connectivity, and the performance requirements of the device and network. This application note only compares the performance of these networks and not some of these other critical parameters.

From a performance standpoint, we see that all relatively small networks with small payload sizes perform similarly. As payload sizes and throughput needs increase, both Thread and Zigbee are better able to carry the load and maintain lower latencies. Latencies increase for all large networks, but Bluetooth experiences the largest increase. If we increase the payload in these larger networks, we see even more substantial increases in latency. This increase is expected; therefore, larger networks should be moved to a routing solution to minimize this latency. In all our multicast testing, however, we should note that our reliability is generally 99.9% or better as the multicast does a good job of ensuring delivery of the messages.

## Related Literature

This application note has provided a comparison of the three mesh network technologies, Bluetooth, Zigbee, and Thread. For specific information on each of these technologies, refer to the following application notes:

- [Bluetooth Mesh Network Performance](https://docs.silabs.com/btmesh/latest/btmesh-11-network-performance/)
- [Zigbee Mesh Network Performance](https://docs.silabs.com/zigbee/latest/zigbee-mesh-network-performance/)
- [AN1408: Thread Mesh Network Performance](https://www.silabs.com/documents/public/application-notes/an1408-openthread-mesh-network-performance.pdf)