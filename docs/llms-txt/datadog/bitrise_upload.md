# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_upload.md

---
title: Continuous Testing and Bitrise
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing and CI/CD > Continuous Testing
  and Bitrise
source_url: https://docs.datadoghq.com/cicd_integrations/bitrise_upload/index.html
---

# Continuous Testing and Bitrise

 [](https://app.bitrise.io/app/2d252b25-8c31-427b-98e8-1d0b2bc484c1) [](https://opensource.org/licenses/Apache-2.0)

## Overview{% #overview %}

With the `synthetics-test-automation-bitrise-step-upload-application` step, you can upload a new version of your application to Datadog to run Synthetic tests against during your Bitrise CI, ensuring that all your teams using Bitrise can benefit from Synthetic tests at every stage of the software lifecycle.

This step requires that your application already exists in Datadog.

For more information on the available configuration, see the [`datadog-ci upload-application` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#upload-application-command).

## Setup{% #setup %}

This step is not available on the official Bitrise Step Library. To get started:

1. Add the following git URL to your workflow. See the [official Bitrise documentation](https://devcenter.bitrise.io/en/steps-and-workflows/introduction-to-steps/adding-steps-to-a-workflow.html#adding-steps-from-alternative-sources) on how to do that though the Bitrise app. You can also configure it locally by referencing the git URL in your `bitrise.yml` file.

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-upload-application.git@v2.7.0:
```
Add your API and application keys to your [secrets in Bitrise](https://devcenter.bitrise.io/en/builds/secrets.html#setting-a-secret).[Configure your step inputs](https://devcenter.bitrise.io/en/steps-and-workflows/introduction-to-steps/step-inputs.html). You can also configure them in your `bitrise.yml` file. The only required inputs are the two secrets you configured earlier. For a comprehensive list of inputs, see the Inputs section.
When running the step locally with the Bitrise CLI, the secrets should be stored in a `.bitrise.secrets.yml` file. See [Managing secrets locally](https://devcenter.bitrise.io/en/bitrise-cli/managing-secrets-locally.html).

## Usage{% #usage %}

### Example task using a global configuration override with `configPath`{% #example-task-using-a-global-configuration-override-with-configpath %}

This task overrides the path to the global `datadog-ci.config.json` file.

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-upload-application.git@v2.7.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - config_path: './synthetics-config.json'
```

### Example including all possible configurations{% #example-including-all-possible-configurations %}

For reference, this is an example of a complete configuration:

```yml
- git::https://github.com/DataDog/synthetics-test-automation-bitrise-step-upload-application.git@v2.7.0:
   inputs:
   - api_key: <DATADOG_API_KEY>
   - app_key: <DATADOG_APP_KEY>
   - config_path: './global.config.json'
   - datadog_site: 'datadoghq.com'
   - latest: true
   - mobile_application_id: '123-123-123'
   - mobile_application_version_file_path: 'path/to/application.apk'
   - version_name: 'example 1.0'
```

## Inputs{% #inputs %}

For more information on the available configuration, see the [`datadog-ci upload-application` documentation](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#upload-application-command).

| Name                                   | Description                                                                                                                                                                                                                            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                              | (**Required**) Your Datadog API key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.                                                 |
| `app_key`                              | (**Required**) Your Datadog application key. This key is [created in your Datadog organization](https://docs.datadoghq.com/account_management/api-app-keys/) and should be stored as a secret.                                         |
| `config_path`                          | The path to the [global configuration file](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration/?tab=npm#global-configuration-file) that configures datadog-ci.**Default:** `datadog-ci.json`                |
| `datadog_site`                         | Your Datadog site. The possible values are listed [in this table](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).**Default:** `datadoghq.com`Set it to  (ensure the correct SITE is selected on the right). |
| `latest`                               | Mark the new version as `latest`. Any tests that run on the latest version will use this version on their next run.**Default:** `false`                                                                                                |
| `mobile_application_id`                | (**Required**) The ID of the application you want to upload the new version to.                                                                                                                                                        |
| `mobile_application_version_file_path` | (**Required**) The path to the new version of your mobile application (`.apk` or `.ipa`). You may use `$BITRISE_IPA_PATH` or `$BITRISE_APK_PATH` from your previous build steps.                                                       |
| `version_name`                         | (**Required**) The name of the new version. It has to be unique.                                                                                                                                                                       |

## Outputs{% #outputs %}

| Name                                      | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DATADOG_UPLOADED_APPLICATION_VERSION_ID` | The version ID of the application that was just uploaded. Pass it to the [Bitrise step to run tests](https://github.com/DataDog/synthetics-test-automation-bitrise-step-run-tests) with the `mobile_application_version` input to test this version of the application. |

## Further reading{% #further-reading %}

Additional helpful documentation, links, and articles:

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing/)
- [Continuous Testing and CI/CD Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)
- [Best practices for continuous testing with Datadog](https://www.datadoghq.com/blog/best-practices-datadog-continuous-testing/)
