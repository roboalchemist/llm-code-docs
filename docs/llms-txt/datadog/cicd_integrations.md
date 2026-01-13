# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations.md

---
title: Continuous Testing and CI/CD
description: >-
  Run Continuous Testing tests on-demand or at predefined intervals in your
  CI/CD pipelines.
breadcrumbs: Docs > Continuous Testing > Continuous Testing and CI/CD
source_url: https://docs.datadoghq.com/cicd_integrations/index.html
---

# Continuous Testing and CI/CD

{% alert level="info" %}
This page is about running Continuous Testing tests in your continuous integration (CI) and continuous delivery (CD) pipelines. If you want to bring your CI/CD metrics and data into Datadog dashboards, see the CI Visibility section.
{% /alert %}

## Overview{% #overview %}

In addition to running tests at predefined intervals, you can reuse your Datadog Synthetic tests and run them on-demand using the `@datadog/datadog-ci` package or the API. Run Datadog Continuous Testing tests in your continuous integration (CI) pipelines to block branches from being deployed and breaking your application in production.

Use Continuous Testing and CI/CD to also run tests as part of your continuous delivery (CD) process and evaluate the state of your applications and services in production immediately after a deployment finishes, or a new release is freshly cut. You can detect potential regressions that may impact your users and automatically trigger a rollback when a critical test fails.

This functionality reduces time spent fixing issues in production by proactively catching bugs and regressions earlier in the process, allowing your engineering teams to focus on non-urgent work instead.

To get started, see Integrations and use the API or the open-source CLI package.

## Integrations{% #integrations %}

- [Azure DevOps Extension](https://docs.datadoghq.com/continuous_testing/cicd_integrations/azure_devops_extension)
- [CircleCI Orb](https://docs.datadoghq.com/continuous_testing/cicd_integrations/circleci_orb)
- [GitHub Actions](https://docs.datadoghq.com/continuous_testing/cicd_integrations/github_actions)
- [GitLab](https://docs.datadoghq.com/continuous_testing/cicd_integrations/gitlab)
- [Jenkins](https://docs.datadoghq.com/continuous_testing/cicd_integrations/jenkins)
- [Upload Applications with Bitrise](https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_upload)
- [Run Tests with Bitrise](https://docs.datadoghq.com/continuous_testing/cicd_integrations/bitrise_run)
- [NPM package](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration)

## Use the CLI{% #use-the-cli %}

The [`@datadog/datadog-ci` package](https://github.com/DataDog/datadog-ci) allows you to run Continuous Testing tests directly within your CI/CD pipeline. To use the [`@datadog/datadog-ci` NPM package](https://www.npmjs.com/package/@datadog/datadog-ci), see [Configuration](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration).

You can trigger tests by searching with tags. For example, use `"ci": "datadog-ci synthetics run-tests --config fileconfig.json -s 'tag:staging'"`. This command works as an argument. Do not use this in your configuration files.

## Use the API{% #use-the-api %}

The Synthetics API endpoints allow you to launch tests at any stage in your staging and deployment lifecycle. For example, after a canary deployment with an automated rollback.

Use the API endpoints to quickly verify that a new deployment does not introduce any regression. See the [Trigger tests from CI/CD pipelines](https://docs.datadoghq.com/api/latest/synthetics/#trigger-tests-from-cicd-pipelines) and [Get details of batch](https://docs.datadoghq.com/api/latest/synthetics/#get-details-of-batch) endpoints to use them within your CI through cURL or a supported client.

### Trigger tests from CI/CD pipelines{% #trigger-tests-from-cicd-pipelines %}

The test triggering endpoint supports up to 100 tests in one request.

- **Endpoint**: `https://api.  /api/v1/synthetics/tests/trigger/ci`
- **Method**: `POST`
- **Argument**: A JSON object containing the list of all tests to trigger and their configuration override.

#### Request data structure{% #request-data-structure %}

```json
{
    "tests": [TEST_TO_TRIGGER, TEST_TO_TRIGGER, ...]
}
```

The `TEST_TO_TRIGGER` objects compose of the required `public_id` for the test you want to trigger and the optional configuration overrides. For descriptions of each field, see [Configure tests](https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration#configure-tests).

A test's public identifier is either the identifier of the test found in the URL of a test's details page (for example: the identifier for `https://app.datadoghq.com/synthetics/details/abc-def-ghi` is `abc-def-ghi`) or the full URL of a test's details page (for example: `https://app.datadoghq.com/synthetics/details/abc-def-ghi`).

For more information, see the [Synthetics API endpoint documentation](https://docs.datadoghq.com/api/latest/synthetics/#trigger-tests-from-cicd-pipelines).

### Get details of batch{% #get-details-of-batch %}

The get batch details endpoint retrieves results for the group of tests triggered in your CI/CD pipeline, otherwise known as a batch. You must provide the `batch_id` for the relevant CI execution.

- **Endpoint**: `https://api.  /api/v1/synthetics/ci/batch/{batch_id}`
- **Method**: `GET`
- **Parameters**: The `batch_id` for the batch of test results you want to inspect.

For more information, see the [Synthetics API endpoint documentation](https://docs.datadoghq.com/api/latest/synthetics/#get-details-of-batch).

## Further Reading{% #further-reading %}

- [Incorporate Datadog Synthetic tests into your CI/CD pipeline](https://www.datadoghq.com/blog/datadog-synthetic-ci-cd-testing/)
- [Best practices for shift-left testing](https://www.datadoghq.com/blog/shift-left-testing-best-practices/)
- [Learn how to run Synthetic tests in a CI/CD pipeline](https://learn.datadoghq.com/courses/synthetic-tests-ci-cd-pipeline)
- [Learn how to configure an API test](https://docs.datadoghq.com/synthetics/api_tests/)
- [Learn how to configure a multistep API test](https://docs.datadoghq.com/synthetics/multistep)
- [Learn how to configure a browser test](https://docs.datadoghq.com/synthetics/browser_tests/)
