<!-- Source: https://namespace.so/docs/reference/cli/workspace-describe -->

# nsc workspace describe

Describe your current workspace.

`workspace describe` describes the currently authenticated [workspace](/docs/workspaces).
To change between workspaces, run [`nsc login`](/docs/reference/cli/login).

## Usage

```
nsc workspace describe [--output <plain|json>] [--key <json-field>]
```

### Example

```
$ nsc workspace describe
Workspace details:
 
Name: Shared Team Workspace
Tenant ID: <id>
Registry URL: nscr.io/<id>
```

## Options

### -o <type>

Specifies the output format. Supported options are `json` and
`plain`. By default, plain output format is used.

### -k <json-field>

Select a JSON field to print. Only supported in concert with `--output=json`.
For example:

```
$ nsc workspace describe -o json -k registry_url
nscr.io/<id>
```

Last updated July 4, 2025
