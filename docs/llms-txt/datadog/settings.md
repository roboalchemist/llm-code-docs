# Source: https://docs.datadoghq.com/incident_response/case_management/settings.md

# Source: https://docs.datadoghq.com/continuous_testing/settings.md

---
title: Continuous Testing Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Testing > Continuous Testing Settings
---

# Continuous Testing Settings

## Overview{% #overview %}

You can access Continuous Testing settings on the [Synthetic Monitoring & Testing Settings page](https://docs.datadoghq.com/synthetics/settings/).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/settings/parallelization.92597a9358f2f264d21398e013d5759a.png?auto=format"
   alt="Set parallelization for your Continuous Testing tests on the Settings page" /%}

By default, all your tests running in CI/CD pipelines run sequentially (one after the other). To change this behavior, set a parallelization value and save your selection.

## Parallelization{% #parallelization %}

Parallel tests are tests that run simultaneously in your [continuous integration and continuous delivery (CI/CD) pipelines](https://docs.datadoghq.com/continuous_testing/cicd_integrations).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/parallelization_explained.655bbc293142ea107a8963afa682b6ea.png?auto=format"
   alt="A diagram that explains the benefits of parallelization vs. sequential test runs" /%}

This ensures you can:

- Reduce pipeline duration and ship new features faster
- Increase development confidence and speed of delivery
- Have complete test coverage and reduce the volume of production-breaking bugs from reaching your codebase

### Estimate parallelization{% #estimate-parallelization %}

Click **Estimate Parallelization** to see how many tests Datadog recommends running in parallel based on your [Continuous Testing metrics](https://docs.datadoghq.com/synthetics/metrics/#continuous-testing).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/estimated_parallelization.5e0fcba7bd006f63930d939091ca5883.png?auto=format"
   alt="Completing the Estimate Parallelization wizard in Continuous Testing Settings" /%}

After specifying the expected duration for testing in your CI pipeline and, optionally, the average number of tests per CI batch, the **Estimated Parallelization** section calculates the amount of parallelization you want to set:

$$\text"estimated parallelization" = {\text"average numbers of tests per CI batch" * \text"average test duration"} / \text"expected duration in your CI pipeline"$$

### Set parallelization{% #set-parallelization %}

1. Under **Set your preferences**, select the **Parallelization** option.
1. Customize the parallelization you need based on how many tests you want to run in parallel.
1. Click **Save Selection**.
1. Confirm your selection.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/settings/parallelization.92597a9358f2f264d21398e013d5759a.png?auto=format"
   alt="Parallelization settings for 25 parallel Continuous Testing test runs" /%}

## Permissions{% #permissions %}

In order to customize the parallelization for Continuous Testing, you must have the `billing_edit` permission.

Otherwise, the following error displays: `You're missing edit permission for Continuous Testing settings. You can run your tests with a parallelization of X (up to X tests running at the same time at a given point during your CI). To increase this value, reach out to your administrator admin.email@datadoghq.com`.

For more information, see [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#billing-and-usage).

## Further reading{% #further-reading %}

- [Integrate your Continuous Testing tests in your CI/CD pipelines](https://docs.datadoghq.com/continuous_testing/cicd_integrations)
- [Configure an API Test](https://docs.datadoghq.com/synthetics/api_tests/)
- [Configure a Browser Test](https://docs.datadoghq.com/synthetics/browser_tests/)
- [Configure a Mobile App Test](https://docs.datadoghq.com/mobile_app_testing/mobile_app_tests/)
- [Explore RUM & Session Replay in Synthetics](https://docs.datadoghq.com/synthetics/guide/explore-rum-through-synthetics/)
- [Create and manage tests with Terraform](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/synthetics_test)
