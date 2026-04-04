# Source: https://www.zuplo.com/docs/dev-portal/zudoku/configuration/docs.md

# Source: https://www.zuplo.com/docs/cli/docs.md

# Zuplo CLI: Docs

<CliCommand
  command="docs"
  description="Runs the Zuplo docs server locally"
  options={[
  {
    "name": "dir",
    "type": "string",
    "description": "The directory containing your Zuplo API",
    "default": ".",
    "required": false,
    "deprecated": false,
    "hidden": true,
    "normalize": true
  },
  {
    "name": "server-url",
    "type": "string",
    "description": "The URL of the Zuplo API server to use (e.g., https://my-api.zuplo.dev)",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "port",
    "type": "number",
    "description": "The port to run the docs server on",
    "default": 9200,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 docs",
    "Start the docs server with default settings (port 9200)"
  ],
  [
    "$0 docs --port 3000",
    "Start the docs server on a custom port"
  ],
  [
    "$0 docs --server-url https://my-api.zuplo.dev",
    "Start the docs server pointing to a remote Zuplo API"
  ],
  [
    "$0 docs --server-url http://localhost:9000",
    "Start the docs server pointing to a local Zuplo API"
  ]
]}
  usage="$0 docs [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
