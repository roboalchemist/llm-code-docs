# Source: https://grafbase.com/docs/cli/commands/extension.md

# Grafbase Extension Command

Tools to create, manage, and deploy Grafbase extensions.

## Initialize a New Extension

Create a new Grafbase extension.

**Usage:**

```bash
grafbase extension init --type <TYPE> <PATH>
```

- `--type`: Specify the type of extension to create. Either `auth` or `resolver`.

## Build an Extension

Build and package a Grafbase extension.

**Usage:**

```bash
grafbase extension build [OPTIONS]
```

- `--output`: Specify the output directory for the built extension. Defaults to `./build`.
- `--debug`: Build the extension in debug mode. Results in a larger and slower build output.
- `--source-dir`: Specify the source directory for the extension. Defaults to `.`.
- `--scratch-dir`: Specify the scratch directory for the extension. Defaults to `./target`.