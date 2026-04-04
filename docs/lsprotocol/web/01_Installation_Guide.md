# Source: https://github.com/microsoft/lsprotocol

# Installation and Usage Guide

# Installation and Usage Guide

## Installation

Install lsprotocol via pip:

```bash
python -m pip install lsprotocol
```

## Quick Start

### Import and Use Types

```python
from lsprotocol import types

# Create a Position
position = types.Position(line=10, character=3)

# Create a Range
range_obj = types.Range(
    start=position,
    end=types.Position(line=10, character=10)
)
```

### Using Type Converters

```python
import json
from lsprotocol import converters, types

# Create a type instance
position = types.Position(line=10, character=3)

# Get a converter
converter = converters.get_converter()

# Convert to JSON-serializable dict
json_dict = converter.unstructure(position, unstructure_as=types.Position)
print(json.dumps(json_dict))  # {"line": 10, "character": 3}

# Convert back from dict to type
position_obj = converter.structure(json_dict, types.Position)
```

## Supported LSP Version

- **LSP Version:** 3.17.0

## Use Cases

lsprotocol is designed for developers building:
- Language Server Protocol (LSP) servers
- LSP clients and editor plugins
- Tools that extend LSP functionality
- Applications that need LSP type definitions

## Project Structure

The project consists of:
- **types.py** - Auto-generated LSP type definitions
- **converters.py** - Type conversion utilities
- **validators.py** - Validation utilities
- **_hooks.py** - Internal hooks for type generation

## Generation Process

The types are generated from the official LSP specification:

```bash
# To regenerate types (requires nox)
python -m pip install nox
python -m nox --session build_lsp
```

## Links

- **GitHub Repository:** https://github.com/microsoft/lsprotocol
- **PyPI Package:** https://pypi.org/project/lsprotocol/
- **Language Server Protocol:** https://microsoft.github.io/language-server-protocol/
