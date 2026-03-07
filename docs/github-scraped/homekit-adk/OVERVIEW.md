# HomeKit Accessory Development Kit (ADK)

## Overview

The HomeKit Accessory Development Kit (HomeKit ADK) is Apple's official kit for developing HomeKit-compatible accessories.
It contains the complete HomeKit Accessory Protocol (HAP) specification, implementation guide, reference implementation in C,
and comprehensive documentation for building HomeKit accessories.

## What's Included

### Documentation
- **HAP Specification**: Complete protocol definition for HomeKit communication
- **Getting Started Guide**: How to build your first HomeKit accessory
- **Crypto Documentation**: Security protocols (SRP, Ed25519, Curve25519)
- **Visual Debug Guide**: Debugging tips for macOS development

### Reference Implementation
- **HAP Library**: Full C implementation of the HomeKit Accessory Protocol
- **Services & Characteristics**: Predefined HomeKit service and characteristic definitions
- **Examples**: Reference implementations for various accessory types
- **Test Suite**: Validation tools for accessory implementations

### Key Features

- **IP and BLE Transport**: Support for both HTTP/IP and Bluetooth LE
- **Security**: TLS 1.2, SRP authentication, frame encryption
- **Pairing**: HomeKit secure pairing and session establishment
- **Accessories**: Support for all HomeKit accessory categories
- **Services**: Lighting, locks, thermostats, sensors, and more
- **Characteristics**: Standardized device attributes and states

## Directory Structure

- `Documentation/` - Official HAP specification and guides
  - `index.rst` - Main documentation index
  - `getting_started.md` - Getting started guide
  - `crypto.md` - Cryptography details
  - `darwin_visual_debug.md` - macOS debugging guide
  - `coding_convention.md` - Development conventions
- `HAP/` - Header files for the HAP implementation
- `HAP-Headers/` - Reference HAP interface definitions
- `Applications/` - Example applications
- `README.md` - Repository overview
- `LICENSE.md` - Apache 2.0 license

## Common Tasks

### Understanding HAP
Start with the Documentation folder to understand the protocol.

### Implementing an Accessory
Use the reference implementation and examples to guide your development.

### Working with Services & Characteristics
Refer to the service definitions for all available HomeKit types.

### Security & Pairing
Review crypto.md for security protocol details.

## Related Resources

- [HAP-nodejs](../hap-nodejs/) - Node.js implementation of HAP
- [Homebridge](https://github.com/homebridge/homebridge) - HomeKit bridge platform
- [HomeKit Official](https://www.apple.com/homekit/) - Apple's HomeKit ecosystem

## License

Apache License 2.0 - See LICENSE.md
