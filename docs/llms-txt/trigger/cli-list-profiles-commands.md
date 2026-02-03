# Source: https://trigger.dev/docs/cli-list-profiles-commands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI list-profiles command

> Use these options when using the `list-profiles` CLI command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest list-profiles
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest list-profiles
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest list-profiles
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField body="Log level" type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField body="Skip telemetry" type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField body="Help" type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField body="Version" type="--version | -v">
  Displays the version number of the CLI.
</ParamField>
