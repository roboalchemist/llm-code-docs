# Source: https://momentic.ai/docs/mobile-cli/commands/run.md

# Source: https://momentic.ai/docs/cli/commands/run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# run

<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

Run Momentic tests in the current project.

By default, tests will output results to a local directory. You can then upload
results to Momentic Cloud using the `momentic results upload`
[command](/cli/commands/results).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to run. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `--disable-cache`

Disable caching entirely. This will cause all steps to run without cached data,
and not save caches after runs. This can result in slower test execution, but
ensures that all steps are run fresh without stored data.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --disable-cache
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --filter workspace-name
  ```
</CodeGroup>

### `--custom-headers <customHeaders...>`

Custom headers to include in the test run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

### `--input-csv <inputCsv>`

Path to a CSV file containing input data for the tests. Each row in the CSV file
will be used as input for a separate test run.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --input-csv path/to/input.csv
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --input-csv path/to/input.csv
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --input-csv path/to/input.csv
  ```
</CodeGroup>

### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the test in. This will override any environment specified
by the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --env env-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --env env-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --env env-name
  ```
</CodeGroup>

### `--name <suiteName>`

A name to assign to the test suite. This will be the suite name in generated
reports and will also be displayed in Momentic Cloud if results are uploaded.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash yarn theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash pnpm theme={null}
  npx momentic run --name my-test-suite
  ```
</CodeGroup>

### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --url-override https://example.com
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --url-override https://example.com
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --url-override https://example.com
  ```
</CodeGroup>

### `--save-cache`

Always save updated step caches after successful test runs, even on the main Git
branch and protected Git branches. Please see the
[cache saving eligibility](/step-cache#cache-saving-eligibility) documentation
for more information.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --save-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --save-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --save-cache
  ```
</CodeGroup>

### `--regenerate-cache`

Run the test without using any existing caches. Running with this option will
still save step caches at the end of the run. This can be useful for updating
caches after changing a configuration option.

Warning: using this option will cause all steps to run without any cached data,
resulting in significantly longer execution times. This option should not be
used on an ongoing basis.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --regenerate-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --regenerate-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --regenerate-cache
  ```
</CodeGroup>

### `--start <start>`

A command to run before starting the test. This can be used to start a local
server or any other command that needs to be run before the test starts.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --start "npm run start"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --start "yarn start"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --start "pnpm start"
  ```
</CodeGroup>

### `--upload-results`

Upload test results to Momentic cloud after the test run. This is the same as
running `momentic results upload <outputDir>` after the test run, where
`<outputDir>` is the directory specified by the `--output-dir` option or
`./test-results` if not specified.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --upload-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --upload-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --upload-results
  ```
</CodeGroup>

### `--wait-on <waitOn>`

The resource to wait for before starting the test. This can be a URL, a file, or
any other resource that can be waited on. This is useful for ensuring that the
resource is available before starting the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000
  ```
</CodeGroup>

### `--wait-on-proxy <waitOnProxy>`

HTTP proxy to use when polling the `--wait-on` resource. Provide the full proxy
URL, including protocol, optional credentials, host, and port.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```
</CodeGroup>

### `--wait-on-timeout <waitOnTimeout>`

The timeout for the `--wait-on` option. If the resource is not available within
this time, the test will fail.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```
</CodeGroup>

### `--retries <retries>`

The number of times to retry a test if it fails.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --retries 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --retries 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --retries 3
  ```
</CodeGroup>

### `-p, --parallel <parallel>`

The number of tests to run in parallel. This can be useful for speeding up test
execution, especially for large test suites. Each test will start its own
browser instance.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --parallel 5
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --parallel 5
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --parallel 5
  ```
</CodeGroup>

### `--timeout-minutes <timeoutMinutes>`

Maximum number of minutes to run tests before stopping. When the timeout is
reached, any currently running tests will be stopped, results will be written to
disk, and a summary will be printed. The process will exit with code 1. This is
useful for CI pipelines where you want to enforce a maximum execution time.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --timeout-minutes 30
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --timeout-minutes 30
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --timeout-minutes 30
  ```
</CodeGroup>

### `--labels <labels...>`

Run tests with the specified labels. This allows you to filter tests based on
assigned labels.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --labels smoke regression
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --labels smoke regression
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --labels smoke regression
  ```
</CodeGroup>

### `--update-golden-files`

Update the golden files for [Visual diff](/steps/visual-diff).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --update-golden-files
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --update-golden-files
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --update-golden-files
  ```
</CodeGroup>

### `--reporter <reporter>`

Specify the reporter to use for the output.

Options:

* `junit`
* `allure-json`
* `playwright-json`
* `buildkite-json`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter junit
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter junit
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter junit
  ```
</CodeGroup>

### `--reporter-dir <reporterDir>`

Specify the directory where the reporter output will be saved. If not specified,
it defaults to `./reports`.

Reporter filenames are based on the suite name. For example, `junit` writes
`{suiteName}.xml` and `buildkite-json` writes `{suiteName}.buildkite.json`.

The suite name comes from `--name` when provided. Otherwise, Momentic uses the
detected project's `name` from `momentic.config.yaml`.

For `buildkite-json`, `scope` comes from the suite name and `name` comes from
the individual test name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter-dir ./reports
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter-dir ./reports
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter-dir ./reports
  ```
</CodeGroup>

### `--output-dir <outputDir>`

Directory to store run artifacts such as screenshots, results, and logs. This
directory will be cleared at the start of execution. If not specified, it
defaults to `./test-results`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --output-dir ./output
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --output-dir ./output
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --output-dir ./output
  ```
</CodeGroup>

### `--shard-index <shardIndex>`

The index of the shard to run. This is used in conjunction with `--shard-count`
to determine which tests to run in this shard. This is useful for running tests
in parallel across multiple machines or processes. The index starts at 1.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --shard-index 1 --shard-count 3
  ```
</CodeGroup>

### `--shard-count <shardCount>`

The total number of shards to run. This is used in conjunction with
`--shard-index` to determine which tests to run in this shard. For example, if
you have 3 shards and you set `--shard-index` to 1, only the tests that belong
to the first shard will be executed.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --shard-index 1 --shard-count 3
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --exclude "billing*"
  ```
</CodeGroup>

### `--skip-quarantined`

Skip quarantined tests entirely. By default, quarantined tests will run, but
their statuses won't impact pipeline success or the exit code of the process.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --skip-quarantined
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --skip-quarantined
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --skip-quarantined
  ```
</CodeGroup>

### `--only-quarantined`

Run only quarantined tests. Only quarantined tests will be executed and their
statuses will impact the pipeline success and the exit code of the process.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --only-quarantined
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --only-quarantined
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --only-quarantined
  ```
</CodeGroup>

### `--ignore-quarantine`

Run all tests and apply their statuses to the pipeline success and exit code.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --ignore-quarantine
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --ignore-quarantine
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --ignore-quarantine
  ```
</CodeGroup>

### `--record-video`

Record videos of test runs. Enabling this option will increase the size of
results. Once results are uploaded, the videos can be viewed in the run viewer.
In order to use this flag, ffmpeg must be installed on the machine. This can be
done using the `momentic install-browsers ffmpeg` command.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --record-video
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --record-video
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --record-video
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).