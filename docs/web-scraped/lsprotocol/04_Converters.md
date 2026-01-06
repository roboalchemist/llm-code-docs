# Source: https://raw.githubusercontent.com/microsoft/lsprotocol/main/packages/python/lsprotocol/converters.py

# Type Converters Module

# Type Converters

The converters module provides utilities for converting between lsprotocol types and JSON-serializable objects.

```python
def get_converter(
```

## Converter Usage

The `get_converter()` function returns a converter instance that can be used to:
- **Unstructure:** Convert lsprotocol types to JSON-serializable dicts
- **Structure:** Convert dicts back to lsprotocol types

### Example:
```python
from lsprotocol import converters, types

position = types.Position(line=10, character=3)
converter = converters.get_converter()
json_data = converter.unstructure(position, unstructure_as=types.Position)
```
