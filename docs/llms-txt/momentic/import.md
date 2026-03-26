# Source: https://momentic.ai/docs/cli/commands/import.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# import

Import all tests, modules, and environments configured on Momentic Cloud to your
local environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic import
  ```

  ```bash yarn theme={null}
  yarn dlx momentic import
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic import
  ```
</CodeGroup>

To import a single test and the modules it uses into your local environment,
pass the test path from Momentic Cloud to the import command.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic import <test-path>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic import <test-path>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic import <test-path>
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).