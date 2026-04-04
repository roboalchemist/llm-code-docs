# Source: https://www.zuplo.com/docs/cli/editor.md

# Zuplo CLI: Editor

<CliCommand
  command="editor"
  description="Starts a local Open API Designer"
  options={[
  {
    "name": "dir",
    "type": "string",
    "description": "The directory containing your Zuplo API",
    "default": ".",
    "required": false,
    "deprecated": false,
    "hidden": true,
    "normalize": false
  },
  {
    "name": "port",
    "type": "number",
    "description": "The port to run the route designer on",
    "default": 9100,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 editor",
    "Start the Open API Designer on the default port (9100)"
  ],
  [
    "$0 editor --port 8080",
    "Start the Open API Designer on a custom port"
  ]
]}
  usage="$0 editor [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
