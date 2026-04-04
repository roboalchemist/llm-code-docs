# Source: https://docs.silabs.com/openthread/3.0.0/multi-pan-rcp-performance-for-openthread-and-zigbee/03-test-approach-and-dependencies.md

# Test Approach and Dependencies

This test effort uses open wireless devices in the Silicon Labs Boston office. The automation is written in Java™ and leverages a set of utilities for communicating with the test device via TCP. This supports simultaneous command transmission and data collection for many devices via the TCP console ports.

Networks are formed for OpenThread (OT) and Zigbee (Zig) using the wireless SoC devices around the office, plus the Multiprotocol RCP DuT. Traffic is generated from the Zig and OT SoC devices by providing the address of the DuT for each protocol.

Collection is based on console output from OT ping and the Zigbee throughput component. The output is parsed and results are written to .csv files on completion of test runs.