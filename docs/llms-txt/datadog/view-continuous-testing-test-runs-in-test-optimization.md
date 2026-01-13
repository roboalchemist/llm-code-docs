# Source: https://docs.datadoghq.com/continuous_testing/guide/view-continuous-testing-test-runs-in-test-optimization.md

---
title: View Continuous Testing Test Runs in Test Optimization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Testing > Continuous Testing Guides > View Continuous
  Testing Test Runs in Test Optimization
source_url: >-
  https://docs.datadoghq.com/guide/view-continuous-testing-test-runs-in-test-optimization/index.html
---

# View Continuous Testing Test Runs in Test Optimization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Mobile Application Testing is not supported on this [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}

## Overview{% #overview %}

[Continuous Testing](https://docs.datadoghq.com/continuous_testing/) enables you to run [Synthetic Monitoring tests](https://docs.datadoghq.com/synthetics/) within your CI/CD pipelines, automating software testing throughout your product's lifecycle. [Test Optimization](https://docs.datadoghq.com/tests/) provides a test-first view into your CI health by displaying important metrics and results from your tests.

You can use Test Optimization to view Continuous Testing test runs, giving you a unified overview of metrics and results from all your test frameworks, including Synthetic Monitoring, in one place.

## View Continuous Testing test runs in Test Optimization{% #view-continuous-testing-test-runs-in-test-optimization %}

1. Navigate to the [Test Runs](https://app.datadoghq.com/ci/test/runs) Explorer in Test Optimization.
1. Filter the **Test Framework** facet to **synthetics**:

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/guide/view-continuous-testing-test-runs-in-test-optimization/test_optimization_test_run_explorer_3.c3e3b29cf3dcba1c333141b7362b7e2e.png?auto=format"
   alt="Test Optimization Test Runs explorer, filtered to synthetics framework facet" /%}

Use this feature to search, filter, and analyze Continuous Testing test runs, combining both Test Optimization and Continuous Testing metadata in a single view.

For example:

- Use the **Flaky**, **New Flaky**, and **Known Flaky** facets to identify flaky test runs.
- Use the **Synthetics Teams** facet to analyze test run status and performance by team.
- Click **Export** and include the **@test.name** column to export a list of test runs and their names.

Select a Continuous Testing test run in the Test Optimization Explorer to view detailed information about that test run:

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/guide/view-continuous-testing-test-runs-in-test-optimization/test_optimization_test_run_detail.41f4ff08f61adbc9955e3f9c1de0cd00.png?auto=format"
   alt="Test Optimization Test Runs details view" /%}

Use these tabs on the side panel:

- **Overview**: Troubleshoot a flaky test by viewing the first and last commit it flaked.
- **History**: Visualize past runs by status and branch.
- **Performance**: Track the mean, minimum, maximum, p95, and trends for test run durations over time.

## Viewing test runs{% #viewing-test-runs %}

From the Test Optimization Explorer, you can jump to a test run in the Synthetic Monitoring page. Click **View in Synthetics** from the details panel of a test run on the Test Optimization page.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/guide/view-continuous-testing-test-runs-in-test-optimization/view_in_synthetics.7544b588cb08c2702c4a9250c45928e9.png?auto=format"
   alt="Test Optimization Test Runs details view, highlighting View in Synthetics button" /%}

Similarly, from the Synthetic Monitoring page, you jump to a test run in the Test Optimization Explorer. Click **View in Test Optimization** from the details panel of a test run on the Synthetic Monitoring page:

{% image
   source="https://datadog-docs.imgix.net/images/continuous_testing/guide/view-continuous-testing-test-runs-in-test-optimization/continuous_testing_test_run_detail.fbb9d793bbb644a980248a443cb9c164.png?auto=format"
   alt="Synthetics Test Runs details view, highlighting View in Test Optimization button" /%}

## Further Reading{% #further-reading %}

- [Getting Started with Continuous Testing](https://docs.datadoghq.com/getting_started/continuous_testing)
- [Using the Test Optimization Explorer](https://docs.datadoghq.com/tests/explorer/)
- [Working with Flaky Tests](https://docs.datadoghq.com/tests/flaky_tests)
