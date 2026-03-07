# Bluetooth Generic Attribute Profile (GATT) Specification

**Source:** Bluetooth Core Specification Version 5.4 - Part G
**Official URL:** https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## Overview

This directory contains the complete Generic Attribute Profile (GATT) specification from the official Bluetooth Core Specification v5.4. GATT is a critical component of Bluetooth Low Energy (BLE) that defines the service framework and procedures for discovering services, reading/writing characteristics, and managing device attributes.

## Document Structure

### Core Sections

1. **[Introduction](01-introduction.md)** - Scope, dependencies, and conventions
2. **[Profile Overview](02-profile-overview.md)** - Protocol stack, roles, fundamentals, and GATT hierarchy
3. **[Service Interoperability Requirements](03-service-interoperability.md)** - Service, include, and characteristic definitions
4. **[GATT Feature Requirements](04-gatt-features.md)** - Detailed feature specifications and procedures
5. **[L2CAP Interoperability Requirements](05-l2cap-interoperability.md)** - Logical Link Control and Adaptation Protocol requirements
6. **[GAP Interoperability Requirements](06-gap-interoperability.md)** - Generic Access Profile requirements
7. **[Defined GATT Services](07-gatt-services.md)** - Standard GATT service definitions
8. **[Security Considerations](08-security.md)** - Security requirements and best practices
9. **[SDP Interoperability Requirements](09-sdp-interoperability.md)** - Service Discovery Protocol integration

### Appendices

- **[Appendix A: Example ATT Server Contents](appendix-a-example-att-server.md)** - Database structure examples
- **[Appendix B: Example Database Hash](appendix-b-database-hash.md)** - Hash computation examples

## Key Concepts

### GATT Roles

- **Client** - Initiates commands and requests; receives responses, indications, and notifications
- **Server** - Accepts incoming commands; sends responses, indications, and notifications

### Core Elements

- **Services** - Collections of characteristics that accomplish a specific function
- **Characteristics** - Data values with properties defining how they can be accessed
- **Attributes** - Individual data elements stored in the server's database
- **Descriptors** - Metadata about characteristics (e.g., CCCD, presentation format)

### Attribute Protocol (ATT)

GATT operates over the Attribute Protocol, which provides:

- Attribute discovery
- Attribute reading and writing
- Notification and indication mechanisms
- Attribute caching strategies

## Use Cases

GATT is fundamental to:

- Wearable devices (fitness trackers, smartwatches)
- Health monitoring devices (heart rate monitors, scales)
- Home automation (smart lights, thermostats)
- IoT sensors and actuators
- Mobile device integration with accessories

## Terminology

Key terms used throughout the specification:

- **UUID** - Universally Unique Identifier for services and characteristics
- **Handle** - Index into the attribute database
- **CCCD** - Client Characteristic Configuration Descriptor
- **ATT** - Attribute Protocol (underlying transport mechanism)
- **MTU** - Maximum Transmission Unit

## Implementation Notes

When implementing GATT:

1. All mandatory capabilities must be supported
2. Attribute caching strategies should implement Robust Caching
3. UUIDs can be either 16-bit or 128-bit identifiers
4. Services can be primary or secondary
5. Characteristics support various access modes (read, write, notify, indicate)
6. Security considerations should be reviewed carefully

## Standards References

This specification is part of the complete Bluetooth Core Specification architecture:

- Volume 0: Overview
- Volume 1: Architecture and conventions
- Volume 2: BR/EDR Controller
- **Volume 3: Host (includes this GATT specification)**
- Volume 4: HCI Interface
- Volume 5: RF PHY
- Volume 6: Low Energy Controller
- Volume 7: Mesh

## Related Specifications

- **GAP (Generic Access Profile)** - Device discovery, connection, and advertising
- **ATT (Attribute Protocol)** - Low-level attribute access mechanism
- **L2CAP** - Logical Link Control and Adaptation Protocol
- **SDP** - Service Discovery Protocol

## Legal Notice

This documentation is extracted from the official Bluetooth Core Specification maintained by the Bluetooth Special Interest Group (SIG). For official and updated versions, visit https://www.bluetooth.com/specifications/

---

**Last Updated:** Bluetooth Core Specification Version 5.4
**Format:** Markdown (converted from official HTML specification)
**Purpose:** Reference documentation for GATT implementation and integration
