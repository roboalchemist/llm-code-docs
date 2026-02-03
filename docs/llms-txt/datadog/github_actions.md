# Source: https://docs.datadoghq.com/security/code_security/static_analysis/github_actions.md

# Source: https://docs.datadoghq.com/security/code_security/secret_scanning/github_actions.md

# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/github_actions.md

---
title: Continuous Testing and CI GitHub Actions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing and CI/CD > Continuous Testing
  and CI GitHub Actions
---

# Continuous Testing and CI GitHub Actions

## Overview{% #overview %}



Trigger Datadog Synthetic tests from your GitHub workflows.

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

## Setup{% #setup %}

To get started:

1. Add your Datadog API and Application Keys as secrets to your GitHub repository.
   - For more information, see [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/).
1. In your GitHub workflow, use `DataDog/synthetics-ci-github-action`.

Your workflow can be simple or complex.

## Simple workflows{% #simple-workflows %}

### Example workflow using public IDs{% #example-workflow-using-public-ids %}

```yaml
name: Run Synthetic tests using the test public IDs
jobs:
  e2e_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Datadog Synthetic tests
        uses: DataDog/synthetics-ci-github-action@v3.8.2
        with:
          api-key: ${{secrets.DD_API_KEY}}
          app-key: ${{secrets.DD_APP_KEY}}
          public-ids: |
            abc-d3f-ghi
            jkl-mn0-pqr
```

### Example workflow using an existing `synthetics.json` file{% #example-workflow-using-an-existing-syntheticsjson-file %}

```yaml
name: Run Synthetic tests using an existing synthetics.json file
jobs:
  e2e_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Datadog Synthetic tests
        uses: DataDog/synthetics-ci-github-action@v3.8.2
        with:
          api-key: ${{secrets.DD_API_KEY}}
          app-key: ${{secrets.DD_APP_KEY}}
```

For an example test file, see this [`test.synthetics.json` file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).

**Note**: By default, this workflow runs all the tests listed in `{,!(node_modules)/**/}*.synthetics.json` files (every file ending with `.synthetics.json` except for those in the `node_modules` folder). You can also trigger a list of Synthetic tests by specifying a `public_id` or using a search query.

## Complex workflows{% #complex-workflows %}

### Example workflow using the `test_search_query`{% #example-workflow-using-the-test_search_query %}

```yaml
name: Run Synthetic tests by test tag
jobs:
  e2e_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Datadog Synthetic tests
        uses: DataDog/synthetics-ci-github-action@v3.8.2
        with:
          api-key: ${{secrets.DD_API_KEY}}
          app-key: ${{secrets.DD_APP_KEY}}
          test-search-query: 'tag:e2e-tests'
```

### Example workflow using a test search query and variable overrides{% #example-workflow-using-a-test-search-query-and-variable-overrides %}

```yaml
name: Run Synthetic tests using search query
jobs:
  e2e_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Datadog Synthetic tests
        uses: DataDog/synthetics-ci-github-action@v3.8.2
        with:
          api-key: ${{secrets.DD_API_KEY}}
          app-key: ${{secrets.DD_APP_KEY}}
          test-search-query: 'tag:staging'
          variables: 'START_URL=https://staging.website.com,PASSWORD=stagingpassword'
```

### Example workflow using a global configuration file with `config_path`{% #example-workflow-using-a-global-configuration-file-with-config_path %}

By default, the path to the global configuration file is `datadog-ci.json`. You can override this path with the `config_path` input.

```yaml
name: Run Synthetic tests with custom config
jobs:
  e2e_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run Datadog Synthetic tests
        uses: DataDog/synthetics-ci-github-action@v3.8.2
        with:
          api-key: ${{secrets.DD_API_KEY}}
          app-key: ${{secrets.DD_APP_KEY}}
          config-path: './global.config.json'
```

## Inputs{% #inputs %}

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api-key`                 | (**Required**) Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.github.com/en/actions/reference/encrypted-secrets).                                                                                                         |
| `app-key`                 | (**Required**) Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.github.com/en/actions/reference/encrypted-secrets).                                                                                                 |
| `batch-timeout`           | Specifies the timeout duration in milliseconds for the CI batch. When a batch times out, the CI job fails and no new test runs are triggered, but ongoing test runs complete normally.**Default:** `1800000` (30 minutes)                                                                                                                                        |
| `config-path`             | The path to the [global configuration file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#global-configuration-file) that configures datadog-ci.**Default:** `datadog-ci.json`                                                                                                                                          |
| `datadog-site`            | Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).**Default:** `datadoghq.com`Set it to  (ensure the correct SITE is selected on the right).                                                                                                                           |
| `fail-on-critical-errors` | Fail the CI job if a critical error that is typically transient occurs, such as rate limits, authentication failures, or Datadog infrastructure issues.**Default:** `false`                                                                                                                                                                                      |
| `fail-on-missing-tests`   | Fail the CI job if the list of tests to run is empty or if some explicitly listed tests are missing.**Default:** `false`                                                                                                                                                                                                                                         |
| `fail-on-timeout`         | Fail the CI job if the CI batch fails as timed out.**Default:** `true`                                                                                                                                                                                                                                                                                           |
| `files`                   | Glob patterns to detect Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files), separated by new lines.**Default:** `{,!(node_modules)/**/}*.synthetics.json`                                                                                                                   |
| `junit-report`            | The filename for a JUnit report if you want to generate one.**Default:** none                                                                                                                                                                                                                                                                                    |
| `locations`               | Override the list of locations to run the test from, separated by new lines or commas. The possible values are listed [in this API response](https://app.datadoghq.com/api/v1/synthetics/locations?only_public=true).**Default:** none                                                                                                                           |
| `public-ids`              | Public IDs of Synthetic tests to run, separated by new lines or commas. If no value is provided, tests are discovered in Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).**Default:** none                                                                               |
| `selective-rerun`         | Whether to only rerun failed tests. If a test has already passed for a given commit, it is not rerun in subsequent CI batches. By default, your [organization's default setting](https://app.datadoghq.com/synthetics/settings/continuous-testing) is used. Set it to `false` to force full runs when your configuration enables it by default.**Default:** none |
| `subdomain`               | The custom subdomain to access your Datadog organization. If your URL is `myorg.datadoghq.com`, the custom subdomain is `myorg`.**Default:** `app`                                                                                                                                                                                                               |
| `test-search-query`       | Use a [search query](https://docs.datadoghq.com/synthetics/explore/#search) to select which Synthetic tests to run. Use the [Synthetic Tests list page's search bar](https://app.datadoghq.com/synthetics/tests) to craft your query, then copy and paste it.**Default:** none                                                                                   |
| `tunnel`                  | Use the [Continuous Testing tunnel](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn#what-is-the-testing-tunnel) to launch tests against internal environments.**Default:** `false`                                                                                                                                                 |
| `variables`               | Override existing or inject new local and [global variables](https://docs.datadoghq.com/synthetics/platform/settings/?tab=specifyvalue#global-variables) in Synthetic tests as key-value pairs, separated by new lines or commas. For example: `START_URL=https://example.org,MY_VARIABLE=My title`.**Default:** none                                            |

## Outputs{% #outputs %}

| Name                        | Description                                                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `batch-url`                 | The URL of the CI batch.                                                                                                                                                                          |
| `critical-errors-count`     | The number of critical errors that occurred during the CI batch.                                                                                                                                  |
| `failed-count`              | The number of results that failed during the CI batch.                                                                                                                                            |
| `failed-non-blocking-count` | The number of results that failed during the CI batch without blocking the CI.                                                                                                                    |
| `passed-count`              | The number of results that passed during the CI batch.                                                                                                                                            |
| `previously-passed-count`   | The number of results that already passed in previous CI batches on the same commit.                                                                                                              |
| `tests-not-found-count`     | The number of tests that could not be found when starting the CI batch.                                                                                                                           |
| `tests-skipped-count`       | The number of tests that were skipped when starting the CI batch.                                                                                                                                 |
| `timed-out-count`           | The number of results that failed due to the CI batch timing out.                                                                                                                                 |
| `raw-results`               | The [`synthetics.Result[]`](https://github.com/DataDog/datadog-ci/blob/251299775d28b0535d0e5557fcc494a8124d3b11/src/commands/synthetics/interfaces.ts#L196-L227) array, as a JSON-encoded string. |

## Contributing{% #contributing %}

See CONTRIBUTING.md

## Further reading{% #further-reading %}

Additional helpful documentation, links, and articles:

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing/)
- [Continuous Testing and CI/CD Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
