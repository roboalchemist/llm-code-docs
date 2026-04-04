# Source: https://docs.datadoghq.com/getting_started/test_impact_analysis.md

---
title: Getting Started with Test Impact Analysis
description: >-
  Skip irrelevant tests using code coverage analysis to reduce CI testing time
  while maintaining reliability and performance.
breadcrumbs: Docs > Getting Started > Getting Started with Test Impact Analysis
---

# Getting Started with Test Impact Analysis

{% alert level="danger" %}
This feature was formerly known as Intelligent Test Runner, and some tags still contain "itr".
{% /alert %}

## Overview{% #overview %}

[Test Impact Analysis](https://docs.datadoghq.com/tests/test_impact_analysis/) allows you to skip irrelevant tests unaffected by a code change.

With [Test Optimization](https://docs.datadoghq.com/tests/), development teams can configure Test Impact Analysis for their test services, set branches to exclude (such as the default branch), and define files to be tracked (which triggers full runs of all tests when any tracked file changes).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/itr_test_selection_diagram.c0975b4c67cb895963cca178b4a3307f.png?auto=format"
   alt="A Venn diagram of the components for Test Impact Analysis: tracked files, excluded branches, and skipped tests" /%}
A Venn diagram displaying how Test Impact Analysis defines an excluded test by using tracked files, excluded branches, and passed tests.
Configure and enable Test Impact Analysis for your test services to reduce unnecessary testing time, enhance CI test efficiency, and reduce costs, while maintaining the reliability and performance across your CI environments.

Test Impact Analysis uses [code coverage data](https://docs.datadoghq.com/tests/code_coverage) to determine whether or not tests should be skipped. For more information, see [How Test Impact Analysis Works in Datadog](https://docs.datadoghq.com/tests/test_impact_analysis/how_it_works/).

## Set up Test Impact Analysis{% #set-up-test-impact-analysis %}

To set up Test Impact Analysis, see the following documentation for your programming language:

- [.net](https://docs.datadoghq.com/tests/test_impact_analysis/setup/dotnet/)
- [java](https://docs.datadoghq.com/tests/test_impact_analysis/setup/java/)
- [javascript](https://docs.datadoghq.com/tests/test_impact_analysis/setup/javascript/)
- [python](https://docs.datadoghq.com/tests/test_impact_analysis/setup/python/)
- [swift](https://docs.datadoghq.com/tests/test_impact_analysis/setup/swift/)
- [ruby](https://docs.datadoghq.com/tests/test_impact_analysis/setup/ruby/)
- [go](https://docs.datadoghq.com/tests/test_impact_analysis/setup/go/)

## Enable Test Impact Analysis{% #enable-test-impact-analysis %}

To enable Test Impact Analysis:

1. Navigate to [**Software Delivery** > **Test Optimization** > **Settings**](https://app.datadoghq.com/ci/settings/test-service).
1. On the **Test Services** tab, click **Configure** in the `Test Impact Analysis` column for a service.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/test-impact-analysis-gs-configuration.fde9c54fae1798940e2c5a39ffb623b6.png?auto=format"
   alt="Enable Test Impact Analysis for a test service on the Test Service Settings page" /%}

You must have the `Test Impact Analysis Activation Write` permission. For more information, see the [Datadog Role Permissions documentation](https://docs.datadoghq.com/account_management/rbac/permissions/).

Disabling Test Impact Analysis on critical branches (such as your default branch) ensures comprehensive test coverage, whereas enabling it to run on feature or development branches helps maximize testing efficiency.

## Configure Test Impact Analysis{% #configure-test-impact-analysis %}

You can configure Test Impact Analysis to prevent specific tests from being skipped. These tests are known as *unskippable tests*, and are run regardless of [code coverage data](https://docs.datadoghq.com/tests/code_coverage).

To configure Test Impact Analysis:

1. For the test you want to enable it on, click **Configure**.
1. Click the **Status** toggle to enable Test Impact Analysis.
1. Specify any branches to exclude (typically the default branch of a repository). Test Impact Analysis does not skip tests for these branches.
1. Specify file directories and files to track (for example, `documentation/content/**` or `domains/shopist/apps/api/BUILD.bazel`). Test Impact Analysis runs all CI tests when any of these tracked files change.
1. Click **Save Settings**.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/test-impact-analysis-gs-config.237f2f7c4b6bf439612f921ea3f90405.png?auto=format"
   alt="Enable Test Impact Analysis, provide branches for Test Impact Analysis to exclude, and add files for Test Impact Analysis to track and run tests when any changes happen" /%}

Once you've configured Test Impact Analysis on a test service, execute a test suite run on your default branch. This establishes a baseline for Test Impact Analysis to accurately skip irrelevant tests in future commits.

## Use Test Impact Analysis data{% #use-test-impact-analysis-data %}

Explore the data collected by enabling Test Impact Analysis, such as the time savings achieved by skipping tests, as well as your organization's usage of Test Impact Analysis, to improve your CI efficiency.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/dashboard.c8a69ec224d9c8249b175dd217e7bf32.png?auto=format"
   alt="The out-of-the-box dashboard displaying information about the time saved by tests skipped by Test Impact Analysis, and your organization's usage of Test Impact Analysis" /%}

You can create [dashboards](https://docs.datadoghq.com/dashboards/) to visualize your testing metrics, or use an [out-of-the-box dashboard](https://app.datadoghq.com/dash/integration/30941/ci-visibility---intelligent-test-runner) containing widgets populated with data collected by Test Impact Analysis to help you identify areas of improvement with usage patterns and trends.

## Examine results in the Test Optimization Explorer{% #examine-results-in-the-test-optimization-explorer %}

The [Test Optimization Explorer](https://docs.datadoghq.com/tests/explorer/) allows you to create visualizations and filter test spans using the data collected from Test Optimization and Test Impact Analysis. When Test Impact Analysis is active, it displays the amount of time saved for each test session or commit. The duration bars turn purple to indicate active test skipping.

{% tab title="Session" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Asession) and select `Session` to start filtering your test session span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/itr_sessions.c5e95b0c0f63d19934d3d1c101620f56.png?auto=format"
   alt="Test session results in the Test Optimization Explorer filtered on tests skipped by Test Impact Analysis" /%}

{% /tab %}

{% tab title="Module" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Amodule) and select `Module` to start filtering your test module span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/itr_modules.28b1dbec87d67d934b89a91a9931f343.png?auto=format"
   alt="Test module results in the Test Optimization Explorer filtered on tests skipped by Test Impact Analysis" /%}

{% /tab %}

{% tab title="Suite" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Asuite) and select `Suite` to start filtering your test suite span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/itr_suites.5838a6837372a4e76a31f3fab8586285.png?auto=format"
   alt="Test suite results in the Test Optimization Explorer filtered on tests skipped by Test Impact Analysis" /%}

{% /tab %}

{% tab title="Test" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Atest) and select `Test` to start filtering your test span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/itr_tests.ad58f6ca6d42ce36492b720dadd24390.png?auto=format"
   alt="Test results in the Test Optimization Explorer filtered on tests skipped by Test Impact Analysis" /%}

{% /tab %}

Use the following out-of-the-box Test Impact Analysis [facets](https://docs.datadoghq.com/continuous_integration/explorer/facets/?tab=testruns) to customize the search query:

{% dl %}

{% dt %}
Code Coverage Enabled
{% /dt %}

{% dd %}
Indicates whether code coverage tracking was active during the test session.
{% /dd %}

{% dt %}
Skipped by ITR
{% /dt %}

{% dd %}
Number of tests that were skipped during the session by Test Impact Analysis.
{% /dd %}

{% dt %}
Test Skipping Enabled
{% /dt %}

{% dd %}
Indicates if Test Impact Analysis was enabled for the test session.
{% /dd %}

{% dt %}
Test Skipping Type
{% /dt %}

{% dd %}
The method or criteria used by Test Impact Analysis to determine which tests to skip.
{% /dd %}

{% dt %}
Tests Skipped
{% /dt %}

{% dd %}
The total count of tests that were not executed during the test session, which may include tests that were configured to skip, or were set as manual exclusions.
{% /dd %}

{% dt %}
Time Saved
{% /dt %}

{% dd %}
The length of time saved for the session by Test Impact Analysis usage.
{% /dd %}

{% /dl %}

For example, to filter test session runs that have `Test Skipping Enabled`, you can use `@test.itr.tests_skipping.enabled:true` in the search query.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/intelligent_test_runner/session_run.693abc55e9c85c90fa2e303c5dec044d.png?auto=format"
   alt="A side panel displaying the first test session run where the Test Skipping feature is enabled for Test Impact Analysis" /%}

Then, click on a test session run and see the amount of time saved by Test Impact Analysis in the **Test Session Details** section on the test session side panel.

## Further Reading{% #further-reading %}

- [Streamline your CI testing with Datadog Intelligent Test Runner](https://www.datadoghq.com/blog/streamline-ci-testing-with-datadog-intelligent-test-runner/)
- [Learn about Test Impact Analysis](https://docs.datadoghq.com/test_impact_analysis/)
- [Learn about Code Coverage](https://docs.datadoghq.com/tests/code_coverage/)
