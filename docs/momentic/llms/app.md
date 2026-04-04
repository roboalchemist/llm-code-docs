# Source: https://momentic.ai/docs/mobile-cli/commands/app.md

# Source: https://momentic.ai/docs/cli/commands/app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# app

Start the Momentic app.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app [options]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app [options]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app [options]
  ```
</CodeGroup>

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `--disable-cache`

Disable caching entirely. This will cause all steps to run without cached data,
and not save caches after runs. This can result in slower test execution, but
ensures that all steps are run fresh without stored data.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --disable-cache
  ```
</CodeGroup>

### `--save-cache`

Always save updated step caches after successful test runs, even on the main Git
branch and protected Git branches. Please see the
[cache saving eligibility](/step-cache#cache-saving-eligibility) documentation
for more information.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --save-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --save-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --save-cache
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).