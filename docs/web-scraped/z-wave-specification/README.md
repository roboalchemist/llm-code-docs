# Z-Wave Protocol Specification

**Official Source**: Z-Wave Alliance 2025-B Specification Package
**Last Updated**: 2026-03-07
**Format**: Full markdown extraction from official PDFs via PyMuPDF

## Overview

This directory contains the complete Z-Wave protocol specification from the Z-Wave Alliance,
extracted from the official 2025-B Specification Package (12 PDFs, 2,375 pages total).

## Documentation Files

### Core Specifications

1. **[Z-Wave Application Specification](./z-wave-application-specification.md)** (4.3MB, 1311 pages)
   - 100+ command class definitions with byte-level frame formats
   - Device types, roles, and lifeline associations
   - Security S0/S2 command encapsulation
   - Requirement IDs (CC:xxxx.xx.xx.xx.xxx format)

2. **[Z-Wave Network Layer Specification](./z-wave-network-specification.md)** (256KB, 174 pages)
   - AODV-based mesh routing protocol
   - Node addressing and identification (8-bit, 1-232)
   - Route request/reply mechanisms
   - Network inclusion/exclusion

3. **[Z-Wave Host API Specification](./z-wave-host-api-specification.md)** (388KB, 320 pages)
   - Serial API protocol between host and Z-Wave module
   - Command/Response frame formats
   - Function IDs and callbacks

4. **[Z-Wave PHY and MAC Layer Specification](./z-wave-phy-mac-specification.md)** (52KB)
   - GFSK modulation (9.6, 40, 100 kbps)
   - CSMA/CA channel access
   - Frame structure and CRC

5. **[Z-Wave Long Range PHY and MAC Specification](./z-wave-lr-phy-mac-specification.md)** (140KB, 80 pages)
   - Long Range variant (up to 100m outdoor)
   - Extended addressing and frame formats

6. **[Frequency Region Allocation](./z-wave-frequency-specification.md)** (8KB, 10 pages)
   - Regional frequency bands (EU 868 MHz, US 908 MHz, CN 920 MHz, JP 922 MHz)
   - Channel specifications and regulatory compliance

7. **[Errata and Updates](./z-wave-errata-specification.md)** (12KB, 12 pages)
   - Known issues and ITU specification corrections

### Test Specifications

8. **[Z-Wave PHY Layer Test Specification](./z-wave-phy-test-specification.md)** (56KB, 43 pages)
9. **[Z-Wave MAC Layer Test Specification](./z-wave-mac-test-specification.md)** (216KB, 122 pages)
10. **[Z-Wave Network Layer Test Specification](./z-wave-network-test-specification.md)** (304KB, 151 pages)
11. **[Z-Wave LR PHY Layer Test Specification](./z-wave-lr-phy-test-specification.md)** (60KB, 42 pages)
12. **[Z-Wave LR MAC Layer Test Specification](./z-wave-lr-mac-test-specification.md)** (108KB, 66 pages)
13. **[Z-Wave LR Network Layer Test Specification](./z-wave-lr-network-test-specification.md)** (76KB, 44 pages)

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

Z-Wave communication is organized around **command classes** with versioned specifications.
Each command class defines frame formats at the byte level with requirement IDs.

Examples: Basic, Binary Switch (v1-v2), Multilevel Switch (v1-v4), Door Lock,
Thermostat, Sensor Multilevel, Meter, Notification, Security S2, and 100+ more.

### Security

- **S0 (Legacy)**: AES-128 CCM (deprecated)
- **S2**: AES-CCMP with ECDH key agreement (current standard)

## License

Z-Wave specifications are copyright Z-Wave Alliance, Inc.
Extracted for reference purposes from the publicly available 2025-B Specification Package.

**Source**: Z-Wave Alliance 2025-B Specification Package
