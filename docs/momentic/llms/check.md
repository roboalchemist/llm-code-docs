# Source: https://momentic.ai/docs/cli/commands/check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# check

## `duplicate-ids`

Ensure that there are no duplicate step and command IDs in your tests and
modules. This is important for maintaining the integrity of your caches and
avoiding conflicts during execution.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-ids
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-ids
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-ids
  ```
</CodeGroup>

### Options

#### `--fix`

Apply fixes to the duplicate IDs found. This will automatically rename the
duplicate IDs to ensure uniqueness.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-ids --fix
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-ids --fix
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-ids --fix
  ```
</CodeGroup>

## `duplicate-names`

Check for duplicate names in your tests and modules. This helps to prevent
confusion and ensures that each test and module are uniquely identified.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-names
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-names
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-names
  ```
</CodeGroup>

## `config`

Check your `momentic.config.yaml` for errors.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check config
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check config
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check config
  ```
</CodeGroup>

### Options

#### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check config --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check config --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check config --config path/to/momentic.config.yaml
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).