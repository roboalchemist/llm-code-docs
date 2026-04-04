# Source: https://www.zuplo.com/docs/cli/openapi-convert.md

# Zuplo CLI: OpenAPI Convert

<CliCommand
  command="openapi convert"
  description="Convert OpenAPI files between JSON and YAML formats"
  options={[
  {
    "name": "input",
    "type": "string",
    "description": "The input OpenAPI file (JSON or YAML)",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "i"
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
    "name": "output",
    "type": "string",
    "description": "Output file path (if not specified, generates based on input)",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "o"
    ],
    "normalize": true
  },
  {
    "name": "json",
    "type": "boolean",
    "description": "Convert to JSON format",
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
    "description": "Convert to YAML format",
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
    "description": "Watch input file for changes and automatically re-convert",
    "default": false,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 oas convert --input openapi.yaml --json",
    "Convert a YAML OpenAPI file to JSON format"
  ],
  [
    "$0 oas convert -i openapi.json --yaml -o api-spec.yaml",
    "Convert a JSON OpenAPI file to YAML with custom output path"
  ],
  [
    "$0 oas convert --input api.yaml --format json",
    "Convert using --format flag instead of --json/--yaml"
  ],
  [
    "$0 oas convert --input openapi.yaml --json --watch",
    "Watch the input file for changes and automatically re-convert"
  ]
]}
  usage="$0 oas convert --input <file> (--json|--yaml|--format <format>) [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
