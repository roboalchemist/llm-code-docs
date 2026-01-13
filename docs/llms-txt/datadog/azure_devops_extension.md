# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/azure_devops_extension.md

---
title: Continuous Testing and Datadog CI Azure DevOps Extension
description: >-
  Use the Synthetics and Datadog CI extension to create tasks that you can use
  in a CI pipeline.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing and CI/CD > Continuous Testing
  and Datadog CI Azure DevOps Extension
source_url: https://docs.datadoghq.com/cicd_integrations/azure_devops_extension/index.html
---

# Continuous Testing and Datadog CI Azure DevOps Extension

[](https://marketplace.visualstudio.com/items?itemName=Datadog.datadog-ci) [](https://dev.azure.com/datadog-ci/Datadog%20CI%20Azure%20DevOps%20Extension/_build/latest?definitionId=4&branchName=main) [](https://opensource.org/licenses/Apache-2.0)

## Overview{% #overview %}

With the [`SyntheticsRunTests`](https://github.com/DataDog/datadog-ci-azure-devops/tree/main/SyntheticsRunTestsTask) task, you can run Synthetic tests within your Azure Pipeline configuration and ensure all your teams using Azure DevOps can benefit from Synthetic tests at every stage of the software lifecycle.

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

## Authentication{% #authentication %}

### Service Connection{% #service-connection %}

To connect to your [Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site), Datadog recommends setting up a custom service connection when configuring the [`SyntheticsRunTests`](https://github.com/DataDog/datadog-ci-azure-devops/tree/main/SyntheticsRunTestsTask) task.

You need to provide the following inputs:

- Datadog site: Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).
- Custom subdomain (default: `app`): The custom subdomain to access your Datadog organization. If your URL is `myorg.datadoghq.com`, the custom subdomain is `myorg`.
- API key: Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/).
- Application key: Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/).

### API and Application keys{% #api-and-application-keys %}

- API key: Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).
- Application key: Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).
- Datadog site: Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).
- Custom subdomain (optional): The custom subdomain to access your Datadog organization. If your URL is `myorg.datadoghq.com`, the custom subdomain is `myorg`.

## Setup{% #setup %}

To connect to your Datadog account, [create a Datadog CI service connection](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints) in your Azure pipelines project. Once created, all you need is the name of the service connection in the tasks.

1. Install the [Datadog Continuous Testing extension from the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Datadog.datadog-ci) in your Azure Organization.
1. Add your Datadog API and application keys in the Datadog CI service connection, or as [secrets to your Azure Pipelines project](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).
1. In your Azure DevOps pipeline, use the [`SyntheticsRunTests`](https://github.com/DataDog/datadog-ci-azure-devops/tree/main/SyntheticsRunTestsTask) task.

Your task can be simple or complex.

## Simple usage{% #simple-usage %}

### Example task using public IDs{% #example-task-using-public-ids %}

```yaml
- task: SyntheticsRunTests@1
  displayName: Run Datadog Synthetic tests
  inputs:
    authenticationType: 'connectedService'
    connectedService: 'my-datadog-ci-connected-service'
    publicIds: |
      abc-d3f-ghi
      jkl-mn0-pqr
```

### Example task using existing `synthetics.json` files{% #example-task-using-existing-syntheticsjson-files %}

```yaml
- task: SyntheticsRunTests@1
  displayName: Run Datadog Synthetic tests
  inputs:
    authenticationType: 'connectedService'
    connectedService: 'my-datadog-ci-connected-service'
    files: 'e2e-tests/*.synthetics.json'
```

For an example test file, see this [`test.synthetics.json` file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).

### Example task using pipeline secrets for authentication{% #example-task-using-pipeline-secrets-for-authentication %}

```yaml
- task: SyntheticsRunTests@1
  inputs:
    authenticationType: 'apiAppKeys'
    apiKey: '$(DatadogApiKey)'
    appKey: '$(DatadogAppKey)'
    datadogSite: '$(DatadogSite)'
    subdomain: 'myorg'
```

## Complex usage{% #complex-usage %}

### Example task using the `testSearchQuery`{% #example-task-using-the-testsearchquery %}

```yaml
- task: SyntheticsRunTests@1
  displayName: Run Datadog Synthetic tests
  inputs:
    authenticationType: 'connectedService'
    connectedService: 'my-datadog-ci-connected-service'
    testSearchQuery: 'tag:e2e-tests'
```

### Example task using the `testSearchQuery` and variable overrides{% #example-task-using-the-testsearchquery-and-variable-overrides %}

```yaml
- task: SyntheticsRunTests@1
  displayName: Run Datadog Synthetic tests
  inputs:
    authenticationType: 'connectedService'
    connectedService: 'my-datadog-ci-connected-service'
    testSearchQuery: 'tag:e2e-tests'
    variables: |
      START_URL=https://staging.website.com
      PASSWORD=$(StagingPassword)
```

### Example task using a global configuration file with `configPath`{% #example-task-using-a-global-configuration-file-with-configpath %}

By default, the path to the global configuration file is `datadog-ci.json`. You can override this path with the `config_path` input.

```yaml
- task: SyntheticsRunTests@1
  displayName: Run Datadog Synthetic tests
  inputs:
    authenticationType: 'connectedService'
    configPath: './global.config.json'
    connectedService: 'my-datadog-ci-connected-service'
```

## Inputs{% #inputs %}

For more information on the available configuration, see the [`datadog-ci synthetics run-tests` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#run-tests-command).

| Name                   | Description                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apiKey`               | Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).**Required** when `authenticationType == apiAppKeys`                                              |
| `appKey`               | Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a [secret](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables).**Required** when `authenticationType == apiAppKeys`                                      |
| `authenticationType`   | (**Required**) How to store and retrieve credentials.Must be either `apiAppKeys` or `connectedService`                                                                                                                                                                                                                                                           |
| `batchTimeout`         | Specifies the timeout duration in milliseconds for the CI batch. When a batch times out, the CI job fails and no new test runs are triggered, but ongoing test runs complete normally.**Default:** `1800000` (30 minutes)                                                                                                                                        |
| `connectedService`     | The name of the Datadog CI service connection.**Required** when `authenticationType == connectedService`                                                                                                                                                                                                                                                         |
| `configPath`           | The path to the [global configuration file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#global-configuration-file) that configures datadog-ci.**Default:** `datadog-ci.json`                                                                                                                                          |
| `datadogSite`          | Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).**Default:** `datadoghq.com`Set it to  (ensure the correct SITE is selected on the right).                                                                                                                           |
| `failOnCriticalErrors` | Fail the CI job if a critical error that is typically transient occurs, such as rate limits, authentication failures, or Datadog infrastructure issues.**Default:** `false`                                                                                                                                                                                      |
| `failOnMissingTests`   | Fail the CI job if the list of tests to run is empty or if some explicitly listed tests are missing.**Default:** `false`                                                                                                                                                                                                                                         |
| `failOnTimeout`        | Fail the CI job if the CI batch fails as timed out.**Default:** `true`                                                                                                                                                                                                                                                                                           |
| `files`                | Glob patterns to detect Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files), separated by new lines.**Default:** `{,!(node_modules)/**/}*.synthetics.json`                                                                                                                   |
| `jUnitReport`          | The filename for a JUnit report if you want to generate one.**Default:** none                                                                                                                                                                                                                                                                                    |
| `locations`            | Override the list of locations to run the test from, separated by new lines or commas. The possible values are listed [in this API response](https://app.datadoghq.com/api/v1/synthetics/locations?only_public=true).**Default:** none                                                                                                                           |
| `publicIds`            | Public IDs of Synthetic tests to run, separated by new lines or commas. If no value is provided, tests are discovered in Synthetic [test configuration files](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#test-files).**Default:** none                                                                               |
| `selectiveRerun`       | Whether to only rerun failed tests. If a test has already passed for a given commit, it is not rerun in subsequent CI batches. By default, your [organization's default setting](https://app.datadoghq.com/synthetics/settings/continuous-testing) is used. Set it to `false` to force full runs when your configuration enables it by default.**Default:** none |
| `subdomain`            | The custom subdomain to access your Datadog organization when `authenticationType == apiAppKeys`. If your URL is `myorg.datadoghq.com`, the custom subdomain is `myorg`.**Default:** `app`                                                                                                                                                                       |
| `testSearchQuery`      | Use a [search query](https://docs.datadoghq.com/synthetics/explore/#search) to select which Synthetic tests to run. Use the [Synthetic Tests list page's search bar](https://app.datadoghq.com/synthetics/tests) to craft your query, then copy and paste it.**Default:** none                                                                                   |
| `variables`            | Override existing or inject new local and [global variables](https://docs.datadoghq.com/synthetics/platform/settings/?tab=specifyvalue#global-variables) in Synthetic tests as key-value pairs, separated by new lines or commas. For example: `START_URL=https://example.org,MY_VARIABLE=My title`.**Default:** none                                            |

## Outputs{% #outputs %}

| Name                     | Description                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `batchUrl`               | The URL of the CI batch.                                                                                                                                                                          |
| `criticalErrorsCount`    | The number of critical errors that occurred during the CI batch.                                                                                                                                  |
| `failedCount`            | The number of results that failed during the CI batch.                                                                                                                                            |
| `failedNonBlockingCount` | The number of results that failed during the CI batch without blocking the CI.                                                                                                                    |
| `passedCount`            | The number of results that passed during the CI batch.                                                                                                                                            |
| `previouslyPassedCount`  | The number of results that already passed in previous CI batches on the same commit.                                                                                                              |
| `testsNotFoundCount`     | The number of tests that could not be found when starting the CI batch.                                                                                                                           |
| `testsSkippedCount`      | The number of tests that were skipped when starting the CI batch.                                                                                                                                 |
| `timedOutCount`          | The number of results that failed due to the CI batch timing out.                                                                                                                                 |
| `rawResults`             | The [`synthetics.Result[]`](https://github.com/DataDog/datadog-ci/blob/251299775d28b0535d0e5557fcc494a8124d3b11/src/commands/synthetics/interfaces.ts#L196-L227) array, as a JSON-encoded string. |

## Further reading{% #further-reading %}

Additional helpful documentation, links, and articles:

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing/)
- [Continuous Testing and CI/CD Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
