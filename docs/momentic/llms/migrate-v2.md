# Source: https://momentic.ai/docs/cli/migrate-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating to v2.x

## Update Momentic version

<Info>
  Make sure `momentic` is installed as a devDependency in the root of your
  repository.
</Info>

<CodeGroup>
  ```bash npm theme={null}
  npm update momentic
  ```

  ```bash yarn theme={null}
  yarn upgrade momentic
  ```

  ```bash pnpm theme={null}
  pnpm update momentic
  ```
</CodeGroup>

Update CI scripts, `package.json`, Makefiles, and any other files in your
codebase that reference `momentic` to the latest `2.x` version.

## Run the migration wizard

This command will update your `momentic.config.yaml` to include feature flags,
Git branch configuration, and AI agent settings.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic migrate v1-v2
  ```

  ```bash yarn theme={null}
  yarn dlx momentic migrate v1-v2
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic migrate v1-v2
  ```
</CodeGroup>

## Run checks for duplicate IDs

Momentic will fail if it detects duplicate command or step IDs. Duplicate IDs
are caused by manually modifying tests outside of the Momentic editor, and can
lead to test flakiness.

To check whether your existing repository has duplicate IDs, run the following
command. Problems can be automatically fixed by adding the `--fix` flag.

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

## Update CI scripts to install browsers

In Momentic 2.0, browsers must be explicitly installed.

If your CI scripts do not already invoke the `install-browsers` command, add
this command before any tests are executed.

You can determine which browsers to install by searching your codebase for the
`browserType` string. See the [install-browsers](/cli/commands/install-browsers)
command for more information.

## Update CI scripts to upload results

`momentic run` now saves all test results to a local directory called
`test-results` by default.

For the results to be available on Momentic Cloud, add a step to run the
`momentic results upload <folder>` command, supplying the path to the directory
containing the local test results.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results upload test-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results upload test-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results upload test-results
  ```
</CodeGroup>

See the [results](/cli/commands/results) command for more information and
details on merging results for sharding setups.

## Update deprecated commands and flags

* The `--report` and `--no-report` flags are no longer supported.
* Using `CI=true` to upload results is no longer necessary and can be removed
  from CI scripts.
* `momentic import-from-cloud` is deprecated and replaced with
  `momentic import`.
* `momentic check-config` is deprecated and replaced with
  `momentic check config`.

## Update tests relying on automatic tab switching

<Tip>
  Use [Switch Tab](/steps/switch-tab) steps instead of relying on automatic tab
  switching.
</Tip>

In Momentic 2.0, switching to newly opened tabs no longer occurs automatically,
as this behavior is inherently racy and flaky.

If you want to continue using automatic tab switching, you can enable it by
adding the following to your `momentic.config.yaml` file:

```yaml momentic.config.yaml theme={null}
browser:
  autoFollowNewTabs: true
```


Built with [Mintlify](https://mintlify.com).