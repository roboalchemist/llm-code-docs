# nsc workspace describe

Display information about your currently authenticated workspace.

## Basic Usage

```bash
nsc workspace describe [--output <plain|json>] [--key <json-field>]
```

## Description

This command describes the currently authenticated workspace and allows you to view details like workspace name, tenant ID, and registry URL.

## Key Features

**Output Options:**

- `-o` or `--output <type>`: Specify output format (json or plain, with plain as default)
- `-k` or `--key <json-field>`: Select a specific JSON field when used with --output=json

## Example Usage

```bash
nsc workspace describe

nsc workspace describe -o json

nsc workspace describe -o json -k registry_url
```

## Related Commands

To switch between workspaces, use the `nsc login` command instead.
