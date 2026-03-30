# Source: https://momentic.ai/docs/quarantine.md

# Source: https://momentic.ai/docs/cli/commands/quarantine.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# quarantine

Quarantine and unquarantine tests

## `add`

Quarantine a test so that it is skipped in all pipelines.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine add [options] <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine add [options] <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine add [options] <test>
  ```
</CodeGroup>

* **\<test>**: The test to quarantine. If not specified, you will be prompted
  to select one interactively.

### Options

#### `--reason <reason>`

The reason for quarantining the test. This will be displayed in the Momentic
Cloud UI to help with debugging.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine add --reason <reason> <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine add --reason <reason> <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine add --reason <reason> <test>
  ```
</CodeGroup>

## `list`

List quarantined tests.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine list
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine list
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine list
  ```
</CodeGroup>

## `remove`

Unquarantine a test so that it is no longer skipped in pipelines.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine remove [options] <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine remove [options] <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine remove [options] <test>
  ```
</CodeGroup>

* **\<test>**: The test to unquarantine. If not specified, you will be prompted
  to select one interactively.

### Options

#### `--reason <reason>`

The reason for unquarantining the test. This is optional, but can be useful for
record-keeping purposes.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine remove --reason <reason> <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine remove --reason <reason> <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine remove --reason <reason> <test>
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).