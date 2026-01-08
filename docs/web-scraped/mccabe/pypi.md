# McCabe on PyPI
# Source: https://pypi.org/project/mccabe/

McCabe is available on PyPI as a Python package for checking cyclomatic complexity.

## Installation

McCabe can be installed via pip:

```bash
pip install mccabe
```

## Usage

McCabe can be used as:
1. A standalone script
2. A Flake8 plugin

### As a Flake8 Plugin

Once installed, enable McCabe complexity checking in Flake8:

```bash
flake8 --max-complexity=10 myfile.py
```

### Suppressing Warnings

To suppress complexity warnings on specific functions, use:

```python
def complex_function():  # noqa: C901
    # implementation
    pass
```

## Configuration

Set maximum complexity in `.flake8` or `setup.cfg`:

```ini
[flake8]
max-complexity = 10
```

For more information, visit the [project repository](https://github.com/PyCQA/mccabe) or the [official documentation](https://github.com/PyCQA/mccabe#readme).
