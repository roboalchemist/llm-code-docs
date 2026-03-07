# HAP-nodejs Overview

## What is HAP-nodejs?

HAP-nodejs is the Node.js/TypeScript implementation of the HomeKit Accessory Protocol (HAP).
It allows you to build HomeKit-compatible accessories and integrate them with the Homebridge platform.

## Key Features

- **HomeKit Protocol Implementation**: Full HAP support for IP and Bluetooth LE
- **Service Definitions**: Predefined HomeKit services and characteristics
- **Pairing & Security**: SRP, Ed25519, and Curve25519 cryptography
- **TypeScript Support**: Full type definitions for IDE support
- **Accessory Categories**: Support for all HomeKit accessory types
- **Session Management**: Encrypted session handling

## Directory Structure

- `docs/` - Generated TypeDoc API documentation
- `README.md` - Getting started guide
- `CHANGELOG.md` - Version history
- `PACKAGE.md` - Package metadata

## Common Tasks

### Creating an Accessory
See the examples in the docs folder for creating HomeKit accessories.

### Pairing with Controllers
HAP-nodejs handles the HomeKit pairing process automatically.

### Working with Services and Characteristics
Use predefined service and characteristic types from the library.

## Related Documentation

- [HomeKit ADK](../homekit-adk/) - Apple's official HomeKit specification
- [Homebridge](https://github.com/homebridge/homebridge) - HomeKit bridge platform
- [HomeKit Protocol](../homekit-specification/) - HAP specification details
