# Source: https://www.zuplo.com/docs/cli/openapi-overlay.md

# Zuplo CLI: OpenAPI Overlay

<CliCommand
  command="openapi overlay"
  description="Apply an OpenAPI Overlay to an OpenAPI document"
  options={[
  {
    "name": "input",
    "type": "string",
    "description": "The input OpenAPI file",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "i"
    ],
    "normalize": true
  },
  {
    "name": "overlay",
    "type": "string",
    "description": "The overlay file",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "l"
    ],
    "normalize": true
  },
  {
    "name": "output",
    "type": "string",
    "description": "The output OpenAPI file path",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "o"
    ],
    "normalize": true
  },
  {
    "name": "format",
    "type": "string",
    "description": "Output format",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "f"
    ],
    "choices": [
      "json",
      "yaml"
    ]
  },
  {
    "name": "json",
    "type": "boolean",
    "description": "Output in JSON format",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "conflicts": [
      "yaml",
      "format"
    ]
  },
  {
    "name": "yaml",
    "type": "boolean",
    "description": "Output in YAML format",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "conflicts": [
      "json",
      "format"
    ]
  },
  {
    "name": "watch",
    "type": "boolean",
    "description": "Watch input and overlay files for changes and automatically re-apply",
    "default": false,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 oas overlay --input openapi.json --overlay changes.json --output result.json",
    "Apply an overlay to an OpenAPI document"
  ],
  [
    "$0 oas overlay -i api.yaml -v overlay.yaml -o result.yaml --yaml",
    "Apply overlay and output in YAML format"
  ],
  [
    "$0 oas overlay \\\n  --input openapi.json \\\n  --overlay overlay.json \\\n  --output result.yaml \\\n  --format yaml",
    "Apply overlay and convert format in one step"
  ],
  [
    "$0 oas overlay \\\n  --input openapi.json \\\n  --overlay changes.json \\\n  --output result.json \\\n  --watch",
    "Watch input and overlay files for changes and automatically re-apply"
  ]
]}
  usage="$0 oas overlay --input <file> --overlay <file> --output <file> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
