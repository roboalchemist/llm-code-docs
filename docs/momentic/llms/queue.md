# Source: https://momentic.ai/docs/cli/commands/queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# queue

<Info>
  **Prerequisites**: These tests and suites must exist in Momentic Cloud.
</Info>

Queue tests and suites to run in Cloud on Momentic infrastructure.

## `tests`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests [options] <tests...>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests [options] <tests...>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests [options] <tests...>
  ```
</CodeGroup>

* **\<tests...>**: The names of the tests to run. You can specify multiple
  tests separated by spaces.

### Options

#### `--custom-headers <customHeaders...>`

Custom headers to include in the test run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

#### `--input-csv <inputCsv>`

Path to a CSV file containing input data for the tests. Each row in the CSV file
will be used as input for a separate test run.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --input-csv path/to/input.csv
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --input-csv path/to/input.csv
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --input-csv path/to/input.csv
  ```
</CodeGroup>

#### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the test in. This will override any environment specified
by the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --env env-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --env env-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --env env-name
  ```
</CodeGroup>

#### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --url-override https://example.com
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --url-override https://example.com
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --url-override https://example.com
  ```
</CodeGroup>

#### `-w, --wait`

Wait for the test run to complete before exiting.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --wait
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --wait
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --wait
  ```
</CodeGroup>

#### `--wait-timeout <waitTimeout>`

Default: `1800`

The maximum time to wait for the test run to complete, in seconds. Must be used
with the `--wait` option. If the test run does not complete within this time,
the command will exit with an error.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --wait --wait-timeout 600
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --wait --wait-timeout 600
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --wait --wait-timeout 600
  ```
</CodeGroup>

## `suites`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue suites [options] <suites...>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue suites [options] <suites...>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue suites [options] <suites...>
  ```
</CodeGroup>

* **\<suites...>**: The names of the suites to run. You can specify multiple
  suites separated by spaces.

### Options

#### `--custom-headers <customHeaders...>`

Custom headers to include in the suite run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

#### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the suite in. This will override any environment
specified by the suite.

```bash  theme={null}
momentic queue suites --env env-name
```

#### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

```bash  theme={null}
momentic queue suites --url-override https://example.com
```

#### `-w, --wait`

Wait for the suite run to complete before exiting.

```bash  theme={null}
momentic queue suites --wait
```

#### `--wait-timeout <waitTimeout>`

Default: `1800`

The maximum time to wait for the suite run to complete, in seconds. Must be used
with the `--wait` option. If the test run does not complete within this time,
the command will exit with an error.

```bash  theme={null}
momentic queue suites --wait --wait-timeout 600
```


Built with [Mintlify](https://mintlify.com).