# Source: https://www.zuplo.com/docs/cli/dev.md

# Zuplo CLI: Dev

<CliCommand
  command="dev"
  description="Runs the Zuplo API locally"
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
    "name": "start-editor",
    "type": "boolean",
    "description": "Start the editor with the local server",
    "default": true,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "start-docs",
    "type": "boolean",
    "description": "Start the docs server with the local development setup",
    "default": true,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "unsafely-ignore-certificate-errors",
    "type": "boolean",
    "description": "Unsafely ignore certificate errors",
    "default": false,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "port",
    "type": "number",
    "description": "The port to run the local server on",
    "default": 9000,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "editor-port",
    "type": "number",
    "description": "The port to run the route designer on",
    "default": 9100,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "docs-port",
    "type": "number",
    "description": "The port to run the docs server on",
    "default": 9200,
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "debug-port",
    "type": "number",
    "description": "The port to run the Chrome inspector on",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 dev",
    "Start the local development server with default settings (port 9000 for API, port 9100 for editor, port 9200 for docs)"
  ],
  [
    "$0 dev --port 8080",
    "Start the local server on a custom port"
  ],
  [
    "$0 dev --no-start-editor",
    "Start only the API server without opening the editor"
  ],
  [
    "$0 dev --no-start-docs",
    "Start the API server without the docs server"
  ],
  [
    "$0 dev --debug-port 9229",
    "Start with Chrome DevTools inspector enabled on port 9229"
  ]
]}
  usage="$0 dev [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
