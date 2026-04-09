# Mypy plugin

Mypy plugin provides type checking for `luigi.Task` using Mypy.

Require Python 3.8 or later.

## How to use

Configure Mypy to use this plugin by adding the following to your `mypy.ini` file:

```
[mypy]
plugins = luigi.mypy

```