# Source: https://www.zuplo.com/docs/cli/test.md

# Zuplo CLI: Test

<CliCommand
  command="test"
  description="Runs the tests under /tests against an endpoint"
  options={[
  {
    "name": "endpoint",
    "type": "string",
    "description": "The URL of the Zuplo API to test against",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "filter",
    "type": "string",
    "description": "A filter to run a subset of tests (e.g., --filter 'test name' or --filter '/test-name-regex/')",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "dir",
    "type": "string",
    "description": "The directory containing your Zuplo API",
    "default": ".",
    "required": false,
    "deprecated": false,
    "hidden": true,
    "normalize": true
  }
]}
  examples={[
  [
    "$0 test --endpoint https://your-api-123abc.zuplo.app",
    "Run all tests against your deployed API"
  ],
  [
    "$0 test --endpoint https://your-api-123abc.zuplo.app --filter 'auth'",
    "Run only tests matching 'auth' in their name"
  ],
  [
    "$0 test --endpoint https://your-api-123abc.zuplo.app --filter '/api\\/v1/'",
    "Run tests matching a regex pattern"
  ],
  [
    "MY_VAR=example $0 test --endpoint https://your-api-123abc.zuplo.app",
    "Run tests with environment variables"
  ]
]}
  usage="$0 test --endpoint <url> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)

## Additional resources

- [Testing your API](../articles/testing.mdx)
- [Custom CI/CD](../articles/custom-ci-cd.mdx)
