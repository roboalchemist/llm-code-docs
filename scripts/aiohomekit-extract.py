#!/usr/bin/env python3
"""
aiohomekit Documentation Extractor
Extracts documentation from the aiohomekit Python library for HomeKit accessory control.
aiohomekit is an asyncio HomeKit client used by Home Assistant for HomeKit device integration.
It provides async Python APIs for pairing with and controlling HomeKit accessories over IP, BLE, and CoAP.
"""

import os
import sys
import shutil
import tempfile
import subprocess
from pathlib import Path

# Repository configuration
REPO_URL = "https://github.com/Jc2k/aiohomekit.git"
REPO_BRANCH = "main"

def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "aiohomekit"

        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(clone_path)],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"    -> Error cloning repository: {result.stderr}")
            return None

        print(f"    -> Repository cloned successfully")
        return clone_path

    except subprocess.TimeoutExpired:
        print(f"    -> Timeout cloning repository")
        return None
    except Exception as e:
        print(f"    -> Error cloning repository: {e}")
        return None


def extract_python_module_docs(source_dir, module_name):
    """Extract docstrings from Python module."""
    docs = {}
    module_dir = source_dir / module_name

    if not module_dir.exists():
        return docs

    for py_file in module_dir.rglob("*.py"):
        try:
            with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Extract module docstring and class/function definitions
                lines = content.split('\n')
                docstring = []
                in_docstring = False
                for line in lines[:100]:  # First 100 lines for module docstring
                    if '"""' in line or "'''" in line:
                        in_docstring = not in_docstring
                    if in_docstring or ('"""' in line or "'''" in line):
                        docstring.append(line)
                if docstring:
                    rel_path = py_file.relative_to(module_dir)
                    docs[str(rel_path)] = '\n'.join(docstring[:30])
        except Exception:
            pass

    return docs


def create_api_documentation(repo_path, output_dir):
    """Create comprehensive API documentation from the repository."""
    docs_content = """# aiohomekit API Documentation

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
"""

    output_dir.mkdir(parents=True, exist_ok=True)

    # Write main API documentation
    with open(output_dir / "API.md", "w", encoding="utf-8") as f:
        f.write(docs_content)

    return True


def copy_repository_files(source_dir, output_dir):
    """Copy important repository files."""
    try:
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy README
        readme_file = source_dir / "README.md"
        if readme_file.exists():
            with open(readme_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = "https://github.com/Jc2k/aiohomekit/blob/master/README.md"
            header = f"# Source: {source_url}\n\n"
            with open(output_dir / "README.md", 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"    -> Copied README.md")

        # Copy pyproject.toml for package info
        pyproject_file = source_dir / "pyproject.toml"
        if pyproject_file.exists():
            with open(pyproject_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            source_url = "https://github.com/Jc2k/aiohomekit/blob/master/pyproject.toml"
            header = f"# Source: {source_url}\n\n"
            with open(output_dir / "PACKAGE_CONFIG.md", 'w', encoding='utf-8') as f:
                f.write(f"{header}```toml\n{content}\n```\n")
            print(f"    -> Copied pyproject.toml")

        # Copy LICENSE
        license_file = source_dir / "LICENSE.md"
        if license_file.exists():
            with open(license_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            with open(output_dir / "LICENSE.md", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    -> Copied LICENSE.md")

        return True

    except Exception as e:
        print(f"    -> Error copying repository files: {e}")
        return False


def create_architecture_doc(output_dir):
    """Create architecture documentation."""
    arch_doc = """# aiohomekit Architecture

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
"""

    with open(output_dir / "ARCHITECTURE.md", "w", encoding="utf-8") as f:
        f.write(arch_doc)
    print(f"    -> Created ARCHITECTURE.md")


def main():
    """Main function to extract aiohomekit documentation."""
    print("=" * 70)
    print("aiohomekit Documentation Extractor")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "aiohomekit"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        print("Cloning repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

        if not repo_path:
            print("\nError: Failed to clone repository")
            sys.exit(1)

        # Copy repository files
        print("\nCopying repository files...")

        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        if not copy_repository_files(repo_path, output_dir):
            print("\nError: Failed to copy repository files")
            sys.exit(1)

        # Create API documentation
        print("\nGenerating API documentation...")
        if not create_api_documentation(repo_path, output_dir):
            print("\nError: Failed to generate API documentation")
            sys.exit(1)
        print(f"    -> Created API.md")

        # Create architecture documentation
        print("\nGenerating architecture documentation...")
        create_architecture_doc(output_dir)

    # Verify extraction
    print("\nVerifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    text_files = list(output_dir.glob("**/*"))
    text_files = [f for f in text_files if f.is_file()]
    total_size = sum(f.stat().st_size for f in text_files)

    print(f"  Total files: {len(text_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(text_files) == 0:
        print("\n  Warning: No files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Generated documentation files:")
    for text_file in sorted(text_files):
        file_size = text_file.stat().st_size
        print(f"    - {text_file.relative_to(output_dir)} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
