# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_run.md

---
title: Continuous Testing and Bitrise
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing and CI/CD > Continuous Testing
  and Bitrise
---

# Continuous Testing and Bitrise

 [](https://app.bitrise.io/app/7846c17b-8a1c-4fc7-aced-5f3b0b2ec6c4) [](https://opensource.org/licenses/Apache-2.0)

## Overview{% #overview %}

With the `synthetics-test-automation-bitrise-step-run-tests` step, you can run Synthetic tests during your Bitrise CI, ensuring that all your teams using Bitrise can benefit from Synthetic tests at every stage of the software lifecycle.

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

## Setup{% #setup %}

This step is not available on the official Bitrise Step Library. To get started:

1. Add the following git URL to your workflow. See the [official Bitrise documentation](https://devcenter.bitrise.io/en/steps-and-workflows/introduction-to-steps/adding-steps-to-a-workflow.html#adding-steps-from-alternative-sources) on how to do that though the Bitrise app. You can also configure it locally by referencing the git URL in your `bitrise.yml` file.

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
```
Add your API and application keys to your [secrets in Bitrise](https://devcenter.bitrise.io/en/builds/secrets.html#setting-a-secret).[Configure your step inputs](https://devcenter.bitrise.io/en/steps-and-workflows/introduction-to-steps/step-inputs.html). You can also configure them in your `bitrise.yml` file. The only required inputs are the two secrets you configured earlier. For a comprehensive list of inputs, see the Inputs section.
When running the step locally with the Bitrise CLI, the secrets should be stored in a `.bitrise.secrets.yml` file. See [Managing secrets locally](https://devcenter.bitrise.io/en/bitrise-cli/managing-secrets-locally.html).

## Simple usage{% #simple-usage %}

### Example using public IDs{% #example-using-public-ids %}

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - public_ids: |
      abc-d3f-ghi
      jkl-mn0-pqr
```

### Example task using existing `synthetics.json` files{% #example-task-using-existing-syntheticsjson-files %}

```yaml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - files: 'e2e-tests/*.synthetics.json'
```

For an example test file, see this [`test.synthetics.json` file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).

## Complex usage{% #complex-usage %}

### Example task using the `testSearchQuery`{% #example-task-using-the-testsearchquery %}

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - test_search_query: 'tag:e2e-tests'
```

### Example task using the `testSearchQuery` and variable overrides{% #example-task-using-the-testsearchquery-and-variable-overrides %}

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - test_search_query: 'tag:e2e-tests'
   - variables: |
      START_URL=https://staging.website.com
      PASSWORD=$STAGING_PASSWORD
```

### Example task using a global configuration override with `configPath`{% #example-task-using-a-global-configuration-override-with-configpath %}

This task overrides the path to the global `global.config.json` file.

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - config_path: './global.config.json'
```

### Example including all possible configurations{% #example-including-all-possible-configurations %}

For reference, this is an example of a complete configuration:

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests.git@v3.8.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - batch_timeout: 4200000
   - config_path: './global.config.json'
   - datadog_site: 'datadoghq.com'
   - device_ids: |
      apple iphone se (2022),15.4.1
      apple iphone 14 pro,16.1
   - fail_on_critical_errors: true
   - fail_on_missing_tests: true
   - fail_on_timeout: true
   - files: 'e2e-tests/*.synthetics.json'
   - junit_report: 'e2e-test-junit'
   - locations: 'aws:us-west-1'
   - mobile_application_version: '01234567-8888-9999-abcd-efffffffffff'
   - mobile_application_version_file_path: 'path/to/application.apk'
   - public_ids: 'abc-d3f-ghi,jkl-mn0-pqr'
   - selective_rerun: true
   - subdomain: 'myorg'
   - test_search_query: 'tag:e2e-tests'
   - tunnel: true
   - variables: |
      START_URL=https://staging.website.com
      PASSWORD=$STAGING_PASSWORD
```

## Inputs{% #inputs %}

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

| Name                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `api_key`                              | (**Required**) Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.                                                                                                                                                                                                                                                     |
| `app_key`                              | (**Required**) Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.                                                                                                                                                                                                                                             |
| `batch_timeout`                        | Specifies the timeout duration in milliseconds for the CI batch. When a batch times out, the CI job fails and no new test runs are triggered, but ongoing test runs complete normally.**Default:** `1800000` (30 minutes)                                                                                                                                                                                                                  |
| `config_path`                          | The path to the [global configuration file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#global-configuration-file) that configures datadog-ci.**Default:** `datadog-ci.json`                                                                                                                                                                                                                    |
| `datadog_site`                         | Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).**Default:** `datadoghq.com`Set it to  (ensure the correct SITE is selected on the right).                                                                                                                                                                                                     |
| `device_ids`                           | Override the list of devices on which to run the Synthetic tests, separated by new lines.**Default:** none                                                                                                                                                                                                                                                                                                                                 |
| `fail_on_critical_errors`              | Fail the CI job if a critical error that is typically transient occurs, such as rate limits, authentication failures, or Datadog infrastructure issues.**Default:** `false`                                                                                                                                                                                                                                                                |
| `fail_on_missing_tests`                | Fail the CI job if the list of tests to run is empty or if some explicitly listed tests are missing.**Default:** `false`                                                                                                                                                                                                                                                                                                                   |
| `fail_on_timeout`                      | Fail the CI job if the CI batch fails as timed out.**Default:** `true`                                                                                                                                                                                                                                                                                                                                                                     |
| `files`                                | Glob patterns to detect Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files), separated by new lines.**Default:** `{,!(node_modules)/**/}*.synthetics.json`                                                                                                                                                                                             |
| `junit_report`                         | The filename for a JUnit report if you want to generate one.**Default:** none                                                                                                                                                                                                                                                                                                                                                              |
| `locations`                            | Override the list of locations to run the test from, separated by new lines or commas. The possible values are listed [in this API response](https://app.datadoghq.com/api/v1/synthetics/locations?only_public=true).**Default:** none                                                                                                                                                                                                     |
| `mobile_application_version_file_path` | Override the mobile application version for [Synthetic mobile application tests](https://docs.datadoghq.com/synthetics/mobile_app_testing/) with a local or recently built application. You may use `$BITRISE_IPA_PATH` or `$BITRISE_APK_PATH` from your previous build steps.**Default:** none                                                                                                                                            |
| `mobile_application_version`           | Override the mobile application version for [Synthetic mobile application tests](https://docs.datadoghq.com/synthetics/mobile_app_testing/). The version must be uploaded and available within Datadog. You can use the [Bitrise step to upload an application](https://github.com/DataDog/synthetics-test-automation-bitrise-step-upload-application) and use its `DATADOG_UPLOADED_APPLICATION_VERSION_ID` output here.**Default:** none |
| `public_ids`                           | Public IDs of Synthetic tests to run, separated by new lines or commas. If no value is provided, tests are discovered in Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).**Default:** none                                                                                                                                                         |
| `selective_rerun`                      | Whether to only rerun failed tests. If a test has already passed for a given commit, it is not rerun in subsequent CI batches. By default, your organization's default setting is used. Set it to `false` to force full runs when your configuration enables it by default.**Default:** none                                                                                                                                               |
| `subdomain`                            | The custom subdomain to access your Datadog organization. If the URL used to access Datadog is `myorg.datadoghq.com`, the custom subdomain is `myorg`.**Default:** `app`                                                                                                                                                                                                                                                                   |
| `test_search_query`                    | Use a [search query](https://docs.datadoghq.com/synthetics/search/#search) to select which Synthetic tests to run. Use the [Synthetic Tests list page's search bar](https://app.datadoghq.com/synthetics/tests) to craft your query, then copy and paste it.**Default:** none                                                                                                                                                              |
| `tunnel`                               | Use the [Continuous Testing tunnel](https://docs.datadoghq.com/continuous_testing/environments/proxy_firewall_vpn#what-is-the-testing-tunnel) to launch tests against internal environments.**Default:** `false`                                                                                                                                                                                                                           |
| `variables`                            | Override existing or inject new local and [global variables](https://docs.datadoghq.com/synthetics/platform/settings/?tab=specifyvalue#global-variables) in Synthetic tests as key-value pairs, separated by new lines or commas. For example: `START_URL=https://example.org,MY_VARIABLE=My title`.**Default:** none                                                                                                                      |

## Further reading{% #further-reading %}

Additional helpful documentation, links, and articles:

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing/)
- [Continuous Testing and CI/CD Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
