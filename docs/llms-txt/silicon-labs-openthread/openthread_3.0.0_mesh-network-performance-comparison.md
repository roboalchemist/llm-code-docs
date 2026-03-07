# Source: https://docs.silabs.com/openthread/3.0.0/mesh-network-performance-comparison/index.md

# Mesh Network Performance Comparison

> **Note: This section replaces _AN1142: Mesh Network Performance Comparison_. Further updates to this application note will be provided here**.

It is important for designers to understand the capabilities and performance characteristics of mesh networking technologies to determine the appropriate one for a given application or product. Networking performance characteristics such as throughput, latency, and the impact of network size on scalability and reliability should be considered. Additional factors such as technologies used in different ecosystems, gateway interfaces, and cloud connectivity should also be factored in when [making a determination](https://www.silabs.com/whitepapers/selecting-the-appropriate-wireless-mesh-network-technology).

This application note reviews the Zigbee, Thread, and Bluetooth mesh networks to evaluate their differences in performance and behavior. Tests were conducted using Silicon Labs’ Wireless Gecko SoC platform capable of running Bluetooth Mesh, Thread, Zigbee, and Proprietary protocols. Silicon Labs Bluetooth Mesh, Thread, and Zigbee software stacks were utilized. The test environment was a commercial office building with active Wi-Fi and Zigbee networks in range. Wireless test clusters were deployed in hallways, meeting rooms, offices, and open areas. These results are intended to provide guidance on design practices and principles as well as expected field performance results.

Additional performance benchmarking information for other technologies is available at [http://www.silabs.com/mesh-performance](https://www.silabs.com/mesh-performance).

## Summary

- Mesh network performance including throughput, latency, and large network scalability is presented.
- Benchmarks performed with Silicon Labs SDKs and Stacks for Bluetooth Mesh, Thread, and Zigbee.

**The information in this application note is based on the SLThread implementation of Thread. SLThread reached ‘end of service’ in December 2019. Silicon Labs is replacing SLThread with an implementation of the more popular OpenThread. We anticipate that the results from OpenThread will be very close to the SLThread results.**