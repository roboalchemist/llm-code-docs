# aiohomekit Architecture

## Module Organization

```
aiohomekit/
├── __init__.py           # Main exports: Controller, exceptions
├── controller/           # Core controller implementation
│   ├── abstract.py      # Abstract base classes and TransportType
│   ├── controller.py    # Main Controller class
│   ├── ip/              # IP protocol implementation
│   ├── ble/             # Bluetooth Low Energy implementation
│   └── coap/            # CoAP protocol implementation
├── crypto/              # Cryptographic primitives
│   ├── chacha20poly1305.py  # AEAD cipher
│   ├── hkdf.py              # Key derivation
│   └── srp.py               # Secure Remote Password
├── protocol/            # HomeKit protocol
│   ├── tlv.py           # TLV8 encoding/decoding
│   └── statuscodes.py   # HAP status codes
├── tlv8.py             # TLV8 utilities
├── pdu.py              # Protocol Data Units
└── characteristic_cache.py  # Caching layer
```

## Protocol Layers

### Layer 1: Transport
- **IP**: TCP/HTTP with mDNS discovery
- **BLE**: Bluetooth Low Energy with characteristic notifications
- **CoAP**: Constrained Application Protocol for low-power devices

### Layer 2: Security
- TLV8-encoded messages
- ChaCha20-Poly1305 AEAD encryption for IP transport
- SRP 3072-bit for pairing
- HKDF for key derivation

### Layer 3: HAP (HomeKit Accessory Protocol)
- Service discovery and enumeration
- Characteristic read/write operations
- Event subscriptions and notifications
- Accessory metadata (name, category, features)

### Layer 4: Application
- Controller class - main entry point
- Pairing management
- Accessory and characteristic caching
- Event handling

## Async Architecture

All operations are async-first using Python's `asyncio`:
- Non-blocking network I/O
- Concurrent operations on multiple accessories
- Event-driven subscription handling
- Timeout management with `async-timeout`

## Data Flow Examples

### Pairing Flow
1. Start pairing via Controller
2. Exchange SRP identity and salt
3. Compute session key using HKDF
4. Exchange pairing information (TLV8 encoded)
5. Store pairing credentials in configuration

### Read Characteristic Flow
1. Open connection to accessory (cached if possible)
2. Build HAP read request (TLV8 format)
3. Encrypt with session key (ChaCha20-Poly1305)
4. Send via transport (IP/BLE/CoAP)
5. Receive and decrypt response
6. Parse characteristic value
7. Return to caller

### Subscribe to Events Flow
1. Open connection to accessory
2. Send subscription request (HAP format)
3. Keep connection open
4. Receive event notifications
5. Parse and deliver to subscribers
6. Maintain connection until unsubscribed

## Key Design Decisions

### Why Hand-Rolled HTTP?
- Need for low-level control over request/response handling
- HAP requires handling unsolicited responses (events)
- Device compatibility requires strict formatting
- Some device quirks require non-standard behavior

### Why Hand-Rolled Crypto?
- Minimize external dependencies
- Ensure cross-platform wheel availability
- Avoid hard system library dependencies
- Integrate seamlessly with Home Assistant

### Why Async-First?
- Home Assistant is fully async
- Allows concurrent operations on multiple devices
- Better resource utilization
- Natural fit for event-driven HomeKit protocol

## Configuration Storage

The library stores configuration in JSON format containing:
- Pairing ID and keys for each accessory
- Controller identity (UUID, LTPK)
- Characteristic metadata cache
- Device-specific quirk information

Configuration files are typically stored in Home Assistant's config directory.

## Error Handling Strategy

The library uses specific exception types to allow fine-grained error handling:
- Transient errors (backoff, busy) trigger retries
- Pairing errors (already paired) are fatal
- Connection errors attempt reconnection
- Protocol errors are reported with context

## Testing

The library uses pytest for testing with:
- Unit tests for cryptography and protocol layers
- Integration tests with real HomeKit devices
- Mock tests for accessories and protocols
- Coverage targets for critical paths
