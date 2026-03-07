# Z-Wave Protocol Specification

**Official Source**: Z-Wave Alliance 2025-B Specification Package
**Last Updated**: 2026-03-07T20:11:54.479214
**Format**: Markdown (extracted from official PDFs)

## Overview

This directory contains the official Z-Wave protocol specification from the Z-Wave Alliance.
Z-Wave is a wireless mesh networking protocol designed for reliable home automation and IoT applications.

### Coverage

- **PHY/MAC Layers**: Physical and Medium Access Control layer specifications
- **Network Layer**: Routing, addressing, and network management
- **Application Layer**: Command classes, device types, and application protocols
- **Host API**: Serial communication protocol between hosts and Z-Wave controllers
- **Regional**: Frequency allocations and regional variations

## Documentation Files

### Core Specifications

1. **[Z-Wave Application Specification](./z-wave-application-specification.md)**
   - Command classes (100+ command class definitions)
   - Device types and roles
   - Application layer protocols
   - Security (S0, S2)

2. **[Z-Wave Network Layer Specification](./z-wave-network-layer.md)**
   - Routing protocols (AODV-based routing)
   - Network topology
   - Node addressing and identification
   - Network security

3. **[Z-Wave Host API Specification](./z-wave-host-api.md)**
   - Serial API protocol
   - Command/Response frames
   - Data link layer
   - Host-to-controller communication

4. **[Z-Wave PHY and MAC Layer Specification](./z-wave-phy-mac.md)**
   - Modulation (GFSK at 9.6-40 kbps)
   - Channel access (CSMA/CA)
   - Frame structure
   - Long Range variant (up to 100m outdoor)

5. **[Frequency Region Allocation](./z-wave-frequency.md)**
   - Regional frequency bands (EU, US, RU, IN, IL, CN, JP, etc.)
   - Channel specifications
   - Regulatory compliance

6. **[Errata and Updates](./z-wave-errata.md)**
   - Known issues and corrections
   - ITU specification updates

## Key Concepts

### Protocol Stack

```text
Application Layer      (Command Classes, Security, Validation)
     ↓
Framework/Transport    (Reliable Delivery, Sequencing)
     ↓
Network Layer         (Routing, Node Addressing, Mesh)
     ↓
Data Link             (Serial API, Host Communication)
     ↓
PHY/MAC Layer         (GFSK Modulation, Channel Access)
     ↓
Radio Hardware        (Transceiver)
```

### Command Classes

Z-Wave communication is organized around **command classes** that define specific functionality:

- **Basic**: Basic on/off control
- **Multilevel Switch**: Dimming and percentage control
- **Door Lock**: Secure locking mechanisms
- **Thermostat**: Temperature control
- **Sensor**: Environmental sensing
- **Meter**: Energy/water/gas metering
- **Notification**: Event reporting
- **Security**: S0 and S2 encryption
- And 100+ more...

### Routing

Z-Wave uses a mesh networking approach:

- Each node can relay messages (with hop count limiting)
- AODV-like routing protocol
- Route request/reply mechanism
- Network stability and convergence

### Security

Two security levels:

- **S0 (S0-Legacy)**: AES-128 CCM (128-bit, deprecated)
- **S2**: AES-CCMP with ECDH key agreement (modern, 256-bit equivalent)

## Technical Details

### Frequency Bands

- **Europe (EU)**: 868.0 - 868.6 MHz
- **North America (US)**: 908.4 - 916.0 MHz
- **Russia (RU)**: 869.0 - 869.2 MHz
- **China (CN)**: 920.0 - 921.7 MHz
- **Japan (JP)**: 922.5 - 923.5 MHz

### Data Rates

- **Standard Z-Wave**: 9.6, 19.2, 40 kbps (GFSK modulation)
- **Z-Wave Long Range**: Up to 100m outdoor range (lower data rate)

### Network Size

- **Maximum nodes**: 232 (devices) + 1 controller = 233
- **Addressing**: 8-bit node IDs (1-232 for devices)
- **Range**: 30m typical indoor, 100m+ with Long Range

## Related Standards

- **ITU-T G.9959**: Underlying PHY/MAC specification (published by ITU)
- **IEEE 802.15.4**: Inspiration for MAC layer design
- **Zigbee**: Competing mesh standard

## Resources

- **Official Site**: https://z-wavealliance.org
- **Developers**: https://developers.z-wavealliance.org
- **Members Portal**: https://sdomembers.z-wavealliance.org
- **SDK**: Available for members

## License

Z-Wave specifications are copyright Z-Wave Alliance. This documentation is extracted for
reference purposes. For official specifications, visit the Z-Wave Alliance website.

## Usage Notes

This documentation was automatically extracted from official Z-Wave Alliance specification PDFs.
For the most authoritative information, consult the official specification documents through
the Z-Wave Alliance Members Portal.

**Generated**: 2026-03-07T20:11:54.479214
**Source**: Z-Wave Alliance 2025-B Specification Package
