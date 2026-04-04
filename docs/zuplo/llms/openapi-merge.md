# Source: https://www.zuplo.com/docs/cli/openapi-merge.md

# Zuplo CLI: OpenAPI Merge

<CliCommand
  command="openapi merge"
  description="Merge an OpenAPI file into your Zuplo project"
  options={[
  {
    "name": "source",
    "type": "string",
    "description": "The OpenAPI file to merge (file path or URL)",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "s"
    ]
  },
  {
    "name": "destination",
    "type": "string",
    "description": "The destination file name (must end with .oas.json)",
    "default": "./config/routes.oas.json",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "d"
    ]
  },
  {
    "name": "merge-mode",
    "type": "string",
    "description": "The merge mode to use when merging the OpenAPI file",
    "default": "path-method",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "m"
    ],
    "choices": [
      "path-method",
      "operation-id"
    ]
  },
  {
    "name": "prepend-path",
    "type": "string",
    "description": "Directly provide a path to prepend to all paths (e.g., '/v1')",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "server-paths",
    "type": "boolean",
    "description": "Prepend the pathname from the first server URL to all paths",
    "default": true,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "watch",
    "type": "boolean",
    "description": "Watch source file for changes and automatically re-merge",
    "default": false,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 oas merge --source openapi.yaml --destination ./config/routes.oas.json",
    "Merge an OpenAPI file into your Zuplo project"
  ],
  [
    "$0 oas merge -s https://api.example.com/openapi.json -d ./config/api.oas.json",
    "Merge an OpenAPI file from a URL"
  ],
  [
    "$0 oas merge \\\n  --source openapi.yaml \\\n  --destination ./config/routes.oas.json \\\n  --merge-mode operation-id",
    "Merge using operation-id instead of path-method matching"
  ],
  [
    "$0 oas merge \\\n  --source openapi.yaml \\\n  --destination ./config/routes.oas.json \\\n  --prepend-path /v1",
    "Merge and prepend '/v1' to all paths"
  ],
  [
    "$0 oas merge \\\n  --source openapi.yaml \\\n  --destination ./config/routes.oas.json \\\n  --watch",
    "Watch the source file for changes and automatically re-merge"
  ]
]}
  usage="$0 oas merge --source <file|url> --destination <file> [options]"
>

## Common use cases

### Importing an existing OpenAPI file

The command supports importing both JSON and YAML formats. The format is
inferred from the file extension.

```bash
zuplo openapi merge --source /path/to/openapi.json
zuplo openapi merge --source /path/to/openapi.yaml
```

When no `--destination` option is provided, the OpenAPI file is automatically
merged into `routes.oas.json`.

To import a remote file, use the `--source` option with a URL. The command
downloads the file to a temporary directory and imports it.

```bash
zuplo openapi merge --source https://example.com/path/to/openapi.json
```

To rename the destination file, use the `--destination` option.

```bash
zuplo openapi merge \
  --source https://example.com/path/to/openapi.json \
  --destination new-name
```

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
