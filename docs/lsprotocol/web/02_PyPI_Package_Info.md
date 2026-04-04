# Source: https://pypi.org/pypi/lsprotocol/json

# lsprotocol - PyPI Package Information

## Package Information

**Name:** lsprotocol
**Version:** 2025.0.0
**Author:** None
**License:** None
**Home Page:** None
**Project URL:** https://pypi.org/project/lsprotocol/

## Summary

Python types for Language Server Protocol.

## Description

# Language Server Protocol Types implementation for Python

`lsprotocol` is a Python implementation of object types used in the Language Server Protocol (LSP). This repository contains the code generator and the generated types for LSP.

## Overview

LSP is used by editors to communicate with various tools to enables services like code completion, documentation on hover, formatting, code analysis, etc. The intent of this library is to allow you to build on top of the types used by LSP. This repository will be kept up to date with the latest version of LSP as it is updated.

## Installation

`python -m pip install lsprotocol`

## Usage

### Using LSP types

```python
from lsprotocol import types

position = types.Position(line=10, character=3)
```

### Using built-in type converters

```python
# test.py
import json
from lsprotocol import converters, types

position = types.Position(line=10, character=3)
converter = converters.get_converter()
print(json.dumps(converter.unstructure(position, unstructure_as=types.Position)))
```

Output:

```console
> python test.py
{"line": 10, "character": 3}
```



## Requires Python

>=3.8

## Classifiers

- Development Status :: 4 - Beta
- License :: OSI Approved :: MIT License
- Programming Language :: Python
- Programming Language :: Python :: 3.10
- Programming Language :: Python :: 3.11
- Programming Language :: Python :: 3.12
- Programming Language :: Python :: 3.8
- Programming Language :: Python :: 3.9
- Programming Language :: Python :: Implementation :: CPython
- Programming Language :: Python :: Implementation :: PyPy
