# Source: https://docs.datadoghq.com/tests.md

---
title: Test Optimization in Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Test Optimization in Datadog
source_url: https://docs.datadoghq.com/index.html
---

# Test Optimization in Datadog

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[Test Optimization](https://app.datadoghq.com/ci/test-repositories) provides a test-first view into your CI health by displaying important metrics and results from your tests. It can help you investigate performance problems and test failures that are most relevant to your work, focusing on the code you are responsible for, rather than the pipelines which run your tests.

## Setup{% #setup %}

Select an option to configure Test Optimization in Datadog:

- [.net](https://docs.datadoghq.com/tests/setup/dotnet/)
- [java](https://docs.datadoghq.com/tests/setup/java/)
- [javascript](https://docs.datadoghq.com/tests/setup/javascript/)
- [python](https://docs.datadoghq.com/tests/setup/python/)
- [ruby](https://docs.datadoghq.com/tests/setup/ruby/)
- [swift](https://docs.datadoghq.com/tests/setup/swift/)
- [go](https://docs.datadoghq.com/tests/setup/go/)
- [upload junit tests to datadog](https://docs.datadoghq.com/tests/setup/junit_xml/)

In addition to tests, Test Optimization provides visibility over the whole testing phase of your project.

### Supported features{% #supported-features %}

| .NET                                                                                                                                                                                                                                                                                    | Java/JVMâbased | Javascript | Python           | Ruby | Swift            | Go  | JUnit Xml |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------- | ---------------- | ---- | ---------------- | --- | --------- |
| {% collapsible-section style="margin-bottom:0" %}
  Accurate time/durations results: Microseconds resolution in test start time and duration.
    {% /collapsible-section %}                                                                                                            | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Distributed traces on integration tests: Tests that make calls to external services instrumented with Datadog show the full distributed trace in their test details.
    {% /collapsible-section %}                                 | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Agent-based reporting: Ability to report test information through the Datadog Agent.
    {% /collapsible-section %}                                                                                                                 | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Agentless reporting: Ability to report test information without the Datadog Agent.
    {% /collapsible-section %}                                                                                                                   | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Test suite level visibility: Visibility over the whole testing process, including session, module, suites, and tests.
    {% /collapsible-section %}                                                                                | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Manual API: Ability to programmatically create CI Visibility events for test frameworks that are not supported by Datadog's automatic instrumentation.
    {% /collapsible-section %}                                               | yes            | yes        | yes              | yes  | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Codeowner by test: Automatic detection of the owner of a test file based on the CODEOWNERS file.
    {% /collapsible-section %}                                                                                                     | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes (partially)  |
| {% collapsible-section style="margin-bottom:0" %}
  Source code start/end: Automatic report of the start and end lines of a test.
    {% /collapsible-section %}                                                                                                                        | yes            | yes        | yes (only start) | yes  | yes (only start) | yes | yes       | yes (only start) |
| {% collapsible-section style="margin-bottom:0" %}
  CI and git info: Automatic collection of git and CI environment metadata, such as CI provider, git commit SHA or pipeline URL.
    {% /collapsible-section %}                                                                       | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Git metadata upload: Automatic upload of git tree information used for [Test Impact Analysis](https://docs.datadoghq.com/tests/test_impact_analysis).
    {% /collapsible-section %}                                                | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Test Impact Analysis *: Capability to enable [Test Impact Analysis](https://docs.datadoghq.com/tests/test_impact_analysis), which intelligently skips tests based on code coverage and git metadata.
    {% /collapsible-section %} | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Code coverage support: Ability to report [total code coverage](https://docs.datadoghq.com/tests/code_coverage) metrics.
    {% /collapsible-section %}                                                                              | yes            | yes        | yes              | yes  | yes              | yes | yes       | yes (manual)     |
| {% collapsible-section style="margin-bottom:0" %}
  Benchmark tests support: Automatic detection of performance statistics for benchmark tests.
    {% /collapsible-section %}                                                                                                          | yes            | yes        | yes              | yes  |
| {% collapsible-section style="margin-bottom:0" %}
  Parameterized tests: Automatic detection of parameterized tests.
    {% /collapsible-section %}                                                                                                                                     | yes            | yes        | yes              | yes  | yes              | yes |
| {% collapsible-section style="margin-bottom:0" %}
  Early flake detection *: Automatically [retry new tests](https://docs.datadoghq.com/tests/flaky_test_management/early_flake_detection) to detect flakiness.
    {% /collapsible-section %}                                          | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Auto test retries *: Automatically [retry failed tests](https://docs.datadoghq.com/tests/flaky_test_management/auto_test_retries) up to N times to avoid failing the build due to test flakiness.
    {% /collapsible-section %}    | yes            | yes        | yes              | yes  | yes              | yes | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Failed test replay *: [Access local variable information](https://docs.datadoghq.com/tests/flaky_test_management/auto_test_retries#failed-test-replay) on retried failed tests.
    {% /collapsible-section %}                      | yes            | yes        | yes              |
| {% collapsible-section style="margin-bottom:0" %}
  Selenium RUM integration: Automatically [link browser sessions to test cases](https://docs.datadoghq.com/tests/browser_tests) when testing RUM-instrumented applications.
    {% /collapsible-section %}                            | yes            | yes        | yes              | yes  | yes              |

\* The feature is opt-in, and needs to be enabled on the [**Test Optimization Settings** page](https://app.datadoghq.com/ci/settings/test-optimization).

## Default configurations{% #default-configurations %}

Tests evaluate the behavior of code for a set of given conditions. Some of those conditions are related to the environment where the tests are run, such as the operating system or the runtime used. The same code executed under different sets of conditions can behave differently, so developers usually configure their tests to run in different sets of conditions and validate that the behavior is the expected for all of them. This specific set of conditions is called a *configuration*.

In Test Optimization, a test with multiple configurations is treated as multiple tests with a separate test for each configuration. In the case where one of the configurations fails but the others pass, only that specific test and configuration combination is marked as failed.

For example, suppose you're testing a single commit and you have a Python test that runs against three different Python versions. If the test fails for one of those versions, that specific test is marked as failed, while the other versions are marked as passed. If you retry the tests against the same commit and now the test for all three Python versions pass, the test with the version that previously failed is now marked as both passed and flaky, while the other two versions remain passed, with no flakiness detected.

### Test configuration attributes{% #test-configuration-attributes %}

When you run your tests with Test Optimization, the library detects and reports information about the environment where tests are run as test tags. For example, the operating system name, such as `Windows` or `Linux`, and the architecture of the platform, such as `arm64` or `x86_64`, are added as tags on each test. These values are shown in the commit and on branch overview pages when a test fails or is flaky for a specific configuration but not others.

The following tags are automatically collected to identify test configurations, and some may only apply to specific platforms:

| Tag Name               | Description                                                     |
| ---------------------- | --------------------------------------------------------------- |
| `os.platform`          | Name of the operating system where the tests are run.           |
| `os.family`            | Family of the operating system where the tests are run.         |
| `os.version`           | Version of the operating system where the tests are run.        |
| `os.architecture`      | Architecture of the operating system where the tests are run.   |
| `runtime.name`         | Name of the runtime system for the tests.                       |
| `runtime.version`      | Version of the runtime system.                                  |
| `runtime.vendor`       | Vendor that built the runtime platform where the tests are run. |
| `runtime.architecture` | Architecture of the runtime system for the tests.               |
| `device.model`         | The device model running the tests.                             |
| `device.name`          | Name of the device.                                             |
| `ui.appearance`        | User Interface style.                                           |
| `ui.orientation`       | Orientation the UI is run in.                                   |
| `ui.localization`      | Language of the application.                                    |

### Parameterized test configurations{% #parameterized-test-configurations %}

When you run parameterized tests, the library detects and reports information about the parameters used. Parameters are a part of test configuration, so the same test case executed with different parameters is considered as two different tests in Test Optimization.

If a test parameter is non-deterministic and has a different value every time a test is run, each test execution is considered a new test in Test Optimization. As a consequence, some product features may not work correctly for such tests: history of executions, flakiness detection, Test Impact Analysis, and others.

Some examples of non-deterministic test parameters are:

- current date
- a random value
- a value that depends on the test execution environment (such as an absolute file path or the current username)
- a value that has no deterministic string representation (for example an instance of a Java class whose `toString()` method is not overridden)

Avoid using non-deterministic test parameters. In case this is not possible, some testing frameworks provide a way to specify a deterministic string representation for a non-deterministic parameter (such as overriding parameter display name).

## Custom configurations{% #custom-configurations %}

There are some configurations that cannot be directly identified and reported automatically because they can depend on environment variables, test run arguments, or other approaches that developers use. For those cases, you must provide the configuration details to the library so Test Optimization can properly identify them.

Define these tags as part of the `DD_TAGS` environment variable using the `test.configuration` prefix.

For example, the following test configuration tags identify a test configuration where disk response time is slow and available memory is low:

```bash
DD_TAGS=test.configuration.disk:slow,test.configuration.memory:low
```

All tags with the `test.configuration` prefix are used as configuration tags, in addition to the automatically collected ones.

Note: Nested `test.configuration` tags, such as `test.configuration.cpu.memory`, are not supported.

In order to filter using these configurations tags, [you must create facets for these tags](https://docs.datadoghq.com/continuous_integration/explorer/facets/).

## Enhance your developer workflow{% #enhance-your-developer-workflow %}

- [Enhancing Developer Workflows with Datadog](https://docs.datadoghq.com/tests/developer_workflows/)
- [Learn about Code Coverage](https://docs.datadoghq.com/tests/code_coverage)
- [Instrument Cypress Browser Tests with Browser RUM](https://docs.datadoghq.com/tests/browser_tests)
- [Instrument Swift Tests with RUM](https://docs.datadoghq.com/tests/swift_tests)

## Use CI tests data{% #use-ci-tests-data %}

When Test Visibility is enabled, the following data is collected from your project:

- Test names and durations.
- Predefined environment variables set by CI providers.
- Git commit history including the hash, message, author information, and files changed (without file contents).
- Information from the CODEOWNERS file.

When creating a [dashboard](https://app.datadoghq.com/dashboard/lists) or a [notebook](https://app.datadoghq.com/notebook/list), you can use CI test data in your search query, which updates the visualization widget options. For more information, see the [Dashboards](https://docs.datadoghq.com/dashboards) and [Notebooks documentation](https://docs.datadoghq.com/notebooks).

## Alert on test data{% #alert-on-test-data %}

When you're evaluating failed or flaky tests, or the performance of a CI test, you can export your search query in the [Test Optimization Explorer](https://app.datadoghq.com/ci/test-runs) to a [CI Test monitor](https://docs.datadoghq.com/monitors/types/ci/) by clicking the **Export** button.

## Further reading{% #further-reading %}

- [Check out the latest Software Delivery releases! (App login required)](https://app.datadoghq.com/release-notes?category=Software%20Delivery)
- [Monitor your CI pipelines and tests with Datadog CI Visibility](https://www.datadoghq.com/blog/datadog-ci-visibility/)
- [Troubleshoot end-to-end tests with CI Visibility and RUM](https://www.datadoghq.com/blog/ci-test-visibility-with-rum/)
- [Learn about CI Test Monitors](https://docs.datadoghq.com/monitors/types/ci/)
- [Learn about Flaky Test Management](https://docs.datadoghq.com/tests/flaky_test_management/)
- [Learn how to instrument your browser tests with RUM](https://docs.datadoghq.com/tests/browser_tests/)
- [Learn how to troubleshoot Test Optimization](https://docs.datadoghq.com/tests/troubleshooting/)
- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
