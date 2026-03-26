# Source: https://momentic.ai/docs/cli/commands/apply.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# apply

## `patch`

Apply patch changes to your Momentic tests.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch [options]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch [options]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch [options]
  ```
</CodeGroup>

### Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --filter workspace-name
  ```
</CodeGroup>

#### `--from <from>`

The identifier of the patch to apply. It consists of three random words
separated by dashes, like `potato-apple-cherry`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --from potato-apple-cherry
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --from potato-apple-cherry
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --from potato-apple-cherry
  ```
</CodeGroup>

#### `--to <to>`

The test name to apply the patch to.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --from potato-apple-cherry --to example-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --from potato-apple-cherry --to example-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --from potato-apple-cherry --to example-test
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).