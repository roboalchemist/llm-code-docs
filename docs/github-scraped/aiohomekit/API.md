# aiohomekit API Documentation

## Overview

aiohomekit is an asyncio HomeKit client library for Python. It provides APIs for:

- Pairing with HomeKit accessories
- Discovering HomeKit devices over mDNS/Bonjour
- Controlling HomeKit accessories over IP, BLE, and CoAP protocols
- Handling HomeKit events and notifications

This library is primarily used by Home Assistant for HomeKit device integration.

## Installation

```bash
pip install aiohomekit
```

## Core Components

### Controller Classes

The main entry point is the `Controller` class which manages connections to HomeKit accessories.

```python
from aiohomekit import Controller

# Create controller instance
controller = Controller()
```

### Key Exceptions

aiohomekit defines several exception classes for error handling:

- `HomeKitException` - Base exception class
- `AccessoryDisconnectedError` - Accessory went offline
- `AccessoryNotFoundError` - Accessory not found
- `AlreadyPairedError` - Already paired with accessory
- `AuthenticationError` - Authentication failed
- `UnpairedError` - Accessory not paired
- `ConfigurationError` - Configuration issue
- `ConfigLoadingError` - Error loading config
- `ConfigSavingError` - Error saving config
- `BackoffError` - Backoff in progress
- `BluetoothAdapterError` - Bluetooth adapter issue
- `BusyError` - Device busy
- `CharacteristicPermissionError` - Permission denied on characteristic
- `FormatError` - Format error
- `HttpException` - HTTP error
- `IncorrectPairingIdError` - Incorrect pairing ID
- `InvalidAuthTagError` - Invalid authentication tag
- `InvalidError` - Invalid value
- `InvalidSignatureError` - Invalid signature
- `MaxPeersError` - Maximum peers reached
- `MaxTriesError` - Maximum retries exceeded
- `ProtocolError` - Protocol error
- `RequestRejected` - Request was rejected
- `UnavailableError` - Service unavailable
- `UnknownError` - Unknown error

## Transport Types

aiohomekit supports multiple transport protocols through the `TransportType` enum:

- **IP** - HomeKit over IP protocol
- **BLE** - Bluetooth Low Energy (Note: Currently supported via bleak library)
- **CoAP** - Constrained Application Protocol for low-power devices

## Project Structure

### Core Modules

- `aiohomekit.controller` - Main Controller class and TransportType
- `aiohomekit.protocol` - TLV8 and status code handling
- `aiohomekit.crypto` - Cryptographic primitives (ChaCha20-Poly1305, SRP, HKDF)
- `aiohomekit.tlv8` - TLV8 encoding/decoding
- `aiohomekit.pdu` - Protocol Data Unit handling
- `aiohomekit.characteristic_cache` - Caching for characteristics

### Protocol Implementation

The library implements the HomeKit Accessory Protocol (HAP) with:

- TLV8 (Type-Length-Value) encoding for HomeKit protocol messages
- ChaCha20-Poly1305 authenticated encryption
- SRP (Secure Remote Password) for secure pairing
- HKDF (HMAC-based Key Derivation Function) for key derivation

### BLE Support

BLE (Bluetooth Low Energy) support includes:

- Device discovery via Bluetooth advertisements
- BLE-specific client implementation
- Manufacturer data parsing
- Key management for BLE connections

## DeviceCompatibility

The library is primarily tested with:

- Phillips Hue Bridge
- Eve Extend Bridge
- Various other HomeKit accessories

See the [Home Assistant homekit_controller](https://github.com/home-assistant/core/tree/dev/homeassistant/components/homekit_controller) for real-world usage examples.

## Device Compatibility Issues

The library handles known quirks with HomeKit devices:

- **JSON Formatting**: Some devices cannot handle spaces in JSON (e.g., `{"foo": "bar"}` fails, `{"foo":"bar"}` works)
- **Boolean Encoding**: Some devices only support specific boolean representations; the library uses `0` or `1`
- **HTTP Headers**: Some devices are sensitive to header ordering and presence; the library matches iOS client behavior
- **TCP Packet Splitting**: Some devices are sensitive to message splitting; the library ensures atomic writes

## Configuration

The library uses configuration files to store:

- Pairing information
- Controller identity
- Accessory metadata
- Characteristic cache

Configuration can be loaded and saved through the Controller API.

## Home Assistant Integration

aiohomekit is the primary HomeKit integration library for Home Assistant:

- Repository: [homekit_controller](https://github.com/home-assistant/core/tree/dev/homeassistant/components/homekit_controller)
- Used for discovering and controlling HomeKit devices
- Handles characteristic updates and notifications

## Contributing

Contributions are welcome but should be tested with real HomeKit devices when possible. The project prioritizes compatibility with real devices over strict spec compliance.

## FAQ

### Does aiohomekit support creating HomeKit accessories?

No, aiohomekit is client-only. For server/accessory implementations, see:

- [homekit_python](https://github.com/jlusiardi/homekit_python/)
- [HAP-python](https://github.com/ikalchev/HAP-python)

### Why not use a standard HTTP library like aiohttp?

The library uses hand-rolled HTTP for several reasons:

- Need for custom session security without monkey patching
- HAP requires handling responses without corresponding requests (events)
- Real-world devices require strict formatting compliance
- Some responses are technically non-standard HTTP
- Maintaining byte-for-byte accuracy on the write path is critical

### Why does aiohomekit use hand-rolled cryptography implementations?

For compatibility with Home Assistant's build process:

- All dependencies must be pip-installable
- Cross-platform wheels must be available (including Raspberry Pi)
- Should not introduce hard system library dependencies
- Libraries used should already be in Home Assistant dependencies

## License

Apache License 2.0

## Repository

GitHub: https://github.com/Jc2k/aiohomekit
