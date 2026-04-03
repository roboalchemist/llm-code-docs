# YAML Documentation

YAML (YAML Ain't Markup Language) is a human-friendly data serialization language for all programming languages.

**Sources:**

- PyYAML Documentation: https://pyyaml.org/wiki/PyYAMLDocumentation
- YAML Official Spec: https://yaml.org/
- YAML 1.2 Specification: https://yaml.org/spec/1.2/spec.html

## What is YAML?

YAML is a human-friendly data serialization language designed to be easy to read and write. It supports mapping structures (hashes/dictionaries), sequences (arrays/lists), and scalar values. YAML is language-independent and has implementations in most programming languages.

## YAML Language Overview

### Basic Data Types

YAML supports several fundamental data types:

- **Scalars**: Strings, integers, floating-point numbers, booleans, null values
- **Sequences**: Ordered lists of values using the `-` character
- **Mappings**: Key-value pairs using the `:` character

### Scalar Types

YAML automatically recognizes different scalar types:

```yaml
# Strings (quoted and unquoted)
name: John Doe
message: "Hello, World!"

# Numbers
integer: 42
float: 3.14

# Booleans
active: true
inactive: false
also_true: yes
also_false: no

# Null values
empty: null
tilde: ~

# Dates (ISO 8601)
date: 2023-01-15
timestamp: 2023-01-15T10:30:00Z
```

### Sequences (Arrays/Lists)

```yaml
# Block style
fruits:
  - apple
  - banana
  - orange

# Flow style (compact)
colors: [red, green, blue]
```

### Mappings (Dictionaries/Objects)

```yaml
# Block style
person:
  name: John
  age: 30
  email: john@example.com

# Flow style (compact)
address: {street: "123 Main St", city: "Boston", zip: 02101}
```

### Nested Structures

```yaml
company:
  name: Acme Corp
  departments:
    - name: Engineering
      employees:
        - name: Alice
          role: Developer
        - name: Bob
          role: DevOps
    - name: Sales
      employees:
        - name: Charlie
          role: Account Manager
```

### Multi-line Strings

```yaml
# Literal style (preserves newlines)
description: |
  This is a multi-line
  literal string.
  It preserves newlines.

# Folded style (converts newlines to spaces)
summary: >
  This is a folded
  string that will be
  converted to a single line.

# Quoted strings
quoted: "This is a quoted string with \"escaped quotes\""
```

### Anchors and Aliases

YAML allows you to reference previously defined values:

```yaml
defaults: &default_settings
  timeout: 30
  retries: 3

service1:
  <<: *default_settings
  host: example.com

service2:
  <<: *default_settings
  host: api.example.com
  timeout: 60  # Override default
```

## PyYAML Library

PyYAML is a full-featured YAML framework for Python. It provides a complete YAML parser and emitter that supports both pure Python and optimized LibYAML-based implementations.

### Installation

```bash
pip install pyyaml
```

To use the faster LibYAML bindings:

```bash
# First install LibYAML (version 0.1.4 or higher)
# Then install PyYAML with LibYAML support
python setup.py --with-libyaml install
```

### Basic Usage

#### Loading YAML

```python
import yaml

# Load from a string
yaml_string = """
name: John
age: 30
hobbies:
  - reading
  - coding
"""
data = yaml.safe_load(yaml_string)

# Load from a file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Load multiple documents
documents = yaml.safe_load_all(yaml_string)
```

#### Dumping YAML

```python
import yaml

data = {
    'name': 'John',
    'age': 30,
    'hobbies': ['reading', 'coding']
}

# Dump to string
yaml_output = yaml.dump(data)
print(yaml_output)

# Dump to file
with open('output.yaml', 'w') as f:
    yaml.dump(data, f)

# Dump multiple documents
documents = [data, {'name': 'Jane', 'age': 25}]
with open('multi.yaml', 'w') as f:
    yaml.dump_all(documents, f)
```

### Safety Considerations

**Warning:** `yaml.load()` is unsafe with untrusted data. It can execute arbitrary Python code.

```python
import yaml

# UNSAFE - Do not use with untrusted input
# yaml.load(untrusted_data)

# SAFE - Always use safe_load for untrusted input
data = yaml.safe_load(untrusted_data)
```

The difference:

- `yaml.load()` - Full YAML parsing, can instantiate arbitrary Python objects
- `yaml.safe_load()` - Only constructs simple Python objects (str, list, dict, etc.)

### Formatting Options

Control output formatting with parameters:

```python
import yaml

data = {'a': 1, 'b': {'c': 3, 'd': 4}}

# Default style (flow for nested collections)
print(yaml.dump(data))
# Output:
# a: 1
# b: {c: 3, d: 4}

# Force block style
print(yaml.dump(data, default_flow_style=False))
# Output:
# a: 1
# b:
#   c: 3
#   d: 4

# Custom indentation
print(yaml.dump(data, indent=4))

# Sort keys
print(yaml.dump(data, sort_keys=True))

# Canonical form
print(yaml.dump(data, canonical=True))
```

### Working with Custom Objects

Define custom YAML tags for your Python classes:

```python
import yaml

class Person(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!person'
    yaml_fields = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, age={self.age})'

# Dumping a custom object
person = Person('Alice', 30)
yaml_output = yaml.dump(person)
# Output: !person
#   age: 30
#   name: Alice

# Loading a custom object
yaml_input = """
!person
name: Bob
age: 25
"""
loaded_person = yaml.safe_load(yaml_input)
print(loaded_person)  # Person(name=Bob, age=25)
```

### LibYAML Bindings

Use optimized LibYAML-based parser and emitter:

```python
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

data = load(stream, Loader=Loader)
output = dump(data, Dumper=Dumper)
```

The LibYAML bindings are significantly faster than pure Python implementations.

## Python 2 vs Python 3

### Python 3 (Recommended)

```python
# In Python 3, strings are always Unicode
import yaml

data = {'name': 'Alice', 'message': '你好'}
yaml_output = yaml.dump(data)  # Returns str
yaml_bytes = yaml.dump(data, encoding='utf-8')  # Returns bytes
```

### Python 2 (Legacy)

```python
# In Python 2, different handling for different string types
yaml_output = yaml.dump(data)  # Returns str
yaml_bytes = yaml.dump(data, encoding='utf-8')  # Returns bytes
```

## Common Use Cases

### Configuration Files

```yaml
# app.yaml
database:
  host: localhost
  port: 5432
  username: admin
  password: secret

server:
  host: 0.0.0.0
  port: 8000
  debug: false
```

### Data Serialization

```yaml
# data.yaml
users:
  - id: 1
    name: Alice
    email: alice@example.com
  - id: 2
    name: Bob
    email: bob@example.com
```

### Infrastructure as Code

```yaml
# docker-compose.yaml
version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: secret
```

## Frequently Asked Questions

### Why are nested collections formatted differently?

By default, PyYAML chooses the style (block or flow) based on whether a collection contains nested collections:

- Block style: Used when the collection has nested collections
- Flow style: Used when the collection only contains scalars

To force block style:

```python
yaml.dump(data, default_flow_style=False)
```

### How do I handle circular references?

Use anchors and aliases:

```yaml
anchor: &reference
  value: 1
use_anchor: *reference
```

### Can I add custom constructors?

Yes, you can extend PyYAML with custom constructors and representers for your data types.

## YAML Best Practices

1. **Use safe_load for untrusted input** - Never use `load()` with untrusted data
2. **Prefer block style for readability** - Use `default_flow_style=False`
3. **Use meaningful keys** - Make YAML configuration self-documenting
4. **Validate after loading** - Check loaded data against a schema
5. **Use version indicators** - Start files with `%YAML 1.2`
6. **Comment your YAML** - Use `#` for documentation
7. **Use proper indentation** - Typically 2 or 4 spaces, never tabs

## YAML Specifications

- **YAML 1.2 (Oct 1, 2021)**: Current stable specification
- **YAML 1.1**: Previous specification (supported by most parsers)
- **YAML 1.0**: Original specification

The official YAML specification is available at https://yaml.org/spec/

## Resources

- **Official YAML Site**: https://yaml.org/
- **PyYAML Documentation**: https://pyyaml.org/wiki/PyYAMLDocumentation
- **PyYAML GitHub**: https://github.com/yaml/pyyaml
- **YAML Test Suite**: https://github.com/yaml/yaml-test-suite
- **YAML Playground**: https://yaml.org/playground/

## YAML Language Features

### Comments

```yaml
# This is a comment
key: value  # Inline comment
```

### Tags and Directives

```yaml
%YAML 1.2
---
# Explicit type tags
explicit_string: !!str 123
explicit_int: !!int "123"
explicit_float: !!float 123
```

### Special Characters Escaping

```yaml
# Strings with special characters
needs_quotes: "This: has, special [characters]"
escaped_quotes: "He said \"Hello\""
newline_char: "Line 1\nLine 2"
```

## Error Handling

```python
import yaml

try:
    data = yaml.safe_load(yaml_input)
except yaml.YAMLError as e:
    print(f"YAML parsing error: {e}")
except yaml.scanner.ScannerError as e:
    print(f"Scanning error: {e}")
except yaml.parser.ParserError as e:
    print(f"Parsing error: {e}")
```

## Performance Considerations

- **LibYAML bindings**: 3-5x faster than pure Python
- **Lazy loading**: Use `yaml.load_all()` for large files with multiple documents
- **Streaming**: For very large files, consider streaming parsers
- **Caching**: Cache parsed YAML to avoid re-parsing

## Comparison with Other Formats

| Feature           | YAML | JSON     | XML | TOML |
| :--- | :--- | :--- | :--- | :--- |
| Human Readable    | Yes | Moderate | No  | Yes  |
| Comments          | Yes | No       | No  | Yes  |
| Quoted Keys       | No  | Yes      | Yes | No   |
| Anchors/Refs      | Yes | No       | Yes | No   |
| Nested Structures | Yes | Yes      | Yes | Yes  |
| Strict Spec       | No  | Yes      | Yes | Yes  |

## YAML in Different Languages

- **Python**: PyYAML
- **JavaScript/Node.js**: js-yaml, yaml
- **Go**: gopkg.in/yaml.v3
- **Rust**: serde_yaml
- **Java**: SnakeYAML
- **PHP**: symfony/yaml
- **Ruby**: YAML
- **C/C++**: LibYAML

## Summary

YAML is a versatile, human-friendly data serialization format ideal for configuration files, data exchange, and infrastructure as code. Python's PyYAML library provides a complete, production-ready implementation with both pure Python and optimized LibYAML bindings for performance-critical applications.

Always prioritize using `yaml.safe_load()` over `yaml.load()` when handling untrusted input to prevent security vulnerabilities.
