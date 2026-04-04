# Source: https://docs.datadoghq.com/getting_started/test_optimization.md

---
title: Getting Started with Test Optimization
description: >-
  Understand test performance and identify flaky tests, performance regressions,
  and failures across CI environments.
breadcrumbs: Docs > Getting Started > Getting Started with Test Optimization
---

# Getting Started with Test Optimization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[Test Optimization](https://docs.datadoghq.com/tests/) allows you to better understand your test posture, identify commits introducing flaky tests, identify performance regressions, and troubleshoot complex test failures.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/list.633605422ad7664093dbaafb336fe342.png?auto=format"
   alt="List of test services in Test Optimization" /%}

You can visualize the performance of your test runs as traces, where spans represent the execution of different parts of the test.

Test Optimization enables development teams to debug, optimize, and accelerate software testing across CI environments by providing insights about test performance, flakiness, and failures. Test Optimization automatically instruments each test and integrates intelligent test selection using the [Test Impact Analysis](https://docs.datadoghq.com/tests/test_impact_analysis), enhancing test efficiency and reducing redundancy.

With historical test data, teams can understand performance regressions, compare the outcome of tests from feature branches to default branches, and establish performance benchmarks. By using Test Optimization, teams can improve their [developer workflows](https://docs.datadoghq.com/tests/developer_workflows) and maintain quality code output.

## Set up a test service{% #set-up-a-test-service %}

Test Optimization tracks the performance and results of your CI tests, and displays results of the test runs.

To start instrumenting and running tests, see the documentation for one of the following languages.

- [.net](https://docs.datadoghq.com/tests/setup/dotnet/)
- [java](https://docs.datadoghq.com/tests/setup/java/)
- [javascript](https://docs.datadoghq.com/tests/setup/javascript/)
- [python](https://docs.datadoghq.com/tests/setup/python/)
- [ruby](https://docs.datadoghq.com/tests/setup/ruby/)
- [swift](https://docs.datadoghq.com/tests/setup/swift/)
- [go](https://docs.datadoghq.com/tests/setup/go/)
- [upload junit tests to datadog](https://docs.datadoghq.com/tests/setup/junit_xml/)

Test Optimization is compatible with any CI provider and is not limited to those supported by CI Visibility. For more information about supported features, see [Test Optimization](https://docs.datadoghq.com/tests/#supported-features).

## Use CI test data{% #use-ci-test-data %}

Access your tests' metrics (such as executions, duration, distribution of duration, overall success rate, failure rate, and more) to start identifying important trends and patterns using the data collected from your tests across CI pipelines.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/tests_dashboard.c8fca2d19c2f1b72499d3b67edeb6a44.png?auto=format"
   alt="Out-of-the-box Test Optimization dashboard in Datadog" /%}

You can create [dashboards](https://docs.datadoghq.com/dashboards/) for monitoring flaky tests, performance regressions, and test failures occurring within your tests. Alternatively, you can utilize an [out-of-the-box dashboard](https://app.datadoghq.com/dash/integration/30897/ci-visibility---tests-dashboard) containing widgets populated with data collected in Test Optimization to visualize the health and performance of your CI test sessions, modules, suites, and tests.

## Manage flaky tests{% #manage-flaky-tests %}

A [flaky test](https://docs.datadoghq.com/glossary/?product=ci-cd#flaky-test) is a test that exhibits both a passing and failing status across multiple test runs for the same commit. If you commit some code and run it through CI, and a test fails, and you run it through CI again and the same test now passes, that test is unreliable and marked as flaky.

You can access flaky test information in the **Flaky Tests** section of a test run's overview page, or as a column on your list of test services on the [**Test List** page](https://app.datadoghq.com/ci/test-services).

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/commit_flaky_tests.2a2087485396d3534ad99b1f2da2dfed.png?auto=format"
   alt="Flaky tests that can be ignored in the Commits section of a test run" /%}

For each branch, the list shows the number of new flaky tests, the number of commits flaked by the tests, total test time, and the branch's latest commit details.

{% dl %}

{% dt %}
Average duration
{% /dt %}

{% dd %}
The average time the test takes to run.
{% /dd %}

{% dt %}
First flaked and Last flaked
{% /dt %}

{% dd %}
The date and commit SHAs for when the test first and most recently exhibited flaky behavior.
{% /dd %}

{% dt %}
Commits flaked
{% /dt %}

{% dd %}
The number of commits in which the test exhibited flaky behavior.
{% /dd %}

{% dt %}
Failure rate
{% /dt %}

{% dd %}
The percentage of test runs that have failed for this test since it first flaked.
{% /dd %}

{% dt %}
Trend
{% /dt %}

{% dd %}
A visualization that indicates whether a flaky test was fixed or it is still actively flaking.
{% /dd %}

{% /dl %}

Test Optimization displays the following graphs to help you understand your flaky test trends and the impact of your flaky tests in a commit's **Flaky Tests** section:

{% dl %}

{% dt %}
New Flaky Test Runs
{% /dt %}

{% dd %}
How often new flaky tests are being detected.
{% /dd %}

{% dt %}
Known Flaky Test Runs
{% /dt %}

{% dd %}
All of the test failures associated with the flaky tests being tracked. This shows every time a flaky test "flakes".
{% /dd %}

{% /dl %}

To ignore new flaky tests for a commit that you've determined the flaky tests were detected by mistake, click on a test containing a **New Flaky** value with a dropdown option, and click **Ignore flaky tests**. For more information, see [Flaky Test Management](https://docs.datadoghq.com/tests/flaky_test_management/).

## Examine results in the Test Optimization Explorer{% #examine-results-in-the-test-optimization-explorer %}

The Test Optimization Explorer allows you to create visualizations and filter test spans using the data collected from your testing. Each test run is reported as a trace, which includes additional spans generated by the test request.

{% tab title="Session" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Asession) and select `Session` to start filtering your test session span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/session.c6ba9ed4da6b66e05288055c0a2d9db4.png?auto=format"
   alt="Test session results in the Test Optimization Explorer filtered on the Shopist repository" /%}

{% /tab %}

{% tab title="Module" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Amodule) and select `Module` to start filtering your test module span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/module.3daccce2ea34786d23528d04fc6dd01b.png?auto=format"
   alt="Test module results in the Test Optimization Explorer filtered on the Shopist repository" /%}

{% /tab %}

{% tab title="Suite" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Asuite) and select `Suite` to start filtering your test suite span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/suite.7fe7ceed5b94a8b47e13db5bc12a4d1f.png?auto=format"
   alt="Test suite results in the Test Optimization Explorer filtered on the Shopist repository" /%}

{% /tab %}

{% tab title="Test" %}
Navigate to [**Software Delivery** > **Test Optimization** > **Test Runs**](https://app.datadoghq.com/ci/test-runs?query=test_level%3Atest) and select `Test` to start filtering your test span results.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/test.3c5a14456beca980a397a162c1496215.png?auto=format"
   alt="Test results in the Test Optimization Explorer filtered on the Shopist repository" /%}

{% /tab %}

Use [facets](https://docs.datadoghq.com/continuous_integration/explorer/facets/?tab=testruns) to customize the search query and identify changes in time spent on each level of your test run.

Once you click on a test on the **Test List** page, you can see a flame graph or a list of spans on the **Trace** tab.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/failed_test_trace.9da1f0ef7b3a3812413cc475eadcc0d5.png?auto=format"
   alt="A stack trace of a failed test run on the Test List page" /%}

You can identify bottlenecks in your test runs and examine individual levels ranked from the largest to smallest percentage of execution time.

## Add custom measures to tests{% #add-custom-measures-to-tests %}

You can programmatically search and manage test events using the CI Visibility Tests API endpoint. For more information, see [the API documentation](https://docs.datadoghq.com/api/latest/ci-visibility-tests/).

To enhance the data collected from your CI tests, you can programmatically add tags or measures (like memory usage) directly to the spans created during test execution. For more information, see [Add Custom Measures To Your Tests](https://docs.datadoghq.com/tests/guides/add_custom_measures/).

## Create a CI monitor{% #create-a-ci-monitor %}

Alert relevant teams in your organization about test performance regressions when failures occur or new flaky tests occur.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/test_visibility/test_monitor.b163b76fbfce7352d5f049423c3975c2.png?auto=format"
   alt="A CI test monitor that triggers alerts when the amount of test failures exceeds one failure" /%}

To set up a monitor that alerts when the amount of test failures exceeds a threshold of 1 failure:

1. Navigate to [**Monitors** > **New Monitor**](https://app.datadoghq.com/monitors/create) and select **CI**.
1. Select a common monitor type for CI tests to get started, for example: `New Flaky Test` to trigger alerts when new flaky tests are added to your code base, `Test Failures` to trigger alerts for test failures, or `Test Performance` to trigger alerts for test performance regressions, or customize your own search query. In this example, select the `Branch (@git.branch)` facet to filter your test runs on the `main` branch.
1. In the `Evaluate the query over the` section, select last 15 minutes.
1. Set the alert conditions to trigger when the evaluated value is above the threshold, and specify values for the alert or warning thresholds, such as `Alert threshold > 1`.
1. Define the monitor notification.
1. Set permissions for the monitor.
1. Click **Create**.

For more information, see the [CI Monitor documentation](https://docs.datadoghq.com/monitors/types/ci/?tab=tests#track-new-flaky-tests).

## Further Reading{% #further-reading %}

- [Troubleshoot end-to-end tests with CI Test Visibility and RUM](https://www.datadoghq.com/blog/ci-test-visibility-with-rum/)
- [Learn about Test Optimization](https://docs.datadoghq.com/tests/)
- [Learn about Flaky Test Management](https://docs.datadoghq.com/tests/flaky_test_management/)
- [Learn about enhancing developer workflows in Datadog](https://docs.datadoghq.com/tests/developer_workflows)
