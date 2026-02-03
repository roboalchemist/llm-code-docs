# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/circleci_orb.md

---
title: Continuous Testing and CircleCI Orb
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing and CI/CD > Continuous Testing
  and CircleCI Orb
---

# Continuous Testing and CircleCI Orb

## Overview{% #overview %}

[](https://circleci.com/gh/DataDog/synthetics-test-automation-circleci-orb) [](https://circleci.com/orbs/registry/orb/datadog/synthetics-ci-orb) [](https://raw.githubusercontent.com/DataDog/synthetics-ci-orb/main/LICENSE) [](https://discuss.circleci.com/c/ecosystem/orbs)

Run Datadog Synthetic tests in your CircleCI pipelines using the Datadog CircleCI orb.

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

## Setup{% #setup %}

To get started:

1. Add your Datadog API and application keys as environment variables to your CircleCI project.
   - For more information, see [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/).
1. Ensure the image running the orb is a Linux-x64-based image with `curl` installed.
1. Customize your CircleCI workflow by adding a `synthetics-ci/run-tests` step and specifying inputs as listed below.

Your workflow can be simple or complex.

## Simple usage{% #simple-usage %}

### Example orb usage using public IDs{% #example-orb-usage-using-public-ids %}

```yml
version: 2.1

orbs:
  synthetics-ci: datadog/synthetics-ci-orb@5.3.0

jobs:
  e2e-tests:
    docker:
      - image: cimg/base:stable
    steps:
      - synthetics-ci/run-tests:
          public_ids: |
            abc-d3f-ghi
            jkl-mn0-pqr

workflows:
  run-tests:
    jobs:
      - e2e-tests
```

### Example orb usage using a global configuration override{% #example-orb-usage-using-a-global-configuration-override %}

This orb overrides the path to the pattern for [test files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).

```yml
version: 2.1

orbs:
  synthetics-ci: datadog/synthetics-ci-orb@5.3.0

jobs:
  e2e-tests:
    docker:
      - image: cimg/base:stable
    steps:
      - synthetics-ci/run-tests:
          files: e2e-tests/*.synthetics.json

workflows:
  run-tests:
    jobs:
      - e2e-tests
```

For another example pipeline that triggers Synthetic tests, see the [`simple-example.yml` file](https://github.com/DataDog/synthetics-test-automation-circleci-orb/blob/main/src/examples/simple-example.yml).

## Complex usage{% #complex-usage %}

### Example orb usage using the `test_search_query`{% #example-orb-usage-using-the-test_search_query %}

```yml
version: 2.1

orbs:
  synthetics-ci: datadog/synthetics-ci-orb@5.3.0

jobs:
  e2e-tests:
    docker:
      - image: cimg/base:stable
    steps:
      - synthetics-ci/run-tests:
          test_search_query: 'tag:e2e-tests'

workflows:
  run-tests:
    jobs:
      - e2e-tests
```

### Example orb usage using the [Continuous Testing tunnel](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn#what-is-the-testing-tunnel){% #example-orb-usage-using-the-continuous-testing-tunnel %}

```yml
version: 2.1

orbs:
  synthetics-ci: datadog/synthetics-ci-orb@5.3.0

jobs:
  e2e-tests:
    docker:
      - image: your-image
    steps:
      - checkout
      - run:
          name: Running server in background
          command: npm start
          background: true
      - synthetics-ci/run-tests:
          config_path: tests/tunnel-config.json
          files: tests/*.synthetics.json
          test_search_query: 'tag:e2e-tests'
          tunnel: true

workflows:
  test-server:
    jobs:
      - build-image
      - integration-tests:
          requires:
            - build-image
```

For additional options such as customizing the `batchTimeout` for your CircleCI pipelines, see [CI/CD Integrations Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration). For another example pipeline that starts a local server and triggers Synthetic tests using the Continuous Testing tunnel, see the [`advanced-example.yml` file](https://github.com/DataDog/synthetics-test-automation-circleci-orb/blob/main/src/examples/advanced-example.yml).

## Inputs{% #inputs %}

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                 | Name of the environment variable containing your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.**Default:** `DATADOG_API_KEY`                                                                                                                |
| `app_key`                 | Name of the environment variable containing your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.**Default:** `DATADOG_APP_KEY`                                                                                                        |
| `background`              | Whether or not this step should run in the background. [See official CircleCI documentation](https://circleci.com/docs/configuration-reference/#background-commands).**Default:** `false`                                                                                                                                                                        |
| `batch_timeout`           | Specifies the timeout duration in milliseconds for the CI batch. When a batch times out, the CI job fails and no new test runs are triggered, but ongoing test runs complete normally.**Default:** `1800000` (30 minutes)                                                                                                                                        |
| `config_path`             | The path to the [global configuration file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#global-configuration-file) that configures datadog-ci.**Default:** `datadog-ci.json`                                                                                                                                          |
| `datadog_site`            | Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).**Default:** `datadoghq.com`Set it to  (ensure the correct SITE is selected on the right).                                                                                                                           |
| `fail_on_critical_errors` | Fail the CI job if a critical error that is typically transient occurs, such as rate limits, authentication failures, or Datadog infrastructure issues.**Default:** `false`                                                                                                                                                                                      |
| `fail_on_missing_tests`   | Fail the CI job if the list of tests to run is empty or if some explicitly listed tests are missing.**Default:** `false`                                                                                                                                                                                                                                         |
| `fail_on_timeout`         | Fail the CI job if the CI batch fails as timed out.**Default:** `true`                                                                                                                                                                                                                                                                                           |
| `files`                   | Glob patterns to detect Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files), separated by new lines.Default: `{,!(node_modules)/**/}*.synthetics.json`                                                                                                                       |
| `junit_report`            | The filename for a JUnit report if you want to generate one.Default: none                                                                                                                                                                                                                                                                                        |
| `locations`               | Override the list of locations to run the test from, separated by new lines or commas. The possible values are listed [in this API response](https://app.datadoghq.com/api/v1/synthetics/locations?only_public=true).**Default:** none                                                                                                                           |
| `no_output_timeout`       | Elapsed time the command can run without output. The string is a decimal with unit suffix, such as `20m`, `1.25h`, `5s`. [See official CircleCI documentation](https://circleci.com/docs/configuration-reference/#run).**Default:** `35m`                                                                                                                        |
| `public_ids`              | Public IDs of Synthetic tests to run, separated by new lines or commas. If no value is provided, tests are discovered in Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).**Default:** none                                                                               |
| `selective_rerun`         | Whether to only rerun failed tests. If a test has already passed for a given commit, it is not rerun in subsequent CI batches. By default, your [organization's default setting](https://app.datadoghq.com/synthetics/settings/continuous-testing) is used. Set it to `false` to force full runs when your configuration enables it by default.**Default:** none |
| `subdomain`               | The custom subdomain to access your Datadog organization. If your URL is `myorg.datadoghq.com`, the custom subdomain is `myorg`.**Default:** `app`                                                                                                                                                                                                               |
| `test_search_query`       | Use a [search query](https://docs.datadoghq.com/synthetics/explore/#search) to select which Synthetic tests to run. Use the [Synthetic Tests list page's search bar](https://app.datadoghq.com/synthetics/tests) to craft your query, then copy and paste it.**Default:** none                                                                                   |
| `tunnel`                  | Use the [Continuous Testing tunnel](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn#what-is-the-testing-tunnel) to launch tests against internal environments.**Default:** `false`                                                                                                                                                 |
| `variables`               | Override existing or inject new local and [global variables](https://docs.datadoghq.com/synthetics/platform/settings/?tab=specifyvalue#global-variables) in Synthetic tests as key-value pairs, separated by new lines or commas. For example: `START_URL=https://example.org,MY_VARIABLE=My title`.**Default:** none                                            |

## Further reading{% #further-reading %}

Additional helpful documentation, links, and articles:

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing/)
- [Continuous Testing and CI/CD Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
