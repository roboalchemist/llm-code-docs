# Source: https://docs.silabs.com/openthread/3.0.0/mesh-network-performance-comparison/01-introduction-and-background.md

# Introduction and Background

Silicon Labs has provided performance testing results from embedded mesh networks as part of developer conferences and industry white papers. The basic performance data of throughput, latency, and impact of security can be used by system designers to define expected behavior. This testing has been previously presented for Zigbee and Thread networks as basic 15.4 mesh networking technologies. These were presented because performance varies even though both systems use the same underlying physical layer defined by IEEE 802.15.4. More recently, we have also published data on Bluetooth Mesh performance using the same test network in our Silicon Labs Research and Development (R&D) facility. The underlying performance details for each of these three mesh technologies are covered in the following individual application notes covering the testing conditions and results:

- [Bluetooth Mesh Network Performance](https://docs.silabs.com/btmesh/latest/btmesh-11-network-performance/)
- [Zigbee Mesh Network Performance](https://docs.silabs.com/zigbee/latest/zigbee-mesh-network-performance/)
- [AN1408: Thread Mesh Network Performance](https://www.silabs.com/documents/public/application-notes/an1408-openthread-mesh-network-performance.pdf)

This paper is intended to present results from the three technologies so they can be evaluated against each other. No single technology is expected to be used for connecting all devices, therefore, this paper provides performance comparisons so networks are used in situations best suited for the technology. Companies developing products can test the network’s performance for the expected use case, and then use this data to assist in selecting the appropriate technology.

This paper does not cover testing conditions and topology as this is covered in each of the individual performance papers. Each mesh network was tested under the same conditions and using the same wireless devices in our Silicon Labs R&D facility.