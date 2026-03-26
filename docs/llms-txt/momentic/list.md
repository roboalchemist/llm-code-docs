# Source: https://momentic.ai/docs/mobile-cli/commands/list.md

# Source: https://momentic.ai/docs/cli/commands/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# list

<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

List tests in the current project.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to list. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --filter workspace-name
  ```
</CodeGroup>

### `--labels <labels...>`

Run tests with the specified labels. This allows you to filter tests based on
assigned labels.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --labels smoke regression
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --labels smoke regression
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --labels smoke regression
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --exclude "billing*"
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).